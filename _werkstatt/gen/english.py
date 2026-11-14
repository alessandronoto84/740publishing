# Baut site/en/index.html (English Editions). Aufruf: python3 gen/english.py $S
# Cover liegen als 600 px breite JPG/WebP unter covers/en/<key>.{jpg,webp}.
# GPLAY: sobald ein Buch bei Google Play Books live ist, den geprüften Link eintragen -> Kaufbutton statt "Coming soon".
import html, json, sys, os
S=sys.argv[1]
BASE='https://740publishing.de/'
CSSV='1794300000'
e=html.escape
from english_data import *
def card(k,t,sub,a,sec,d):
    u=GPLAY.get(k)
    act=(f'<div class="buys"><a class="buy sm" href="{e(u)}" target="_blank" rel="noopener"><span class="fmt">E-book</span><span class="shop">Google Play Books</span></a></div>' if u
         else '<p class="ensoon">Coming soon on Google Play Books</p>')
    return (f'<article class="mini enbook" id="{k}"><picture><source srcset="../covers/en/{k}.webp" type="image/webp">'
            f'<img class="cover" src="../covers/en/{k}.jpg" alt="Cover of “{e(t)}” by {e(a)}" width="100" height="150" loading="lazy"></picture>'
            f'<div class="info"><h3>{e(t)}</h3>{f"<p class=\"ensub\">{e(sub)}</p>" if sub else ""}<p class="author">{e(a)}</p>'
            f'<p class="mblurb">{e(d)}</p>{act}</div></article>')
secs=''
for sec in (N,F):
    items=[card(*b) for b in EN if b[4]==sec]
    secs+=f'<section class="catsec"><h2 class="sech">{sec} <span>{len(items)}</span></h2><div class="minigrid">{"".join(items)}</div></section>\n'
ld={"@context":"https://schema.org","@graph":[{"@type":"Book","name":t,**({"alternativeHeadline":sub} if sub else {}),"author":{"@type":"Person","name":a},"inLanguage":"en","bookFormat":"https://schema.org/EBook","image":BASE+f"covers/en/{k}.jpg","publisher":{"@type":"Organization","name":"740 Publishing"}} for k,t,sub,a,sec,d in EN]}
import picks as _pk
_PB=[{'k':k,'t':t,'a':a,'g':sec,'cov':f'../covers/en/{k}.jpg','href':f'#{k}','d':d} for k,t,sub,a,sec,d in EN]
_PBK={b['k']:b for b in _PB}
TICKER=_pk.ticker([_PBK[k] for k in EN_FEATURED if k in _PBK],'Featured','English Editions','Featured English Editions')
PICKS=_pk.picks(_PB,{'lang':'en','aria':'Book recommendations','day':'Our pick of the day','rnd':'Discover a random book','again':'↻ Another one','more':'View this book →'})
page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>English Editions – 740 Publishing</title>
<meta name="description" content="English e-book editions from 740 Publishing: novels and nonfiction by Konstanze Frey, Friedhelm Westerkamp, Evan J. Moore and more. Coming soon on Google Play Books.">
<link rel="canonical" href="{BASE}en/">
<link rel="alternate" hreflang="en" href="{BASE}en/">
<link rel="alternate" hreflang="de" href="{BASE}">
<meta name="theme-color" content="#0b0a08">
<meta property="og:type" content="website">
<meta property="og:title" content="English Editions – 740 Publishing">
<meta property="og:description" content="English e-book editions from 740 Publishing. Coming soon on Google Play Books.">
<meta property="og:image" content="{BASE}logo.png">
<meta property="og:url" content="{BASE}en/">
<meta property="og:locale" content="en_US">
<link rel="icon" href="../logo-small.png">
<link rel="stylesheet" href="../style.css?v={CSSV}">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False).replace("</","<\\/")}</script>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="../"><img src="../logo-small.png" alt="740 Publishing" width="52" height="40"><span>740 Publishing</span></a><nav><a href="#novels">Novels</a><a href="#nonfiction">Nonfiction</a><a href="../" hreflang="de" lang="de" title="Deutsche Startseite">DE</a></nav></div></header>
<main>
  {TICKER}
  <section class="sec wrap enintro">
    <p class="eyebrow">740 Publishing</p>
    <h1 class="sech">English Editions</h1>
    <hr class="rule">
    <p class="enlead">Selected titles from our German program, now translated into English. All {len(EN)} e-books have been submitted to Google Play Books and will be available there soon.</p>
  </section>
  {PICKS}
  <div class="catalog enlist"><div class="sec wrap">
{secs.replace('<section class="catsec"><h2 class="sech">Novels','<section class="catsec" id="novels"><h2 class="sech">Novels').replace('<section class="catsec"><h2 class="sech">Nonfiction','<section class="catsec" id="nonfiction"><h2 class="sech">Nonfiction')}  </div></div>
</main>
<footer class="foot"><div class="wrap"><img src="../logo-small.png" alt="740 Publishing" width="70" height="54"><address>740 Publishing · Burgstraße 12 · 49808 Lingen (Ems) · Germany<br>740publishingverlag@gmail.com</address><nav><a href="../impressum.html" hreflang="de">Legal notice</a><a href="../datenschutz.html" hreflang="de">Privacy</a></nav></div></footer>
<script src="../entdecken.js?v=1" defer></script>
<script src="../chatbot.js?v=3" defer></script>
</body>
</html>
'''
os.makedirs(f'{S}/site/en',exist_ok=True)
open(f'{S}/site/en/index.html','w').write(page)
print('english',len(EN))
