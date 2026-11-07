# Wissensbasis für den Chat-Assistenten (chatbot.js) aus den fertigen Seiten erzeugen.
# Aufruf nach build.py, pages.py und english.py:  python3 gen/chatbot_kb.py $S
# Liest nur, was auf der Webseite steht (Buchseiten, Startseite, English Editions, Impressum),
# und schreibt $S/site/chatbot-wissen.js (setzt window.ChatbotWissen).
import glob, html, json, os, re, sys

S = sys.argv[1]
SITE = f'{S}/site'


def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()


def one(pat, s, flags=re.S):
    m = re.search(pat, s, flags)
    return txt(m.group(1)) if m else ''


# ---------- Bücher aus den Buchseiten ----------
books = []
for f in sorted(glob.glob(f'{SITE}/buch/*.html')):
    s = open(f, encoding='utf-8').read()
    info = s[s.find('<article class="bp">'):s.find('</article>')]
    cr = re.search(r'<nav class="crumbs".*?</nav>', s, re.S)
    crumbs = re.findall(r'<a href="[^"]*">([^<]+)</a>', cr.group(0) if cr else '')
    cat = html.unescape(crumbs[1]) if len(crumbs) > 1 else ''
    fmts, shops = [], []
    for fm, shop in re.findall(r'<a class="buy"[^>]*><span class="fmt">([^<]+)</span><span class="shop">([^<]+)</span></a>', info):
        fm = html.unescape(fm)
        if fm not in fmts:
            fmts.append(fm)
        sh = re.sub(r'^bei | kaufen$', '', html.unescape(shop))
        if sh not in shops:
            shops.append(sh)
    pend = [html.unescape(x) for x in re.findall(r'<span class="buy pend"[^>]*><span class="fmt">([^<]+)</span>', info)]
    b = {
        't': one(r'<h1>(.*?)</h1>', info),
        'sub': one(r'<p class="bp-kw">(.*?)</p>', info),
        'a': re.sub(r'^von ', '', one(r'<p class="bp-author">(.*?)</p>', info)),
        'g': one(r'<p class="eyebrow">(.*?)</p>', info),
        'c': cat,
        'd': one(r'<p class="bp-blurb">(.*?)</p>', info),
        'f': fmts + [f'{p} (erscheint in Kürze)' for p in pend if p not in fmts],
        'shops': shops,
        'u': 'buch/' + os.path.basename(f),
    }
    ser = one(r'<p class="bp-series">(.*?)</p>', info)
    if ser:
        b['r'] = ser.replace('Reihe: ', '')
    if b['t']:
        books.append(b)

# ---------- Startseite ----------
idx = open(f'{SITE}/index.html', encoding='utf-8').read()
neu_sec = re.search(r'<section class="sec wrap" id="neu">(.*?)</section>', idx, re.S)
neu_titles = [txt(t) for t in re.findall(r'<article class="book"[^>]*>.*?<h2>(.*?)</h2>', neu_sec.group(1) if neu_sec else '', re.S)]
by_title = {b['t']: b for b in books}
neu_urls = [by_title[t]['u'] for t in neu_titles if t in by_title]
series = [(txt(n), txt(d)) for n, d in re.findall(r'<div class="series"><div class="shead"><h3>(.*?)</h3><p>(.*?)</p>', idx, re.S)]
about_p = [txt(p) for p in re.findall(r'<p[^>]*>(.*?)</p>', re.search(r'<section class="sec wrap about" id="verlag">(.*?)</section>', idx, re.S).group(1), re.S)]
about_p = [p for p in about_p if len(p) > 60]
avail = next((p for p in about_p if 'erhältlich' in p), '')
avail = next((x.strip() + '.' for x in re.split(r'(?<=\.)\s', avail) if 'erhältlich' in x), avail)
avail = avail.rstrip('.') + '.'
_m = re.search(r'mailto:([\w.+-]+@[\w-]+\.[a-z]+)', idx)
mail = _m.group(1) if _m else ''
social = []
for u, lab in [('instagram.com', 'Instagram'), ('tiktok.com', 'TikTok'), ('linktr.ee', 'Linktree')]:
    m = re.search(r'href="(https://[^"]*' + re.escape(u) + r'[^"]*)"', idx)
    if m:
        social.append({'t': lab, 'h': m.group(1)})
addr = re.sub(r'^740 Publishing\s*·\s*', '', one(r'<address>(.*?)</address>', idx).replace(mail, '').strip(' ·'))

# ---------- Impressum ----------
imp = txt(open(f'{SITE}/impressum.html', encoding='utf-8').read().split('<main', 1)[-1].split('</main>')[0])
_o = re.search(r'Inhaber: (.+?) Burgstraße', imp)
owner = _o.group(1) if _o else ''

# ---------- English Editions ----------
en = open(f'{SITE}/en/index.html', encoding='utf-8').read()
en_main = en[en.find('<main'):]
en_titles = [txt(t) for t in re.findall(r'<article class="mini enbook"[^>]*>.*?<h3[^>]*>(.*?)</h3>', en_main, re.S)]
soon = len(re.findall(r'Coming soon on Google Play Books', en_main))
en_count = len(en_titles)

# ---------- Kategorien ----------
cats = [html.unescape(c) for c in re.findall(r'<section class="catsec" data-cat="([^"]+)">', idx)]
for b in books:
    if b['c'] and b['c'] not in cats:
        cats.append(b['c'])
count = {c: sum(1 for b in books if b['c'] == c) for c in cats}
KAT_KW = {
    'Romane': ['roman', 'romane', 'belletristik', 'geschichten', 'fiction'],
    'Sachbuch & Ratgeber': ['sachbuch', 'sachbuecher', 'ratgeber', 'sachbuechern'],
    'Reiseführer': ['reisefuehrer', 'reisebuch', 'reisebuecher', 'reisen', 'reise'],
}
kategorien = {c: {'c': c, 'k': KAT_KW.get(c, [c.lower()])} for c in cats}
authors = []
for b in books:
    if b['a'] not in authors:
        authors.append(b['a'])

contact_links = ([{'t': 'E-Mail schreiben', 'h': f'mailto:{mail}'}] if mail else []) + [{'t': 'Impressum', 'h': 'impressum.html'}]

faq = []
def F(id, q, a, k, links=None, nxt=None, b=None):
    e = {'id': id, 'q': q, 'a': a, 'k': k}
    if links: e['links'] = links
    if nxt: e['next'] = nxt
    if b: e['b'] = b
    faq.append(e)

F('programm', 'Welche Bücher gibt es?',
  f'Im Programm sind {len(books)} Titel:\n' + '\n'.join(f'- {c}: {count[c]}' for c in cats) +
  '\nFrag mich nach einem Titel, einer Autorin, einem Autor oder einem Thema, zum Beispiel „Bücher über Kaffee“ oder „Reiseführer Japan“.',
  ['welche bücher', 'bücher', 'buch', 'programm', 'katalog', 'sortiment', 'alle bücher', 'titel', 'angebot', 'gesamtkatalog', 'übersicht', 'liste'],
  [{'t': 'Gesamtkatalog', 'h': 'index.html#katalog'}], cats + ['Neuerscheinungen'])
if neu_urls:
    F('neu', 'Was ist neu?', 'Das sind die aktuellen Neuerscheinungen:',
      ['neu', 'neuerscheinung', 'neuerscheinungen', 'neuheiten', 'aktuell', 'neuste', 'neueste', 'rampenlicht', 'trailer'],
      [{'t': 'Neuerscheinungen ansehen', 'h': 'index.html#neu'}], ['Wie bestelle ich?', 'Welche Bücher gibt es?'], neu_urls[:4])
if series:
    F('reihen', 'Welche Reihen gibt es?', 'Diese Reihen gibt es bei 740 Publishing:\n' + '\n'.join(f'- {n}: {d}' for n, d in series),
      ['reihe', 'reihen', 'serie', 'serien', 'band', 'baende', 'fortsetzung', 'teil'],
      [{'t': 'Unsere Reihen', 'h': 'index.html#reihen'}], ['Reiseführer', 'Welche Bücher gibt es?'])
F('bestellen', 'Wie bestelle ich?',
  avail + '\nAuf jeder Buchseite findest du die Kauf-Buttons für die verfügbaren Formate, zum Beispiel „bei epubli kaufen“ oder „bei Amazon kaufen“, und die ISBN. Bei manchen Ausgaben steht „erscheint in Kürze“, die gibt es noch nicht im Handel.',
  ['bestellen', 'bestellung', 'kaufen', 'kauf', 'erhältlich', 'bekommen', 'kriegen', 'epubli', 'amazon', 'buchhandel', 'buchhandlung', 'hugendubel', 'shop', 'lieferung', 'versand', 'isbn', 'wo kaufen', 'wie bestelle'],
  [{'t': 'Zum Katalog', 'h': 'index.html#katalog'}], ['Gibt es E-Books?', 'Was kostet ein Buch?', 'Kontakt'])
F('formate', 'Gibt es E-Books und gedruckte Bücher?',
  avail + '\nWelche Formate es für ein bestimmtes Buch gibt (E-Book, Taschenbuch, Hardcover), steht auf der jeweiligen Buchseite. Nenn mir einfach den Titel.',
  ['ebook', 'e book', 'e-book', 'kindle', 'epub', 'taschenbuch', 'hardcover', 'gebunden', 'print', 'gedruckt', 'format', 'formate', 'digital', 'softcover'],
  None, ['Wie bestelle ich?', 'Welche Bücher gibt es?'])
F('preis', 'Was kostet ein Buch?',
  'Preise stehen nicht auf dieser Webseite. Den aktuellen Preis siehst du beim Shop, zu dem die Kauf-Buttons auf der Buchseite führen (zum Beispiel epubli oder Amazon).',
  ['preis', 'preise', 'kosten', 'kostet', 'euro', 'teuer', 'guenstig', 'billig', 'rabatt', 'gutschein'],
  None, ['Wie bestelle ich?'])
if en_count:
    F('englisch', 'Gibt es englische Ausgaben?',
      f'Ja. {en_count} ausgewählte Titel gibt es als „English Editions“ übersetzt ins Englische, als E-Book. ' +
      ('Sie wurden bei Google Play Books eingereicht und sind dort bald erhältlich („coming soon“).' if soon else 'Sie sind bei Google Play Books erhältlich.') +
      '\nAusgaben: ' + ', '.join(en_titles) + '.',
      ['englisch', 'english', 'englische', 'englischer', 'übersetzung', 'übersetzt', 'translation', 'google play', 'play books', 'ausland', 'in english', 'edition', 'editions'],
      [{'t': 'English Editions', 'h': 'en/'}], ['Welche Bücher gibt es?', 'Kontakt'])
F('kontakt', 'Wie erreiche ich den Verlag?',
  f'740 Publishing\n{addr}\nE-Mail: {mail}' + ('\nAuf Social Media: ' + ', '.join(s["t"] for s in social) + '.' if social else ''),
  ['kontakt', 'kontaktieren', 'erreichen', 'email', 'e mail', 'mail', 'adresse', 'anschrift', 'schreiben', 'nachricht', 'frage', 'anfrage', 'ansprechpartner', 'telefon', 'anrufen', 'instagram', 'tiktok', 'linktree', 'social media'],
  contact_links + social, ['Impressum', 'Rezensionsexemplar'])
F('impressum', 'Impressum', 'Das Impressum mit allen Pflichtangaben findest du hier. Inhaber von 740 Publishing ist ' + (owner or 'Alessandro Noto') + ', ' + addr + '.',
  ['impressum', 'inhaber', 'verantwortlich', 'betreiber', 'rechtliches', 'datenschutz', 'datenschutzerklärung'],
  [{'t': 'Impressum', 'h': 'impressum.html'}, {'t': 'Datenschutz', 'h': 'datenschutz.html'}], ['Kontakt'])
F('presse', 'Gibt es Rezensionsexemplare?',
  'Ja. Wer über Bücher schreibt, einen Buchblog oder einen Bookstagram- oder BookTok-Kanal betreibt, kann Rezensionsexemplare als E-Book oder Print anfragen, per E-Mail an ' + mail + '.',
  ['presse', 'rezension', 'rezensionsexemplar', 'rezensionsexemplare', 'blogger', 'blog', 'bookstagram', 'booktok', 'leseexemplar', 'influencer', 'kooperation'],
  [{'t': 'Exemplar anfragen', 'h': f'mailto:{mail}?subject=Anfrage%20Rezensionsexemplar'}, {'t': 'Presse & Blogger', 'h': 'index.html#presse'}], ['Kontakt'])
F('verlag', 'Wer ist 740 Publishing?', '\n'.join(about_p[:2]),
  ['verlag', 'ueber euch', 'wer seid', 'wer ist', 'über uns', 'lingen', 'unabhängig', 'verleger', 'hintergrund', 'firma', '740'],
  [{'t': 'Über den Verlag', 'h': 'index.html#verlag'}], ['Welche Bücher gibt es?', 'Kontakt'])
F('autoren', 'Welche Autorinnen und Autoren gibt es?',
  'Bei 740 Publishing erscheinen Bücher von: ' + ', '.join(authors) + '. Laut Impressum erscheinen die Bücher teilweise unter Pseudonymen.\nNenn mir einen Namen, dann zeige ich dir die Bücher.',
  ['autor', 'autoren', 'autorin', 'autorinnen', 'schriftsteller', 'pseudonym', 'pseudonyme', 'wer schreibt', 'geschrieben'],
  None, authors[:4])
F('bot', 'Speichert der Assistent meine Eingaben?',
  'Ich bin ein automatischer Assistent. Ich laufe nur in deinem Browser, nutze keine Cookies und speichere oder versende deine Eingaben nicht. Ich antworte ausschließlich mit Informationen von dieser Webseite und bin keine Beratung.',
  ['speichern', 'gespeichert', 'cookies', 'datenschutz assistent', 'bot', 'chatbot', 'ki', 'künstliche intelligenz', 'mensch', 'wer bist du', 'roboter'],
  None, ['Welche Bücher gibt es?', 'Kontakt'])
F('danke', 'Danke', 'Gern! Wenn du noch etwas wissen möchtest, frag einfach.',
  ['danke', 'dankeschön', 'super', 'toll', 'perfekt', 'tschüss', 'ciao', 'bye'], None, None)

kb = {
    'titel': '740 Publishing · Assistent',
    'begruessung': 'Hallo! Ich bin der automatische Assistent von 740 Publishing. Frag mich nach Büchern, Autorinnen und Autoren, Themen, Bestellung oder Kontakt.',
    'vorschlaege': ['Welche Bücher gibt es?', 'Wie bestelle ich?', 'Kontakt', 'Gibt es englische Ausgaben?'],
    'nachBuch': ['Wie bestelle ich?', 'Welche Bücher gibt es?', 'Kontakt'],
    'fallback': {
        'a': 'Dazu habe ich auf dieser Webseite leider nichts gefunden. Versuch es mit einem Buchtitel, einem Namen oder einem Thema, oder schreib dem Verlag direkt: ' + mail,
        'links': contact_links,
        'next': ['Welche Bücher gibt es?', 'Wie bestelle ich?', 'Kontakt'],
    },
    'katalog': {'t': 'Gesamtkatalog', 'h': 'index.html#katalog'},
    'kategorien': kategorien,
    'faq': faq,
    'buecher': books,
}
out = f'{SITE}/chatbot-wissen.js'
with open(out, 'w', encoding='utf-8') as fh:
    fh.write('/* Automatisch erzeugt von _werkstatt/gen/chatbot_kb.py aus den Seiteninhalten. Nicht von Hand ändern. */\n')
    fh.write('window.ChatbotWissen=' + json.dumps(kb, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('chatbot', len(books), 'Bücher,', len(faq), 'FAQ,', en_count, 'EN', os.path.getsize(out), 'Bytes')
