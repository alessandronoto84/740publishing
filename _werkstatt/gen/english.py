# Baut site/en/index.html (English Editions). Aufruf: python3 gen/english.py $S
# Cover liegen als 600 px breite JPG/WebP unter covers/en/<key>.{jpg,webp}.
# GPLAY: sobald ein Buch bei Google Play Books live ist, den geprüften Link eintragen -> Kaufbutton statt "Coming soon".
import html, json, sys, os
S=sys.argv[1]
BASE='https://alessandronoto84.github.io/740publishing/'
CSSV='1793200000'
e=html.escape
N='Novels'; F='Nonfiction'
# (key, Titel, Untertitel, Autor, Bereich, Kurzbeschreibung)
# Quellen: Beschreibung.txt / EPUB-Metadaten in outputs/en/<KUERZEL>/; bei KARMA, LUCK, ORDER, BAD LUCK und
# The Game Never Stops gibt es keine Beschreibung.txt -> Übersetzung des deutschen Webseitentexts (catalog.BLURB).
EN=[
 ('karma','KARMA','A Novel','Konstanze Frey',N,'Primary school teacher Maggie Hollweg wants to make the world a little better, but her good deeds keep ending in chaos. Her suspicion: her karma works in reverse. A humorous small-town novel full of comedy and heart.'),
 ('luck','LUCK','A Novel','Konstanze Frey',N,'Manni Ackermann works at the lost-and-found office of a small town. As inexplicable coincidences pile up, everyone starts calling him the “Lucky Man”. A warm-hearted novel with gentle humor about kindness and the small encounters that change a life.'),
 ('order','ORDER','A Novel','Konstanze Frey',N,'Since the death of his wife, order has been Gerd Bollmann’s only reliable companion. But suddenly things and people stop keeping to what was agreed. A wise, warm-hearted novel about control, loss and letting go.'),
 ('bad-luck','BAD LUCK','A Novel','Konstanze Frey',N,'Rosi Diekmann has a plan for everything: spare keys, an emergency kit, smoke detectors. Until someone enters her life who sees possibilities wherever she sees risks. A warm-hearted novel about fear, control and life as a risk.'),
 ('manuscript','The Manuscript','','Evan J. Moore',N,'One rainy evening in Berlin, magazine editor Adrian Kessler finds a black notebook on the street. Soon afterward, handwritten pages describe his life with a precision that should be impossible. A quiet, hypnotic literary mystery about grief, memory, and what remains when the line between a story and reality begins to disappear.'),
 ('black-water','Black Water','','Juna Morel',N,'Lena Vargas is a ghostwriter in Vienna. When the reclusive investor Nikolaj Voss hires her to write his memoir, she travels to his estate in the Austrian mountains, where a small black lake lies among the firs. An atmospheric dark romance about control and trust, about what we hide and what we let someone see.'),
 ('game','The Game Never Stops','How Incentives Shape Societies — and Who Writes the Rules','Friedhelm Westerkamp',F,'Why do politicians, corporations and the media act the way they do? Because people respond to incentives, not ideals. Friedhelm Westerkamp combines game theory, psychology and economics to show how the rules of the game shape entire societies, and who writes those rules.'),
 ('beauty','Why Beauty Is Power','The Modern Art of Feminine Radiance and Impact','Katharina Bruns',F,'An honest look at beauty as a social force: how attractiveness shapes dating, friendships and the workplace, and which mechanisms run in the background that nobody names openly. Every chapter ends with a practical exercise.'),
 ('spirit','The Big Book of Spiritual Practice','','Leonard Kramer',F,'A workbook and reference guide for people who are searching but don’t want a doctrine. It keeps three things strictly apart: what research supports, what traditions teach, and what people report from their own experience. With 56 guided exercises and a 90-day integration program.'),
 ('psych','Psychology in Everyday Life','','Friedhelm Westerkamp',F,'A complete tour of the science of the human mind, written for curious readers rather than specialists. Forty chapters, from the brain, perception and memory to emotions, stress, relationships, sleep, work and aging, with an honest account of how the famous studies have held up.'),
 ('drugs','DRUGS','History, Effects, Addiction and Policy','Alessandro Noto',F,'A sober, fact-based account of psychoactive substances and their place in human history, from a thirteen-thousand-year-old brew to today’s synthetic opioids. With a reference lexicon of substances. Abridged English edition.'),
 ('body-cult','Body Cult','Scars, Ink and Identity','Samuel Dorn',F,'Long before people wrote, they began to change their skin. Body Cult follows this impulse across more than 100,000 years, from Stone Age body paint and the tattoos of Ötzi the Iceman to Polynesian tattooing, Japanese irezumi and modern body modification.'),
 ('astrology','ASTROLOGY','The Big Book of Zodiac Signs, Planets, Houses, and Your Personal Birth Chart','Vivian Dahl',F,'Your zodiac sign is only the first word of a much richer language. This book takes you from the basics to reading your own birth chart, step by step and without dogma, and is honest about what astrology is and isn’t.'),
 ('ai','Artificial Intelligence','Understand It. Use It. Shape It.','Friedhelm Westerkamp',F,'A clear, practical guide for beginners, professionals and businesses: what AI assistants actually do, how to write prompts that get results, and where AI saves real time and where it doesn’t. Revised and updated English edition.'),
 ('digital-exhaustion','Digital Exhaustion','How Constant Digital Stimulation Drains and Empties Us—and What We Can Really Do About It','Friedhelm Westerkamp',F,'Why do you feel exhausted after a day in which you did almost nothing? Friedhelm Westerkamp shows how the attention economy works, what it does to concentration, sleep and relationships, and how to win back attention and rest. Revised and updated English edition.'),
]
GPLAY={k:'' for k,*_ in EN}  # z. B. GPLAY['karma']='https://play.google.com/store/books/details?id=...'

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
  <section class="sec wrap enintro">
    <p class="eyebrow">740 Publishing</p>
    <h1 class="sech">English Editions</h1>
    <hr class="rule">
    <p class="enlead">Selected titles from our German program, now translated into English. All {len(EN)} e-books have been submitted to Google Play Books and will be available there soon.</p>
  </section>
  <div class="catalog enlist"><div class="sec wrap">
{secs.replace('<section class="catsec"><h2 class="sech">Novels','<section class="catsec" id="novels"><h2 class="sech">Novels').replace('<section class="catsec"><h2 class="sech">Nonfiction','<section class="catsec" id="nonfiction"><h2 class="sech">Nonfiction')}  </div></div>
</main>
<footer class="foot"><div class="wrap"><img src="../logo-small.png" alt="740 Publishing" width="70" height="54"><address>740 Publishing · Burgstraße 12 · 49808 Lingen (Ems) · Germany<br>740publishingverlag@gmail.com</address><nav><a href="../impressum.html" hreflang="de">Legal notice</a><a href="../datenschutz.html" hreflang="de">Privacy</a></nav></div></footer>
</body>
</html>
'''
os.makedirs(f'{S}/site/en',exist_ok=True)
open(f'{S}/site/en/index.html','w').write(page)
print('english',len(EN))
