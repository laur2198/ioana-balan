# Geometrie randata — `galerie.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/galerie.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 3092.75 | 160/0/96/0 | transparent | none |
| `<main>` | 1024 | 1024 | 2845.25 | 160/0/96/0 | transparent | none |
| `<main>` | 768 | 768 | 3289.39 | 160/0/96/0 | transparent | none |
| `<main>` | 390 | 390 | 3770.50 | 128/0/64/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 3524px, 1024 → 3276px, 768 → 3766px, 390 → 4358px.

Sectiuni masurate: **3**.

---

## S1 — Galerie de Spectacole

`section` · clase: `max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop mb-12 md:mb-20 text-center`

Eyebrow: «Arhivă Vizuală & Portofoliu»

Titlu: «Galerie de Spectacole»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 200 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 200 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 200 | 0/64/0/64 | transparent | none |
| **section** | 390 | 390 | 208 | 0/16/0/16 | transparent | none |
| **container 1** (`span.font-label-md`) | 1440 | 1072 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 1024 | 896 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 768 | 640 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 390 | 358 | 20 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1440 | 1072 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1024 | 896 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 768 | 640 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 390 | 358 | 36 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-md`) | 1440 | 768 | 84 | 0/16/0/16 | transparent | none |
| **container 3** (`p.font-body-md`) | 1024 | 768 | 84 | 0/16/0/16 | transparent | none |
| **container 3** (`p.font-body-md`) | 768 | 640 | 84 | 0/16/0/16 | transparent | none |
| **container 3** (`p.font-body-md`) | 390 | 358 | 120 | 0/16/0/16 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arhivă Vizuală & Portofoliu | span | 1440 | 184 | 160 | 1072 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Arhivă Vizuală & Portofoliu | span | 1024 | 64 | 160 | 896 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Arhivă Vizuală & Portofoliu | span | 768 | 64 | 160 | 640 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Arhivă Vizuală & Portofoliu | span | 390 | 16 | 128 | 358 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | center |
| Galerie de Spectacole | h1 | 1440 | 184 | 196 | 1072 | 56 | 48 | 56 | -0.96 | 500 | #c8c6c5 | center |
| Galerie de Spectacole | h1 | 1024 | 64 | 196 | 896 | 56 | 48 | 56 | -0.96 | 500 | #c8c6c5 | center |
| Galerie de Spectacole | h1 | 768 | 64 | 196 | 640 | 56 | 48 | 56 | -0.96 | 500 | #c8c6c5 | center |
| Galerie de Spectacole | h1 | 390 | 16 | 164 | 358 | 36 | 30 | 36 | normal | 400 | #c8c6c5 | center |
| Descoperă cele mai frumoase imagini live de la n | p | 1440 | 336 | 276 | 768 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Descoperă cele mai frumoase imagini live de la n | p | 1024 | 128 | 276 | 768 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Descoperă cele mai frumoase imagini live de la n | p | 768 | 64 | 276 | 640 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Descoperă cele mai frumoase imagini live de la n | p | 390 | 16 | 216 | 358 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | Arhivă Vizuală & Portofoliu | Galerie de Spectacole | 16 | 16 | 16 | 16 |
| `section` | Galerie de Spectacole | Descoperă cele mai frumoase imagini live de la n | 24 | 24 | 24 | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S2 — Cum arată un eveniment (#clipuri)

`section#clipuri` · clase: `bg-surface-container-low py-16 md:py-24`

Eyebrow: «Evenimente»

Titlu: «Cum arată un eveniment»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 1915.75 | 96/0/96/0 | #1c1b1b | none |
| **section** | 1024 | 1024 | 1668.25 | 96/0/96/0 | #1c1b1b | none |
| **section** | 768 | 768 | 2112.39 | 96/0/96/0 | #1c1b1b | none |
| **section** | 390 | 390 | 2552 | 64/0/64/0 | #1c1b1b | none |
| **container interior** | 1440 | 1200 | 1723.75 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 1476.25 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 1920.39 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 2424 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.flex`) | 1440 | 1072 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 1024 | 896 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 768 | 640 | 72 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 390 | 358 | 100 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.gallery-grid`) | 1440 | 1072 | 1595.75 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.gallery-grid`) | 1024 | 896 | 1348.25 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.gallery-grid`) | 768 | 640 | 1792.39 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.gallery-grid`) | 390 | 358 | 2284 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Evenimente | span | 1440 | 184 | 536 | 312.66 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 1024 | 64 | 536 | 312.66 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 768 | 64 | 536 | 312.66 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Evenimente | span | 390 | 16 | 448 | 234.48 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Cum arată un eveniment | h2 | 1440 | 184 | 568 | 312.66 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Cum arată un eveniment | h2 | 1024 | 64 | 568 | 312.66 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Cum arată un eveniment | h2 | 768 | 64 | 568 | 312.66 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Cum arată un eveniment | h2 | 390 | 16 | 480 | 234.48 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Vezi canalul YouTube | a | 1440 | 1028.42 | 588 | 227.58 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi canalul YouTube | a | 1024 | 732.42 | 588 | 227.58 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi canalul YouTube | a | 768 | 476.42 | 588 | 227.58 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Vezi canalul YouTube | a | 390 | 16 | 528 | 227.58 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1440 | 1238 | 589 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 942 | 589 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 686 | 589 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 225.58 | 529 | 18 | 18 | 18 | 20 | 1.40 | 600 | #c8c6c5 | start |
| img BcUXKbLqrsU.jpg | img | 1440 | 185 | 665 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img BcUXKbLqrsU.jpg | img | 1024 | 65 | 665 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img BcUXKbLqrsU.jpg | img | 768 | 65 | 665 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img BcUXKbLqrsU.jpg | img | 390 | 17 | 589 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 436.50 | 800.38 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 272.50 | 775.63 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 263.83 | 770.73 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 677.69 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Muzică de petrecere | span | 1440 | 205 | 895.06 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică de petrecere | span | 1024 | 85 | 845.56 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică de petrecere | span | 768 | 85 | 835.80 | 376.66 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică de petrecere | span | 390 | 37 | 730.69 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Atmosferă de petrecere la nuntă | span | 1440 | 205 | 912.66 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Atmosferă de petrecere la nuntă | span | 1024 | 85 | 863.16 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Atmosferă de petrecere la nuntă | span | 768 | 85 | 853.39 | 376.66 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Atmosferă de petrecere la nuntă | span | 390 | 37 | 748.28 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| img ioana-balan-hora-mireasa-1440.jpg | img | 1440 | 733 | 665 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-hora-mireasa-1440.jpg | img | 1024 | 525 | 665 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-hora-mireasa-1440.jpg | img | 768 | 65 | 924.48 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-hora-mireasa-1440.jpg | img | 390 | 17 | 806.38 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-lumina-violet-1440.jpg | img | 1440 | 185 | 983.75 | 522 | 318.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-lumina-violet-1440.jpg | img | 1024 | 65 | 934.25 | 434 | 269.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-lumina-violet-1440.jpg | img | 768 | 507.66 | 665 | 195.33 | 492.97 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-lumina-violet-1440.jpg | img | 390 | 17 | 1023.75 | 169 | 356 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-rochie-alba-imprimeu-694.jpg | img | 1440 | 733 | 983.75 | 522 | 0 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-rochie-alba-imprimeu-694.jpg | img | 1024 | 525 | 934.25 | 434 | 0 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-rochie-alba-imprimeu-694.jpg | img | 768 | 65 | 1183.97 | 195.33 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-rochie-alba-imprimeu-694.jpg | img | 390 | 204 | 1023.75 | 169 | 169 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img 3uyEZ2vY6eE.jpg | img | 1440 | 733 | 1009.75 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img 3uyEZ2vY6eE.jpg | img | 1024 | 525 | 960.25 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img 3uyEZ2vY6eE.jpg | img | 768 | 286.33 | 1183.97 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img 3uyEZ2vY6eE.jpg | img | 390 | 17 | 1397.75 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 984.50 | 1145.13 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 732.50 | 1070.88 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 485.16 | 1289.70 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 1486.44 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Live la nuntă | span | 1440 | 753 | 1239.81 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Live la nuntă | span | 1024 | 545 | 1140.81 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Live la nuntă | span | 768 | 306.33 | 1354.77 | 376.66 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Live la nuntă | span | 390 | 37 | 1539.44 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| „Un trandafir crește la firida mea” | span | 1440 | 753 | 1257.41 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Un trandafir crește la firida mea” | span | 1024 | 545 | 1158.41 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Un trandafir crește la firida mea” | span | 768 | 306.33 | 1372.36 | 376.66 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Un trandafir crește la firida mea” | span | 390 | 37 | 1557.03 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| img hora-nunta-invitati-1024.jpg | img | 1440 | 185 | 1328.50 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 1024 | 65 | 1229.50 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 768 | 65 | 1443.45 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img hora-nunta-invitati-1024.jpg | img | 390 | 17 | 1615.13 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-sala-eveniment-480.jpg | img | 1440 | 733 | 1328.50 | 248 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-sala-eveniment-480.jpg | img | 1024 | 525 | 1229.50 | 204 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-sala-eveniment-480.jpg | img | 768 | 507.66 | 1443.45 | 195.33 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-sala-eveniment-480.jpg | img | 390 | 204 | 1210.75 | 169 | 169 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img Yqw4PZ0pU5o.jpg | img | 1440 | 185 | 1647.25 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Yqw4PZ0pU5o.jpg | img | 1024 | 65 | 1498.75 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Yqw4PZ0pU5o.jpg | img | 768 | 65 | 1702.94 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Yqw4PZ0pU5o.jpg | img | 390 | 17 | 1832.50 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 436.50 | 1782.63 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 272.50 | 1609.38 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 263.83 | 1808.67 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 1921.19 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Cover live · 2025 | span | 1440 | 205 | 1877.31 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Cover live · 2025 | span | 1024 | 85 | 1679.31 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Cover live · 2025 | span | 768 | 85 | 1873.73 | 376.66 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Cover live · 2025 | span | 390 | 37 | 1974.19 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| „Am atins cerul cu mâna” | span | 1440 | 205 | 1894.91 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Am atins cerul cu mâna” | span | 1024 | 85 | 1696.91 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Am atins cerul cu mâna” | span | 768 | 85 | 1891.33 | 376.66 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Am atins cerul cu mâna” | span | 390 | 37 | 1991.78 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| img formatie-ring-dans-480.jpg | img | 1440 | 1007 | 1328.50 | 248 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-ring-dans-480.jpg | img | 1024 | 755 | 1229.50 | 204 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-ring-dans-480.jpg | img | 768 | 507.66 | 1702.94 | 195.33 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-ring-dans-480.jpg | img | 390 | 17 | 2049.88 | 169 | 169 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-sacouri-albe-480.jpg | img | 1440 | 733 | 1647.25 | 248 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-sacouri-albe-480.jpg | img | 1024 | 525 | 1498.75 | 204 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-sacouri-albe-480.jpg | img | 768 | 65 | 1962.42 | 195.33 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-sacouri-albe-480.jpg | img | 390 | 204 | 2049.88 | 169 | 169 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img iIYF1xiX6sM.jpg | img | 1440 | 185 | 1966 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img iIYF1xiX6sM.jpg | img | 1024 | 65 | 1768 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img iIYF1xiX6sM.jpg | img | 768 | 286.33 | 1962.42 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img iIYF1xiX6sM.jpg | img | 390 | 17 | 2236.88 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 436.50 | 2101.38 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 272.50 | 1878.63 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 485.16 | 2068.16 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 2325.56 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Nuntă · botez · corporate | span | 1440 | 205 | 2196.06 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Nuntă · botez · corporate | span | 1024 | 85 | 1948.56 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Nuntă · botez · corporate | span | 768 | 306.33 | 2133.22 | 376.66 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Nuntă · botez · corporate | span | 390 | 37 | 2378.56 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Muzică de petrecere live | span | 1440 | 205 | 2213.66 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Muzică de petrecere live | span | 1024 | 85 | 1966.16 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Muzică de petrecere live | span | 768 | 306.33 | 2150.81 | 376.66 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| Muzică de petrecere live | span | 390 | 37 | 2396.16 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |
| img formatie-lumini-scena-480.jpg | img | 1440 | 1007 | 1647.25 | 248 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-lumini-scena-480.jpg | img | 1024 | 755 | 1498.75 | 204 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-lumini-scena-480.jpg | img | 768 | 65 | 2221.91 | 195.33 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img formatie-lumini-scena-480.jpg | img | 390 | 17 | 2454.25 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img Fj15ExZHAYs.jpg | img | 1440 | 733 | 1966 | 522 | 292.75 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Fj15ExZHAYs.jpg | img | 1024 | 525 | 1768 | 434 | 243.25 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Fj15ExZHAYs.jpg | img | 768 | 286.33 | 2221.91 | 416.66 | 233.48 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| img Fj15ExZHAYs.jpg | img | 390 | 17 | 2671.63 | 356 | 199.38 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1440 | 984.50 | 2101.38 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 1024 | 732.50 | 1878.63 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 768 | 485.16 | 2327.64 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| svg (icon) | svg | 390 | 185.50 | 2760.31 | 22 | 22 | 16 | 24 | normal | 400 | #e5e2e1 | left |
| Colaj live · 2024 | span | 1440 | 753 | 2196.06 | 482 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Colaj live · 2024 | span | 1024 | 545 | 1948.56 | 394 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Colaj live · 2024 | span | 768 | 306.33 | 2392.70 | 376.66 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| Colaj live · 2024 | span | 390 | 37 | 2813.31 | 316 | 12 | 10 | 12 | 1.80 | 600 | #ffffff @0.8 | left |
| „Ce naș, ce nașă” · „Jos pălăria” | span | 1440 | 753 | 2213.66 | 482 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Ce naș, ce nașă” · „Jos pălăria” | span | 1024 | 545 | 1966.16 | 394 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Ce naș, ce nașă” · „Jos pălăria” | span | 768 | 306.33 | 2410.30 | 376.66 | 27.50 | 22 | 27.50 | normal | 500 | #ffffff | left |
| „Ce naș, ce nașă” · „Jos pălăria” | span | 390 | 37 | 2830.91 | 316 | 22.50 | 18 | 22.50 | normal | 500 | #ffffff | left |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.max-w-[1200px]` | [Evenimente Cum arată un eveniment Vezi c] | [Muzică de petrecere Atmosferă de petrece] | 56 | 56 | 56 | 40 |
| `div.flex` | [Evenimente Cum arată un eveniment] | Vezi canalul YouTube | -20 ¹ | -20 ¹ | -20 ¹ | 16 |
| `div` | Evenimente | Cum arată un eveniment | 12 | 12 | 12 | 12 |
| `div.gallery-grid` | [Muzică de petrecere Atmosferă de petrece] | div.relative | -294.75 ¹ | -245.25 ¹ | 24 | 16 |
| `div.gallery-grid` | div.relative | div.relative | 24 ¹ | 24 ¹ | -494.97 ¹ | 16 |
| `div.gallery-grid` | div.relative | div.relative | -320.75 ¹ | -271.25 ¹ | 24 ¹ | -358 ¹ |
| `div.gallery-grid` | div.relative | [Live la nuntă „Un trandafir crește la fi] | 24 | 24 | -235.48 ¹ | 203 |
| `div.gallery-grid` | [Live la nuntă „Un trandafir crește la fi] | div.relative | 24 ¹ | 24 ¹ | 24 | 16 |
| `div.gallery-grid` | div.relative | div.relative | -294.75 ¹ | -245.25 ¹ | -235.49 ¹ | -605.75 |
| `div.gallery-grid` | div.relative | [Cover live · 2025 „Am atins cerul cu mân] | 24 ¹ | 24 ¹ | 24 ¹ | 450.75 |
| `div.gallery-grid` | [Cover live · 2025 „Am atins cerul cu mân] | div.relative | -613.50 ¹ | -514.50 ¹ | -235.48 ¹ | 16 |
| `div.gallery-grid` | div.relative | div.relative | 24 ¹ | 24 ¹ | 24 ¹ | -171 ¹ |
| `div.gallery-grid` | div.relative | [Nuntă · botez · corporate Muzică de petr] | 24 ¹ | 24 ¹ | -235.49 ¹ | 16 |
| `div.gallery-grid` | [Nuntă · botez · corporate Muzică de petr] | div.relative | -613.50 ¹ | -514.50 ¹ | 24 ¹ | 16 |
| `div.gallery-grid` | div.relative | [Colaj live · 2024 „Ce naș, ce nașă” · „J] | 24 | 24 | -235.48 ¹ | 16 |
| `button.video-card` | img BcUXKbLqrsU.jpg | span.video-card__veil | -292.75 | -243.25 | -233.48 | -199.38 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -148.75 | -131.69 |
| `button.video-card` | span.video-card__play | [Muzică de petrecere Atmosferă de petrece] | 31.68 | 6.93 | 2.07 | -10 |
| `span.video-card__meta` | Muzică de petrecere | Atmosferă de petrecere la nuntă | 5.60 | 5.60 | 5.59 | 5.59 |
| `button.video-card` | img 3uyEZ2vY6eE.jpg | span.video-card__veil | -292.75 | -243.25 | -233.48 | -199.38 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -148.75 | -131.69 |
| `button.video-card` | span.video-card__play | [Live la nuntă „Un trandafir crește la fi] | 31.68 | 6.93 | 2.07 | -10 |
| `span.video-card__meta` | Live la nuntă | „Un trandafir crește la firida mea” | 5.60 | 5.60 | 5.59 | 5.59 |
| `button.video-card` | img Yqw4PZ0pU5o.jpg | span.video-card__veil | -292.75 | -243.25 | -233.48 | -199.38 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -148.75 | -131.69 |
| `button.video-card` | span.video-card__play | [Cover live · 2025 „Am atins cerul cu mân] | 31.68 | 6.93 | 2.06 | -10 |
| `span.video-card__meta` | Cover live · 2025 | „Am atins cerul cu mâna” | 5.60 | 5.60 | 5.60 | 5.59 |
| `button.video-card` | img iIYF1xiX6sM.jpg | span.video-card__veil | -292.75 | -243.25 | -233.49 | -199.37 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -148.75 | -131.69 |
| `button.video-card` | span.video-card__play | [Nuntă · botez · corporate Muzică de petr] | 31.68 | 6.93 | 2.06 | -10 |
| `span.video-card__meta` | Nuntă · botez · corporate | Muzică de petrecere live | 5.60 | 5.60 | 5.59 | 5.60 |
| `button.video-card` | img Fj15ExZHAYs.jpg | span.video-card__veil | -292.75 | -243.25 | -233.48 | -199.37 |
| `button.video-card` | span.video-card__veil | span.video-card__play | -178.37 | -153.62 | -148.75 | -131.69 |
| `button.video-card` | span.video-card__play | [Colaj live · 2024 „Ce naș, ce nașă” · „J] | 31.68 | 6.93 | 2.06 | -10 |
| `span.video-card__meta` | Colaj live · 2024 | „Ce naș, ce nașă” · „Jos pălăria” | 5.60 | 5.60 | 5.60 | 5.60 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 312.66 + 227.58 | 16px | 16px | **NU** — 20…72, delta 52 |
| `div.flex` | 1024 | flex | 312.66 + 227.58 | 16px | 16px | **NU** — 20…72, delta 52 |
| `div.flex` | 768 | flex | 312.66 + 227.58 | 16px | 16px | **NU** — 20…72, delta 52 |
| `div.flex` | 390 | flex | 234.48 + 227.58 | 16px | 16px | **NU** — 20…64, delta 44 |
| `div.gallery-grid` | 1440 | grid | 250px 250px 250px 250px | 24px | 24px | **NU** — 2…320.75, delta 318.75 |
| `div.gallery-grid` | 1024 | grid | 206px 206px 206px 206px | 24px | 24px | **NU** — 2…271.25, delta 269.25 |
| `div.gallery-grid` | 768 | grid | 197.328px 197.328px 197.328px | 24px | 24px | **NU** — 235.48…494.97, delta 259.49 |
| `div.gallery-grid` | 390 | grid | 171px 171px | 16px | 16px | **NU** — 171…358, delta 187 |

---

## S3 — Esența Tradiției în Imagini.

`section` · clase: `max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop py-20 md:py-32 border-t border-outline-variant/10`

Titlu: «Esența Tradiției în Imagini.»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 641 | 128/64/128/64 | transparent | T 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 641 | 128/64/128/64 | transparent | T 1px #444748 @0.1 |
| **section** | 768 | 768 | 641 | 128/64/128/64 | transparent | T 1px #444748 @0.1 |
| **section** | 390 | 390 | 770.50 | 80/16/80/16 | transparent | T 1px #444748 @0.1 |
| **container interior** | 1440 | 1072 | 384 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 896 | 384 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 640 | 384 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 358 | 609.50 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1440 | 524 | 258 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 1024 | 436 | 334 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 768 | 308 | 382 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.text-center`) | 390 | 358 | 305.50 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.relative`) | 1440 | 524 | 384 | 0/0/0/0 | transparent | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| └ coloana 2 (`div.relative`) | 1024 | 436 | 384 | 0/0/0/0 | transparent | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| └ coloana 2 (`div.relative`) | 768 | 308 | 384 | 0/0/0/0 | transparent | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |
| └ coloana 2 (`div.relative`) | 390 | 358 | 256 | 0/0/0/0 | transparent | T 1px #444748 @0.15, R 1px #444748 @0.15, B 1px #444748 @0.15, L 1px #444748 @0.15 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Esența Tradiției în Imagini. | h2 | 1440 | 184 | 2547.75 | 524 | 56 | 48 | 56 | -0.96 | 500 | #c8c6c5 | left |
| Esența Tradiției în Imagini. | h2 | 1024 | 64 | 2262.25 | 436 | 112 | 48 | 56 | -0.96 | 500 | #c8c6c5 | left |
| Esența Tradiției în Imagini. | h2 | 768 | 64 | 2682.39 | 308 | 112 | 48 | 56 | -0.96 | 500 | #c8c6c5 | left |
| Esența Tradiției în Imagini. | h2 | 390 | 16 | 3017 | 358 | 37.50 | 30 | 37.50 | normal | 400 | #c8c6c5 | center |
| Rămâneți la curent cu ultimele mele spectacole ș | p | 1440 | 184 | 2627.75 | 524 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | left |
| Rămâneți la curent cu ultimele mele spectacole ș | p | 1024 | 64 | 2398.25 | 436 | 84 | 18 | 28 | normal | 400 | #c6c6c6 | left |
| Rămâneți la curent cu ultimele mele spectacole ș | p | 768 | 64 | 2818.39 | 308 | 112 | 18 | 28 | normal | 400 | #c6c6c6 | left |
| Rămâneți la curent cu ultimele mele spectacole ș | p | 390 | 16 | 3070.50 | 358 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Rezervă pe WhatsApp | a | 1440 | 184 | 2751.75 | 277.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 1024 | 64 | 2522.25 | 245.16 | 74 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 768 | 64 | 2970.39 | 173.28 | 94 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 390 | 16 | 3198.50 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Cere ofertă | a | 1440 | 477.72 | 2751.75 | 193.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 1024 | 325.16 | 2522.25 | 174.84 | 74 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 768 | 253.28 | 2970.39 | 146.42 | 94 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 390 | 16 | 3268.50 | 358 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| img ioana-balan-portret-sesiune-foto-cal.jpg | img | 1440 | 733 | 2485.75 | 522 | 382 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-sesiune-foto-cal.jpg | img | 1024 | 525 | 2238.25 | 434 | 382 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-sesiune-foto-cal.jpg | img | 768 | 397 | 2682.39 | 306 | 382 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portret-sesiune-foto-cal.jpg | img | 390 | 17 | 3371.50 | 356 | 254 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| IOANA BALAN | p | 1440 | 901.08 | 2652.75 | 185.84 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| IOANA BALAN | p | 1024 | 649.08 | 2405.25 | 185.84 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| IOANA BALAN | p | 768 | 457.08 | 2849.39 | 185.84 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| IOANA BALAN | p | 390 | 102.08 | 3474.50 | 185.84 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | center |
| Autenticitate în fiecare notă. | p | 1440 | 901.08 | 2680.75 | 185.84 | 20 | 14 | 20 | normal | 400 | #c6c6c6 | center |
| Autenticitate în fiecare notă. | p | 1024 | 649.08 | 2433.25 | 185.84 | 20 | 14 | 20 | normal | 400 | #c6c6c6 | center |
| Autenticitate în fiecare notă. | p | 768 | 457.08 | 2877.39 | 185.84 | 20 | 14 | 20 | normal | 400 | #c6c6c6 | center |
| Autenticitate în fiecare notă. | p | 390 | 102.08 | 3502.50 | 185.84 | 20 | 14 | 20 | normal | 400 | #c6c6c6 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | [Esența Tradiției în Imagini. Rămâneți la] | [IOANA BALAN Autenticitate în fiecare not] | -321 ¹ | -359 ¹ | -383 ¹ | 48 |
| `div.text-center` | Esența Tradiției în Imagini. | Rămâneți la curent cu ultimele mele spectacole ș | 24 | 24 | 24 | 16 |
| `div.text-center` | Rămâneți la curent cu ultimele mele spectacole ș | [Rezervă pe WhatsApp Cere ofertă] | 40 | 40 | 40 | 32 |
| `div.flex` | Rezervă pe WhatsApp | Cere ofertă | -54 ¹ | -74 ¹ | -94 ¹ | 16 |
| `div.relative` | img ioana-balan-portret-sesiune-foto-cal.jpg | [IOANA BALAN Autenticitate în fiecare not] | -382 | -382 | -382 | -254 |
| `div.text-center` | IOANA BALAN | Autenticitate în fiecare notă. | 8 | 8 | 8 | 8 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 524px 524px | 24px | 24px | **NU** — 258…384, delta 126 |
| `div.grid` | 1024 | grid | 436px 436px | 24px | 24px | **NU** — 334…384, delta 50 |
| `div.grid` | 768 | grid | 308px 308px | 24px | 24px | **NU** — 382…384, delta 2 |
| `div.grid` | 390 | grid | 358px | 48px | 48px | **NU** — 256…305.50, delta 49.50 |
| `div.flex` | 1440 | flex | 277.72 + 193.36 | 16px | 16px | da (54) |
| `div.flex` | 1024 | flex | 245.16 + 174.84 | 16px | 16px | da (74) |
| `div.flex` | 768 | flex | 173.28 + 146.42 | 16px | 16px | da (94) |
| `div.flex` | 390 | flex | 358 + 358 | 16px | 16px | da (54) |

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Galerie de Spectacole» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400
- `h2` «Esența Tradiției în Imagini.» — font-weight **difera intre viewport-uri**: 1440: 500, 1024: 500, 768: 500, 390: 400

### Borduri care vin din `assets/styles.css`, nu din clase

- `button.video-card` «[Muzică de petrecere Atmosferă de petrece]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.video-card__play` «span.video-card__play» — T 2px #ffffff @0.85, R 2px #ffffff @0.85, B 2px #ffffff @0.85, L 2px #ffffff @0.85, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Live la nuntă „Un trandafir crește la fi]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Cover live · 2025 „Am atins cerul cu mân]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Nuntă · botez · corporate Muzică de petr]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `button.video-card` «[Colaj live · 2024 „Ce naș, ce nașă” · „J]» — T 1px #444748 @0.2, R 1px #444748 @0.2, B 1px #444748 @0.2, L 1px #444748 @0.2, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.w-full` «Rezervă pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Suprapuneri intre elemente

- in `button.video-card`: «img BcUXKbLqrsU.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 178.37px la 1440 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img BcUXKbLqrsU.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 153.62px la 1024 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img BcUXKbLqrsU.jpg» si «span.video-card__veil» se suprapun pe verticala cu 233.48px la 768 (suprapunere orizontala 416.66px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 148.75px la 768 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img BcUXKbLqrsU.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.38px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__veil» si «span.video-card__play» se suprapun pe verticala cu 131.69px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Muzică de petrecere Atmosferă de petrece]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img 3uyEZ2vY6eE.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img 3uyEZ2vY6eE.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img 3uyEZ2vY6eE.jpg» si «span.video-card__veil» se suprapun pe verticala cu 233.48px la 768 (suprapunere orizontala 416.65px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img 3uyEZ2vY6eE.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.38px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Live la nuntă „Un trandafir crește la fi]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Yqw4PZ0pU5o.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Yqw4PZ0pU5o.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Yqw4PZ0pU5o.jpg» si «span.video-card__veil» se suprapun pe verticala cu 233.48px la 768 (suprapunere orizontala 416.66px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Yqw4PZ0pU5o.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.38px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Cover live · 2025 „Am atins cerul cu mân]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img iIYF1xiX6sM.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img iIYF1xiX6sM.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img iIYF1xiX6sM.jpg» si «span.video-card__veil» se suprapun pe verticala cu 233.49px la 768 (suprapunere orizontala 416.65px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img iIYF1xiX6sM.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.37px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Nuntă · botez · corporate Muzică de petr]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Fj15ExZHAYs.jpg» si «span.video-card__veil» se suprapun pe verticala cu 292.75px la 1440 (suprapunere orizontala 522px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Fj15ExZHAYs.jpg» si «span.video-card__veil» se suprapun pe verticala cu 243.25px la 1024 (suprapunere orizontala 434px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Fj15ExZHAYs.jpg» si «span.video-card__veil» se suprapun pe verticala cu 233.48px la 768 (suprapunere orizontala 416.65px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «img Fj15ExZHAYs.jpg» si «span.video-card__veil» se suprapun pe verticala cu 199.37px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `button.video-card`: «span.video-card__play» si «[Colaj live · 2024 „Ce naș, ce nașă” · „J]» se suprapun pe verticala cu 10px la 390 (suprapunere orizontala 64px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img ioana-balan-portret-sesiune-foto-cal.jpg» si «[IOANA BALAN Autenticitate în fiecare not]» se suprapun pe verticala cu 382px la 1440 (suprapunere orizontala 522px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img ioana-balan-portret-sesiune-foto-cal.jpg» si «[IOANA BALAN Autenticitate în fiecare not]» se suprapun pe verticala cu 382px la 1024 (suprapunere orizontala 434px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img ioana-balan-portret-sesiune-foto-cal.jpg» si «[IOANA BALAN Autenticitate în fiecare not]» se suprapun pe verticala cu 382px la 768 (suprapunere orizontala 306px, position static/absolute) — stratificare intentionata (`position: absolute`)
- in `div.relative`: «img ioana-balan-portret-sesiune-foto-cal.jpg» si «[IOANA BALAN Autenticitate în fiecare not]» se suprapun pe verticala cu 254px la 390 (suprapunere orizontala 356px, position static/absolute) — stratificare intentionata (`position: absolute`)

### Ordine vizuala diferita de ordinea din document

- in `div.gallery-grid` la 390 — ordinea vizuala difera de cea din document: document = «[Muzică de petrecere Atmosferă de petrece]» → «div.relative» → «div.relative» → «div.relative» → «[Live la nuntă „Un trandafir crește la fi]» → «div.relative» → «div.relative» → «[Cover live · 2025 „Am atins cerul cu mân]» → «div.relative» → «div.relative» → «[Nuntă · botez · corporate Muzică de petr]» → «div.relative» → «[Colaj live · 2024 „Ce naș, ce nașă” · „J]»; vizual = «[Muzică de petrecere Atmosferă de petrece]» → «div.relative» → «div.relative» → «div.relative» → «div.relative» → «[Live la nuntă „Un trandafir crește la fi]» → «div.relative» → «[Cover live · 2025 „Am atins cerul cu mân]» → «div.relative» → «div.relative» → «[Nuntă · botez · corporate Muzică de petr]» → «div.relative» → «[Colaj live · 2024 „Ce naș, ce nașă” · „J]» (utilitare `order-*`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Galerie de Spectacole | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | — | — | o singura coloana |
| Cum arată un eveniment (#clipuri) | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | x 16px / y 16px | in `div.flex` (lat. 1072 la 1440, flex):<br>1440: 312.66 + 227.58 · 1024: 312.66 + 227.58 · 768: 312.66 + 227.58 · 390: 234.48 + 227.58 |
| Esența Tradiției în Imagini. | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 128 sus / 128 jos · 1024: 128 sus / 128 jos · 768: 128 sus / 128 jos · 390: 80 sus / 80 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | 1440: x 24px / y 24px · 1024: x 24px / y 24px · 768: x 24px / y 24px · 390: x 48px / y 48px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 524 + 524 · 1024: 436 + 436 · 768: 308 + 308 · 390: 358 + 358 |
