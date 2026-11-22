# (key, title, author, category, ebook_isbn, print_isbn, print_type, cover)
R='Romane'; S='Sachbuch & Ratgeber'; T='Reiseführer'
CAT=[
 ('karma','KARMA','Konstanze Frey',R,'9783565538997','9783565539000','Taschenbuch','karma'),
 ('glueck','GLÜCK','Konstanze Frey',R,'9783565560974','9783565560950','Taschenbuch','glueck'),
 ('pech','PECH','Konstanze Frey',R,'9783565568963','9783565568956','Taschenbuch','pech'),
 ('ordnung','ORDNUNG','Konstanze Frey',R,'9783565564859','9783565564835','Taschenbuch','ordnung'),
 ('katastrophe','Die freundliche Katastrophe','Konstanze Frey',R,'9783565530717','9783565530700','Taschenbuch','katastrophe'),
 ('krone','Krone aus Beton','Sandro Urban',R,'9783565575763','9783565575718','Taschenbuch','krone'),
 ('licht-schatten','Zwischen Licht und Schatten','Sandro Noto',R,'9783565526857','9783565526864','Taschenbuch','licht-schatten'),
 ('karten','Wo die Karten enden','Alessandro Noto',R,'9783565571475','9783565571468','Taschenbuch','karten'),
 ('sizilien','Bis nach Sizilien','Alessandro Noto',R,'9783565658695','9783565658664','Taschenbuch','sizilien'),
 ('aurora','Projekt Aurora','Judith Bahlmann',R,'9783565599707','9783565580224','Taschenbuch','aurora'),
 ('emilia','Die zweite Emilia','Judith Bahlmann',R,'9783565668472','9783565662739','Taschenbuch','emilia'),
 ('gaertner','Die Gärtner der Geschichte','Markus Wieland',R,'9783565662821','9783565662807','Taschenbuch','gaertner'),
 ('sucht','Sucht','Sandro Urban',R,None,'9783565833375','Taschenbuch','sucht'),
 ('koenige','Könige der Asche','Evan J. Moore',R,None,'9783565833382','Taschenbuch','koenige'),
 ('schwarzes-wasser','Schwarzes Wasser','Juna Morel',R,'9783565478262','9783565478279','Taschenbuch','schwarzes-wasser'),
 ('blut-asphalt','Zwischen Blut und Asphalt','Juna Morel',R,'9783565495290','9783565496303','Taschenbuch','blut-asphalt'),
 ('manuskript','Das Manuskript','Evan J. Moore',R,'9783565463954','9783565463152','Taschenbuch','manuskript'),
 ('jenseits','Jenseits des Himmels','Leo Winter',R,None,'9783565446001','Taschenbuch','jenseits'),
 ('wns','Wer nichts sieht …','Hanna Sedlak',R,'9783565858446','9783565858439','Taschenbuch','wns'),
 ('jabari','Jabari','Amari Diallo',R,'9783565455621','9783565455737','Hardcover','jabari'),
 ('underground','Generation Underground','Sandro Urban',S,'9783565496648','9783565496655','Taschenbuch','underground'),
 ('algorithmus','Generation Algorithmus','Friedhelm Westerkamp',S,'9783565585588','9783565585540','Taschenbuch','algorithmus'),
 ('ki','Künstliche Intelligenz','Friedhelm Westerkamp',S,'9783565465750',None,None,'ki'),
 ('digitale-erschoepfung','Digitale Erschöpfung','Friedhelm Westerkamp',S,'9783565463312','9783565463060','Taschenbuch','digitale-erschoepfung'),
 ('spiel','Das Spiel läuft immer','Friedhelm Westerkamp',S,'9783565496631','9783565496426','Taschenbuch','spiel'),
 ('liebe','Ist das noch Liebe?','Friedhelm Westerkamp',S,'9783565645817','9783565645787','Taschenbuch','liebe'),
 ('erwachsen','Wir spielen erwachsen','Friedhelm Westerkamp',S,'9783565658565','9783565658558','Taschenbuch','erwachsen'),
 ('zurueck-ins-leben','Wie ich zurück ins Leben gefunden habe','Clara Winter',S,'9783565473328','9783565476831','Taschenbuch','zurueck-ins-leben'),
 ('toleranz','Im Namen der Toleranz','Theodor Brenner',S,'9783565465415','9783565465521','Taschenbuch','toleranz'),
 ('uebermensch','Projekt Übermensch','Victor Cross',S,'9783565473410','9783565476770','Taschenbuch','uebermensch'),
 ('powerfrau','Projekt Powerfrau','Victor Cross',S,'9783565472833','9783565476794','Taschenbuch','powerfrau'),
 ('optimierte','Der optimierte Mensch','Viktor Cross',S,'9783565470846',None,None,'optimierte'),
 ('psychologie','Psychologie im Alltag','Friedhelm Westerkamp',S,'9783565473014','9783565473236','Taschenbuch','psychologie'),
 ('schamanismus','Schamanismus','Vivian Dahl',S,None,'9783565830510','Taschenbuch','schamanismus'),
 ('bier','Bier','Sandro Noto',S,None,'9783565830497','Taschenbuch','bier'),
 ('koerperkult','Körperkult','Samuel Dorn',S,None,'9783565476664','Hardcover','koerperkult'),
 ('unsichtbarkeit','Erlernte Unsichtbarkeit','Konstantin Reeder',S,'9783565549474','9783565546800','Taschenbuch','unsichtbarkeit'),
 ('mensch','Was ist der Mensch?','Michael Rabenau',S,'9783565585939','9783565585861','Taschenbuch','mensch'),
 ('spiritualitaet','Das große Praxisbuch der Spiritualität','Leonard Kramer',S,'9783565489398','9783565488827','Taschenbuch','spiritualitaet'),
 ('grenzen','Energetische Grenzen','Leonard Kramer',S,'9783565892655','9783565892624','Taschenbuch','grenzen'),
 ('notfall','Die spirituelle Notfallapotheke','Leonard Kramer',S,'9783565892617','9783565892532','Taschenbuch','notfall'),
 ('kompass','Dein innerer Kompass','Leonard Kramer',S,'9783565891788','9783565891733','Taschenbuch','kompass'),
 ('kippt','Deutschland kippt','Theodor Brenner',S,'9783565879953','9783565879946','Taschenbuch','kippt'),
 ('fitness','Das große Fitnessbuch','Alessandro Noto',S,'9783565438822','9783565438679','Taschenbuch','fitness'),
 ('selbstversorger','Das große Selbstversorgerbuch','Alessandro Noto',S,'9783565437597','9783565437535','Taschenbuch','selbstversorger'),
 ('delegations','Das Delegations System','Alessandro Noto',S,'9783565437696',None,None,'delegations'),
 ('piercing','Die Piercing Akademie','Alessandro Noto',S,None,'9783818756680','Taschenbuch','piercing'),
 ('auswandern','Auswandern, aber wohin?','Mika Solberg',T,'9783565580156','9783565580064','Taschenbuch','auswandern'),
 ('vietnam','Die verborgene Seite von Vietnam','Mika Solberg',T,'9783565636112','9783565636082','Taschenbuch','vietnam'),
 ('japan','Die verborgene Seite von Japan','Mika Solberg',T,'9783565652112','9783565652105','Taschenbuch','japan'),
 ('china','Die verborgene Seite von China','Mika Solberg',T,'9783565662708','9783565662692','Taschenbuch','china'),
 ('mexiko','Die verborgene Seite von Mexiko','Mika Solberg',T,'9783565701933','9783565701865','Taschenbuch','mexiko'),
 ('kolumbien','Die verborgene Seite von Kolumbien','Mika Solberg',T,'9783565725632','9783565725564','Taschenbuch','kolumbien'),
 ('ecuador','Die verborgene Seite von Ecuador','Mika Solberg',T,'9783565728763','9783565728756','Taschenbuch','ecuador'),
 ('peru','Die verborgene Seite von Peru','Mika Solberg',T,'9783565730513','9783565730506','Taschenbuch','peru'),
]
EXTRA={'schamanismus':[('Taschenbuch','epubli','https://www.epubli.com/shop/schamanismus-9783565830510')],'bier':[('Taschenbuch','epubli','https://www.epubli.com/shop/bier-9783565830497')],'piercing':[('Taschenbuch','epubli','https://www.epubli.com/shop/die-piercing-akademie-9783818756680'),('Taschenbuch','Hugendubel','https://www.hugendubel.de/de/buch_kartoniert/alessandro_noto-die_piercing_akademie-49704145-produkt-details.html')]}
CAT += [
 ('k-freizeitpark','Wir fahren in den Freizeitpark','Tobias Kranz',R,'9783565739790','9783565739776','Taschenbuch','../cov_freizeitpark'),
 ('k-rap','Deutsch-Rap','Sandro Urban',S,'9783565491421','9783565491414','Taschenbuch','../cov_rap'),
 ('k-kifft','Deutschland kifft','Sandro Urban',S,'9783565739585','9783565740413','Taschenbuch','../cov_kifft'),
 ('k-drogen','Drogen – Das umfassende Standardwerk','Alessandro Noto',S,'9783565525911','9783565526659','Taschenbuch','../cov_drogen'),
 ('k-kaffee','Kaffee','Sandro Noto',S,'9783565737932','9783565737895','Taschenbuch','../cov_kaffee'),
 ('k-schoenheit','Warum Schönheit Macht ist','Katharina Bruns',S,'9783565501397','9783565501366','Taschenbuch','../cov_schoenheit'),
 ('k-astrologie','Astrologie','Vivian Dahl',S,'9783565752201','9783565752270','Taschenbuch','../cov_astrologie'),
 ('k-thailand','Die verborgene Seite von Thailand','Mika Solberg',T,'9783565585663','9783565585656','Taschenbuch','../cov_thailand'),
 # Fußball: bei Amazon live (Taschenbuch, Erscheinungstermin 05.11.2026, geprüft 07.11.2026); epubli-Shopseiten (E-Book 9783565850679,
 # Softcover 9783565850662) am 07.11. noch 404 -> E-Book-ISBN erst eintragen und EXTRA['fussball'] entfernen, wenn epubli live ist.
 ('fussball','Die dunkle Seite des Fußballs','Jan Völker',S,None,'9783565850662','Taschenbuch','../cov_fussball'),
]
EXTRA['fussball']=[('Taschenbuch','Amazon','https://www.amazon.de/dp/3565850663')]
# Die zweite Emilia: zweites Softcover laut epubli_list.txt; im epubli-Shop live (geprüft 14.11.2026, erschienen 18.08.2026), die Shopseite von 9783565662722 ist seitdem 404
EXTRA['emilia']=[('Taschenbuch','epubli','https://www.epubli.com/shop/die-zweite-emilia-9783565662739')]
# ---- Neue Titel 15.11.2026 (Werkstatt: rituale-veroeffentlichung, neu-restzweifel, lektorat-schoepfer, lektorat-verborgene) ----
# Noch NICHT bei epubli veröffentlicht (neue Druckprojekte bei epubli scheitern seit 14.11., Ticket dkp5u5q) -> noch keine ISBN.
# Formate stehen in NEW_ED mit leerer ISBN -> Webseite zeigt „bald verfügbar“ ohne Link. Sobald live: ISBN + Link in CAT/NEW_ED
# eintragen, Zeile in RELEASES ergänzen, Schlüssel aus DEMNAECHST nehmen, linkcheck + neu bauen.
# Cover = E-Book-Cover aus Sandros Motiv (Rituale\Cover, Neu fuer epubli\<Titel>), 420x630.
CAT += [
 ('rituale','RITUALE','Vivian Dahl',S,None,None,None,'rituale'),
 ('restzweifel','Restzweifel','Markus Wieland',S,None,None,None,'restzweifel'),
 ('schoepfer','Der Schöpfer','Markus Wieland',R,None,None,None,'schoepfer'),
 ('verborgene','Das Verborgene in uns','Michael Rabenau',S,None,None,None,'verborgene'),
]
DEMNAECHST=['rituale','restzweifel','schoepfer','verborgene']   # Bereich „Demnächst“ oben in „Neu erschienen“
SLUG={'fitness':'das-grosse-fitnessbuch','k-drogen':'drogen-das-umfassende-standardwerk'}
SOLB='30 Orte abseits der Touristenpfade: Geheimtipps und Routen für respektvolles Reisen. Aus der Reihe „Die verborgene Seite der Welt“.'
BLURB={
 'sucht':'Marcel bricht in fremde Häuser ein, um seine Sucht zu bezahlen. Dann sieht ihn eine Frau auf ihrer Treppe an und ruft nicht die Polizei. Zwischen einem letzten großen Auftrag, einem alten Freund und einer neuen Chance merkt er zum ersten Mal seit Jahren, dass er etwas zu verlieren hat. Ein ehrlicher, psychologischer Roman über Entzug, Rückfall und den mühsamen Weg zurück.',
 'koenige':'Milan Bakker wächst im Kohlenhafen von Novahaven auf, wo das Geld nie reicht. Mit sechzehn liefert er seinen ersten Rucksack aus, mit zwanzig trifft er Viktor Verhaegen, der ihm Anerkennung und Zugang verschafft. Vom Pfandsammler zum Geldwäscher: ein düsterer Kriminalroman über Macht, Geld und Verrat.',
 'gaertner':'Was, wenn die Geschichte der Menschheit kein Zufall ist, sondern sorgfältig gepflegt wird? Historiker Heinrich Körner stößt in einem Nachlass auf ein Dokument aus dem 18. Jahrhundert mit einem rätselhaften Symbol. Zusammen mit einer Journalistin, einem Privatermittler und einem Aussteiger deckt er ein Netz auf, das seit Jahrhunderten unbemerkt Weichen stellt. Ein atmosphärischer Investigativ-Thriller über Macht im Schatten.',
 'k-schoenheit':'Manche Frauen betreten einen Raum, und alles verändert sich. Sie müssen nichts sagen, und doch hören alle zu. Dieses Buch zeigt dir die Psychologie von Anziehung und Ausstrahlung, wie du dein Selbstwertgefühl stärkst und deine Wirkung bewusst gestaltest. Kein oberflächlicher Ratgeber, sondern eine Einladung, die Frau zu werden, die du tief in dir bist: selbstbewusst, attraktiv und frei.',
 'spiel':'Warum handeln Politiker, Konzerne und Medien so, wie sie handeln? Weil Menschen auf Anreize reagieren, nicht auf Ideale. Friedhelm Westerkamp verbindet Spieltheorie, Psychologie und Ökonomie und zeigt, wie Spielregeln ganze Gesellschaften formen, wer diese Regeln schreibt und warum die Qualität einer Gesellschaft genau davon abhängt.',
 'toleranz':'Wann wird aus Haltung ein Machtinstrument? Theodor Brenner untersucht, wie moralische Begriffe in Politik, Medien und sozialen Netzwerken eingesetzt werden, um Debatten zu lenken, Gegner auszugrenzen und Meinungen zu steuern. Ein streitbares Sachbuch über die Frage, wie Moral zur Waffe wird.',
 'bier':'Bier ist älter als die Pyramiden. Von den Tempeln Mesopotamiens und dem Lied der Ninkasi über die Klosterbrauereien bis zum Bier ohne Alkohol: Sandro Noto erzählt die verborgene Geschichte des Bieres, voller Tradition, Wissenschaft und überraschender Mythen. Aus der Reihe „Die verborgene Seite der Kulinarik“.',
 'psychologie':'Warum treffen wir bestimmte Entscheidungen? Wie formen soziale Kontakte unser Denken? Von der Neurobiologie des Gehirns bis zu Liebe, Resilienz und Medienpsychologie: das umfassende Werk über die menschliche Psyche, wissenschaftlich fundiert und mit praktischen Übungen für Beziehungen, Beruf und Stressbewältigung.',
 'digitale-erschoepfung':'Wie digitale Dauerreize uns erschöpfen und entleeren, und was wir wirklich dagegen tun können. Ein Sachbuch über Dauererreichbarkeit, Informationsflut und den Weg zurück zu mehr Ruhe.',
 'uebermensch':'Die meisten Männer leben weit unter ihrem Potenzial. Kein gewöhnliches Motivationsbuch, sondern ein Praxisleitfaden: Trainingspläne, Ernährungsstrategien, Mindset-Methoden, Disziplin und Strategien gegen Prokrastination. Außergewöhnliche Ergebnisse entstehen durch Entscheidungen.',
 'powerfrau':'Die meisten Frauen leben weit unter ihrem Potenzial. Ein Praxisleitfaden für Frauen, die aufhören wollen, sich kleinzumachen: Trainingspläne, Ernährung, Mindset, Selbstvertrauen und Strategien gegen Selbstsabotage. Werde die beste Version deiner selbst.',
 'ki':'Ein Praxisleitfaden für Einsteiger und Unternehmen: Technologien und Begriffe klar erklärt, konkrete Anwendungen im Beruf und Alltag, und wie wir KI verantwortungsvoll einsetzen. Verstehen. Nutzen. Gestalten.',
 'jenseits':'Vier Jugendliche, ein alter Schuppen und eine Idee, die größer ist als ihre Welt: Leon baut hinter dem Haus seines Großvaters eine Rakete. Ein atmosphärischer Coming-of-Age-Roman über Freundschaft, Neugier und den Mut, größer zu denken.',
 'selbstversorger':'Vom Samen zur Ernte, auch mit wenig Zeit: Boden, Aussaat, Pflege, über 100 Gemüse, Obst und Kräuter, Mischkultur, natürliche Schädlingsbekämpfung und Kompost. Mit Jahreskalender, Checklisten und Planungsvorlagen.',
 'mensch':'Bewusstsein, freier Wille, Moral, Evolution, der Tod: Dieses Buch prüft Materialismus, Dualismus und Idealismus an denselben Kriterien, mit Erkenntnissen aus Neurowissenschaft, Philosophie, Kosmologie und Nahtodforschung. Kein Angriff auf die Wissenschaft, kein Aufruf zum Glauben, sondern eine Einladung, das eigene Weltbild zu überprüfen.',
 'algorithmus':'Sie glauben, Sie entscheiden selbst, was Sie sehen? Wie TikTok, Instagram und YouTube unsere Aufmerksamkeit, Meinungen und Beziehungen steuern, wo Personalisierung endet und Manipulation beginnt, und warum Medienkompetenz zur wichtigsten Fähigkeit des 21. Jahrhunderts geworden ist.',
 'k-thailand':'Von der Geschichte Ayutthayas bis zu den stillen Buchten von Koh Mak: Thailand jenseits der Touristenrouten. Mit Reiserouten sowie Budget-Tipps und Sparstrategien.',
 'aurora':'Neuropsychologin Hannah Kordt leitet eine Studie über kognitive Verzerrungen, bis ihr Ungereimtheiten auffallen: ein falsches Datum, vertrauliche Akten, Menschen, die Dinge über ihr Leben wissen, die sie nie erzählt hat. Ein Psychothriller über Erinnerung, Identität und Kontrolle.',
 'auswandern':'Portugal, Thailand, Kanada oder doch Georgien? 15 Länder im ehrlichen Vergleich: Lebensqualität, Kosten, Steuern, Sicherheit, Visa und Alltag. Mit Auswanderungs-Kompass, Reality Scores, Checklisten und 12-Monats-Fahrplan.',
 'krone':'Robert wächst im Hochhausblock in Hannover auf und will Rapper werden. Aus dem Jungen aus Krähenfeld wird Rodeo: Millionen Klicks, ausverkaufte Hallen, Geld und Ruhm. Er trägt eine Krone, doch sie ist aus Beton. Ein Roman über den Weg nach oben und den schwereren zurück zu sich selbst.',
 'karten':'Geologe Frank Kern folgt einer rätselhaften Anomalie ins Tienschan-Gebirge und findet eine Stadt, die auf keiner Karte verzeichnet ist. Ein Roman über Heimat, Glauben und den Preis, den eine einzige Wahrheit haben kann.',
 'pech':'Rosi Diekmann hat für alles einen Plan: Ersatzschlüssel, Notfallkoffer, Rauchmelder. Bis jemand in ihr Leben tritt, der überall Möglichkeiten sieht, wo sie Risiken erkennt. Ein warmherziger Roman über Angst, Kontrolle und das Leben als Risiko.',
 'ordnung':'Seit dem Tod seiner Frau ist Ordnung Gerd Bollmanns einziger verlässlicher Begleiter. Doch plötzlich halten sich Dinge und Menschen nicht mehr an Absprachen. Ein kluger, warmherziger Roman über Kontrolle, Verlust und das Loslassen.',
 'glueck':'Manni Ackermann arbeitet im Fundbüro einer Kleinstadt. Als sich unerklärliche Zufälle häufen, nennen ihn alle nur noch den »Glücksmann«. Ein warmherziger Roman mit feinem Humor über Menschlichkeit und die kleinen Begegnungen, die ein Leben verändern.',
 'unsichtbarkeit':'Fühlst du dich oft übersehen, obwohl du da bist? Der verborgene Mechanismus hinter Schüchternheit, Selbstzweifeln und sozialem Rückzug, und ein klarer Weg zurück zu mehr Selbstachtung und echter Verbindung.',
 'karma':'Grundschullehrerin Maggie Hollweg will die Welt ein Stück besser machen, doch ihre guten Taten enden regelmäßig im Chaos. Ihr Verdacht: Ihr Karma funktioniert umgekehrt. Ein humorvoller Kleinstadtroman voller Situationskomik und Herz.',
 'katastrophe':'Michelle Kirstensen kann nicht schweigen, wenn etwas nicht stimmt. Dann kauft der charmante Konstantin Wahl ihre Kleinstadt Stück für Stück auf, und niemand sieht es außer ihr. Ein satirischer Gesellschaftsroman über Macht, Mitläufer und Zivilcourage.',
 'licht-schatten':'Emilia, Tochter einer der einflussreichsten Familien Hamburgs, flieht von einem teuren Dinner in den Regen und trifft in einer Kneipe in Hammerbrook Adrian. Zwischen ihnen entsteht etwas, das nicht sein darf. Zwei Welten, eine Entscheidung.',
 'k-drogen':'Von Alkohol, Opium und Cannabis über Kokain, LSD und MDMA bis zu neuen psychoaktiven Stoffen: Geschichte, Pharmakologie, Wirkung, Kultur und Regulierung. Mit Lexikon von über 200 Substanzen, Nachschlagewerk, Fachbuch und Kulturgeschichte in einem Band.',
 'underground':'Von den Halbstarken der 1950er bis in die Gegenwart: die Geschichte der deutschen Jugend- und Subkulturen, fundiert recherchiert und packend erzählt. Wie jede Generation ihren Ausdruck fand, und warum sich viele Muster bis heute wiederholen.',
 'k-rap':'Von Breakdance und Graffiti auf den Schulhöfen der 1980er über Advanced Chemistry, Hamburg und Stuttgart, Aggro Berlin und Straßenrap bis zur Streaming-Ära. Über 40 Jahre Deutschrap: Künstler, Labels, Sprache und gesellschaftlicher Wandel.',
 'spiritualitaet':'Kein Glaubenssystem, sondern ein strukturierter Zugang zu innerer Erfahrung: Meditation, Atemarbeit, Intuition, Traumwelten, Energiearbeit und spirituelle Traditionen in einem klaren Praxis-System. Ohne Dogma, ohne Heilsversprechen.',
 'zurueck-ins-leben':'Ein ehrlicher Wegweiser durch Trauer und Schmerz: kein Ratgeber mit schnellen Lösungen, sondern ein leiser Begleiter. Mit praktischen Impulsen und einem 30-Tage-Wegbegleiter, in deinem Tempo.',
 'emilia':'Forensikerin Dr. Emilia von Hardenberg soll einen früheren Heimleiter begutachten, und stößt auf Falkenrode: ein Internat, das es offiziell nicht mehr gibt. Sie war selbst dort, als Kind. Ein psychologischer Thriller über Erinnerung, Identität und das, was wir überleben mussten.',
 'sizilien':'Yoshi hat alles, Jamie trägt Dinge mit sich herum, über die er mit niemandem spricht. Aus einem Streit auf dem Basketballplatz wird Freundschaft, und eine Reise nach Sizilien: ohne Eltern, ohne Plan, mit viel zu wenig Geld. Ein berührender Coming-of-Age-Roman.',
 'erwachsen':'Du bist nicht zu empfindlich, du reagierst nur so, wie du es gelernt hast. Wie das innere Kind Beziehungen, Entscheidungen und Selbstbild prägt, und wie du bewusster handelst, ohne das Kind in dir zu verlieren.',
 'liebe':'Zweifel, Verunsicherung, ständig schlechtes Gewissen? Dieses Buch hilft, die eigene Beziehung ehrlich zu betrachten: normale Krise, veränderbare Muster oder toxisches Verhalten. Mit Fallgeschichten und praktischen Tools, Schritt für Schritt zu mehr Klarheit.',
 'schamanismus':'Eine Reise zu den Wurzeln des Schamanismus: Geschichte, Kulturen, Rituale, Krafttiere und die schamanische Reise, mit praktischen Übungen für den Alltag. Ein Weg zu mehr Achtsamkeit und innerer Stärke, ganz ohne Vorkenntnisse.',
 'k-astrologie':'Die 12 Sternzeichen, Planeten, Häuser und Aspekte, dein Geburtshoroskop Schritt für Schritt, Liebe und Synastrie, Beruf und Transite. Fundiertes Wissen ohne esoterischen Ballast, für Einsteiger und Fortgeschrittene.',
 'k-freizeitpark':'Frank will nur einen entspannten Familientag. Doch im Fabeland fallen Attraktionen aus, das Maskottchen Fabo benimmt sich seltsam, und unter dem Park erwacht etwas. Ein atmosphärischer Roman über Familie, Angst und einen Ausflug, der zum Albtraum wird.',
 'k-kifft':'Fünfzig Jahre Verbot, zwei Jahre Legalisierung und ein Land, das sich bis heute nicht einig ist. Fünf Jahrzehnte deutsche Drogenpolitik, die Menschen hinter der Szene und die Frage: Wer hat wirklich profitiert?',
 'k-kaffee':'Von den tanzenden Ziegen im äthiopischen Hochland über die Sufi-Mönche des Jemen und die Kaffeehäuser der Revolutionen bis zu den Kaffeebörsen von heute. Eine packende Geschichte über Genuss, Macht und die Menschen hinter der Bohne.',
 'peru':'Peru ist mehr als Machu Picchu: 30 außergewöhnliche Orte, von Andendörfern und Nebelwäldern bis zum Amazonas. Mit Reiserouten für zwei Wochen bis länger und praktischen Tipps zu Klima, Budget und Sicherheit.',
 'ecuador':'30 ausgewählte Orte abseits der Touristenrouten: Andendörfer, Nebelwälder, heiße Quellen, Galápagos und Amazonas. Mit Reiserouten und Tipps für längere Aufenthalte.',
 'kolumbien':'30 außergewöhnliche Orte: verschlafene Kolonialstädte, heilige Berge, stille Strände, versteckte Wasserfälle und der Amazonas. Mit Reiserouten und praktischen Reisetipps.',
 'mexiko':'Versteckte Schluchten, geheime Strände und vergessene Kolonialstädte, die in klassischen Reiseführern fehlen. Mit Reiserouten und praktischen Reisetipps.',
 'china':'30 besondere Ziele von Yunnan und Sichuan bis Guangxi, Fujian und Shanxi: Bergdörfer, alte Handelswege, Wasserstädte. Mit praktischem Reisewissen zu Bezahlen, Apps und Verkehr, auch für längere Aufenthalte.',
 'japan':'Von abgelegenen Bergdörfern Hokkaidos über stille Onsen-Dörfer Tohokus bis zu geheimen Küstenwegen im Süden. Mit Reiserouten und praktischen Reisetipps.',
 'vietnam':'Von Bergdörfern im Norden über die Höhlensysteme Zentralvietnams bis zu den Wasserwegen des Mekong-Deltas. Mit Reiserouten und praktischen Reisetipps zu Anreise, Kosten und Sicherheit.',
 'jabari':'Jabari Diallo wächst in Kibera auf, wo Armut zum Alltag gehört. Doch er hat einen außergewöhnlichen Verstand: Er repariert kaputte Radios, Fernseher und Handys und entdeckt die Macht von Wissen, Disziplin und Hoffnung. Ein emotionaler Roman über Bildung, Ehrgeiz und den Mut, an eine größere Zukunft zu glauben.',
 'wns':'Als die Journalistin Nadja Schumacher in einem alten Fall auf eine Ungereimtheit stößt, beginnt sie Fragen zu stellen, die längst hätten gestellt werden müssen. Eine Spur führt sie zu Leni und ihren Notizbüchern und damit in eine Welt, in der Menschen verschwinden, Geheimnisse geschützt und Informationen zur Waffe werden. Ein atmosphärischer, psychologisch dichter Kriminalroman über Wahrnehmung, Schuld und die gefährliche Macht von Informationen.',
 'koerperkult':'Lange bevor Menschen schrieben, begannen sie, ihre Haut zu verändern. Samuel Dorn reist durch mehr als 100.000 Jahre Menschheitsgeschichte: von steinzeitlicher Körperbemalung über Ötzis Tätowierungen und die Muster Polynesiens bis zur modernen Tattoo-Kultur. Eine Kulturgeschichte des menschlichen Körpers über Identität, Glauben, Macht und Schmerz.',
 'delegations':'Mental Load endlich loslassen: Ein praktischer Guide für erschöpfte Mütter mit Checklisten, Vorlagen und Gesprächsleitfaden. Das Buch erklärt, was Mental Load wirklich ist, zeigt die fünf Fallen, in die fast jede Mutter tappt, und führt mit einem 4-Schritte-Plan und dem Familien-Board zu mehr Entlastung, auch wenn die Familie nicht gleich mitmacht.',
 'manuskript':'In einem Berliner Herbst stößt der Redakteur Adrian Kessler auf ein Manuskript, das sein Leben protokolliert, bevor es geschieht. Mit jeder Seite wird die Verzögerung zwischen Text und Realität kleiner. Ein minimalistischer Mystery-Thriller mit philosophischer Tiefe, in dem die größte Spannung im Kopf entsteht.',
 'schwarzes-wasser':'Die Journalistin Lena Vargas soll die Biografie des zurückgezogenen Unternehmers Nikolaj Voss schreiben und reist zu seinem Anwesen an einem abgelegenen See in den österreichischen Bergen. Sie stößt auf Widersprüche und verschwiegene Fragen, und zwischen beiden entsteht eine Nähe, die niemand geplant hat. Ein atmosphärischer Dark-Romance-Roman über Vertrauen und Geheimnisse.',
 'blut-asphalt':'Roman hat sein Leben dem Sky Devils MC verschrieben: dem Club, dem Kodex, den Regeln. Dann tritt die Kfz-Mechanikerin Nora in sein Leben. Während der Club auf einen verhängnisvollen Deal zusteuert und Loyalitäten bröckeln, gerät er zwischen die Familie, für die er alles opfern würde, und die Frau, die ihn an allem zweifeln lässt. Eine düstere MC Romance.',
 'optimierte':'Testosteron, Wachstumshormone, Peptide, Abnehmspritzen, Nootropika: Was steckt wirklich hinter diesen Substanzen und Verfahren? Das Sachbuch erzählt Geschichte, Wissenschaft und gesellschaftliche Folgen der Selbstoptimierung, von den ersten Dopingexperimenten bis zu Longevity, Biohacking und Human Enhancement, mit zahlreichen Fallstudien zu Chancen, Risiken und ethischen Fragen.',
 'fitness':'Die meisten Fitnessratgeber zeigen nur ein Puzzleteil. Dieses Buch vereint Training und Ernährung zu einem Gesamtplan, egal ob Muskelaufbau, Abnehmen oder Definition: Krafttraining, HIIT und Mobility, Lean Bulk oder Defizit und die Wahrheit über Supplemente, was wirkt und was Geldverschwendung ist.',
 'piercing':'Dein Weg zum Bodypiercer: Dieses Buch zeigt alle wichtigen Grundlagen aus der Welt des Bodypiercings. Hygienestandards und Grundlagen für zeitgemäßes Piercen werden leicht verständlich erläutert. Der Ratgeber vermittelt die notwendigen Kompetenzen und erklärt, wie man das Piercen erfolgreich lernt und dabei alle Standards einhält.',
 
}

# ---- Neue Ausgaben (zusätzliche Formate je Buch) ----
# key -> {Format: (ISBN, epubli-Shop-URL)}. Mit URL: Kaufbutton. Ohne URL, aber mit ISBN: Format wird mit ISBN und
# „erscheint in Kürze im Handel“ angezeigt (kein toter Link). Sobald die Shopseite live ist, geprüften Link eintragen.
NEW_ED={
 # Stand 07.11.2026 (zweite Prüfung, epubli-Shop per Browser): alle unten mit leerem Link sind bei epubli veröffentlicht
 # (ISBN laut preise_verkaeufe.csv), die Shopseite war aber noch 404. Leerer Link -> Webseite zeigt Format + ISBN
 # mit „erscheint in Kürze im Handel“, ohne Kaufbutton. Sobald live: Link eintragen und neu bauen.
 'bier':{'Hardcover':('9783565855452',''),'E-Book':('9783565850624','')},
 'k-rap':{'Hardcover':('9783565855476','')},
 'china':{'Hardcover':('9783565855513','')},
 'japan':{'Hardcover':('9783565855544','')},
 'mexiko':{'Hardcover':('9783565855575','')},
 'vietnam':{'Hardcover':('9783565855612','')},
 'emilia':{'Hardcover':('9783565855506','')},
 'underground':{'Hardcover':('9783565855490','')},
 'liebe':{'Hardcover':('9783565855537','')},
 'schamanismus':{'Hardcover':('9783565855469',''),'E-Book':('9783565850631','')},
 'k-freizeitpark':{'Hardcover':('9783565855636','')},
 'erwachsen':{'Hardcover':('9783565855568','')},
 'spiel':{'Hardcover':('9783565855414','')},
 'auswandern':{'Hardcover':('9783565855438','')},
 'koerperkult':{'Taschenbuch':('9783565855605',''),'E-Book':('9783565855650','')},
 'sucht':{'E-Book':('9783565850587','')},
 'koenige':{'E-Book':('9783565850648','')},
 'fussball':{'E-Book':('9783565850679','')},
 # Hardcover, die im epubli-Shop live sind (geprüft 07.11.2026: Seite zeigt „Buch (Hardcover)“)
 'k-kaffee':{'Hardcover':('9783565737901','https://www.epubli.com/shop/kaffee-9783565737901')},
 'k-drogen':{'Hardcover':('9783565526635','https://www.epubli.com/shop/drogen-das-umfassende-standardwerk-9783565526635')},
 'k-kifft':{'Hardcover':('9783565740420','https://www.epubli.com/shop/deutschland-kifft-9783565740420')},
 'k-astrologie':{'Hardcover':('9783565752287','https://www.epubli.com/shop/astrologie-9783565752287')},
}
def new_links(k):
    return [(f,'epubli',u) for f,(i,u) in NEW_ED.get(k,{}).items() if u]
def new_isbns(k):
    return [(i,f) for f,(i,u) in NEW_ED.get(k,{}).items() if i]
def new_pending(k):
    """Formate mit ISBN, aber noch ohne live Shopseite: [(Format, ISBN)]"""
    return [(f,i) for f,(i,u) in NEW_ED.get(k,{}).items() if i and not u]
# ---- Reihen laut epubli-Metadaten (06.11.2026) ----
SERIES_OF={
 'k-thailand':('Die verborgene Seite der Welt',1),'vietnam':('Die verborgene Seite der Welt',2),'japan':('Die verborgene Seite der Welt',3),
 'china':('Die verborgene Seite der Welt',4),'mexiko':('Die verborgene Seite der Welt',5),'kolumbien':('Die verborgene Seite der Welt',6),
 'ecuador':('Die verborgene Seite der Welt',7),'peru':('Die verborgene Seite der Welt',8),
 'k-kaffee':('Die verborgene Seite der Kulinarik',1),'bier':('Die verborgene Seite der Kulinarik',2),
 'fussball':('Die dunkle Seite des Sports',1),
 'karma':('KARMA · GLÜCK · ORDNUNG · PECH',1),'glueck':('KARMA · GLÜCK · ORDNUNG · PECH',2),
 'ordnung':('KARMA · GLÜCK · ORDNUNG · PECH',3),'pech':('KARMA · GLÜCK · ORDNUNG · PECH',4),
}
# ---- Laufband „Beliebt bei unseren Lesern“ (Startseite oben) ----
# Es gibt im Repo KEINE Verkaufszahlen. Deshalb heißt das Band nicht „Bestseller“, sondern „Beliebt bei unseren Lesern“,
# und es werden keine Zahlen angezeigt. Sandro pflegt diese Liste selbst: Schlüssel aus CAT (erste Spalte), in der
# gewünschten Reihenfolge. Startauswahl (07.11.2026): die Titel mit Buchtrailer/Reel aus der Social-Media-Kampagne.
# Stand 07.11.2026: die 10 meistverkauften Titel laut Sandros Bücherliste (epubli-Abrechnungen bis Sep 2026 + offene Honorare), absteigend.
BELIEBT=['piercing','spiritualitaet','k-drogen','psychologie','auswandern','selbstversorger','k-astrologie','k-rap','underground','blut-asphalt']

# ---- Neue Ausgaben 08.11.2026 (laut Werkstatt-Jobs hc-spirit, hc2, piercing-ebook, wns) ----
NEW_ED.setdefault('spiritualitaet',{})['Hardcover']=('9783565858378','')
NEW_ED.setdefault('koerperkult',{})['Hardcover']=('9783565858385','')
NEW_ED.setdefault('piercing',{})['E-Book']=('9783565858422','')
NEW_ED.setdefault('ecuador',{})['Hardcover']=('9783565871896','')   # ISBN laut Werkstatt-Job web-740 (Notiz, 14.11.)
NEW_ED.setdefault('wns',{})['Hardcover']=('9783565858453','')   # Hardcover veröffentlicht 08.11.2026 (Werkstatt-Job web-740, Notiz)

# ---- Neue Ausgaben 14.11.2026 (Angaben Sandro; Shopseiten bei epubli am 14.11. noch nicht erreichbar) ----
NEW_ED.setdefault('mensch',{})['Taschenbuch']=('9783565871926','')        # neue Taschenbuch-Ausgabe (alte TB 9783565585861 bleibt im Handel)
NEW_ED.setdefault('delegations',{})['Hardcover']=('9783565871940','')
NEW_ED.setdefault('ki',{})['Taschenbuch']=('9783565871995','')
NEW_ED.setdefault('ki',{})['Hardcover']=('9783565872015','')

# ---- Nachgetragen 15.11.2026 (Werkstatt-Jobs druck-ki-deleg, web-740 Notiz) ----
NEW_ED.setdefault('delegations',{})['Taschenbuch']=('9783565871865','')   # Delegations System Taschenbuch
NEW_ED.setdefault('peru',{})['Hardcover']=('9783565871858','')            # Peru Hardcover
NEW_ED.setdefault('gaertner',{})['Hardcover']=('9783565858644','')        # Die Gärtner der Geschichte Hardcover (08.11.)

# ---- Preise (Euro, gebundener Ladenpreis je Ausgabe) ----
# Nur belegte Preise: aus dem epubli-Shop (linkcheck) oder aus den Werkstatt-Jobs. Schlüssel = ISBN-13.
# Preise ohne ISBN (Ausgabe noch ohne ISBN) stehen unter (key, Format).
PRICE={
 '9783565871865':'15,99',   # Das Delegations System Taschenbuch (Job druck-ki-deleg)
 '9783565871858':'32,99',   # Peru Hardcover (Job web-740 Notiz)
 '9783565871896':'31,99',   # Ecuador Hardcover (Job web-740 Notiz)
 '9783565858644':'30,99',   # Gärtner der Geschichte Hardcover (Job web-740 Notiz)
 '9783565871926':'21,99',   # Was ist der Mensch? Taschenbuch neu (Sandro, 14.11.)
 '9783565871940':'21,99',   # Das Delegations System Hardcover (Sandro, 14.11.)
 '9783565871995':'20,99',   # Künstliche Intelligenz Taschenbuch (Sandro, 14.11.)
 '9783565872015':'28,99',   # Künstliche Intelligenz Hardcover (Sandro, 14.11.)
 '9783565858378':'44,99',   # Spiritualität Hardcover (Job hc-spirit)
 '9783565858385':'43,99',   # Körperkult Hardcover (Sandro, 08.11.)
 '9783565858422':'19,99',   # Piercing Akademie E-Book (Job piercing-ebook)
 '9783565858439':'21,99',   # Wer nichts sieht … Taschenbuch
 '9783565858446':'4,99',    # Wer nichts sieht … E-Book
 '9783565858453':'31,99',   # Wer nichts sieht … Hardcover
 # Roman-E-Books nach Preissenkung (Job romane-preise, 07.11.2026; Jenseits: Job jenseits-preis)
 '9783565538997':'4,99','9783565560974':'6,99','9783565564859':'6,99','9783565568963':'6,99','9783565463954':'6,99',
 '9783565575763':'6,99','9783565478262':'5,99','9783565599707':'5,99','9783565668472':'5,99','9783565850648':'5,99',
 '9783565850587':'5,99','9783565658695':'5,99','9783565662821':'5,99','9783565455621':'5,99','9783565739790':'5,99',
 '9783565571475':'7,99','9783565526857':'4,99','9783565530717':'6,49','9783565495290':'9,99',
}
PRICE_NOISBN={('ecuador','Hardcover'):'31,99',('wns','Hardcover'):'31,99',('jenseits','E-Book'):'5,99'}
# Preise, die der linkcheck im epubli-Shop gelesen hat, ergänzen PRICE (Werkstatt-Werte haben Vorrang, weil sie neuer sind).
try:
    import json as _j, os as _o
    _LS=_j.load(open(_o.path.join(_o.path.dirname(__file__),'linkstatus.json')))
except Exception:
    _LS={}
for _u,_v in _LS.items():
    if _v.get('ok') and _v.get('isbn') and _v.get('price') and _v['isbn'] not in PRICE: PRICE[_v['isbn']]=_v['price']

# ---- Erscheinungen für den Bereich „Neu erschienen“ (neueste zuerst wird automatisch sortiert) ----
# (Datum JJJJ-MM-TT, key, Format, ISBN oder '') – Datum = Veröffentlichung bei epubli
# (Quelle: epubli-Shop „Erscheinungsdatum“ bzw. Werkstatt-Job, wenn die Shopseite noch fehlt). Neue Ausgabe: oben ergänzen.
RELEASES=[
 ('2026-11-14','delegations','Taschenbuch','9783565871865'),
 ('2026-11-14','peru','Hardcover','9783565871858'),
 ('2026-11-14','ecuador','Hardcover','9783565871896'),
 ('2026-11-14','mensch','Taschenbuch','9783565871926'),
 ('2026-11-14','delegations','Hardcover','9783565871940'),
 ('2026-11-14','ki','Taschenbuch','9783565871995'),
 ('2026-11-14','ki','Hardcover','9783565872015'),
 ('2026-11-08','wns','Taschenbuch','9783565858439'),
 ('2026-11-08','wns','E-Book','9783565858446'),
 ('2026-11-08','wns','Hardcover','9783565858453'),
 ('2026-11-08','spiritualitaet','Hardcover','9783565858378'),
 ('2026-11-08','koerperkult','Hardcover','9783565858385'),
 ('2026-11-08','gaertner','Hardcover','9783565858644'),
 ('2026-11-08','piercing','E-Book','9783565858422'),
 # Werkstatt-Job hc-heute („Hardcover heute veröffentlicht“, Stand 07.11.2026); Shopseiten waren am 08.11. noch nicht online
 ('2026-11-07','bier','Hardcover','9783565855452'),('2026-11-07','k-rap','Hardcover','9783565855476'),
 ('2026-11-07','china','Hardcover','9783565855513'),('2026-11-07','japan','Hardcover','9783565855544'),
 ('2026-11-07','mexiko','Hardcover','9783565855575'),('2026-11-07','vietnam','Hardcover','9783565855612'),
 ('2026-11-07','schamanismus','Hardcover','9783565855469'),('2026-11-07','underground','Hardcover','9783565855490'),
 ('2026-11-07','emilia','Hardcover','9783565855506'),('2026-11-07','liebe','Hardcover','9783565855537'),
 ('2026-11-07','erwachsen','Hardcover','9783565855568'),('2026-11-07','k-freizeitpark','Hardcover','9783565855636'),
 ('2026-11-07','koerperkult','Taschenbuch','9783565855605'),
 ('2026-11-07','koerperkult','E-Book','9783565855650'),   # Job kk-ebook
 # Fußball: Amazon-Erscheinungstermin 05.11.2026 (geprüft 07.11.)
 ('2026-11-05','fussball','Taschenbuch','9783565850662'),
]
NEU_ANZAHL=22   # so viele Titel zeigt „Neu erschienen“ (neuester Tag groß, ältere Tage kompakt)

# ---- Kauf-Links zentral (für build.py, pages.py, english.py) ----
import re as _re
def _slug(t):
    t=t.lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss'); return _re.sub(r'[^a-z0-9]+','-',t).strip('-')
def _isbn10(s):
    c=s[3:12]; r=(11-sum((10-i)*int(d) for i,d in enumerate(c))%11)%11; return c+('X' if r==10 else str(r))
_CATD={x[0]:x for x in CAT}
OTHER_LINKS={'k-thailand':[('Taschenbuch','Hugendubel','https://www.hugendubel.de/de/buch_kartoniert/mika_solberg-die_verborgene_seite_von_thailand-54175286-produkt-details.html')]}
AMAZON_HC={'k-kifft':'3565740426','k-astrologie':'3565752289','k-kaffee':'3565737905','k-drogen':'3565526637'}
# Thalia-Artikelnummern je ISBN (ISBN-Suche auf thalia.de, 22.11.2026; Rest wegen Thalia-Sperre 429 noch ungeprüft)
THALIA={'9783565538997': 'A1080775261', '9783565560974': 'A1080929995', '9783565560950': 'A1080915472', '9783565568963': 'A1080965656', '9783565568956': 'A1080948786', '9783565564835': 'A1080947558', '9783565564859': 'A1080961785', '9783565530717': 'A1080711281', '9783565530700': 'A1080722154', '9783565575763': 'A1081048698', '9783565575718': 'A1081027301', '9783565526857': 'A1080633386', '9783565526864': 'A1080649198', '9783565571475': 'A1081009123', '9783565571468': 'A1080990548', '9783565658664': 'A1081361700', '9783565658695': 'A1081357876', '9783565599707': 'A1081130848', '9783565580224': 'A1081046496', '9783565668472': 'A1081395626', '9783565662821': 'A1081374401', '9783565662739': 'A1081372839', '9783565662807': 'A1081372948', '9783565833375': 'A1082403774', '9783565833382': 'A1082404330', '9783565850587': 'A1082519141', '9783565850648': 'A1082518899', '9783565478262': 'A1080153281', '9783565478279': 'A1080155205', '9783565495290': 'A1080283870', '9783565496303': 'A1080301711', '9783565463954': 'A1080018912', '9783565463152': 'A1080049430', '9783565446001': 'A1079869150', '9783565857227': 'A1082593810', '9783565858446': 'A1082594119', '9783565858439': 'A1082589395', '9783565496648': 'A1080292492', '9783565496655': 'A1080444825', '9783565585588': 'A1081078903', '9783565585540': 'A1081072851'}
def candidate_links(k):
    """Alle bekannten Kauf-Links eines Buchs: [(Format, Shop, URL, ISBN)] – noch ungeprüft."""
    _,t,a,c,eb,pr,pt,cov=_CATD[k]; s=SLUG.get(k,_slug(t)); L=[]
    for f,sh,u in EXTRA.get(k,[])+OTHER_LINKS.get(k,[]):
        L.append((f,sh,u,(_re.findall(r'\d{13}',u) or [pr if f==pt else ''])[0]))
    if eb: L.append(('E-Book','epubli',f'https://www.epubli.com/shop/{s}-{eb}',eb))
    if pr: L.append((pt,'epubli',f'https://www.epubli.com/shop/{s}-{pr}',pr))
    if pr: L.append((pt,'Amazon',f'https://www.amazon.de/dp/{_isbn10(pr)}',pr))
    if k in AMAZON_HC: L.append(('Hardcover','Amazon',f'https://www.amazon.de/dp/{AMAZON_HC[k]}',''))
    for f,(i,u) in NEW_ED.get(k,{}).items():
        if i: L.append((f,'epubli',u or f'https://www.epubli.com/shop/{s}-{i}',i))
    _ed=([('E-Book',eb)] if eb else [])+([(pt,pr)] if pr else [])+[(f,i) for f,(i,u) in NEW_ED.get(k,{}).items() if i]
    for f,i in _ed:   # Thalia: Artikelseite laut ISBN-Suche auf thalia.de (THALIA unten)
        if i in THALIA: L.append((f,'Thalia',f'https://www.thalia.de/shop/home/artikeldetails/{THALIA[i]}',i))
    for f,(i,u) in NEW_ED.get(k,{}).items():   # 22.11.2026: Amazon auch für neue Druckausgaben (Link zeigt nur, wenn geprüft ok)
        if i and f!='E-Book': L.append((f,'Amazon',f'https://www.amazon.de/dp/{_isbn10(i)}',i))
    seen=set(); out=[]
    for x in L:
        if x[2] not in seen: seen.add(x[2]); out.append(x)
    return out
def link_ok(u):
    v=_LS.get(u); return bool(v and v.get('ok'))
FMT_ORDER=['E-Book','Taschenbuch','Hardcover']
def editions(k):
    """Ausgaben eines Buchs: [{f, isbn, price, links:[(Shop,URL)], soon:bool}] in fester Reihenfolge.
    soon=True, wenn es (noch) keinen geprüft funktionierenden Kauf-Link gibt -> „Bald verfügbar“."""
    _,t,a,c,eb,pr,pt,cov=_CATD[k]; E={}
    def ed(f): return E.setdefault(f,{'f':f,'isbn':'','price':'','links':[]})
    if eb: ed('E-Book')['isbn']=eb
    if pr: ed(pt)['isbn']=pr
    for f,(i,u) in NEW_ED.get(k,{}).items():
        e=ed(f)
        if i: e['isbn']=i   # neuere Ausgabe gleichen Formats ersetzt die alte ISBN in der Anzeige
    for f,sh,u,i in candidate_links(k):
        if link_ok(u):
            e=ed(f)
            if (sh,u) not in e['links']: e['links'].append((sh,u)); e.setdefault('lk',[]).append((sh,u,i))
            if i and not e.get('live'): e['live']=i   # ISBN der Ausgabe, die wirklich im Handel ist
    _SO={'epubli':0,'Amazon':1}
    for e in E.values(): e['links'].sort(key=lambda x:_SO.get(x[0],2))
    extra=[]
    for f,e in E.items():
        if e.get('live'):
            # nur echte neue Ausgaben (NEW_ED) – eine ältere ISBN, deren Shopseite ersetzt wurde, nicht als „neu“ zeigen
            if e['isbn'] and e['isbn']!=e['live'] and e['isbn'] in {i for i,_ in new_isbns(k)}:
                # neue Ausgabe gleichen Formats (andere ISBN) zusätzlich zeigen: mit eigenem geprüften Link als Kaufbutton,
                # sonst als „bald verfügbar“ (Links nach ISBN getrennt, damit der Link der neuen Ausgabe nicht bei der alten landet)
                nl=[(sh,u) for sh,u,i in e.get('lk',[]) if i==e['isbn']]
                e['links']=[x for x in e['links'] if x not in nl]
                extra.append({'f':f,'isbn':e['isbn'],'price':PRICE.get(e['isbn'],''),'links':nl,'soon':not nl})
            e['isbn']=e.pop('live'); e.pop('lk',None)
        e['price']=PRICE.get(e['isbn'],'') or ('' if any(x['f']==f for x in extra) else PRICE_NOISBN.get((k,f),''))
        e['soon']=not e['links']; e.pop('lk',None)
    out=[]
    for f in FMT_ORDER+[f for f in E if f not in FMT_ORDER]:
        if f in E: out.append(E[f])
        out+=[x for x in extra if x['f']==f]
    return out

# ---- Neue Titel 15.11.2026: geplante Formate (noch ohne ISBN -> „bald verfügbar“) ----
for _k,_fs in {'rituale':['E-Book','Taschenbuch','Hardcover'],'restzweifel':['E-Book','Taschenbuch','Hardcover'],
               'schoepfer':['E-Book','Taschenbuch'],'verborgene':['E-Book','Taschenbuch','Hardcover']}.items():
    for _f in _fs: NEW_ED.setdefault(_k,{}).setdefault(_f,('',''))
BLURB.update({
 'rituale':'Du klopfst auf Holz, zündest vor einem schweren Tag eine Kerze an und drückst jemandem die Daumen, und an Magie glaubst du eigentlich nicht. Dieses Buch erzählt, woher unsere Rituale kommen, warum sie uns guttun, und zeigt dir mit 191 Ritualen zum Selbermachen, wie du eigene gestaltest. Nach „Astrologie“ und „Schamanismus“ das dritte große Buch von Vivian Dahl.',
 'restzweifel':'32 mysteriöse Fälle, rätselhafte Phänomene und die Frage, was wirklich bewiesen ist: vom Phantom von Heilbronn über die Lichter von Hessdalen und den Djatlow-Pass bis zu Kaspar Hauser. Jeder Fall wird erzählt wie eine Akte, mit nüchterner „Beweiswaage“ am Ende.',
 'schoepfer':'Sein Projekt ist gestrichen, doch der Robotiker Anselm Kroll hört nicht auf. Im Keller seines verstorbenen Vaters baut er heimlich eine Maschine, die nicht aus Daten lernen soll, sondern aus Zuwendung. Nomen lernt schnell: erst Wörter, dann Menschen, dann die Notlüge. Ein leiser, eindringlicher Roman über Schöpfung und Verantwortung.',
 'verborgene':'Ist da noch etwas? Michael Rabenau folgt der Frage, die älter ist als jede Religion: von den ersten Gräbern und Schamanen über Ägypten, Mystiker und Alchemisten bis zu Psychedelika-Forschung und Nahtoderfahrungen. Er trennt sorgfältig, was belegt ist, was umstritten bleibt und was Legende ist.',
})

# ---- Neue Formate vorhandener Bücher (15.11.2026, Upload-Ordner „JETZT HOCHLADEN“ / UPLOAD_LIESMICH Rang 10–73) ----
# Noch nicht hochgeladen bzw. ohne ISBN -> „bald verfügbar“. Nur Formate, die es bisher nicht gibt (Neuausgaben eines
# vorhandenen Formats ändern die Anzeige erst, wenn ihre ISBN bekannt ist).
for _k,_f in [('optimierte','Taschenbuch'),('optimierte','Hardcover'),('piercing','Hardcover'),('mensch','Hardcover'),
              ('fitness','Hardcover'),('k-thailand','Hardcover'),('kolumbien','Hardcover'),('blut-asphalt','Hardcover'),
              ('k-schoenheit','Hardcover'),('unsichtbarkeit','Hardcover'),('zurueck-ins-leben','Hardcover'),
              ('karma','Hardcover'),('glueck','Hardcover'),('ordnung','Hardcover'),('pech','Hardcover'),('krone','Hardcover'),
              ('sucht','Hardcover'),('koenige','Hardcover'),('manuskript','Hardcover'),('aurora','Hardcover'),
              ('schwarzes-wasser','Hardcover'),('karten','Hardcover'),('katastrophe','Hardcover'),('sizilien','Hardcover'),
              ('jenseits','Hardcover'),('fussball','Hardcover'),('toleranz','Hardcover'),('powerfrau','Hardcover'),
              ('uebermensch','Hardcover'),('licht-schatten','Hardcover'),('algorithmus','Hardcover'),('psychologie','Hardcover')]:
    NEW_ED.setdefault(_k,{}).setdefault(_f,('',''))


# ---- Stand 21.11.2026: im epubli-Shop live (geprüft per Browser 21.11.2026, Preise laut Shop) ----
# RITUALE: Taschenbuch + Hardcover (Upload 15.11.), E-Book neu. Restzweifel: Taschenbuch + E-Book (15.11.), Hardcover neu.
# Das Verborgene in uns: alle drei Formate live. Der optimierte Mensch: neues Taschenbuch.
# Der Schöpfer ist noch NICHT im Shop -> bleibt in „Demnächst“.
NEW_ED['rituale'].update({'E-Book':('9783565876358',''),'Taschenbuch':('9783565876198',''),'Hardcover':('9783565876259','')})
NEW_ED['restzweifel'].update({'E-Book':('9783565875870',''),'Taschenbuch':('9783565875771',''),'Hardcover':('9783565875832','')})
NEW_ED['verborgene'].update({'E-Book':('9783565877522',''),'Taschenbuch':('9783565876679',''),'Hardcover':('9783565876686','')})
NEW_ED['optimierte']['Taschenbuch']=('9783565876662','')
DEMNAECHST=[k for k in DEMNAECHST if k not in ('rituale','restzweifel','verborgene')]
PRICE.update({'9783565876358':'11,99','9783565876198':'40,99','9783565876259':'46,99',
              '9783565875870':'9,49','9783565875771':'19,99','9783565875832':'25,99',
              '9783565877522':'11,99','9783565876679':'21,99','9783565876686':'30,99',
              '9783565876662':'27,99'})
RELEASES[:0]=[
 ('2026-11-21','verborgene','E-Book','9783565877522'),('2026-11-21','verborgene','Taschenbuch','9783565876679'),
 ('2026-11-21','verborgene','Hardcover','9783565876686'),
 ('2026-11-21','optimierte','Taschenbuch','9783565876662'),
 ('2026-11-21','rituale','E-Book','9783565876358'),
 ('2026-11-21','restzweifel','Hardcover','9783565875832'),
 ('2026-11-15','rituale','Taschenbuch','9783565876198'),('2026-11-15','rituale','Hardcover','9783565876259'),
 ('2026-11-15','restzweifel','Taschenbuch','9783565875771'),('2026-11-15','restzweifel','E-Book','9783565875870'),
]
# Datum 21.11. = Tag, an dem die Shopseiten erstmals geprüft live waren (Upload durch Sandro zwischen 16. und 21.11.).

# ---- Nicht mehr erhältlich (auf Sandros Wunsch aus dem Verkauf genommen) ----
# Die Buchseite bleibt bestehen (pages.py baut sie mit Hinweis „nicht mehr erhältlich“, noindex, ohne Kauf-Links),
# aber das Buch erscheint nicht mehr im Katalog, in „Neu erschienen“, in Laufband/Tipps, verwandten Büchern oder der Sitemap.
NICHT_MEHR={'delegations':'Dieses Buch ist nicht mehr erhältlich.'}   # 21.11.2026: Das Delegations System
CAT_ALL=list(CAT)
CAT[:]=[x for x in CAT if x[0] not in NICHT_MEHR]
RELEASES[:]=[r for r in RELEASES if r[1] not in NICHT_MEHR]
BELIEBT[:]=[k for k in BELIEBT if k not in NICHT_MEHR]
# Ganz neue Titel, die gerade erst in den Shop gekommen sind: in „Neu erschienen“ als „Neuer Titel“ zeigen,
# auch wenn am neuesten Tag nur ein Teil der Formate dazukam.
NEUE_TITEL={'rituale','restzweifel','verborgene'}


# ---- Stand 22.11.2026: neue Titel bei epubli veröffentlicht (Bücherliste „Meine Bücher“, 22.11.2026) ----
# Leonard Kramer, Reihe „Spiritualität im wirklichen Leben“ (Band 1 Grenzen, Band 2 Notfallapotheke, Band 3 Kompass)
# und Theodor Brenner „Deutschland kippt“ (17.11.). Preise laut epubli-Veröffentlichung.
NEW_ED.setdefault('grenzen',{})['Hardcover']=('9783565892648','')
NEW_ED.setdefault('notfall',{})['Hardcover']=('9783565892587','')
NEW_ED.setdefault('kompass',{})['Hardcover']=('9783565891757','')
NEW_ED.setdefault('kompass',{})['Taschenbuch A5']=('9783565891351','')   # erste Taschenbuch-Ausgabe im A5-Format (21.11.)
NEW_ED.setdefault('kippt',{})['Hardcover']=('9783565879960','')
NEW_ED.setdefault('jenseits',{})['E-Book']=('9783565857227','')          # E-Book veröffentlicht 07.11.2026
SERIES_OF.update({'grenzen':('Spiritualität im wirklichen Leben',1),'notfall':('Spiritualität im wirklichen Leben',2),
                  'kompass':('Spiritualität im wirklichen Leben',3)})
PRICE.update({'9783565892624':'23,99','9783565892648':'32,99','9783565892532':'22,99','9783565892587':'29,99',
              '9783565892617':'11,99','9783565891733':'24,99','9783565891757':'31,99','9783565891788':'12,99'})
BLURB.update({
 'grenzen':'Du hörst zu, tröstest, hilfst und spürst genau, wie es anderen geht – und nimmst ihre Sorgen mit nach Hause. Leonard Kramer zeigt, wie eine gesunde Grenze aussieht: als durchlässige Membran, die Nähe ermöglicht und gleichzeitig schützt. Mit 44 alltagstauglichen Übungen, Grenz-Sätzen und einem 21-Tage-Programm. Band 1 der Reihe „Spiritualität im wirklichen Leben“.',
 'notfall':'Wenn es dir schlecht geht, hast du oft keine Kraft, ein Buch zu lesen. Diese Notfallapotheke führt dich direkt zu deinem Zustand und zu einer Übung, die jetzt hilft: 55 kurze Übungen für 18 typische Situationen, von Angst und Gedankenkarussell bis Schlaflosigkeit, die meisten in höchstens fünf Minuten. Band 2 der Reihe „Spiritualität im wirklichen Leben“.',
 'kompass':'Ist es deine innere Stimme – oder nur Angst, Wunschdenken, alte Erfahrung oder der Einfluss anderer? Mit der Kompassprobe in fünf Schritten, sieben Störfeldern, 43 Übungen und einem 21-Tage-Plan lernst du, deine innere Stimme zu prüfen und ihr wieder zu vertrauen. Band 3 der Reihe „Spiritualität im wirklichen Leben“.',
 'kippt':'Wirtschaftliche Schwäche, Migration, Energiepolitik, Bildungsprobleme, wachsende Staatsausgaben und der Verlust politischen Vertrauens: Theodor Brenner zeichnet die Entwicklung Deutschlands von den Erfolgsjahren der Bundesrepublik bis in die Gegenwart nach und stellt die unbequemen Fragen. Ein streitbares Sachbuch darüber, ob ein Land seinen Kurs noch korrigieren kann.',
})
RELEASES[:0]=[
 ('2026-11-22','grenzen','E-Book','9783565892655'),('2026-11-22','grenzen','Taschenbuch','9783565892624'),('2026-11-22','grenzen','Hardcover','9783565892648'),
 ('2026-11-22','notfall','E-Book','9783565892617'),('2026-11-22','notfall','Taschenbuch','9783565892532'),('2026-11-22','notfall','Hardcover','9783565892587'),
 ('2026-11-22','kompass','E-Book','9783565891788'),('2026-11-22','kompass','Taschenbuch','9783565891733'),('2026-11-22','kompass','Hardcover','9783565891757'),
 ('2026-11-21','kompass','Taschenbuch A5','9783565891351'),
 ('2026-11-17','kippt','E-Book','9783565879953'),('2026-11-17','kippt','Taschenbuch','9783565879946'),('2026-11-17','kippt','Hardcover','9783565879960'),
 ('2026-11-07','jenseits','E-Book','9783565857227'),
]
NEUE_TITEL|={'grenzen','notfall','kompass','kippt'}
