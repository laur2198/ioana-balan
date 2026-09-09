# Geometrie randata — `politica-cookie.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/politica-cookie.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 6616.48 | 128/0/96/0 | transparent | none |
| `<main>` | 1024 | 1024 | 6616.48 | 128/0/96/0 | transparent | none |
| `<main>` | 768 | 768 | 6616.48 | 128/0/96/0 | transparent | none |
| `<main>` | 390 | 390 | 7271.20 | 96/0/64/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 7047px, 1024 → 7047px, 768 → 7093px, 390 → 7858px.

Sectiuni masurate: **21**.

---

## S1 — [EXEMPLU]

`aside` · clase: `legal-draft-banner mb-10 md:mb-14`

Eyebrow: «[EXEMPLU]»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 178 | 20/24/20/24 | #c41236 @0.14 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236 |
| **section** | 1024 | 576 | 178 | 20/24/20/24 | #c41236 @0.14 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236 |
| **section** | 768 | 576 | 178 | 20/24/20/24 | #c41236 @0.14 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236 |
| **section** | 390 | 342 | 276 | 20/24/20/24 | #c41236 @0.14 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236 |
| **container 1** (`p#avertisment-titlu`) | 1440 | 521 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`p#avertisment-titlu`) | 1024 | 521 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`p#avertisment-titlu`) | 768 | 521 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`p#avertisment-titlu`) | 390 | 287 | 40 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 1440 | 521 | 104 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 1024 | 521 | 104 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 768 | 521 | 104 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-md`) | 390 | 287 | 182 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.legal-tbc`) | 1440 | 104.73 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 1024 | 104.73 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 768 | 104.73 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 390 | 104.73 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Document în lucru — nu este în vigoare | p | 1440 | 462 | 149 | 521 | 20 | 14 | 20 | 2.52 | 600 | #ffffff | start |
| Document în lucru — nu este în vigoare | p | 1024 | 254 | 149 | 521 | 20 | 14 | 20 | 2.52 | 600 | #ffffff | start |
| Document în lucru — nu este în vigoare | p | 768 | 126 | 149 | 521 | 20 | 14 | 20 | 2.52 | 600 | #ffffff | start |
| Document în lucru — nu este în vigoare | p | 390 | 54 | 117 | 287 | 40 | 14 | 20 | 2.52 | 600 | #ffffff | start |
| Textul de mai jos este o versiune de lucru, afiș | p | 1440 | 462 | 181 | 521 | 104 | 16 | 26 | normal | 400 | #e5e2e1 | start |
| Textul de mai jos este o versiune de lucru, afiș | p | 1024 | 254 | 181 | 521 | 104 | 16 | 26 | normal | 400 | #e5e2e1 | start |
| Textul de mai jos este o versiune de lucru, afiș | p | 768 | 126 | 181 | 521 | 104 | 16 | 26 | normal | 400 | #e5e2e1 | start |
| Textul de mai jos este o versiune de lucru, afiș | p | 390 | 54 | 169 | 287 | 182 | 16 | 26 | normal | 400 | #e5e2e1 | start |
| [EXEMPLU] | span | 1440 | 611.48 | 207 | 104.73 | 26 | 16 | 26 | normal | 600 | #e5e2e1 | start |
| [EXEMPLU] | span | 1024 | 403.48 | 207 | 104.73 | 26 | 16 | 26 | normal | 600 | #e5e2e1 | start |
| [EXEMPLU] | span | 768 | 275.48 | 207 | 104.73 | 26 | 16 | 26 | normal | 600 | #e5e2e1 | start |
| [EXEMPLU] | span | 390 | 143.05 | 221 | 104.73 | 26 | 16 | 26 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `aside.legal-draft-banner` | Document în lucru — nu este în vigoare | Textul de mai jos este o versiune de lucru, afiș | 12 | 12 | 12 | 12 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S2 — Politica de cookie-uri

`header` · clase: `mb-8 md:mb-10`

Eyebrow: «Document legal»

Titlu: «Politica de cookie-uri»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 128 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 128 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 128 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 109.50 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 1440 | 576 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 1024 | 576 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 768 | 576 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 390 | 342 | 20 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1440 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1024 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 768 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 390 | 342 | 37.50 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-md`) | 1440 | 576 | 24 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-md`) | 1024 | 576 | 24 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-md`) | 768 | 576 | 24 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-md`) | 390 | 342 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong.font-semibold`) | 1440 | 143.98 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong.font-semibold`) | 1024 | 143.98 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong.font-semibold`) | 768 | 143.98 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong.font-semibold`) | 390 | 143.98 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`span.legal-tbc`) | 1440 | 166.09 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 1024 | 166.09 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 768 | 166.09 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 390 | 166.09 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Document legal | span | 1440 | 432 | 362 | 576 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Document legal | span | 1024 | 224 | 362 | 576 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Document legal | span | 768 | 96 | 362 | 576 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Document legal | span | 390 | 24 | 412 | 342 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Politica de cookie-uri | h1 | 1440 | 432 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Politica de cookie-uri | h1 | 1024 | 224 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Politica de cookie-uri | h1 | 768 | 96 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Politica de cookie-uri | h1 | 390 | 24 | 444 | 342 | 37.50 | 30 | 37.50 | normal | 400 | #e5e2e1 | start |
| Ultima actualizare: | strong | 1440 | 432 | 468 | 143.98 | 20 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| Ultima actualizare: | strong | 1024 | 224 | 468 | 143.98 | 20 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| Ultima actualizare: | strong | 768 | 96 | 468 | 143.98 | 20 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| Ultima actualizare: | strong | 390 | 24 | 499.50 | 143.98 | 20 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| [DATA-PUBLICARE] | span | 1440 | 580.48 | 465 | 166.09 | 26 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| [DATA-PUBLICARE] | span | 1024 | 372.48 | 465 | 166.09 | 26 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| [DATA-PUBLICARE] | span | 768 | 244.48 | 465 | 166.09 | 26 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| [DATA-PUBLICARE] | span | 390 | 172.48 | 496.50 | 166.09 | 26 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 587.48 | 465 | 1 | 1 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 379.48 | 465 | 1 | 1 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 251.48 | 465 | 1 | 1 | 16 | 24 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 179.48 | 496.50 | 1 | 1 | 16 | 24 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `header.mb-8` | Document legal | Politica de cookie-uri | 12 | 12 | 12 | 12 |
| `header.mb-8` | Politica de cookie-uri | [Ultima actualizare: valoare de completat] | 16 | 16 | 16 | 16 |
| `p.font-body-md` | Ultima actualizare: | [DATA-PUBLICARE] | -23 ¹ | -23 ¹ | -23 ¹ | -23 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S3 — div.motif-separator

`div` · clase: `motif-separator w-full mb-10 md:mb-12`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S4 — cuprins

`details#cuprins` · clase: `toc glass-card p-5 md:p-6 mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 491 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 1024 | 576 | 491 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 768 | 576 | 491 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 390 | 342 | 86 | 20/20/20/20 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **container 1** (`summary.flex`) | 1440 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 1024 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 768 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 390 | 300 | 44 | 0/0/0/0 | transparent | none |
| **container 2** (`nav.mt-4`) | 1440 | 526 | 381 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 1024 | 526 | 381 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 768 | 526 | 381 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 390 | 300 | 429 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| └ coloana 1 (`ol.flex`) | 1440 | 526 | 360 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 1024 | 526 | 360 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 768 | 526 | 360 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 390 | 300 | 408 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cuprins | summary | 1440 | 457 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 1024 | 249 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 768 | 121 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 390 | 45 | 638.50 | 300 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| 1. Ce sunt cookie-urile | a | 1440 | 457 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Ce sunt cookie-urile | a | 1024 | 249 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Ce sunt cookie-urile | a | 768 | 121 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Ce sunt cookie-urile | a | 390 | 45 | 719.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Temeiul legal | a | 1440 | 457 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Temeiul legal | a | 1024 | 249 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Temeiul legal | a | 768 | 121 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Temeiul legal | a | 390 | 45 | 759.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Ce cookie-uri folosim | a | 1440 | 457 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Ce cookie-uri folosim | a | 1024 | 249 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Ce cookie-uri folosim | a | 768 | 121 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Ce cookie-uri folosim | a | 390 | 45 | 799.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Conținut încorporat de la terți | a | 1440 | 457 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Conținut încorporat de la terți | a | 1024 | 249 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Conținut încorporat de la terți | a | 768 | 121 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Conținut încorporat de la terți | a | 390 | 45 | 839.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Cum vă puteți retrage consimțământul | a | 1440 | 457 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Cum vă puteți retrage consimțământul | a | 1024 | 249 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Cum vă puteți retrage consimțământul | a | 768 | 121 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Cum vă puteți retrage consimțământul | a | 390 | 45 | 879.50 | 300 | 64 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Cum puteți controla cookie-urile din browser | a | 1440 | 457 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Cum puteți controla cookie-urile din browser | a | 1024 | 249 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Cum puteți controla cookie-urile din browser | a | 768 | 121 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Cum puteți controla cookie-urile din browser | a | 390 | 45 | 943.50 | 300 | 64 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Drepturile dumneavoastră | a | 1440 | 457 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Drepturile dumneavoastră | a | 1024 | 249 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Drepturile dumneavoastră | a | 768 | 121 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Drepturile dumneavoastră | a | 390 | 45 | 1007.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Modificarea acestei politici | a | 1440 | 457 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Modificarea acestei politici | a | 1024 | 249 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Modificarea acestei politici | a | 768 | 121 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Modificarea acestei politici | a | 390 | 45 | 1047.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Contact | a | 1440 | 457 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Contact | a | 1024 | 249 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Contact | a | 768 | 121 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Contact | a | 390 | 45 | 1087.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `details#cuprins` | Cuprins | [1. Ce sunt cookie-urile 2. Temeiul legal] | 16 | 16 | 16 | 16 |
| `ol.flex` | [1. Ce sunt cookie-urile] | [2. Temeiul legal] | 0 | 0 | 0 | 0 |
| `ol.flex` | [2. Temeiul legal] | [3. Ce cookie-uri folosim] | 0 | 0 | 0 | 0 |
| `ol.flex` | [3. Ce cookie-uri folosim] | [4. Conținut încorporat de la terți] | 0 | 0 | 0 | 0 |
| `ol.flex` | [4. Conținut încorporat de la terți] | [5. Cum vă puteți retrage consimțământul] | 0 | 0 | 0 | 0 |
| `ol.flex` | [5. Cum vă puteți retrage consimțământul] | [6. Cum puteți controla cookie-urile din ] | 0 | 0 | 0 | 0 |
| `ol.flex` | [6. Cum puteți controla cookie-urile din ] | [7. Drepturile dumneavoastră] | 0 | 0 | 0 | 0 |
| `ol.flex` | [7. Drepturile dumneavoastră] | [8. Modificarea acestei politici] | 0 | 0 | 0 | 0 |
| `ol.flex` | [8. Modificarea acestei politici] | [9. Contact] | 0 | 0 | 0 | 0 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S5 — 1. Ce sunt cookie-urile (#sectiunea-1)

`section#sectiunea-1` · clase: `mb-12 md:mb-16`

Titlu: «1. Ce sunt cookie-urile»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 410.38 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 410.38 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 410.38 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 559.50 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 236.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`code`) | 1440 | 124.89 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 1 (`code`) | 1024 | 124.89 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 1 (`code`) | 768 | 124.89 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 1 (`code`) | 390 | 118.34 | 21 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 1440 | 143.70 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 1024 | 143.70 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 768 | 143.70 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 390 | 136.06 | 21 | 2/6/2/6 | #20201f | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. Ce sunt cookie-urile | h2 | 1440 | 432 | 1157 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Ce sunt cookie-urile | h2 | 1024 | 224 | 1157 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Ce sunt cookie-urile | h2 | 768 | 96 | 1157 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Ce sunt cookie-urile | h2 | 390 | 24 | 751.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Un cookie este un fișier de mici dimensiuni, alc | p | 1440 | 432 | 1217 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Un cookie este un fișier de mici dimensiuni, alc | p | 1024 | 224 | 1217 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Un cookie este un fișier de mici dimensiuni, alc | p | 768 | 96 | 1217 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Un cookie este un fișier de mici dimensiuni, alc | p | 390 | 24 | 801.50 | 342 | 236.75 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Cookie-urile nu pot rula programe, nu transmit v | p | 1440 | 432 | 1392.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Cookie-urile nu pot rula programe, nu transmit v | p | 1024 | 224 | 1392.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Cookie-urile nu pot rula programe, nu transmit v | p | 768 | 96 | 1392.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Cookie-urile nu pot rula programe, nu transmit v | p | 390 | 24 | 1056.25 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Pe lângă cookie-uri, site-urile pot folosi tehno | p | 1440 | 432 | 1473.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pe lângă cookie-uri, site-urile pot folosi tehno | p | 1024 | 224 | 1473.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pe lângă cookie-uri, site-urile pot folosi tehno | p | 768 | 96 | 1473.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pe lângă cookie-uri, site-urile pot folosi tehno | p | 390 | 24 | 1163.03 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| localStorage | code | 1440 | 579.72 | 1508.50 | 124.89 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| localStorage | code | 1024 | 371.72 | 1508.50 | 124.89 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| localStorage | code | 768 | 243.72 | 1508.50 | 124.89 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| localStorage | code | 390 | 96.09 | 1226.22 | 118.34 | 21 | 14.72 | 27.23 | normal | 400 | #e5e2e1 | start |
| sessionStorage | code | 1440 | 714.30 | 1508.50 | 143.70 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| sessionStorage | code | 1024 | 506.30 | 1508.50 | 143.70 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| sessionStorage | code | 768 | 378.30 | 1508.50 | 143.70 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| sessionStorage | code | 390 | 24 | 1255.81 | 136.06 | 21 | 14.72 | 27.23 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-1` | 1. Ce sunt cookie-urile | Un cookie este un fișier de mici dimensiuni, alc | 20 | 20 | 20 | 20 |
| `section#sectiunea-1` | Un cookie este un fișier de mici dimensiuni, alc | Cookie-urile nu pot rula programe, nu transmit v | 18 | 18 | 18 | 18 |
| `section#sectiunea-1` | Cookie-urile nu pot rula programe, nu transmit v | Pe lângă cookie-uri, site-urile pot folosi tehno | 18 | 18 | 18 | 18 |
| `p` | localStorage | sessionStorage | -23 ¹ | -23 ¹ | -23 ¹ | 8.59 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S6 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S7 — 2. Temeiul legal (#sectiunea-2)

`section#sectiunea-2` · clase: `mb-12 md:mb-16`

Titlu: «2. Temeiul legal»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 532.69 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 532.69 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 532.69 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 735.47 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1440 | 576 | 167.19 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1024 | 576 | 167.19 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 768 | 576 | 167.19 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 390 | 342 | 217.16 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 94.31 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 94.31 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 94.31 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 118.38 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| **container 4** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 207.16 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 122.78 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 122.78 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 122.78 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 323.53 | 49.59 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 1440 | 546.25 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 1024 | 546.25 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 768 | 546.25 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 390 | 320.75 | 79.19 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 227.81 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 227.81 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 227.81 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 291.89 | 49.59 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2. Temeiul legal | h2 | 1440 | 432 | 1719.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Temeiul legal | h2 | 1024 | 224 | 1719.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Temeiul legal | h2 | 768 | 96 | 1719.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Temeiul legal | h2 | 390 | 24 | 1431 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Utilizarea cookie-urilor este reglementată în Ro | p | 1440 | 432 | 1779.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea cookie-urilor este reglementată în Ro | p | 1024 | 224 | 1779.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea cookie-urilor este reglementată în Ro | p | 768 | 96 | 1779.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea cookie-urilor este reglementată în Ro | p | 390 | 24 | 1481 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| privind prelucrarea datelor cu caracter personal | li | 1440 | 432 | 1828.81 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| privind prelucrarea datelor cu caracter personal | li | 1024 | 224 | 1828.81 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| privind prelucrarea datelor cu caracter personal | li | 768 | 96 | 1828.81 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| privind prelucrarea datelor cu caracter personal | li | 390 | 24 | 1558.19 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| art. 4 alin. (5) din Legea nr. 506/2004 | strong | 1440 | 458 | 1833.81 | 306.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| art. 4 alin. (5) din Legea nr. 506/2004 | strong | 1024 | 250 | 1833.81 | 306.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| art. 4 alin. (5) din Legea nr. 506/2004 | strong | 768 | 122 | 1833.81 | 306.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| art. 4 alin. (5) din Legea nr. 506/2004 | strong | 390 | 50 | 1562.19 | 288.56 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| , atunci când prin cookie-uri se prelucrează dat | li | 1440 | 432 | 1933.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , atunci când prin cookie-uri se prelucrează dat | li | 1024 | 224 | 1933.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , atunci când prin cookie-uri se prelucrează dat | li | 768 | 96 | 1933.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , atunci când prin cookie-uri se prelucrează dat | li | 390 | 24 | 1686.56 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Regulamentul (UE) 2016/679 (GDPR) | strong | 1440 | 458 | 1938.13 | 298.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Regulamentul (UE) 2016/679 (GDPR) | strong | 1024 | 250 | 1938.13 | 298.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Regulamentul (UE) 2016/679 (GDPR) | strong | 768 | 122 | 1938.13 | 298.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Regulamentul (UE) 2016/679 (GDPR) | strong | 390 | 50 | 1690.56 | 281.02 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Regula este următoarea: cookie-urile funcționări | p | 1440 | 432 | 2014 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Regula este următoarea: cookie-urile funcționări | p | 1024 | 224 | 2014 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Regula este următoarea: cookie-urile funcționări | p | 768 | 96 | 2014 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Regula este următoarea: cookie-urile funcționări | p | 390 | 24 | 1793.34 | 342 | 207.16 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| strict necesare | strong | 1440 | 733.20 | 2019 | 122.78 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| strict necesare | strong | 1024 | 525.20 | 2019 | 122.78 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| strict necesare | strong | 768 | 397.20 | 2019 | 122.78 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| strict necesare | strong | 390 | 24 | 1797.34 | 323.53 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| numai după ce v-ați exprimat consimțământul prin | strong | 1440 | 432 | 2081.88 | 546.25 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce v-ați exprimat consimțământul prin | strong | 1024 | 224 | 2081.88 | 546.25 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce v-ați exprimat consimțământul prin | strong | 768 | 96 | 2081.88 | 546.25 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce v-ați exprimat consimțământul prin | strong | 390 | 24 | 1915.72 | 320.75 | 79.19 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Continuarea navigării, derularea paginii sau sim | p | 1440 | 432 | 2157.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Continuarea navigării, derularea paginii sau sim | p | 1024 | 224 | 2157.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Continuarea navigării, derularea paginii sau sim | p | 768 | 96 | 2157.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Continuarea navigării, derularea paginii sau sim | p | 390 | 24 | 2018.50 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| nu constituie consimțământ | strong | 1440 | 432 | 2194.19 | 227.81 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie consimțământ | strong | 1024 | 224 | 2194.19 | 227.81 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie consimțământ | strong | 768 | 96 | 2194.19 | 227.81 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie consimțământ | strong | 390 | 24 | 2052.09 | 291.89 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-2` | 2. Temeiul legal | Utilizarea cookie-urilor este reglementată în Ro | 20 | 20 | 20 | 20 |
| `section#sectiunea-2` | Utilizarea cookie-urilor este reglementată în Ro | [art. 4 alin. (5) din Legea nr. 506/2004 ] | 18 | 18 | 18 | 18 |
| `section#sectiunea-2` | [art. 4 alin. (5) din Legea nr. 506/2004 ] | Regula este următoarea: cookie-urile funcționări | 18 | 18 | 18 | 18 |
| `section#sectiunea-2` | Regula este următoarea: cookie-urile funcționări | Continuarea navigării, derularea paginii sau sim | 18 | 18 | 18 | 18 |
| `ul.motif-list` | privind prelucrarea datelor cu caracter personal | , atunci când prin cookie-uri se prelucrează dat | 10 | 10 | 10 | 10 |
| `p` | strict necesare | numai după ce v-ați exprimat consimțământul prin | 42.88 | 42.88 | 42.88 | 68.78 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S8 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S9 — 3. Ce cookie-uri folosim (#sectiunea-3)

`section#sectiunea-3` · clase: `mb-12 md:mb-16`

Eyebrow: «[NUME-COOKIE]»

Titlu: «3. Ce cookie-uri folosim»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 1075.42 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 1075.42 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 1075.42 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 1430.80 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`h3#sectiunea-3-1`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 2** (`h3#sectiunea-3-1`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 2** (`h3#sectiunea-3-1`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 2** (`h3#sectiunea-3-1`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 4** (`p.md:hidden`) | 1440 | **nerandat** | — | — | — | — |
| **container 4** (`p.md:hidden`) | 1024 | **nerandat** | — | — | — | — |
| **container 4** (`p.md:hidden`) | 768 | **nerandat** | — | — | — | — |
| **container 4** (`p.md:hidden`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 5** (`div.overflow-x-auto`) | 1440 | 800 | 98.98 | 0/0/0/0 | transparent | none |
| **container 5** (`div.overflow-x-auto`) | 1024 | 800 | 98.98 | 0/0/0/0 | transparent | none |
| **container 5** (`div.overflow-x-auto`) | 768 | 576 | 98.98 | 0/0/0/0 | transparent | none |
| **container 5** (`div.overflow-x-auto`) | 390 | 342 | 98.98 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 1440 | 800 | 98.98 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 1024 | 800 | 98.98 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 768 | 640 | 98.98 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 390 | 640 | 98.98 | 0/0/0/0 | transparent | none |
| **container 6** (`blockquote.legal-note`) | 1440 | 576 | 157.75 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 6** (`blockquote.legal-note`) | 1024 | 576 | 157.75 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 6** (`blockquote.legal-note`) | 768 | 576 | 157.75 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 6** (`blockquote.legal-note`) | 390 | 342 | 239.16 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| └ coloana 1 (`p`) | 1440 | 533 | 125.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 1024 | 533 | 125.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 768 | 533 | 125.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 390 | 299 | 207.16 | 0/0/0/0 | transparent | none |
| **container 7** (`h3#sectiunea-3-2`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 7** (`h3#sectiunea-3-2`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 7** (`h3#sectiunea-3-2`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 7** (`h3#sectiunea-3-2`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 524.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 524.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 524.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 320.19 | 49.59 | 0/0/0/0 | transparent | none |
| **container 9** (`blockquote.legal-note`) | 1440 | 576 | 220.63 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 9** (`blockquote.legal-note`) | 1024 | 576 | 220.63 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 9** (`blockquote.legal-note`) | 768 | 576 | 220.63 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| **container 9** (`blockquote.legal-note`) | 390 | 342 | 327.94 | 16/20/16/20 | #1c1b1b | L 3px #800020 |
| └ coloana 1 (`p`) | 1440 | 533 | 188.63 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 1024 | 533 | 188.63 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 768 | 533 | 188.63 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p`) | 390 | 299 | 295.94 | 0/0/0/0 | transparent | none |
| **container 10** (`h3#sectiunea-3-3`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 10** (`h3#sectiunea-3-3`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 10** (`h3#sectiunea-3-3`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 10** (`h3#sectiunea-3-3`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 559.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 559.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 559.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 262.86 | 49.59 | 0/0/0/0 | transparent | none |
| **container 12** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 12** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 12** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 12** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3. Ce cookie-uri folosim | h2 | 1440 | 432 | 2404.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Ce cookie-uri folosim | h2 | 1024 | 224 | 2404.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Ce cookie-uri folosim | h2 | 768 | 96 | 2404.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Ce cookie-uri folosim | h2 | 390 | 24 | 2286.47 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| 3.1 Cookie-uri strict necesare | h3 | 1440 | 432 | 2484.06 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.1 Cookie-uri strict necesare | h3 | 1024 | 224 | 2484.06 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.1 Cookie-uri strict necesare | h3 | 768 | 96 | 2484.06 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.1 Cookie-uri strict necesare | h3 | 390 | 24 | 2356.47 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Aceste cookie-uri sunt indispensabile pentru fun | p | 1440 | 432 | 2532.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste cookie-uri sunt indispensabile pentru fun | p | 1024 | 224 | 2532.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste cookie-uri sunt indispensabile pentru fun | p | 768 | 96 | 2532.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste cookie-uri sunt indispensabile pentru fun | p | 390 | 24 | 2402.47 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Glisați lateral pentru a vedea tot tabelul. | p | 1440 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 1024 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 768 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 390 | 24 | 2568.44 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Nume | th | 1440 | 320.50 | 2644.88 | 226.45 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Nume | th | 1024 | 112.50 | 2644.88 | 226.45 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Nume | th | 768 | 96.50 | 2644.88 | 181.09 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Nume | th | 390 | 24.50 | 2616.53 | 181.09 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Furnizor | th | 1440 | 546.95 | 2644.88 | 180.94 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Furnizor | th | 1024 | 338.95 | 2644.88 | 180.94 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Furnizor | th | 768 | 277.59 | 2644.88 | 144.70 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Furnizor | th | 390 | 205.59 | 2616.53 | 144.70 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 1440 | 727.89 | 2644.88 | 134.16 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 1024 | 519.89 | 2644.88 | 134.16 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 768 | 422.30 | 2644.88 | 107.28 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 390 | 350.30 | 2616.53 | 107.28 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată | th | 1440 | 862.05 | 2644.88 | 161.31 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată | th | 1024 | 654.05 | 2644.88 | 161.31 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată | th | 768 | 529.58 | 2644.88 | 129 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată | th | 390 | 457.58 | 2616.53 | 129 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Tip | th | 1440 | 1023.36 | 2644.88 | 96.14 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Tip | th | 1024 | 815.36 | 2644.88 | 96.14 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Tip | th | 768 | 658.58 | 2644.88 | 76.92 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Tip | th | 390 | 586.58 | 2616.53 | 76.92 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| [NUME-COOKIE] | span | 1440 | 337 | 2703.77 | 145.50 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [NUME-COOKIE] | span | 1024 | 129 | 2703.77 | 145.50 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [NUME-COOKIE] | span | 768 | 113 | 2703.77 | 145.50 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [NUME-COOKIE] | span | 390 | 41 | 2675.42 | 145.50 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1440 | 344 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1024 | 136 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 768 | 120 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 390 | 48 | 2675.42 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| ioana-balan.ro | td | 1440 | 546.95 | 2692.27 | 180.94 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| ioana-balan.ro | td | 1024 | 338.95 | 2692.27 | 180.94 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| ioana-balan.ro | td | 768 | 277.59 | 2692.27 | 144.70 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| ioana-balan.ro | td | 390 | 205.59 | 2663.92 | 144.70 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| [SCOP] | span | 1440 | 744.39 | 2703.77 | 72.75 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [SCOP] | span | 1024 | 536.39 | 2703.77 | 72.75 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [SCOP] | span | 768 | 438.80 | 2703.77 | 72.75 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [SCOP] | span | 390 | 366.80 | 2675.42 | 72.75 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1440 | 751.39 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1024 | 543.39 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 768 | 445.80 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 390 | 373.80 | 2675.42 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [DURATĂ] | span | 1440 | 878.55 | 2703.77 | 94.16 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [DURATĂ] | span | 1024 | 670.55 | 2703.77 | 94.16 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [DURATĂ] | span | 768 | 546.08 | 2703.77 | 94.16 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| [DURATĂ] | span | 390 | 474.08 | 2675.42 | 94.16 | 26 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1440 | 885.55 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 1024 | 677.55 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 768 | 553.08 | 2703.77 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| valoare de completat: | span | 390 | 481.08 | 2675.42 | 1 | 1 | 16 | 25.60 | normal | 600 | #e5e2e1 | left |
| HTTP | td | 1440 | 1023.36 | 2692.27 | 96.14 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| HTTP | td | 1024 | 815.36 | 2692.27 | 96.14 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| HTTP | td | 768 | 658.58 | 2692.27 | 76.92 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| HTTP | td | 390 | 586.58 | 2663.92 | 76.92 | 50.59 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Inventarul se stabilește prin scanarea site-ului | p | 1440 | 455 | 2779.36 | 533 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Inventarul se stabilește prin scanarea site-ului | p | 1024 | 247 | 2779.36 | 533 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Inventarul se stabilește prin scanarea site-ului | p | 768 | 119 | 2779.36 | 533 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Inventarul se stabilește prin scanarea site-ului | p | 390 | 47 | 2751.02 | 299 | 207.16 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| De completat după finalizarea site-ului. | strong | 1440 | 455 | 2784.36 | 322.05 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| De completat după finalizarea site-ului. | strong | 1024 | 247 | 2784.36 | 322.05 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| De completat după finalizarea site-ului. | strong | 768 | 119 | 2784.36 | 322.05 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| De completat după finalizarea site-ului. | strong | 390 | 47 | 2755.02 | 270.03 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| 3.2 Cookie-uri de analiză | h3 | 1440 | 432 | 2961.11 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.2 Cookie-uri de analiză | h3 | 1024 | 224 | 2961.11 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.2 Cookie-uri de analiză | h3 | 768 | 96 | 2961.11 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.2 Cookie-uri de analiză | h3 | 390 | 24 | 3014.17 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| În prezent, site-ul nu utilizează cookie-uri de  | strong | 1440 | 432 | 3014.11 | 524.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| În prezent, site-ul nu utilizează cookie-uri de  | strong | 1024 | 224 | 3014.11 | 524.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| În prezent, site-ul nu utilizează cookie-uri de  | strong | 768 | 96 | 3014.11 | 524.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| În prezent, site-ul nu utilizează cookie-uri de  | strong | 390 | 24 | 3064.17 | 320.19 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Dacă se activează ulterior un serviciu de analiz | p | 1440 | 455 | 3074.55 | 533 | 188.63 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă se activează ulterior un serviciu de analiz | p | 1024 | 247 | 3074.55 | 533 | 188.63 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă se activează ulterior un serviciu de analiz | p | 768 | 119 | 3074.55 | 533 | 188.63 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă se activează ulterior un serviciu de analiz | p | 390 | 47 | 3153.36 | 299 | 295.94 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 3.3 Cookie-uri de publicitate | h3 | 1440 | 432 | 3319.17 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.3 Cookie-uri de publicitate | h3 | 1024 | 224 | 3319.17 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.3 Cookie-uri de publicitate | h3 | 768 | 96 | 3319.17 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 3.3 Cookie-uri de publicitate | h3 | 390 | 24 | 3505.30 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Site-ul nu utilizează cookie-uri de publicitate  | strong | 1440 | 432 | 3372.17 | 559.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Site-ul nu utilizează cookie-uri de publicitate  | strong | 1024 | 224 | 3372.17 | 559.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Site-ul nu utilizează cookie-uri de publicitate  | strong | 768 | 96 | 3372.17 | 559.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Site-ul nu utilizează cookie-uri de publicitate  | strong | 390 | 24 | 3555.30 | 262.86 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Nu transmitem date către rețele publicitare și n | p | 1440 | 432 | 3416.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu transmitem date către rețele publicitare și n | p | 1024 | 224 | 3416.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu transmitem date către rețele publicitare și n | p | 768 | 96 | 3416.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu transmitem date către rețele publicitare și n | p | 390 | 24 | 3628.48 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-3` | 3. Ce cookie-uri folosim | 3.1 Cookie-uri strict necesare | 40 | 40 | 40 | 40 |
| `section#sectiunea-3` | 3.1 Cookie-uri strict necesare | Aceste cookie-uri sunt indispensabile pentru fun | 16 | 16 | 16 | 16 |
| `section#sectiunea-3` | Aceste cookie-uri sunt indispensabile pentru fun | Glisați lateral pentru a vedea tot tabelul. | n/r | n/r | n/r | 18 |
| `section#sectiunea-3` | Glisați lateral pentru a vedea tot tabelul. | [Nume Furnizor Scop Durată Tip valoare de] | n/r | n/r | n/r | 18 |
| `section#sectiunea-3` | [Nume Furnizor Scop Durată Tip valoare de] | [De completat după finalizarea site-ului.] | 20 | 20 | 20 | 20 |
| `section#sectiunea-3` | [De completat după finalizarea site-ului.] | 3.2 Cookie-uri de analiză | 40 | 40 | 40 | 40 |
| `section#sectiunea-3` | 3.2 Cookie-uri de analiză | [În prezent, site-ul nu utilizează cookie] | 16 | 16 | 16 | 16 |
| `section#sectiunea-3` | [În prezent, site-ul nu utilizează cookie] | [Dacă se activează ulterior un serviciu d] | 18 | 18 | 18 | 18 |
| `section#sectiunea-3` | [Dacă se activează ulterior un serviciu d] | 3.3 Cookie-uri de publicitate | 40 | 40 | 40 | 40 |
| `section#sectiunea-3` | 3.3 Cookie-uri de publicitate | [Site-ul nu utilizează cookie-uri de publ] | 16 | 16 | 16 | 16 |
| `section#sectiunea-3` | [Site-ul nu utilizează cookie-uri de publ] | Nu transmitem date către rețele publicitare și n | 18 | 18 | 18 | 18 |
| `table.legal-table` | [Nume Furnizor Scop Durată Tip] | [valoare de completat: [NUME-COOKIE] ioan] | 0 | 0 | 0 | 0 |
| `tr` | Nume | Furnizor | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ |
| `tr` | Furnizor | Scop | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ |
| `tr` | Scop | Durată | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ |
| `tr` | Durată | Tip | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ | -47.39 ¹ |
| `tr` | [valoare de completat: [NUME-COOKIE]] | ioana-balan.ro | -50.59 ¹ | -50.59 ¹ | -50.59 ¹ | -50.60 ¹ |
| `tr` | ioana-balan.ro | [valoare de completat: [SCOP]] | -50.59 ¹ | -50.59 ¹ | -50.59 ¹ | -50.60 ¹ |
| `tr` | [valoare de completat: [SCOP]] | [valoare de completat: [DURATĂ]] | -50.59 ¹ | -50.59 ¹ | -50.59 ¹ | -50.60 ¹ |
| `tr` | [valoare de completat: [DURATĂ]] | HTTP | -50.59 ¹ | -50.59 ¹ | -50.59 ¹ | -50.60 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S10 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S11 — 4. Conținut încorporat de la terți (#sectiunea-4)

`section#sectiunea-4` · clase: `mb-12 md:mb-16`

Titlu: «4. Conținut încorporat de la terți»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 697.88 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 697.88 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 697.88 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 891.44 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 236.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 220.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 220.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 220.19 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 207.23 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`code`) | 1440 | 200.16 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 1024 | 200.16 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 768 | 200.16 | 23 | 2/6/2/6 | #20201f | none |
| └ coloana 2 (`code`) | 390 | 189.23 | 21 | 2/6/2/6 | #20201f | none |
| └ coloana 3 (`strong`) | 1440 | 551.09 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`strong`) | 1024 | 551.09 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`strong`) | 768 | 551.09 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`strong`) | 390 | 328.11 | 79.19 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 1440 | 284.30 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 1024 | 284.30 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 768 | 284.30 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 390 | 267.56 | 20 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 210.39 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 210.39 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 210.39 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 198.02 | 20 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 221.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 221.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 221.52 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 208.48 | 20 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4. Conținut încorporat de la terți | h2 | 1440 | 432 | 3631.48 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Conținut încorporat de la terți | h2 | 1024 | 224 | 3631.48 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Conținut încorporat de la terți | h2 | 768 | 96 | 3631.48 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Conținut încorporat de la terți | h2 | 390 | 24 | 3837.27 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Anumite pagini pot include conținut găzduit de t | p | 1440 | 432 | 3691.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Anumite pagini pot include conținut găzduit de t | p | 1024 | 224 | 3691.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Anumite pagini pot include conținut găzduit de t | p | 768 | 96 | 3691.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Anumite pagini pot include conținut găzduit de t | p | 390 | 24 | 3887.27 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Playerele video sunt încărcate în modul cu confi | p | 1440 | 432 | 3772.36 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Playerele video sunt încărcate în modul cu confi | p | 1024 | 224 | 3772.36 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Playerele video sunt încărcate în modul cu confi | p | 768 | 96 | 3772.36 | 576 | 157.19 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Playerele video sunt încărcate în modul cu confi | p | 390 | 24 | 3964.45 | 342 | 236.75 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Materiale video (YouTube). | strong | 1440 | 432 | 3777.36 | 220.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Materiale video (YouTube). | strong | 1024 | 224 | 3777.36 | 220.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Materiale video (YouTube). | strong | 768 | 96 | 3777.36 | 220.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Materiale video (YouTube). | strong | 390 | 24 | 3968.45 | 207.23 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| youtube-nocookie.com | code | 1440 | 633.83 | 3807.80 | 200.16 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| youtube-nocookie.com | code | 1024 | 425.83 | 3807.80 | 200.16 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| youtube-nocookie.com | code | 768 | 297.83 | 3807.80 | 200.16 | 23 | 15.64 | 28.93 | normal | 400 | #e5e2e1 | start |
| youtube-nocookie.com | code | 390 | 88.34 | 4027.64 | 189.23 | 21 | 14.72 | 27.23 | normal | 400 | #e5e2e1 | start |
| numai după ce dați clic pe imaginea de previzual | strong | 1440 | 432 | 3808.80 | 551.09 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce dați clic pe imaginea de previzual | strong | 1024 | 224 | 3808.80 | 551.09 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce dați clic pe imaginea de previzual | strong | 768 | 96 | 3808.80 | 551.09 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după ce dați clic pe imaginea de previzual | strong | 390 | 24 | 4027.64 | 328.11 | 79.19 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Din momentul în care porniți redarea, se aplică  | p | 1440 | 432 | 3947.55 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Din momentul în care porniți redarea, se aplică  | p | 1024 | 224 | 3947.55 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Din momentul în care porniți redarea, se aplică  | p | 768 | 96 | 3947.55 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Din momentul în care porniți redarea, se aplică  | p | 390 | 24 | 4219.20 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| https://policies.google.com/privacy | a | 1440 | 432 | 4015.42 | 284.30 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://policies.google.com/privacy | a | 1024 | 224 | 4015.42 | 284.30 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://policies.google.com/privacy | a | 768 | 96 | 4015.42 | 284.30 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://policies.google.com/privacy | a | 390 | 24 | 4311.98 | 267.56 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Fonturile utilizate pe site sunt găzduite pe ser | p | 1440 | 432 | 4059.86 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fonturile utilizate pe site sunt găzduite pe ser | p | 1024 | 224 | 4059.86 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fonturile utilizate pe site sunt găzduite pe ser | p | 768 | 96 | 4059.86 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fonturile utilizate pe site sunt găzduite pe ser | p | 390 | 24 | 4355.58 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Fonturi și resurse grafice. | strong | 1440 | 432 | 4064.86 | 210.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Fonturi și resurse grafice. | strong | 1024 | 224 | 4064.86 | 210.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Fonturi și resurse grafice. | strong | 768 | 96 | 4064.86 | 210.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Fonturi și resurse grafice. | strong | 390 | 24 | 4359.58 | 198.02 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Linkurile către Facebook, Instagram, YouTube, Ti | p | 1440 | 432 | 4203.61 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Linkurile către Facebook, Instagram, YouTube, Ti | p | 1024 | 224 | 4203.61 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Linkurile către Facebook, Instagram, YouTube, Ti | p | 768 | 96 | 4203.61 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Linkurile către Facebook, Instagram, YouTube, Ti | p | 390 | 24 | 4551.14 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Linkuri către rețele sociale. | strong | 1440 | 432 | 4208.61 | 221.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Linkuri către rețele sociale. | strong | 1024 | 224 | 4208.61 | 221.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Linkuri către rețele sociale. | strong | 768 | 96 | 4208.61 | 221.52 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Linkuri către rețele sociale. | strong | 390 | 24 | 4555.14 | 208.48 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-4` | 4. Conținut încorporat de la terți | Anumite pagini pot include conținut găzduit de t | 20 | 20 | 20 | 20 |
| `section#sectiunea-4` | Anumite pagini pot include conținut găzduit de t | Playerele video sunt încărcate în modul cu confi | 18 | 18 | 18 | 18 |
| `section#sectiunea-4` | Playerele video sunt încărcate în modul cu confi | Din momentul în care porniți redarea, se aplică  | 18 | 18 | 18 | 18 |
| `section#sectiunea-4` | Din momentul în care porniți redarea, se aplică  | Fonturile utilizate pe site sunt găzduite pe ser | 18 | 18 | 18 | 18 |
| `section#sectiunea-4` | Fonturile utilizate pe site sunt găzduite pe ser | Linkurile către Facebook, Instagram, YouTube, Ti | 18 | 18 | 18 | 18 |
| `p` | Materiale video (YouTube). | youtube-nocookie.com | 10.44 | 10.44 | 10.44 | 39.19 |
| `p` | youtube-nocookie.com | numai după ce dați clic pe imaginea de previzual | -22 | -22 | -22 | -21 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S12 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S13 — 5. Cum vă puteți retrage consimțământul (#sectiunea-5)

`section#sectiunea-5` · clase: `mb-12 md:mb-16`

Titlu: «5. Cum vă puteți retrage consimțământul»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 203.75 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 203.75 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 203.75 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 245.97 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5. Cum vă puteți retrage consimțământul | h2 | 1440 | 432 | 4481.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Cum vă puteți retrage consimțământul | h2 | 1024 | 224 | 4481.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Cum vă puteți retrage consimțământul | h2 | 768 | 96 | 4481.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Cum vă puteți retrage consimțământul | h2 | 390 | 24 | 4848.70 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Dacă v-ați exprimat consimțământul pentru cookie | p | 1440 | 432 | 4541.36 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă v-ați exprimat consimțământul pentru cookie | p | 1024 | 224 | 4541.36 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă v-ați exprimat consimțământul pentru cookie | p | 768 | 96 | 4541.36 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă v-ați exprimat consimțământul pentru cookie | p | 390 | 24 | 4928.70 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Retragerea consimțământului nu afectează legalit | p | 1440 | 432 | 4622.23 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Retragerea consimțământului nu afectează legalit | p | 1024 | 224 | 4622.23 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Retragerea consimțământului nu afectează legalit | p | 768 | 96 | 4622.23 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Retragerea consimțământului nu afectează legalit | p | 390 | 24 | 5035.48 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-5` | 5. Cum vă puteți retrage consimțământul | Dacă v-ați exprimat consimțământul pentru cookie | 20 | 20 | 20 | 20 |
| `section#sectiunea-5` | Dacă v-ați exprimat consimțământul pentru cookie | Retragerea consimțământului nu afectează legalit | 18 | 18 | 18 | 18 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S14 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S15 — 6. Cum puteți controla cookie-urile din browser (#sectiunea-6)

`section#sectiunea-6` · clase: `mb-12 md:mb-16`

Titlu: «6. Cum puteți controla cookie-urile din browser»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 553.25 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 553.25 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 553.25 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 807.06 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 80 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 80 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 80 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1440 | 576 | 260.06 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1024 | 576 | 260.06 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 768 | 576 | 260.06 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 390 | 342 | 454.31 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| **container 4** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6. Cum puteți controla cookie-urile din browser | h2 | 1440 | 432 | 4837.11 | 576 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Cum puteți controla cookie-urile din browser | h2 | 1024 | 224 | 4837.11 | 576 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Cum puteți controla cookie-urile din browser | h2 | 768 | 96 | 4837.11 | 576 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Cum puteți controla cookie-urile din browser | h2 | 390 | 24 | 5214.67 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Orice browser modern vă permite să blocați sau s | p | 1440 | 432 | 4937.11 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice browser modern vă permite să blocați sau s | p | 1024 | 224 | 4937.11 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice browser modern vă permite să blocați sau s | p | 768 | 96 | 4937.11 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice browser modern vă permite să blocați sau s | p | 390 | 24 | 5294.67 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Google Chrome: | strong | 1440 | 458 | 5054.42 | 133.30 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Google Chrome: | strong | 1024 | 250 | 5054.42 | 133.30 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Google Chrome: | strong | 768 | 122 | 5054.42 | 133.30 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Google Chrome: | strong | 390 | 50 | 5464.64 | 125.45 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://support.google.com/chrome/answer/95647 | a | 1440 | 596.08 | 5054.42 | 408.77 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.google.com/chrome/answer/95647 | a | 1024 | 388.08 | 5054.42 | 408.77 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.google.com/chrome/answer/95647 | a | 768 | 260.08 | 5054.42 | 408.77 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.google.com/chrome/answer/95647 | a | 390 | 50 | 5494.23 | 315.70 | 49.59 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Mozilla Firefox: | strong | 1440 | 458 | 5095.86 | 124.91 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Mozilla Firefox: | strong | 1024 | 250 | 5095.86 | 124.91 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Mozilla Firefox: | strong | 768 | 122 | 5095.86 | 124.91 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Mozilla Firefox: | strong | 390 | 50 | 5563.42 | 117.55 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://support.mozilla.org/ro/kb/protectie-avan | a | 1440 | 458 | 5095.86 | 475.89 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.mozilla.org/ro/kb/protectie-avan | a | 1024 | 250 | 5095.86 | 475.89 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.mozilla.org/ro/kb/protectie-avan | a | 768 | 122 | 5095.86 | 475.89 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.mozilla.org/ro/kb/protectie-avan | a | 390 | 50 | 5593.02 | 309.16 | 49.59 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Microsoft Edge: | strong | 1440 | 458 | 5168.73 | 129.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Microsoft Edge: | strong | 1024 | 250 | 5168.73 | 129.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Microsoft Edge: | strong | 768 | 122 | 5168.73 | 129.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Microsoft Edge: | strong | 390 | 50 | 5662.20 | 122.08 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://support.microsoft.com/ro-ro/microsoft-ed | a | 1440 | 458 | 5168.73 | 510.19 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.microsoft.com/ro-ro/microsoft-ed | a | 1024 | 250 | 5168.73 | 510.19 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.microsoft.com/ro-ro/microsoft-ed | a | 768 | 122 | 5168.73 | 510.19 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.microsoft.com/ro-ro/microsoft-ed | a | 390 | 50 | 5691.80 | 254.39 | 49.59 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Safari: | strong | 1440 | 458 | 5241.61 | 53.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Safari: | strong | 1024 | 250 | 5241.61 | 53.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Safari: | strong | 768 | 122 | 5241.61 | 53.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Safari: | strong | 390 | 50 | 5760.98 | 50.45 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://support.apple.com/ro-ro/guide/safari/sfr | a | 1440 | 516.39 | 5241.61 | 471.17 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.apple.com/ro-ro/guide/safari/sfr | a | 1024 | 308.39 | 5241.61 | 471.17 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.apple.com/ro-ro/guide/safari/sfr | a | 768 | 180.39 | 5241.61 | 471.17 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://support.apple.com/ro-ro/guide/safari/sfr | a | 390 | 50 | 5760.98 | 280.09 | 49.59 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Opera: | strong | 1440 | 458 | 5283.05 | 55.50 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Opera: | strong | 1024 | 250 | 5283.05 | 55.50 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Opera: | strong | 768 | 122 | 5283.05 | 55.50 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Opera: | strong | 390 | 50 | 5830.17 | 52.23 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://help.opera.com/en/latest/web-preferences | a | 1440 | 518.28 | 5283.05 | 409.78 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://help.opera.com/en/latest/web-preferences | a | 1024 | 310.28 | 5283.05 | 409.78 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://help.opera.com/en/latest/web-preferences | a | 768 | 182.28 | 5283.05 | 409.78 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://help.opera.com/en/latest/web-preferences | a | 390 | 50 | 5859.77 | 288.78 | 49.59 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Blocarea completă a cookie-urilor poate afecta f | p | 1440 | 432 | 5327.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Blocarea completă a cookie-urilor poate afecta f | p | 1024 | 224 | 5327.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Blocarea completă a cookie-urilor poate afecta f | p | 768 | 96 | 5327.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Blocarea completă a cookie-urilor poate afecta f | p | 390 | 24 | 5932.95 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-6` | 6. Cum puteți controla cookie-urile din browser | Orice browser modern vă permite să blocați sau s | 20 | 20 | 20 | 20 |
| `section#sectiunea-6` | Orice browser modern vă permite să blocați sau s | [Google Chrome: https://support.google.co] | 18 | 18 | 18 | 18 |
| `section#sectiunea-6` | [Google Chrome: https://support.google.co] | Blocarea completă a cookie-urilor poate afecta f | 18 | 18 | 18 | 18 |
| `ul.motif-list` | [Google Chrome: https://support.google.co] | [Mozilla Firefox: https://support.mozilla] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Mozilla Firefox: https://support.mozilla] | [Microsoft Edge: https://support.microsof] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Microsoft Edge: https://support.microsof] | [Safari: https://support.apple.com/ro-ro/] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Safari: https://support.apple.com/ro-ro/] | [Opera: https://help.opera.com/en/latest/] | 10 | 10 | 10 | 10 |
| `li` | Google Chrome: | https://support.google.com/chrome/answer/95647 | -20 ¹ | -20 ¹ | -20 ¹ | 9.59 |
| `li` | Mozilla Firefox: | https://support.mozilla.org/ro/kb/protectie-avan | -20 | -20 | -20 | 9.60 |
| `li` | Microsoft Edge: | https://support.microsoft.com/ro-ro/microsoft-ed | -20 | -20 | -20 | 9.60 |
| `li` | Safari: | https://support.apple.com/ro-ro/guide/safari/sfr | -20 ¹ | -20 ¹ | -20 ¹ | -20 |
| `li` | Opera: | https://help.opera.com/en/latest/web-preferences | -20 ¹ | -20 ¹ | -20 ¹ | 9.60 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S16 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S17 — 7. Drepturile dumneavoastră (#sectiunea-7)

`section#sectiunea-7` · clase: `mb-12 md:mb-16`

Titlu: «7. Drepturile dumneavoastră»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 378.94 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 378.94 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 378.94 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 470.72 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 1440 | 568.67 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 1024 | 568.67 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 768 | 568.67 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 390 | 137.52 | 20 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 458.38 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 458.38 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 458.38 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 330.36 | 79.19 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 1440 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 1024 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 768 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 390 | 226.92 | 20 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7. Drepturile dumneavoastră | h2 | 1440 | 432 | 5542.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Drepturile dumneavoastră | h2 | 1024 | 224 | 5542.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Drepturile dumneavoastră | h2 | 768 | 96 | 5542.36 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Drepturile dumneavoastră | h2 | 390 | 24 | 6141.73 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Atunci când prin cookie-uri se prelucrează date  | p | 1440 | 432 | 5602.36 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Atunci când prin cookie-uri se prelucrează date  | p | 1024 | 224 | 5602.36 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Atunci când prin cookie-uri se prelucrează date  | p | 768 | 96 | 5602.36 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Atunci când prin cookie-uri se prelucrează date  | p | 390 | 24 | 6191.73 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Aceste drepturi și modalitatea de exercitare sun | p | 1440 | 432 | 5746.11 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste drepturi și modalitatea de exercitare sun | p | 1024 | 224 | 5746.11 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste drepturi și modalitatea de exercitare sun | p | 768 | 96 | 5746.11 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste drepturi și modalitatea de exercitare sun | p | 390 | 24 | 6387.30 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Termeni și condiții | a | 1440 | 432 | 5751.11 | 568.67 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Termeni și condiții | a | 1024 | 224 | 5751.11 | 568.67 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Termeni și condiții | a | 768 | 96 | 5751.11 | 568.67 | 51.44 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Termeni și condiții | a | 390 | 147.98 | 6420.89 | 137.52 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Vă puteți adresa în orice moment , . | p | 1440 | 432 | 5826.98 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Vă puteți adresa în orice moment , . | p | 1024 | 224 | 5826.98 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Vă puteți adresa în orice moment , . | p | 768 | 96 | 5826.98 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Vă puteți adresa în orice moment , . | p | 390 | 24 | 6494.08 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Autorității Naționale de Supraveghere a Prelucră | strong | 1440 | 432 | 5831.98 | 458.38 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale de Supraveghere a Prelucră | strong | 1024 | 224 | 5831.98 | 458.38 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale de Supraveghere a Prelucră | strong | 768 | 96 | 5831.98 | 458.38 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale de Supraveghere a Prelucră | strong | 390 | 24 | 6498.08 | 330.36 | 79.19 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 1440 | 432 | 5894.86 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 1024 | 224 | 5894.86 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 768 | 96 | 5894.86 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 390 | 24 | 6586.86 | 226.92 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-7` | 7. Drepturile dumneavoastră | Atunci când prin cookie-uri se prelucrează date  | 20 | 20 | 20 | 20 |
| `section#sectiunea-7` | Atunci când prin cookie-uri se prelucrează date  | Aceste drepturi și modalitatea de exercitare sun | 18 | 18 | 18 | 18 |
| `section#sectiunea-7` | Aceste drepturi și modalitatea de exercitare sun | Vă puteți adresa în orice moment , . | 18 | 18 | 18 | 18 |
| `p` | Autorității Naționale de Supraveghere a Prelucră | https://www.dataprotection.ro | 11.44 | 11.44 | 11.44 | 9.59 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S18 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S19 — 8. Modificarea acestei politici (#sectiunea-8)

`section#sectiunea-8` · clase: `mb-12 md:mb-16`

Titlu: «8. Modificarea acestei politici»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 154.31 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 154.31 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 154.31 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 197.97 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8. Modificarea acestei politici | h2 | 1440 | 432 | 6073.30 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Modificarea acestei politici | h2 | 1024 | 224 | 6073.30 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Modificarea acestei politici | h2 | 768 | 96 | 6073.30 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Modificarea acestei politici | h2 | 390 | 24 | 6732.45 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Actualizăm această politică ori de câte ori se m | p | 1440 | 432 | 6133.30 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Actualizăm această politică ori de câte ori se m | p | 1024 | 224 | 6133.30 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Actualizăm această politică ori de câte ori se m | p | 768 | 96 | 6133.30 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Actualizăm această politică ori de câte ori se m | p | 390 | 24 | 6782.45 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-8` | 8. Modificarea acestei politici | Actualizăm această politică ori de câte ori se m | 20 | 20 | 20 | 20 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S20 — div.motif-separator

`div` · clase: `motif-separator w-full mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 1024 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 768 | 576 | 24 | 0/0/0/0 |  +bg-image | none |
| **section** | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## S21 — 9. Contact (#sectiunea-9)

`section#sectiunea-9` · clase: `—`

Eyebrow: «[EMAIL-OFICIAL]»

Titlu: «9. Contact»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 122.88 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 122.88 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 122.88 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 138.78 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.legal-tbc`) | 1440 | 155 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 1024 | 155 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 768 | 155 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 1 (`span.legal-tbc`) | 390 | 146.83 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9. Contact | h2 | 1440 | 432 | 6379.61 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Contact | h2 | 1024 | 224 | 6379.61 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Contact | h2 | 768 | 96 | 6379.61 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Contact | h2 | 390 | 24 | 7050.42 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Pentru orice întrebare privind utilizarea cookie | p | 1440 | 432 | 6439.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind utilizarea cookie | p | 1024 | 224 | 6439.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind utilizarea cookie | p | 768 | 96 | 6439.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind utilizarea cookie | p | 390 | 24 | 7100.42 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| [EMAIL-OFICIAL] | span | 1440 | 544.73 | 6473.05 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 1024 | 336.73 | 6473.05 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 768 | 208.73 | 6473.05 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 390 | 24 | 7160.61 | 146.83 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 551.73 | 6470.05 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 343.73 | 6470.05 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 215.73 | 6470.05 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 31 | 7158.61 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-9` | 9. Contact | Pentru orice întrebare privind utilizarea cookie | 20 | 20 | 20 | 20 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Politica de cookie-uri» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[30px]`; weight rezolvat 400/500, font-size masurat 30/48px
- `h2` «1. Ce sunt cookie-urile» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «2. Temeiul legal» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «3. Ce cookie-uri folosim» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «3.1 Cookie-uri strict necesare» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `p` «Glisați lateral pentru a vedea tot tabelul.» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[14px]`; weight rezolvat 400, font-size masurat 16px
- `h3` «3.2 Cookie-uri de analiză» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «3.3 Cookie-uri de publicitate» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h2` «4. Conținut încorporat de la terți» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «5. Cum vă puteți retrage consimțământul» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «6. Cum puteți controla cookie-urile din browser» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «7. Drepturile dumneavoastră» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «8. Modificarea acestei politici» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «9. Contact» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px

### Borduri care vin din `assets/styles.css`, nu din clase

- `aside.legal-draft-banner` «[Document în lucru — nu este în vigoare T]» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[EXEMPLU]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[DATA-PUBLICARE]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `details#cuprins` «[Cuprins 1. Ce sunt cookie-urile 2. Temei]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Nume» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Furnizor» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Scop» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Durată» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Tip» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «[valoare de completat: [NUME-COOKIE]]» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[NUME-COOKIE]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «ioana-balan.ro» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «[valoare de completat: [SCOP]]» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[SCOP]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «[valoare de completat: [DURATĂ]]» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[DURATĂ]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «HTTP» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `blockquote.legal-note` «[De completat după finalizarea site-ului.]» — L 3px #800020, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `blockquote.legal-note` «[Dacă se activează ulterior un serviciu d]» — L 3px #800020, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[EMAIL-OFICIAL]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «3. Ce cookie-uri folosim» declara `mb-*` ∈ {20}px, dar distanta reala pana la «3.1 Cookie-uri strict necesare» e 40px la 1440
- «3. Ce cookie-uri folosim» declara `mb-*` ∈ {20}px, dar distanta reala pana la «3.1 Cookie-uri strict necesare» e 40px la 1024
- «3. Ce cookie-uri folosim» declara `mb-*` ∈ {20}px, dar distanta reala pana la «3.1 Cookie-uri strict necesare» e 40px la 768
- «3. Ce cookie-uri folosim» declara `mb-*` ∈ {20}px, dar distanta reala pana la «3.1 Cookie-uri strict necesare» e 40px la 390

### Elemente care nu se randeaza la un viewport

- `p.md:hidden` «Glisați lateral pentru a vedea tot tabelul.» — `getClientRects().length == 0` la 1440, 1024, 768 (randat la 390); `display` raportat: none

### Suprapuneri intre elemente

- in `p`: «youtube-nocookie.com» si «numai după ce dați clic pe imaginea de previzual» se suprapun pe verticala cu 22px la 1440 (suprapunere orizontala 200.15px, position static/static) — **ambele in flux normal**
- in `p`: «youtube-nocookie.com» si «numai după ce dați clic pe imaginea de previzual» se suprapun pe verticala cu 22px la 1024 (suprapunere orizontala 200.15px, position static/static) — **ambele in flux normal**
- in `p`: «youtube-nocookie.com» si «numai după ce dați clic pe imaginea de previzual» se suprapun pe verticala cu 22px la 768 (suprapunere orizontala 200.15px, position static/static) — **ambele in flux normal**
- in `p`: «numai după ce dați clic pe imaginea de previzual» si «youtube-nocookie.com» se suprapun pe verticala cu 79.19px la 390 (suprapunere orizontala 189.24px, position static/static) — **ambele in flux normal**
- in `li`: «Mozilla Firefox:» si «https://support.mozilla.org/ro/kb/protectie-avan» se suprapun pe verticala cu 20px la 1440 (suprapunere orizontala 124.91px, position static/static) — **ambele in flux normal**
- in `li`: «Mozilla Firefox:» si «https://support.mozilla.org/ro/kb/protectie-avan» se suprapun pe verticala cu 20px la 1024 (suprapunere orizontala 124.91px, position static/static) — **ambele in flux normal**
- in `li`: «Mozilla Firefox:» si «https://support.mozilla.org/ro/kb/protectie-avan» se suprapun pe verticala cu 20px la 768 (suprapunere orizontala 124.91px, position static/static) — **ambele in flux normal**
- in `li`: «Microsoft Edge:» si «https://support.microsoft.com/ro-ro/microsoft-ed» se suprapun pe verticala cu 20px la 1440 (suprapunere orizontala 129.72px, position static/static) — **ambele in flux normal**
- in `li`: «Microsoft Edge:» si «https://support.microsoft.com/ro-ro/microsoft-ed» se suprapun pe verticala cu 20px la 1024 (suprapunere orizontala 129.72px, position static/static) — **ambele in flux normal**
- in `li`: «Microsoft Edge:» si «https://support.microsoft.com/ro-ro/microsoft-ed» se suprapun pe verticala cu 20px la 768 (suprapunere orizontala 129.72px, position static/static) — **ambele in flux normal**
- in `li`: «Safari:» si «https://support.apple.com/ro-ro/guide/safari/sfr» se suprapun pe verticala cu 20px la 390 (suprapunere orizontala 50.45px, position static/static) — **ambele in flux normal**


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| [EXEMPLU] | 1440: 528 · 1024: 528 · 768: 528 · 390: 294 | vert (sectiune): 20 sus / 20 jos<br>oriz (container): 24 L / 24 R | — | — | o singura coloana |
| Politica de cookie-uri | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| cuprins | 1440: 528 · 1024: 528 · 768: 528 · 390: 302 | vert (sectiune): 1440: 24 sus / 24 jos · 1024: 24 sus / 24 jos · 768: 24 sus / 24 jos · 390: 20 sus / 20 jos<br>oriz (container): 1440: 24 L / 24 R · 1024: 24 L / 24 R · 768: 24 L / 24 R · 390: 20 L / 20 R | — | — | o singura coloana |
| 1. Ce sunt cookie-urile (#sectiunea-1) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 2. Temeiul legal (#sectiunea-2) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 3. Ce cookie-uri folosim (#sectiunea-3) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 4. Conținut încorporat de la terți (#sectiunea-4) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 5. Cum vă puteți retrage consimțământul (#sectiunea-5) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 6. Cum puteți controla cookie-urile din browser (#sectiunea-6) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 7. Drepturile dumneavoastră (#sectiunea-7) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 8. Modificarea acestei politici (#sectiunea-8) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 9. Contact (#sectiunea-9) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
