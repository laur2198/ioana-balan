# Geometrie randata — `blog.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/blog.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1200 | 1616.50 | 160/64/96/64 | transparent | none |
| `<main>` | 1024 | 1024 | 1560.50 | 160/64/96/64 | transparent | none |
| `<main>` | 768 | 768 | 2182.39 | 160/64/96/64 | transparent | none |
| `<main>` | 390 | 390 | 3219.69 | 128/16/64/16 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 2054px, 1024 → 1998px, 768 → 2671px, 390 → 3825px.

Sectiuni masurate: **4**.

---

## S1 — Sfaturi și Inspirație pentru Evenimente Memorabile

`section` · clase: `mb-20 text-center md:text-left`

Eyebrow: «Articol & Inspirație»

Titlu: «Sfaturi și Inspirație pentru Evenimente Memorabile»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1072 | 239.19 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 896 | 239.19 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 302.39 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 242.38 | 0/0/0/0 | transparent | none |
| **container interior** | 1440 | 1072 | 239.19 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 896 | 239.19 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 302.39 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 358 | 242.38 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-8`) | 1440 | 706.66 | 239.19 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-8`) | 1024 | 589.33 | 239.19 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-8`) | 768 | 418.66 | 302.39 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-8`) | 390 | 358 | 242.38 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Articol & Inspirație | span | 1440 | 184 | 160 | 706.66 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | left |
| Articol & Inspirație | span | 1024 | 64 | 160 | 589.33 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | left |
| Articol & Inspirație | span | 768 | 64 | 160 | 418.66 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | left |
| Articol & Inspirație | span | 390 | 16 | 128 | 358 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Sfaturi și Inspirație pentru Evenimente Memorabi | h1 | 1440 | 184 | 196 | 706.66 | 123.19 | 56 | 61.60 | normal | 400 | #e5e2e1 | left |
| Sfaturi și Inspirație pentru Evenimente Memorabi | h1 | 1024 | 64 | 196 | 589.33 | 123.19 | 56 | 61.60 | normal | 400 | #e5e2e1 | left |
| Sfaturi și Inspirație pentru Evenimente Memorabi | h1 | 768 | 64 | 196 | 418.66 | 158.39 | 48 | 52.80 | normal | 400 | #e5e2e1 | left |
| Sfaturi și Inspirație pentru Evenimente Memorabi | h1 | 390 | 16 | 164 | 358 | 70.38 | 32 | 35.20 | normal | 400 | #e5e2e1 | center |
| Descoperă secretele unei petreceri reușite, de l | p | 1440 | 184 | 343.19 | 672 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | left |
| Descoperă secretele unei petreceri reușite, de l | p | 1024 | 64 | 343.19 | 589.33 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | left |
| Descoperă secretele unei petreceri reușite, de l | p | 768 | 64 | 378.39 | 418.66 | 84 | 18 | 28 | normal | 400 | #c4c7c7 | left |
| Descoperă secretele unei petreceri reușite, de l | p | 390 | 16 | 258.38 | 358 | 112 | 18 | 28 | normal | 400 | #c4c7c7 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.md:col-span-8` | Articol & Inspirație | Sfaturi și Inspirație pentru Evenimente Memorabi | 16 | 16 | 16 | 16 |
| `div.md:col-span-8` | Sfaturi și Inspirație pentru Evenimente Memorabi | Descoperă secretele unei petreceri reușite, de l | 24 | 24 | 24 | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S2 — Cum să alegi formația de nuntă perfectă în 2026

`div` · clase: `lg:col-span-9 space-y-12`

Eyebrow: «Sfaturi Muzicale»

Titlu: «Cum să alegi formația de nuntă perfectă în 2026»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 792 | 1041.31 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 660 | 985.31 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 1006 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 2101.31 | 0/0/0/0 | transparent | none |
| **container interior** | 1440 | 792 | 1041.31 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 660 | 985.31 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 1006 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 358 | 2101.31 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`article.flex`) | 1440 | 384 | 508.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`article.flex`) | 1024 | 318 | 464.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`article.flex`) | 768 | 308 | 475 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`article.flex`) | 390 | 358 | 491.33 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`article.flex`) | 1440 | 384 | 508.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`article.flex`) | 1024 | 318 | 464.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`article.flex`) | 768 | 308 | 475 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`article.flex`) | 390 | 358 | 491.33 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`article.flex`) | 1440 | 384 | 508.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`article.flex`) | 1024 | 318 | 496.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`article.flex`) | 768 | 308 | 507 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`article.flex`) | 390 | 358 | 523.33 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`article.flex`) | 1440 | 384 | 508.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`article.flex`) | 1024 | 318 | 496.66 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`article.flex`) | 768 | 308 | 507 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`article.flex`) | 390 | 358 | 523.33 | 0/0/0/0 | #1c1b1b | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img blog-cover.jpg | img | 1440 | 185 | 480.19 | 382 | 254.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover.jpg | img | 1024 | 65 | 480.19 | 316 | 210.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover.jpg | img | 768 | 65 | 543.39 | 306 | 204 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover.jpg | img | 390 | 17 | 451.38 | 356 | 237.33 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sfaturi Muzicale | span | 1440 | 213 | 508.19 | 110.42 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Sfaturi Muzicale | span | 1024 | 93 | 508.19 | 110.42 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Sfaturi Muzicale | span | 768 | 93 | 571.39 | 110.42 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Sfaturi Muzicale | span | 390 | 45 | 479.38 | 110.42 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Cum să alegi formația de nuntă perfectă în 2026 | h2 | 1440 | 217 | 766.84 | 318 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum să alegi formația de nuntă perfectă în 2026 | h2 | 1024 | 97 | 722.84 | 252 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum să alegi formația de nuntă perfectă în 2026 | h2 | 768 | 97 | 779.39 | 242 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum să alegi formația de nuntă perfectă în 2026 | h2 | 390 | 49 | 720.70 | 292 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Planificarea unei nunți începe cu muzica. Află c | p | 1440 | 217 | 846.84 | 318 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Planificarea unei nunți începe cu muzica. Află c | p | 1024 | 97 | 802.84 | 252 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Planificarea unei nunți începe cu muzica. Află c | p | 768 | 97 | 859.39 | 242 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Planificarea unei nunți începe cu muzica. Află c | p | 390 | 49 | 800.70 | 292 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Citește Articolul Complet | a | 1440 | 217 | 929.84 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 1024 | 97 | 885.84 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 768 | 97 | 939.39 | 242 | 45 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 390 | 49 | 883.70 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| img blog-cover-2.jpg | img | 1440 | 593 | 480.19 | 382 | 254.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-2.jpg | img | 1024 | 407 | 480.19 | 316 | 210.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-2.jpg | img | 768 | 397 | 543.39 | 306 | 204 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-2.jpg | img | 390 | 17 | 966.70 | 356 | 237.33 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Botezuri | span | 1440 | 621 | 508.19 | 57.22 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Botezuri | span | 1024 | 435 | 508.19 | 57.22 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Botezuri | span | 768 | 425 | 571.39 | 57.22 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Botezuri | span | 390 | 45 | 994.70 | 57.22 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Muzica populară vs. Muzica ușoară la botez | h2 | 1440 | 625 | 766.84 | 318 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Muzica populară vs. Muzica ușoară la botez | h2 | 1024 | 439 | 722.84 | 252 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Muzica populară vs. Muzica ușoară la botez | h2 | 768 | 429 | 779.39 | 242 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Muzica populară vs. Muzica ușoară la botez | h2 | 390 | 49 | 1236.03 | 292 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Dilema oricărui părinte: tradiție sau modernism? | p | 1440 | 625 | 846.84 | 318 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Dilema oricărui părinte: tradiție sau modernism? | p | 1024 | 439 | 802.84 | 252 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Dilema oricărui părinte: tradiție sau modernism? | p | 768 | 429 | 859.39 | 242 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Dilema oricărui părinte: tradiție sau modernism? | p | 390 | 49 | 1316.03 | 292 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Citește Articolul Complet | a | 1440 | 625 | 929.84 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 1024 | 439 | 885.84 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 768 | 429 | 939.39 | 242 | 45 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 390 | 49 | 1399.03 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| img blog-cover-3.jpg | img | 1440 | 185 | 1012.84 | 382 | 254.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-3.jpg | img | 1024 | 65 | 968.84 | 316 | 210.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-3.jpg | img | 768 | 65 | 1042.39 | 306 | 204 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-3.jpg | img | 390 | 17 | 1482.03 | 356 | 237.33 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Nunți | span | 1440 | 213 | 1040.84 | 36.66 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Nunți | span | 1024 | 93 | 996.84 | 36.66 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Nunți | span | 768 | 93 | 1070.39 | 36.66 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Nunți | span | 390 | 45 | 1510.03 | 36.66 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Repertoriul de muzica populara nunta: Tendințe a | h2 | 1440 | 217 | 1299.50 | 318 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Repertoriul de muzica populara nunta: Tendințe a | h2 | 1024 | 97 | 1211.50 | 252 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Repertoriul de muzica populara nunta: Tendințe a | h2 | 768 | 97 | 1278.39 | 242 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Repertoriul de muzica populara nunta: Tendințe a | h2 | 390 | 49 | 1751.36 | 292 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Folclorul rămâne inima petrecerilor românești. D | p | 1440 | 217 | 1379.50 | 318 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Folclorul rămâne inima petrecerilor românești. D | p | 1024 | 97 | 1323.50 | 252 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Folclorul rămâne inima petrecerilor românești. D | p | 768 | 97 | 1390.39 | 242 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Folclorul rămâne inima petrecerilor românești. D | p | 390 | 49 | 1863.36 | 292 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Citește Articolul Complet | a | 1440 | 217 | 1462.50 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 1024 | 97 | 1406.50 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 768 | 97 | 1470.39 | 242 | 45 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 390 | 49 | 1946.36 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| img blog-cover-4.jpg | img | 1440 | 593 | 1012.84 | 382 | 254.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-4.jpg | img | 1024 | 407 | 968.84 | 316 | 210.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-4.jpg | img | 768 | 397 | 1042.39 | 306 | 204 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img blog-cover-4.jpg | img | 390 | 17 | 2029.36 | 356 | 237.33 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Evenimente Private | span | 1440 | 621 | 1040.84 | 125.25 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Evenimente Private | span | 1024 | 435 | 996.84 | 125.25 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Evenimente Private | span | 768 | 425 | 1070.39 | 125.25 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Evenimente Private | span | 390 | 45 | 2057.36 | 125.25 | 12 | 10 | 24 | 1 | 400 | #c8c6c5 | start |
| Cum transformi un eveniment privat într-un spect | h2 | 1440 | 625 | 1299.50 | 318 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum transformi un eveniment privat într-un spect | h2 | 1024 | 439 | 1211.50 | 252 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum transformi un eveniment privat într-un spect | h2 | 768 | 429 | 1278.39 | 242 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum transformi un eveniment privat într-un spect | h2 | 390 | 49 | 2298.69 | 292 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| De la calitatea sunetului la prezența scenică, m | p | 1440 | 625 | 1379.50 | 318 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| De la calitatea sunetului la prezența scenică, m | p | 1024 | 439 | 1323.50 | 252 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| De la calitatea sunetului la prezența scenică, m | p | 768 | 429 | 1390.39 | 242 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| De la calitatea sunetului la prezența scenică, m | p | 390 | 49 | 2410.69 | 292 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Citește Articolul Complet | a | 1440 | 625 | 1462.50 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 1024 | 439 | 1406.50 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 768 | 429 | 1470.39 | 242 | 45 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Citește Articolul Complet | a | 390 | 49 | 2493.69 | 249.09 | 25 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | [Sfaturi Muzicale Cum să alegi formația d] | [Botezuri Muzica populară vs. Muzica ușoa] | -508.65 ¹ | -464.65 ¹ | -475 ¹ | 24 |
| `div.grid` | [Botezuri Muzica populară vs. Muzica ușoa] | [Nunți Repertoriul de muzica populara nun] | 24 ¹ | 24 ¹ | 24 ¹ | 24 |
| `div.grid` | [Nunți Repertoriul de muzica populara nun] | [Evenimente Private Cum transformi un eve] | -508.66 ¹ | -496.66 ¹ | -507 ¹ | 24 |
| `article.flex` | [Sfaturi Muzicale] | [Cum să alegi formația de nuntă perfectă ] | 0 | 0 | 0 | 0 |
| `div.relative` | img blog-cover.jpg | [Sfaturi Muzicale] | -238.65 | -194.65 | -188 | -221.32 |
| `div.p-8` | Cum să alegi formația de nuntă perfectă în 2026 | Planificarea unei nunți începe cu muzica. Află c | 16 | 16 | 16 | 16 |
| `div.p-8` | Planificarea unei nunți începe cu muzica. Află c | [Citește Articolul Complet] | 32 | 32 | 32 | 32 |
| `article.flex` | [Botezuri] | [Muzica populară vs. Muzica ușoară la bot] | 0 | 0 | 0 | 0 |
| `div.relative` | img blog-cover-2.jpg | [Botezuri] | -238.65 | -194.65 | -188 | -221.33 |
| `div.p-8` | Muzica populară vs. Muzica ușoară la botez | Dilema oricărui părinte: tradiție sau modernism? | 16 | 16 | 16 | 16 |
| `div.p-8` | Dilema oricărui părinte: tradiție sau modernism? | [Citește Articolul Complet] | 32 | 32 | 32 | 32 |
| `article.flex` | [Nunți] | [Repertoriul de muzica populara nunta: Te] | 0 | 0 | 0 | 0 |
| `div.relative` | img blog-cover-3.jpg | [Nunți] | -238.66 | -194.66 | -188 | -221.33 |
| `div.p-8` | Repertoriul de muzica populara nunta: Tendințe a | Folclorul rămâne inima petrecerilor românești. D | 16 | 16 | 16 | 16 |
| `div.p-8` | Folclorul rămâne inima petrecerilor românești. D | [Citește Articolul Complet] | 32 | 32 | 32 | 32 |
| `article.flex` | [Evenimente Private] | [Cum transformi un eveniment privat într-] | 0 | 0 | 0 | 0 |
| `div.relative` | img blog-cover-4.jpg | [Evenimente Private] | -238.66 | -194.66 | -188 | -221.33 |
| `div.p-8` | Cum transformi un eveniment privat într-un spect | De la calitatea sunetului la prezența scenică, m | 16 | 16 | 16 | 16 |
| `div.p-8` | De la calitatea sunetului la prezența scenică, m | [Citește Articolul Complet] | 32 | 32 | 32 | 32 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 384px 384px | 24px | 24px | da (508.66) |
| `div.grid` | 1024 | grid | 318px 318px | 24px | 24px | **NU** — 464.66…496.66, delta 32 |
| `div.grid` | 768 | grid | 308px 308px | 24px | 24px | **NU** — 475…507, delta 32 |
| `div.grid` | 390 | grid | 358px | 24px | 24px | **NU** — 491.33…523.33, delta 32 |

`mt-auto` in `div.grid` — `rect.bottom` card − `rect.bottom` element impins jos (constant intre carduri = chiar functioneaza):

| Card | Element impins | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|
| card 1 | [Citește Articolul Complet] | 33 | 33 | 33 | 33 |
| card 2 | [Citește Articolul Complet] | 33 | 33 | 33 | 33 |
| card 3 | [Citește Articolul Complet] | 33 | 33 | 33 | 33 |
| card 4 | [Citește Articolul Complet] | 33 | 33 | 33 | 33 |

Verdict: 1440: constant, 1024: constant, 768: constant, 390: constant.

---

## S3 — Primește Noutăți

`section` · clase: `bg-surface-container border border-outline-variant/20 p-8`

Titlu: «Primește Noutăți»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 232 | 377 | 32/32/32/32 | #20201f | T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2 |
| **section** | 1024 | 188 | 433 | 32/32/32/32 | #20201f | T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2 |
| **section** | 768 | 640 | 305 | 32/32/32/32 | #20201f | T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2 |
| **section** | 390 | 358 | 329 | 32/32/32/32 | #20201f | T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2 |
| **container 1** (`h3.font-headline-md`) | 1440 | 166 | 32 | 0/0/0/0 | transparent | none |
| **container 1** (`h3.font-headline-md`) | 1024 | 122 | 64 | 0/0/0/0 | transparent | none |
| **container 1** (`h3.font-headline-md`) | 768 | 574 | 32 | 0/0/0/0 | transparent | none |
| **container 1** (`h3.font-headline-md`) | 390 | 292 | 32 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 1440 | 166 | 120 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 1024 | 122 | 144 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 768 | 574 | 48 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 390 | 292 | 72 | 0/0/0/0 | transparent | none |
| **container 3** (`form.space-y-4`) | 1440 | 166 | 119 | 0/0/0/0 | transparent | none |
| **container 3** (`form.space-y-4`) | 1024 | 122 | 119 | 0/0/0/0 | transparent | none |
| **container 3** (`form.space-y-4`) | 768 | 574 | 119 | 0/0/0/0 | transparent | none |
| **container 3** (`form.space-y-4`) | 390 | 292 | 119 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`label.sr-only`) | 1440 | 1 | 1 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`label.sr-only`) | 1024 | 1 | 1 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`label.sr-only`) | 768 | 1 | 1 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`label.sr-only`) | 390 | 1 | 1 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`input#newsletter-email`) | 1440 | 166 | 41 | 8/12/8/12 | transparent | B 1px #444748 @0.4 |
| └ coloana 2 (`input#newsletter-email`) | 1024 | 122 | 41 | 8/12/8/12 | transparent | B 1px #444748 @0.4 |
| └ coloana 2 (`input#newsletter-email`) | 768 | 574 | 41 | 8/12/8/12 | transparent | B 1px #444748 @0.4 |
| └ coloana 2 (`input#newsletter-email`) | 390 | 292 | 41 | 8/12/8/12 | transparent | B 1px #444748 @0.4 |
| └ coloana 3 (`button.w-full`) | 1440 | 166 | 46 | 12/0/12/0 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 3 (`button.w-full`) | 1024 | 122 | 46 | 12/0/12/0 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 3 (`button.w-full`) | 768 | 574 | 46 | 12/0/12/0 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 3 (`button.w-full`) | 390 | 292 | 46 | 12/0/12/0 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Primește Noutăți | h3 | 1440 | 1057 | 512.19 | 166 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Primește Noutăți | h3 | 1024 | 805 | 512.19 | 122 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Primește Noutăți | h3 | 768 | 97 | 1629.39 | 574 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Primește Noutăți | h3 | 390 | 49 | 2632.69 | 292 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Abonează-te pentru a primi ghiduri exclusive și  | p | 1440 | 1057 | 560.19 | 166 | 120 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Abonează-te pentru a primi ghiduri exclusive și  | p | 1024 | 805 | 592.19 | 122 | 144 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Abonează-te pentru a primi ghiduri exclusive și  | p | 768 | 97 | 1677.39 | 574 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Abonează-te pentru a primi ghiduri exclusive și  | p | 390 | 49 | 2680.69 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Adresa ta de email | label | 1440 | 1056 | 703.19 | 1 | 1 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Adresa ta de email | label | 1024 | 804 | 759.19 | 1 | 1 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Adresa ta de email | label | 768 | 96 | 1748.39 | 1 | 1 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Adresa ta de email | label | 390 | 48 | 2775.69 | 1 | 1 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1440 | 1057 | 720.19 | 166 | 41 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1024 | 805 | 776.19 | 122 | 41 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 768 | 97 | 1765.39 | 574 | 41 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 390 | 49 | 2792.69 | 292 | 41 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Abonează-te | button | 1440 | 1057 | 777.19 | 166 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Abonează-te | button | 1024 | 805 | 833.19 | 122 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Abonează-te | button | 768 | 97 | 1822.39 | 574 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Abonează-te | button | 390 | 49 | 2849.69 | 292 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | Primește Noutăți | Abonează-te pentru a primi ghiduri exclusive și  | 16 | 16 | 16 | 16 |
| `section` | Abonează-te pentru a primi ghiduri exclusive și  | [Adresa ta de email Abonează-te] | 24 | 24 | 24 | 24 |
| `form.space-y-4` | Adresa ta de email | input.w-full | 16 ¹ | 16 ¹ | 16 ¹ | 16 ¹ |
| `form.space-y-4` | input.w-full | Abonează-te | 16 | 16 | 16 | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S4 — Tag-uri SEO

`section` · clase: `—`

Eyebrow: «formatie nunta Bucuresti»

Titlu: «Tag-uri SEO»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 232 | 221 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 188 | 263 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 137 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 179 | 0/0/0/0 | transparent | none |
| **container 1** (`h3.font-label-md`) | 1440 | 232 | 37 | 0/0/16/0 | transparent | B 1px #444748 @0.3 |
| **container 1** (`h3.font-label-md`) | 1024 | 188 | 37 | 0/0/16/0 | transparent | B 1px #444748 @0.3 |
| **container 1** (`h3.font-label-md`) | 768 | 640 | 37 | 0/0/16/0 | transparent | B 1px #444748 @0.3 |
| **container 1** (`h3.font-label-md`) | 390 | 358 | 37 | 0/0/16/0 | transparent | B 1px #444748 @0.3 |
| **container 2** (`div.flex`) | 1440 | 232 | 160 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 1024 | 188 | 202 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 768 | 640 | 76 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 390 | 358 | 118 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.px-3`) | 1440 | 153.61 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`span.px-3`) | 1024 | 153.61 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`span.px-3`) | 768 | 153.61 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 1 (`span.px-3`) | 390 | 153.61 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`span.px-3`) | 1440 | 144.70 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`span.px-3`) | 1024 | 144.70 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`span.px-3`) | 768 | 144.70 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 2 (`span.px-3`) | 390 | 144.70 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`span.px-3`) | 1440 | 132.28 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`span.px-3`) | 1024 | 132.28 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`span.px-3`) | 768 | 132.28 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 3 (`span.px-3`) | 390 | 132.28 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`span.px-3`) | 1440 | 109.59 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`span.px-3`) | 1024 | 109.59 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`span.px-3`) | 768 | 109.59 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 4 (`span.px-3`) | 390 | 109.59 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 5 (`span.px-3`) | 1440 | 109.02 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 5 (`span.px-3`) | 1024 | 109.02 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 5 (`span.px-3`) | 768 | 109.02 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |
| └ coloana 5 (`span.px-3`) | 390 | 109.02 | 34 | 4/12/4/12 | transparent | T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tag-uri SEO | h3 | 1440 | 1024 | 904.19 | 232 | 37 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tag-uri SEO | h3 | 1024 | 772 | 960.19 | 188 | 37 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tag-uri SEO | h3 | 768 | 64 | 1949.39 | 640 | 37 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tag-uri SEO | h3 | 390 | 16 | 2976.69 | 358 | 37 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| formatie nunta Bucuresti | span | 1440 | 1024 | 965.19 | 153.61 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| formatie nunta Bucuresti | span | 1024 | 772 | 1021.19 | 153.61 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| formatie nunta Bucuresti | span | 768 | 64 | 2010.39 | 153.61 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| formatie nunta Bucuresti | span | 390 | 16 | 3037.69 | 153.61 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| muzica populara nunta | span | 1440 | 1024 | 1007.19 | 144.70 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| muzica populara nunta | span | 1024 | 772 | 1063.19 | 144.70 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| muzica populara nunta | span | 768 | 225.61 | 2010.39 | 144.70 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| muzica populara nunta | span | 390 | 177.61 | 3037.69 | 144.70 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| solist muzica usoara | span | 1440 | 1024 | 1049.19 | 132.28 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| solist muzica usoara | span | 1024 | 772 | 1105.19 | 132.28 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| solist muzica usoara | span | 768 | 378.31 | 2010.39 | 132.28 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| solist muzica usoara | span | 390 | 16 | 3079.69 | 132.28 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| repertoriu botez | span | 1440 | 1024 | 1091.19 | 109.59 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| repertoriu botez | span | 1024 | 772 | 1147.19 | 109.59 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| repertoriu botez | span | 768 | 518.59 | 2010.39 | 109.59 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| repertoriu botez | span | 390 | 156.28 | 3079.69 | 109.59 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| premium events | span | 1440 | 1141.59 | 1091.19 | 109.02 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| premium events | span | 1024 | 772 | 1189.19 | 109.02 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| premium events | span | 768 | 64 | 2052.39 | 109.02 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |
| premium events | span | 390 | 16 | 3121.69 | 109.02 | 34 | 11 | 24 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | Tag-uri SEO | [formatie nunta Bucuresti muzica populara] | 24 | 24 | 24 | 24 |
| `div.flex` | formatie nunta Bucuresti | muzica populara nunta | 8 | 8 | -34 ¹ | -34 ¹ |
| `div.flex` | muzica populara nunta | solist muzica usoara | 8 | 8 | -34 ¹ | 8 ¹ |
| `div.flex` | solist muzica usoara | repertoriu botez | 8 | 8 | -34 ¹ | -34 ¹ |
| `div.flex` | repertoriu botez | premium events | -34 ¹ | 8 | 8 ¹ | 8 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 153.61 + 144.70 + 132.28 + 109.59 + 109.02 | 8px | 8px | da (34) |
| `div.flex` | 1024 | flex | 153.61 + 144.70 + 132.28 + 109.59 + 109.02 | 8px | 8px | da (34) |
| `div.flex` | 768 | flex | 153.61 + 144.70 + 132.28 + 109.59 + 109.02 | 8px | 8px | da (34) |
| `div.flex` | 390 | flex | 153.61 + 144.70 + 132.28 + 109.59 + 109.02 | 8px | 8px | da (34) |

---

## Ce nu se vede din clase

### `line-height` mostenit de la `<body>`, nu setat pe element

- `span` «Sfaturi Muzicale» la 1440 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Sfaturi Muzicale» la 1024 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Sfaturi Muzicale» la 768 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Sfaturi Muzicale» la 390 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Botezuri» la 1440 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Botezuri» la 1024 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Botezuri» la 768 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Botezuri» la 390 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Nunți» la 1440 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Nunți» la 1024 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Nunți» la 768 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Nunți» la 390 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Evenimente Private» la 1440 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Evenimente Private» la 1024 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Evenimente Private» la 768 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «Evenimente Private» la 390 — font-size 10px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.40)
- `span` «formatie nunta Bucuresti» la 1440 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «formatie nunta Bucuresti» la 1024 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «formatie nunta Bucuresti» la 768 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «formatie nunta Bucuresti» la 390 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «muzica populara nunta» la 1440 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «muzica populara nunta» la 1024 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «muzica populara nunta» la 768 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «muzica populara nunta» la 390 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «solist muzica usoara» la 1440 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «solist muzica usoara» la 1024 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «solist muzica usoara» la 768 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «solist muzica usoara» la 390 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «repertoriu botez» la 1440 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «repertoriu botez» la 1024 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «repertoriu botez» la 768 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «repertoriu botez» la 390 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «premium events» la 1440 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «premium events» la 1024 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «premium events» la 768 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)
- `span` «premium events» la 390 — font-size 11px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.18)

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Sfaturi și Inspirație pentru Evenimente Memorabi» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[32px]`; weight rezolvat 400, font-size masurat 32/48/56px
- `span` «Sfaturi Muzicale» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[10px]`; weight rezolvat 400, font-size masurat 10px
- `span` «Botezuri» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[10px]`; weight rezolvat 400, font-size masurat 10px
- `span` «Nunți» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[10px]`; weight rezolvat 400, font-size masurat 10px
- `span` «Evenimente Private» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[10px]`; weight rezolvat 400, font-size masurat 10px
- `span` «formatie nunta Bucuresti» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `span` «muzica populara nunta» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `span` «solist muzica usoara» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `span` «repertoriu botez» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `span` «premium events» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px

### Borduri care vin din `assets/styles.css`, nu din clase

- `article.flex` «[Sfaturi Muzicale Cum să alegi formația d]» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.flex` «[Botezuri Muzica populară vs. Muzica ușoa]» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.flex` «[Nunți Repertoriul de muzica populara nun]» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.flex` «[Evenimente Private Cum transformi un eve]» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.w-full` «Abonează-te» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.px-3` «formatie nunta Bucuresti» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.px-3` «muzica populara nunta» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.px-3` «solist muzica usoara» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.px-3` «repertoriu botez» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.px-3` «premium events» — T 1px #e3e2de @0.15, R 1px #e3e2de @0.15, B 1px #e3e2de @0.15, L 1px #e3e2de @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Suprapuneri intre elemente

- in `div.relative`: «img blog-cover.jpg» si «[Sfaturi Muzicale]» se suprapun pe verticala cu 238.65px la 1440 (suprapunere orizontala 134.42px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover.jpg» si «[Sfaturi Muzicale]» se suprapun pe verticala cu 194.65px la 1024 (suprapunere orizontala 134.42px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover.jpg» si «[Sfaturi Muzicale]» se suprapun pe verticala cu 188px la 768 (suprapunere orizontala 134.42px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover.jpg» si «[Sfaturi Muzicale]» se suprapun pe verticala cu 221.32px la 390 (suprapunere orizontala 134.42px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-2.jpg» si «[Botezuri]» se suprapun pe verticala cu 238.65px la 1440 (suprapunere orizontala 81.22px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-2.jpg» si «[Botezuri]» se suprapun pe verticala cu 194.65px la 1024 (suprapunere orizontala 81.22px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-2.jpg» si «[Botezuri]» se suprapun pe verticala cu 188px la 768 (suprapunere orizontala 81.22px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-2.jpg» si «[Botezuri]» se suprapun pe verticala cu 221.33px la 390 (suprapunere orizontala 81.22px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-3.jpg» si «[Nunți]» se suprapun pe verticala cu 238.66px la 1440 (suprapunere orizontala 60.66px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-3.jpg» si «[Nunți]» se suprapun pe verticala cu 194.66px la 1024 (suprapunere orizontala 60.66px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-3.jpg» si «[Nunți]» se suprapun pe verticala cu 188px la 768 (suprapunere orizontala 60.66px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-3.jpg» si «[Nunți]» se suprapun pe verticala cu 221.33px la 390 (suprapunere orizontala 60.66px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-4.jpg» si «[Evenimente Private]» se suprapun pe verticala cu 238.66px la 1440 (suprapunere orizontala 149.25px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-4.jpg» si «[Evenimente Private]» se suprapun pe verticala cu 194.66px la 1024 (suprapunere orizontala 149.25px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-4.jpg» si «[Evenimente Private]» se suprapun pe verticala cu 188px la 768 (suprapunere orizontala 149.25px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img blog-cover-4.jpg» si «[Evenimente Private]» se suprapun pe verticala cu 221.33px la 390 (suprapunere orizontala 149.25px, position static/absolute) — stratificare intentionata (`position: absolute`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Sfaturi și Inspirație pentru Evenimente Memorabile | 1440: 672 · 1024: 589.33 · 768: 418.66 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Cum să alegi formația de nuntă perfectă în 2026 | 1440: 382 · 1024: 316 · 768: 306 · 390: 356 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Primește Noutăți | 1440: 168 · 1024: 124 · 768: 576 · 390: 294 | vert (sectiune): 32 sus / 32 jos<br>oriz (container): 32 L / 32 R | — | — | o singura coloana |
| Tag-uri SEO | 1440: 232 · 1024: 188 · 768: 640 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 4/12/4/12 | x 8px / y 8px | in `div.flex` (lat. 232 la 1440, flex):<br>153.61 + 144.70 + 132.28 + 109.59 + 109.02 |
