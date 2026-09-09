# Geometrie randata — `index.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/index.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.
- Hero-ul din `index.html` e de asemenea deja masurat si e **sarit** aici.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 5512.06 | 0/0/0/0 | transparent | none |
| `<main>` | 1024 | 1024 | 5513.09 | 0/0/0/0 | transparent | none |
| `<main>` | 768 | 768 | 6246.42 | 0/0/0/0 | transparent | none |
| `<main>` | 390 | 390 | 6771.14 | 0/0/0/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 5949px, 1024 → 5950px, 768 → 6735px, 390 → 7376px.

Sectiuni masurate: **7**.

---

## S1 — Muzică pentru nuntă, botez și corporate

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-y border-outline-variant/10`

Eyebrow: «Nuntă · Botez · Corporate»

Titlu: «Muzică pentru nuntă, botez și corporate»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 676 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 700 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 708 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 1188 | 64/0/64/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 482 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 506 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 514 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 1058 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1440 | 1072 | 116 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1024 | 896 | 116 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 768 | 640 | 116 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 390 | 358 | 128 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1440 | 1072 | 302 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1024 | 896 | 326 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 768 | 640 | 334 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 390 | 358 | 882 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nuntă · Botez · Corporate | span | 1440 | 184 | 841 | 1072 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| Nuntă · Botez · Corporate | span | 1024 | 64 | 854.19 | 896 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| Nuntă · Botez · Corporate | span | 768 | 64 | 1162.17 | 640 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| Nuntă · Botez · Corporate | span | 390 | 16 | 990.39 | 358 | 24 | 12 | 24 | 3.60 | 400 | #c8c6c5 | center |
| Muzică pentru nuntă, botez și corporate | h2 | 1440 | 184 | 873 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Muzică pentru nuntă, botez și corporate | h2 | 1024 | 64 | 886.19 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Muzică pentru nuntă, botez și corporate | h2 | 768 | 64 | 1194.17 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Muzică pentru nuntă, botez și corporate | h2 | 390 | 16 | 1026.39 | 358 | 48 | 28 | 24 | normal | 400 | #e5e2e1 | center |
| svg (icon) | svg | 1440 | 336.66 | 1054 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 187.33 | 1067.19 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 144.66 | 1367.17 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 177 | 1191.39 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| Muzică Nuntă | h3 | 1440 | 285.73 | 1114 | 137.86 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Nuntă | h3 | 1024 | 136.39 | 1127.19 | 137.86 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Nuntă | h3 | 768 | 93.73 | 1419.17 | 137.86 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Nuntă | h3 | 390 | 126.06 | 1251.39 | 137.86 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Formație live și sonorizare proprie, cu repertor | p | 1440 | 217 | 1162 | 275.33 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Formație live și sonorizare proprie, cu repertor | p | 1024 | 97 | 1175.19 | 216.66 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Formație live și sonorizare proprie, cu repertor | p | 768 | 89 | 1467.17 | 147.33 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Formație live și sonorizare proprie, cu repertor | p | 390 | 41 | 1299.39 | 308 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Detalii | a | 1440 | 306.66 | 1266 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 1024 | 157.31 | 1303.19 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 768 | 114.66 | 1627.17 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 390 | 146.98 | 1395.39 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 384.67 | 1269 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 235.33 | 1306.19 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 192.67 | 1630.17 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 225 | 1398.39 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 701.98 | 1054 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 493.98 | 1067.19 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 365.98 | 1367.17 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 177 | 1493.39 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| Muzică Botez | h3 | 1440 | 655.70 | 1114 | 128.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Botez | h3 | 1024 | 447.70 | 1127.19 | 128.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Botez | h3 | 768 | 319.70 | 1419.17 | 128.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică Botez | h3 | 390 | 130.70 | 1553.39 | 128.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Program potrivit pentru botez: muzică de petrece | p | 1440 | 582.33 | 1162 | 275.33 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Program potrivit pentru botez: muzică de petrece | p | 1024 | 403.66 | 1175.19 | 216.67 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Program potrivit pentru botez: muzică de petrece | p | 768 | 310.33 | 1467.17 | 147.33 | 144 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Program potrivit pentru botez: muzică de petrece | p | 390 | 41 | 1601.39 | 308 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Detalii | a | 1440 | 671.98 | 1266 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 1024 | 463.98 | 1303.19 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 768 | 335.98 | 1627.17 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 390 | 146.98 | 1697.39 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 750 | 1269 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 542 | 1306.19 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 414 | 1630.17 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 225 | 1700.39 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 1067.33 | 1054 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 800.66 | 1067.19 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 587.31 | 1367.17 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 177 | 1795.39 | 36 | 36 | 36 | 40 | normal | 400 | #c8c6c5 | center |
| Corporate | h3 | 1440 | 1036.03 | 1114 | 98.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Corporate | h3 | 1024 | 769.36 | 1127.19 | 98.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Corporate | h3 | 768 | 556.02 | 1419.17 | 98.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Corporate | h3 | 390 | 145.70 | 1855.39 | 98.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| Muzică live și DJ pentru gale și recepții corpor | p | 1440 | 947.66 | 1162 | 275.34 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Muzică live și DJ pentru gale și recepții corpor | p | 1024 | 710.33 | 1175.19 | 216.66 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Muzică live și DJ pentru gale și recepții corpor | p | 768 | 531.66 | 1467.17 | 147.33 | 144 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Muzică live și DJ pentru gale și recepții corpor | p | 390 | 41 | 1903.39 | 308 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Detalii | a | 1440 | 1037.31 | 1266 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 1024 | 770.64 | 1303.19 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 768 | 557.31 | 1627.17 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| Detalii | a | 390 | 146.98 | 1999.39 | 96.02 | 24 | 16 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 1115.33 | 1269 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 848.66 | 1306.19 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 635.33 | 1630.17 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 225 | 2002.39 | 18 | 18 | 18 | 24 | 1.60 | 400 | #c8c6c5 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Nuntă · Botez · Corporate Muzică pentru ] | [Muzică Nuntă Formație live și sonorizare] | 64 | 64 | 64 | 48 |
| `div.text-center` | Nuntă · Botez · Corporate | Muzică pentru nuntă, botez și corporate | 12 | 12 | 12 | 12 |
| `div.text-center` | Muzică pentru nuntă, botez și corporate | div.motif-rule | 20 | 20 | 20 | 20 |
| `div.grid` | [Muzică Nuntă Formație live și sonorizare] | [Muzică Botez Program potrivit pentru bot] | -302 ¹ | -326 ¹ | -334 ¹ | 24 |
| `div.grid` | [Muzică Botez Program potrivit pentru bot] | [Corporate Muzică live și DJ pentru gale ] | -302 ¹ | -326 ¹ | -334 ¹ | 24 |
| `article.glass-panel` | svg (icon) | Muzică Nuntă | 24 | 24 | 16 | 24 |
| `article.glass-panel` | Muzică Nuntă | Formație live și sonorizare proprie, cu repertor | 16 | 16 | 16 | 16 |
| `article.glass-panel` | Formație live și sonorizare proprie, cu repertor | Detalii | 32 | 32 | 40 | 24 |
| `article.glass-panel` | svg (icon) | Muzică Botez | 24 | 24 | 16 | 24 |
| `article.glass-panel` | Muzică Botez | Program potrivit pentru botez: muzică de petrece | 16 | 16 | 16 | 16 |
| `article.glass-panel` | Program potrivit pentru botez: muzică de petrece | Detalii | 32 | 32 | 16 | 24 |
| `article.glass-panel` | svg (icon) | Corporate | 24 | 24 | 16 | 24 |
| `article.glass-panel` | Corporate | Muzică live și DJ pentru gale și recepții corpor | 16 | 16 | 16 | 16 |
| `article.glass-panel` | Muzică live și DJ pentru gale și recepții corpor | Detalii | 32 | 32 | 16 | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 341.328px 341.328px 341.344px | 24px | 24px | da (302) |
| `div.grid` | 1024 | grid | 282.656px 282.672px 282.656px | 24px | 24px | da (326) |
| `div.grid` | 768 | grid | 197.328px 197.328px 197.328px | 24px | 24px | da (334) |
| `div.grid` | 390 | grid | 358px | 24px | 24px | da (278) |

`mt-auto` in `div.grid` — `rect.bottom` card − `rect.bottom` element impins jos (constant intre carduri = chiar functioneaza):

| Card | Element impins | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|
| card 1 | Detalii | 33 | 33 | 25 | 25 |
| card 2 | Detalii | 33 | 33 | 25 | 25 |
| card 3 | Detalii | 33 | 33 | 25 | 25 |

Verdict: 1440: constant, 1024: constant, 768: constant, 390: constant.

---

## S2 — Pachete pentru 2026–2027

`section` · clase: `py-16 md:py-24 bg-surface-container-highest border-y border-outline-variant/10`

Eyebrow: «Oferte»

Titlu: «Pachete pentru 2026–2027»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 381 | 96/0/96/0 | #353535 | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 438 | 96/0/96/0 | #353535 | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 581 | 96/0/96/0 | #353535 | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 521 | 64/0/64/0 | #353535 | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 187 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 244 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 387 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 391 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.flex`) | 1440 | 1072 | 187 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 1024 | 896 | 244 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 768 | 640 | 387 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 390 | 358 | 391 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Oferte | span | 1440 | 184 | 1530.50 | 624 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Oferte | span | 1024 | 64 | 1554.19 | 448 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Oferte | span | 768 | 64 | 1870.17 | 640 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Oferte | span | 390 | 16 | 2178.39 | 358 | 24 | 12 | 24 | 3.60 | 400 | #c8c6c5 | start |
| Pachete pentru 2026–2027 | h2 | 1440 | 184 | 1562.50 | 624 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Pachete pentru 2026–2027 | h2 | 1024 | 64 | 1586.19 | 448 | 112 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Pachete pentru 2026–2027 | h2 | 768 | 64 | 1902.17 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Pachete pentru 2026–2027 | h2 | 390 | 16 | 2214.39 | 358 | 40 | 32 | 40 | normal | 400 | #e5e2e1 | start |
| Formație live, interpreți, DJ/MC și producție te | p | 1440 | 184 | 1634.50 | 576 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Formație live, interpreți, DJ/MC și producție te | p | 1024 | 64 | 1714.19 | 448 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Formație live, interpreți, DJ/MC și producție te | p | 768 | 64 | 1974.17 | 576 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Formație live, interpreți, DJ/MC și producție te | p | 390 | 16 | 2270.39 | 358 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| svg (icon) | svg | 1440 | 872 | 1544 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 576 | 1609.69 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 64 | 2121.17 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 16 | 2409.39 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| Formație 6 instrumente + 3 interpreți | span | 1440 | 904 | 1542 | 276.70 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Formație 6 instrumente + 3 interpreți | span | 1024 | 608 | 1607.69 | 276.70 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Formație 6 instrumente + 3 interpreți | span | 768 | 96 | 2119.17 | 276.70 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Formație 6 instrumente + 3 interpreți | span | 390 | 48 | 2407.39 | 276.70 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| svg (icon) | svg | 1440 | 872 | 1592 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 576 | 1657.69 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 64 | 2157.17 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 16 | 2457.39 | 20 | 20 | 20 | 24 | normal | 400 | #c8c6c5 | start |
| DJ/MC, lumini și ecran LED în pachetul Premium | span | 1440 | 904 | 1578 | 352 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ/MC, lumini și ecran LED în pachetul Premium | span | 1024 | 608 | 1643.69 | 352 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ/MC, lumini și ecran LED în pachetul Premium | span | 768 | 96 | 2155.17 | 363.25 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ/MC, lumini și ecran LED în pachetul Premium | span | 390 | 48 | 2443.39 | 326 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Vezi ofertele | a | 1440 | 872 | 1650 | 384 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Vezi ofertele | a | 1024 | 576 | 1715.69 | 384 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Vezi ofertele | a | 768 | 64 | 2203.17 | 640 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Vezi ofertele | a | 390 | 16 | 2515.39 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.flex` | [Oferte Pachete pentru 2026–2027 Formație] | [Formație 6 instrumente + 3 interpreți DJ] | -173.50 ¹ | -215.50 ¹ | 64 | 40 |
| `div.w-full` | Oferte | Pachete pentru 2026–2027 | 12 | 12 | 12 | 12 |
| `div.w-full` | Pachete pentru 2026–2027 | Formație live, interpreți, DJ/MC și producție te | 16 | 16 | 16 | 16 |
| `div.w-full` | [Formație 6 instrumente + 3 interpreți DJ] | Vezi ofertele | 24 | 24 | 24 | 24 |
| `ul.flex` | [Formație 6 instrumente + 3 interpreți] | [DJ/MC, lumini și ecran LED în pachetul P] | 12 | 12 | 12 | 12 |
| `li.flex` | svg (icon) | Formație 6 instrumente + 3 interpreți | -22 ¹ | -22 ¹ | -22 ¹ | -22 ¹ |
| `li.flex` | svg (icon) | DJ/MC, lumini și ecran LED în pachetul Premium | -34 ¹ | -34 ¹ | -22 ¹ | -34 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 624 + 384 | 64px | 64px | **NU** — 160…187, delta 27 |
| `div.flex` | 1024 | flex | 448 + 384 | 64px | 64px | **NU** — 187…244, delta 57 |
| `div.flex` | 768 | flex | 640 + 640 | 64px | 64px | **NU** — 160…163, delta 3 |
| `div.flex` | 390 | flex | 358 + 358 | 40px | 40px | **NU** — 164…187, delta 23 |
| `li.flex` | 1440 | flex | 20 + 276.70 | 12px | 12px | **NU** — 20…24, delta 4 |
| `li.flex` | 1024 | flex | 20 + 276.70 | 12px | 12px | **NU** — 20…24, delta 4 |
| `li.flex` | 768 | flex | 20 + 276.70 | 12px | 12px | **NU** — 20…24, delta 4 |
| `li.flex` | 390 | flex | 20 + 276.70 | 12px | 12px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 20 + 352 | 12px | 12px | **NU** — 20…48, delta 28 |
| `li.flex` | 1024 | flex | 20 + 352 | 12px | 12px | **NU** — 20…48, delta 28 |
| `li.flex` | 768 | flex | 20 + 363.25 | 12px | 12px | **NU** — 20…24, delta 4 |
| `li.flex` | 390 | flex | 20 + 326 | 12px | 12px | **NU** — 20…48, delta 28 |

---

## S3 — Peste 15 ani pe scenă

`section` · clase: `py-16 md:py-24 bg-background overflow-hidden`

Eyebrow: «15+»

Titlu: «Peste 15 ani pe scenă»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 724.31 | 96/0/96/0 | #131313 | none |
| **section** | 1024 | 1024 | 632.66 | 96/0/96/0 | #131313 | none |
| **section** | 768 | 768 | 661 | 96/0/96/0 | #131313 | none |
| **section** | 390 | 390 | 1034 | 64/0/64/0 | #131313 | none |
| **container interior** | 1440 | 1200 | 532.31 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 440.66 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 469 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 906 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.md:col-span-5`) | 1440 | 432.66 | 532.31 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-5`) | 1024 | 359.33 | 440.66 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-5`) | 768 | 252.66 | 307.31 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.md:col-span-5`) | 390 | 358 | 443 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.md:col-span-7`) | 1440 | 615.34 | 365 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.md:col-span-7`) | 1024 | 512.67 | 391 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.md:col-span-7`) | 768 | 363.34 | 469 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.md:col-span-7`) | 390 | 358 | 423 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 1440 | 201 | 1914 | 398.66 | 498.31 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 1024 | 81 | 2008.19 | 325.33 | 406.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 768 | 81 | 2548.02 | 218.66 | 273.31 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 390 | 25 | 3170.39 | 340 | 425 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Peste 15 ani pe scenă | h2 | 1440 | 640.66 | 1980.66 | 615.34 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Peste 15 ani pe scenă | h2 | 1024 | 447.33 | 2016.02 | 512.67 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Peste 15 ani pe scenă | h2 | 768 | 340.66 | 2450.17 | 363.34 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Peste 15 ani pe scenă | h2 | 390 | 16 | 2698.39 | 358 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | start |
| Muzica nu este doar o profesie pentru mine, ci f | p | 1440 | 640.66 | 2052.66 | 615.34 | 78 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Muzica nu este doar o profesie pentru mine, ci f | p | 1024 | 447.33 | 2088.02 | 512.67 | 78 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Muzica nu este doar o profesie pentru mine, ci f | p | 768 | 340.66 | 2522.17 | 363.34 | 130 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Muzica nu este doar o profesie pentru mine, ci f | p | 390 | 16 | 2746.39 | 358 | 130 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Pentru mine, cea mai mare răsplată este să văd e | p | 1440 | 640.66 | 2154.66 | 615.34 | 78 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Pentru mine, cea mai mare răsplată este să văd e | p | 1024 | 447.33 | 2190.02 | 512.67 | 104 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Pentru mine, cea mai mare răsplată este să văd e | p | 768 | 340.66 | 2676.17 | 363.34 | 130 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| Pentru mine, cea mai mare răsplată este să văd e | p | 390 | 16 | 2892.39 | 358 | 130 | 16 | 26 | normal | 400 | #c6c6c6 | start |
| 15+ | span | 1440 | 640.66 | 2281.66 | 106.38 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 15+ | span | 1024 | 447.33 | 2343.02 | 106.38 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 15+ | span | 768 | 340.66 | 2855.17 | 106.38 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 15+ | span | 390 | 16 | 3063.39 | 83.17 | 28 | 28 | 28 | normal | 400 | #c8c6c5 | start |
| Ani pe scenă | span | 1440 | 640.66 | 2325.66 | 106.38 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Ani pe scenă | span | 1024 | 447.33 | 2387.02 | 106.38 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Ani pe scenă | span | 768 | 340.66 | 2899.17 | 106.38 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Ani pe scenă | span | 390 | 16 | 3101.39 | 83.17 | 15 | 12 | 24 | normal | 400 | #c6c6c6 | start |
| 3 | span | 1440 | 787.03 | 2281.66 | 127.19 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 3 | span | 1024 | 593.70 | 2343.02 | 127.19 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 3 | span | 768 | 487.03 | 2855.17 | 127.19 | 36 | 36 | 36 | normal | 400 | #c8c6c5 | start |
| 3 | span | 390 | 123.17 | 3063.39 | 99.67 | 28 | 28 | 28 | normal | 400 | #c8c6c5 | start |
| Albume proprii | span | 1440 | 787.03 | 2325.66 | 127.19 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Albume proprii | span | 1024 | 593.70 | 2387.02 | 127.19 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Albume proprii | span | 768 | 487.03 | 2899.17 | 127.19 | 17 | 14 | 20 | 0.70 | 600 | #c6c6c6 | start |
| Albume proprii | span | 390 | 123.17 | 3101.39 | 99.67 | 15 | 12 | 24 | normal | 400 | #c6c6c6 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | div.md:col-span-5 | [Peste 15 ani pe scenă Muzica nu este doa] | -448.65 ¹ | -415.82 ¹ | -388.16 ¹ | -906 |
| `div.md:col-span-5` | div.border | div.absolute | -160 | -160 | -160 | -104 |
| `div.md:col-span-7` | Peste 15 ani pe scenă | [Muzica nu este doar o profesie pentru mi] | 32 | 32 | 32 | 24 |
| `div.space-y-4` | Muzica nu este doar o profesie pentru mine, ci f | Pentru mine, cea mai mare răsplată este să văd e | 24 | 24 | 24 | 16 |
| `div.space-y-4` | Pentru mine, cea mai mare răsplată este să văd e | [15+ Ani pe scenă 3 Albume proprii] | 24 | 24 | 24 | 16 |
| `div.flex` | [15+ Ani pe scenă] | [3 Albume proprii] | -64 ¹ | -64 ¹ | -64 ¹ | -58 ¹ |
| `div` | 15+ | Ani pe scenă | 8 | 8 | 8 | 10 |
| `div` | 3 | Albume proprii | 8 | 8 | 8 | 10 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | 1440 | grid | 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px | 24px | 24px | **NU** — 365…532.31, delta 167.31 |
| `div.max-w-[1200px]` | 1024 | grid | 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px | 24px | 24px | **NU** — 391…440.66, delta 49.66 |
| `div.max-w-[1200px]` | 768 | grid | 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px | 24px | 24px | **NU** — 307.31…469, delta 161.69 |
| `div.max-w-[1200px]` | 390 | grid | 358px | 40px | 40px | **NU** — 423…443, delta 20 |
| `div.flex` | 1440 | flex | 106.38 + 127.19 | 40px | 40px | da (64) |
| `div.flex` | 1024 | flex | 106.38 + 127.19 | 40px | 40px | da (64) |
| `div.flex` | 768 | flex | 106.38 + 127.19 | 40px | 40px | da (64) |
| `div.flex` | 390 | flex | 83.17 + 99.67 | 24px | 24px | da (58) |

---

## S4 — Vezi cum arată un eveniment

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-y border-outline-variant/10`

Eyebrow: «Evenimente»

Titlu: «Vezi cum arată un eveniment»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 696.75 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 647.25 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 575.25 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 716.75 | 64/0/64/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 502.75 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 453.25 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 381.25 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 586.75 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.mb-10`) | 1440 | 1072 | 68 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.mb-10`) | 1024 | 896 | 68 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.mb-10`) | 768 | 640 | 68 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.mb-10`) | 390 | 358 | 52 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1440 | 1072 | 294.75 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1024 | 896 | 245.25 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 768 | 640 | 173.25 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 390 | 358 | 418.75 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.mt-8`) | 1440 | 1072 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.mt-8`) | 1024 | 896 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.mt-8`) | 768 | 640 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.mt-8`) | 390 | 358 | 44 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evenimente | span | 1440 | 184 | 2622.31 | 1072 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 1024 | 64 | 2624.84 | 896 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 768 | 64 | 3112.17 | 640 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 390 | 16 | 3733.39 | 358 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi cum arată un eveniment | h2 | 1440 | 184 | 2650.31 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Vezi cum arată un eveniment | h2 | 1024 | 64 | 2652.84 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Vezi cum arată un eveniment | h2 | 768 | 64 | 3140.17 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Vezi cum arată un eveniment | h2 | 390 | 16 | 3761.39 | 358 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | start |
| img XFdALRgk7Fg.jpg | img | 1440 | 185 | 2747.31 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img XFdALRgk7Fg.jpg | img | 1024 | 65 | 2749.84 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img XFdALRgk7Fg.jpg | img | 768 | 65 | 3237.17 | 306 | 171.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img XFdALRgk7Fg.jpg | img | 390 | 17 | 3826.39 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 436.50 | 2882.69 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 272.50 | 2860.47 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 208.50 | 3311.80 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 3915.08 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Formație live | span | 1440 | 205 | 2977.38 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Formație live | span | 1024 | 85 | 2930.41 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Formație live | span | 768 | 85 | 3318.23 | 266 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Formație live | span | 390 | 37 | 3968.08 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Formație de nuntă în București | span | 1440 | 205 | 2994.97 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Formație de nuntă în București | span | 1024 | 85 | 2948 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Formație de nuntă în București | span | 768 | 85 | 3335.83 | 266 | 55 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Formație de nuntă în București | span | 390 | 37 | 3985.67 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| img hzOdwacBNN0.jpg | img | 1440 | 733 | 2747.31 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img hzOdwacBNN0.jpg | img | 1024 | 525 | 2749.84 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img hzOdwacBNN0.jpg | img | 768 | 397 | 3237.17 | 306 | 171.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img hzOdwacBNN0.jpg | img | 390 | 17 | 4043.77 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 984.50 | 2882.69 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 732.50 | 2860.47 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 540.50 | 3311.80 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 4132.45 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Muzică populară | span | 1440 | 753 | 2977.38 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică populară | span | 1024 | 545 | 2930.41 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică populară | span | 768 | 417 | 3318.23 | 266 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică populară | span | 390 | 37 | 4185.45 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Colaj de Moldova, live la nuntă | span | 1440 | 753 | 2994.97 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Colaj de Moldova, live la nuntă | span | 1024 | 545 | 2948 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Colaj de Moldova, live la nuntă | span | 768 | 417 | 3335.83 | 266 | 55 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Colaj de Moldova, live la nuntă | span | 390 | 37 | 4203.05 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| Vezi toate videoclipurile | a | 1440 | 590.16 | 3081.06 | 259.67 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi toate videoclipurile | a | 1024 | 382.16 | 3034.09 | 259.67 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi toate videoclipurile | a | 768 | 254.16 | 3449.42 | 259.67 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi toate videoclipurile | a | 390 | 65.16 | 4276.14 | 259.67 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1440 | 831.83 | 3094.06 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 623.83 | 3047.09 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 495.83 | 3462.42 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 306.83 | 4289.14 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Evenimente Vezi cum arată un eveniment] | [Formație live Formație de nuntă în Bucur] | 56 | 56 | 56 | 40 |
| `div.max-w-[1200px]` | [Formație live Formație de nuntă în Bucur] | [Vezi toate videoclipurile] | 40 | 40 | 40 | 32 |
| `div.mb-10` | Evenimente | Vezi cum arată un eveniment | 8 | 8 | 8 | 8 |
| `div.grid` | [Formație live Formație de nuntă în Bucur] | [Muzică populară Colaj de Moldova, live l] | -294.75 ¹ | -245.25 ¹ | -173.25 ¹ | 16 |
| `button.video-card` | img XFdALRgk7Fg.jpg | span.video-card__veil | -292.75 | -243.25 | -171.25 | -199.38 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -117.62 | -131.69 |
| `button.video-card` | span.video-card__play | [Formație live Formație de nuntă în Bucur] | 31.69 | 6.94 | -56.57 | -10 |
| `span.video-card__meta` | Formație live | Formație de nuntă în București | 5.59 | 5.59 | 5.60 | 5.59 |
| `button.video-card` | img hzOdwacBNN0.jpg | span.video-card__veil | -292.75 | -243.25 | -171.25 | -199.37 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -117.62 | -131.69 |
| `button.video-card` | span.video-card__play | [Muzică populară Colaj de Moldova, live l] | 31.69 | 6.94 | -56.57 | -10 |
| `span.video-card__meta` | Muzică populară | Colaj de Moldova, live la nuntă | 5.59 | 5.59 | 5.60 | 5.60 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 524px 524px | 24px | 24px | da (294.75) |
| `div.grid` | 1024 | grid | 436px 436px | 24px | 24px | da (245.25) |
| `div.grid` | 768 | grid | 308px 308px | 24px | 24px | da (173.25) |
| `div.grid` | 390 | grid | 358px | 16px | 16px | da (201.38) |

---

## S5 — Ce Spun Mirii și Gazdele

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-y border-outline-variant/10`

Eyebrow: «Recomandări»

Titlu: «Ce Spun Mirii și Gazdele»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 812 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 860 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 1072 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 1208 | 64/0/64/0 | #1c1b1b | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 618 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 666 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 878 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 1078 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1440 | 1072 | 124 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1024 | 896 | 124 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 768 | 640 | 124 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 390 | 358 | 108 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1440 | 1072 | 358 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 1024 | 896 | 406 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 768 | 640 | 618 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.grid`) | 390 | 358 | 866 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1440 | 1072 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1024 | 896 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 768 | 640 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 390 | 358 | 24 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recomandări | span | 1440 | 184 | 3319.06 | 1072 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Recomandări | span | 1024 | 64 | 3272.09 | 896 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Recomandări | span | 768 | 64 | 3687.42 | 640 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Recomandări | span | 390 | 16 | 4450.14 | 358 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Ce Spun Mirii și Gazdele | h2 | 1440 | 184 | 3355.06 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce Spun Mirii și Gazdele | h2 | 1024 | 64 | 3308.09 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce Spun Mirii și Gazdele | h2 | 768 | 64 | 3723.42 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce Spun Mirii și Gazdele | h2 | 390 | 16 | 4486.14 | 358 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | center |
| svg (icon) | svg | 1440 | 217 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 97 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 97 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 41 | 4623.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 235 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 115 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 115 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 59 | 4623.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 253 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 133 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 133 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 77 | 4623.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 271 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 151 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 151 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 95 | 4623.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 289 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 169 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 169 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 113 | 4623.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| „Recomand 🙌🏻 Formația a fost super la nunta noas | blockquote | 1440 | 217 | 3572.06 | 275.33 | 216 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Recomand 🙌🏻 Formația a fost super la nunta noas | blockquote | 1024 | 97 | 3525.09 | 216.66 | 264 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Recomand 🙌🏻 Formația a fost super la nunta noas | blockquote | 768 | 97 | 3940.42 | 131.33 | 456 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Recomand 🙌🏻 Formația a fost super la nunta noas | blockquote | 390 | 41 | 4655.14 | 308 | 192 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cristina Lixandru | figcaption | 1440 | 217 | 3812.06 | 275.33 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Cristina Lixandru | figcaption | 1024 | 97 | 3813.09 | 216.66 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Cristina Lixandru | figcaption | 768 | 97 | 4420.42 | 131.33 | 40 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Cristina Lixandru | figcaption | 390 | 41 | 4871.14 | 308 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| svg (icon) | svg | 1440 | 582.33 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 403.66 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 318.33 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 41 | 4957.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 600.33 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 421.66 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 336.33 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 59 | 4957.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 618.33 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 439.66 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 354.33 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 77 | 4957.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 636.33 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 457.66 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 372.33 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 95 | 4957.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 654.33 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 475.66 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 390.33 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 113 | 4957.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| „Ne-au oferit o nunta de nota 10. Pe lângă show- | blockquote | 1440 | 582.33 | 3572.06 | 275.33 | 216 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Ne-au oferit o nunta de nota 10. Pe lângă show- | blockquote | 1024 | 403.66 | 3525.09 | 216.67 | 264 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Ne-au oferit o nunta de nota 10. Pe lângă show- | blockquote | 768 | 318.33 | 3940.42 | 131.33 | 456 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Ne-au oferit o nunta de nota 10. Pe lângă show- | blockquote | 390 | 41 | 4989.14 | 308 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Alexandru Dimov | figcaption | 1440 | 582.33 | 3812.06 | 275.33 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Alexandru Dimov | figcaption | 1024 | 403.66 | 3813.09 | 216.67 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Alexandru Dimov | figcaption | 768 | 318.33 | 4420.42 | 131.33 | 40 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Alexandru Dimov | figcaption | 390 | 41 | 5109.14 | 308 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| svg (icon) | svg | 1440 | 947.66 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 710.33 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 539.66 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 41 | 5195.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 965.66 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 728.33 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 557.66 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 59 | 5195.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 983.66 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 746.33 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 575.66 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 77 | 5195.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1001.66 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 764.33 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 593.66 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 95 | 5195.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1019.66 | 3540.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 782.33 | 3493.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 611.66 | 3908.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 113 | 5195.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| „Nu sunt genul de persoana care scrie recenzii,  | blockquote | 1440 | 947.66 | 3572.06 | 275.34 | 216 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Nu sunt genul de persoana care scrie recenzii,  | blockquote | 1024 | 710.33 | 3525.09 | 216.66 | 264 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Nu sunt genul de persoana care scrie recenzii,  | blockquote | 768 | 539.66 | 3940.42 | 131.33 | 476 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| „Nu sunt genul de persoana care scrie recenzii,  | blockquote | 390 | 41 | 5227.14 | 308 | 168 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Oana Goga | figcaption | 1440 | 947.66 | 3812.06 | 275.34 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Oana Goga | figcaption | 1024 | 710.33 | 3813.09 | 216.66 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Oana Goga | figcaption | 768 | 539.66 | 4440.42 | 131.33 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Oana Goga | figcaption | 390 | 41 | 5419.14 | 308 | 20 | 14 | 20 | 0.70 | 600 | #c4c7c7 | start |
| Rezervă data ta | a | 1440 | 633.27 | 3916.06 | 173.45 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Rezervă data ta | a | 1024 | 425.27 | 3917.09 | 173.45 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Rezervă data ta | a | 768 | 297.27 | 4544.42 | 173.45 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Rezervă data ta | a | 390 | 108.27 | 5507.14 | 173.45 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 788.72 | 3917.06 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 580.72 | 3918.09 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 452.72 | 4545.42 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 263.72 | 5508.14 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Recomandări Ce Spun Mirii și Gazdele] | [„Recomand 🙌🏻 Formația a fost super la nu] | 64 | 64 | 64 | 40 |
| `div.max-w-[1200px]` | [„Recomand 🙌🏻 Formația a fost super la nu] | [Rezervă data ta] | 48 | 48 | 48 | 40 |
| `div.text-center` | Recomandări | Ce Spun Mirii și Gazdele | 16 | 16 | 16 | 16 |
| `div.text-center` | Ce Spun Mirii și Gazdele | div.motif-rule | 24 | 24 | 24 | 24 |
| `div.grid` | [„Recomand 🙌🏻 Formația a fost super la nu] | [„Ne-au oferit o nunta de nota 10. Pe lân] | -358 ¹ | -406 ¹ | -618 ¹ | 16 |
| `div.grid` | [„Ne-au oferit o nunta de nota 10. Pe lân] | [„Nu sunt genul de persoana care scrie re] | -358 ¹ | -406 ¹ | -618 ¹ | 16 |
| `figure.p-6` | div.flex | „Recomand 🙌🏻 Formația a fost super la nunta noas | 16 | 16 | 16 | 16 |
| `figure.p-6` | „Recomand 🙌🏻 Formația a fost super la nunta noas | Cristina Lixandru | 24 | 24 | 24 | 24 |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `figure.p-6` | div.flex | „Ne-au oferit o nunta de nota 10. Pe lângă show- | 16 | 16 | 16 | 16 |
| `figure.p-6` | „Ne-au oferit o nunta de nota 10. Pe lângă show- | Alexandru Dimov | 24 | 24 | 24 | 24 |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `figure.p-6` | div.flex | „Nu sunt genul de persoana care scrie recenzii,  | 16 | 16 | 16 | 16 |
| `figure.p-6` | „Nu sunt genul de persoana care scrie recenzii,  | Oana Goga | 24 | 24 | 24 | 24 |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |
| `div.flex` | svg (icon) | svg (icon) | -16 ¹ | -16 ¹ | -16 ¹ | -16 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 341.328px 341.328px 341.344px | 24px | 24px | da (358) |
| `div.grid` | 1024 | grid | 282.656px 282.672px 282.656px | 24px | 24px | da (406) |
| `div.grid` | 768 | grid | 197.328px 197.328px 197.328px | 24px | 24px | da (618) |
| `div.grid` | 390 | grid | 358px | 16px | 16px | **NU** — 222…318, delta 96 |
| `div.flex` | 1440 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 1024 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 768 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 390 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 1440 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 1024 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 768 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 390 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 1440 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 1024 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 768 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |
| `div.flex` | 390 | flex | 16 + 16 + 16 + 16 + 16 | 2px | 2px | da (16) |

---

## S6 — Ce ne întrebați cel mai des

`section` · clase: `py-16 md:py-24 bg-surface-container-lowest border-y border-outline-variant/10`

Eyebrow: «Întrebări Frecvente»

Titlu: «Ce ne întrebați cel mai des»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 836 | 96/0/96/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 836 | 96/0/96/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 836 | 96/0/96/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 726 | 64/0/64/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 642 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 642 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 642 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 596 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1440 | 1072 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1024 | 896 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 768 | 640 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 390 | 358 | 104 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 1440 | 768 | 374 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 1024 | 768 | 374 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 768 | 640 | 374 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 390 | 358 | 368 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1440 | 1072 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1024 | 896 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 768 | 640 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 390 | 358 | 44 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Întrebări Frecvente | span | 1440 | 184 | 4131.06 | 1072 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 1024 | 64 | 4132.09 | 896 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 768 | 64 | 4759.42 | 640 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 390 | 16 | 5658.14 | 358 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Ce ne întrebați cel mai des | h2 | 1440 | 184 | 4167.06 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h2 | 1024 | 64 | 4168.09 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h2 | 768 | 64 | 4795.42 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h2 | 390 | 16 | 5694.14 | 358 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | center |
| Prețul unei formații pentru 2026-2027? | h3 | 1440 | 361 | 4332.06 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 1024 | 153 | 4333.09 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 768 | 89 | 4960.42 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 390 | 37 | 5823.14 | 256.84 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 4340.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 4341.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 4968.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 5826.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1440 | 337 | 4388.06 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1024 | 129 | 4389.09 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 768 | 65 | 5016.42 | 638 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 390 | 17 | 5865.14 | 356 | 144 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cântați și în afara Bucureștiului? | h3 | 1440 | 361 | 4526.06 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 1024 | 153 | 4527.09 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 768 | 89 | 5154.42 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 390 | 37 | 6047.14 | 215.09 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 4534.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 4535.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5162.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 6050.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 1440 | 337 | 4582.06 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 1024 | 129 | 4583.09 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 768 | 65 | 5210.42 | 638 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 390 | 17 | 6089.14 | 356 | 192 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cum rezerv data — avans și contract? | h3 | 1440 | 361 | 4624.06 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 1024 | 153 | 4625.09 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 768 | 89 | 5252.42 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 390 | 37 | 6127.14 | 243.53 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 4632.06 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 4633.09 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5260.42 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 6130.14 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Data se blochează pe bază de contract și un avan | div | 1440 | 337 | 4680.06 | 766 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 1024 | 129 | 4681.09 | 766 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 768 | 65 | 5308.42 | 638 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 390 | 17 | 6169.14 | 356 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Vezi toate întrebările frecvente | a | 1440 | 553.95 | 4729.06 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 1024 | 345.95 | 4730.09 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 768 | 217.95 | 5357.42 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 390 | 28.95 | 6210.14 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 868.05 | 4742.06 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 660.05 | 4743.09 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 532.05 | 5370.42 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 343.05 | 6223.14 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Întrebări Frecvente Ce ne întrebați cel ] | [Prețul unei formații pentru 2026-2027? P] | 56 | 56 | 56 | 40 |
| `div.max-w-[1200px]` | [Prețul unei formații pentru 2026-2027? P] | [Vezi toate întrebările frecvente] | 48 | 48 | 48 | 40 |
| `div.text-center` | Întrebări Frecvente | Ce ne întrebați cel mai des | 16 | 16 | 16 | 16 |
| `div.text-center` | Ce ne întrebați cel mai des | div.motif-rule | 20 | 20 | 20 | 20 |
| `div.max-w-3xl` | [Prețul unei formații pentru 2026-2027? P] | [Cântați și în afara Bucureștiului? Da. C] | 16 | 16 | 16 | 16 |
| `div.max-w-3xl` | [Cântați și în afara Bucureștiului? Da. C] | [Cum rezerv data — avans și contract? Dat] | 16 | 16 | 16 | 16 |
| `details.group` | [Prețul unei formații pentru 2026-2027?] | Prețul depinde de pachet, de tipul evenimentului | 0 | 0 | 0 | 0 |
| `summary.flex` | Prețul unei formații pentru 2026-2027? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cântați și în afara Bucureștiului?] | Da. Cântăm cel mai des în București, Ploiești, B | 0 | 0 | 0 | 0 |
| `summary.flex` | Cântați și în afara Bucureștiului? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cum rezerv data — avans și contract?] | Data se blochează pe bază de contract și un avan | 0 | 0 | 0 | 0 |
| `summary.flex` | Cum rezerv data — avans și contract? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 256.84 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 215.09 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 243.53 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |

---

## S7 — Rezervă Formație Nuntă

`section` · clase: `py-16 md:py-32 relative overflow-hidden`

Eyebrow: «+40 722 911 485»

Titlu: «Rezervă Formație Nuntă»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 642 | 128/0/128/0 | transparent | none |
| **section** | 1024 | 1024 | 642 | 128/0/128/0 | transparent | none |
| **section** | 768 | 768 | 748 | 128/0/128/0 | transparent | none |
| **section** | 390 | 390 | 452 | 64/0/64/0 | transparent | none |
| **container 1** (`div.absolute`) | 1440 | 1440 | 642 | 0/0/0/0 | #c8c6c5 | none |
| **container 1** (`div.absolute`) | 1024 | 1024 | 642 | 0/0/0/0 | #c8c6c5 | none |
| **container 1** (`div.absolute`) | 768 | 768 | 748 | 0/0/0/0 | #c8c6c5 | none |
| **container 1** (`div.absolute`) | 390 | 390 | 452 | 0/0/0/0 | #c8c6c5 | none |
| **container 2** (`div.max-w-[1200px]`) | 1440 | 1200 | 386 | 0/64/0/64 | transparent | none |
| **container 2** (`div.max-w-[1200px]`) | 1024 | 1024 | 386 | 0/64/0/64 | transparent | none |
| **container 2** (`div.max-w-[1200px]`) | 768 | 768 | 492 | 0/64/0/64 | transparent | none |
| **container 2** (`div.max-w-[1200px]`) | 390 | 390 | 324 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.glass-panel`) | 1440 | 1072 | 386 | 80/80/80/80 | #1c1b1b @0.85 | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-panel`) | 1024 | 896 | 386 | 80/80/80/80 | #1c1b1b @0.85 | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-panel`) | 768 | 640 | 492 | 80/80/80/80 | #1c1b1b @0.85 | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-panel`) | 390 | 358 | 324 | 32/32/32/32 | #1c1b1b @0.85 | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rezervă Formație Nuntă | h2 | 1440 | 265 | 5079.06 | 910 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Rezervă Formație Nuntă | h2 | 1024 | 145 | 5080.09 | 734 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Rezervă Formație Nuntă | h2 | 768 | 145 | 5707.42 | 478 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Rezervă Formație Nuntă | h2 | 390 | 49 | 6416.14 | 292 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | center |
| Disponibilă pentru nunți, botezuri și evenimente | p | 1440 | 432 | 5159.06 | 576 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Disponibilă pentru nunți, botezuri și evenimente | p | 1024 | 224 | 5160.09 | 576 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Disponibilă pentru nunți, botezuri și evenimente | p | 768 | 145 | 5787.42 | 478 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Disponibilă pentru nunți, botezuri și evenimente | p | 390 | 49 | 6456.14 | 292 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| svg (icon) | svg | 1440 | 504.27 | 5269.06 | 20 | 20 | 20 | 28 | normal | 400 | #e5e2e1 | center |
| svg (icon) | svg | 1024 | 296.27 | 5270.09 | 20 | 20 | 20 | 28 | normal | 400 | #e5e2e1 | center |
| svg (icon) | svg | 768 | 285.59 | 5925.42 | 20 | 20 | 20 | 28 | normal | 400 | #e5e2e1 | center |
| svg (icon) | svg | 390 | 112.30 | 6570.14 | 20 | 20 | 20 | 28 | normal | 400 | #e5e2e1 | center |
| +40 722 911 485 | span | 1440 | 554.27 | 5263.06 | 160.81 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| +40 722 911 485 | span | 1024 | 346.27 | 5264.09 | 160.81 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| +40 722 911 485 | span | 768 | 335.59 | 5919.42 | 160.81 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | center |
| +40 722 911 485 | span | 390 | 158.30 | 6568.14 | 129.41 | 24 | 20 | 24 | normal | 400 | #e5e2e1 | center |
| Cere ofertă | a | 1440 | 780.08 | 5256.06 | 169.66 | 46 | 14 | 20 | 0.70 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 1024 | 572.08 | 5257.09 | 169.66 | 46 | 14 | 20 | 0.70 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 768 | 299.17 | 5991.42 | 169.66 | 46 | 14 | 20 | 0.70 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 390 | 114.64 | 6624.14 | 160.72 | 50 | 12 | 24 | 1.20 | 400 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | div.absolute | [Rezervă Formație Nuntă Disponibilă pentr] | -514 | -514 | -620 | -388 |
| `div.glass-panel` | Rezervă Formație Nuntă | Disponibilă pentru nunți, botezuri și evenimente | 24 | 24 | 24 | 16 |
| `div.glass-panel` | Disponibilă pentru nunți, botezuri și evenimente | [+40 722 911 485 Cere ofertă] | 40 | 40 | 40 | 32 |
| `div.flex` | [+40 722 911 485] | div.hidden | -48 ¹ | -48 ¹ | n/r | n/r |
| `div.flex` | div.hidden | Cere ofertă | -47 ¹ | -47 ¹ | n/r | n/r |
| `a.flex` | span.w-10 | +40 722 911 485 | -40 ¹ | -40 ¹ | -40 ¹ | -32 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 224.81 + 1 + 169.66 | 32px | 32px | **NU** — 46…48, delta 2 |
| `div.flex` | 1024 | flex | 224.81 + 1 + 169.66 | 32px | 32px | **NU** — 46…48, delta 2 |
| `div.flex` | 768 | flex | 224.81 + 169.66 | 32px | 32px | **NU** — 46…48, delta 2 |
| `div.flex` | 390 | flex | 185.41 + 160.72 | 24px | 24px | **NU** — 40…50, delta 10 |
| `a.flex` | 1440 | flex | 48 + 160.81 | 16px | 16px | **NU** — 32…48, delta 16 |
| `a.flex` | 1024 | flex | 48 + 160.81 | 16px | 16px | **NU** — 32…48, delta 16 |
| `a.flex` | 768 | flex | 48 + 160.81 | 16px | 16px | **NU** — 32…48, delta 16 |
| `a.flex` | 390 | flex | 40 + 129.41 | 16px | 16px | **NU** — 24…40, delta 16 |

---

## Ce nu se vede din clase

### `line-height` mostenit de la `<body>`, nu setat pe element

- `span` «Nuntă · Botez · Corporate» la 390 — font-size 12px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.00)
- `h2` «Muzică pentru nuntă, botez și corporate» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `span` «Oferte» la 390 — font-size 12px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.00)
- `h2` «Peste 15 ani pe scenă» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `span` «Ani pe scenă» la 390 — font-size 12px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.00)
- `span` «Albume proprii» la 390 — font-size 12px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.00)
- `h2` «Vezi cum arată un eveniment» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `h2` «Ce Spun Mirii și Gazdele» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `h2` «Ce ne întrebați cel mai des» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `h2` «Rezervă Formație Nuntă» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `span` «+40 722 911 485» la 390 — font-size 20px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 1.20)
- `a` «Cere ofertă» la 390 — font-size 12px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 2.00)

### `font-weight` diferit de ce sugereaza numele clasei

- `span` «Nuntă · Botez · Corporate» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400/600, font-size masurat 12/14px
- `h2` «Muzică pentru nuntă, botez și corporate» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `span` «Oferte» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400/600, font-size masurat 12/14px
- `h2` «Pachete pentru 2026–2027» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[32px]`; weight rezolvat 400/500, font-size masurat 32/48px
- `p` «Formație live, interpreți, DJ/MC și producție te» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `h2` «Peste 15 ani pe scenă» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `span` «15+» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400, font-size masurat 28/36px
- `span` «Ani pe scenă» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400/600, font-size masurat 12/14px
- `span` «3» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400, font-size masurat 28/36px
- `span` «Albume proprii» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400/600, font-size masurat 12/14px
- `h2` «Vezi cum arată un eveniment» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `h2` «Ce Spun Mirii și Gazdele» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `h2` «Ce ne întrebați cel mai des» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `h3` «Prețul unei formații pentru 2026-2027?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cântați și în afara Bucureștiului?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cum rezerv data — avans și contract?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Rezervă Formație Nuntă» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/48px
- `p` «Disponibilă pentru nunți, botezuri și evenimente» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «+40 722 911 485» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `a` «Cere ofertă» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400/600, font-size masurat 12/14px

### Borduri care vin din `assets/styles.css`, nu din clase

- `span.motif-rule__gem` «span.motif-rule__gem» — T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.bg-accent` «Vezi ofertele» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Formație live Formație de nuntă în Bucur]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.video-card__play` «span.video-card__play» — T 2px #ffffff @0.85, R 2px #ffffff @0.85, B 2px #ffffff @0.85, L 2px #ffffff @0.85, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Muzică populară Colaj de Moldova, live l]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `div.glass-panel` «[Rezervă Formație Nuntă Disponibilă pentr]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «Formație live și sonorizare proprie, cu repertor» declara `mb-*` ∈ {16/24/32}px, dar distanta reala pana la «Detalii» e 40px la 768
- «15+» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Ani pe scenă» e 8px la 1440
- «15+» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Ani pe scenă» e 8px la 1024
- «15+» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Ani pe scenă» e 8px la 768
- «15+» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Ani pe scenă» e 10px la 390
- «3» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Albume proprii» e 8px la 1440
- «3» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Albume proprii» e 8px la 1024
- «3» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Albume proprii» e 8px la 768
- «3» declara `mb-*` ∈ {4}px, dar distanta reala pana la «Albume proprii» e 10px la 390

### Elemente care nu se randeaza la un viewport

- `div.hidden` «div.hidden» — `getClientRects().length == 0` la 768, 390 (randat la 1440, 1024); `display` raportat: block

### Suprapuneri intre elemente

- in `div.md:col-span-5`: «div.border» si «div.absolute» se suprapun pe verticala cu 160px la 1440 (suprapunere orizontala 160px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.md:col-span-5`: «div.border» si «div.absolute» se suprapun pe verticala cu 160px la 1024 (suprapunere orizontala 160px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.md:col-span-5`: «div.border» si «div.absolute» se suprapun pe verticala cu 160px la 768 (suprapunere orizontala 160px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.md:col-span-5`: «div.border» si «div.absolute» se suprapun pe verticala cu 104px la 390 (suprapunere orizontala 104px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img XFdALRgk7Fg.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 178.37px la 1440 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img XFdALRgk7Fg.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 153.62px la 1024 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img XFdALRgk7Fg.jpg» si «span.video-card__veil» se suprapun pe verticala cu 171.25px la 768 (suprapunere orizontala 306px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 117.62px la 768 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Formație live Formație de nuntă în Bucur]» se suprapun pe verticala cu 56.57px la 768 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img XFdALRgk7Fg.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.38px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 131.69px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Formație live Formație de nuntă în Bucur]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img hzOdwacBNN0.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img hzOdwacBNN0.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img hzOdwacBNN0.jpg» si «span.video-card__veil» se suprapun pe verticala cu 171.25px la 768 (suprapunere orizontala 306px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Muzică populară Colaj de Moldova, live l]» se suprapun pe verticala cu 56.57px la 768 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img hzOdwacBNN0.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.37px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Muzică populară Colaj de Moldova, live l]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Rezervă Formație Nuntă Disponibilă pentr]» se suprapun pe verticala cu 514px la 1440 (suprapunere orizontala 1200px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Rezervă Formație Nuntă Disponibilă pentr]» se suprapun pe verticala cu 514px la 1024 (suprapunere orizontala 1024px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Rezervă Formație Nuntă Disponibilă pentr]» se suprapun pe verticala cu 620px la 768 (suprapunere orizontala 768px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Rezervă Formație Nuntă Disponibilă pentr]» se suprapun pe verticala cu 388px la 390 (suprapunere orizontala 390px, position absolute/relative) — stratificare intentionata (`position: absolute`)

### Ordine vizuala diferita de ordinea din document

- in `div.max-w-[1200px]` la 390 — ordinea vizuala difera de cea din document: document = «div.md:col-span-5» → «[Peste 15 ani pe scenă Muzica nu este doa]»; vizual = «[Peste 15 ani pe scenă Muzica nu este doa]» → «div.md:col-span-5» (utilitare `order-*`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Muzică pentru nuntă, botez și corporate | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 1440: 32/32/32/32<br>1024: 32/32/32/32<br>768: 24/24/24/24<br>390: 24/24/24/24 | x 24px / y 24px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 341.33 + 341.33 + 341.34 · 1024: 282.66 + 282.67 + 282.66 · 768: 197.33 + 197.33 + 197.33 · 390: 358 + 358 + 358 |
| Pachete pentru 2026–2027 | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | 1440: x 64px / y 64px · 1024: x 64px / y 64px · 768: x 64px / y 64px · 390: x 40px / y 40px | in `div.flex` (lat. 1072 la 1440, flex):<br>1440: 624 + 384 · 1024: 448 + 384 · 768: 640 + 640 · 390: 358 + 358 |
| Peste 15 ani pe scenă | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | 1440: x 24px / y 24px · 1024: x 24px / y 24px · 768: x 24px / y 24px · 390: x 40px / y 40px | in `div.max-w-[1200px]` (lat. 1200 la 1440, grid):<br>1440: 432.66 + 615.34 · 1024: 359.33 + 512.67 · 768: 252.66 + 363.34 · 390: 358 + 358 |
| Vezi cum arată un eveniment | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | 1440: x 24px / y 24px · 1024: x 24px / y 24px · 768: x 24px / y 24px · 390: x 16px / y 16px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 524 + 524 · 1024: 436 + 436 · 768: 308 + 308 · 390: 358 + 358 |
| Ce Spun Mirii și Gazdele | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 1440: 32/32/32/32<br>1024: 32/32/32/32<br>768: 32/32/32/32<br>390: 24/24/24/24 | 1440: x 24px / y 24px · 1024: x 24px / y 24px · 768: x 24px / y 24px · 390: x 16px / y 16px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 341.33 + 341.33 + 341.34 · 1024: 282.66 + 282.67 + 282.66 · 768: 197.33 + 197.33 + 197.33 · 390: 358 + 358 + 358 |
| Ce ne întrebați cel mai des | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 766 la 1440, flex):<br>1440: 390.91 + 16 · 1024: 390.91 + 16 · 768: 390.91 + 16 · 390: 256.84 + 16 |
| Rezervă Formație Nuntă | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 128 sus / 128 jos · 1024: 128 sus / 128 jos · 768: 128 sus / 128 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 / 12/32/12/32 | 1440: x 32px / y 32px · 1024: x 32px / y 32px · 768: x 32px / y 32px · 390: x 24px / y 24px | in `div.flex` (lat. 910 la 1440, flex):<br>1440: 224.81 + 1 + 169.66 · 1024: 224.81 + 1 + 169.66 · 768: 224.81 + 169.66 · 390: 185.41 + 160.72 |
