# Übergabe: 740 Publishing – Webseite & Social-Media-Marketing
Stand: 06.11.2026, 01:45 Uhr

Diese Datei ist die Übergabe an einen neuen Chat. **Bitte zuerst komplett lesen und dann weitermachen.** Den neuen Chat mit dem PC verbinden, damit der Ordner „Meine Bücher“ (unter Dokumente) erreichbar ist. Darin liegen alle Bücher als PDF/E-Book mit Covern.

---

## 1. Wer und was
- **Sandro (Alessandro Noto)**, Verleger von **740 Publishing**, Burgstraße 12, 49808 Lingen (Ems), 740publishingverlag@gmail.com.
- Er schreibt unter vielen Pseudonymen (Konstanze Frey, Victor Cross, Friedhelm Westerkamp, Juna Morel, Leo Winter, Clara Winter, Sandro Urban, Leonard Kramer, Evan J. Moore, Mika Solberg, Vivian Dahl, Judith Bahlmann u. a.). Veröffentlicht wird über **epubli**, die Bücher landen dann bei Amazon und im Buchhandel.
- **Arbeitsweise:** Er will nach jedem abgeschlossenen Schritt ein ausdrückliches **„Go“**. Gewünscht sind ehrliche Einschätzungen, klare Empfehlungen statt Optionslisten und keine Passwörter im Chat. Er spricht viel per Sprachnachricht, deshalb Tippfehler großzügig deuten.

## 2. Webseite
- **Live:** https://alessandronoto84.github.io/740publishing/
- **Repo:** `alessandronoto84/740publishing` (public, GitHub Pages, Branch `main`, `.nojekyll`). Commits als `Alessandro Noto <740publishingverlag@gmail.com>`.
- **Design:** Schwarz-Gold. Schriften Cormorant Garamond und Figtree, selbst gehostet (keine Google Fonts, wegen DSGVO).
- **Startseite:**
  - Animierte Bühne: schräge, laufende Cover-Wand, das Logo erscheint mit goldenem Lichtstreifen.
  - Slogan **„Für alle, die mehr wissen wollen.“** baut sich Wort für Wort auf. Die Verzögerungen stehen inline an jedem `<span>`, nicht im CSS.
  - Unterzeile: „Sachbücher, Ratgeber, Reiseführer und Romane über Psychologie, Gesundheit, Kultur, Gesellschaft und die Welt.“
  - Abschnitte: Neuerscheinungen (mit Trailer-Player), Demnächst (aktuell nur Fußball), **Unsere Reihen**, Gesamtkatalog mit **Suchfeld** und Kategorie-Chips, **Über 740 Publishing**, **Presse & Blogger** (mailto-Button), Footer mit Instagram/TikTok/Linktree.
  - Sandro mag die Animation. Der Slogan wurde zusammen erarbeitet. Er wollte nichts Reißerisches, sondern breit formuliert, weil sein Programm auch Psychologie, Fitness, Garten und Ratgeber umfasst.
- **57 Buchseiten** unter `/buch/<slug>.html`, jeweils mit:
  - Seitentitel mit Suchbegriff und eigener Beschreibung für Google
  - Book-JSON-LD
  - Abschnitten „Für wen ist dieses Buch?“ und „Das erwartet dich“
  - verwandten Büchern
- **Seiten-Infrastruktur:**
  - `sitemap.xml` und `robots.txt` liegen im Repo.
  - Google Search Console ist eingerichtet (Verlagskonto, HTML-Datei `googlef03703abd89cc161.html`) und die Sitemap eingereicht.
  - Impressum und Datenschutz sind vorhanden. Die CSS-Datei wird mit `?v=<zahl>` gegen den Browser-Cache abgesichert.
- **Eigene Domain 740publishing.de:** macht Sandro später. Die DNS-Einträge stehen unten unter Punkt 7.

### Bau-Werkstatt (in diesem Repo unter `_werkstatt/`)
- `gen/catalog.py`: **zentrale Bücherliste.**
  - `CAT` = Tupel `(key, Titel, Autor, Kategorie, ebook_isbn, print_isbn, print_typ, cover)`. Cover `'../cov_x'` → `covers/cov_x.jpg`, sonst `covers/cat/<cover>.jpg`.
  - `BLURB` = Verkaufstexte, `EXTRA` = Sonderlinks, `SLUG` = abweichende epubli-Slugs.
- `gen/seo.py`: pro Buch (Suchbegriff-Untertitel, „Für wen“-Liste, „Das erwartet dich“-Liste).
- `gen/build.py`: baut `index.html`. Aufruf `python3 gen/build.py $S`.
- `gen/pages.py`: baut die Buchseiten, `sitemap.xml` und `robots.txt`. Aufruf `python3 gen/pages.py $S`.
- `gen/index_tpl.html`: Vorlage der Startseite.
- `gen/english.py`: baut `en/index.html` („English Editions“, 15 englische E-Books). Aufruf `python3 gen/english.py $S`. Cover 600 px unter `covers/en/<key>.{jpg,webp}`. Sobald ein Buch bei Google Play live ist, geprüften Link in `GPLAY['<key>']` eintragen, dann erscheint ein Kaufbutton statt „Coming soon on Google Play Books“.
- `catalog.py` → `NEW_ED`: neue Ausgaben (12 Hardcover + Körperkult-Softcover), bei epubli angelegt, aber noch nicht veröffentlicht. Leere Einträge werden nicht angezeigt; nach Veröffentlichung ISBN und geprüften epubli-Link eintragen und neu bauen. `SERIES_OF`: Reihe und Band je Buch (laut epubli-Metadaten 06.11.).
- `gen/wall.txt`: welche Cover in der animierten Wand laufen. Die Thumbnails liegen unter `covers/wall/`, 200×300.
- `posts/tpl.html`, `asr/posts2.cjs`: rendern die Instagram-Karussells (je 3 Bilder, 1080×1350) nach `site/posts/<k>_{1,2,3}.jpg`.
  - Liest `posts/data.json` mit Feldern `k, title, author, hook, text, formats, line` und das Cover `posts/cover_<k>.png`.
  - Aufruf: `cd asr && node posts2.cjs $S`. Playwright und Chromium sind vorinstalliert.
- `covers_hd/`: hochauflösende Frontcover als JPG. Für `posts2.cjs` vorher nach `posts/cover_<k>.png` konvertieren.
- `gen/chatbot_kb.py`: baut die Wissensbasis des **Chat-Assistenten** (`chatbot-wissen.js`) aus den fertigen Seiten (Buchseiten, Startseite, English Editions, Impressum). Aufruf **nach** build/pages/english: `python3 gen/chatbot_kb.py $S`. Der Assistent selbst: `chatbot.js` + `chatbot.css` im Repo-Root (rein im Browser, keine Cookies, kein Server); eingebunden in `index_tpl.html`, `pages.py` (FOOT), `impressum.html`, `datenschutz.html`. Auch auf `en/` (eingebunden in `english.py`): die Wissensbasis enthält Deutsch und Englisch (`sprachen.de/en`), der Bot wählt nach `<html lang>`. Script-Version `?v=` bei Änderungen am Bot in Vorlage, `pages.py`, `english.py`, Impressum und Datenschutz hochzählen.
- **Startseiten-Module oben (seit 07.11.2026)**, gebaut von `gen/picks.py`, Browser-Logik in `entdecken.js` (Repo-Root, keine Cookies):
  - **Laufband „Beliebt bei unseren Lesern“**: Liste `BELIEBT` in `catalog.py` (Schlüssel aus `CAT`, Reihenfolge = Anzeige). Es gibt keine Verkaufszahlen im Repo, deshalb kein „Bestseller“ und keine Zahlen. Startauswahl = die 10 Titel mit Trailer. Auf `en/` heißt es „Featured English Editions“ (Liste `EN_FEATURED` in `english.py`), weil die englischen Ausgaben noch nicht im Handel sind.
  - **„Unser Tipp des Tages“**: feste gemischte Reihenfolge (Seed 740), Tagesindex nach Datum Europe/Berlin → für alle Besucher am selben Tag gleich, jedes Buch einmal pro Durchlauf.
  - **„Zufällig entdeckt“**: bei jedem Aufruf ein zufälliges Buch (nie gleich dem Tipp), Button „Noch ein Buch“.
- `epubli_list.txt`: komplette Liste aller epubli-Veröffentlichungen mit ISBNs (Stand 06.11.).

**Ordnerstruktur für die Skripte:**
- `S` = Arbeitsordner mit den Unterordnern `gen/`, `posts/`, `asr/` und `site/`.
- `site/` ist eine Kopie des Repos ohne `_werkstatt`.
- Ablauf: Repo nach `S/site` klonen, `_werkstatt/*` nach `S/` kopieren, bauen. Danach `S/site` zurück ins Repo kopieren, committen und pushen.

### Link-Regeln
- **Amazon:** ISBN-13 → ISBN-10 → `https://www.amazon.de/dp/<isbn10>`. Die Prüfziffer neu berechnen, die Funktion `isbn10()` steht in `pages.py`.
- **epubli:** `https://www.epubli.com/shop/<titel-slug>-<ISBN13>`, mit ä→ae, ö→oe, ü→ue, ß→ss.
- **Stand 06.11.:** Alle 57 Amazon-, 59 epubli- und 2 Hugendubel-Links geprüft, **alle funktionieren**.
- Die Sandbox kommt nicht direkt an Amazon, epubli oder github.io heran. Prüfen geht über den Chrome-Browser (Claude in Chrome) mit `fetch()` von der jeweiligen Seite aus.

## 3. Social Media (Metricool)
- **Konto:**
  - Metricool, `blogId` **7678602**, Brand-Zeitzone Asia/Bangkok. Daten immer mit `timezone: Europe/Berlin` senden.
  - Netzwerke: Instagram @740_publishing, TikTok @740publishing (Firmenkonto; **nie** das Privatkonto „Mr. Oni Mahoni“), YouTube, Facebook. Free-Plan.
  - Medien müssen öffentliche URLs sein. Die Karussellbilder liegen unter `https://alessandronoto84.github.io/740publishing/posts/<k>_<n>.jpg`. Vor dem Einplanen warten, bis GitHub Pages fertig deployt ist, sonst kommt „Failed to normalize media“.
- **Karussell-Format:**
  - Instagram, Facebook (`type POST`) und TikTok (Foto-Post mit `title`, `commercialContentOwnBrand: true`), `instagramData.isAiGenerated: true`.
  - Text: Hook + Emoji, Verkaufstext, Titel/Autor, Formate, „Wischen für mehr“, Kauflinks, „Link in der Bio“, Frage, 5 Hashtags.
  - `firstCommentText` enthält die Kauflinks.
- **Reels:** die 10 Buchtrailer.
  - Videos liegen im Metricool-Entwurf `uuid 7312264904212431583`. **Nicht löschen.**
  - Eingeplant: 27.10 Astrologie, Freizeitpark, Thailand; 29.10 Kaffee; 31.10 Deutsch-Rap; 2.11 Schönheit; 4.11 Deutschland kifft; 6.11 Drogen (jeweils 18:30).
  - Fußball-Reel fehlt noch, das Buch ist gerade erschienen (siehe unten).
- **Buchvorstellungen (Karussells):** eingeplant von **27.10. bis 10.12., jeden Tag eine** (meist 18:30 Uhr, an Reel-Tagen bis 7.11. um 12:30). Insgesamt 45 Bücher. Zuletzt: 9.12. Sucht, 10.12. Könige der Asche.
- **Linktree:** linktr.ee/740Publishing ist in den Bios eingetragen.

## 4. OFFENE AUFGABEN (in dieser Reihenfolge)
1. **Aus „Meine Bücher“ auf dem PC die Frontcover holen** (scharf, mindestens 600 px breit) für diese 12 Bücher, die bisher nur unscharfe Cover haben (ca. 194 px):
   - KARMA
   - Zwischen Licht und Schatten
   - Generation Underground
   - Drogen
   - Schwarzes Wasser
   - Zwischen Blut und Asphalt
   - Das Manuskript
   - Jabari
   - Körperkult
   - Der optimierte Mensch
   - Das große Fitnessbuch
   - Die Piercing Akademie

   Plus **Das Delegations System** (gar kein Cover). Danach Webseite neu bauen: `covers/cat/<cover>.jpg` mit 420 px Breite, Drogen als `covers/cov_drogen.jpg`, dazu `covers/wall/` und `covers_hd/`.
2. **Klappentexte** aus den Büchern bzw. Coverdateien lesen und daraus Verkaufstexte (`BLURB`) plus `seo.py`-Einträge („Für wen“ / „Das erwartet dich“) schreiben. Betrifft diese 8 Bücher:
   - Schwarzes Wasser
   - Zwischen Blut und Asphalt
   - Das Manuskript
   - Jabari
   - Körperkult
   - Der optimierte Mensch
   - Das große Fitnessbuch
   - Die Piercing Akademie

   **Nichts erfinden.** Nur, was in den Texten steht.
3. **„Das Delegations System“** (Alessandro Noto, E-Book, ISBN 9783565437696) in den Katalog aufnehmen.
   - Kategorie Sachbuch & Ratgeber.
   - Shop-Untertitel: „Ein praktischer Guide für erschöpfte Mütter mit Checklisten, Vorlagen & Gesprächsleitfaden“, Thema Mental Load verstehen, delegieren, loslassen.
4. **Buchvorstellungen (Karussells) für diese 13 Bücher** bauen und **ab 11.12. täglich um 18:30 Uhr** in Metricool einplanen.
5. **Die dunkle Seite des Fußballs** (Jan Völker) ist erschienen. Sobald die epubli-Shop-Seite live ist (am 06.11. noch 404):
   - aus „Demnächst“ in den Katalog verschieben; ISBN E-Book 9783565850679, Softcover 9783565850662
   - Verkaufstext aus dem Buch schreiben, Karussell bauen
   - **Fußball-Reel** einplanen. Das Video ist im Metricool-Entwurf (`mtr_12533345646441126853`), das Cover liegt in `covers_hd/fussball.jpg` und `covers/cov_fussball.jpg`.
6. **Neue E-Books ergänzen**, sobald die Shop-Seiten live sind (am 06.11. noch 404):
   - Bier: E-Book 9783565850624 (in `catalog.py` steht bisher nur das Taschenbuch, `EXTRA['bier']` dann entfernen)
   - Schamanismus: E-Book 9783565850631 (`EXTRA['schamanismus']` dann entfernen)
   - Sucht: E-Book 9783565850587
   - Könige der Asche: E-Book 9783565850648
7. **Die zweite Emilia** hat zwei Taschenbuch-ISBNs (9783565662722 und 9783565662739), beide bei Amazon gelistet.
   - Empfehlung an Sandro: Er löscht bei epubli selbst die …662739. Claude löscht nichts bei epubli.
   - Die Webseite nutzt …662722.

## 5. Später / Ideen
- Amazon-Sichtbarkeit: Beschreibungen und Schlagwörter bei epubli optimieren, Amazon Author Central für jedes Pseudonym, Rezensionsexemplare an Blogger. **Keine gekauften Rezensionen.** Texte bereitet Claude vor, Sandro trägt sie ein.
- Rituale (Vivian Dahl) schreibt Sandro gerade. ZUFALL (Konstanze Frey) ist noch nicht geschrieben. Helena Waldner wird nicht mehr genutzt. Neue Bücher zuerst unter „Demnächst“ aufnehmen.

## 6. Bekannte Stolpersteine
- **Bücherliste bei epubli:** „Meine Bücher“ lädt im Claude-Chrome-Tab erst nach ca. 20–30 Sekunden.
- **Beschreibungen im epubli-Shop:** werden per JavaScript nachgeladen. Im gerenderten Tab mit `document.body.innerText` ab „Beschreibung“ auslesen.
- **Downloads aus der Sandbox:** epubli, Amazon und github.io sind dort gesperrt (Proxy 403). Bilder also nicht dort herunterladen, sondern vom PC nehmen.
- **Cookie-Banner:** immer „Mehr“ → „Services speichern“, also nur die notwendigen Cookies.

## 7. Domain (für später)
Bei 740publishing.de:
- A-Records 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- CNAME `www` → `alessandronoto84.github.io`
- danach in GitHub Pages die Custom Domain eintragen und in allen Dateien `BASE` (in `pages.py`, `index_tpl.html`) und die Sitemap anpassen.
