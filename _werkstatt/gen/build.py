import html, json, sys
S=sys.argv[1]
books=[
 ('astrologie','Astrologie','Das große Buch über Sternzeichen, Planeten, Häuser und dein persönliches Horoskop','Vivian Dahl','Spiritualität',None,'Du bist mehr als dein Sternzeichen. Dein Geburtshoroskop ist ein Fingerabdruck des Himmels. Dieses Buch zeigt Schritt für Schritt, wie Sternzeichen, Planeten und Häuser zusammenspielen, verständlich und ohne Vorwissen.',
  [('E-Book','epubli','https://www.epubli.com/shop/astrologie-9783565752201'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565752270'),('Hardcover','Amazon','https://www.amazon.de/dp/3565752289')],'9783565752270'),
 ('freizeitpark','Wir fahren in den Freizeitpark','Roman','Tobias Kranz','Roman',None,'Kühltasche gepackt, Motor läuft, Sabina hat einen Plan für jede Minute. Oma Ingrid sieht das gelassen. Dann ein seltsames Winken, ein Grollen, ein Atemzug unter dem Boden. Was als Familienkomödie beginnt, wird zum Ausflug, den niemand vergisst.',
  [('E-Book','epubli','https://www.epubli.com/shop/wir-fahren-in-den-freizeitpark-9783565739790'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565739770')],'9783565739776'),
 ('thailand','Die verborgene Seite von Thailand','30 Orte abseits der Touristenpfade','Mika Solberg','Reiseführer','Die verborgene Seite der Welt','Echte Dörfer, echte Natur und ein Land, das man erst dort wirklich versteht. 30 Orte, an denen sonst kaum jemand landet, mit Geheimtipps, Routen und Insiderwissen für respektvolles Reisen.',
  [('E-Book','epubli','https://www.epubli.com/shop/die-verborgene-seite-von-thailand-9783565585663'),('Taschenbuch','Amazon','https://www.amazon.de/dp/356558565X'),('Taschenbuch','Hugendubel','https://www.hugendubel.de/de/buch_kartoniert/mika_solberg-die_verborgene_seite_von_thailand-54175286-produkt-details.html')],'9783565585656'),
 ('kaffee','Kaffee','Vom Ritual der Sufi-Mönche zur globalen Börsenware','Sandro Noto','Kulinarik','Die verborgene Seite der Kulinarik','Kaffee hat Klöster durchwacht, Religionen herausgefordert und Revolutionen begleitet. Seine Geschichte erzählt von Kolonialismus, Ausbeutung und globaler Macht, bis in die Börsen von heute.',
  [('E-Book','epubli','https://www.epubli.com/shop/kaffee-9783565737932'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565737891'),('Hardcover','Amazon','https://www.amazon.de/dp/3565737905')],'9783565737895'),
 ('rap','Deutsch-Rap','Die komplette Geschichte einer deutschen Revolution','Sandro Urban','Musik',None,'Deutschrap begann auf Straßen, in Jugendzentren und zwischen Plattenbauten. Aus Heidelberg wurde ein Aufbruch, aus Stuttgart eine Bewegung, Berlin machte daraus eine Ansage. Von den ersten Freestyles bis zur Streaming-Ära.',
  [('E-Book','epubli','https://www.epubli.com/shop/deutsch-rap-9783565491421'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565491418')],'9783565491414'),
 ('schoenheit','Warum Schönheit Macht ist','Die moderne Kunst weiblicher Ausstrahlung und Wirkung','Katharina Bruns','Persönlichkeit',None,'Die Frau, die alle Blicke auf sich zieht, ist nicht unbedingt die Schönste. Sie ist die, die aufgehört hat, um Aufmerksamkeit zu kämpfen. Ein Buch über Haltung, Präsenz und den Blick auf sich selbst.',
  [('E-Book','epubli','https://www.epubli.com/shop/warum-schoenheit-macht-ist-9783565501397'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565501367')],'9783565501366'),
 ('kifft','Deutschland kifft','Die Geschichte einer verbotenen Kultur','Sandro Urban','Sachbuch',None,'Einst Nutzpflanze, dann verboten, heute teilweise legalisiert. Die Kulturgeschichte von Cannabis in Deutschland zwischen Schwarzmarkt, Social Clubs und Medizinalcannabis, und was die Teil-Legalisierung wirklich bedeutet.',
  [('E-Book','epubli','https://www.epubli.com/shop/deutschland-kifft-9783565739585'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565740418'),('Hardcover','Amazon','https://www.amazon.de/dp/3565740426')],'9783565740413'),
 ('drogen','Drogen','Das umfassende Standardwerk','Alessandro Noto','Sachbuch',None,'Von uralten Ritualen bis zum globalen Drogenkrieg: über 200 Substanzen mit ihren Wirkungen, Mechanismen und Geschichten. Geschichte, Wirkung, Politik und Kultur psychoaktiver Substanzen, wissenschaftlich fundiert.',
  [('E-Book','epubli','https://www.epubli.com/shop/drogen-das-umfassende-standardwerk-9783565525911'),('Taschenbuch','Amazon','https://www.amazon.de/dp/3565526653'),('Hardcover','Amazon','https://www.amazon.de/dp/3565526637')],'9783565526659'),
]
def isbnfmt(i): return f'{i[:3]}-{i[3]}-{i[4:10]}-{i[10:12]}-{i[12]}'
genres=[]
for b in books:
    if b[4] not in genres: genres.append(b[4])
cards=[];ld=[]
for k,t,sub,a,g,series,blurb,links,isbn in books:
    btns=f'<button class="buy trl" type="button" data-video="trailer/{k}.mp4" data-poster="trailer/{k}.jpg" data-title="{html.escape(t)}"><span class="fmt">▶ Trailer</span><span class="shop">ansehen</span></button>'+''.join(f'<a class="buy" href="{u}" target="_blank" rel="noopener"><span class="fmt">{f}</span><span class="shop">{s}</span></a>' for f,s,u in links)
    ser=f'<p class="series">Reihe: {html.escape(series)}</p>' if series else ''
    cards.append(f'''      <article class="book" id="{k}" data-genre="{g}">
        <button class="covbtn" type="button" data-video="trailer/{k}.mp4" data-poster="trailer/{k}.jpg" data-title="{html.escape(t)}" aria-label="Trailer zu „{html.escape(t)}“ abspielen"><img class="cover" src="covers/cov_{k}.jpg" alt="Cover von „{html.escape(t)}“" width="150" height="225" loading="lazy"><span class="playic" aria-hidden="true"></span><span class="playlbl">Trailer</span></button>
        <div class="info">
          <p class="meta"><span class="genre">{g}</span><span>{a}</span></p>
          <h2>{html.escape(t)}</h2>
          <p class="sub">{html.escape(sub)}</p>
          {ser}
          <p class="blurb">{html.escape(blurb)}</p>
          <div class="buys">{btns}</div>
          <p class="isbn">ISBN {isbnfmt(isbn)}</p>
        </div>
      </article>''')
    ld.append({"@type":"Book","name":t,"alternateName":sub,"author":{"@type":"Person","name":a},"isbn":isbn,"genre":g,"inLanguage":"de","image":f"covers/cov_{k}.jpg","publisher":{"@type":"Organization","name":"740 Publishing"},"offers":[{"@type":"Offer","url":u,"seller":{"@type":"Organization","name":s}} for f,s,u in links]})
chips='<button class="chip" aria-pressed="true" data-g="alle">Alle</button>'+''.join(f'<button class="chip" aria-pressed="false" data-g="{g}">{g}</button>' for g in genres)
tpl=open(f'{S}/gen/index_tpl.html').read()
out=tpl.replace('{{CARDS}}','\n'.join(cards)).replace('{{CHIPS}}',chips).replace('{{LD}}',json.dumps({"@context":"https://schema.org","@graph":ld},ensure_ascii=False))
open(f'{S}/site/index.html','w').write(out)
print('ok',len(out))

# ---- Gesamtkatalog ----
sys.path.insert(0,f'{S}/gen')
from catalog import CAT, EXTRA, SLUG, BLURB
TRAILER={'bier':'bier','k-freizeitpark':'freizeitpark','k-rap':'rap','k-kifft':'kifft','k-drogen':'drogen','k-kaffee':'kaffee','k-schoenheit':'schoenheit','k-astrologie':'astrologie','k-thailand':'thailand'}
def slug(t):
    t=t.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    import re; return re.sub(r'[^a-z0-9]+','-',t).strip('-')
def isbn10(s):
    c=s[3:12]; r=(11-sum((10-i)*int(d) for i,d in enumerate(c))%11)%11
    return c+('X' if r==10 else str(r))
order=['Romane','Sachbuch & Ratgeber','Reiseführer']
secs=[]
for cat in order:
    items=[]
    for k,t,a,c,eb,pr,pt,cov in CAT:
        if c!=cat: continue
        if k in EXTRA: links=EXTRA[k]
        else:
            links=[]
            if eb: links.append(('E-Book','epubli',f'https://www.epubli.com/shop/{SLUG.get(k,slug(t))}-{eb}'))
            if pr: links.append((pt,'Amazon',f'https://www.amazon.de/dp/{isbn10(pr)}'))
            if pr and not eb: links.append((pt,'epubli',f'https://www.epubli.com/shop/{slug(t)}-{pr}'))
        btns=''.join(f'<a class="buy sm" href="{u}" target="_blank" rel="noopener"><span class="fmt">{f}</span><span class="shop">{s}</span></a>' for f,s,u in links)
        img=(f'<button class="covbtn" type="button" data-video="trailer/{TRAILER[k]}.mp4" data-poster="trailer/{TRAILER[k]}.jpg" data-title="{html.escape(t)}" aria-label="Trailer zu „{html.escape(t)}“ abspielen"><img class="cover" src="covers/cat/{cov}.jpg" alt="Cover von „{html.escape(t)}“" width="100" height="150" loading="lazy"><span class="playic" aria-hidden="true"></span></button>' if k in TRAILER else f'<img class="cover" src="covers/cat/{cov}.jpg" alt="Cover von „{html.escape(t)}“" width="100" height="150" loading="lazy">') if cov else f'<div class="cover blank" aria-hidden="true"><span>{html.escape(t)}</span></div>'
        items.append(f'<article class="mini" id="{k}">{img}<div class="info"><h3><a href="buch/{slug(t)}.html">{html.escape(t)}</a></h3><p class="author">{html.escape(a)}</p>{("<p class=\"mblurb\">"+html.escape(BLURB[k])+"</p>") if k in BLURB else ""}<p class="more"><a href="buch/{slug(t)}.html">Mehr zum Buch →</a></p><div class="buys">{btns}</div></div></article>')
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
 ('Konstanze Frey','Warmherzige, humorvolle Kleinstadtromane.',['karma','glueck','pech','ordnung','katastrophe']),
 ('Projekt-Reihe von Victor Cross','Körper, Geist und Identität: Praxisbücher für die eigene Transformation.',['uebermensch','powerfrau','optimierte']),
 ('Vivian Dahl','Sachbücher über Astrologie, Schamanismus und spirituelle Traditionen.',['k-astrologie','schamanismus'])]
_C={x[0]:x for x in CAT}
def _cv(cov): return f'covers/{cov[3:]}.jpg' if cov.startswith('../') else f'covers/cat/{cov}.jpg'
_ser=[]
for _n,_d,_ks in SERIES:
    _it=''.join(f'<a class="sbk" href="buch/{slug(_C[k][1])}.html"><img src="{_cv(_C[k][7])}" alt="Cover von „{html.escape(_C[k][1])}“" width="120" height="180" loading="lazy"><span>{html.escape(_C[k][1].replace("Die verborgene Seite von ",""))}</span></a>' for k in _ks)
    _ser.append(f'<div class="series"><div class="shead"><h3>{html.escape(_n)}</h3><p>{html.escape(_d)} <b>{len(_ks)} Bände</b></p></div><div class="srow">{_it}</div></div>')
out=open(f'{S}/site/index.html').read().replace('{{SERIES}}','\n'.join(_ser)).replace('{{WALL}}',WALL).replace('{{CATALOG}}','\n'.join(secs)).replace('{{CATCHIPS}}',catchips).replace('{{COUNT}}',str(len(CAT)))
open(f'{S}/site/index.html','w').write(out)
print('catalog',len(CAT))
