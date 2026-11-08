# Gemeinsame Bausteine für build.py und pages.py: Format-Badges und Kauf-Buttons je Buch.
# Daten kommen aus catalog.editions(k) (geprüfte Links aus linkstatus.json, Preise aus catalog.PRICE).
import html
from catalog import editions
e=html.escape

def isbnfmt(i): return f'{i[:3]}-{i[3]}-{i[4:10]}-{i[10:12]}-{i[12]}' if i and len(i)==13 else i

def badges(k):
    """Zeile mit allen Formaten: lieferbar (gefüllt) oder „bald verfügbar“ (gestrichelt), mit Preis, wenn belegt."""
    out=[]
    for ed in editions(k):
        pr=f' <span class="pr">{e(ed["price"])}&nbsp;€</span>' if ed['price'] else ''
        if ed['soon']:
            out.append(f'<span class="fb bald" title="Bald verfügbar{(" · ISBN "+isbnfmt(ed["isbn"])) if ed["isbn"] else ""}">{e(ed["f"])}{pr}<small>bald verfügbar</small></span>')
        else:
            out.append(f'<span class="fb">{e(ed["f"])}{pr}</span>')
    return f'<p class="fbs" aria-label="Formate">{"".join(out)}</p>' if out else ''

def buttons(k, sm=False, verb=False, one=False):
    """Kauf-Buttons nur für geprüft funktionierende Links; Formate ohne Link als „Bald verfügbar“ (ohne Link)."""
    c=' sm' if sm else ''; out=[]
    for ed in editions(k):
        pr=f' · {e(ed["price"])} €' if ed['price'] else ''
        for shop,u in (ed['links'][:1] if one else ed['links']):   # one=True: nur ein Shop je Format (epubli zuerst)
            lab=f'bei {shop} kaufen' if verb else shop
            out.append(f'<a class="buy{c}" href="{e(u)}" target="_blank" rel="noopener"><span class="fmt">{e(ed["f"])}</span><span class="shop">{e(lab)}</span></a>')   # Preis steht im Badge
    # Formate ohne funktionierenden Link stehen als „bald verfügbar“ in badges(), nicht als Button.
    return ''.join(out)

def live_formats(k): return [ed['f'] for ed in editions(k) if not ed['soon']]
def soon_formats(k): return [ed for ed in editions(k) if ed['soon']]
