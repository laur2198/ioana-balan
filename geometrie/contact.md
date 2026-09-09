# Geometrie randata — `contact.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/contact.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 1190.75 | 160/0/0/0 | transparent | none |
| `<main>` | 1024 | 1024 | 1215.13 | 160/0/0/0 | transparent | none |
| `<main>` | 768 | 768 | 1864.75 | 160/0/0/0 | transparent | none |
| `<main>` | 390 | 390 | 2113.50 | 128/0/0/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 1622px, 1024 → 1646px, 768 → 2342px, 390 → 2701px.

Sectiuni masurate: **4**.

---

## S1 — div.absolute

`div` · clase: `absolute inset-0 motif-texture pointer-events-none`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 1190.75 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 1024 | 1215.13 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 768 | 1864.75 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 390 | 2113.50 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S2 — div.absolute

`div` · clase: `absolute top-0 right-0 w-1/2 h-full hidden lg:block opacity-20 pointer-events-none`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 720 | 1190.75 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 512 | 1215.13 | 0/0/0/0 | transparent | none |
| **section** | 768 | **nerandat** | — | — | — | — |
| **section** | 390 | **nerandat** | — | — | — | — |
| **container interior** | 1440 | 720 | 1190.75 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 512 | 1215.13 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | **nerandat** | — | — | — | — |
| **container interior** | 390 | **nerandat** | — | — | — | — |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 1440 | 720 | 0 | 720 | 1190.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 1024 | 512 | 0 | 512 | 1215.13 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 768 | **nerandat** | | | | | | | | | |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 390 | **nerandat** | | | | | | | | | |

---

## S3 — Rezervări și Contact Ioana Balan

`div` · clase: `col-span-12 lg:col-span-5 flex flex-col justify-center space-y-10 md:space-y-12`

Eyebrow: «Email Oficial»

Titlu: «Rezervări și Contact Ioana Balan»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 432.66 | 870.75 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 359.33 | 895.13 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 650 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 750 | 0/0/0/0 | transparent | none |
| **container 1** (`section`) | 1440 | 432.66 | 308 | 0/0/0/0 | transparent | none |
| **container 1** (`section`) | 1024 | 359.33 | 388 | 0/0/0/0 | transparent | none |
| **container 1** (`section`) | 768 | 640 | 252 | 0/0/0/0 | transparent | none |
| **container 1** (`section`) | 390 | 358 | 290 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h1.font-display-lg`) | 1440 | 432.66 | 112 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h1.font-display-lg`) | 1024 | 359.33 | 168 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h1.font-display-lg`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h1.font-display-lg`) | 390 | 358 | 70 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 1440 | 432.66 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 1024 | 359.33 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 768 | 448 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-body-lg`) | 390 | 358 | 48 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.mt-6`) | 1440 | 432.66 | 100 | 12/16/12/16 | #2a2a2a | L 2px #c8c6c5 |
| └ coloana 3 (`div.mt-6`) | 1024 | 359.33 | 124 | 12/16/12/16 | #2a2a2a | L 2px #c8c6c5 |
| └ coloana 3 (`div.mt-6`) | 768 | 640 | 100 | 12/16/12/16 | #2a2a2a | L 2px #c8c6c5 |
| └ coloana 3 (`div.mt-6`) | 390 | 358 | 132 | 16/16/16/16 | #2a2a2a | L 2px #c8c6c5 |
| **container 2** (`div.flex`) | 1440 | 432.66 | 74 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 1024 | 359.33 | 74 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 768 | 640 | 54 | 0/0/0/0 | transparent | none |
| **container 2** (`div.flex`) | 390 | 358 | 124 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.inline-block`) | 1440 | 232.55 | 74 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 1024 | 188.86 | 74 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 768 | 277.72 | 54 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 390 | 358 | 54 | 16/32/16/32 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 2 (`a.inline-block`) | 1440 | 184.11 | 74 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 1024 | 154.47 | 74 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 768 | 214.73 | 54 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 390 | 358 | 54 | 16/32/16/32 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| **container 3** (`address.space-y-6`) | 1440 | 432.66 | 248 | 0/0/0/0 | transparent | none |
| **container 3** (`address.space-y-6`) | 1024 | 359.33 | 272 | 0/0/0/0 | transparent | none |
| **container 3** (`address.space-y-6`) | 768 | 640 | 248 | 0/0/0/0 | transparent | none |
| **container 3** (`address.space-y-6`) | 390 | 358 | 256 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.flex`) | 1440 | 432.66 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.flex`) | 1024 | 359.33 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.flex`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.flex`) | 390 | 358 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a.flex`) | 1440 | 432.66 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a.flex`) | 1024 | 359.33 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a.flex`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a.flex`) | 390 | 358 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 1440 | 432.66 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 1024 | 359.33 | 96 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 768 | 640 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.flex`) | 390 | 358 | 96 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rezervări și Contact Ioana Balan | h1 | 1440 | 184 | 312.38 | 432.66 | 112 | 48 | 56 | -0.96 | 500 | #c8c6c5 | start |
| Rezervări și Contact Ioana Balan | h1 | 1024 | 64 | 272.56 | 359.33 | 168 | 48 | 56 | -0.96 | 500 | #c8c6c5 | start |
| Rezervări și Contact Ioana Balan | h1 | 768 | 64 | 240 | 640 | 56 | 48 | 56 | -0.96 | 500 | #c8c6c5 | start |
| Rezervări și Contact Ioana Balan | h1 | 390 | 16 | 176 | 358 | 70 | 28 | 35 | normal | 500 | #c8c6c5 | start |
| Spuneți-ne data și locația — revenim în aceeași  | p | 1440 | 184 | 440.38 | 432.66 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Spuneți-ne data și locația — revenim în aceeași  | p | 1024 | 64 | 456.56 | 359.33 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Spuneți-ne data și locația — revenim în aceeași  | p | 768 | 64 | 312 | 448 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Spuneți-ne data și locația — revenim în aceeași  | p | 390 | 16 | 262 | 358 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Consultanță muzicală gratuită | p | 1440 | 202 | 532.38 | 398.66 | 24 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Consultanță muzicală gratuită | p | 1024 | 82 | 548.56 | 325.33 | 24 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Consultanță muzicală gratuită | p | 768 | 82 | 404 | 606 | 24 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Consultanță muzicală gratuită | p | 390 | 34 | 350 | 324 | 24 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Vă ajutăm să alegeți programul artistic perfect  | p | 1440 | 202 | 560.38 | 398.66 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Vă ajutăm să alegeți programul artistic perfect  | p | 1024 | 82 | 576.56 | 325.33 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Vă ajutăm să alegeți programul artistic perfect  | p | 768 | 82 | 432 | 606 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Vă ajutăm să alegeți programul artistic perfect  | p | 390 | 34 | 378 | 324 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Rezervă pe WhatsApp | a | 1440 | 184 | 668.38 | 232.55 | 74 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 1024 | 64 | 708.56 | 188.86 | 74 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 768 | 64 | 540 | 277.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 390 | 16 | 506 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| +40 722 911 485 | a | 1440 | 432.55 | 668.38 | 184.11 | 74 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 1024 | 268.86 | 708.56 | 154.47 | 74 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 768 | 357.72 | 540 | 214.73 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 390 | 16 | 576 | 358 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| svg (icon) | svg | 1440 | 200 | 806.38 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 80 | 846.56 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 80 | 658 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 32 | 686 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Email Oficial | span | 1440 | 248 | 790.38 | 220.94 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Email Oficial | span | 1024 | 128 | 830.56 | 220.94 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Email Oficial | span | 768 | 128 | 642 | 220.94 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Email Oficial | span | 390 | 80 | 670 | 220.94 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| ioanabalanoficial@gmail.com | span | 1440 | 248 | 814.38 | 220.94 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| ioanabalanoficial@gmail.com | span | 1024 | 128 | 854.56 | 220.94 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| ioanabalanoficial@gmail.com | span | 768 | 128 | 666 | 220.94 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| ioanabalanoficial@gmail.com | span | 390 | 80 | 694 | 220.94 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| svg (icon) | svg | 1440 | 200 | 894.38 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 80 | 934.56 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 80 | 746 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 32 | 766 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Telefon Rezervări | span | 1440 | 248 | 878.38 | 168.53 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Telefon Rezervări | span | 1024 | 128 | 918.56 | 168.53 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Telefon Rezervări | span | 768 | 128 | 730 | 168.53 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Telefon Rezervări | span | 390 | 80 | 750 | 168.53 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| +40 722 911 485 | span | 1440 | 248 | 902.38 | 168.53 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| +40 722 911 485 | span | 1024 | 128 | 942.56 | 168.53 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| +40 722 911 485 | span | 768 | 128 | 754 | 168.53 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| +40 722 911 485 | span | 390 | 80 | 774 | 168.53 | 32 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| svg (icon) | svg | 1440 | 200 | 982.38 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 80 | 1022.56 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 80 | 834 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 32 | 846 | 16 | 16 | 16 | 24 | normal | 400 | #c8c6c5 | start |
| Arie de Acoperire | p | 1440 | 248 | 966.38 | 368.66 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Arie de Acoperire | p | 1024 | 128 | 1006.56 | 295.33 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Arie de Acoperire | p | 768 | 128 | 818 | 576 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Arie de Acoperire | p | 390 | 80 | 830 | 294 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Performanțe live în București, Ploiești, Brașov  | p | 1440 | 248 | 990.38 | 368.66 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Performanțe live în București, Ploiești, Brașov  | p | 1024 | 128 | 1030.56 | 295.33 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Performanțe live în București, Ploiești, Brașov  | p | 768 | 128 | 842 | 576 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Performanțe live în București, Ploiești, Brașov  | p | 390 | 80 | 854 | 294 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.col-span-12` | [Rezervări și Contact Ioana Balan Spuneți] | [Rezervă pe WhatsApp +40 722 911 485] | 48 | 48 | 48 | 40 |
| `div.col-span-12` | [Rezervă pe WhatsApp +40 722 911 485] | [Email Oficial ioanabalanoficial@gmail.co] | 48 | 48 | 48 | 40 |
| `section` | Rezervări și Contact Ioana Balan | Spuneți-ne data și locația — revenim în aceeași  | 16 | 16 | 16 | 16 |
| `section` | Spuneți-ne data și locația — revenim în aceeași  | [Consultanță muzicală gratuită Vă ajutăm ] | 24 | 24 | 24 | 24 |
| `div.mt-6` | Consultanță muzicală gratuită | Vă ajutăm să alegeți programul artistic perfect  | 4 | 4 | 4 | 4 |
| `div.flex` | Rezervă pe WhatsApp | +40 722 911 485 | -74 ¹ | -74 ¹ | -54 ¹ | 16 |
| `address.space-y-6` | [Email Oficial ioanabalanoficial@gmail.co] | [Telefon Rezervări +40 722 911 485] | 32 | 32 | 32 | 24 |
| `address.space-y-6` | [Telefon Rezervări +40 722 911 485] | [Arie de Acoperire Performanțe live în Bu] | 32 | 32 | 32 | 24 |
| `a.flex` | span.shrink-0 | [Email Oficial ioanabalanoficial@gmail.co] | -48 ¹ | -48 ¹ | -48 ¹ | -48 ¹ |
| `span.block` | Email Oficial | ioanabalanoficial@gmail.com | 4 | 4 | 4 | 4 |
| `a.flex` | span.shrink-0 | [Telefon Rezervări +40 722 911 485] | -48 ¹ | -48 ¹ | -48 ¹ | -48 ¹ |
| `span.block` | Telefon Rezervări | +40 722 911 485 | 4 | 4 | 4 | 4 |
| `div.flex` | div.shrink-0 | [Arie de Acoperire Performanțe live în Bu] | -48 ¹ | -48 ¹ | -48 ¹ | -48 ¹ |
| `div` | Arie de Acoperire | Performanțe live în București, Ploiești, Brașov  | 4 | 4 | 4 | 4 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 232.55 + 184.11 | 16px | 16px | da (74) |
| `div.flex` | 1024 | flex | 188.86 + 154.47 | 16px | 16px | da (74) |
| `div.flex` | 768 | flex | 277.72 + 214.73 | 16px | 16px | da (54) |
| `div.flex` | 390 | flex | 358 + 358 | 16px | 16px | da (54) |
| `a.flex` | 1440 | flex | 48 + 220.94 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 1024 | flex | 48 + 220.94 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 768 | flex | 48 + 220.94 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 390 | flex | 48 + 220.94 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 1440 | flex | 48 + 168.53 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 1024 | flex | 48 + 168.53 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 768 | flex | 48 + 168.53 | 16px | 16px | **NU** — 48…56, delta 8 |
| `a.flex` | 390 | flex | 48 + 168.53 | 16px | 16px | **NU** — 48…56, delta 8 |
| `div.flex` | 1440 | flex | 48 + 368.66 | 16px | 16px | **NU** — 48…72, delta 24 |
| `div.flex` | 1024 | flex | 48 + 295.33 | 16px | 16px | **NU** — 48…96, delta 48 |
| `div.flex` | 768 | flex | 48 + 576 | 16px | 16px | **NU** — 48…72, delta 24 |
| `div.flex` | 390 | flex | 48 + 294 | 16px | 16px | **NU** — 48…96, delta 48 |

---

## S4 — Cere ofertă personalizată

`div` · clase: `col-span-12 lg:col-span-7`

Eyebrow: «(opțional)»

Titlu: «Cere ofertă personalizată»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 615.34 | 870.75 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 512.67 | 895.13 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 870.75 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 1091.50 | 0/0/0/0 | transparent | none |
| **container interior** | 1440 | 615.34 | 870.75 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| **container interior** | 1024 | 512.67 | 895.13 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| **container interior** | 768 | 640 | 870.75 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| **container interior** | 390 | 358 | 1091.50 | 24/24/24/24 | #1c1b1b | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| └ coloana 1 (`div.absolute`) | 1440 | 96 | 96 | 0/0/0/0 | transparent | T 1px #444748 @0.2, R 1px #444748 @0.2 |
| └ coloana 1 (`div.absolute`) | 1024 | 96 | 96 | 0/0/0/0 | transparent | T 1px #444748 @0.2, R 1px #444748 @0.2 |
| └ coloana 1 (`div.absolute`) | 768 | 96 | 96 | 0/0/0/0 | transparent | T 1px #444748 @0.2, R 1px #444748 @0.2 |
| └ coloana 1 (`div.absolute`) | 390 | 48 | 48 | 0/0/0/0 | transparent | T 1px #444748 @0.2, R 1px #444748 @0.2 |
| └ coloana 2 (`h2.font-headline-md`) | 1440 | 517.34 | 32 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2.font-headline-md`) | 1024 | 414.67 | 32 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2.font-headline-md`) | 768 | 542 | 32 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2.font-headline-md`) | 390 | 308 | 32 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`form#bookingForm`) | 1440 | 517.34 | 700.75 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`form#bookingForm`) | 1024 | 414.67 | 725.13 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`form#bookingForm`) | 768 | 542 | 700.75 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`form#bookingForm`) | 390 | 308 | 977.50 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cere ofertă personalizată | h2 | 1440 | 689.66 | 289 | 517.34 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| Cere ofertă personalizată | h2 | 1024 | 496.33 | 289 | 414.67 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| Cere ofertă personalizată | h2 | 768 | 113 | 963 | 542 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| Cere ofertă personalizată | h2 | 390 | 41 | 999 | 308 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| Nume complet | label | 1440 | 689.66 | 361 | 238.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Nume complet | label | 1024 | 496.33 | 361 | 187.33 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Nume complet | label | 768 | 113 | 1035 | 251 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Nume complet | label | 390 | 41 | 1063 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| input.w-full | input | 1440 | 689.66 | 393 | 238.67 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1024 | 496.33 | 393 | 187.33 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 768 | 113 | 1067 | 251 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 390 | 41 | 1095 | 308 | 50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Telefon | label | 1440 | 968.33 | 361 | 238.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Telefon | label | 1024 | 723.66 | 361 | 187.34 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Telefon | label | 768 | 404 | 1035 | 251 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Telefon | label | 390 | 41 | 1177 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| input.w-full | input | 1440 | 968.33 | 393 | 238.67 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1024 | 723.66 | 393 | 187.34 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 768 | 404 | 1067 | 251 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 390 | 41 | 1209 | 308 | 50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Data evenimentului | label | 1440 | 689.66 | 475 | 238.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data evenimentului | label | 1024 | 496.33 | 475 | 187.33 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data evenimentului | label | 768 | 113 | 1149 | 251 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data evenimentului | label | 390 | 41 | 1291 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| input.w-full | input | 1440 | 689.66 | 507 | 238.67 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1024 | 496.33 | 507 | 187.33 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 768 | 113 | 1181 | 251 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 390 | 41 | 1323 | 308 | 50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Tipul evenimentului | label | 1440 | 968.33 | 475 | 238.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Tipul evenimentului | label | 1024 | 723.66 | 475 | 187.34 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Tipul evenimentului | label | 768 | 404 | 1149 | 251 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Tipul evenimentului | label | 390 | 41 | 1405 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| [Concert / spectacol Nuntă / botez Gală c] | select | 1440 | 968.33 | 507 | 238.67 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| [Concert / spectacol Nuntă / botez Gală c] | select | 1024 | 723.66 | 507 | 187.34 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| [Concert / spectacol Nuntă / botez Gală c] | select | 768 | 404 | 1181 | 251 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| [Concert / spectacol Nuntă / botez Gală c] | select | 390 | 41 | 1437 | 308 | 50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Concert / spectacol | option | 1440 | **nerandat** | | | | | | | | | |
| Concert / spectacol | option | 1024 | **nerandat** | | | | | | | | | |
| Concert / spectacol | option | 768 | **nerandat** | | | | | | | | | |
| Concert / spectacol | option | 390 | **nerandat** | | | | | | | | | |
| Nuntă / botez | option | 1440 | **nerandat** | | | | | | | | | |
| Nuntă / botez | option | 1024 | **nerandat** | | | | | | | | | |
| Nuntă / botez | option | 768 | **nerandat** | | | | | | | | | |
| Nuntă / botez | option | 390 | **nerandat** | | | | | | | | | |
| Gală corporate | option | 1440 | **nerandat** | | | | | | | | | |
| Gală corporate | option | 1024 | **nerandat** | | | | | | | | | |
| Gală corporate | option | 768 | **nerandat** | | | | | | | | | |
| Gală corporate | option | 390 | **nerandat** | | | | | | | | | |
| Recepție privată | option | 1440 | **nerandat** | | | | | | | | | |
| Recepție privată | option | 1024 | **nerandat** | | | | | | | | | |
| Recepție privată | option | 768 | **nerandat** | | | | | | | | | |
| Recepție privată | option | 390 | **nerandat** | | | | | | | | | |
| Alt tip de eveniment | option | 1440 | **nerandat** | | | | | | | | | |
| Alt tip de eveniment | option | 1024 | **nerandat** | | | | | | | | | |
| Alt tip de eveniment | option | 768 | **nerandat** | | | | | | | | | |
| Alt tip de eveniment | option | 390 | **nerandat** | | | | | | | | | |
| Adresă email | label | 1440 | 689.66 | 589 | 517.34 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Adresă email | label | 1024 | 496.33 | 589 | 414.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Adresă email | label | 768 | 113 | 1263 | 542 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Adresă email | label | 390 | 41 | 1519 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| (opțional) | span | 1440 | 792.09 | 591 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 1024 | 598.77 | 591 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 768 | 215.44 | 1265 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 390 | 143.44 | 1521 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| input.w-full | input | 1440 | 689.66 | 621 | 517.34 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 1024 | 496.33 | 621 | 414.67 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 768 | 113 | 1295 | 542 | 42 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.w-full | input | 390 | 41 | 1551 | 308 | 50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Detalii suplimentare | label | 1440 | 689.66 | 703 | 517.34 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Detalii suplimentare | label | 1024 | 496.33 | 703 | 414.67 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Detalii suplimentare | label | 768 | 113 | 1377 | 542 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Detalii suplimentare | label | 390 | 41 | 1633 | 308 | 24 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| (opțional) | span | 1440 | 843.09 | 705 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 1024 | 649.77 | 705 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 768 | 266.44 | 1379 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| (opțional) | span | 390 | 194.44 | 1635 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 @0.7 | start |
| textarea.w-full | textarea | 1440 | 689.66 | 735 | 517.34 | 114 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| textarea.w-full | textarea | 1024 | 496.33 | 735 | 414.67 | 114 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| textarea.w-full | textarea | 768 | 113 | 1409 | 542 | 114 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| textarea.w-full | textarea | 390 | 41 | 1665 | 308 | 122 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| input.mt-0.5 | input | 1440 | 689.66 | 905 | 20 | 20 | 16 | 24 | normal | 400 | #a01028 | start |
| input.mt-0.5 | input | 1024 | 496.33 | 905 | 20 | 20 | 16 | 24 | normal | 400 | #a01028 | start |
| input.mt-0.5 | input | 768 | 113 | 1579 | 20 | 20 | 16 | 24 | normal | 400 | #a01028 | start |
| input.mt-0.5 | input | 390 | 41 | 1835 | 20 | 20 | 16 | 24 | normal | 400 | #a01028 | start |
| Sunt de acord ca datele introduse să fie folosit | label | 1440 | 721.66 | 903 | 485.34 | 48.75 | 15 | 24.38 | normal | 400 | #c4c7c7 | start |
| Sunt de acord ca datele introduse să fie folosit | label | 1024 | 528.33 | 903 | 382.67 | 73.13 | 15 | 24.38 | normal | 400 | #c4c7c7 | start |
| Sunt de acord ca datele introduse să fie folosit | label | 768 | 145 | 1577 | 510 | 48.75 | 15 | 24.38 | normal | 400 | #c4c7c7 | start |
| Sunt de acord ca datele introduse să fie folosit | label | 390 | 73 | 1833 | 276 | 97.50 | 15 | 24.38 | normal | 400 | #c4c7c7 | start |
| Politica de confidențialitate | a | 1440 | 1006.03 | 929.38 | 191.36 | 19 | 15 | 24.38 | normal | 400 | #c8c6c5 | start |
| Politica de confidențialitate | a | 1024 | 545.05 | 953.75 | 191.36 | 19 | 15 | 24.38 | normal | 400 | #c8c6c5 | start |
| Politica de confidențialitate | a | 768 | 429.38 | 1603.38 | 191.36 | 19 | 15 | 24.38 | normal | 400 | #c8c6c5 | start |
| Politica de confidențialitate | a | 390 | 73 | 1883.75 | 270.64 | 43.38 | 15 | 24.38 | normal | 400 | #c8c6c5 | start |
| Bifați acest acord pentru a putea trimite solici | p | 1440 | **nerandat** | | | | | | | | | |
| Bifați acest acord pentru a putea trimite solici | p | 1024 | **nerandat** | | | | | | | | | |
| Bifați acest acord pentru a putea trimite solici | p | 768 | **nerandat** | | | | | | | | | |
| Bifați acest acord pentru a putea trimite solici | p | 390 | **nerandat** | | | | | | | | | |
| Trimite Solicitarea | button | 1440 | 689.66 | 1007.75 | 287.34 | 54 | 14 | 20 | 2.80 | 600 | #ffffff | center |
| Trimite Solicitarea | button | 1024 | 496.33 | 1032.13 | 287.34 | 54 | 14 | 20 | 2.80 | 600 | #ffffff | center |
| Trimite Solicitarea | button | 768 | 113 | 1681.75 | 287.34 | 54 | 14 | 20 | 2.80 | 600 | #ffffff | center |
| Trimite Solicitarea | button | 390 | 41 | 1978.50 | 308 | 62 | 14 | 20 | 2.80 | 600 | #ffffff | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | div.absolute | Cere ofertă personalizată | -48 | -48 | -48 | -24 |
| `section` | Cere ofertă personalizată | [Nume complet Telefon Data evenimentului ] | 40 | 40 | 40 | 32 |
| `form#bookingForm` | [Nume complet Telefon] | [Data evenimentului Tipul evenimentului C] | 40 | 40 | 40 | 32 |
| `form#bookingForm` | [Data evenimentului Tipul evenimentului C] | [Adresă email (opțional)] | 40 | 40 | 40 | 32 |
| `form#bookingForm` | [Adresă email (opțional)] | [Detalii suplimentare (opțional)] | 40 | 40 | 40 | 32 |
| `form#bookingForm` | [Detalii suplimentare (opțional)] | [Sunt de acord ca datele introduse să fie] | 40 | 40 | 40 | 32 |
| `form#bookingForm` | [Sunt de acord ca datele introduse să fie] | [Trimite Solicitarea] | 40 | 40 | 40 | 32 |
| `div.grid` | [Nume complet] | [Telefon] | -74 ¹ | -74 ¹ | -74 ¹ | 32 |
| `div.relative` | Nume complet | input.w-full | 8 | 8 | 8 | 8 |
| `div.relative` | Telefon | input.w-full | 8 | 8 | 8 | 8 |
| `div.grid` | [Data evenimentului] | [Tipul evenimentului Concert / spectacol ] | -74 ¹ | -74 ¹ | -74 ¹ | 32 |
| `div.relative` | Data evenimentului | input.w-full | 8 | 8 | 8 | 8 |
| `div.relative` | Tipul evenimentului | [Concert / spectacol Nuntă / botez Gală c] | 8 | 8 | 8 | 8 |
| `div.relative` | Adresă email | input.w-full | 8 | 8 | 8 | 8 |
| `div.relative` | Detalii suplimentare | textarea.w-full | 8 | 8 | 8 | 8 |
| `div.flex` | input.mt-0.5 | Sunt de acord ca datele introduse să fie folosit | -22 ¹ | -22 ¹ | -22 ¹ | -22 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 238.672px 238.672px | 40px | 40px | da (74) |
| `div.grid` | 1024 | grid | 187.328px 187.344px | 40px | 40px | da (74) |
| `div.grid` | 768 | grid | 251px 251px | 40px | 40px | da (74) |
| `div.grid` | 390 | grid | 308px | 32px | 32px | da (82) |
| `div.grid` | 1440 | grid | 238.672px 238.672px | 40px | 40px | da (74) |
| `div.grid` | 1024 | grid | 187.328px 187.344px | 40px | 40px | da (74) |
| `div.grid` | 768 | grid | 251px 251px | 40px | 40px | da (74) |
| `div.grid` | 390 | grid | 308px | 32px | 32px | da (82) |
| `div.flex` | 1440 | flex | 20 + 485.34 | 12px | 12px | **NU** — 20…48.75, delta 28.75 |
| `div.flex` | 1024 | flex | 20 + 382.67 | 12px | 12px | **NU** — 20…73.13, delta 53.13 |
| `div.flex` | 768 | flex | 20 + 510 | 12px | 12px | **NU** — 20…48.75, delta 28.75 |
| `div.flex` | 390 | flex | 20 + 276 | 12px | 12px | **NU** — 20…97.50, delta 77.50 |

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `label` «Sunt de acord ca datele introduse să fie folosit» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[15px]`; weight rezolvat 400, font-size masurat 15px
- `p` «Bifați acest acord pentru a putea trimite solici» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[15px]`; weight rezolvat , font-size masurat px

### Borduri care vin din `assets/styles.css`, nu din clase

- `a.inline-block` «Rezervă pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.w-full` «Trimite Solicitarea» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Elemente care nu se randeaza la un viewport

- `div.absolute` «div.absolute» — `getClientRects().length == 0` la 768, 390 (randat la 1440, 1024); `display` raportat: block
- `img.w-full` «img ioana-balan-portrait-artist-muzica-populara-s.jpg» — `getClientRects().length == 0` la 768, 390 (randat la 1440, 1024); `display` raportat: block

### Suprapuneri intre elemente

- in `section`: «div.absolute» si «Cere ofertă personalizată» se suprapun pe verticala cu 48px la 1440 (suprapunere orizontala 48px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «Cere ofertă personalizată» se suprapun pe verticala cu 48px la 1024 (suprapunere orizontala 48px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «Cere ofertă personalizată» se suprapun pe verticala cu 48px la 768 (suprapunere orizontala 48px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «Cere ofertă personalizată» se suprapun pe verticala cu 24px la 390 (suprapunere orizontala 24px, position absolute/static) — stratificare intentionata (`position: absolute`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| div.absolute | 1440: 1440 · 1024: 1024 · 768: 768 · 390: 390 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.absolute | 1440: 720 · 1024: 512 · 768: n/r · 390: n/r | vert (sectiune): 1440: 0 sus / 0 jos · 1024: 0 sus / 0 jos · 768: n/r · 390: n/r<br>oriz (container): 1440: 0 L / 0 R · 1024: 0 L / 0 R · 768: n/r · 390: n/r | — | — | o singura coloana |
| Rezervări și Contact Ioana Balan | 1440: 432.66 · 1024: 359.33 · 768: 448 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Cere ofertă personalizată | 1440: 615.34 · 1024: 512.67 · 768: 640 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 | 1440: x 40px / y 40px · 1024: x 40px / y 40px · 768: x 40px / y 40px · 390: x 32px / y 32px | in `div.grid` (lat. 517.34 la 1440, grid):<br>1440: 238.67 + 238.67 · 1024: 187.33 + 187.34 · 768: 251 + 251 · 390: 308 + 308 |
