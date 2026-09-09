# Geometrie randata — `oferte.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/oferte.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 5979 | 128/0/0/0 | transparent | none |
| `<main>` | 1024 | 1024 | 6051 | 128/0/0/0 | transparent | none |
| `<main>` | 768 | 768 | 6452.88 | 80/0/0/0 | transparent | none |
| `<main>` | 390 | 390 | 8135 | 80/0/0/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 6410px, 1024 → 6482px, 768 → 6930px, 390 → 8722px.

Sectiuni masurate: **6**.

---

## S1 — Pachete și prețuri pentru nuntă și botez

`section` · clase: `relative min-h-[38vh] md:min-h-[42vh] flex items-end justify-center overflow-hidden mb-12 md:mb-20 px-6 md:px-margin-desktop py-10`

Eyebrow: «Oferte 2026-2027»

Titlu: «Pachete și prețuri pentru nuntă și botez»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 404 | 40/64/40/64 | transparent | none |
| **section** | 1024 | 1024 | 404 | 40/64/40/64 | transparent | none |
| **section** | 768 | 768 | 460 | 40/64/40/64 | transparent | none |
| **section** | 390 | 390 | 443 | 40/24/40/24 | transparent | none |
| **container 1** (`div.absolute`) | 1440 | 1440 | 404 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 1024 | 1024 | 404 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 768 | 768 | 460 | 0/0/0/0 | transparent | none |
| **container 1** (`div.absolute`) | 390 | 390 | 443 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 1440 | 1440 | 404 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 1024 | 1024 | 404 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 768 | 768 | 460 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 390 | 390 | 443 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.absolute`) | 1440 | 1440 | 404 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 1024 | 1024 | 404 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 768 | 768 | 460 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.absolute`) | 390 | 390 | 443 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.relative`) | 1440 | 736.75 | 324 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 1024 | 736.75 | 324 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 768 | 640 | 380 | 40/16/40/16 | transparent | none |
| **container 2** (`div.relative`) | 390 | 342 | 363 | 32/16/32/16 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1440 | 704.75 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1024 | 704.75 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 768 | 608 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 390 | 310 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 1440 | 704.75 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 1024 | 704.75 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 768 | 608 | 112 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h1.font-display-lg`) | 390 | 310 | 75 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 1440 | 672 | 84 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 1024 | 672 | 84 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 768 | 608 | 84 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 390 | 310 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`div.motif-separator`) | 1440 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 4 (`div.motif-separator`) | 1024 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 4 (`div.motif-separator`) | 768 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 4 (`div.motif-separator`) | 390 | 96 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-live-show.jpg | img | 1440 | 0 | 128 | 1440 | 404 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-live-show.jpg | img | 1024 | 0 | 128 | 1024 | 404 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-live-show.jpg | img | 768 | 0 | 80 | 768 | 460 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-live-show.jpg | img | 390 | 0 | 80 | 390 | 443 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Oferte 2026-2027 | span | 1440 | 367.63 | 208 | 704.75 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Oferte 2026-2027 | span | 1024 | 159.63 | 208 | 704.75 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Oferte 2026-2027 | span | 768 | 80 | 160 | 608 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Oferte 2026-2027 | span | 390 | 40 | 152 | 310 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Pachete și prețuri pentru nuntă și botez | h1 | 1440 | 367.63 | 240 | 704.75 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Pachete și prețuri pentru nuntă și botez | h1 | 1024 | 159.63 | 240 | 704.75 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Pachete și prețuri pentru nuntă și botez | h1 | 768 | 80 | 192 | 608 | 112 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Pachete și prețuri pentru nuntă și botez | h1 | 390 | 40 | 184 | 310 | 75 | 30 | 37.50 | normal | 400 | #e5e2e1 | center |
| Ioana Balan este solistă de muzică populară și d | p | 1440 | 384 | 316 | 672 | 84 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Ioana Balan este solistă de muzică populară și d | p | 1024 | 176 | 316 | 672 | 84 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Ioana Balan este solistă de muzică populară și d | p | 768 | 80 | 324 | 608 | 84 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Ioana Balan este solistă de muzică populară și d | p | 390 | 40 | 279 | 310 | 120 | 16 | 24 | normal | 400 | #c4c7c7 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | div.absolute | [Oferte 2026-2027 Pachete și prețuri pent] | -364 | -364 | -420 | -403 |
| `div.absolute` | img ioana-balan-live-show.jpg | div.absolute | -404 | -404 | -460 | -443 |
| `div.relative` | Oferte 2026-2027 | Pachete și prețuri pentru nuntă și botez | 12 | 12 | 12 | 12 |
| `div.relative` | Pachete și prețuri pentru nuntă și botez | Ioana Balan este solistă de muzică populară și d | 20 | 20 | 20 | 20 |
| `div.relative` | Ioana Balan este solistă de muzică populară și d | div.motif-separator | 28 | 28 | 28 | 28 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `section` | 1440 | flex | 1440 + 736.75 | 0px | 0px | **NU** — 324…404, delta 80 |
| `section` | 1024 | flex | 1024 + 736.75 | 0px | 0px | **NU** — 324…404, delta 80 |
| `section` | 768 | flex | 768 + 640 | 0px | 0px | **NU** — 380…460, delta 80 |
| `section` | 390 | flex | 390 + 342 | 0px | 0px | **NU** — 363…443, delta 80 |

---

## S2 — Condiții comerciale

`section` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-12 md:mb-16`

Eyebrow: «De confirmat»

Titlu: «Condiții comerciale»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 254 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 254 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 302 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 406 | 0/24/0/24 | transparent | none |
| **container interior** | 1440 | 1024 | 254 | 32/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| **container interior** | 1024 | 896 | 254 | 32/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| **container interior** | 768 | 640 | 302 | 32/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| **container interior** | 390 | 342 | 406 | 24/24/24/24 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 1 (`h2#conditii-titlu`) | 1440 | 958 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#conditii-titlu`) | 1024 | 830 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#conditii-titlu`) | 768 | 574 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#conditii-titlu`) | 390 | 292 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`ul.motif-list`) | 1440 | 958 | 148 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`ul.motif-list`) | 1024 | 830 | 148 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`ul.motif-list`) | 768 | 574 | 196 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`ul.motif-list`) | 390 | 292 | 316 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Condiții comerciale | h2 | 1440 | 241 | 645 | 958 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Condiții comerciale | h2 | 1024 | 97 | 645 | 830 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Condiții comerciale | h2 | 768 | 97 | 653 | 574 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Condiții comerciale | h2 | 390 | 49 | 596 | 292 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Prețurile sunt exprimate în euro și se achită în | li | 1440 | 241 | 685 | 958 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Prețurile sunt exprimate în euro și se achită în | li | 1024 | 97 | 685 | 830 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Prețurile sunt exprimate în euro și se achită în | li | 768 | 97 | 693 | 574 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Prețurile sunt exprimate în euro și se achită în | li | 390 | 49 | 636 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Configurația pachetelor și prețurile de mai jos  | li | 1440 | 241 | 725 | 958 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Configurația pachetelor și prețurile de mai jos  | li | 1024 | 97 | 725 | 830 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Configurația pachetelor și prețurile de mai jos  | li | 768 | 97 | 757 | 574 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Configurația pachetelor și prețurile de mai jos  | li | 390 | 49 | 724 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele din afara localității se ada | li | 1440 | 241 | 765 | 958 | 68 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele din afara localității se ada | li | 1024 | 97 | 765 | 830 | 68 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele din afara localității se ada | li | 768 | 97 | 821 | 574 | 68 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele din afara localității se ada | li | 390 | 49 | 812 | 292 | 140 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 849.41 | 783 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 705.41 | 783 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 160.63 | 863 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 89 | 902 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| __ RON/km | span | 1440 | 961.31 | 773 | 92.06 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| __ RON/km | span | 1024 | 817.31 | 773 | 92.06 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| __ RON/km | span | 768 | 272.53 | 853 | 92.06 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| __ RON/km | span | 390 | 200.91 | 892 | 92.06 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-5xl` | Condiții comerciale | [Prețurile sunt exprimate în euro și se a] | 20 | 20 | 20 | 20 |
| `ul.motif-list` | Prețurile sunt exprimate în euro și se achită în | Configurația pachetelor și prețurile de mai jos  | 16 | 16 | 16 | 16 |
| `ul.motif-list` | Configurația pachetelor și prețurile de mai jos  | Pentru evenimentele din afara localității se ada | 16 | 16 | 16 | 16 |
| `span.price-tbc` | De confirmat | __ RON/km | -23.19 ¹ | -23.19 ¹ | -23.19 ¹ | -23.19 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 92.06 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 92.06 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 92.06 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 92.06 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |

---

## S3 — Patru pachete, pentru nuntă și pentru botez (#pachete)

`section#pachete` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-16 md:mb-24`

Eyebrow: «Buget redus»

Titlu: «Patru pachete, pentru nuntă și pentru botez»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 3184 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 3256 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 3573.88 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 5320 | 0/24/0/24 | transparent | none |
| **container 1** (`div.mb-8`) | 1440 | 1072 | 84 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-8`) | 1024 | 896 | 84 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-8`) | 768 | 640 | 84 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-8`) | 390 | 342 | 108 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#pachete-titlu`) | 1440 | 1072 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#pachete-titlu`) | 1024 | 896 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#pachete-titlu`) | 768 | 640 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2#pachete-titlu`) | 390 | 342 | 64 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.motif-rule`) | 1440 | 220 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.motif-rule`) | 1024 | 220 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.motif-rule`) | 768 | 220 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.motif-rule`) | 390 | 220 | 24 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 1440 | 1024 | 2181.50 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 1024 | 896 | 2349.50 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 768 | 640 | 2859.38 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 390 | 342 | 4815 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`article.glass-card`) | 1440 | 500 | 1328.50 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 1 (`article.glass-card`) | 1024 | 436 | 1424.50 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 1 (`article.glass-card`) | 768 | 308 | 1773.19 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 1 (`article.glass-card`) | 390 | 342 | 1149 | 48/24/24/24 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 2 (`article.glass-card`) | 1440 | 500 | 1328.50 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 2 (`article.glass-card`) | 1024 | 436 | 1424.50 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 2 (`article.glass-card`) | 768 | 308 | 1773.19 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 2 (`article.glass-card`) | 390 | 342 | 1632 | 48/24/24/24 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 3 (`article.glass-card`) | 1440 | 500 | 829 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 3 (`article.glass-card`) | 1024 | 436 | 901 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 3 (`article.glass-card`) | 768 | 308 | 1062.19 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 3 (`article.glass-card`) | 390 | 342 | 993 | 48/24/24/24 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 4 (`article.glass-card`) | 1440 | 500 | 829 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 4 (`article.glass-card`) | 1024 | 436 | 901 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 4 (`article.glass-card`) | 768 | 308 | 1062.19 | 56/32/32/32 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| └ coloana 4 (`article.glass-card`) | 390 | 342 | 969 | 48/24/24/24 | #1c1b1b | T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2 |
| **container 3** (`figure.max-w-5xl`) | 1440 | 1024 | 814.50 | 0/0/0/0 | transparent | none |
| **container 3** (`figure.max-w-5xl`) | 1024 | 896 | 718.50 | 0/0/0/0 | transparent | none |
| **container 3** (`figure.max-w-5xl`) | 768 | 640 | 526.50 | 0/0/0/0 | transparent | none |
| **container 3** (`figure.max-w-5xl`) | 390 | 342 | 325 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.border`) | 1440 | 1024 | 774.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.border`) | 1024 | 896 | 678.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.border`) | 768 | 640 | 486.50 | 12/12/12/12 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.border`) | 390 | 342 | 261 | 8/8/8/8 | transparent | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`figcaption.font-body-md`) | 1440 | 1024 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`figcaption.font-body-md`) | 1024 | 896 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`figcaption.font-body-md`) | 768 | 640 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`figcaption.font-body-md`) | 390 | 342 | 48 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patru pachete, pentru nuntă și pentru botez | h2 | 1440 | 184 | 930 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Patru pachete, pentru nuntă și pentru botez | h2 | 1024 | 64 | 930 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Patru pachete, pentru nuntă și pentru botez | h2 | 768 | 64 | 986 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Patru pachete, pentru nuntă și pentru botez | h2 | 390 | 24 | 1025 | 342 | 64 | 24 | 32 | normal | 400 | #e5e2e1 | center |
| Buget redus | span | 1440 | 591.63 | 1063 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 1024 | 383.63 | 1063 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 768 | 255.63 | 1119 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 390 | 249.63 | 1166 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Nuntă | span | 1440 | 241 | 1119 | 434 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 1024 | 97 | 1119 | 370 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 768 | 97 | 1175 | 242 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 390 | 49 | 1214 | 292 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Pachet Standard | h3 | 1440 | 241 | 1147 | 434 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 1024 | 97 | 1147 | 370 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 768 | 97 | 1203 | 242 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 390 | 49 | 1242 | 292 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Sâmbătă | span | 1440 | 241 | 1199 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 1024 | 97 | 1199 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 768 | 97 | 1255 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 390 | 49 | 1290 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 255 | 1255 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 111 | 1255 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 111 | 1289 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 1342 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 5.500 € | span | 1440 | 366.91 | 1233 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 1024 | 222.91 | 1233 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 768 | 111 | 1306.19 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 390 | 174.91 | 1324 | 91.72 | 36 | 30 | 36 | normal | 400 | #e5e2e1 | start |
| Formație live, doi interpreți și DJ pentru toată | p | 1440 | 241 | 1301 | 434 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație live, doi interpreți și DJ pentru toată | p | 1024 | 97 | 1301 | 370 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație live, doi interpreți și DJ pentru toată | p | 768 | 97 | 1374.19 | 242 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație live, doi interpreți și DJ pentru toată | p | 390 | 49 | 1388 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de 4 instrumente: clapă, vioară, acorde | li | 1440 | 241 | 1373 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, vioară, acorde | li | 1024 | 97 | 1373 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, vioară, acorde | li | 768 | 97 | 1470.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, vioară, acorde | li | 390 | 49 | 1484 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 1440 | 241 | 1433 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 1024 | 97 | 1433 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 768 | 97 | 1554.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 390 | 49 | 1544 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară românească și inte | li | 1440 | 241 | 1469 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară românească și inte | li | 1024 | 97 | 1493 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară românească și inte | li | 768 | 97 | 1614.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară românească și inte | li | 390 | 49 | 1604 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC pe toată durata evenimentului | li | 1440 | 241 | 1529 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC pe toată durata evenimentului | li | 1024 | 97 | 1553 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC pe toată durata evenimentului | li | 768 | 97 | 1698.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC pe toată durata evenimentului | li | 390 | 49 | 1664 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală  | li | 1440 | 241 | 1565 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală  | li | 1024 | 97 | 1589 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală  | li | 768 | 97 | 1758.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală  | li | 390 | 49 | 1724 | 292 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu pentru valsul mirilor | li | 1440 | 241 | 1625 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu pentru valsul mirilor | li | 1024 | 97 | 1649 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu pentru valsul mirilor | li | 768 | 97 | 1842.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu pentru valsul mirilor | li | 390 | 49 | 1808 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Gheață carbonică la primirea invitaților și la m | li | 1440 | 241 | 1661 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Gheață carbonică la primirea invitaților și la m | li | 1024 | 97 | 1685 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Gheață carbonică la primirea invitaților și la m | li | 768 | 97 | 1902.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Gheață carbonică la primirea invitaților și la m | li | 390 | 49 | 1868 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1440 | 241 | 1721 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1024 | 97 | 1745 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 768 | 97 | 1986.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 390 | 49 | 1928 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1440 | 241 | 1757 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1024 | 97 | 1805 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 768 | 97 | 2046.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 390 | 49 | 1988 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 1440 | 241 | 1793 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 1024 | 97 | 1841 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 768 | 97 | 2106.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 390 | 49 | 2048 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Duminică | span | 1440 | 241 | 2205.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 1024 | 97 | 2301.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 768 | 97 | 2706.19 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 390 | 49 | 2141 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 255 | 2253.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 111 | 2349.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 111 | 2754.19 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 2186 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 4.800 € | span | 1440 | 366.91 | 2239.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 4.800 € | span | 1024 | 222.91 | 2335.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 4.800 € | span | 768 | 222.91 | 2740.19 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 4.800 € | span | 390 | 174.91 | 2175 | 61.14 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Scrieți-ne pe WhatsApp | a | 1440 | 241 | 2303.50 | 434 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 1024 | 97 | 2399.50 | 370 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 768 | 97 | 2804.19 | 242 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 390 | 49 | 2235 | 292 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cel mai căutat | span | 1440 | 1100.33 | 1063 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 1024 | 828.33 | 1063 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 768 | 572.33 | 1119 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 390 | 234.33 | 2339 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Nuntă | span | 1440 | 765 | 1119 | 434 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 1024 | 557 | 1119 | 370 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 768 | 429 | 1175 | 242 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Nuntă | span | 390 | 49 | 2387 | 292 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Pachet Premium | h3 | 1440 | 765 | 1147 | 434 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 1024 | 557 | 1147 | 370 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 768 | 429 | 1203 | 242 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 390 | 49 | 2415 | 292 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Sâmbătă | span | 1440 | 765 | 1199 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 1024 | 557 | 1199 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 768 | 429 | 1255 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 390 | 49 | 2463 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 779 | 1255 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 571 | 1255 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 443 | 1289 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 2515 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 6.500 € | span | 1440 | 890.91 | 1233 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 6.500 € | span | 1024 | 682.91 | 1233 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 6.500 € | span | 768 | 443 | 1306.19 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 6.500 € | span | 390 | 174.91 | 2497 | 91.72 | 36 | 30 | 36 | normal | 400 | #e5e2e1 | start |
| Formație extinsă, trei interpreți și producție c | p | 1440 | 765 | 1301 | 434 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație extinsă, trei interpreți și producție c | p | 1024 | 557 | 1301 | 370 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație extinsă, trei interpreți și producție c | p | 768 | 429 | 1374.19 | 242 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație extinsă, trei interpreți și producție c | p | 390 | 49 | 2561 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de 6 instrumente: clapă, vioară, saxofo | li | 1440 | 765 | 1373 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 6 instrumente: clapă, vioară, saxofo | li | 1024 | 557 | 1373 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 6 instrumente: clapă, vioară, saxofo | li | 768 | 429 | 1470.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 6 instrumente: clapă, vioară, saxofo | li | 390 | 49 | 2657 | 292 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Țambal | li | 1440 | 765 | 1433 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Țambal | li | 1024 | 557 | 1433 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Țambal | li | 768 | 429 | 1554.19 | 242 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Țambal | li | 390 | 49 | 2741 | 292 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| (opțional) | span | 1440 | 851.64 | 1435 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 1024 | 643.64 | 1435 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 768 | 515.64 | 1556.19 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 390 | 135.64 | 2743 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Un interpret de muzică populară și de petrecere | li | 1440 | 765 | 1469 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 1024 | 557 | 1469 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 768 | 429 | 1590.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și de petrecere | li | 390 | 49 | 2777 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară | li | 1440 | 765 | 1505 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară | li | 1024 | 557 | 1529 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară | li | 768 | 429 | 1650.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică ușoară | li | 390 | 49 | 2837 | 292 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică balcanică | li | 1440 | 765 | 1541 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică balcanică | li | 1024 | 557 | 1565 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică balcanică | li | 768 | 429 | 1710.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică balcanică | li | 390 | 49 | 2873 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| (opțional) | span | 1440 | 1044.97 | 1543 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 1024 | 836.97 | 1567 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 768 | 532.05 | 1736.19 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 390 | 75 | 2899 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| DJ și MC profesionist pe toată durata evenimentu | li | 1440 | 765 | 1577 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC profesionist pe toată durata evenimentu | li | 1024 | 557 | 1601 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC profesionist pe toată durata evenimentu | li | 768 | 429 | 1770.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ și MC profesionist pe toată durata evenimentu | li | 390 | 49 | 2933 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Ecran LED cu imagini personalizate | li | 1440 | 765 | 1613 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Ecran LED cu imagini personalizate | li | 1024 | 557 | 1661 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Ecran LED cu imagini personalizate | li | 768 | 429 | 1830.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Ecran LED cu imagini personalizate | li | 390 | 49 | 2993 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| (opțional) | span | 1440 | 1061.03 | 1615 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 1024 | 853.03 | 1663 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 768 | 561.11 | 1856.19 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 390 | 75 | 3019 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Sonorizare profesională | li | 1440 | 765 | 1649 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională | li | 1024 | 557 | 1697 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională | li | 768 | 429 | 1890.19 | 242 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională | li | 390 | 49 | 3053 | 292 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu și gheață carbonică | li | 1440 | 765 | 1685 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu și gheață carbonică | li | 1024 | 557 | 1733 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu și gheață carbonică | li | 768 | 429 | 1926.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Mașină de fum greu și gheață carbonică | li | 390 | 49 | 3089 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Zece corpuri de lumină ambientală | li | 1440 | 765 | 1721 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Zece corpuri de lumină ambientală | li | 1024 | 557 | 1769 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Zece corpuri de lumină ambientală | li | 768 | 429 | 1986.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Zece corpuri de lumină ambientală | li | 390 | 49 | 3149 | 292 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Vulcani CO2 pe toată durata petrecerii | li | 1440 | 765 | 1757 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Vulcani CO2 pe toată durata petrecerii | li | 1024 | 557 | 1805 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Vulcani CO2 pe toată durata petrecerii | li | 768 | 429 | 2046.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Vulcani CO2 pe toată durata petrecerii | li | 390 | 49 | 3185 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Schelă profesională de lumini, cu 4–6 moving-hea | li | 1440 | 765 | 1793 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Schelă profesională de lumini, cu 4–6 moving-hea | li | 1024 | 557 | 1841 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Schelă profesională de lumini, cu 4–6 moving-hea | li | 768 | 429 | 2106.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Schelă profesională de lumini, cu 4–6 moving-hea | li | 390 | 49 | 3245 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto trei ore, cu accesorii și fotografii | li | 1440 | 765 | 1829 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto trei ore, cu accesorii și fotografii | li | 1024 | 557 | 1901 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto trei ore, cu accesorii și fotografii | li | 768 | 429 | 2166.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto trei ore, cu accesorii și fotografii | li | 390 | 49 | 3305 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto 360 | li | 1440 | 765 | 1889 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto 360 | li | 1024 | 557 | 1961 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto 360 | li | 768 | 429 | 2250.19 | 242 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Cabină foto 360 | li | 390 | 49 | 3365 | 292 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| (opțional) | span | 1440 | 916.91 | 1891 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 1024 | 708.91 | 1963 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 768 | 580.91 | 2252.19 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| (opțional) | span | 390 | 200.91 | 3367 | 71.91 | 20 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Panou floral sau glamour, la alegerea dumneavoas | li | 1440 | 765 | 1925 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Panou floral sau glamour, la alegerea dumneavoas | li | 1024 | 557 | 1997 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Panou floral sau glamour, la alegerea dumneavoas | li | 768 | 429 | 2286.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Panou floral sau glamour, la alegerea dumneavoas | li | 390 | 49 | 3401 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Inginer de sunet și lumini prezent toată seara | li | 1440 | 765 | 1961 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Inginer de sunet și lumini prezent toată seara | li | 1024 | 557 | 2057 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Inginer de sunet și lumini prezent toată seara | li | 768 | 429 | 2346.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Inginer de sunet și lumini prezent toată seara | li | 390 | 49 | 3461 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Staff tehnic pentru montaj și demontaj | li | 1440 | 765 | 1997 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Staff tehnic pentru montaj și demontaj | li | 1024 | 557 | 2093 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Staff tehnic pentru montaj și demontaj | li | 768 | 429 | 2406.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Staff tehnic pentru montaj și demontaj | li | 390 | 49 | 3521 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prestație muzicală fără limită de programe | li | 1440 | 765 | 2033 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prestație muzicală fără limită de programe | li | 1024 | 557 | 2129 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prestație muzicală fără limită de programe | li | 768 | 429 | 2466.19 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prestație muzicală fără limită de programe | li | 390 | 49 | 3581 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 1440 | 765 | 2069 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 1024 | 557 | 2165 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 768 | 429 | 2526.19 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea serii, fără cost  | li | 390 | 49 | 3641 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Elementele marcate „opțional” se tarifează separ | p | 1440 | 765 | 2141 | 434 | 19.50 | 13 | 19.50 | normal | 400 | #c4c7c7 | start |
| Elementele marcate „opțional” se tarifează separ | p | 1024 | 557 | 2237 | 370 | 19.50 | 13 | 19.50 | normal | 400 | #c4c7c7 | start |
| Elementele marcate „opțional” se tarifează separ | p | 768 | 429 | 2622.19 | 242 | 39 | 13 | 19.50 | normal | 400 | #c4c7c7 | start |
| Elementele marcate „opțional” se tarifează separ | p | 390 | 49 | 3713 | 292 | 39 | 13 | 19.50 | normal | 400 | #c4c7c7 | start |
| Duminică | span | 1440 | 765 | 2205.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 1024 | 557 | 2301.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 768 | 429 | 2706.19 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 390 | 49 | 3797 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 779 | 2253.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 571 | 2349.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 443 | 2754.19 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 3842 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 5.500 € | span | 1440 | 890.91 | 2239.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 1024 | 682.91 | 2335.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 768 | 554.91 | 2740.19 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 5.500 € | span | 390 | 174.91 | 3831 | 61.14 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Scrieți-ne pe WhatsApp | a | 1440 | 765 | 2303.50 | 434 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-ne pe WhatsApp | a | 1024 | 557 | 2399.50 | 370 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-ne pe WhatsApp | a | 768 | 429 | 2804.19 | 242 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Scrieți-ne pe WhatsApp | a | 390 | 49 | 3891 | 292 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Buget redus | span | 1440 | 591.63 | 2415.50 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 1024 | 383.63 | 2511.50 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 768 | 255.63 | 2916.19 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Buget redus | span | 390 | 249.63 | 3995 | 115.38 | 30.50 | 11 | 16.50 | 1.10 | 400 | #c6c6c6 | start |
| Botez | span | 1440 | 241 | 2471.50 | 434 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 1024 | 97 | 2567.50 | 370 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 768 | 97 | 2972.19 | 242 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 390 | 49 | 4043 | 292 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Pachet Standard | h3 | 1440 | 241 | 2499.50 | 434 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 1024 | 97 | 2595.50 | 370 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 768 | 97 | 3000.19 | 242 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Standard | h3 | 390 | 49 | 4071 | 292 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Sâmbătă | span | 1440 | 241 | 2551.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 1024 | 97 | 2647.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 768 | 97 | 3052.19 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 390 | 49 | 4119 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 255 | 2607.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 111 | 2703.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 111 | 3086.19 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 4171 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 3.200 € | span | 1440 | 366.91 | 2585.50 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.200 € | span | 1024 | 222.91 | 2681.50 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.200 € | span | 768 | 111 | 3103.38 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.200 € | span | 390 | 174.91 | 4153 | 91.72 | 36 | 30 | 36 | normal | 400 | #e5e2e1 | start |
| Formație de trei instrumente și DJ, cu două prog | p | 1440 | 241 | 2653.50 | 434 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de trei instrumente și DJ, cu două prog | p | 1024 | 97 | 2749.50 | 370 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de trei instrumente și DJ, cu două prog | p | 768 | 97 | 3171.38 | 242 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de trei instrumente și DJ, cu două prog | p | 390 | 49 | 4217 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de 3 instrumente: clapă, saxofon și vio | li | 1440 | 241 | 2725.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 3 instrumente: clapă, saxofon și vio | li | 1024 | 97 | 2821.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 3 instrumente: clapă, saxofon și vio | li | 768 | 97 | 3267.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 3 instrumente: clapă, saxofon și vio | li | 390 | 49 | 4313 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară, în do | li | 1440 | 241 | 2761.50 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară, în do | li | 1024 | 97 | 2881.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară, în do | li | 768 | 97 | 3327.38 | 242 | 96 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară, în do | li | 390 | 49 | 4373 | 292 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 1440 | 241 | 2821.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 1024 | 97 | 2941.50 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 768 | 97 | 3435.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 390 | 49 | 4457 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 1440 | 241 | 2857.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 1024 | 97 | 2977.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 768 | 97 | 3495.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 390 | 49 | 4517 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1440 | 241 | 2893.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1024 | 97 | 3037.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 768 | 97 | 3555.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 390 | 49 | 4577 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1440 | 241 | 2929.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1024 | 97 | 3097.50 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 768 | 97 | 3615.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 390 | 49 | 4637 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 1440 | 241 | 2965.50 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 1024 | 97 | 3133.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 768 | 97 | 3675.38 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 390 | 49 | 4697 | 292 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Duminică | span | 1440 | 241 | 3058.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 1024 | 97 | 3226.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 768 | 97 | 3792.38 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 390 | 49 | 4814 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 255 | 3106.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 111 | 3274.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 111 | 3840.38 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 4859 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 2.800 € | span | 1440 | 366.91 | 3092.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 2.800 € | span | 1024 | 222.91 | 3260.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 2.800 € | span | 768 | 222.91 | 3826.38 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 2.800 € | span | 390 | 174.91 | 4848 | 61.14 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Scrieți-ne pe WhatsApp | a | 1440 | 241 | 3156.50 | 434 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 1024 | 97 | 3324.50 | 370 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 768 | 97 | 3890.38 | 242 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 390 | 49 | 4908 | 292 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cel mai căutat | span | 1440 | 1100.33 | 2415.50 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 1024 | 828.33 | 2511.50 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 768 | 572.33 | 2916.19 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Cel mai căutat | span | 390 | 234.33 | 5012 | 130.67 | 28.50 | 11 | 16.50 | 1.10 | 400 | #ffffff | start |
| Botez | span | 1440 | 765 | 2471.50 | 434 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 1024 | 557 | 2567.50 | 370 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 768 | 429 | 2972.19 | 242 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Botez | span | 390 | 49 | 5060 | 292 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Pachet Premium | h3 | 1440 | 765 | 2499.50 | 434 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 1024 | 557 | 2595.50 | 370 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 768 | 429 | 3000.19 | 242 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pachet Premium | h3 | 390 | 49 | 5088 | 292 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Sâmbătă | span | 1440 | 765 | 2551.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 1024 | 557 | 2647.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 768 | 429 | 3052.19 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Sâmbătă | span | 390 | 49 | 5136 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 779 | 2607.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 571 | 2703.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 443 | 3086.19 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 5188 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 3.800 € | span | 1440 | 890.91 | 2585.50 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.800 € | span | 1024 | 682.91 | 2681.50 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.800 € | span | 768 | 443 | 3103.38 | 110.06 | 40 | 36 | 40 | normal | 400 | #e5e2e1 | start |
| 3.800 € | span | 390 | 174.91 | 5170 | 91.72 | 36 | 30 | 36 | normal | 400 | #e5e2e1 | start |
| Formație de patru instrumente pentru un sunet ma | p | 1440 | 765 | 2653.50 | 434 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de patru instrumente pentru un sunet ma | p | 1024 | 557 | 2749.50 | 370 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de patru instrumente pentru un sunet ma | p | 768 | 429 | 3171.38 | 242 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de patru instrumente pentru un sunet ma | p | 390 | 49 | 5234 | 292 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| Formație de 4 instrumente: clapă, acordeon, saxo | li | 1440 | 765 | 2725.50 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, acordeon, saxo | li | 1024 | 557 | 2821.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, acordeon, saxo | li | 768 | 429 | 3267.38 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Formație de 4 instrumente: clapă, acordeon, saxo | li | 390 | 49 | 5330 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară | li | 1440 | 765 | 2785.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară | li | 1024 | 557 | 2881.50 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară | li | 768 | 429 | 3351.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Un interpret de muzică populară și ușoară | li | 390 | 49 | 5390 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 1440 | 765 | 2821.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 1024 | 557 | 2917.50 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 768 | 429 | 3411.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ profesionist pe toată durata evenimentului | li | 390 | 49 | 5450 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 1440 | 765 | 2857.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 1024 | 557 | 2953.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 768 | 429 | 3471.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Sonorizare profesională, dimensionată după sală | li | 390 | 49 | 5510 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1440 | 765 | 2893.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 1024 | 557 | 3013.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 768 | 429 | 3531.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Muzică de tip cafe-concert la primirea invitațil | li | 390 | 49 | 5570 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1440 | 765 | 2929.50 | 434 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 1024 | 557 | 3073.50 | 370 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 768 | 429 | 3591.38 | 242 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Moment de virtuozitate instrumentală | li | 390 | 49 | 5630 | 292 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 1440 | 765 | 2965.50 | 434 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 1024 | 557 | 3109.50 | 370 | 48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 768 | 429 | 3651.38 | 242 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Consultanță pentru organizarea evenimentului, fă | li | 390 | 49 | 5690 | 292 | 72 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Duminică | span | 1440 | 765 | 3058.50 | 434 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 1024 | 557 | 3226.50 | 370 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 768 | 429 | 3792.38 | 242 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| Duminică | span | 390 | 49 | 5807 | 292 | 18 | 12 | 18 | 1.20 | 400 | #c4c7c7 | start |
| De confirmat | span | 1440 | 779 | 3106.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 1024 | 571 | 3274.50 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 768 | 443 | 3840.38 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De confirmat | span | 390 | 63 | 5852 | 101.91 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| 3.300 € | span | 1440 | 890.91 | 3092.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 3.300 € | span | 1024 | 682.91 | 3260.50 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 3.300 € | span | 768 | 554.91 | 3826.38 | 73.38 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | start |
| 3.300 € | span | 390 | 174.91 | 5841 | 61.14 | 28 | 20 | 28 | normal | 400 | #e5e2e1 | start |
| Scrieți-ne pe WhatsApp | a | 1440 | 765 | 3156.50 | 434 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 1024 | 557 | 3324.50 | 370 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 768 | 429 | 3890.38 | 242 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Scrieți-ne pe WhatsApp | a | 390 | 49 | 5901 | 292 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| img formatie-instrumentala-tambal-1304.jpg | img | 1440 | 221 | 3312.50 | 998 | 748.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-instrumentala-tambal-1304.jpg | img | 1024 | 77 | 3480.50 | 870 | 652.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-instrumentala-tambal-1304.jpg | img | 768 | 77 | 4046.38 | 614 | 460.50 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-instrumentala-tambal-1304.jpg | img | 390 | 33 | 6029 | 324 | 243 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Configurația extinsă, cu țambal — inclus opționa | figcaption | 1440 | 208 | 4090 | 1024 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Configurația extinsă, cu țambal — inclus opționa | figcaption | 1024 | 64 | 4162 | 896 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Configurația extinsă, cu țambal — inclus opționa | figcaption | 768 | 64 | 4535.88 | 640 | 24 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Configurația extinsă, cu țambal — inclus opționa | figcaption | 390 | 24 | 6297 | 342 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#pachete` | [Patru pachete, pentru nuntă și pentru bo] | [Buget redus Nuntă Pachet Standard Sâmbăt] | 48 | 48 | 48 | 32 |
| `section#pachete` | [Buget redus Nuntă Pachet Standard Sâmbăt] | [Configurația extinsă, cu țambal — inclus] | 56 | 56 | 56 | 40 |
| `div.mb-8` | Patru pachete, pentru nuntă și pentru botez | div.motif-rule | 20 | 20 | 20 | 20 |
| `div.grid` | [Buget redus Nuntă Pachet Standard Sâmbăt] | [Cel mai căutat Nuntă Pachet Premium Sâmb] | -1328.50 ¹ | -1424.50 ¹ | -1773.19 ¹ | 24 |
| `div.grid` | [Cel mai căutat Nuntă Pachet Premium Sâmb] | [Buget redus Botez Pachet Standard Sâmbăt] | 24 ¹ | 24 ¹ | 24 ¹ | 24 |
| `div.grid` | [Buget redus Botez Pachet Standard Sâmbăt] | [Cel mai căutat Botez Pachet Premium Sâmb] | -829 ¹ | -901 ¹ | -1062.19 ¹ | 24 |
| `article.glass-card` | Buget redus | Nuntă | 25.50 | 25.50 | 25.50 | 17.50 |
| `article.glass-card` | Nuntă | Pachet Standard | 8 | 8 | 8 | 8 |
| `article.glass-card` | Pachet Standard | [Sâmbătă De confirmat5.500 €] | 20 | 20 | 20 | 20 |
| `article.glass-card` | [Sâmbătă De confirmat5.500 €] | Formație live, doi interpreți și DJ pentru toată | 20 | 20 | 20 | 20 |
| `article.glass-card` | Formație live, doi interpreți și DJ pentru toată | [Formație de 4 instrumente: clapă, vioară] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Formație de 4 instrumente: clapă, vioară] | [Duminică De confirmat4.800 €] | 343.50 | 391.50 | 507 | 24 |
| `article.glass-card` | [Duminică De confirmat4.800 €] | Scrieți-ne pe WhatsApp | 24 | 24 | 24 | 24 |
| `div.mb-5` | Sâmbătă | [De confirmat5.500 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 5.500 € | -35.19 ¹ | -35.19 ¹ | 4 | -31.19 ¹ |
| `ul.motif-list` | Formație de 4 instrumente: clapă, vioară, acorde | Un interpret de muzică populară și de petrecere | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică populară și de petrecere | Un interpret de muzică ușoară românească și inte | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică ușoară românească și inte | DJ și MC pe toată durata evenimentului | 12 | 12 | 12 | 12 |
| `ul.motif-list` | DJ și MC pe toată durata evenimentului | Sonorizare profesională, dimensionată după sală  | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Sonorizare profesională, dimensionată după sală  | Mașină de fum greu pentru valsul mirilor | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Mașină de fum greu pentru valsul mirilor | Gheață carbonică la primirea invitaților și la m | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Gheață carbonică la primirea invitaților și la m | Muzică de tip cafe-concert la primirea invitațil | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Muzică de tip cafe-concert la primirea invitațil | Moment de virtuozitate instrumentală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Moment de virtuozitate instrumentală | Consultanță pentru organizarea serii, fără cost  | 12 | 12 | 12 | 12 |
| `div.mt-auto` | Duminică | [De confirmat4.800 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 4.800 € | -27.19 ¹ | -27.19 ¹ | -27.19 ¹ | -24.19 ¹ |
| `article.glass-card` | Cel mai căutat | Nuntă | 27.50 | 27.50 | 27.50 | 19.50 |
| `article.glass-card` | Nuntă | Pachet Premium | 8 | 8 | 8 | 8 |
| `article.glass-card` | Pachet Premium | [Sâmbătă De confirmat6.500 €] | 20 | 20 | 20 | 20 |
| `article.glass-card` | [Sâmbătă De confirmat6.500 €] | Formație extinsă, trei interpreți și producție c | 20 | 20 | 20 | 20 |
| `article.glass-card` | Formație extinsă, trei interpreți și producție c | [Formație de 6 instrumente: clapă, vioară] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Formație de 6 instrumente: clapă, vioară] | Elementele marcate „opțional” se tarifează separ | 24 | 24 | 24 | 24 |
| `article.glass-card` | Elementele marcate „opțional” se tarifează separ | [Duminică De confirmat5.500 €] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Duminică De confirmat5.500 €] | Scrieți-ne pe WhatsApp | 24 | 24 | 24 | 24 |
| `div.mb-5` | Sâmbătă | [De confirmat6.500 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 6.500 € | -35.19 ¹ | -35.19 ¹ | 4 | -31.19 ¹ |
| `ul.motif-list` | Formație de 6 instrumente: clapă, vioară, saxofo | Țambal | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Țambal | Un interpret de muzică populară și de petrecere | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică populară și de petrecere | Un interpret de muzică ușoară | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică ușoară | Un interpret de muzică balcanică | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică balcanică | DJ și MC profesionist pe toată durata evenimentu | 12 | 12 | 12 | 12 |
| `ul.motif-list` | DJ și MC profesionist pe toată durata evenimentu | Ecran LED cu imagini personalizate | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Ecran LED cu imagini personalizate | Sonorizare profesională | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Sonorizare profesională | Mașină de fum greu și gheață carbonică | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Mașină de fum greu și gheață carbonică | Zece corpuri de lumină ambientală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Zece corpuri de lumină ambientală | Vulcani CO2 pe toată durata petrecerii | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Vulcani CO2 pe toată durata petrecerii | Schelă profesională de lumini, cu 4–6 moving-hea | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Schelă profesională de lumini, cu 4–6 moving-hea | Cabină foto trei ore, cu accesorii și fotografii | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Cabină foto trei ore, cu accesorii și fotografii | Cabină foto 360 | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Cabină foto 360 | Panou floral sau glamour, la alegerea dumneavoas | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Panou floral sau glamour, la alegerea dumneavoas | Inginer de sunet și lumini prezent toată seara | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Inginer de sunet și lumini prezent toată seara | Staff tehnic pentru montaj și demontaj | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Staff tehnic pentru montaj și demontaj | Prestație muzicală fără limită de programe | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Prestație muzicală fără limită de programe | Consultanță pentru organizarea serii, fără cost  | 12 | 12 | 12 | 12 |
| `div.mt-auto` | Duminică | [De confirmat5.500 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 5.500 € | -27.19 ¹ | -27.19 ¹ | -27.19 ¹ | -24.19 ¹ |
| `article.glass-card` | Buget redus | Botez | 25.50 | 25.50 | 25.50 | 17.50 |
| `article.glass-card` | Botez | Pachet Standard | 8 | 8 | 8 | 8 |
| `article.glass-card` | Pachet Standard | [Sâmbătă De confirmat3.200 €] | 20 | 20 | 20 | 20 |
| `article.glass-card` | [Sâmbătă De confirmat3.200 €] | Formație de trei instrumente și DJ, cu două prog | 20 | 20 | 20 | 20 |
| `article.glass-card` | Formație de trei instrumente și DJ, cu două prog | [Formație de 3 instrumente: clapă, saxofo] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Formație de 3 instrumente: clapă, saxofo] | [Duminică De confirmat2.800 €] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Duminică De confirmat2.800 €] | Scrieți-ne pe WhatsApp | 24 | 24 | 24 | 24 |
| `div.mb-5` | Sâmbătă | [De confirmat3.200 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 3.200 € | -35.19 ¹ | -35.19 ¹ | 4 | -31.19 ¹ |
| `ul.motif-list` | Formație de 3 instrumente: clapă, saxofon și vio | Un interpret de muzică populară și ușoară, în do | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică populară și ușoară, în do | DJ profesionist pe toată durata evenimentului | 12 | 12 | 12 | 12 |
| `ul.motif-list` | DJ profesionist pe toată durata evenimentului | Sonorizare profesională, dimensionată după sală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Sonorizare profesională, dimensionată după sală | Muzică de tip cafe-concert la primirea invitațil | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Muzică de tip cafe-concert la primirea invitațil | Moment de virtuozitate instrumentală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Moment de virtuozitate instrumentală | Consultanță pentru organizarea evenimentului, fă | 12 | 12 | 12 | 12 |
| `div.mt-auto` | Duminică | [De confirmat2.800 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 2.800 € | -27.19 ¹ | -27.19 ¹ | -27.18 ¹ | -24.19 ¹ |
| `article.glass-card` | Cel mai căutat | Botez | 27.50 | 27.50 | 27.50 | 19.50 |
| `article.glass-card` | Botez | Pachet Premium | 8 | 8 | 8 | 8 |
| `article.glass-card` | Pachet Premium | [Sâmbătă De confirmat3.800 €] | 20 | 20 | 20 | 20 |
| `article.glass-card` | [Sâmbătă De confirmat3.800 €] | Formație de patru instrumente pentru un sunet ma | 20 | 20 | 20 | 20 |
| `article.glass-card` | Formație de patru instrumente pentru un sunet ma | [Formație de 4 instrumente: clapă, acorde] | 24 | 24 | 24 | 24 |
| `article.glass-card` | [Formație de 4 instrumente: clapă, acorde] | [Duminică De confirmat3.300 €] | 24 | 48 | 48 | 24 |
| `article.glass-card` | [Duminică De confirmat3.300 €] | Scrieți-ne pe WhatsApp | 24 | 24 | 24 | 24 |
| `div.mb-5` | Sâmbătă | [De confirmat3.800 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 3.800 € | -35.19 ¹ | -35.19 ¹ | 4 | -31.19 ¹ |
| `ul.motif-list` | Formație de 4 instrumente: clapă, acordeon, saxo | Un interpret de muzică populară și ușoară | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Un interpret de muzică populară și ușoară | DJ profesionist pe toată durata evenimentului | 12 | 12 | 12 | 12 |
| `ul.motif-list` | DJ profesionist pe toată durata evenimentului | Sonorizare profesională, dimensionată după sală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Sonorizare profesională, dimensionată după sală | Muzică de tip cafe-concert la primirea invitațil | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Muzică de tip cafe-concert la primirea invitațil | Moment de virtuozitate instrumentală | 12 | 12 | 12 | 12 |
| `ul.motif-list` | Moment de virtuozitate instrumentală | Consultanță pentru organizarea evenimentului, fă | 12 | 12 | 12 | 12 |
| `div.mt-auto` | Duminică | [De confirmat3.300 €] | 8 | 8 | 8 | 8 |
| `span.price-tbc` | De confirmat | 3.300 € | -27.19 ¹ | -27.19 ¹ | -27.18 ¹ | -24.19 ¹ |
| `figure.max-w-5xl` | div.border | Configurația extinsă, cu țambal — inclus opționa | 16 | 16 | 16 | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 500px 500px | 24px | 24px | **NU** — 829…1328.50, delta 499.50 |
| `div.grid` | 1024 | grid | 436px 436px | 24px | 24px | **NU** — 901…1424.50, delta 523.50 |
| `div.grid` | 768 | grid | 308px 308px | 24px | 24px | **NU** — 1062.19…1773.19, delta 711 |
| `div.grid` | 390 | grid | 342px | 24px | 24px | **NU** — 969…1632, delta 663 |

`mt-auto` in `div.grid` — `rect.bottom` card − `rect.bottom` element impins jos (constant intre carduri = chiar functioneaza):

| Card | Element impins | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|
| card 1 | [Duminică De confirmat4.800 €] | 111 | 111 | 111 | 103 |
| card 2 | [Duminică De confirmat5.500 €] | 111 | 111 | 111 | 103 |
| card 3 | [Duminică De confirmat2.800 €] | 111 | 111 | 111 | 103 |
| card 4 | [Duminică De confirmat3.300 €] | 111 | 111 | 111 | 103 |

Verdict: 1440: constant, 1024: constant, 768: constant, 390: constant.
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 91.72 | 10px | 4px | **NU** — 13.19…36, delta 22.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 61.14 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 91.72 | 10px | 4px | **NU** — 13.19…36, delta 22.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 61.14 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 91.72 | 10px | 4px | **NU** — 13.19…36, delta 22.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 61.14 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 110.06 | 10px | 4px | **NU** — 13.19…40, delta 26.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 91.72 | 10px | 4px | **NU** — 13.19…36, delta 22.81 |
| `span.price-tbc` | 1440 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 1024 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 768 | inline-flex | 101.91 + 73.38 | 10px | 4px | **NU** — 13.19…32, delta 18.81 |
| `span.price-tbc` | 390 | inline-flex | 101.91 + 61.14 | 10px | 4px | **NU** — 13.19…28, delta 14.81 |

---

## S4 — Acoperire

`section` · clase: `max-w-max-width mx-auto px-6 md:px-margin-desktop mb-16 md:mb-24`

Eyebrow: «Unde cântăm»

Titlu: «Acoperire»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 208 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 208 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 236 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 296 | 0/24/0/24 | transparent | none |
| **container interior** | 1440 | 768 | 208 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 768 | 208 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 236 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 342 | 296 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1440 | 768 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1024 | 768 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 768 | 640 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 390 | 342 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2#acoperire-titlu`) | 1440 | 768 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2#acoperire-titlu`) | 1024 | 768 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2#acoperire-titlu`) | 768 | 640 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`h2#acoperire-titlu`) | 390 | 342 | 32 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 1440 | 768 | 112 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 1024 | 768 | 112 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 768 | 640 | 140 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`p.font-body-lg`) | 390 | 342 | 208 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Unde cântăm | span | 1440 | 336 | 4210 | 768 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Unde cântăm | span | 1024 | 128 | 4282 | 768 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Unde cântăm | span | 768 | 64 | 4655.88 | 640 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Unde cântăm | span | 390 | 24 | 6409 | 342 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Acoperire | h2 | 1440 | 336 | 4242 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Acoperire | h2 | 1024 | 128 | 4314 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Acoperire | h2 | 768 | 64 | 4687.88 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Acoperire | h2 | 390 | 24 | 6441 | 342 | 32 | 24 | 32 | normal | 400 | #e5e2e1 | center |
| Cele mai multe evenimente le avem în București,  | p | 1440 | 336 | 4306 | 768 | 112 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Cele mai multe evenimente le avem în București,  | p | 1024 | 128 | 4378 | 768 | 112 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Cele mai multe evenimente le avem în București,  | p | 768 | 64 | 4751.88 | 640 | 140 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Cele mai multe evenimente le avem în București,  | p | 390 | 24 | 6497 | 342 | 208 | 16 | 26 | normal | 400 | #c4c7c7 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-3xl` | Unde cântăm | Acoperire | 12 | 12 | 12 | 12 |
| `div.max-w-3xl` | Acoperire | Cele mai multe evenimente le avem în București,  | 24 | 24 | 24 | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S5 — Preț, rezervare și contract

`section` · clase: `py-16 md:py-24 bg-background`

Eyebrow: «Întrebări Frecvente»

Titlu: «Preț, rezervare și contract»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 1038 | 96/0/96/0 | #131313 | none |
| **section** | 1024 | 1024 | 1038 | 96/0/96/0 | #131313 | none |
| **section** | 768 | 768 | 1038 | 96/0/96/0 | #131313 | none |
| **section** | 390 | 390 | 946 | 64/0/64/0 | #131313 | none |
| **container interior** | 1440 | 1200 | 846 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 846 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 846 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 818 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1440 | 1072 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1024 | 896 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 768 | 640 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 390 | 358 | 122 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 1440 | 768 | 570 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 1024 | 768 | 570 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 768 | 640 | 570 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.max-w-3xl`) | 390 | 358 | 572 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1440 | 1072 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 1024 | 896 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 768 | 640 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`div.text-center`) | 390 | 358 | 44 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Întrebări Frecvente | span | 1440 | 184 | 4610 | 1072 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 1024 | 64 | 4682 | 896 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 768 | 64 | 5083.88 | 640 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Întrebări Frecvente | span | 390 | 16 | 6833 | 358 | 20 | 14 | 20 | 4.20 | 600 | #c8c6c5 | center |
| Preț, rezervare și contract | h2 | 1440 | 184 | 4646 | 1072 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Preț, rezervare și contract | h2 | 1024 | 64 | 4718 | 896 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Preț, rezervare și contract | h2 | 768 | 64 | 5119.88 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Preț, rezervare și contract | h2 | 390 | 16 | 6869 | 358 | 42 | 28 | 42 | normal | 400 | #e5e2e1 | center |
| Prețul unei formații pentru 2026-2027? | h3 | 1440 | 361 | 4819 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 1024 | 153 | 4891 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 768 | 89 | 5292.88 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 390 | 37 | 7016 | 256.84 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 4827 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 4899 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5300.88 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 7019 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1440 | 337 | 4875 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1024 | 129 | 4947 | 766 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 768 | 65 | 5348.88 | 638 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 390 | 17 | 7058 | 356 | 144 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cum rezerv data — avans și contract? | h3 | 1440 | 361 | 5013 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 1024 | 153 | 5085 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 768 | 89 | 5486.88 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 390 | 37 | 7240 | 243.53 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 5021 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 5093 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5494.88 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 7243 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Data se blochează pe bază de contract și un avan | div | 1440 | 337 | 5069 | 766 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 1024 | 129 | 5141 | 766 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 768 | 65 | 5542.88 | 638 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 390 | 17 | 7282 | 356 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cât este avansul și când se achită restul? | h3 | 1440 | 361 | 5111 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 1024 | 153 | 5183 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 768 | 89 | 5584.88 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 390 | 37 | 7320 | 255.17 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 5119 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 5191 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5592.88 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 7323 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 1440 | 361 | 5167 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 1024 | 153 | 5239 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 768 | 89 | 5640.88 | 590 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 390 | 37 | 7362 | 316 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 377 | 5181 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 169 | 5253 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 105 | 5654.88 | 558 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 53 | 7376 | 284 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 1440 | 361 | 5209 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 1024 | 153 | 5281 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 768 | 89 | 5682.88 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 390 | 37 | 7400 | 284 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 5217 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 5289 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5690.88 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 7414 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 1440 | 361 | 5265 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 1024 | 153 | 5337 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 768 | 89 | 5738.88 | 590 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 390 | 37 | 7464 | 316 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 377 | 5279 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 169 | 5351 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 105 | 5752.88 | 558 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 53 | 7478 | 284 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 1440 | 361 | 5307 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 1024 | 153 | 5379 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 768 | 89 | 5780.88 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 390 | 37 | 7502 | 284 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1063 | 5315 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 855 | 5387 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 663 | 5788.88 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 337 | 7516 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 1440 | 361 | 5363 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 1024 | 153 | 5435 | 718 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 768 | 89 | 5836.88 | 590 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 390 | 37 | 7566 | 316 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 377 | 5377 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 169 | 5449 | 686 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 105 | 5850.88 | 558 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 53 | 7580 | 284 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Vezi toate întrebările frecvente | a | 1440 | 553.95 | 5412 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 1024 | 345.95 | 5484 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 768 | 217.95 | 5885.88 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Vezi toate întrebările frecvente | a | 390 | 28.95 | 7607 | 332.09 | 44 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1440 | 868.05 | 5425 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 1024 | 660.05 | 5497 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 768 | 532.05 | 5898.88 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |
| svg (icon) | svg | 390 | 343.05 | 7620 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Întrebări Frecvente Preț, rezervare și c] | [Prețul unei formații pentru 2026-2027? P] | 64 | 64 | 64 | 40 |
| `div.max-w-[1200px]` | [Prețul unei formații pentru 2026-2027? P] | [Vezi toate întrebările frecvente] | 48 | 48 | 48 | 40 |
| `div.text-center` | Întrebări Frecvente | Preț, rezervare și contract | 16 | 16 | 16 | 16 |
| `div.text-center` | Preț, rezervare și contract | div.motif-rule | 20 | 20 | 20 | 20 |
| `div.max-w-3xl` | [Prețul unei formații pentru 2026-2027? P] | [Cum rezerv data — avans și contract? Dat] | 16 | 16 | 16 | 16 |
| `div.max-w-3xl` | [Cum rezerv data — avans și contract? Dat] | [Cât este avansul și când se achită restu] | 16 | 16 | 16 | 16 |
| `div.max-w-3xl` | [Cât este avansul și când se achită restu] | [Cu cât timp înainte ar trebui să vă cont] | 16 | 16 | 16 | 16 |
| `div.max-w-3xl` | [Cu cât timp înainte ar trebui să vă cont] | [Ce se întâmplă dacă trebuie să amân even] | 16 | 16 | 16 | 16 |
| `details.group` | [Prețul unei formații pentru 2026-2027?] | Prețul depinde de pachet, de tipul evenimentului | 0 | 0 | 0 | 0 |
| `summary.flex` | Prețul unei formații pentru 2026-2027? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cum rezerv data — avans și contract?] | Data se blochează pe bază de contract și un avan | 0 | 0 | 0 | 0 |
| `summary.flex` | Cum rezerv data — avans și contract? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cât este avansul și când se achită restu] | [Răspuns de confirmatAvansul se achită la] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cât este avansul și când se achită restul? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cu cât timp înainte ar trebui să vă cont] | [Răspuns de confirmatPentru nunțile din s] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cu cât timp înainte ar trebui să vă contactez? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [Ce se întâmplă dacă trebuie să amân even] | [Răspuns de confirmatAmânarea se discută ] | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce se întâmplă dacă trebuie să amân evenimentul? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 256.84 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 243.53 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 255.17 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 284 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 284 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |

---

## S6 — Verificați dacă data este liberă

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-t border-outline-variant/10 text-center`

Titlu: «Verificați dacă data este liberă»

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
| Verificați dacă data este liberă | h2 | 1440 | 400 | 5649 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Verificați dacă data este liberă | h2 | 1024 | 192 | 5721 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Verificați dacă data este liberă | h2 | 768 | 64 | 6122.88 | 640 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Verificați dacă data este liberă | h2 | 390 | 16 | 7780 | 358 | 35 | 28 | 35 | normal | 400 | #e5e2e1 | center |
| Scrieți-ne data și localitatea. Vă răspundem în  | p | 1440 | 400 | 5725 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-ne data și localitatea. Vă răspundem în  | p | 1024 | 192 | 5797 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-ne data și localitatea. Vă răspundem în  | p | 768 | 64 | 6198.88 | 640 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Scrieți-ne data și localitatea. Vă răspundem în  | p | 390 | 16 | 7835 | 358 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Rezervă pe WhatsApp | a | 1440 | 449.77 | 5821 | 293.72 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 1024 | 241.77 | 5893 | 293.72 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 768 | 113.77 | 6294.88 | 293.72 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 390 | 16 | 7947 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| +40 722 911 485 | a | 1440 | 759.48 | 5821 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 1024 | 551.48 | 5893 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 768 | 423.48 | 6294.88 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 390 | 16 | 8017 | 358 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-2xl` | Verificați dacă data este liberă | Scrieți-ne data și localitatea. Vă răspundem în  | 20 | 20 | 20 | 20 |
| `div.max-w-2xl` | Scrieți-ne data și localitatea. Vă răspundem în  | [Rezervă pe WhatsApp +40 722 911 485] | 40 | 40 | 40 | 40 |
| `div.flex` | Rezervă pe WhatsApp | +40 722 911 485 | -62 ¹ | -62 ¹ | -62 ¹ | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 293.72 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 1024 | flex | 293.72 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 768 | flex | 293.72 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 390 | flex | 358 + 358 | 16px | 16px | da (54) |

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Pachete și prețuri pentru nuntă și botez» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `h2` «Patru pachete, pentru nuntă și pentru botez» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `span` «Buget redus» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `h3` «Pachet Standard» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `span` «Sâmbătă» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400, font-size masurat 12px
- `span` «Duminică» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[12px]`; weight rezolvat 400, font-size masurat 12px
- `span` «Cel mai căutat» — `font-label-md` (tokenul poarta weight) + marime arbitrara `text-[11px]`; weight rezolvat 400, font-size masurat 11px
- `h3` «Pachet Premium» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `p` «Elementele marcate „opțional” se tarifează separ» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[13px]`; weight rezolvat 400, font-size masurat 13px
- `h2` «Acoperire» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `h2` «Preț, rezervare și contract» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `h3` «Prețul unei formații pentru 2026-2027?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cum rezerv data — avans și contract?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cât este avansul și când se achită restul?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cu cât timp înainte ar trebui să vă contactez?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Ce se întâmplă dacă trebuie să amân evenimentul?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Verificați dacă data este liberă» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/48px

### Borduri care vin din `assets/styles.css`, nu din clase

- `div.max-w-5xl` «[Condiții comerciale Prețurile sunt expri]» — T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat__ RON/km]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.motif-rule__gem` «span.motif-rule__gem» — T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.glass-card` «[Buget redus Nuntă Pachet Standard Sâmbăt]» — T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat5.500 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat4.800 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.glass-card` «[Cel mai căutat Nuntă Pachet Premium Sâmb]» — T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat6.500 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.block` «Scrieți-ne pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.glass-card` «[Buget redus Botez Pachet Standard Sâmbăt]» — T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat3.200 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat2.800 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `article.glass-card` «[Cel mai căutat Botez Pachet Premium Sâmb]» — T 1px #c6c6c6 @0.2, R 1px #c6c6c6 @0.2, B 1px #c6c6c6 @0.2, L 1px #c6c6c6 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat3.800 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.price-tbc` «[De confirmat3.300 €]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Avansul se achită la semnarea contractului și bl» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Pentru nunțile din sezonul cald, ideal cu 8–12 l» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Amânarea se discută direct cu noi și se consemne» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.inline-block` «Rezervă pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «[Formație de 4 instrumente: clapă, vioară]» declara `mb-*` ∈ {24}px, dar distanta reala pana la «[Duminică De confirmat4.800 €]» e 343.50px la 1440
- «[Formație de 4 instrumente: clapă, vioară]» declara `mb-*` ∈ {24}px, dar distanta reala pana la «[Duminică De confirmat4.800 €]» e 391.50px la 1024
- «[Formație de 4 instrumente: clapă, vioară]» declara `mb-*` ∈ {24}px, dar distanta reala pana la «[Duminică De confirmat4.800 €]» e 507px la 768
- «[Formație de 4 instrumente: clapă, acorde]» declara `mb-*` ∈ {24}px, dar distanta reala pana la «[Duminică De confirmat3.300 €]» e 48px la 1024
- «[Formație de 4 instrumente: clapă, acorde]» declara `mb-*` ∈ {24}px, dar distanta reala pana la «[Duminică De confirmat3.300 €]» e 48px la 768

### Suprapuneri intre elemente

- in `section`: «div.absolute» si «[Oferte 2026-2027 Pachete și prețuri pent]» se suprapun pe verticala cu 364px la 1440 (suprapunere orizontala 736.75px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Oferte 2026-2027 Pachete și prețuri pent]» se suprapun pe verticala cu 364px la 1024 (suprapunere orizontala 736.75px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Oferte 2026-2027 Pachete și prețuri pent]» se suprapun pe verticala cu 420px la 768 (suprapunere orizontala 640px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `section`: «div.absolute» si «[Oferte 2026-2027 Pachete și prețuri pent]» se suprapun pe verticala cu 403px la 390 (suprapunere orizontala 342px, position absolute/relative) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «img ioana-balan-live-show.jpg» si «div.absolute» se suprapun pe verticala cu 404px la 1440 (suprapunere orizontala 1440px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «img ioana-balan-live-show.jpg» si «div.absolute» se suprapun pe verticala cu 404px la 1024 (suprapunere orizontala 1024px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «img ioana-balan-live-show.jpg» si «div.absolute» se suprapun pe verticala cu 460px la 768 (suprapunere orizontala 768px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.absolute`: «img ioana-balan-live-show.jpg» si «div.absolute» se suprapun pe verticala cu 443px la 390 (suprapunere orizontala 390px, position static/absolute) — stratificare intentionata (`position: absolute`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Pachete și prețuri pentru nuntă și botez | 1440: 1440 · 1024: 1024 · 768: 768 · 390: 390 | vert (sectiune): 40 sus / 40 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Condiții comerciale | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | — | — | o singura coloana |
| Patru pachete, pentru nuntă și pentru botez (#pachete) | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | 1440: 56/32/32/32<br>1024: 56/32/32/32<br>768: 56/32/32/32<br>390: 48/24/24/24 | x 24px / y 24px | in `div.grid` (lat. 1024 la 1440, grid):<br>1440: 500 + 500 + 500 + 500 · 1024: 436 + 436 + 436 + 436 · 768: 308 + 308 + 308 + 308 · 390: 342 + 342 + 342 + 342 |
| Acoperire | 1440: 1072 · 1024: 896 · 768: 640 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 24 L / 24 R | — | — | o singura coloana |
| Preț, rezervare și contract | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 766 la 1440, flex):<br>1440: 390.91 + 16 · 1024: 390.91 + 16 · 768: 390.91 + 16 · 390: 256.84 + 16 |
| Verificați dacă data este liberă | 1440: 640 · 1024: 640 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 16 L / 16 R | 1440: 20/48/20/48<br>1024: 20/48/20/48<br>768: 20/48/20/48<br>390: 16/32/16/32 | x 16px / y 16px | in `div.flex` (lat. 640 la 1440, flex):<br>1440: 293.72 + 230.73 · 1024: 293.72 + 230.73 · 768: 293.72 + 230.73 · 390: 358 + 358 |
