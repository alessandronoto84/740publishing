# Baut index.html (Startseite). Aufruf: python3 gen/build.py $S  (S/gen = dieser Ordner, S/site = Repo)
import html, json, sys, re, datetime
S=sys.argv[1]
# Bücher mit Buchtrailer (Bereich „Buchtrailer“). Kauf-Links kommen zentral aus catalog.editions(), die Linkliste hier ist nur Altbestand.
books=[
 ('astrologie','Astrologie','Das große Buch über Sternzeichen, Planeten, Häuser und dein persönliches Horoskop','Vivian Dahl','Spiritualität',None,'Du bist mehr als dein Sternzeichen. Dein Geburtshoroskop ist ein Fingerabdruck des Himmels. Dieses Buch zeigt Schritt für Schritt, wie Sternzeichen, Planeten und Häuser zusammenspielen, verständlich und ohne Vorwissen.',
  [('E-Book','epubli','https://www.epubli.com/shop/astrologie-9783565752201'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565752270'),('Hardcover','Amazon','https://www.amazon.de/dp/3565752289')],'9783565752270'),
 ('freizeitpark','Wir fahren in den Freizeitpark','Roman','Tobias Kranz','Roman',None,'Kühltasche gepackt, Motor läuft, Sabina hat einen Plan für jede Minute. Oma Ingrid sieht das gelassen. Dann ein seltsames Winken, ein Grollen, ein Atemzug unter dem Boden. Was als Familienkomödie beginnt, wird zum Ausflug, den niemand vergisst.',
  [('E-Book','epubli','https://www.epubli.com/shop/wir-fahren-in-den-freizeitpark-9783565739790'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565739770')],'9783565739776'),
 ('thailand','Die verborgene Seite von Thailand','30 Orte abseits der Touristenpfade','Mika Solberg','Reiseführer','Die verborgene Seite der Welt','Echte Dörfer, echte Natur und ein Land, das man erst dort wirklich versteht. 30 Orte, an denen sonst kaum jemand landet, mit Geheimtipps und Routen für respektvolles Reisen.',
  [('E-Book','epubli','https://www.epubli.com/shop/die-verborgene-seite-von-thailand-9783565585663'),('Taschenbuch','Amazon','https://www.amazon.de/dp/356558565X'),('Taschenbuch','Hugendubel','https://www.hugendubel.de/de/buch_kartoniert/mika_solberg-die_verborgene_seite_von_thailand-54175286-produkt-details.html')],'9783565585656'),
 ('kaffee','Kaffee','Vom Ritual der Sufi-Mönche zur globalen Börsenware','Sandro Noto','Kulinarik','Die verborgene Seite der Kulinarik','Kaffee hat Klöster durchwacht, Religionen herausgefordert und Revolutionen begleitet. Seine Geschichte erzählt von Kolonialismus, Ausbeutung und globaler Macht, bis in die Börsen von heute.',
  [('E-Book','epubli','https://www.epubli.com/shop/kaffee-9783565737932'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565737891'),('Hardcover','Amazon','https://www.amazon.de/dp/3565737905')],'9783565737895'),
 ('rap','Deutsch-Rap','Die komplette Geschichte einer deutschen Revolution','Sandro Urban','Musik',None,'Deutschrap begann auf Straßen, in Jugendzentren und zwischen Plattenbauten. Aus Heidelberg wurde ein Aufbruch, aus Stuttgart eine Bewegung, Berlin machte daraus eine Ansage. Von den ersten Freestyles bis zur Streaming-Ära.',
  [('E-Book','epubli','https://www.epubli.com/shop/deutsch-rap-9783565491421'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565491418')],'9783565491414'),
 ('schoenheit','Warum Schönheit Macht ist','Die moderne Kunst weiblicher Ausstrahlung und Wirkung','Katharina Bruns','Persönlichkeit',None,'Die Frau, die alle Blicke auf sich zieht, ist nicht unbedingt die Schönste. Sie ist die, die aufgehört hat, um Aufmerksamkeit zu kämpfen. Ein Buch über Haltung, Präsenz und den Blick auf sich selbst.',
  [('E-Book','epubli','https://www.epubli.com/shop/warum-schoenheit-macht-ist-9783565501397'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565501367')],'9783565501366'),
 ('kifft','Deutschland kifft','Die Geschichte einer verbotenen Kultur','Sandro Urban','Sachbuch',None,'Einst Nutzpflanze, dann verboten, heute teilweise legalisiert. Die Kulturgeschichte von Cannabis in Deutschland zwischen Schwarzmarkt, Social Clubs und Medizinalcannabis, und was die Teil-Legalisierung wirklich bedeutet.',
  [('E-Book','epubli','https://www.epubli.com/shop/deutschland-kifft-9783565739585'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565740418'),('Hardcover','Amazon','https://www.amazon.de/dp/3565740426')],'9783565740413'),
 ('drogen','Drogen','Das umfassende Standardwerk','Alessandro Noto','Sachbuch',None,'Von uralten Ritualen bis zum globalen Drogenkrieg: über 200 Substanzen mit ihren Wirkungen, Mechanismen und Geschichten. Geschichte, Wirkung, Politik und Wissenschaft psychoaktiver Substanzen.',
  [('E-Book','epubli','https://www.epubli.com/shop/drogen-das-umfassende-standardwerk-9783565525911'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565526653'),('Hardcover','Amazon','https://www.amazon.de/dp/3565526637')],'9783565526659'),
]
sys.path.insert(0,f'{S}/gen')
import catalog as C
from catalog import CAT, BLURB, SERIES_OF, editions, RELEASES, NEU_ANZAHL
from render import badges, buttons, isbnfmt
e=html.escape
def slug(t):
    t=t.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss'); return re.sub(r'[^a-z0-9]+','-',t).strip('-')
def cv(cov): return f'covers/{cov[3:]}.jpg' if cov.startswith('../') else f'covers/cat/{cov}.jpg'
CD={x[0]:x for x in CAT}

# ---- Buchtrailer (8 Bücher mit Video) ----
NKEY={'freizeitpark':'k-freizeitpark','thailand':'k-thailand','kaffee':'k-kaffee','rap':'k-rap','schoenheit':'k-schoenheit','kifft':'k-kifft','drogen':'k-drogen','astrologie':'k-astrologie'}
cards=[]
for k,t,sub,a,g,series,blurb,links,isbn in books:
    ck=NKEY.get(k,k)
    ser=f'<p class="series">Reihe: {e(SERIES_OF[ck][0])} · Band {SERIES_OF[ck][1]}</p>' if ck in SERIES_OF else ''
    btns=f'<button class="buy trl" type="button" data-video="trailer/{k}.mp4" data-poster="trailer/{k}.jpg" data-title="{e(t)}"><span class="fmt">▶ Trailer</span><span class="shop">ansehen</span></button>'+buttons(ck)
    cards.append(f'''      <article class="book" id="{k}" data-genre="{g}">
        <button class="covbtn" type="button" data-video="trailer/{k}.mp4" data-poster="trailer/{k}.jpg" data-title="{e(t)}" aria-label="Trailer zu „{e(t)}“ abspielen"><img class="cover" src="covers/cov_{k}.jpg" alt="Cover von „{e(t)}“" width="150" height="225" loading="lazy" decoding="async"><span class="playic" aria-hidden="true"></span><span class="playlbl">Trailer</span></button>
        <div class="info">
          <p class="meta"><span class="genre">{g}</span><span>{e(a)}</span></p>
          <h3><a href="buch/{slug(CD[ck][1])}.html">{e(t)}</a></h3>
          <p class="sub">{e(sub)}</p>
          {ser}
          <p class="blurb">{e(blurb)}</p>
          {badges(ck)}
          <div class="buys">{btns}</div>
        </div>
      </article>''')

# ---- Neu erschienen: nach Erscheinungsdatum, neueste zuerst ----
# Quellen: catalog.RELEASES (von Hand gepflegt) + Erscheinungsdatum aus dem epubli-Shop (linkstatus.json, vom linkcheck).
ev={}
for d,k,f,i in RELEASES: ev[(k,f)]=(d,k,f,i,'werkstatt')
for x in CAT:
    k=x[0]
    for f,sh,u,i in C.candidate_links(k):
        v=C._LS.get(u) or {}
        if v.get('ok') and v.get('date') and (k,f) not in ev:
            dd,mm,yy=v['date'].split('.'); ev[(k,f)]=(f'{yy}-{mm}-{dd}',k,f,i,'epubli')
byk={}
for d,k,f,i,src in ev.values():
    if k not in CD: continue
    byk.setdefault(k,[]).append((d,f))
newest=sorted(((max(d for d,_ in v),k) for k,v in byk.items()),reverse=True)[:NEU_ANZAHL]
MON=['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
def dlabel(d): y,m,dd=d.split('-'); return f'{int(dd)}. {MON[int(m)-1]} {y}'
def fjoin(L): return L[0] if len(L)==1 else ', '.join(L[:-1])+' und '+L[-1]
def short(s,n=170): return s if len(s)<=n else s[:n].rsplit(' ',1)[0].rstrip(',:;.')+' …'
groups=[]
for d,k in newest:
    if not groups or groups[-1][0]!=d: groups.append((d,[]))
    groups[-1][1].append(k)
neu=[]
for gi,(d,ks) in enumerate(groups):
    items=[]
    for k in ks:
        _,t,a,c,eb,pr,pt,cov=CD[k]
        fs=[f for dd,f in byk[k] if dd==d]; fs=[f for f in C.FMT_ORDER if f in fs]
        eds={x['f']:x for x in editions(k)}
        alln=set(fs)>=set(eds)   # alle Formate neu -> ganz neues Buch
        what=('Neuer Titel' if alln and len(fs)>1 else 'Neu als '+fjoin(fs))
        img=f'<a class="nb-cov" href="buch/{slug(t)}.html" tabindex="-1" aria-hidden="true"><img class="cover" src="{cv(cov)}" alt="" width="120" height="180" loading="lazy" decoding="async"></a>'
        if gi==0:
            items.append(f'''<article class="nb"><div class="nb-in">{img}<div class="info"><p class="nb-what">{e(what)}</p><h3><a href="buch/{slug(t)}.html">{e(t)}</a></h3><p class="author">{e(a)}</p>{('<p class="mblurb">'+e(short(BLURB[k]))+'</p>') if k in BLURB else ''}{badges(k)}<div class="buys">{buttons(k,sm=True,one=True)}</div></div></div></article>''')
        else:   # ältere Tage kompakt: Cover, Titel, was neu ist, Status
            nf=[x for x in eds.values() if x['f'] in fs]
            st=' · '.join(f"{x['f']}{(' '+x['price']+' €') if x['price'] else ''}: {'bald verfügbar' if x['soon'] else 'erhältlich'}" for x in nf)
            items.append(f'''<a class="nbc" href="buch/{slug(t)}.html"><img src="{cv(cov)}" alt="" width="56" height="84" loading="lazy" decoding="async"><span class="nbc-t"><b>{e(t)}</b><small>{e(a)}</small><em>{e(what)}</em><i>{e(st)}</i></span></a>''')
    cls='nbgrid' if gi==0 else 'nbcgrid'
    neu.append(f'<div class="nbgroup{" first" if gi==0 else ""}"><h3 class="nbdate"><time datetime="{d}">{dlabel(d)}</time></h3><div class="{cls}">{"".join(items)}</div></div>')
NEU='\n'.join(neu)

# ---- JSON-LD: alle Bücher mit geprüften Angeboten ----
BASE='https://740publishing.de/'
ld=[]
for k,t,a,c,eb,pr,pt,cov in CAT:
    offers=[]
    for ed in editions(k):
        for sh,u in ed['links']:
            o={"@type":"Offer","url":u,"seller":{"@type":"Organization","name":sh},"availability":"https://schema.org/InStock"}
            if ed['price']: o.update({"price":ed['price'].replace(',','.'),"priceCurrency":"EUR"})
            offers.append(o)
    b={"@type":"Book","name":t,"author":{"@type":"Person","name":a},"inLanguage":"de","image":BASE+cv(cov),"url":f'{BASE}buch/{slug(t)}.html',"publisher":{"@type":"Organization","name":"740 Publishing"}}
    i=pr or eb
    if i: b["isbn"]=i
    if offers: b["offers"]=offers
    ld.append(b)

# ---- Gesamtkatalog ----
TRAILER={'bier':'bier','fussball':'fussball','k-freizeitpark':'freizeitpark','k-rap':'rap','k-kifft':'kifft','k-drogen':'drogen','k-kaffee':'kaffee','k-schoenheit':'schoenheit','k-astrologie':'astrologie','k-thailand':'thailand'}
order=['Romane','Sachbuch & Ratgeber','Reiseführer']
secs=[]
for cat in order:
    items=[]
    for k,t,a,c,eb,pr,pt,cov in CAT:
        if c!=cat: continue
        src=cv(cov)
        img=(f'<button class="covbtn" type="button" data-video="trailer/{TRAILER[k]}.mp4" data-poster="trailer/{TRAILER[k]}.jpg" data-title="{e(t)}" aria-label="Trailer zu „{e(t)}“ abspielen"><img class="cover" src="{src}" alt="Cover von „{e(t)}“" width="100" height="150" loading="lazy" decoding="async"><span class="playic" aria-hidden="true"></span></button>' if k in TRAILER else f'<img class="cover" src="{src}" alt="Cover von „{e(t)}“" width="100" height="150" loading="lazy" decoding="async">') if cov else f'<div class="cover blank" aria-hidden="true"><span>{e(t)}</span></div>'
        items.append(f'<article class="mini" id="{k}">{img}<div class="info"><h3><a href="buch/{slug(t)}.html">{e(t)}</a></h3><p class="author">{e(a)}</p>{badges(k)}{("<p class=\"mblurb\">"+e(BLURB[k])+"</p>") if k in BLURB else ""}<p class="more"><a href="buch/{slug(t)}.html">Mehr zum Buch</a></p><div class="buys">{buttons(k,sm=True)}</div></div></article>')
    secs.append(f'<section class="catsec" data-cat="{cat}"><h2 class="sech">{cat} <span>{len(items)}</span></h2><div class="minigrid">{"".join(items)}</div></section>')
catchips='<button class="chip cchip" aria-pressed="true" data-c="alle">Alle</button>'+''.join(f'<button class="chip cchip" aria-pressed="false" data-c="{c}">{c}</button>' for c in order)
import random as _r
_names=open(f'{S}/gen/wall.txt').read().split()
_r.Random(7).shuffle(_names)
_cols=[]
for _i in range(7):
    _c=[_names[(_i*6+_j)%len(_names)] for _j in range(6)]
    _imgs=''.join(f'<img src="covers/wall/{n}.jpg" alt="" width="200" height="300" decoding="async">' for n in _c+_c)
    _cols.append(f'<div class="col c{_i}">{_imgs}</div>')
WALL=''.join(_cols)
SERIES=[('Die verborgene Seite der Welt','Reiseführer von Mika Solberg: 30 Orte abseits der Touristenpfade pro Land.',['k-thailand','vietnam','japan','china','mexiko','kolumbien','ecuador','peru']),
 ('Die verborgene Seite der Kulinarik','Die Kulturgeschichte dessen, was wir täglich genießen.',['k-kaffee','bier']),
 ('KARMA · GLÜCK · ORDNUNG · PECH','Die Romanreihe von Konstanze Frey: warmherzige, humorvolle Kleinstadtromane.',['karma','glueck','ordnung','pech']),
 ('Projekt-Reihe von Victor Cross','Körper, Geist und Identität: Praxisbücher für die eigene Transformation.',['uebermensch','powerfrau','optimierte']),
 ('Vivian Dahl','Sachbücher über Astrologie, Schamanismus und spirituelle Traditionen.',['k-astrologie','schamanismus'])]
_ser=[]
for _n,_d,_ks in SERIES:
    _it=''.join(f'<a class="sbk" href="buch/{slug(CD[k][1])}.html"><img src="{cv(CD[k][7])}" alt="Cover von „{e(CD[k][1])}“" width="120" height="180" loading="lazy" decoding="async"><span>{e(CD[k][1].replace("Die verborgene Seite von ",""))}</span></a>' for k in _ks)
    _ser.append(f'<div class="series"><div class="shead"><h3>{e(_n)}</h3><p>{e(_d)} <b>{len(_ks)} Bände</b></p></div><div class="srow">{_it}</div></div>')
# ---- Laufband + Tipp des Tages + Zufallsbuch (gen/picks.py, Browser-Logik in entdecken.js) ----
from catalog import BELIEBT
import picks as _pk
_PB=[{'k':k,'t':t,'a':a,'g':c,'cov':cv(cov),'href':f'buch/{slug(t)}.html','d':BLURB.get(k,'')} for k,t,a,c,eb,pr,pt,cov in CAT if cov]
_PBK={b['k']:b for b in _PB}
TICKER=_pk.ticker([_PBK[k] for k in BELIEBT if k in _PBK],'Beliebt','bei unseren Lesern','Beliebt bei unseren Lesern')
PICKS=_pk.picks(_PB,{'lang':'de','aria':'Buchtipps','day':'Unser Tipp des Tages','rnd':'Zufällig entdeckt','again':'↻ Noch ein Buch','more':'Mehr zum Buch →'})
tpl=open(f'{S}/gen/index_tpl.html').read()
out=(tpl.replace('{{CARDS}}','\n'.join(cards)).replace('{{NEU}}',NEU).replace('{{LD}}',json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False).replace('</','<\\/'))
        .replace('{{TICKER}}',TICKER).replace('{{PICKS}}',PICKS).replace('{{SERIES}}','\n'.join(_ser)).replace('{{WALL}}',WALL)
        .replace('{{CATALOG}}','\n'.join(secs)).replace('{{CATCHIPS}}',catchips).replace('{{COUNT}}',str(len(CAT))))
assert '{{' not in out, re.findall(r'\{\{[A-Z]+\}\}',out)
open(f'{S}/site/index.html','w').write(out)
print('index ok',len(out),'· neu:',', '.join(f'{d}:{"/".join(ks)}' for d,ks in groups))
