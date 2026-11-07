# Startseiten-Module: Laufband „Beliebt bei unseren Lesern“, „Unser Tipp des Tages“ und Zufallsbuch.
# Wird von build.py (deutsche Startseite) und english.py (en/) benutzt. Logik im Browser: entdecken.js (Repo-Root).
#
# Bücher-Datensatz je Buch: dict(k, t, a, g, cov, href, d)
#   k = Schlüssel, t = Titel, a = Autor, g = Bereich, cov = Cover-URL, href = Ziel-Link, d = Kurztext
#
# Tipp des Tages: Die Bücher werden einmal fest (Seed) gemischt; jeden Tag (Datum in Europe/Berlin) kommt das
# nächste Buch dieser Reihenfolge dran. So ist der Tipp für alle Besucher am selben Tag gleich und jedes Buch kommt
# einmal pro Durchlauf dran. Zufallsbuch: bei jedem Seitenaufruf neu, nie gleich dem Tipp des Tages.
import html, json, random, datetime
try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None

e = html.escape
SEED = 740

def order(books):
    """Feste, gemischte Reihenfolge für den Tipp des Tages (identisch in Python und im Browser, da als Liste eingebettet)."""
    b = list(books)
    random.Random(SEED).shuffle(b)
    return b

def day_index(n):
    """Gleiche Formel wie entdecken.js: Tage seit 1970-01-01 (Datum in Europe/Berlin) modulo n."""
    now = datetime.datetime.now(ZoneInfo('Europe/Berlin')) if ZoneInfo else datetime.datetime.utcnow()
    d = now.date()
    return (d - datetime.date(1970, 1, 1)).days % n

def ticker(items, label, rest, aria):
    """label = Kurzform (auch auf dem Handy sichtbar), rest = Fortsetzung (nur ab Tablet-Breite)."""
    """Laufband. items = Liste der Bücher in Anzeigereihenfolge. Inhalt doppelt für die Endlos-Schleife."""
    def one(b, hide=False):
        h = ' tabindex="-1"' if hide else ''
        return (f'<a class="tk" href="{e(b["href"])}"{h}><img src="{e(b["cov"])}" alt="" width="28" height="42" decoding="async">'
                f'<span class="tk-t">{e(b["t"])}</span><span class="tk-a">{e(b["a"])}</span></a>')
    row = ''.join(one(b) for b in items)
    dup = ''.join(one(b, True) for b in items)
    dur = max(30, len(items) * 6)
    return (f'<div class="tick" role="region" aria-label="{e(aria)}">'
            f'<span class="tick-lbl"><span aria-hidden="true">★</span> {e(label)}<span class="tick-rest">&nbsp;{e(rest)}</span></span>'
            f'<div class="tick-view"><div class="tick-track" style="--dur:{dur}s">'
            f'<div class="tick-set">{row}</div><div class="tick-set" aria-hidden="true">{dup}</div>'
            f'</div></div></div>')

def card_inner(b, more):
    """Innenleben einer Tipp-Karte (gleiche Struktur wie render() in entdecken.js)."""
    return (f'<a class="pick-cov" href="{e(b["href"])}" tabindex="-1" aria-hidden="true"><img src="{e(b["cov"])}" alt="" width="120" height="180" loading="lazy"></a>'
            f'<div class="pick-body"><p class="pick-g">{e(b["g"])}</p>'
            f'<h3><a href="{e(b["href"])}">{e(b["t"])}</a></h3>'
            f'<p class="pick-a">{e(b["a"])}</p>'
            f'<p class="pick-d">{e(b["d"])}</p>'
            f'<a class="pick-more" href="{e(b["href"])}">{e(more)}</a></div>')

def picks(books, L):
    """Abschnitt mit „Tipp des Tages“ und Zufallsbuch. L = Beschriftungen (Sprache)."""
    ordered = order(books)
    n = len(ordered)
    i = day_index(n)
    tip, rnd = ordered[i], ordered[(i + 1) % n]   # Startzustand ohne JavaScript; das Skript ersetzt beides
    data = {'lang': L['lang'], 'more': L['more'], 'books': [{k: b[k] for k in ('k', 't', 'a', 'g', 'cov', 'href', 'd')} for b in ordered]}
    js = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    return f'''<section class="picks wrap" id="entdecken" aria-label="{e(L['aria'])}">
    <article class="pick pick-day">
      <header class="pick-h"><p class="eyebrow">{e(L['day'])}</p><p class="pick-date" id="pick-date"></p></header>
      <div class="pick-card" id="pick-day">{card_inner(tip, L['more'])}</div>
    </article>
    <article class="pick pick-rnd">
      <header class="pick-h"><p class="eyebrow">{e(L['rnd'])}</p><button class="pick-again" type="button" id="pick-again" hidden>{e(L['again'])}</button></header>
      <div class="pick-card" id="pick-rnd" aria-live="polite">{card_inner(rnd, L['more'])}</div>
    </article>
    <script type="application/json" id="pick-data">{js}</script>
  </section>'''
