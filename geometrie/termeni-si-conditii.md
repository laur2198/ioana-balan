# Geometrie randata — `termeni-si-conditii.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/termeni-si-conditii.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 12068.36 | 128/0/96/0 | transparent | none |
| `<main>` | 1024 | 1024 | 12068.36 | 128/0/96/0 | transparent | none |
| `<main>` | 768 | 768 | 12141.94 | 128/0/96/0 | transparent | none |
| `<main>` | 390 | 390 | 12836.09 | 96/0/64/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 12499px, 1024 → 12499px, 768 → 12619px, 390 → 13423px.

Sectiuni masurate: **37**.

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

## S2 — Termeni și condiții

`header` · clase: `mb-8 md:mb-10`

Eyebrow: «Document legal»

Titlu: «Termeni și condiții»

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
| Termeni și condiții | h1 | 1440 | 432 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Termeni și condiții | h1 | 1024 | 224 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Termeni și condiții | h1 | 768 | 96 | 394 | 576 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Termeni și condiții | h1 | 390 | 24 | 444 | 342 | 37.50 | 30 | 37.50 | normal | 400 | #e5e2e1 | start |
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
| `header.mb-8` | Document legal | Termeni și condiții | 12 | 12 | 12 | 12 |
| `header.mb-8` | Termeni și condiții | [Ultima actualizare: valoare de completat] | 16 | 16 | 16 | 16 |
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
| **section** | 1440 | 576 | 771 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 1024 | 576 | 771 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 768 | 576 | 771 | 24/24/24/24 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **section** | 390 | 342 | 86 | 20/20/20/20 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **container 1** (`summary.flex`) | 1440 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 1024 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 768 | 526 | 44 | 0/0/0/0 | transparent | none |
| **container 1** (`summary.flex`) | 390 | 300 | 44 | 0/0/0/0 | transparent | none |
| **container 2** (`nav.mt-4`) | 1440 | 526 | 661 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 1024 | 526 | 661 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 768 | 526 | 661 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| **container 2** (`nav.mt-4`) | 390 | 300 | 709 | 20/0/0/0 | transparent | T 1px #444748 @0.3 |
| └ coloana 1 (`ol.flex`) | 1440 | 526 | 640 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 1024 | 526 | 640 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 768 | 526 | 640 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`ol.flex`) | 390 | 300 | 688 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cuprins | summary | 1440 | 457 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 1024 | 249 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 768 | 121 | 627 | 526 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| Cuprins | summary | 390 | 45 | 638.50 | 300 | 44 | 14 | 20 | 2.10 | 600 | #e5e2e1 | start |
| 1. Identificarea operatorului | a | 1440 | 457 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Identificarea operatorului | a | 1024 | 249 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Identificarea operatorului | a | 768 | 121 | 708 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 1. Identificarea operatorului | a | 390 | 45 | 719.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Obiectul site-ului | a | 1440 | 457 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Obiectul site-ului | a | 1024 | 249 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Obiectul site-ului | a | 768 | 121 | 748 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 2. Obiectul site-ului | a | 390 | 45 | 759.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Acceptarea termenilor | a | 1440 | 457 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Acceptarea termenilor | a | 1024 | 249 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Acceptarea termenilor | a | 768 | 121 | 788 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 3. Acceptarea termenilor | a | 390 | 45 | 799.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Informațiile publicate. Prețuri | a | 1440 | 457 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Informațiile publicate. Prețuri | a | 1024 | 249 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Informațiile publicate. Prețuri | a | 768 | 121 | 828 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 4. Informațiile publicate. Prețuri | a | 390 | 45 | 839.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Rezervarea și încheierea contractului | a | 1440 | 457 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Rezervarea și încheierea contractului | a | 1024 | 249 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Rezervarea și încheierea contractului | a | 768 | 121 | 868 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 5. Rezervarea și încheierea contractului | a | 390 | 45 | 879.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Deplasarea | a | 1440 | 457 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Deplasarea | a | 1024 | 249 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Deplasarea | a | 768 | 121 | 908 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 6. Deplasarea | a | 390 | 45 | 919.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Modificarea și anularea rezervării | a | 1440 | 457 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Modificarea și anularea rezervării | a | 1024 | 249 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Modificarea și anularea rezervării | a | 768 | 121 | 948 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 7. Modificarea și anularea rezervării | a | 390 | 45 | 959.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Drepturi de proprietate intelectuală | a | 1440 | 457 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Drepturi de proprietate intelectuală | a | 1024 | 249 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Drepturi de proprietate intelectuală | a | 768 | 121 | 988 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 8. Drepturi de proprietate intelectuală | a | 390 | 45 | 999.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Materiale audio-video de la evenimente | a | 1440 | 457 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Materiale audio-video de la evenimente | a | 1024 | 249 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Materiale audio-video de la evenimente | a | 768 | 121 | 1028 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 9. Materiale audio-video de la evenimente | a | 390 | 45 | 1039.50 | 300 | 64 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 10. Limitarea răspunderii | a | 1440 | 457 | 1068 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 10. Limitarea răspunderii | a | 1024 | 249 | 1068 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 10. Limitarea răspunderii | a | 768 | 121 | 1068 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 10. Limitarea răspunderii | a | 390 | 45 | 1103.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 11. Linkuri către site-uri terțe | a | 1440 | 457 | 1108 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 11. Linkuri către site-uri terțe | a | 1024 | 249 | 1108 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 11. Linkuri către site-uri terțe | a | 768 | 121 | 1108 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 11. Linkuri către site-uri terțe | a | 390 | 45 | 1143.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 12. Prelucrarea datelor cu caracter personal | a | 1440 | 457 | 1148 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 12. Prelucrarea datelor cu caracter personal | a | 1024 | 249 | 1148 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 12. Prelucrarea datelor cu caracter personal | a | 768 | 121 | 1148 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 12. Prelucrarea datelor cu caracter personal | a | 390 | 45 | 1183.50 | 300 | 64 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 13. Cookie-uri | a | 1440 | 457 | 1188 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 13. Cookie-uri | a | 1024 | 249 | 1188 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 13. Cookie-uri | a | 768 | 121 | 1188 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 13. Cookie-uri | a | 390 | 45 | 1247.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 14. Soluționarea litigiilor | a | 1440 | 457 | 1228 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 14. Soluționarea litigiilor | a | 1024 | 249 | 1228 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 14. Soluționarea litigiilor | a | 768 | 121 | 1228 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 14. Soluționarea litigiilor | a | 390 | 45 | 1287.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 15. Modificarea termenilor | a | 1440 | 457 | 1268 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 15. Modificarea termenilor | a | 1024 | 249 | 1268 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 15. Modificarea termenilor | a | 768 | 121 | 1268 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 15. Modificarea termenilor | a | 390 | 45 | 1327.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 16. Contact | a | 1440 | 457 | 1308 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 16. Contact | a | 1024 | 249 | 1308 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 16. Contact | a | 768 | 121 | 1308 | 526 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| 16. Contact | a | 390 | 45 | 1367.50 | 300 | 40 | 16 | 24 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `details#cuprins` | Cuprins | [1. Identificarea operatorului 2. Obiectu] | 16 | 16 | 16 | 16 |
| `ol.flex` | [1. Identificarea operatorului] | [2. Obiectul site-ului] | 0 | 0 | 0 | 0 |
| `ol.flex` | [2. Obiectul site-ului] | [3. Acceptarea termenilor] | 0 | 0 | 0 | 0 |
| `ol.flex` | [3. Acceptarea termenilor] | [4. Informațiile publicate. Prețuri] | 0 | 0 | 0 | 0 |
| `ol.flex` | [4. Informațiile publicate. Prețuri] | [5. Rezervarea și încheierea contractului] | 0 | 0 | 0 | 0 |
| `ol.flex` | [5. Rezervarea și încheierea contractului] | [6. Deplasarea] | 0 | 0 | 0 | 0 |
| `ol.flex` | [6. Deplasarea] | [7. Modificarea și anularea rezervării] | 0 | 0 | 0 | 0 |
| `ol.flex` | [7. Modificarea și anularea rezervării] | [8. Drepturi de proprietate intelectuală] | 0 | 0 | 0 | 0 |
| `ol.flex` | [8. Drepturi de proprietate intelectuală] | [9. Materiale audio-video de la eveniment] | 0 | 0 | 0 | 0 |
| `ol.flex` | [9. Materiale audio-video de la eveniment] | [10. Limitarea răspunderii] | 0 | 0 | 0 | 0 |
| `ol.flex` | [10. Limitarea răspunderii] | [11. Linkuri către site-uri terțe] | 0 | 0 | 0 | 0 |
| `ol.flex` | [11. Linkuri către site-uri terțe] | [12. Prelucrarea datelor cu caracter pers] | 0 | 0 | 0 | 0 |
| `ol.flex` | [12. Prelucrarea datelor cu caracter pers] | [13. Cookie-uri] | 0 | 0 | 0 | 0 |
| `ol.flex` | [13. Cookie-uri] | [14. Soluționarea litigiilor] | 0 | 0 | 0 | 0 |
| `ol.flex` | [14. Soluționarea litigiilor] | [15. Modificarea termenilor] | 0 | 0 | 0 | 0 |
| `ol.flex` | [15. Modificarea termenilor] | [16. Contact] | 0 | 0 | 0 | 0 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S5 — 1. Identificarea operatorului (#sectiunea-1)

`section#sectiunea-1` · clase: `mb-12 md:mb-16`

Eyebrow: «[DENUMIRE-FIRMĂ-EXACTĂ]»

Titlu: «1. Identificarea operatorului»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 478.38 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 478.38 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 478.38 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 627.50 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 180.66 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 180.66 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 180.66 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 170.02 | 20 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1440 | 576 | 238.63 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 1024 | 576 | 238.63 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 768 | 576 | 238.63 | 0/0/0/0 | transparent | none |
| **container 3** (`ul.motif-list`) | 390 | 342 | 316.34 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| **container 4** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1. Identificarea operatorului | h2 | 1440 | 432 | 1437 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Identificarea operatorului | h2 | 1024 | 224 | 1437 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Identificarea operatorului | h2 | 768 | 96 | 1437 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 1. Identificarea operatorului | h2 | 390 | 24 | 751.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Site-ul este deținut și administrat de: | p | 1440 | 432 | 1497 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este deținut și administrat de: | p | 1024 | 224 | 1497 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este deținut și administrat de: | p | 768 | 96 | 1497 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este deținut și administrat de: | p | 390 | 24 | 801.50 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| https://ioana-balan.ro | strong | 1440 | 489.11 | 1502 | 180.66 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| https://ioana-balan.ro | strong | 1024 | 281.11 | 1502 | 180.66 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| https://ioana-balan.ro | strong | 768 | 153.11 | 1502 | 180.66 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| https://ioana-balan.ro | strong | 390 | 77.75 | 805.50 | 170.02 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Denumire: | strong | 1440 | 458 | 1551.44 | 84.75 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Denumire: | strong | 1024 | 250 | 1551.44 | 84.75 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Denumire: | strong | 768 | 122 | 1551.44 | 84.75 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Denumire: | strong | 390 | 50 | 882.69 | 79.77 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [DENUMIRE-FIRMĂ-EXACTĂ] | span | 1440 | 547.53 | 1548.44 | 258.45 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [DENUMIRE-FIRMĂ-EXACTĂ] | span | 1024 | 339.53 | 1548.44 | 258.45 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [DENUMIRE-FIRMĂ-EXACTĂ] | span | 768 | 211.53 | 1548.44 | 258.45 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [DENUMIRE-FIRMĂ-EXACTĂ] | span | 390 | 50 | 879.69 | 248.28 | 55.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 554.53 | 1545.44 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 346.53 | 1545.44 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 218.53 | 1545.44 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 141.27 | 877.69 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Cod unic de înregistrare: | strong | 1440 | 458 | 1592.88 | 202.06 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Cod unic de înregistrare: | strong | 1024 | 250 | 1592.88 | 202.06 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Cod unic de înregistrare: | strong | 768 | 122 | 1592.88 | 202.06 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Cod unic de înregistrare: | strong | 390 | 50 | 951.88 | 190.17 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [CUI] | span | 1440 | 664.84 | 1589.88 | 58.44 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [CUI] | span | 1024 | 456.84 | 1589.88 | 58.44 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [CUI] | span | 768 | 328.84 | 1589.88 | 58.44 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [CUI] | span | 390 | 244.67 | 948.88 | 55.94 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 671.84 | 1586.88 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 463.84 | 1586.88 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 335.84 | 1586.88 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 251.67 | 946.88 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Număr de ordine în registrul comerțului: | strong | 1440 | 458 | 1634.31 | 326.27 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Număr de ordine în registrul comerțului: | strong | 1024 | 250 | 1634.31 | 326.27 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Număr de ordine în registrul comerțului: | strong | 768 | 122 | 1634.31 | 326.27 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Număr de ordine în registrul comerțului: | strong | 390 | 50 | 991.47 | 307.06 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [NR-REG-COM] | span | 1440 | 789.05 | 1631.31 | 143.89 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [NR-REG-COM] | span | 1024 | 581.05 | 1631.31 | 143.89 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [NR-REG-COM] | span | 768 | 453.05 | 1631.31 | 143.89 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [NR-REG-COM] | span | 390 | 50 | 1018.06 | 136.38 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 796.05 | 1628.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 588.05 | 1628.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 460.05 | 1628.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 57 | 1016.06 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Sediu social: | strong | 1440 | 458 | 1675.75 | 104.55 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Sediu social: | strong | 1024 | 250 | 1675.75 | 104.55 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Sediu social: | strong | 768 | 122 | 1675.75 | 104.55 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Sediu social: | strong | 390 | 50 | 1060.66 | 98.39 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [ADRESĂ-SEDIU-SOCIAL] | span | 1440 | 567.33 | 1672.75 | 228.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [ADRESĂ-SEDIU-SOCIAL] | span | 1024 | 359.33 | 1672.75 | 228.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [ADRESĂ-SEDIU-SOCIAL] | span | 768 | 231.33 | 1672.75 | 228.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [ADRESĂ-SEDIU-SOCIAL] | span | 390 | 50 | 1057.66 | 244.97 | 55.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 574.33 | 1669.75 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 366.33 | 1669.75 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 238.33 | 1669.75 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 159.89 | 1055.66 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| E-mail: | strong | 1440 | 458 | 1717.19 | 57.59 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| E-mail: | strong | 1024 | 250 | 1717.19 | 57.59 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| E-mail: | strong | 768 | 122 | 1717.19 | 57.59 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| E-mail: | strong | 390 | 50 | 1129.84 | 54.20 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 1440 | 520.38 | 1714.19 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 1024 | 312.38 | 1714.19 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 768 | 184.38 | 1714.19 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 390 | 108.70 | 1126.84 | 146.83 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 527.38 | 1711.19 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 319.38 | 1711.19 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 191.38 | 1711.19 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 115.70 | 1124.84 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Telefon: | strong | 1440 | 458 | 1758.63 | 66.83 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Telefon: | strong | 1024 | 250 | 1758.63 | 66.83 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Telefon: | strong | 768 | 122 | 1758.63 | 66.83 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Telefon: | strong | 390 | 50 | 1169.44 | 62.89 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 1440 | 529.61 | 1755.63 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 1024 | 321.61 | 1755.63 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 768 | 193.61 | 1755.63 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 390 | 117.39 | 1166.44 | 100.78 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 536.61 | 1752.63 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 328.61 | 1752.63 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 200.61 | 1752.63 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 124.39 | 1164.44 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Denumit în continuare „Operatorul", „noi" sau „P | p | 1440 | 432 | 1803.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Denumit în continuare „Operatorul", „noi" sau „P | p | 1024 | 224 | 1803.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Denumit în continuare „Operatorul", „noi" sau „P | p | 768 | 96 | 1803.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Denumit în continuare „Operatorul", „noi" sau „P | p | 390 | 24 | 1213.03 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Aceste informații sunt furnizate în conformitate | p | 1440 | 432 | 1852.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste informații sunt furnizate în conformitate | p | 1024 | 224 | 1852.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste informații sunt furnizate în conformitate | p | 768 | 96 | 1852.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aceste informații sunt furnizate în conformitate | p | 390 | 24 | 1290.22 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-1` | 1. Identificarea operatorului | Site-ul este deținut și administrat de: | 20 | 20 | 20 | 20 |
| `section#sectiunea-1` | Site-ul este deținut și administrat de: | [Denumire: valoare de completat: [DENUMIR] | 18 | 18 | 18 | 18 |
| `section#sectiunea-1` | [Denumire: valoare de completat: [DENUMIR] | Denumit în continuare „Operatorul", „noi" sau „P | 18 | 18 | 18 | 18 |
| `section#sectiunea-1` | Denumit în continuare „Operatorul", „noi" sau „P | Aceste informații sunt furnizate în conformitate | 18 | 18 | 18 | 18 |
| `ul.motif-list` | [Denumire: valoare de completat: [DENUMIR] | [Cod unic de înregistrare: valoare de com] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Cod unic de înregistrare: valoare de com] | [Număr de ordine în registrul comerțului:] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Număr de ordine în registrul comerțului:] | [Sediu social: valoare de completat: [ADR] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [Sediu social: valoare de completat: [ADR] | [E-mail: valoare de completat: [EMAIL-OFI] | 10 | 10 | 10 | 10 |
| `ul.motif-list` | [E-mail: valoare de completat: [EMAIL-OFI] | [Telefon: valoare de completat: [TELEFON]] | 10 | 10 | 10 | 10 |
| `li` | Denumire: | [DENUMIRE-FIRMĂ-EXACTĂ] | -23 ¹ | -23 ¹ | -23 ¹ | -23 |
| `li` | Cod unic de înregistrare: | [CUI] | -23 ¹ | -23 ¹ | -23 ¹ | -23 ¹ |
| `li` | Număr de ordine în registrul comerțului: | [NR-REG-COM] | -23 ¹ | -23 ¹ | -23 ¹ | 6.59 |
| `li` | Sediu social: | [ADRESĂ-SEDIU-SOCIAL] | -23 ¹ | -23 ¹ | -23 ¹ | -23 |
| `li` | E-mail: | [EMAIL-OFICIAL] | -23 ¹ | -23 ¹ | -23 ¹ | -23 ¹ |
| `li` | Telefon: | [TELEFON] | -23 ¹ | -23 ¹ | -23 ¹ | -23 ¹ |

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

## S7 — 2. Obiectul site-ului (#sectiunea-2)

`section#sectiunea-2` · clase: `mb-12 md:mb-16`

Titlu: «2. Obiectul site-ului»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 393.53 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2. Obiectul site-ului | h2 | 1440 | 432 | 2067.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Obiectul site-ului | h2 | 1024 | 224 | 2067.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Obiectul site-ului | h2 | 768 | 96 | 2067.38 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 2. Obiectul site-ului | h2 | 390 | 24 | 1499 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Site-ul prezintă activitatea artistică a Ioanei  | p | 1440 | 432 | 2127.38 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul prezintă activitatea artistică a Ioanei  | p | 1024 | 224 | 2127.38 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul prezintă activitatea artistică a Ioanei  | p | 768 | 96 | 2127.38 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul prezintă activitatea artistică a Ioanei  | p | 390 | 24 | 1549 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Site-ul are caracter de prezentare. Nu permite a | p | 1440 | 432 | 2239.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul are caracter de prezentare. Nu permite a | p | 1024 | 224 | 2239.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul are caracter de prezentare. Nu permite a | p | 768 | 96 | 2239.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul are caracter de prezentare. Nu permite a | p | 390 | 24 | 1714.97 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-2` | 2. Obiectul site-ului | Site-ul prezintă activitatea artistică a Ioanei  | 20 | 20 | 20 | 20 |
| `section#sectiunea-2` | Site-ul prezintă activitatea artistică a Ioanei  | Site-ul are caracter de prezentare. Nu permite a | 18 | 18 | 18 | 18 |

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

## S9 — 3. Acceptarea termenilor (#sectiunea-3)

`section#sectiunea-3` · clase: `mb-12 md:mb-16`

Titlu: «3. Acceptarea termenilor»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 298.06 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 393.53 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 207.16 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3. Acceptarea termenilor | h2 | 1440 | 432 | 2517.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Acceptarea termenilor | h2 | 1024 | 224 | 2517.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Acceptarea termenilor | h2 | 768 | 96 | 2517.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 3. Acceptarea termenilor | h2 | 390 | 24 | 2012.53 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Prin accesarea și utilizarea site-ului confirmaț | p | 1440 | 432 | 2577.44 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prin accesarea și utilizarea site-ului confirmaț | p | 1024 | 224 | 2577.44 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prin accesarea și utilizarea site-ului confirmaț | p | 768 | 96 | 2577.44 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prin accesarea și utilizarea site-ului confirmaț | p | 390 | 24 | 2062.53 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Acceptarea prezentelor condiții nu constituie co | p | 1440 | 432 | 2689.75 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acceptarea prezentelor condiții nu constituie co | p | 1024 | 224 | 2689.75 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acceptarea prezentelor condiții nu constituie co | p | 768 | 96 | 2689.75 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acceptarea prezentelor condiții nu constituie co | p | 390 | 24 | 2198.91 | 342 | 207.16 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-3` | 3. Acceptarea termenilor | Prin accesarea și utilizarea site-ului confirmaț | 20 | 20 | 20 | 20 |
| `section#sectiunea-3` | Prin accesarea și utilizarea site-ului confirmaț | Acceptarea prezentelor condiții nu constituie co | 18 | 18 | 18 | 18 |

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

## S11 — 4. Informațiile publicate. Prețuri (#sectiunea-4)

`section#sectiunea-4` · clase: `mb-12 md:mb-16`

Titlu: «4. Informațiile publicate. Prețuri»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 625.56 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 625.56 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 625.56 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 854.25 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 1440 | 576 | 322.94 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 1024 | 576 | 322.94 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 768 | 576 | 322.94 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 390 | 342 | 483.91 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 390 | 342 | 118.38 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 390 | 342 | 118.38 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| **container 5** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4. Informațiile publicate. Prețuri | h2 | 1440 | 432 | 2967.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Informațiile publicate. Prețuri | h2 | 1024 | 224 | 2967.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Informațiile publicate. Prețuri | h2 | 768 | 96 | 2967.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 4. Informațiile publicate. Prețuri | h2 | 390 | 24 | 2526.06 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Depunem eforturi rezonabile pentru ca informații | p | 1440 | 432 | 3027.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Depunem eforturi rezonabile pentru ca informații | p | 1024 | 224 | 3027.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Depunem eforturi rezonabile pentru ca informații | p | 768 | 96 | 3027.50 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Depunem eforturi rezonabile pentru ca informații | p | 390 | 24 | 2576.06 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Prețurile afișate: | p | 1440 | 432 | 3108.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețurile afișate: | p | 1024 | 224 | 3108.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețurile afișate: | p | 768 | 96 | 3108.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețurile afișate: | p | 390 | 24 | 2712.44 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| sunt exprimate în și au caracter ; | li | 1440 | 432 | 3157.81 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt exprimate în și au caracter ; | li | 1024 | 224 | 3157.81 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt exprimate în și au caracter ; | li | 768 | 96 | 3157.81 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt exprimate în și au caracter ; | li | 390 | 24 | 2760.03 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| euro | strong | 1440 | 600.80 | 3162.81 | 37.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| euro | strong | 1024 | 392.80 | 3162.81 | 37.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| euro | strong | 768 | 264.80 | 3162.81 | 37.19 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| euro | strong | 390 | 184.39 | 2764.03 | 35 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| orientativ | strong | 1440 | 756.59 | 3162.81 | 78.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| orientativ | strong | 1024 | 548.59 | 3162.81 | 78.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| orientativ | strong | 768 | 420.59 | 3162.81 | 78.39 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| orientativ | strong | 390 | 50 | 2793.63 | 73.78 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| în sensul art. 1188 Cod civil, ci invitație de a | li | 1440 | 432 | 3199.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| în sensul art. 1188 Cod civil, ci invitație de a | li | 1024 | 224 | 3199.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| în sensul art. 1188 Cod civil, ci invitație de a | li | 768 | 96 | 3199.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| în sensul art. 1188 Cod civil, ci invitație de a | li | 390 | 24 | 2829.22 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| nu constituie ofertă fermă | strong | 1440 | 458 | 3204.25 | 212.69 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie ofertă fermă | strong | 1024 | 250 | 3204.25 | 212.69 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie ofertă fermă | strong | 768 | 122 | 3204.25 | 212.69 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu constituie ofertă fermă | strong | 390 | 50 | 2833.22 | 200.17 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| se achită , la cursul de schimb comunicat de Ban | li | 1440 | 432 | 3272.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| se achită , la cursul de schimb comunicat de Ban | li | 1024 | 224 | 3272.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| se achită , la cursul de schimb comunicat de Ban | li | 768 | 96 | 3272.13 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| se achită , la cursul de schimb comunicat de Ban | li | 390 | 24 | 2928 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| în lei | strong | 1440 | 534.98 | 3277.13 | 38.09 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| în lei | strong | 1024 | 326.98 | 3277.13 | 38.09 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| în lei | strong | 768 | 198.98 | 3277.13 | 38.09 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| în lei | strong | 390 | 122.45 | 2932 | 35.84 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| sunt valabile pentru configurația de pachet desc | li | 1440 | 432 | 3345 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt valabile pentru configurația de pachet desc | li | 1024 | 224 | 3345 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt valabile pentru configurația de pachet desc | li | 768 | 96 | 3345 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| sunt valabile pentru configurația de pachet desc | li | 390 | 24 | 3056.38 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| costurile de deplasare, care se calculează separ | li | 1440 | 432 | 3417.88 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| costurile de deplasare, care se calculează separ | li | 1024 | 224 | 3417.88 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| costurile de deplasare, care se calculează separ | li | 768 | 96 | 3417.88 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| costurile de deplasare, care se calculează separ | li | 390 | 24 | 3184.75 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| nu includ | strong | 1440 | 458 | 3422.88 | 75.33 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu includ | strong | 1024 | 250 | 3422.88 | 75.33 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu includ | strong | 768 | 122 | 3422.88 | 75.33 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu includ | strong | 390 | 50 | 3188.75 | 70.89 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Prețul ferm, configurația finală a pachetului și | p | 1440 | 432 | 3498.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețul ferm, configurația finală a pachetului și | p | 1024 | 224 | 3498.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețul ferm, configurația finală a pachetului și | p | 768 | 96 | 3498.75 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prețul ferm, configurația finală a pachetului și | p | 390 | 24 | 3261.94 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-4` | 4. Informațiile publicate. Prețuri | Depunem eforturi rezonabile pentru ca informații | 20 | 20 | 20 | 20 |
| `section#sectiunea-4` | Depunem eforturi rezonabile pentru ca informații | Prețurile afișate: | 18 | 18 | 18 | 18 |
| `section#sectiunea-4` | Prețurile afișate: | [sunt exprimate în euro și au caracter or] | 18 | 18 | 18 | 18 |
| `section#sectiunea-4` | [sunt exprimate în euro și au caracter or] | Prețul ferm, configurația finală a pachetului și | 18 | 18 | 18 | 18 |
| `ul.motif-list` | sunt exprimate în și au caracter ; | în sensul art. 1188 Cod civil, ci invitație de a | 10 | 10 | 10 | 10 |
| `ul.motif-list` | în sensul art. 1188 Cod civil, ci invitație de a | se achită , la cursul de schimb comunicat de Ban | 10 | 10 | 10 | 10 |
| `ul.motif-list` | se achită , la cursul de schimb comunicat de Ban | sunt valabile pentru configurația de pachet desc | 10 | 10 | 10 | 10 |
| `ul.motif-list` | sunt valabile pentru configurația de pachet desc | costurile de deplasare, care se calculează separ | 10 | 10 | 10 | 10 |
| `li` | euro | orientativ | -20 ¹ | -20 ¹ | -20 ¹ | 9.60 ¹ |

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

## S13 — 5. Rezervarea și încheierea contractului (#sectiunea-5)

`section#sectiunea-5` · clase: `mb-12 md:mb-16`

Titlu: «5. Rezervarea și încheierea contractului»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 440.38 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 440.38 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 440.38 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 530.72 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 3** (`ol.list-decimal`) | 1440 | 576 | 187.19 | 0/0/0/24 | transparent | none |
| **container 3** (`ol.list-decimal`) | 1024 | 576 | 187.19 | 0/0/0/24 | transparent | none |
| **container 3** (`ol.list-decimal`) | 768 | 576 | 187.19 | 0/0/0/24 | transparent | none |
| **container 3** (`ol.list-decimal`) | 390 | 342 | 207.56 | 0/0/0/24 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 552 | 62.88 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1024 | 552 | 62.88 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 768 | 552 | 62.88 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 390 | 318 | 59.19 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 1440 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 1024 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 768 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 390 | 318 | 59.19 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 1440 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 1024 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 768 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 390 | 318 | 29.59 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 1440 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 1024 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 768 | 552 | 31.44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 390 | 318 | 29.59 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 527.84 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 527.84 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 527.84 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 284.69 | 49.59 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5. Rezervarea și încheierea contractului | h2 | 1440 | 432 | 3745.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Rezervarea și încheierea contractului | h2 | 1024 | 224 | 3745.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Rezervarea și încheierea contractului | h2 | 768 | 96 | 3745.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 5. Rezervarea și încheierea contractului | h2 | 390 | 24 | 3500.31 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Rezervarea unei date se face în următorii pași: | p | 1440 | 432 | 3805.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Rezervarea unei date se face în următorii pași: | p | 1024 | 224 | 3805.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Rezervarea unei date se face în următorii pași: | p | 768 | 96 | 3805.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Rezervarea unei date se face în următorii pași: | p | 390 | 24 | 3580.31 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Ne contactați prin telefon, WhatsApp sau e-mail  | li | 1440 | 456 | 3854.50 | 552 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne contactați prin telefon, WhatsApp sau e-mail  | li | 1024 | 248 | 3854.50 | 552 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne contactați prin telefon, WhatsApp sau e-mail  | li | 768 | 120 | 3854.50 | 552 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne contactați prin telefon, WhatsApp sau e-mail  | li | 390 | 48 | 3657.50 | 318 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Stabilim împreună configurația pachetului și pre | li | 1440 | 456 | 3927.38 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Stabilim împreună configurația pachetului și pre | li | 1024 | 248 | 3927.38 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Stabilim împreună configurația pachetului și pre | li | 768 | 120 | 3927.38 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Stabilim împreună configurația pachetului și pre | li | 390 | 48 | 3726.69 | 318 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Semnăm contractul de prestări servicii. | li | 1440 | 456 | 3968.81 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Semnăm contractul de prestări servicii. | li | 1024 | 248 | 3968.81 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Semnăm contractul de prestări servicii. | li | 768 | 120 | 3968.81 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Semnăm contractul de prestări servicii. | li | 390 | 48 | 3795.88 | 318 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Achitați avansul stabilit prin contract. | li | 1440 | 456 | 4010.25 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Achitați avansul stabilit prin contract. | li | 1024 | 248 | 4010.25 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Achitați avansul stabilit prin contract. | li | 768 | 120 | 4010.25 | 552 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Achitați avansul stabilit prin contract. | li | 390 | 48 | 3835.47 | 318 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Data evenimentului se consideră rezervată . Veri | p | 1440 | 432 | 4059.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Data evenimentului se consideră rezervată . Veri | p | 1024 | 224 | 4059.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Data evenimentului se consideră rezervată . Veri | p | 768 | 96 | 4059.69 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Data evenimentului se consideră rezervată . Veri | p | 390 | 24 | 3883.06 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| numai după semnarea contractului și confirmarea  | strong | 1440 | 432 | 4064.69 | 527.84 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după semnarea contractului și confirmarea  | strong | 1024 | 224 | 4064.69 | 527.84 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după semnarea contractului și confirmarea  | strong | 768 | 96 | 4064.69 | 527.84 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai după semnarea contractului și confirmarea  | strong | 390 | 24 | 3916.66 | 284.69 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-5` | 5. Rezervarea și încheierea contractului | Rezervarea unei date se face în următorii pași: | 20 | 20 | 20 | 20 |
| `section#sectiunea-5` | Rezervarea unei date se face în următorii pași: | [Ne contactați prin telefon, WhatsApp sau] | 18 | 18 | 18 | 18 |
| `section#sectiunea-5` | [Ne contactați prin telefon, WhatsApp sau] | Data evenimentului se consideră rezervată . Veri | 18 | 18 | 18 | 18 |
| `ol.list-decimal` | Ne contactați prin telefon, WhatsApp sau e-mail  | Stabilim împreună configurația pachetului și pre | 10 | 10 | 10 | 10 |
| `ol.list-decimal` | Stabilim împreună configurația pachetului și pre | Semnăm contractul de prestări servicii. | 10 | 10 | 10 | 10 |
| `ol.list-decimal` | Semnăm contractul de prestări servicii. | Achitați avansul stabilit prin contract. | 10 | 10 | 10 | 10 |

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

## S15 — 6. Deplasarea (#sectiunea-6)

`section#sectiunea-6` · clase: `mb-12 md:mb-16`

Eyebrow: «[TARIF]»

Titlu: «6. Deplasarea»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 316.06 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 316.06 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 316.06 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 352.34 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 131.27 | 26 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 131.27 | 26 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 131.27 | 26 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 324.23 | 52.59 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6. Deplasarea | h2 | 1440 | 432 | 4337.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Deplasarea | h2 | 1024 | 224 | 4337.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Deplasarea | h2 | 768 | 96 | 4337.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 6. Deplasarea | h2 | 390 | 24 | 4151.03 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Serviciile sunt disponibile la nivel național. | p | 1440 | 432 | 4397.44 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Serviciile sunt disponibile la nivel național. | p | 1024 | 224 | 4397.44 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Serviciile sunt disponibile la nivel național. | p | 768 | 96 | 4397.44 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Serviciile sunt disponibile la nivel național. | p | 390 | 24 | 4201.03 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele desfășurate în afara localit | p | 1440 | 432 | 4446.88 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele desfășurate în afara localit | p | 1024 | 224 | 4446.88 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele desfășurate în afara localit | p | 768 | 96 | 4446.88 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru evenimentele desfășurate în afara localit | p | 390 | 24 | 4248.63 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| lei/km | strong | 1440 | 828.75 | 4480.31 | 131.27 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| lei/km | strong | 1024 | 620.75 | 4480.31 | 131.27 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| lei/km | strong | 768 | 492.75 | 4480.31 | 131.27 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| lei/km | strong | 390 | 24 | 4308.81 | 324.23 | 52.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [TARIF] | span | 1440 | 828.75 | 4480.31 | 76.59 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TARIF] | span | 1024 | 620.75 | 4480.31 | 76.59 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TARIF] | span | 768 | 492.75 | 4480.31 | 76.59 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TARIF] | span | 390 | 275.22 | 4308.81 | 73.02 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 835.75 | 4477.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 627.75 | 4477.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 499.75 | 4477.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 282.22 | 4306.81 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Pentru distanțele care impun cazare peste noapte | p | 1440 | 432 | 4559.19 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru distanțele care impun cazare peste noapte | p | 1024 | 224 | 4559.19 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru distanțele care impun cazare peste noapte | p | 768 | 96 | 4559.19 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru distanțele care impun cazare peste noapte | p | 390 | 24 | 4385 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-6` | 6. Deplasarea | Serviciile sunt disponibile la nivel național. | 20 | 20 | 20 | 20 |
| `section#sectiunea-6` | Serviciile sunt disponibile la nivel național. | Pentru evenimentele desfășurate în afara localit | 18 | 18 | 18 | 18 |
| `section#sectiunea-6` | Pentru evenimentele desfășurate în afara localit | Pentru distanțele care impun cazare peste noapte | 18 | 18 | 18 | 18 |

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

## S17 — 7. Modificarea și anularea rezervării (#sectiunea-7)

`section#sectiunea-7` · clase: `mb-12 md:mb-16`

Titlu: «7. Modificarea și anularea rezervării»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 275.16 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7. Modificarea și anularea rezervării | h2 | 1440 | 432 | 4805.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Modificarea și anularea rezervării | h2 | 1024 | 224 | 4805.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Modificarea și anularea rezervării | h2 | 768 | 96 | 4805.50 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 7. Modificarea și anularea rezervării | h2 | 390 | 24 | 4623.38 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Condițiile de modificare, amânare și anulare a e | p | 1440 | 432 | 4865.50 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Condițiile de modificare, amânare și anulare a e | p | 1024 | 224 | 4865.50 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Condițiile de modificare, amânare și anulare a e | p | 768 | 96 | 4865.50 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Condițiile de modificare, amânare și anulare a e | p | 390 | 24 | 4673.38 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| În situații de forță majoră, în sensul art. 1351 | p | 1440 | 432 | 4977.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În situații de forță majoră, în sensul art. 1351 | p | 1024 | 224 | 4977.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În situații de forță majoră, în sensul art. 1351 | p | 768 | 96 | 4977.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În situații de forță majoră, în sensul art. 1351 | p | 390 | 24 | 4809.75 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-7` | 7. Modificarea și anularea rezervării | Condițiile de modificare, amânare și anulare a e | 20 | 20 | 20 | 20 |
| `section#sectiunea-7` | Condițiile de modificare, amânare și anulare a e | În situații de forță majoră, în sensul art. 1351 | 18 | 18 | 18 | 18 |

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

## S19 — 8. Drepturi de proprietate intelectuală (#sectiunea-8)

`section#sectiunea-8` · clase: `mb-12 md:mb-16`

Titlu: «8. Drepturi de proprietate intelectuală»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 428.38 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 428.38 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 428.38 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 607.50 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8. Drepturi de proprietate intelectuală | h2 | 1440 | 432 | 5192.69 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Drepturi de proprietate intelectuală | h2 | 1024 | 224 | 5192.69 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Drepturi de proprietate intelectuală | h2 | 768 | 96 | 5192.69 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 8. Drepturi de proprietate intelectuală | h2 | 390 | 24 | 5018.53 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Întregul conținut al site-ului — texte, fotograf | p | 1440 | 432 | 5252.69 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Întregul conținut al site-ului — texte, fotograf | p | 1024 | 224 | 5252.69 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Întregul conținut al site-ului — texte, fotograf | p | 768 | 96 | 5252.69 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Întregul conținut al site-ului — texte, fotograf | p | 390 | 24 | 5098.53 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Este interzisă reproducerea, distribuirea, modif | p | 1440 | 432 | 5365 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Este interzisă reproducerea, distribuirea, modif | p | 1024 | 224 | 5365 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Este interzisă reproducerea, distribuirea, modif | p | 768 | 96 | 5365 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Este interzisă reproducerea, distribuirea, modif | p | 390 | 24 | 5264.50 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Înregistrările muzicale prezentate pot aparține  | p | 1440 | 432 | 5477.31 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Înregistrările muzicale prezentate pot aparține  | p | 1024 | 224 | 5477.31 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Înregistrările muzicale prezentate pot aparține  | p | 768 | 96 | 5477.31 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Înregistrările muzicale prezentate pot aparține  | p | 390 | 24 | 5430.47 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Utilizarea site-ului nu conferă niciun drept de  | p | 1440 | 432 | 5558.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea site-ului nu conferă niciun drept de  | p | 1024 | 224 | 5558.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea site-ului nu conferă niciun drept de  | p | 768 | 96 | 5558.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea site-ului nu conferă niciun drept de  | p | 390 | 24 | 5537.25 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-8` | 8. Drepturi de proprietate intelectuală | Întregul conținut al site-ului — texte, fotograf | 20 | 20 | 20 | 20 |
| `section#sectiunea-8` | Întregul conținut al site-ului — texte, fotograf | Este interzisă reproducerea, distribuirea, modif | 18 | 18 | 18 | 18 |
| `section#sectiunea-8` | Este interzisă reproducerea, distribuirea, modif | Înregistrările muzicale prezentate pot aparține  | 18 | 18 | 18 | 18 |
| `section#sectiunea-8` | Înregistrările muzicale prezentate pot aparține  | Utilizarea site-ului nu conferă niciun drept de  | 18 | 18 | 18 | 18 |

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

## S21 — 9. Materiale audio-video de la evenimente (#sectiunea-9)

`section#sectiunea-9` · clase: `mb-12 md:mb-16`

Titlu: «9. Materiale audio-video de la evenimente»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 441.53 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 539.47 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 539.47 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 539.47 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 329.98 | 49.59 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9. Materiale audio-video de la evenimente | h2 | 1440 | 432 | 5773.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Materiale audio-video de la evenimente | h2 | 1024 | 224 | 5773.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Materiale audio-video de la evenimente | h2 | 768 | 96 | 5773.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 9. Materiale audio-video de la evenimente | h2 | 390 | 24 | 5746.03 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Fotografiile și înregistrările realizate în cadr | p | 1440 | 432 | 5833.06 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fotografiile și înregistrările realizate în cadr | p | 1024 | 224 | 5833.06 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fotografiile și înregistrările realizate în cadr | p | 768 | 96 | 5833.06 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Fotografiile și înregistrările realizate în cadr | p | 390 | 24 | 5826.03 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| numai cu acordul scris prealabil al beneficiarul | strong | 1440 | 432 | 5869.50 | 539.47 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai cu acordul scris prealabil al beneficiarul | strong | 1024 | 224 | 5869.50 | 539.47 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai cu acordul scris prealabil al beneficiarul | strong | 768 | 96 | 5869.50 | 539.47 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| numai cu acordul scris prealabil al beneficiarul | strong | 390 | 24 | 5889.22 | 329.98 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Beneficiarul poate refuza acest acord fără ca re | p | 1440 | 432 | 5976.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Beneficiarul poate refuza acest acord fără ca re | p | 1024 | 224 | 5976.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Beneficiarul poate refuza acest acord fără ca re | p | 768 | 96 | 5976.81 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Beneficiarul poate refuza acest acord fără ca re | p | 390 | 24 | 5992 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Acordul poate fi retras ulterior, cu efect pentr | p | 1440 | 432 | 6057.69 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acordul poate fi retras ulterior, cu efect pentr | p | 1024 | 224 | 6057.69 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acordul poate fi retras ulterior, cu efect pentr | p | 768 | 96 | 6057.69 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Acordul poate fi retras ulterior, cu efect pentr | p | 390 | 24 | 6098.78 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-9` | 9. Materiale audio-video de la evenimente | Fotografiile și înregistrările realizate în cadr | 20 | 20 | 20 | 20 |
| `section#sectiunea-9` | Fotografiile și înregistrările realizate în cadr | Beneficiarul poate refuza acest acord fără ca re | 18 | 18 | 18 | 18 |
| `section#sectiunea-9` | Beneficiarul poate refuza acest acord fără ca re | Acordul poate fi retras ulterior, cu efect pentr | 18 | 18 | 18 | 18 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S22 — div.motif-separator

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

## S23 — 10. Limitarea răspunderii (#sectiunea-10)

`section#sectiunea-10` · clase: `mb-12 md:mb-16`

Titlu: «10. Limitarea răspunderii»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 347.50 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 411.53 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10. Limitarea răspunderii | h2 | 1440 | 432 | 6272.56 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 10. Limitarea răspunderii | h2 | 1024 | 224 | 6272.56 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 10. Limitarea răspunderii | h2 | 768 | 96 | 6272.56 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 10. Limitarea răspunderii | h2 | 390 | 24 | 6307.56 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Site-ul este pus la dispoziție în forma în care  | p | 1440 | 432 | 6332.56 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este pus la dispoziție în forma în care  | p | 1024 | 224 | 6332.56 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este pus la dispoziție în forma în care  | p | 768 | 96 | 6332.56 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul este pus la dispoziție în forma în care  | p | 390 | 24 | 6357.56 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Nu răspundem pentru daune indirecte rezultate di | p | 1440 | 432 | 6413.44 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu răspundem pentru daune indirecte rezultate di | p | 1024 | 224 | 6413.44 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu răspundem pentru daune indirecte rezultate di | p | 768 | 96 | 6413.44 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu răspundem pentru daune indirecte rezultate di | p | 390 | 24 | 6464.34 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Prezenta limitare nu înlătură și nu restrânge ră | p | 1440 | 432 | 6494.31 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prezenta limitare nu înlătură și nu restrânge ră | p | 1024 | 224 | 6494.31 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prezenta limitare nu înlătură și nu restrânge ră | p | 768 | 96 | 6494.31 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Prezenta limitare nu înlătură și nu restrânge ră | p | 390 | 24 | 6571.13 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-10` | 10. Limitarea răspunderii | Site-ul este pus la dispoziție în forma în care  | 20 | 20 | 20 | 20 |
| `section#sectiunea-10` | Site-ul este pus la dispoziție în forma în care  | Nu răspundem pentru daune indirecte rezultate di | 18 | 18 | 18 | 18 |
| `section#sectiunea-10` | Nu răspundem pentru daune indirecte rezultate di | Prezenta limitare nu înlătură și nu restrânge ră | 18 | 18 | 18 | 18 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S24 — div.motif-separator

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

## S25 — 11. Linkuri către site-uri terțe (#sectiunea-11)

`section#sectiunea-11` · clase: `mb-12 md:mb-16`

Titlu: «11. Linkuri către site-uri terțe»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 275.16 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 11. Linkuri către site-uri terțe | h2 | 1440 | 432 | 6772.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 11. Linkuri către site-uri terțe | h2 | 1024 | 224 | 6772.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 11. Linkuri către site-uri terțe | h2 | 768 | 96 | 6772.06 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 11. Linkuri către site-uri terțe | h2 | 390 | 24 | 6839.09 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Site-ul poate conține linkuri către platforme te | p | 1440 | 432 | 6832.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul poate conține linkuri către platforme te | p | 1024 | 224 | 6832.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul poate conține linkuri către platforme te | p | 768 | 96 | 6832.06 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Site-ul poate conține linkuri către platforme te | p | 390 | 24 | 6889.09 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Accesarea unui site terț se face pe răspunderea  | p | 1440 | 432 | 6944.38 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Accesarea unui site terț se face pe răspunderea  | p | 1024 | 224 | 6944.38 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Accesarea unui site terț se face pe răspunderea  | p | 768 | 96 | 6944.38 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Accesarea unui site terț se face pe răspunderea  | p | 390 | 24 | 7025.47 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-11` | 11. Linkuri către site-uri terțe | Site-ul poate conține linkuri către platforme te | 20 | 20 | 20 | 20 |
| `section#sectiunea-11` | Site-ul poate conține linkuri către platforme te | Accesarea unui site terț se face pe răspunderea  | 18 | 18 | 18 | 18 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S26 — div.motif-separator

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

## S27 — 12. Prelucrarea datelor cu caracter personal (#sectiunea-12)

`section#sectiunea-12` · clase: `mb-12 md:mb-16`

Eyebrow: «[FURNIZOR-HOSTING]»

Titlu: «12. Prelucrarea datelor cu caracter personal»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 2956.61 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 2956.61 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 3030.19 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 3532.88 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 88.78 | 0/0/0/0 | transparent | none |
| **container 3** (`h3#sectiunea-12-1`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 3** (`h3#sectiunea-12-1`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 3** (`h3#sectiunea-12-1`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 3** (`h3#sectiunea-12-1`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 4** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 5** (`h3#sectiunea-12-2`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 5** (`h3#sectiunea-12-2`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 5** (`h3#sectiunea-12-2`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 5** (`h3#sectiunea-12-2`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 6** (`p.md:hidden`) | 1440 | **nerandat** | — | — | — | — |
| **container 6** (`p.md:hidden`) | 1024 | **nerandat** | — | — | — | — |
| **container 6** (`p.md:hidden`) | 768 | **nerandat** | — | — | — | — |
| **container 6** (`p.md:hidden`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 7** (`div.overflow-x-auto`) | 1440 | 800 | 608.48 | 0/0/0/0 | transparent | none |
| **container 7** (`div.overflow-x-auto`) | 1024 | 800 | 608.48 | 0/0/0/0 | transparent | none |
| **container 7** (`div.overflow-x-auto`) | 768 | 576 | 682.06 | 0/0/0/0 | transparent | none |
| **container 7** (`div.overflow-x-auto`) | 390 | 342 | 682.06 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 1440 | 800 | 608.48 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 1024 | 800 | 608.48 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 768 | 768 | 682.06 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`table.legal-table`) | 390 | 768 | 682.06 | 0/0/0/0 | transparent | none |
| **container 8** (`h3#sectiunea-12-3`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 8** (`h3#sectiunea-12-3`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 8** (`h3#sectiunea-12-3`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 8** (`h3#sectiunea-12-3`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 9** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 9** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 9** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 9** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 10** (`ul.motif-list`) | 1440 | 576 | 155.75 | 0/0/0/0 | transparent | none |
| **container 10** (`ul.motif-list`) | 1024 | 576 | 155.75 | 0/0/0/0 | transparent | none |
| **container 10** (`ul.motif-list`) | 768 | 576 | 155.75 | 0/0/0/0 | transparent | none |
| **container 10** (`ul.motif-list`) | 390 | 342 | 266.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| **container 11** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 11** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 12** (`h3#sectiunea-12-4`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 12** (`h3#sectiunea-12-4`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 12** (`h3#sectiunea-12-4`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 12** (`h3#sectiunea-12-4`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 13** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 13** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 13** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 13** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |
| **container 14** (`h3#sectiunea-12-5`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 14** (`h3#sectiunea-12-5`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 14** (`h3#sectiunea-12-5`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 14** (`h3#sectiunea-12-5`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 15** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 15** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 15** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 15** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 16** (`ul.motif-list`) | 1440 | 576 | 384.38 | 0/0/0/0 | transparent | none |
| **container 16** (`ul.motif-list`) | 1024 | 576 | 384.38 | 0/0/0/0 | transparent | none |
| **container 16** (`ul.motif-list`) | 768 | 576 | 384.38 | 0/0/0/0 | transparent | none |
| **container 16** (`ul.motif-list`) | 390 | 342 | 425.13 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 3 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 4 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 5 (`li`) | 390 | 342 | 29.59 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 1440 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 1024 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 768 | 576 | 31.44 | 0/0/0/26 |  +bg-image | none |
| └ coloana 6 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| └ coloana 7 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 7 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 7 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 7 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 8 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 8 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 8 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 8 (`li`) | 390 | 342 | 59.19 | 0/0/0/26 |  +bg-image | none |
| **container 17** (`p`) | 1440 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 17** (`p`) | 1024 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 17** (`p`) | 768 | 576 | 125.75 | 0/0/0/0 | transparent | none |
| **container 17** (`p`) | 390 | 342 | 177.56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 63.61 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 63.61 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 63.61 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 59.88 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 1440 | 569.80 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 1024 | 569.80 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 768 | 569.80 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`strong`) | 390 | 112.05 | 20 | 0/0/0/0 | transparent | none |
| **container 18** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 18** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 18** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 18** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 19** (`h3#sectiunea-12-6`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 19** (`h3#sectiunea-12-6`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 19** (`h3#sectiunea-12-6`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 19** (`h3#sectiunea-12-6`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 20** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 20** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 20** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 20** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 21** (`p`) | 1440 | 576 | 220.06 | 0/0/0/0 | transparent | none |
| **container 21** (`p`) | 1024 | 576 | 220.06 | 0/0/0/0 | transparent | none |
| **container 21** (`p`) | 768 | 576 | 220.06 | 0/0/0/0 | transparent | none |
| **container 21** (`p`) | 390 | 342 | 236.75 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1440 | 509.78 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 1024 | 509.78 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 768 | 509.78 | 51.44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`strong`) | 390 | 313.14 | 79.19 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 1440 | 223.94 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 1024 | 223.94 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 768 | 223.94 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`a`) | 390 | 210.77 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`a`) | 1440 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`a`) | 1024 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`a`) | 768 | 241.11 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`a`) | 390 | 226.92 | 20 | 0/0/0/0 | transparent | none |
| **container 22** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 22** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 22** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 22** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 23** (`h3#sectiunea-12-7`) | 1440 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 23** (`h3#sectiunea-12-7`) | 1024 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 23** (`h3#sectiunea-12-7`) | 768 | 576 | 32 | 0/0/0/0 | transparent | none |
| **container 23** (`h3#sectiunea-12-7`) | 390 | 342 | 60 | 0/0/0/0 | transparent | none |
| **container 24** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 24** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 24** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 24** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12. Prelucrarea datelor cu caracter personal | h2 | 1440 | 432 | 7159.25 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 12. Prelucrarea datelor cu caracter personal | h2 | 1024 | 224 | 7159.25 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 12. Prelucrarea datelor cu caracter personal | h2 | 768 | 96 | 7159.25 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 12. Prelucrarea datelor cu caracter personal | h2 | 390 | 24 | 7234.25 | 342 | 60 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Această secțiune constituie informarea prevăzută | p | 1440 | 432 | 7219.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Această secțiune constituie informarea prevăzută | p | 1024 | 224 | 7219.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Această secțiune constituie informarea prevăzută | p | 768 | 96 | 7219.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Această secțiune constituie informarea prevăzută | p | 390 | 24 | 7314.25 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.1 Operatorul | h3 | 1440 | 432 | 7322.13 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.1 Operatorul | h3 | 1024 | 224 | 7322.13 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.1 Operatorul | h3 | 768 | 96 | 7322.13 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.1 Operatorul | h3 | 390 | 24 | 7443.03 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Operatorul datelor este entitatea identificată l | p | 1440 | 432 | 7370.13 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Operatorul datelor este entitatea identificată l | p | 1024 | 224 | 7370.13 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Operatorul datelor este entitatea identificată l | p | 768 | 96 | 7370.13 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Operatorul datelor este entitatea identificată l | p | 390 | 24 | 7489.03 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.2 Ce date prelucrăm, în ce scop și în ce teme | h3 | 1440 | 432 | 7504.44 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.2 Ce date prelucrăm, în ce scop și în ce teme | h3 | 1024 | 224 | 7504.44 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.2 Ce date prelucrăm, în ce scop și în ce teme | h3 | 768 | 96 | 7504.44 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.2 Ce date prelucrăm, în ce scop și în ce teme | h3 | 390 | 24 | 7647.41 | 342 | 60 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Glisați lateral pentru a vedea tot tabelul. | p | 1440 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 1024 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 768 | **nerandat** | | | | | | | | | |
| Glisați lateral pentru a vedea tot tabelul. | p | 390 | 24 | 7723.41 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Categorie de date | th | 1440 | 320.50 | 7552.94 | 208.47 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Categorie de date | th | 1024 | 112.50 | 7552.94 | 208.47 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Categorie de date | th | 768 | 96.50 | 7552.94 | 197.69 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Categorie de date | th | 390 | 24.50 | 7771.50 | 197.69 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 1440 | 528.97 | 7552.94 | 183.44 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 1024 | 320.97 | 7552.94 | 183.44 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 768 | 294.19 | 7552.94 | 176.73 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Scop | th | 390 | 222.19 | 7771.50 | 176.73 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Temei juridic | th | 1440 | 712.41 | 7552.94 | 206.72 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Temei juridic | th | 1024 | 504.41 | 7552.94 | 206.72 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Temei juridic | th | 768 | 470.92 | 7552.94 | 197.81 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Temei juridic | th | 390 | 398.92 | 7771.50 | 197.81 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată de stocare | th | 1440 | 919.13 | 7552.94 | 200.38 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată de stocare | th | 1024 | 711.13 | 7552.94 | 200.38 | 47.39 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată de stocare | th | 768 | 668.73 | 7552.94 | 194.77 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Durată de stocare | th | 390 | 596.73 | 7771.50 | 194.77 | 69.78 | 14 | 22.40 | 0.84 | 600 | #e5e2e1 | left |
| Nume, telefon, e-mail, data și tipul evenimentul | td | 1440 | 320.50 | 7600.33 | 208.47 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Nume, telefon, e-mail, data și tipul evenimentul | td | 1024 | 112.50 | 7600.33 | 208.47 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Nume, telefon, e-mail, data și tipul evenimentul | td | 768 | 96.50 | 7622.72 | 197.69 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Nume, telefon, e-mail, data și tipul evenimentul | td | 390 | 24.50 | 7841.28 | 197.69 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Răspuns la solicitare, verificare disponibilitat | td | 1440 | 528.97 | 7600.33 | 183.44 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Răspuns la solicitare, verificare disponibilitat | td | 1024 | 320.97 | 7600.33 | 183.44 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Răspuns la solicitare, verificare disponibilitat | td | 768 | 294.19 | 7622.72 | 176.73 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Răspuns la solicitare, verificare disponibilitat | td | 390 | 222.19 | 7841.28 | 176.73 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR — demersuri precon | td | 1440 | 712.41 | 7600.33 | 206.72 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR — demersuri precon | td | 1024 | 504.41 | 7600.33 | 206.72 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR — demersuri precon | td | 768 | 470.92 | 7622.72 | 197.81 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR — demersuri precon | td | 390 | 398.92 | 7841.28 | 197.81 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 12 luni de la ultima interacțiune, dacă nu se în | td | 1440 | 919.13 | 7600.33 | 200.38 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 12 luni de la ultima interacțiune, dacă nu se în | td | 1024 | 711.13 | 7600.33 | 200.38 | 152.97 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 12 luni de la ultima interacțiune, dacă nu se în | td | 768 | 668.73 | 7622.72 | 194.77 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 12 luni de la ultima interacțiune, dacă nu se în | td | 390 | 596.73 | 7841.28 | 194.77 | 178.56 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Date de identificare și de facturare | td | 1440 | 320.50 | 7753.30 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Date de identificare și de facturare | td | 1024 | 112.50 | 7753.30 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Date de identificare și de facturare | td | 768 | 96.50 | 7801.28 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Date de identificare și de facturare | td | 390 | 24.50 | 8019.84 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Executarea contractului de prestări servicii | td | 1440 | 528.97 | 7753.30 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Executarea contractului de prestări servicii | td | 1024 | 320.97 | 7753.30 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Executarea contractului de prestări servicii | td | 768 | 294.19 | 7801.28 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Executarea contractului de prestări servicii | td | 390 | 222.19 | 8019.84 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR | td | 1440 | 712.41 | 7753.30 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR | td | 1024 | 504.41 | 7753.30 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR | td | 768 | 470.92 | 7801.28 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. b) GDPR | td | 390 | 398.92 | 8019.84 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Pe durata contractului | td | 1440 | 919.13 | 7753.30 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Pe durata contractului | td | 1024 | 711.13 | 7753.30 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Pe durata contractului | td | 768 | 668.73 | 7801.28 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Pe durata contractului | td | 390 | 596.73 | 8019.84 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Documente financiar-contabile | td | 1440 | 320.50 | 7855.08 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Documente financiar-contabile | td | 1024 | 112.50 | 7855.08 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Documente financiar-contabile | td | 768 | 96.50 | 7903.06 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Documente financiar-contabile | td | 390 | 24.50 | 8121.63 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Îndeplinirea obligațiilor legale contabile și fi | td | 1440 | 528.97 | 7855.08 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Îndeplinirea obligațiilor legale contabile și fi | td | 1024 | 320.97 | 7855.08 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Îndeplinirea obligațiilor legale contabile și fi | td | 768 | 294.19 | 7903.06 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Îndeplinirea obligațiilor legale contabile și fi | td | 390 | 222.19 | 8121.63 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | td | 1440 | 712.41 | 7855.08 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | td | 1024 | 504.41 | 7855.08 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | td | 768 | 470.92 | 7903.06 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | td | 390 | 398.92 | 8121.63 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 10 ani, conform legii contabilității | td | 1440 | 919.13 | 7855.08 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 10 ani, conform legii contabilității | td | 1024 | 711.13 | 7855.08 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 10 ani, conform legii contabilității | td | 768 | 668.73 | 7903.06 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 10 ani, conform legii contabilității | td | 390 | 596.73 | 8121.63 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Fotografii și înregistrări de la eveniment, folo | td | 1440 | 320.50 | 7956.86 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Fotografii și înregistrări de la eveniment, folo | td | 1024 | 112.50 | 7956.86 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Fotografii și înregistrări de la eveniment, folo | td | 768 | 96.50 | 8004.84 | 197.69 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Fotografii și înregistrări de la eveniment, folo | td | 390 | 24.50 | 8223.41 | 197.69 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Promovarea activității artistice | td | 1440 | 528.97 | 7956.86 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Promovarea activității artistice | td | 1024 | 320.97 | 7956.86 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Promovarea activității artistice | td | 768 | 294.19 | 8004.84 | 176.73 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Promovarea activității artistice | td | 390 | 222.19 | 8223.41 | 176.73 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. a) GDPR — consimțământ | td | 1440 | 712.41 | 7956.86 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. a) GDPR — consimțământ | td | 1024 | 504.41 | 7956.86 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. a) GDPR — consimțământ | td | 768 | 470.92 | 8004.84 | 197.81 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. a) GDPR — consimțământ | td | 390 | 398.92 | 8223.41 | 197.81 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Până la retragerea consimțământului | td | 1440 | 919.13 | 7956.86 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Până la retragerea consimțământului | td | 1024 | 711.13 | 7956.86 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Până la retragerea consimțământului | td | 768 | 668.73 | 8004.84 | 194.77 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Până la retragerea consimțământului | td | 390 | 596.73 | 8223.41 | 194.77 | 127.38 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Adresă IP, date tehnice de acces la server | td | 1440 | 320.50 | 8058.64 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Adresă IP, date tehnice de acces la server | td | 1024 | 112.50 | 8058.64 | 208.47 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Adresă IP, date tehnice de acces la server | td | 768 | 96.50 | 8132.22 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Adresă IP, date tehnice de acces la server | td | 390 | 24.50 | 8350.78 | 197.69 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Securitatea și funcționarea site-ului | td | 1440 | 528.97 | 8058.64 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Securitatea și funcționarea site-ului | td | 1024 | 320.97 | 8058.64 | 183.44 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Securitatea și funcționarea site-ului | td | 768 | 294.19 | 8132.22 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Securitatea și funcționarea site-ului | td | 390 | 222.19 | 8350.78 | 176.73 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. f) GDPR — interes legitim | td | 1440 | 712.41 | 8058.64 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. f) GDPR — interes legitim | td | 1024 | 504.41 | 8058.64 | 206.72 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. f) GDPR — interes legitim | td | 768 | 470.92 | 8132.22 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Art. 6 alin. (1) lit. f) GDPR — interes legitim | td | 390 | 398.92 | 8350.78 | 197.81 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Maximum 30 de zile | td | 1440 | 919.13 | 8058.64 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Maximum 30 de zile | td | 1024 | 711.13 | 8058.64 | 200.38 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Maximum 30 de zile | td | 768 | 668.73 | 8132.22 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| Maximum 30 de zile | td | 390 | 596.73 | 8350.78 | 194.77 | 101.78 | 16 | 25.60 | normal | 400 | #c4c7c7 | left |
| 12.3 Cui transmitem datele | h3 | 1440 | 432 | 8200.92 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.3 Cui transmitem datele | h3 | 1024 | 224 | 8200.92 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.3 Cui transmitem datele | h3 | 768 | 96 | 8274.50 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.3 Cui transmitem datele | h3 | 390 | 24 | 8493.06 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Datele pot fi accesate de: | p | 1440 | 432 | 8248.92 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Datele pot fi accesate de: | p | 1024 | 224 | 8248.92 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Datele pot fi accesate de: | p | 768 | 96 | 8322.50 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Datele pot fi accesate de: | p | 390 | 24 | 8539.06 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| furnizorul de găzduire web: ; | li | 1440 | 432 | 8298.36 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul de găzduire web: ; | li | 1024 | 224 | 8298.36 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul de găzduire web: ; | li | 768 | 96 | 8371.94 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul de găzduire web: ; | li | 390 | 24 | 8586.66 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| [FURNIZOR-HOSTING] | span | 1440 | 683.06 | 8300.36 | 200.73 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-HOSTING] | span | 1024 | 475.06 | 8300.36 | 200.73 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-HOSTING] | span | 768 | 347.06 | 8373.94 | 200.73 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-HOSTING] | span | 390 | 50 | 8587.66 | 314.08 | 55.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 690.06 | 8297.36 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 482.06 | 8297.36 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 354.06 | 8370.94 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 268.83 | 8585.66 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| furnizorul serviciului de e-mail: ; | li | 1440 | 432 | 8339.80 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul serviciului de e-mail: ; | li | 1024 | 224 | 8339.80 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul serviciului de e-mail: ; | li | 768 | 96 | 8413.38 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| furnizorul serviciului de e-mail: ; | li | 390 | 24 | 8655.84 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| [FURNIZOR-EMAIL] | span | 1440 | 711.22 | 8341.80 | 175.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-EMAIL] | span | 1024 | 503.22 | 8341.80 | 175.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-EMAIL] | span | 768 | 375.22 | 8415.38 | 175.14 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [FURNIZOR-EMAIL] | span | 390 | 50 | 8686.44 | 165.78 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 718.22 | 8338.80 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 510.22 | 8338.80 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 382.22 | 8412.38 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 57 | 8684.44 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| contabilul sau firma de contabilitate, pentru do | li | 1440 | 432 | 8381.23 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| contabilul sau firma de contabilitate, pentru do | li | 1024 | 224 | 8381.23 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| contabilul sau firma de contabilitate, pentru do | li | 768 | 96 | 8454.81 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| contabilul sau firma de contabilitate, pentru do | li | 390 | 24 | 8725.03 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| autoritățile publice, atunci când legea o impune | li | 1440 | 432 | 8422.67 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| autoritățile publice, atunci când legea o impune | li | 1024 | 224 | 8422.67 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| autoritățile publice, atunci când legea o impune | li | 768 | 96 | 8496.25 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| autoritățile publice, atunci când legea o impune | li | 390 | 24 | 8794.22 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Nu vindem, nu închiriem și nu comercializăm în n | p | 1440 | 432 | 8472.11 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu vindem, nu închiriem și nu comercializăm în n | p | 1024 | 224 | 8472.11 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu vindem, nu închiriem și nu comercializăm în n | p | 768 | 96 | 8545.69 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Nu vindem, nu închiriem și nu comercializăm în n | p | 390 | 24 | 8871.41 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.4 Transferuri în afara Spațiului Economic Eur | h3 | 1440 | 432 | 8574.98 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.4 Transferuri în afara Spațiului Economic Eur | h3 | 1024 | 224 | 8574.98 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.4 Transferuri în afara Spațiului Economic Eur | h3 | 768 | 96 | 8648.56 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.4 Transferuri în afara Spațiului Economic Eur | h3 | 390 | 24 | 8970.59 | 342 | 60 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Dacă vreunul dintre furnizorii de mai sus preluc | p | 1440 | 432 | 8622.98 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă vreunul dintre furnizorii de mai sus preluc | p | 1024 | 224 | 8622.98 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă vreunul dintre furnizorii de mai sus preluc | p | 768 | 96 | 8696.56 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă vreunul dintre furnizorii de mai sus preluc | p | 390 | 24 | 9046.59 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.5 Drepturile dumneavoastră | h3 | 1440 | 432 | 8788.73 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.5 Drepturile dumneavoastră | h3 | 1024 | 224 | 8788.73 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.5 Drepturile dumneavoastră | h3 | 768 | 96 | 8862.31 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.5 Drepturile dumneavoastră | h3 | 390 | 24 | 9264.16 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Aveți dreptul de: | p | 1440 | 432 | 8836.73 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți dreptul de: | p | 1024 | 224 | 8836.73 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți dreptul de: | p | 768 | 96 | 8910.31 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți dreptul de: | p | 390 | 24 | 9310.16 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| la datele prelucrate; | li | 1440 | 432 | 8886.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la datele prelucrate; | li | 1024 | 224 | 8886.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la datele prelucrate; | li | 768 | 96 | 8959.75 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la datele prelucrate; | li | 390 | 24 | 9357.75 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| acces | strong | 1440 | 458 | 8891.17 | 48.97 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| acces | strong | 1024 | 250 | 8891.17 | 48.97 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| acces | strong | 768 | 122 | 8964.75 | 48.97 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| acces | strong | 390 | 50 | 9361.75 | 46.08 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| a datelor inexacte; | li | 1440 | 432 | 8927.61 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor inexacte; | li | 1024 | 224 | 8927.61 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor inexacte; | li | 768 | 96 | 9001.19 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor inexacte; | li | 390 | 24 | 9397.34 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| rectificare | strong | 1440 | 458 | 8932.61 | 84.20 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| rectificare | strong | 1024 | 250 | 8932.61 | 84.20 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| rectificare | strong | 768 | 122 | 9006.19 | 84.20 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| rectificare | strong | 390 | 50 | 9401.34 | 79.25 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| a datelor („dreptul de a fi uitat"); | li | 1440 | 432 | 8969.05 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor („dreptul de a fi uitat"); | li | 1024 | 224 | 8969.05 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor („dreptul de a fi uitat"); | li | 768 | 96 | 9042.63 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor („dreptul de a fi uitat"); | li | 390 | 24 | 9436.94 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| ștergere | strong | 1440 | 458 | 8974.05 | 68.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| ștergere | strong | 1024 | 250 | 8974.05 | 68.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| ștergere | strong | 768 | 122 | 9047.63 | 68.72 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| ștergere | strong | 390 | 50 | 9440.94 | 64.67 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| a prelucrării; | li | 1440 | 432 | 9010.48 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a prelucrării; | li | 1024 | 224 | 9010.48 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a prelucrării; | li | 768 | 96 | 9084.06 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a prelucrării; | li | 390 | 24 | 9476.53 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| restricționare | strong | 1440 | 458 | 9015.48 | 110.38 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| restricționare | strong | 1024 | 250 | 9015.48 | 110.38 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| restricționare | strong | 768 | 122 | 9089.06 | 110.38 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| restricționare | strong | 390 | 50 | 9480.53 | 103.88 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| a datelor; | li | 1440 | 432 | 9051.92 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor; | li | 1024 | 224 | 9051.92 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor; | li | 768 | 96 | 9125.50 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| a datelor; | li | 390 | 24 | 9516.13 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| portabilitate | strong | 1440 | 458 | 9056.92 | 99.56 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| portabilitate | strong | 1024 | 250 | 9056.92 | 99.56 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| portabilitate | strong | 768 | 122 | 9130.50 | 99.56 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| portabilitate | strong | 390 | 50 | 9520.13 | 93.70 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| la prelucrarea întemeiată pe interes legitim; | li | 1440 | 432 | 9093.36 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la prelucrarea întemeiată pe interes legitim; | li | 1024 | 224 | 9093.36 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la prelucrarea întemeiată pe interes legitim; | li | 768 | 96 | 9166.94 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| la prelucrarea întemeiată pe interes legitim; | li | 390 | 24 | 9555.72 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| opoziție | strong | 1440 | 458 | 9098.36 | 65.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| opoziție | strong | 1024 | 250 | 9098.36 | 65.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| opoziție | strong | 768 | 122 | 9171.94 | 65.58 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| opoziție | strong | 390 | 50 | 9559.72 | 61.72 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| , oricând, fără ca aceasta să afecteze legalitat | li | 1440 | 432 | 9134.80 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , oricând, fără ca aceasta să afecteze legalitat | li | 1024 | 224 | 9134.80 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , oricând, fără ca aceasta să afecteze legalitat | li | 768 | 96 | 9208.38 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , oricând, fără ca aceasta să afecteze legalitat | li | 390 | 24 | 9624.91 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| retragere a consimțământului | strong | 1440 | 458 | 9139.80 | 241.02 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| retragere a consimțământului | strong | 1024 | 250 | 9139.80 | 241.02 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| retragere a consimțământului | strong | 768 | 122 | 9213.38 | 241.02 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| retragere a consimțământului | strong | 390 | 50 | 9628.91 | 226.83 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| de a , inclusiv creare de profiluri. | li | 1440 | 432 | 9207.67 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| de a , inclusiv creare de profiluri. | li | 1024 | 224 | 9207.67 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| de a , inclusiv creare de profiluri. | li | 768 | 96 | 9281.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| de a , inclusiv creare de profiluri. | li | 390 | 24 | 9723.69 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| nu face obiectul unei decizii automate | strong | 1440 | 497.44 | 9212.67 | 310.63 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu face obiectul unei decizii automate | strong | 1024 | 289.44 | 9212.67 | 310.63 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu face obiectul unei decizii automate | strong | 768 | 161.44 | 9286.25 | 310.63 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| nu face obiectul unei decizii automate | strong | 390 | 50 | 9727.69 | 252.67 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Exercitarea acestor drepturi este . Răspundem în | p | 1440 | 432 | 9288.55 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Exercitarea acestor drepturi este . Răspundem în | p | 1024 | 224 | 9288.55 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Exercitarea acestor drepturi este . Răspundem în | p | 768 | 96 | 9362.13 | 576 | 125.75 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Exercitarea acestor drepturi este . Răspundem în | p | 390 | 24 | 9800.88 | 342 | 177.56 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| gratuită | strong | 1440 | 698.50 | 9293.55 | 63.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| gratuită | strong | 1024 | 490.50 | 9293.55 | 63.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| gratuită | strong | 768 | 362.50 | 9367.13 | 63.61 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| gratuită | strong | 390 | 274.83 | 9804.88 | 59.88 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| cel mult o lună | strong | 1440 | 432 | 9293.55 | 569.80 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| cel mult o lună | strong | 1024 | 224 | 9293.55 | 569.80 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| cel mult o lună | strong | 768 | 96 | 9367.13 | 569.80 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| cel mult o lună | strong | 390 | 217.52 | 9834.47 | 112.05 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| Pentru a vă exercita drepturile, scrieți-ne la a | p | 1440 | 432 | 9432.30 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru a vă exercita drepturile, scrieți-ne la a | p | 1024 | 224 | 9432.30 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru a vă exercita drepturile, scrieți-ne la a | p | 768 | 96 | 9505.88 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru a vă exercita drepturile, scrieți-ne la a | p | 390 | 24 | 9996.44 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.6 Dreptul de a depune plângere | h3 | 1440 | 432 | 9535.17 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.6 Dreptul de a depune plângere | h3 | 1024 | 224 | 9535.17 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.6 Dreptul de a depune plângere | h3 | 768 | 96 | 9608.75 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.6 Dreptul de a depune plângere | h3 | 390 | 24 | 10095.63 | 342 | 30 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Dacă apreciați că v-am încălcat drepturile, vă p | p | 1440 | 432 | 9583.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă apreciați că v-am încălcat drepturile, vă p | p | 1024 | 224 | 9583.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă apreciați că v-am încălcat drepturile, vă p | p | 768 | 96 | 9656.75 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Dacă apreciați că v-am încălcat drepturile, vă p | p | 390 | 24 | 10141.63 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | p | 1440 | 432 | 9632.61 | 576 | 220.06 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | p | 1024 | 224 | 9632.61 | 576 | 220.06 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | p | 768 | 96 | 9706.19 | 576 | 220.06 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | p | 390 | 24 | 10218.81 | 342 | 236.75 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Autoritatea Națională de Supraveghere a Prelucră | strong | 1440 | 432 | 9637.61 | 509.78 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autoritatea Națională de Supraveghere a Prelucră | strong | 1024 | 224 | 9637.61 | 509.78 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autoritatea Națională de Supraveghere a Prelucră | strong | 768 | 96 | 9711.19 | 509.78 | 51.44 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autoritatea Națională de Supraveghere a Prelucră | strong | 390 | 24 | 10222.81 | 313.14 | 79.19 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| anspdcp@dataprotection.ro | a | 1440 | 492.39 | 9794.80 | 223.94 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| anspdcp@dataprotection.ro | a | 1024 | 284.39 | 9794.80 | 223.94 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| anspdcp@dataprotection.ro | a | 768 | 156.39 | 9868.38 | 223.94 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| anspdcp@dataprotection.ro | a | 390 | 80.84 | 10400.38 | 210.77 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 1440 | 477.89 | 9826.23 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 1024 | 269.89 | 9826.23 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 768 | 141.89 | 9899.81 | 241.11 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://www.dataprotection.ro | a | 390 | 67.19 | 10429.97 | 226.92 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Aveți, de asemenea, dreptul de a vă adresa insta | p | 1440 | 432 | 9870.67 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți, de asemenea, dreptul de a vă adresa insta | p | 1024 | 224 | 9870.67 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți, de asemenea, dreptul de a vă adresa insta | p | 768 | 96 | 9944.25 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Aveți, de asemenea, dreptul de a vă adresa insta | p | 390 | 24 | 10473.56 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| 12.7 Caracterul obligatoriu al furnizării datelo | h3 | 1440 | 432 | 9973.55 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.7 Caracterul obligatoriu al furnizării datelo | h3 | 1024 | 224 | 9973.55 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.7 Caracterul obligatoriu al furnizării datelo | h3 | 768 | 96 | 10047.13 | 576 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| 12.7 Caracterul obligatoriu al furnizării datelo | h3 | 390 | 24 | 10572.75 | 342 | 60 | 20 | 30 | normal | 400 | #e5e2e1 | start |
| Furnizarea datelor prin formularul de contact es | p | 1440 | 432 | 10021.55 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Furnizarea datelor prin formularul de contact es | p | 1024 | 224 | 10021.55 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Furnizarea datelor prin formularul de contact es | p | 768 | 96 | 10095.13 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Furnizarea datelor prin formularul de contact es | p | 390 | 24 | 10648.75 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-12` | 12. Prelucrarea datelor cu caracter personal | Această secțiune constituie informarea prevăzută | 20 | 20 | 20 | 20 |
| `section#sectiunea-12` | Această secțiune constituie informarea prevăzută | 12.1 Operatorul | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.1 Operatorul | Operatorul datelor este entitatea identificată l | 16 | 16 | 16 | 16 |
| `section#sectiunea-12` | Operatorul datelor este entitatea identificată l | 12.2 Ce date prelucrăm, în ce scop și în ce teme | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.2 Ce date prelucrăm, în ce scop și în ce teme | Glisați lateral pentru a vedea tot tabelul. | n/r | n/r | n/r | 16 |
| `section#sectiunea-12` | Glisați lateral pentru a vedea tot tabelul. | [Categorie de date Scop Temei juridic Dur] | n/r | n/r | n/r | 18 |
| `section#sectiunea-12` | [Categorie de date Scop Temei juridic Dur] | 12.3 Cui transmitem datele | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.3 Cui transmitem datele | Datele pot fi accesate de: | 16 | 16 | 16 | 16 |
| `section#sectiunea-12` | Datele pot fi accesate de: | [furnizorul de găzduire web: valoare de c] | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | [furnizorul de găzduire web: valoare de c] | Nu vindem, nu închiriem și nu comercializăm în n | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | Nu vindem, nu închiriem și nu comercializăm în n | 12.4 Transferuri în afara Spațiului Economic Eur | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.4 Transferuri în afara Spațiului Economic Eur | Dacă vreunul dintre furnizorii de mai sus preluc | 16 | 16 | 16 | 16 |
| `section#sectiunea-12` | Dacă vreunul dintre furnizorii de mai sus preluc | 12.5 Drepturile dumneavoastră | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.5 Drepturile dumneavoastră | Aveți dreptul de: | 16 | 16 | 16 | 16 |
| `section#sectiunea-12` | Aveți dreptul de: | [acces la datele prelucrate; rectificare ] | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | [acces la datele prelucrate; rectificare ] | Exercitarea acestor drepturi este . Răspundem în | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | Exercitarea acestor drepturi este . Răspundem în | Pentru a vă exercita drepturile, scrieți-ne la a | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | Pentru a vă exercita drepturile, scrieți-ne la a | 12.6 Dreptul de a depune plângere | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.6 Dreptul de a depune plângere | Dacă apreciați că v-am încălcat drepturile, vă p | 16 | 16 | 16 | 16 |
| `section#sectiunea-12` | Dacă apreciați că v-am încălcat drepturile, vă p | B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | B-dul G-ral. Gheorghe Magheru nr. 28-30, Sector  | Aveți, de asemenea, dreptul de a vă adresa insta | 18 | 18 | 18 | 18 |
| `section#sectiunea-12` | Aveți, de asemenea, dreptul de a vă adresa insta | 12.7 Caracterul obligatoriu al furnizării datelo | 40 | 40 | 40 | 40 |
| `section#sectiunea-12` | 12.7 Caracterul obligatoriu al furnizării datelo | Furnizarea datelor prin formularul de contact es | 16 | 16 | 16 | 16 |
| `table.legal-table` | [Categorie de date Scop Temei juridic Dur] | [Nume, telefon, e-mail, data și tipul eve] | 0 | 0 | 0 | 0 |
| `tr` | Categorie de date | Scop | -47.39 ¹ | -47.39 ¹ | -69.78 ¹ | -69.78 ¹ |
| `tr` | Scop | Temei juridic | -47.39 ¹ | -47.39 ¹ | -69.78 ¹ | -69.78 ¹ |
| `tr` | Temei juridic | Durată de stocare | -47.39 ¹ | -47.39 ¹ | -69.78 ¹ | -69.78 ¹ |
| `tbody` | [Nume, telefon, e-mail, data și tipul eve] | [Date de identificare și de facturare Exe] | 0 | 0 | 0 | 0 |
| `tbody` | [Date de identificare și de facturare Exe] | [Documente financiar-contabile Îndeplinir] | 0 | 0 | 0 | 0 |
| `tbody` | [Documente financiar-contabile Îndeplinir] | [Fotografii și înregistrări de la evenime] | 0 | 0 | 0 | 0 |
| `tbody` | [Fotografii și înregistrări de la evenime] | [Adresă IP, date tehnice de acces la serv] | 0 | 0 | 0 | 0 |
| `tr` | Nume, telefon, e-mail, data și tipul evenimentul | Răspuns la solicitare, verificare disponibilitat | -152.97 ¹ | -152.97 ¹ | -178.56 ¹ | -178.56 ¹ |
| `tr` | Răspuns la solicitare, verificare disponibilitat | Art. 6 alin. (1) lit. b) GDPR — demersuri precon | -152.97 ¹ | -152.97 ¹ | -178.56 ¹ | -178.56 ¹ |
| `tr` | Art. 6 alin. (1) lit. b) GDPR — demersuri precon | 12 luni de la ultima interacțiune, dacă nu se în | -152.97 ¹ | -152.97 ¹ | -178.56 ¹ | -178.56 ¹ |
| `tr` | Date de identificare și de facturare | Executarea contractului de prestări servicii | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.79 ¹ |
| `tr` | Executarea contractului de prestări servicii | Art. 6 alin. (1) lit. b) GDPR | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.79 ¹ |
| `tr` | Art. 6 alin. (1) lit. b) GDPR | Pe durata contractului | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.79 ¹ |
| `tr` | Documente financiar-contabile | Îndeplinirea obligațiilor legale contabile și fi | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `tr` | Îndeplinirea obligațiilor legale contabile și fi | Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `tr` | Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege | 10 ani, conform legii contabilității | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `tr` | Fotografii și înregistrări de la eveniment, folo | Promovarea activității artistice | -101.78 ¹ | -101.78 ¹ | -127.38 ¹ | -127.37 ¹ |
| `tr` | Promovarea activității artistice | Art. 6 alin. (1) lit. a) GDPR — consimțământ | -101.78 ¹ | -101.78 ¹ | -127.38 ¹ | -127.37 ¹ |
| `tr` | Art. 6 alin. (1) lit. a) GDPR — consimțământ | Până la retragerea consimțământului | -101.78 ¹ | -101.78 ¹ | -127.38 ¹ | -127.37 ¹ |
| `tr` | Adresă IP, date tehnice de acces la server | Securitatea și funcționarea site-ului | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `tr` | Securitatea și funcționarea site-ului | Art. 6 alin. (1) lit. f) GDPR — interes legitim | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `tr` | Art. 6 alin. (1) lit. f) GDPR — interes legitim | Maximum 30 de zile | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ | -101.78 ¹ |
| `ul.motif-list` | furnizorul de găzduire web: ; | furnizorul serviciului de e-mail: ; | 10 | 10 | 10 | 10 |
| `ul.motif-list` | furnizorul serviciului de e-mail: ; | contabilul sau firma de contabilitate, pentru do | 10 | 10 | 10 | 10 |
| `ul.motif-list` | contabilul sau firma de contabilitate, pentru do | autoritățile publice, atunci când legea o impune | 10 | 10 | 10 | 10 |
| `ul.motif-list` | la datele prelucrate; | a datelor inexacte; | 10 | 10 | 10 | 10 |
| `ul.motif-list` | a datelor inexacte; | a datelor („dreptul de a fi uitat"); | 10 | 10 | 10 | 10 |
| `ul.motif-list` | a datelor („dreptul de a fi uitat"); | a prelucrării; | 10 | 10 | 10 | 10 |
| `ul.motif-list` | a prelucrării; | a datelor; | 10 | 10 | 10 | 10 |
| `ul.motif-list` | a datelor; | la prelucrarea întemeiată pe interes legitim; | 10 | 10 | 10 | 10 |
| `ul.motif-list` | la prelucrarea întemeiată pe interes legitim; | , oricând, fără ca aceasta să afecteze legalitat | 10 | 10 | 10 | 10 |
| `ul.motif-list` | , oricând, fără ca aceasta să afecteze legalitat | de a , inclusiv creare de profiluri. | 10 | 10 | 10 | 10 |
| `p` | gratuită | cel mult o lună | -20 | -20 | -20 | 9.59 |
| `p` | Autoritatea Națională de Supraveghere a Prelucră | anspdcp@dataprotection.ro | 105.75 | 105.75 | 105.75 | 98.38 |
| `p` | anspdcp@dataprotection.ro | https://www.dataprotection.ro | 11.43 | 11.43 | 11.43 | 9.59 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S28 — div.motif-separator

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

## S29 — 13. Cookie-uri (#sectiunea-13)

`section#sectiunea-13` · clase: `mb-12 md:mb-16`

Titlu: «13. Cookie-uri»

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
| └ coloana 1 (`a`) | 1440 | 170.20 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 1024 | 170.20 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 768 | 170.20 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a`) | 390 | 160.19 | 20 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 13. Cookie-uri | h2 | 1440 | 432 | 10267.86 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 13. Cookie-uri | h2 | 1024 | 224 | 10267.86 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 13. Cookie-uri | h2 | 768 | 96 | 10341.44 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 13. Cookie-uri | h2 | 390 | 24 | 10887.13 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Utilizarea modulelor cookie este descrisă în , c | p | 1440 | 432 | 10327.86 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea modulelor cookie este descrisă în , c | p | 1024 | 224 | 10327.86 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea modulelor cookie este descrisă în , c | p | 768 | 96 | 10401.44 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Utilizarea modulelor cookie este descrisă în , c | p | 390 | 24 | 10937.13 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Politica de cookie-uri | a | 1440 | 786.23 | 10332.86 | 170.20 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Politica de cookie-uri | a | 1024 | 578.23 | 10332.86 | 170.20 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Politica de cookie-uri | a | 768 | 450.23 | 10406.44 | 170.20 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| Politica de cookie-uri | a | 390 | 24 | 10970.72 | 160.19 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-13` | 13. Cookie-uri | Utilizarea modulelor cookie este descrisă în , c | 20 | 20 | 20 | 20 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S30 — div.motif-separator

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

## S31 — 14. Soluționarea litigiilor (#sectiunea-14)

`section#sectiunea-14` · clase: `mb-12 md:mb-16`

Titlu: «14. Soluționarea litigiilor»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 456.38 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 456.38 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 456.38 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 575.91 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 59.19 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 1440 | 576 | 135.75 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 1024 | 576 | 135.75 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 768 | 576 | 135.75 | 0/0/0/0 | transparent | none |
| **container 4** (`ul.motif-list`) | 390 | 342 | 187.56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 1 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1440 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 1024 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 768 | 576 | 62.88 | 0/0/0/26 |  +bg-image | none |
| └ coloana 2 (`li`) | 390 | 342 | 88.78 | 0/0/0/26 |  +bg-image | none |
| **container 5** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 342 | 147.97 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 1440 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 1024 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 768 | 576 | 31.44 | 0/0/0/0 | transparent | none |
| **container 6** (`p`) | 390 | 342 | 29.59 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 14. Soluționarea litigiilor | h2 | 1440 | 432 | 10542.73 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 14. Soluționarea litigiilor | h2 | 1024 | 224 | 10542.73 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 14. Soluționarea litigiilor | h2 | 768 | 96 | 10616.31 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 14. Soluționarea litigiilor | h2 | 390 | 24 | 11145.91 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Orice neînțelegere se rezolvă, pe cât posibil, p | p | 1440 | 432 | 10602.73 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice neînțelegere se rezolvă, pe cât posibil, p | p | 1024 | 224 | 10602.73 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice neînțelegere se rezolvă, pe cât posibil, p | p | 768 | 96 | 10676.31 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Orice neînțelegere se rezolvă, pe cât posibil, p | p | 390 | 24 | 11195.91 | 342 | 59.19 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| În calitate de consumator, vă puteți adresa: | p | 1440 | 432 | 10652.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În calitate de consumator, vă puteți adresa: | p | 1024 | 224 | 10652.17 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În calitate de consumator, vă puteți adresa: | p | 768 | 96 | 10725.75 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| În calitate de consumator, vă puteți adresa: | p | 390 | 24 | 11273.09 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| — | li | 1440 | 432 | 10701.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| — | li | 1024 | 224 | 10701.61 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| — | li | 768 | 96 | 10775.19 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| — | li | 390 | 24 | 11320.69 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Autorității Naționale pentru Protecția Consumato | strong | 1440 | 458 | 10706.61 | 496.98 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale pentru Protecția Consumato | strong | 1024 | 250 | 10706.61 | 496.98 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale pentru Protecția Consumato | strong | 768 | 122 | 10780.19 | 496.98 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Autorității Naționale pentru Protecția Consumato | strong | 390 | 50 | 11324.69 | 282.20 | 49.59 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://anpc.ro | a | 1440 | 458 | 10738.05 | 118.64 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro | a | 1024 | 250 | 10738.05 | 118.64 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro | a | 768 | 122 | 10811.63 | 118.64 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro | a | 390 | 50 | 11383.88 | 111.66 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| , în temeiul OG nr. 38/2015 — | li | 1440 | 432 | 10774.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , în temeiul OG nr. 38/2015 — | li | 1024 | 224 | 10774.48 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , în temeiul OG nr. 38/2015 — | li | 768 | 96 | 10848.06 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| , în temeiul OG nr. 38/2015 — | li | 390 | 24 | 11419.47 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Soluționării Alternative a Litigiilor (SAL) | strong | 1440 | 458 | 10779.48 | 321.22 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Soluționării Alternative a Litigiilor (SAL) | strong | 1024 | 250 | 10779.48 | 321.22 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Soluționării Alternative a Litigiilor (SAL) | strong | 768 | 122 | 10853.06 | 321.22 | 20 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| Soluționării Alternative a Litigiilor (SAL) | strong | 390 | 50 | 11423.47 | 302.33 | 20 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| https://anpc.ro/ce-este-sal/ | a | 1440 | 479.78 | 10810.92 | 222.97 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro/ce-este-sal/ | a | 1024 | 271.78 | 10810.92 | 222.97 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro/ce-este-sal/ | a | 768 | 143.78 | 10884.50 | 222.97 | 20 | 17 | 31.45 | normal | 400 | #e5e2e1 | start |
| https://anpc.ro/ce-este-sal/ | a | 390 | 50 | 11482.66 | 209.86 | 20 | 16 | 29.60 | normal | 400 | #e5e2e1 | start |
| Litigiile nesoluționate amiabil sunt de competen | p | 1440 | 432 | 10855.36 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Litigiile nesoluționate amiabil sunt de competen | p | 1024 | 224 | 10855.36 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Litigiile nesoluționate amiabil sunt de competen | p | 768 | 96 | 10928.94 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Litigiile nesoluționate amiabil sunt de competen | p | 390 | 24 | 11526.25 | 342 | 147.97 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Legea aplicabilă este legea română. | p | 1440 | 432 | 10967.67 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Legea aplicabilă este legea română. | p | 1024 | 224 | 10967.67 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Legea aplicabilă este legea română. | p | 768 | 96 | 11041.25 | 576 | 31.44 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Legea aplicabilă este legea română. | p | 390 | 24 | 11692.22 | 342 | 29.59 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-14` | 14. Soluționarea litigiilor | Orice neînțelegere se rezolvă, pe cât posibil, p | 20 | 20 | 20 | 20 |
| `section#sectiunea-14` | Orice neînțelegere se rezolvă, pe cât posibil, p | În calitate de consumator, vă puteți adresa: | 18 | 18 | 18 | 18 |
| `section#sectiunea-14` | În calitate de consumator, vă puteți adresa: | [Autorității Naționale pentru Protecția C] | 18 | 18 | 18 | 18 |
| `section#sectiunea-14` | [Autorității Naționale pentru Protecția C] | Litigiile nesoluționate amiabil sunt de competen | 18 | 18 | 18 | 18 |
| `section#sectiunea-14` | Litigiile nesoluționate amiabil sunt de competen | Legea aplicabilă este legea română. | 18 | 18 | 18 | 18 |
| `ul.motif-list` | — | , în temeiul OG nr. 38/2015 — | 10 | 10 | 10 | 10 |
| `li` | Autorității Naționale pentru Protecția Consumato | https://anpc.ro | 11.44 | 11.44 | 11.44 | 9.60 |
| `li` | Soluționării Alternative a Litigiilor (SAL) | https://anpc.ro/ce-este-sal/ | 11.44 | 11.44 | 11.44 | 39.19 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S32 — div.motif-separator

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

## S33 — 15. Modificarea termenilor (#sectiunea-15)

`section#sectiunea-15` · clase: `mb-12 md:mb-16`

Titlu: «15. Modificarea termenilor»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 235.19 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 304.75 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 576 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1440 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 1024 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 768 | 576 | 94.31 | 0/0/0/0 | transparent | none |
| **container 2** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 576 | 62.88 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 342 | 118.38 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 15. Modificarea termenilor | h2 | 1440 | 432 | 11151.11 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 15. Modificarea termenilor | h2 | 1024 | 224 | 11151.11 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 15. Modificarea termenilor | h2 | 768 | 96 | 11224.69 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 15. Modificarea termenilor | h2 | 390 | 24 | 11841.81 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Ne rezervăm dreptul de a modifica prezentele con | p | 1440 | 432 | 11211.11 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne rezervăm dreptul de a modifica prezentele con | p | 1024 | 224 | 11211.11 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne rezervăm dreptul de a modifica prezentele con | p | 768 | 96 | 11284.69 | 576 | 94.31 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Ne rezervăm dreptul de a modifica prezentele con | p | 390 | 24 | 11891.81 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| Modificările produc efecte de la data publicării | p | 1440 | 432 | 11323.42 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Modificările produc efecte de la data publicării | p | 1024 | 224 | 11323.42 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Modificările produc efecte de la data publicării | p | 768 | 96 | 11397 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Modificările produc efecte de la data publicării | p | 390 | 24 | 12028.19 | 342 | 118.38 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-15` | 15. Modificarea termenilor | Ne rezervăm dreptul de a modifica prezentele con | 20 | 20 | 20 | 20 |
| `section#sectiunea-15` | Ne rezervăm dreptul de a modifica prezentele con | Modificările produc efecte de la data publicării | 18 | 18 | 18 | 18 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S34 — div.motif-separator

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

## S35 — 16. Contact (#sectiunea-16)

`section#sectiunea-16` · clase: `mb-12 md:mb-16`

Eyebrow: «[EMAIL-OFICIAL]»

Titlu: «16. Contact»

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
| └ coloana 2 (`span.legal-tbc`) | 1440 | 106.08 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 1024 | 106.08 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 768 | 106.08 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |
| └ coloana 2 (`span.legal-tbc`) | 390 | 100.78 | 26 | 1/6/1/6 | #c41236 @0.18 | T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16. Contact | h2 | 1440 | 432 | 11538.30 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 16. Contact | h2 | 1024 | 224 | 11538.30 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 16. Contact | h2 | 768 | 96 | 11611.88 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| 16. Contact | h2 | 390 | 24 | 12266.56 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Pentru orice întrebare privind prezentele condiț | p | 1440 | 432 | 11598.30 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind prezentele condiț | p | 1024 | 224 | 11598.30 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind prezentele condiț | p | 768 | 96 | 11671.88 | 576 | 62.88 | 17 | 31.45 | normal | 400 | #c4c7c7 | start |
| Pentru orice întrebare privind prezentele condiț | p | 390 | 24 | 12316.56 | 342 | 88.78 | 16 | 29.60 | normal | 400 | #c4c7c7 | start |
| [EMAIL-OFICIAL] | span | 1440 | 432 | 11631.73 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 1024 | 224 | 11631.73 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 768 | 96 | 11705.31 | 155 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [EMAIL-OFICIAL] | span | 390 | 217.34 | 12347.16 | 146.83 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 439 | 11628.73 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 231 | 11628.73 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 103 | 11702.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 224.34 | 12345.16 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 1440 | 761.95 | 11631.73 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 1024 | 553.95 | 11631.73 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 768 | 425.95 | 11705.31 | 106.08 | 26 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| [TELEFON] | span | 390 | 184.16 | 12376.75 | 100.78 | 26 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1440 | 768.95 | 11628.73 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 1024 | 560.95 | 11628.73 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 768 | 432.95 | 11702.31 | 1 | 1 | 17 | 31.45 | normal | 600 | #e5e2e1 | start |
| valoare de completat: | span | 390 | 191.16 | 12374.75 | 1 | 1 | 16 | 29.60 | normal | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#sectiunea-16` | 16. Contact | Pentru orice întrebare privind prezentele condiț | 20 | 20 | 20 | 20 |
| `p` | [EMAIL-OFICIAL] | [TELEFON] | -26 ¹ | -26 ¹ | -26 ¹ | 3.59 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S36 — div.motif-separator

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

## S37 — Document elaborat în conformitate cu: Regulame

`p` · clase: `italic font-body-md text-[15px] md:text-body-md text-on-surface-variant leading-relaxed`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **section** | 768 | 576 | 157.19 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 236.75 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele**: sectiunea nu contine elemente cu text propriu sau media.

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Termeni și condiții» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[30px]`; weight rezolvat 400/500, font-size masurat 30/48px
- `h2` «1. Identificarea operatorului» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «2. Obiectul site-ului» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «3. Acceptarea termenilor» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «4. Informațiile publicate. Prețuri» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «5. Rezervarea și încheierea contractului» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «6. Deplasarea» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «7. Modificarea și anularea rezervării» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «8. Drepturi de proprietate intelectuală» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «9. Materiale audio-video de la evenimente» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «10. Limitarea răspunderii» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «11. Linkuri către site-uri terțe» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «12. Prelucrarea datelor cu caracter personal» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «12.1 Operatorul» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «12.2 Ce date prelucrăm, în ce scop și în ce teme» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `p` «Glisați lateral pentru a vedea tot tabelul.» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[14px]`; weight rezolvat 400, font-size masurat 16px
- `h3` «12.3 Cui transmitem datele» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «12.4 Transferuri în afara Spațiului Economic Eur» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «12.5 Drepturile dumneavoastră» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «12.6 Dreptul de a depune plângere» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h3` «12.7 Caracterul obligatoriu al furnizării datelo» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[20px]`; weight rezolvat 400/500, font-size masurat 20/24px
- `h2` «13. Cookie-uri» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «14. Soluționarea litigiilor» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «15. Modificarea termenilor» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «16. Contact» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `p` «Document elaborat în conformitate cu: Regulament» — `font-body-md` (tokenul poarta weight) + marime arbitrara `text-[15px]`; weight rezolvat 400, font-size masurat 16/17px

### Borduri care vin din `assets/styles.css`, nu din clase

- `aside.legal-draft-banner` «[Document în lucru — nu este în vigoare T]» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 6px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[EXEMPLU]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[DATA-PUBLICARE]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `details#cuprins` «[Cuprins 1. Identificarea operatorului 2.]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[DENUMIRE-FIRMĂ-EXACTĂ]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[CUI]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[NR-REG-COM]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[ADRESĂ-SEDIU-SOCIAL]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[EMAIL-OFICIAL]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[TELEFON]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[TARIF]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Categorie de date» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Scop» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Temei juridic» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `th` «Durată de stocare» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Nume, telefon, e-mail, data și tipul evenimentul» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Răspuns la solicitare, verificare disponibilitat» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Art. 6 alin. (1) lit. b) GDPR — demersuri precon» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «12 luni de la ultima interacțiune, dacă nu se în» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Date de identificare și de facturare» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Executarea contractului de prestări servicii» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Art. 6 alin. (1) lit. b) GDPR» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Pe durata contractului» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Documente financiar-contabile» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Îndeplinirea obligațiilor legale contabile și fi» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Art. 6 alin. (1) lit. c) GDPR, coroborat cu Lege» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «10 ani, conform legii contabilității» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Fotografii și înregistrări de la eveniment, folo» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Promovarea activității artistice» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Art. 6 alin. (1) lit. a) GDPR — consimțământ» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Până la retragerea consimțământului» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Adresă IP, date tehnice de acces la server» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Securitatea și funcționarea site-ului» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Art. 6 alin. (1) lit. f) GDPR — interes legitim» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `td` «Maximum 30 de zile» — T 1px #c6c6c6 @0.18, R 1px #c6c6c6 @0.18, B 1px #c6c6c6 @0.18, L 1px #c6c6c6 @0.18, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[FURNIZOR-HOSTING]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.legal-tbc` «[FURNIZOR-EMAIL]» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «[Categorie de date Scop Temei juridic Dur]» declara `mb-*` ∈ {20}px, dar distanta reala pana la «12.3 Cui transmitem datele» e 40px la 1440
- «[Categorie de date Scop Temei juridic Dur]» declara `mb-*` ∈ {20}px, dar distanta reala pana la «12.3 Cui transmitem datele» e 40px la 1024
- «[Categorie de date Scop Temei juridic Dur]» declara `mb-*` ∈ {20}px, dar distanta reala pana la «12.3 Cui transmitem datele» e 40px la 768
- «[Categorie de date Scop Temei juridic Dur]» declara `mb-*` ∈ {20}px, dar distanta reala pana la «12.3 Cui transmitem datele» e 40px la 390

### Elemente care nu se randeaza la un viewport

- `p.md:hidden` «Glisați lateral pentru a vedea tot tabelul.» — `getClientRects().length == 0` la 1440, 1024, 768 (randat la 390); `display` raportat: none

### Suprapuneri intre elemente

- in `li`: «[DENUMIRE-FIRMĂ-EXACTĂ]» si «Denumire:» se suprapun pe verticala cu 52.59px la 390 (suprapunere orizontala 79.77px, position relative/static) — **ambele in flux normal**
- in `li`: «[ADRESĂ-SEDIU-SOCIAL]» si «Sediu social:» se suprapun pe verticala cu 52.59px la 390 (suprapunere orizontala 98.39px, position relative/static) — **ambele in flux normal**
- in `p`: «cel mult o lună» si «gratuită» se suprapun pe verticala cu 51.43px la 1440 (suprapunere orizontala 63.61px, position static/static) — **ambele in flux normal**
- in `p`: «cel mult o lună» si «gratuită» se suprapun pe verticala cu 51.43px la 1024 (suprapunere orizontala 63.61px, position static/static) — **ambele in flux normal**
- in `p`: «cel mult o lună» si «gratuită» se suprapun pe verticala cu 51.43px la 768 (suprapunere orizontala 63.61px, position static/static) — **ambele in flux normal**


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| [EXEMPLU] | 1440: 528 · 1024: 528 · 768: 528 · 390: 294 | vert (sectiune): 20 sus / 20 jos<br>oriz (container): 24 L / 24 R | — | — | o singura coloana |
| Termeni și condiții | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| cuprins | 1440: 528 · 1024: 528 · 768: 528 · 390: 302 | vert (sectiune): 1440: 24 sus / 24 jos · 1024: 24 sus / 24 jos · 768: 24 sus / 24 jos · 390: 20 sus / 20 jos<br>oriz (container): 1440: 24 L / 24 R · 1024: 24 L / 24 R · 768: 24 L / 24 R · 390: 20 L / 20 R | — | — | o singura coloana |
| 1. Identificarea operatorului (#sectiunea-1) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 2. Obiectul site-ului (#sectiunea-2) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 3. Acceptarea termenilor (#sectiunea-3) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 4. Informațiile publicate. Prețuri (#sectiunea-4) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 5. Rezervarea și încheierea contractului (#sectiunea-5) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 6. Deplasarea (#sectiunea-6) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 7. Modificarea și anularea rezervării (#sectiunea-7) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 8. Drepturi de proprietate intelectuală (#sectiunea-8) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 9. Materiale audio-video de la evenimente (#sectiunea-9) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 10. Limitarea răspunderii (#sectiunea-10) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 11. Linkuri către site-uri terțe (#sectiunea-11) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 12. Prelucrarea datelor cu caracter personal (#sectiunea-12) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 13. Cookie-uri (#sectiunea-13) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 14. Soluționarea litigiilor (#sectiunea-14) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 15. Modificarea termenilor (#sectiunea-15) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| 16. Contact (#sectiunea-16) | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| div.motif-separator | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Document elaborat în conformitate cu: Regulame | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
