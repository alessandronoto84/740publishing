import html, json, sys, os, re, datetime
S=sys.argv[1]; sys.path.insert(0,f'{S}/gen')
from catalog import CAT, EXTRA, SLUG, BLURB, new_links, new_isbns, SERIES_OF
from seo import SEO
BASE='https://alessandronoto84.github.io/740publishing/'
TRAILER={'bier':'bier','k-freizeitpark':'freizeitpark','k-rap':'rap','k-kifft':'kifft','k-drogen':'drogen','k-kaffee':'kaffee','k-schoenheit':'schoenheit','k-astrologie':'astrologie','k-thailand':'thailand'}
EXTRA_LINKS={'k-kifft':[('Hardcover','Amazon','https://www.amazon.de/dp/3565740426')],'k-astrologie':[('Hardcover','Amazon','https://www.amazon.de/dp/3565752289')],'k-kaffee':[('Hardcover','Amazon','https://www.amazon.de/dp/3565737905')],'k-drogen':[('Hardcover','Amazon','https://www.amazon.de/dp/3565526637')]}
GENRE={'Romane':'Roman','Sachbuch & Ratgeber':'Sachbuch','Reiseführer':'Reiseführer'}
def slug(t):
    t=t.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss'); return re.sub(r'[^a-z0-9]+','-',t).strip('-')
def isbn10(s):
    c=s[3:12]; r=(11-sum((10-i)*int(d) for i,d in enumerate(c))%11)%11; return c+('X' if r==10 else str(r))
def isbnfmt(i): return f'{i[:3]}-{i[3]}-{i[4:10]}-{i[10:12]}-{i[12]}'
def links_of(k,t,eb,pr,pt):
    if k in EXTRA: return EXTRA[k]+new_links(k)
    L=[]
    if eb: L.append(('E-Book','epubli',f'https://www.epubli.com/shop/{SLUG.get(k,slug(t))}-{eb}'))
    if pr: L.append((pt,'Amazon',f'https://www.amazon.de/dp/{isbn10(pr)}'))
    if pr and not eb: L.append((pt,'epubli',f'https://www.epubli.com/shop/{slug(t)}-{pr}'))
    return L+EXTRA_LINKS.get(k,[])+new_links(k)
def cover_of(k,cov): return f'covers/{cov[3:]}.jpg' if cov.startswith('../') else f'covers/cat/{cov}.jpg'
e=html.escape
books=[]
for k,t,a,c,eb,pr,pt,cov in CAT:
    books.append(dict(k=k,t=t,a=a,c=c,eb=eb,pr=pr,pt=pt,img=cover_of(k,cov),s=slug(t),links=links_of(k,t,eb,pr,pt),b=BLURB.get(k,'')))
os.makedirs(f'{S}/site/buch',exist_ok=True)
HEAD='''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0b0a08">
<meta property="og:type" content="book">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{img}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../logo-small.png">
<link rel="stylesheet" href="../style.css?v=1793200000">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="../"><img src="../logo-small.png" alt="740 Publishing" width="52" height="40"><span>740 Publishing</span></a><nav><a href="../#neu">Neu</a><a href="../#reihen">Reihen</a><a href="../#katalog">Alle Bücher</a><a href="../#verlag">Verlag</a><a href="../en/" hreflang="en" lang="en" title="English Editions">EN</a></nav></div></header>
'''
FOOT='''<footer class="foot"><div class="wrap"><img src="../logo-small.png" alt="740 Publishing" width="70" height="54"><address>740 Publishing · Burgstraße 12 · 49808 Lingen (Ems)<br>740publishingverlag@gmail.com</address><nav><a href="../impressum.html">Impressum</a><a href="../datenschutz.html">Datenschutz</a></nav></div></footer>
'''
PLAYER='''<dialog class="player" id="player" aria-label="Buchtrailer"><div class="pl-head"><span class="pl-title" id="pl-title"></span><button class="pl-close" type="button" id="pl-close" aria-label="Schließen">✕</button></div><video id="pl-video" controls playsinline preload="none"></video></dialog>
<script>(function(){var d=document.getElementById('player'),v=document.getElementById('pl-video'),t=document.getElementById('pl-title');function c(){try{v.pause()}catch(e){}v.removeAttribute('src');v.load();if(d.open)d.close()}document.querySelectorAll('[data-video]').forEach(function(b){b.addEventListener('click',function(){v.poster=b.getAttribute('data-poster');v.src=b.getAttribute('data-video');t.textContent=b.getAttribute('data-title');if(d.showModal)d.showModal();else d.setAttribute('open','');var p=v.play();if(p&&p.catch)p.catch(function(){})})});document.getElementById('pl-close').addEventListener('click',c);d.addEventListener('click',function(e){if(e.target===d)c()});d.addEventListener('cancel',function(e){e.preventDefault();c()})})();</script>
'''
def fjoin(f): return f[0] if len(f)==1 else ', '.join(f[:-1])+' & '+f[-1]
def trunc(s,n=155):
    return s if len(s)<=n else s[:n-1].rsplit(' ',1)[0].rstrip(',:;')+'…'
for b in books:
    url=f'{BASE}buch/{b["s"]}.html'; img=BASE+b['img']; g=GENRE[b['c']]
    fmts=[]; [fmts.append(f) for f,_,_ in b['links'] if f not in fmts]
    kw,fw,inh=SEO.get(b['k'],(None,None,None))
    desc=trunc(f'„{b["t"]}“ von {b["a"]}{" – "+kw if kw else ""}. {b["b"]}' if b['b'] else f'„{b["t"]}“ von {b["a"]} bei 740 Publishing. Jetzt als {fjoin(fmts)} kaufen.')
    title=f'{b["t"]}: {kw} – {b["a"]} | 740 Publishing' if kw else f'{b["t"]} – {b["a"]} | {g} kaufen | 740 Publishing'
    isbn=b['pr'] or b['eb']
    ld={"@context":"https://schema.org","@graph":[
      {"@type":"Book","@id":url+"#book","name":b['t'],"url":url,"image":img,"description":b['b'] or None,"author":{"@type":"Person","name":b['a']},"publisher":{"@type":"Organization","name":"740 Publishing","url":BASE},"inLanguage":"de","genre":g,
       "workExample":[{"@type":"Book","isbn":i,"bookFormat":"https://schema.org/"+("EBook" if fm=='E-Book' else "Hardcover" if fm=='Hardcover' else "Paperback")} for i,fm in ((b['eb'],'E-Book'),(b['pr'],b['pt']),*new_isbns(b['k'])) if i],
       **({"isPartOf":{"@type":"BookSeries","name":SERIES_OF[b['k']][0]},"position":SERIES_OF[b['k']][1]} if b['k'] in SERIES_OF else {}),
       "offers":[{"@type":"Offer","url":u,"availability":"https://schema.org/InStock","seller":{"@type":"Organization","name":s}} for f,s,u in b['links']]},
      {"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"740 Publishing","item":BASE},{"@type":"ListItem","position":2,"name":b['c'],"item":BASE+"#katalog"},{"@type":"ListItem","position":3,"name":b['t'],"item":url}]}]}
    ld["@graph"][0]={k:v for k,v in ld["@graph"][0].items() if v is not None}
    btns=''.join(f'<a class="buy" href="{u}" target="_blank" rel="noopener"><span class="fmt">{f}</span><span class="shop">bei {s} kaufen</span></a>' for f,s,u in b['links'])
    tr=TRAILER.get(b['k'])
    trbtn=f'<button class="buy trl" type="button" data-video="../trailer/{tr}.mp4" data-poster="../trailer/{tr}.jpg" data-title="{e(b["t"])}"><span class="fmt">▶ Trailer</span><span class="shop">ansehen</span></button>' if tr else ''
    isbns=' · '.join(f'{lab}: ISBN {isbnfmt(i)}' for i,lab in ((b['eb'],'E-Book'),(b['pr'],b['pt']),*new_isbns(b['k'])) if i)
    ser=SERIES_OF.get(b['k'])
    same=[x for x in books if x is not b and x['a']==b['a'] and x['t']!=b['t']]
    more=same[:4] if same else []
    more+= [x for x in books if x is not b and x['c']==b['c'] and x not in more and x['t']!=b['t']][:4-len(more)]
    rel=''.join(f'<a class="relb" href="{x["s"]}.html"><img src="../{x["img"]}" alt="Cover von „{e(x["t"])}“" width="90" height="135" loading="lazy"><span>{e(x["t"])}</span><small>{e(x["a"])}</small></a>' for x in more)
    body=f'''<main class="wrap bookpage">
<nav class="crumbs" aria-label="Brotkrumen"><a href="../">Start</a> › <a href="../#katalog">{e(b["c"])}</a> › <span>{e(b["t"])}</span></nav>
<article class="bp">
  <div class="bp-cover"><img src="../{b["img"]}" alt="Cover von „{e(b["t"])}“ von {e(b["a"])}" width="300" height="450"></div>
  <div class="bp-info">
    <p class="eyebrow">{e(g)}</p>
    <h1>{e(b["t"])}</h1>
    {f'<p class="bp-kw">{e(kw)}</p>' if kw else ''}
    <p class="bp-author">von {e(b["a"])}</p>
    {f'<p class="bp-series">Reihe: {e(ser[0])} · Band {ser[1]}</p>' if ser else ''}
    <hr class="rule">
    {f'<p class="bp-blurb">{e(b["b"])}</p>' if b['b'] else ''}
    <p class="bp-avail">Jetzt erhältlich als {e(fjoin(fmts))}</p>
    <div class="buys">{trbtn}{btns}</div>
    <p class="isbn">{isbns}</p>
  </div>
</article>
{f'<section class="bp-more"><div><h2>Für wen ist dieses Buch?</h2><ul>'+''.join(f'<li>{e(x)}</li>' for x in fw)+'</ul></div><div><h2>Das erwartet dich</h2><ul>'+''.join(f'<li>{e(x)}</li>' for x in inh)+'</ul></div></section>' if fw else ''}
{f'<section class="bp-rel"><h2 class="sech">Das könnte dich auch interessieren</h2><div class="relgrid">{rel}</div></section>' if rel else ''}
<p class="bp-back"><a href="../#katalog">← Alle Bücher von 740 Publishing</a></p>
</main>
'''
    page=HEAD.format(title=e(title),desc=e(desc),url=url,ogt=e(f'{b["t"]} – {b["a"]}'),img=img,ld=json.dumps(ld,ensure_ascii=False).replace('</','<\\/'))+body+(PLAYER if tr else '')+FOOT+'</body>\n</html>\n'
    open(f'{S}/site/buch/{b["s"]}.html','w').write(page)
today=datetime.date.today().isoformat()
urls=[BASE,BASE+'en/']+[f'{BASE}buch/{b["s"]}.html' for b in books]
open(f'{S}/site/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls)+'</urlset>\n')
open(f'{S}/site/robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
print(len(books),'Seiten')
