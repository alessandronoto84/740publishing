/* 740 Publishing – „Unser Tipp des Tages“ und Zufallsbuch (Startseite DE + EN).
   Daten: <script type="application/json" id="pick-data"> (gebaut von _werkstatt/gen/picks.py).
   Tipp des Tages: Tage seit 1970-01-01 (Datum in Europe/Berlin) modulo Anzahl Bücher -> gleich für alle Besucher.
   Zufallsbuch: bei jedem Aufruf neu, nie gleich dem Tipp des Tages. Keine Cookies, kein Speicher. */
(function () {
  var el = document.getElementById('pick-data');
  if (!el) return;
  var D;
  try { D = JSON.parse(el.textContent); } catch (e) { return; }
  var B = D.books || [], n = B.length;
  if (n < 2) return;

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function render(b) {
    var h = esc(b.href);
    return '<a class="pick-cov" href="' + h + '" tabindex="-1" aria-hidden="true"><img src="' + esc(b.cov) + '" alt="" width="120" height="180" loading="lazy"></a>' +
      '<div class="pick-body"><p class="pick-g">' + esc(b.g) + '</p>' +
      '<h3><a href="' + h + '">' + esc(b.t) + '</a></h3>' +
      '<p class="pick-a">' + esc(b.a) + '</p>' +
      '<p class="pick-d">' + esc(b.d) + '</p>' +
      '<a class="pick-more" href="' + h + '">' + esc(D.more) + '</a></div>';
  }

  // Heutiges Datum in Berlin (YYYY-MM-DD), unabhängig von der Zeitzone des Besuchers
  var now = new Date(), ymd;
  try {
    ymd = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Berlin', year: 'numeric', month: '2-digit', day: '2-digit' }).format(now);
  } catch (e) { ymd = now.toISOString().slice(0, 10); }
  var p = ymd.split('-'), day = Math.floor(Date.UTC(+p[0], +p[1] - 1, +p[2]) / 864e5);
  var ti = ((day % n) + n) % n;

  var dayBox = document.getElementById('pick-day'), rndBox = document.getElementById('pick-rnd');
  if (dayBox) dayBox.innerHTML = render(B[ti]);

  var dt = document.getElementById('pick-date');
  if (dt) {
    try {
      dt.textContent = now.toLocaleDateString(D.lang === 'en' ? 'en-GB' : 'de-DE', { timeZone: 'Europe/Berlin', weekday: 'long', day: 'numeric', month: 'long' });
    } catch (e) { dt.textContent = ymd; }
  }

  var cur = -1;
  function draw() {
    if (!rndBox) return;
    var r, tries = 0;
    do { r = Math.floor(Math.random() * n); tries++; } while ((r === ti || r === cur) && tries < 50);
    cur = r;
    rndBox.innerHTML = render(B[r]);
  }
  draw();
  var again = document.getElementById('pick-again');
  if (again) { again.hidden = false; again.addEventListener('click', draw); }
})();
