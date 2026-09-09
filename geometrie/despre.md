# Geometrie randata — `despre.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/despre.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 3092.50 | 128/0/0/0 | transparent | none |
| `<main>` | 1024 | 1024 | 2825.19 | 128/0/0/0 | transparent | none |
| `<main>` | 768 | 768 | 5057.13 | 80/0/0/0 | transparent | none |
| `<main>` | 390 | 390 | 4070.47 | 80/0/0/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 3524px, 1024 → 3256px, 768 → 5534px, 390 → 4657px.

Sectiuni masurate: **6**.

---

## S1 — Despre mine

`section` · clase: `relative min-h-[32vh] md:min-h-[36vh] flex items-end justify-center overflow-hidden mb-12 md:mb-16 px-6 md:px-margin-desktop py-10`

Eyebrow: «Despre»

Titlu: «Despre mine»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 324 | 40/64/40/64 | transparent | none |
| **section** | 1024 | 1024 | 300 | 40/64/40/64 | transparent | none |
| **section** | 768 | 768 | 368.63 | 40/64/40/64 | transparent | none |
| **section** | 390 | 390 | 270.08 | 40/24/40/24 | transparent | none |
| **container 1** (`div.absolute`) | 1440 | 1440 | 324 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 1024 | 1024 | 300 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 768 | 768 | 368.63 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 390 | 390 | 270.08 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`picture.block`) | 1440 | 1440 | 324 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`picture.block`) | 1024 | 1024 | 300 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`picture.block`) | 768 | 768 | 368.63 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`picture.block`) | 390 | 390 | 270.08 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.absolute`) | 1440 | 1440 | 324 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 1024 | 1024 | 300 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 768 | 768 | 368.63 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 390 | 390 | 270.08 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.relative`) | 1440 | 260.83 | 220 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 1024 | 260.83 | 220 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 768 | 260.83 | 220 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 390 | 177.53 | 185.50 | 32/16/32/16 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1440 | 228.83 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1024 | 228.83 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 768 | 228.83 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 390 | 145.53 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 1440 | 228.83 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 1024 | 228.83 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 768 | 228.83 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 390 | 145.53 | 37.50 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.motif-separator`) | 1440 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 3 (`div.motif-separator`) | 1024 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 3 (`div.motif-separator`) | 768 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 3 (`div.motif-separator`) | 390 | 96 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img hora-nunta-invitati-1024.jpg | img | 1440 | 0 | 128 | 1440 | 324 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 1024 | 0 | 128 | 1024 | 300 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 768 | 0 | 80 | 768 | 368.63 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 390 | 0 | 80 | 390 | 270.08 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Despre | span | 1440 | 605.58 | 232 | 228.83 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Despre | span | 1024 | 397.58 | 208 | 228.83 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Despre | span | 768 | 269.58 | 228.63 | 228.83 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Despre | span | 390 | 122.23 | 156.58 | 145.53 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Despre mine | h1 | 1440 | 605.58 | 264 | 228.83 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Despre mine | h1 | 1024 | 397.58 | 240 | 228.83 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Despre mine | h1 | 768 | 269.58 | 260.63 | 228.83 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Despre mine | h1 | 390 | 122.23 | 188.58 | 145.53 | 37.50 | 30 | 37.50 | normal | 400 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | div.absolute | [Despre Despre mine] | -260 | -260 | -260 | -225.50 |
| `div.absolute` | picture.block | div.absolute | -324 | -300 | -368.63 | -270.08 |
| `div.relative` | Despre | Despre mine | 12 | 12 | 12 | 12 |
| `div.relative` | Despre mine | div.motif-separator | 28 | 28 | 28 | 28 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `section` | 1440 | flex | 1440 + 260.83 | 0px | 0px | **NU** — 220…324, delta 104 |
| `section` | 1024 | flex | 1024 + 260.83 | 0px | 0px | **NU** — 220…300, delta 80 |
| `section` | 768 | flex | 768 + 260.83 | 0px | 0px | **NU** — 220…368.63, delta 148.63 |
| `section` | 390 | flex | 390 + 177.53 | 0px | 0px | **NU** — 185.50…270.08, delta 84.58 |

---

## S2 — Numele meu este Ioana Balan. Sunt o fire visăt

`section` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 497.50 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 440 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 1185.50 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 977 | 0/24/0/24 | transparent | none |
| **container interior** | 1440 | 1072 | 497.50 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 896 | 440 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 1185.50 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 342 | 977 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 1440 | 604.80 | 356 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 1024 | 499.19 | 440 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 768 | 640 | 328 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 390 | 342 | 514 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.order-1`) | 1440 | 403.20 | 497.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 1024 | 332.80 | 409.48 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 768 | 640 | 793.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 390 | 342 | 423 | 8/8/8/8 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Numele meu este Ioana Balan. Sunt o fire visătoa | p | 1440 | 184 | 586.75 | 604.80 | 168 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Numele meu este Ioana Balan. Sunt o fire visătoa | p | 1024 | 64 | 492 | 499.19 | 196 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Numele meu este Ioana Balan. Sunt o fire visătoa | p | 768 | 64 | 1370.13 | 640 | 140 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Numele meu este Ioana Balan. Sunt o fire visătoa | p | 390 | 24 | 861.08 | 342 | 234 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| În fiecare zi învăț, perseverez și mă perfecțion | p | 1440 | 184 | 774.75 | 604.80 | 168 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| În fiecare zi învăț, perseverez și mă perfecțion | p | 1024 | 64 | 708 | 499.19 | 224 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| În fiecare zi învăț, perseverez și mă perfecțion | p | 768 | 64 | 1530.13 | 640 | 168 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| În fiecare zi învăț, perseverez și mă perfecțion | p | 390 | 24 | 1115.08 | 342 | 260 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| img ioana-balan-ie-broderie-aurie-1440.jpg | img | 1440 | 865.80 | 529 | 377.20 | 471.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-broderie-aurie-1440.jpg | img | 1024 | 640.19 | 520.25 | 306.80 | 383.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-broderie-aurie-1440.jpg | img | 768 | 77 | 525.63 | 614 | 767.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-broderie-aurie-1440.jpg | img | 390 | 33 | 407.08 | 324 | 405 | 16 | 24 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | [Numele meu este Ioana Balan. Sunt o fire] | div.order-1 | -426.75 ¹ | -424.75 ¹ | -1185.50 | -977 |
| `div.order-2` | Numele meu este Ioana Balan. Sunt o fire visătoa | În fiecare zi învăț, perseverez și mă perfecțion | 20 | 20 | 20 | 20 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 604.797px 403.203px | 64px | 64px | **NU** — 356…497.50, delta 141.50 |
| `div.grid` | 1024 | grid | 499.188px 332.797px | 64px | 64px | **NU** — 409.48…440, delta 30.52 |
| `div.grid` | 768 | grid | 640px | 64px | 64px | **NU** — 328…793.50, delta 465.50 |
| `div.grid` | 390 | grid | 342px | 40px | 40px | **NU** — 423…514, delta 91 |

---

## S3 — Rădăcini

`section` · clase: `bg-surface-container-lowest border-y border-outline-variant/10 py-16 md:py-[72px] mb-16`

Titlu: «Rădăcini»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 699.50 | 72/0/72/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 601.70 | 72/0/72/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 768 | 768 | 1311.50 | 72/0/72/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **section** | 390 | 390 | 1009 | 64/0/64/0 | #0e0e0e | T 1px #444748 @0.1, B 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 553.50 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 455.70 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 1165.50 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 879 | 0/24/0/24 | transparent | none |
| └ coloana 1 (`div.grid`) | 1440 | 1072 | 553.50 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.grid`) | 1024 | 896 | 455.70 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.grid`) | 768 | 640 | 1165.50 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.grid`) | 390 | 342 | 879 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-ie-cosita-impletita-1440.jpg | img | 1440 | 197 | 1163.50 | 422 | 527.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-cosita-impletita-1440.jpg | img | 1024 | 77 | 1082 | 343.77 | 429.70 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-cosita-impletita-1440.jpg | img | 768 | 77 | 1848.13 | 614 | 767.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-ie-cosita-impletita-1440.jpg | img | 390 | 33 | 1513.08 | 324 | 405 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Rădăcini | h2 | 1440 | 696 | 1259.25 | 560 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h2 | 1024 | 497.77 | 1100.84 | 462.23 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h2 | 768 | 64 | 2692.63 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h2 | 390 | 24 | 1967.08 | 342 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| Prima persoană care mi-a îndrumat pașii în muzic | p | 1440 | 696 | 1371.25 | 560 | 224 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Prima persoană care mi-a îndrumat pașii în muzic | p | 1024 | 497.77 | 1212.84 | 462.23 | 280 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Prima persoană care mi-a îndrumat pașii în muzic | p | 768 | 64 | 2804.63 | 640 | 196 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Prima persoană care mi-a îndrumat pașii în muzic | p | 390 | 24 | 2071.08 | 342 | 312 | 16 | 26 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | div.border | [Rădăcini Prima persoană care mi-a îndrum] | -444.75 ¹ | -423.86 ¹ | 64 | 40 |
| `div.space-y-6` | Rădăcini | div.motif-separator | 24 | 24 | 24 | 24 |
| `div.space-y-6` | div.motif-separator | Prima persoană care mi-a îndrumat pașii în muzic | 24 | 24 | 24 | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 448px 560px | 64px | 64px | **NU** — 336…553.50, delta 217.50 |
| `div.grid` | 1024 | grid | 369.766px 462.234px | 64px | 64px | **NU** — 392…455.70, delta 63.70 |
| `div.grid` | 768 | grid | 640px | 64px | 64px | **NU** — 308…793.50, delta 485.50 |
| `div.grid` | 390 | grid | 342px | 40px | 40px | **NU** — 416…423, delta 7 |

---

## S4 — ca o frumoasă și de preț zestre, purtată cu mâ

`section` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 199 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 199 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 199 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 157.39 | 0/24/0/24 | transparent | none |
| **container interior** | 1440 | 480 | 199 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 480 | 199 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 480 | 199 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 342 | 157.39 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.motif-separator`) | 1440 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 1 (`div.motif-separator`) | 1024 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 1 (`div.motif-separator`) | 768 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 1 (`div.motif-separator`) | 390 | 96 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`blockquote.font-display-lg`) | 1440 | 480 | 135 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`blockquote.font-display-lg`) | 1024 | 480 | 135 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`blockquote.font-display-lg`) | 768 | 480 | 135 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`blockquote.font-display-lg`) | 390 | 342 | 101.39 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ca o frumoasă și de preț zestre, purtată cu mând | blockquote | 1440 | 480 | 1905 | 480 | 135 | 36 | 45 | normal | 400 | #e5e2e1 | center |
| ca o frumoasă și de preț zestre, purtată cu mând | blockquote | 1024 | 272 | 1725.70 | 480 | 135 | 36 | 45 | normal | 400 | #e5e2e1 | center |
| ca o frumoasă și de preț zestre, purtată cu mând | blockquote | 768 | 144 | 3201.63 | 480 | 135 | 36 | 45 | normal | 400 | #e5e2e1 | center |
| ca o frumoasă și de preț zestre, purtată cu mând | blockquote | 390 | 24 | 2568.08 | 342 | 101.39 | 26 | 33.80 | normal | 400 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `figure.max-w-[30rem]` | div.motif-separator | ca o frumoasă și de preț zestre, purtată cu mând | 40 | 40 | 40 | 32 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S5 — Primii pași

`section` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-16`

Titlu: «Primii pași»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 497.50 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 409.48 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 1165.50 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 853 | 0/24/0/24 | transparent | none |
| **container interior** | 1440 | 1072 | 497.50 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 896 | 409.48 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 1165.50 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 342 | 853 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 1440 | 604.80 | 308 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 1024 | 499.19 | 336 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 768 | 640 | 308 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.order-2`) | 390 | 342 | 390 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.order-1`) | 1440 | 403.20 | 497.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 1024 | 332.80 | 409.48 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 768 | 640 | 793.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.order-1`) | 390 | 342 | 423 | 8/8/8/8 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Primii pași | h2 | 1440 | 184 | 2198.75 | 604.80 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Primii pași | h2 | 1024 | 64 | 1961.44 | 499.19 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Primii pași | h2 | 768 | 64 | 4258.13 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Primii pași | h2 | 390 | 24 | 3196.47 | 342 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| Am început prin a fi apreciată de cei apropiați. | p | 1440 | 184 | 2310.75 | 604.80 | 196 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Am început prin a fi apreciată de cei apropiați. | p | 1024 | 64 | 2073.44 | 499.19 | 224 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Am început prin a fi apreciată de cei apropiați. | p | 768 | 64 | 4370.13 | 640 | 196 | 18 | 28 | normal | 400 | #c4c7c7 | start |
| Am început prin a fi apreciată de cei apropiați. | p | 390 | 24 | 3300.47 | 342 | 286 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 1440 | 865.80 | 2117 | 377.20 | 471.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 1024 | 640.19 | 1937.70 | 306.80 | 383.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 768 | 77 | 3413.63 | 614 | 767.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-scena-costum-rosu-1440.jpg | img | 390 | 33 | 2742.47 | 324 | 405 | 16 | 24 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | [Primii pași Am început prin a fi aprecia] | div.order-1 | -402.75 ¹ | -372.74 ¹ | -1165.50 | -853 |
| `div.order-2` | Primii pași | div.motif-separator | 24 | 24 | 24 | 24 |
| `div.order-2` | div.motif-separator | Am început prin a fi apreciată de cei apropiați. | 24 | 24 | 24 | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 604.797px 403.203px | 64px | 64px | **NU** — 308…497.50, delta 189.50 |
| `div.grid` | 1024 | grid | 499.188px 332.797px | 64px | 64px | **NU** — 336…409.48, delta 73.48 |
| `div.grid` | 768 | grid | 640px | 64px | 64px | **NU** — 308…793.50, delta 485.50 |
| `div.grid` | 390 | grid | 342px | 40px | 40px | **NU** — 390…423, delta 33 |

---

## S6 — Hai să ne cunoaștem

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-t border-outline-variant/10 text-center`

Titlu: «Hai să ne cunoaștem»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 427 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 427 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 768 | 768 | 427 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 390 | 390 | 420 | 64/0/64/0 | #1c1b1b | T 1px #444748 @0.1 |
| **container interior** | 1440 | 672 | 234 | 0/16/0/16 | transparent | none |
| **container interior** | 1024 | 672 | 234 | 0/16/0/16 | transparent | none |
| **container interior** | 768 | 672 | 234 | 0/16/0/16 | transparent | none |
| **container interior** | 390 | 390 | 291 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`h2.font-display-lg`) | 1440 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-display-lg`) | 1024 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-display-lg`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-display-lg`) | 390 | 358 | 35 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 1440 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 1024 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 390 | 358 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 1440 | 640 | 62 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 1024 | 640 | 62 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 768 | 640 | 62 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 390 | 358 | 124 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hai să ne cunoaștem | h2 | 1440 | 400 | 2762.50 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Hai să ne cunoaștem | h2 | 1024 | 192 | 2495.19 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Hai să ne cunoaștem | h2 | 768 | 64 | 4727.13 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Hai să ne cunoaștem | h2 | 390 | 16 | 3715.47 | 358 | 35 | 28 | 35 | normal | 400 | #e5e2e1 | center |
| Scrieți-mi câteva rânduri despre evenimentul dum | p | 1440 | 400 | 2838.50 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-mi câteva rânduri despre evenimentul dum | p | 1024 | 192 | 2571.19 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-mi câteva rânduri despre evenimentul dum | p | 768 | 64 | 4803.13 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-mi câteva rânduri despre evenimentul dum | p | 390 | 16 | 3770.47 | 358 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Scrieți-mi pe WhatsApp | a | 1440 | 441.23 | 2934.50 | 310.78 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-mi pe WhatsApp | a | 1024 | 233.23 | 2667.19 | 310.78 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-mi pe WhatsApp | a | 768 | 105.23 | 4899.13 | 310.78 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-mi pe WhatsApp | a | 390 | 16 | 3882.47 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| +40 722 911 485 | a | 1440 | 768.02 | 2934.50 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 1024 | 560.02 | 2667.19 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 768 | 432.02 | 4899.13 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 390 | 16 | 3952.47 | 358 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-2xl` | Hai să ne cunoaștem | Scrieți-mi câteva rânduri despre evenimentul dum | 20 | 20 | 20 | 20 |
| `div.max-w-2xl` | Scrieți-mi câteva rânduri despre evenimentul dum | [Scrieți-mi pe WhatsApp +40 722 911 485] | 40 | 40 | 40 | 40 |
| `div.flex` | Scrieți-mi pe WhatsApp | +40 722 911 485 | -62 ¹ | -62 ¹ | -62 ¹ | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 310.78 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 1024 | flex | 310.78 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 768 | flex | 310.78 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 390 | flex | 358 + 358 | 16px | 16px | da (54) |

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Despre mine» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `h2` «Rădăcini» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `blockquote` «ca o frumoasă și de preț zestre, purtată cu mând» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[26px]`; weight rezolvat 400, font-size masurat 26/36px
- `h2` «Primii pași» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `h2` «Hai să ne cunoaștem» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/48px

### Borduri care vin din `assets/styles.css`, nu din clase

- `a.inline-block` «Scrieți-mi pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «Despre mine» declara `mb-*` ∈ {20}px, dar distanta reala pana la «div.motif-separator» e 28px la 1440
- «Despre mine» declara `mb-*` ∈ {20}px, dar distanta reala pana la «div.motif-separator» e 28px la 1024
- «Despre mine» declara `mb-*` ∈ {20}px, dar distanta reala pana la «div.motif-separator» e 28px la 768
- «Despre mine» declara `mb-*` ∈ {20}px, dar distanta reala pana la «div.motif-separator» e 28px la 390

### Suprapuneri intre elemente

- in `section`: «div.absolute» si «[Despre Despre mine]» se suprapun pe verticala cu 260px la 1440 (suprapunere orizontala 260.83px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Despre Despre mine]» se suprapun pe verticala cu 260px la 1024 (suprapunere orizontala 260.83px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Despre Despre mine]» se suprapun pe verticala cu 260px la 768 (suprapunere orizontala 260.83px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Despre Despre mine]» se suprapun pe verticala cu 225.50px la 390 (suprapunere orizontala 177.54px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «picture.block» si «div.absolute» se suprapun pe verticala cu 324px la 1440 (suprapunere orizontala 1440px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «picture.block» si «div.absolute» se suprapun pe verticala cu 300px la 1024 (suprapunere orizontala 1024px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «picture.block» si «div.absolute» se suprapun pe verticala cu 368.63px la 768 (suprapunere orizontala 768px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «picture.block» si «div.absolute» se suprapun pe verticala cu 270.08px la 390 (suprapunere orizontala 390px, position static/absolute) — stratificare intentionata (`position: absolute`)

### Ordine vizuala diferita de ordinea din document

- in `div.grid` la 768 — ordinea vizuala difera de cea din document: document = «[Numele meu este Ioana Balan. Sunt o fire]» → «div.order-1»; vizual = «div.order-1» → «[Numele meu este Ioana Balan. Sunt o fire]» (utilitare `order-*`)
- in `div.grid` la 390 — ordinea vizuala difera de cea din document: document = «[Numele meu este Ioana Balan. Sunt o fire]» → «div.order-1»; vizual = «div.order-1» → «[Numele meu este Ioana Balan. Sunt o fire]» (utilitare `order-*`)
- in `div.grid` la 768 — ordinea vizuala difera de cea din document: document = «[Primii pași Am început prin a fi aprecia]» → «div.order-1»; vizual = «div.order-1» → «[Primii pași Am început prin a fi aprecia]» (utilitare `order-*`)
- in `div.grid` la 390 — ordinea vizuala difera de cea din document: document = «[Primii pași Am început prin a fi aprecia]» → «div.order-1»; vizual = «div.order-1» → «[Primii pași Am început prin a fi aprecia]» (utilitare `order-*`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Despre mine | 1440: 1440 · 1024: 1024 · 768: 768 · 390: 390 | vert (sectiune): 40 sus / 40 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Numele meu este Ioana Balan. Sunt o fire visăt | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | 1440: 0/0/0/0 / 12/12/12/12<br>1024: 0/0/0/0 / 12/12/12/12<br>768: 0/0/0/0 / 12/12/12/12<br>390: 0/0/0/0 / 8/8/8/8 | 1440: x 64px / y 64px · 1024: x 64px / y 64px · 768: x 64px / y 64px · 390: x 40px / y 40px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 604.80 + 403.20 · 1024: 499.19 + 332.80 · 768: 640 + 640 · 390: 342 + 342 |
| Rădăcini | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 1440: 72 sus / 72 jos · 1024: 72 sus / 72 jos · 768: 72 sus / 72 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | 1440: 0/0/0/0 / 12/12/12/12<br>1024: 0/0/0/0 / 12/12/12/12<br>768: 0/0/0/0 / 12/12/12/12<br>390: 0/0/0/0 / 8/8/8/8 | 1440: x 64px / y 64px · 1024: x 64px / y 64px · 768: x 64px / y 64px · 390: x 40px / y 40px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 448 + 560 · 1024: 369.77 + 462.23 · 768: 640 + 640 · 390: 342 + 342 |
| ca o frumoasă și de preț zestre, purtată cu mâ | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | — | — | o singura coloana |
| Primii pași | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | 1440: 0/0/0/0 / 12/12/12/12<br>1024: 0/0/0/0 / 12/12/12/12<br>768: 0/0/0/0 / 12/12/12/12<br>390: 0/0/0/0 / 8/8/8/8 | 1440: x 64px / y 64px · 1024: x 64px / y 64px · 768: x 64px / y 64px · 390: x 40px / y 40px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 604.80 + 403.20 · 1024: 499.19 + 332.80 · 768: 640 + 640 · 390: 342 + 342 |
| Hai să ne cunoaștem | 1440: 640 · 1024: 640 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 16 L / 16 R | 1440: 20/48/20/48<br>1024: 20/48/20/48<br>768: 20/48/20/48<br>390: 16/32/16/32 | x 16px / y 16px | in `div.flex` (lat. 640 la 1440, flex):<br>1440: 310.78 + 230.73 · 1024: 310.78 + 230.73 · 768: 310.78 + 230.73 · 390: 358 + 358 |
