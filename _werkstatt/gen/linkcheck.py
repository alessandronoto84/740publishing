# Prüft alle Kauf-Links der Webseite und schreibt das Ergebnis nach gen/linkstatus.json.
# Die Webseite zeigt einen Kauf-Button NUR, wenn der Link hier als ok (funktioniert) eingetragen ist.
# Alles andere erscheint als „Bald verfügbar“ (ohne Link).
#
# Aufruf (im Ordner _werkstatt):
#   python3 gen/linkcheck.py                 -> alle Links per HTTP prüfen (braucht Internet, z. B. auf dem PC)
#   python3 gen/linkcheck.py --list          -> nur die Liste aller Links ausgeben (links.json), nichts prüfen
#   python3 gen/linkcheck.py --import X.json -> Ergebnisse aus einer Browser-Prüfung übernehmen (Format wie linkstatus.json)
#   python3 gen/linkcheck.py --report        -> Übersicht: was ok ist, was fehlt
#
# Regeln für „ok“:
#   epubli:     HTTP 200 UND der Buchtitel steht im <title> der Seite (epubli liefert bei falschem Slug 404)
#   Amazon:     HTTP 200 UND die Seite ist kein „Seite nicht gefunden“ / Captcha UND enthält den Titel
#   Hugendubel: HTTP 200 UND der Titel steht auf der Seite
#   Google Play (english.py, GPLAY): HTTP 200 UND der Titel steht auf der Seite
# Netzwerkfehler (z. B. Sandbox ohne Zugang) ändern nichts: der alte Eintrag bleibt, der Link gilt dann als „nicht geprüft“.
import json, os, sys, re, time, datetime, html, unicodedata, urllib.request, urllib.error
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
STATUS=os.path.join(HERE,'linkstatus.json')
import catalog as C

def norm(s):
    s=unicodedata.normalize('NFD',html.unescape(s)).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def all_links():
    out=[]
    for x in C.CAT:
        k,t=x[0],x[1]
        for f,sh,u,i in C.candidate_links(k): out.append({'k':k,'t':t,'f':f,'shop':sh,'url':u,'isbn':i})
    try:
        import importlib.util
        spec=importlib.util.spec_from_file_location('en_data',os.path.join(HERE,'english_data.py')); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k,t,*_ in m.EN:
            u=m.GPLAY.get(k)
            if u: out.append({'k':'en:'+k,'t':t,'f':'E-book','shop':'Google Play','url':u,'isbn':''})
    except FileNotFoundError: pass
    return out

def load():
    try: return json.load(open(STATUS))
    except Exception: return {}

def save(st):
    json.dump(dict(sorted(st.items())),open(STATUS,'w'),ensure_ascii=False,indent=1)

def check(l):
    req=urllib.request.Request(l['url'],headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36','Accept-Language':'de-DE,de;q=0.9'})
    try:
        with urllib.request.urlopen(req,timeout=25) as r: code=r.status; body=r.read(800000).decode('utf-8','ignore')
    except urllib.error.HTTPError as e: code=e.code; body=''
    except Exception as e: return None   # nicht erreichbar -> nicht prüfbar
    title=(re.search(r'<title[^>]*>(.*?)</title>',body,re.S|re.I) or [None,''])[1]
    want=norm(l['t'].split('–')[0].split('…')[0])[:40]
    ok=code==200
    if ok and l['shop']=='epubli': ok=want in norm(title)
    elif ok and l['shop']=='Amazon': ok=('captcha' not in body.lower()) and ('nicht gefunden' not in norm(title)) and want in norm(body)
    elif ok: ok=want in norm(body)
    res={'ok':ok,'code':code,'shop':l['shop'],'checked':datetime.date.today().isoformat(),'title':html.unescape(title.strip())[:120]}
    if l['shop']=='epubli' and ok:
        m=re.search(r'Erscheinungsdatum:\s*([\d.]+)',body); p=re.search(r'(\d+,\d\d)\s*(?:&nbsp;)?€\s*inkl',body)
        if m: res['date']=m.group(1)
        if p: res['price']=p.group(1)
        res['isbn']=l['isbn']
    return res

def main(a):
    st=load()
    if '--list' in a:
        L=all_links(); json.dump(L,open(os.path.join(HERE,'links.json'),'w'),ensure_ascii=False,indent=1); print(len(L),'Links -> gen/links.json'); return
    if '--import' in a:
        src=json.load(open(a[a.index('--import')+1])); n=0
        for u,v in src.items(): st[u]={**st.get(u,{}),**v}; n+=1
        save(st); print(n,'Ergebnisse übernommen'); return
    if '--report' in a:
        L=all_links(); bad=[l for l in L if not st.get(l['url'],{}).get('ok')]
        print(f"{len(L)-len(bad)} von {len(L)} Links ok. Nicht ok / nicht geprüft:")
        for l in bad: v=st.get(l['url']); print(f"  {l['t']} · {l['f']} · {l['shop']}: {('HTTP '+str(v.get('code'))) if v else 'nicht geprüft'}  {l['url']}")
        return
    L=all_links(); unreach=0
    for i,l in enumerate(L):
        r=check(l)
        if r is None: unreach+=1; continue
        st[l['url']]={**st.get(l['url'],{}),**r}
        time.sleep(0.7)
    save(st)
    bad=[l for l in L if not st.get(l['url'],{}).get('ok')]
    print(f"geprüft: {len(L)-unreach}, nicht erreichbar: {unreach}, nicht ok: {len(bad)} -> gen/linkstatus.json")
    if unreach==len(L): print('Hinweis: kein Zugriff auf die Shops (Sandbox?). Prüfung im Browser machen und mit --import übernehmen (siehe README).')

if __name__=='__main__': main(sys.argv[1:])
