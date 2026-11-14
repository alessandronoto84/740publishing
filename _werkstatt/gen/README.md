# Webseite 740 Publishing – so bleibt sie aktuell

Alle Seiten werden aus Daten erzeugt. **Nie die fertigen HTML-Dateien von Hand ändern**, sondern die Daten unten und dann neu bauen.

## Ordner
`S` ist ein Arbeitsordner mit zwei Verknüpfungen: `S/gen` → `_werkstatt/gen`, `S/site` → Repo-Wurzel.

## Bauen (Reihenfolge einhalten)
```
python3 gen/linkcheck.py            # 1. alle Kauf-Links prüfen (braucht Internet)
python3 gen/build.py   $S           # 2. Startseite index.html
python3 gen/pages.py   $S           # 3. Buchseiten buch/*.html, sitemap.xml, robots.txt
python3 gen/english.py $S           # 4. English Editions en/index.html
python3 gen/chatbot_kb.py $S        # 5. Wissen des Chat-Assistenten (liest die fertigen Seiten)
```
Vor jedem Push: `python3 gen/linkcheck.py --report` (zeigt, welche Links nicht funktionieren).

## Was ändere ich wo?
| Aufgabe | Datei / Daten |
|---|---|
| Neues Buch | `catalog.py` → `CAT` (Schlüssel, Titel, Autor, Bereich, E-Book-ISBN, Druck-ISBN, Druckart, Cover) + `BLURB` (Klappentext). Cover als JPG 420×630 nach `covers/cat/<cover>.jpg`. Optional `seo.py`. |
| Neue Ausgabe (z. B. Hardcover) eines vorhandenen Buchs | `catalog.py` → `NEW_ED['<key>']['Hardcover']=('<ISBN>','')`. Den Link baut die Webseite selbst (`epubli.com/shop/<titel-slug>-<ISBN>`). |
| „Neu erschienen“ | `catalog.py` → `RELEASES`: Zeile `('JJJJ-MM-TT','<key>','<Format>','<ISBN>')` oben ergänzen. Ältere Daten liest der Linkcheck automatisch aus dem epubli-Shop („Erscheinungsdatum“). Anzahl: `NEU_ANZAHL`. |
| Preise | `catalog.py` → `PRICE` (ISBN → Preis). Der Linkcheck ergänzt Preise aus dem epubli-Shop automatisch; Einträge in `PRICE` haben Vorrang (z. B. nach einer Preisänderung). |
| Englische Ausgaben | `english_data.py` → `EN`. Sobald ein Buch bei Google Play live ist: geprüften Link in `GPLAY['<key>']` eintragen → Kaufbutton statt „Coming soon“. |
| Laufband „Beliebt“ | `catalog.py` → `BELIEBT` |

## Kauf-Links und „Bald verfügbar“
Die Webseite zeigt einen Kauf-Button **nur**, wenn der Link in `linkstatus.json` als funktionierend (`"ok": true`) steht.
Jedes Format ohne funktionierenden Link erscheint als gestricheltes Badge **„bald verfügbar“** (ohne Link).
Damit gibt es keine toten Links: Sobald epubli/Amazon die Seite freischaltet, `linkcheck.py` laufen lassen und neu bauen, dann erscheint der Button von selbst.

`linkcheck.py` prüft: HTTP-Status 200 **und** der Buchtitel steht auf der Zielseite (epubli liefert bei unbekannter ISBN eine 404-Seite, Amazon eine „nicht gefunden“-Seite).
Beim epubli-Shop liest es außerdem Preis und Erscheinungsdatum mit.

**Wenn das Skript keinen Internetzugang hat** (z. B. in der Claude-Sandbox: epubli/Amazon sind dort gesperrt), meldet es „nicht erreichbar“ und lässt die alten Ergebnisse stehen.
Dann im Browser prüfen (Claude in Chrome: auf `epubli.com` bzw. `amazon.de` eine Seite öffnen und per `fetch()` jede URL aus `links.json` abrufen; bei epubli werden Preis/Datum erst per JavaScript geladen, also die Seite in einem iframe rendern und `Erscheinungsdatum:` / `€ inkl. MwSt.` aus dem Text lesen).
Das Ergebnis als JSON `{url: {"ok":true|false,"code":200,"shop":"epubli","checked":"JJJJ-MM-TT","price":"21,99","date":"08.11.2026","isbn":"978…"}}` speichern und mit
`python3 gen/linkcheck.py --import ergebnis.json` übernehmen. `python3 gen/linkcheck.py --list` schreibt alle zu prüfenden Links nach `links.json`.

## Prüfen vor dem Push
- Bauen ohne Fehler (alle fünf Schritte oben).
- `python3 gen/linkcheck.py --report`
- Lokale Seite: `python3 -m http.server` im Repo, Startseite und eine Buchseite bei 390 px und 1440 px ansehen.

## Ghostwriting-Seite „Buch schreiben lassen“
- `buch-schreiben-lassen/index.html` und `ghostwriting.css` (Repo-Wurzel) sind **handgepflegt**, nicht generiert. Kein Bauskript überschreibt sie.
- Preise, Paketumfänge, FAQ und Texte direkt in `buch-schreiben-lassen/index.html` pflegen (auch das JSON-LD im `<head>` und die FAQ-Daten dort mitändern).
- Anfrageformular: Ohne Endpunkt öffnet es das E-Mail-Programm des Besuchers (mailto an die Verlagsadresse). Für einen Formulardienst die Adresse am Formular eintragen: `<form … data-endpoint="https://…">`. Dann wird per POST (JSON) gesendet. Vorher Datenschutzerklärung ergänzen.
- Werbung auf der Startseite: Hinweis-Pille im Hero (`.hero-gw`) und Werbeblock `#ghostwriting` (`.gwpromo`, zwischen Tipp des Tages und „Neu erschienen“) stehen fest in `index_tpl.html`, Styles am Ende von `style.css`. Preis „ab 3.900 €“ dort mitändern, wenn sich der START-Preis ändert.
- Navigation „Buch schreiben lassen“ (`class="nav-gw"`) steht in `index_tpl.html`, `pages.py` (HEAD/FOOT), `impressum.html`, `datenschutz.html`. Die URL steht in der Sitemap (`pages.py`).
- Der Chat-Assistent liest die Seite mit ein (`chatbot_kb.py`, Pakete aus `.pack`, FAQ aus `<details>`). Nach Änderungen an der Seite `python3 gen/chatbot_kb.py $S` laufen lassen.
