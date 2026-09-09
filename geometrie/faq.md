# Geometrie randata — `faq.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/faq.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 3573 | 128/0/96/0 | transparent | none |
| `<main>` | 1024 | 1024 | 3573 | 128/0/96/0 | transparent | none |
| `<main>` | 768 | 768 | 3573 | 128/0/96/0 | transparent | none |
| `<main>` | 390 | 390 | 3311 | 96/0/64/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 4004px, 1024 → 4004px, 768 → 4050px, 390 → 3898px.

Sectiuni masurate: **8**.

---

## S1 — Ce ne întrebați cel mai des

`header` · clase: `mb-8 md:mb-10 text-center`

Eyebrow: «Întrebări frecvente»

Titlu: «Ce ne întrebați cel mai des»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 216 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 216 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 216 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 245.50 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 1440 | 704 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 1024 | 704 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 768 | 704 | 20 | 0/0/0/0 | transparent | none |
| **container 1** (`span.font-label-md`) | 390 | 342 | 20 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1440 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1024 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 768 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 390 | 342 | 37.50 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-lg`) | 1440 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-lg`) | 1024 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-lg`) | 768 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 3** (`p.font-body-lg`) | 390 | 342 | 104 | 0/0/0/0 | transparent | none |
| **container 4** (`div.motif-rule`) | 1440 | 220 | 24 | 0/0/0/0 | transparent | none |
| **container 4** (`div.motif-rule`) | 1024 | 220 | 24 | 0/0/0/0 | transparent | none |
| **container 4** (`div.motif-rule`) | 768 | 220 | 24 | 0/0/0/0 | transparent | none |
| **container 4** (`div.motif-rule`) | 390 | 220 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.motif-rule__gem`) | 1440 | 16.97 | 16.97 | 0/0/0/0 | transparent | T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020 |
| └ coloana 1 (`span.motif-rule__gem`) | 1024 | 16.97 | 16.97 | 0/0/0/0 | transparent | T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020 |
| └ coloana 1 (`span.motif-rule__gem`) | 768 | 16.97 | 16.97 | 0/0/0/0 | transparent | T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020 |
| └ coloana 1 (`span.motif-rule__gem`) | 390 | 16.97 | 16.97 | 0/0/0/0 | transparent | T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Întrebări frecvente | span | 1440 | 368 | 128 | 704 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Întrebări frecvente | span | 1024 | 160 | 128 | 704 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Întrebări frecvente | span | 768 | 32 | 128 | 704 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Întrebări frecvente | span | 390 | 24 | 96 | 342 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | center |
| Ce ne întrebați cel mai des | h1 | 1440 | 368 | 160 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h1 | 1024 | 160 | 160 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h1 | 768 | 32 | 160 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Ce ne întrebați cel mai des | h1 | 390 | 24 | 128 | 342 | 37.50 | 30 | 37.50 | normal | 400 | #e5e2e1 | center |
| Rezervare, program, cerințe tehnice, deplasare ș | p | 1440 | 368 | 236 | 704 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Rezervare, program, cerințe tehnice, deplasare ș | p | 1024 | 160 | 236 | 704 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Rezervare, program, cerințe tehnice, deplasare ș | p | 768 | 32 | 236 | 704 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Rezervare, program, cerințe tehnice, deplasare ș | p | 390 | 24 | 185.50 | 342 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `header.mb-8` | Întrebări frecvente | Ce ne întrebați cel mai des | 12 | 12 | 12 | 12 |
| `header.mb-8` | Ce ne întrebați cel mai des | Rezervare, program, cerințe tehnice, deplasare ș | 20 | 20 | 20 | 20 |
| `header.mb-8` | Rezervare, program, cerințe tehnice, deplasare ș | div.motif-rule | 28 | 28 | 28 | 28 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S2 — Preț

`nav` · clase: `mb-12 md:mb-16`

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 96 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 96 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 96 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 148 | 0/0/0/0 | transparent | none |
| **container interior** | 1440 | 704 | 96 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 704 | 96 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 704 | 96 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 342 | 148 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1440 | 75.48 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 1024 | 75.48 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 768 | 75.48 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`li`) | 390 | 75.48 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 1440 | 243.73 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 1024 | 243.73 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 768 | 243.73 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`li`) | 390 | 243.73 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 1440 | 123.77 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 1024 | 123.77 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 768 | 123.77 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 3 (`li`) | 390 | 123.77 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 1440 | 190.84 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 1024 | 190.84 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 768 | 190.84 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 4 (`li`) | 390 | 190.84 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 5 (`li`) | 1440 | 128.94 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 5 (`li`) | 1024 | 128.94 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 5 (`li`) | 768 | 128.94 | 44 | 0/0/0/0 | transparent | none |
| └ coloana 5 (`li`) | 390 | 128.94 | 44 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Preț | a | 1440 | 391.08 | 384 | 75.48 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Preț | a | 1024 | 183.08 | 384 | 75.48 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Preț | a | 768 | 55.08 | 384 | 75.48 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Preț | a | 390 | 31.39 | 373.50 | 75.48 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Rezervare și contract | a | 1440 | 474.56 | 384 | 243.73 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Rezervare și contract | a | 1024 | 266.56 | 384 | 243.73 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Rezervare și contract | a | 768 | 138.56 | 384 | 243.73 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Rezervare și contract | a | 390 | 114.88 | 373.50 | 243.73 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Prestația | a | 1440 | 726.30 | 384 | 123.77 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Prestația | a | 1024 | 518.30 | 384 | 123.77 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Prestația | a | 768 | 390.30 | 384 | 123.77 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Prestația | a | 390 | 33.69 | 425.50 | 123.77 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tehnic și locație | a | 1440 | 858.06 | 384 | 190.84 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tehnic și locație | a | 1024 | 650.06 | 384 | 190.84 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tehnic și locație | a | 768 | 522.06 | 384 | 190.84 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Tehnic și locație | a | 390 | 165.45 | 425.50 | 190.84 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Deplasare | a | 1440 | 655.53 | 436 | 128.94 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Deplasare | a | 1024 | 447.53 | 436 | 128.94 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Deplasare | a | 768 | 319.53 | 436 | 128.94 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |
| Deplasare | a | 390 | 130.53 | 477.50 | 128.94 | 44 | 14 | 20 | 1.40 | 600 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `ul.flex` | [Preț] | [Rezervare și contract] | -44 ¹ | -44 ¹ | -44 ¹ | -44 ¹ |
| `ul.flex` | [Rezervare și contract] | [Prestația] | -44 ¹ | -44 ¹ | -44 ¹ | 8 |
| `ul.flex` | [Prestația] | [Tehnic și locație] | -44 ¹ | -44 ¹ | -44 ¹ | -44 ¹ |
| `ul.flex` | [Tehnic și locație] | [Deplasare] | 8 ¹ | 8 ¹ | 8 ¹ | 8 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `ul.flex` | 1440 | flex | 75.48 + 243.73 + 123.77 + 190.84 + 128.94 | 8px | 8px | da (44) |
| `ul.flex` | 1024 | flex | 75.48 + 243.73 + 123.77 + 190.84 + 128.94 | 8px | 8px | da (44) |
| `ul.flex` | 768 | flex | 75.48 + 243.73 + 123.77 + 190.84 + 128.94 | 8px | 8px | da (44) |
| `ul.flex` | 390 | flex | 75.48 + 243.73 + 123.77 + 190.84 + 128.94 | 8px | 8px | da (44) |

---

## S3 — Preț (#pret)

`section#pret` · clase: `mb-14 md:mb-20`

Titlu: «Preț»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 290 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 290 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 290 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 330 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`div.motif-separator`) | 1440 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 1024 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 768 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 3** (`div.space-y-4`) | 1440 | 704 | 178 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 1024 | 704 | 178 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 768 | 704 | 178 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 390 | 342 | 232 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.faq-item`) | 1440 | 704 | 178 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 1024 | 704 | 178 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 768 | 704 | 178 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 390 | 342 | 232 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Preț | h2 | 1440 | 368 | 544 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Preț | h2 | 1024 | 160 | 544 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Preț | h2 | 768 | 32 | 544 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Preț | h2 | 390 | 24 | 569.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 1440 | 393 | 681 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 1024 | 185 | 681 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 768 | 57 | 681 | 390.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Prețul unei formații pentru 2026-2027? | h3 | 390 | 45 | 688.50 | 256.84 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 689 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 689 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 689 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 691.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1440 | 369 | 737 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 1024 | 161 | 737 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 768 | 33 | 737 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Prețul depinde de pachet, de tipul evenimentului | div | 390 | 25 | 730.50 | 340 | 168 | 16 | 24 | normal | 400 | #c6c6c6 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#pret` | Preț | div.motif-separator | 16 | 16 | 16 | 16 |
| `section#pret` | div.motif-separator | [Prețul unei formații pentru 2026-2027? P] | 32 | 32 | 32 | 28 |
| `details.group` | [Prețul unei formații pentru 2026-2027?] | Prețul depinde de pachet, de tipul evenimentului | 0 | 0 | 0 | 0 |
| `summary.flex` | Prețul unei formații pentru 2026-2027? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 390.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 256.84 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |

---

## S4 — Rezervare și contract (#rezervare-si-contract)

`section#rezervare-si-contract` · clase: `mb-14 md:mb-20`

Eyebrow: «Răspuns de confirmat»

Titlu: «Rezervare și contract»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 446 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`div.motif-separator`) | 1440 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 1024 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 768 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 3** (`div.space-y-4`) | 1440 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 1024 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 768 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 390 | 342 | 348 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Rezervare și contract | h2 | 1440 | 368 | 914 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rezervare și contract | h2 | 1024 | 160 | 914 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rezervare și contract | h2 | 768 | 32 | 914 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rezervare și contract | h2 | 390 | 24 | 955.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 1440 | 393 | 1051 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 1024 | 185 | 1051 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 768 | 57 | 1051 | 368.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum rezerv data — avans și contract? | h3 | 390 | 45 | 1074.50 | 243.53 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1059 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1059 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1059 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1077.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Data se blochează pe bază de contract și un avan | div | 1440 | 369 | 1107 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 1024 | 161 | 1107 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 768 | 33 | 1107 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Data se blochează pe bază de contract și un avan | div | 390 | 25 | 1116.50 | 340 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cât este avansul și când se achită restul? | h3 | 1440 | 393 | 1149 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 1024 | 185 | 1149 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 768 | 57 | 1149 | 387.84 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât este avansul și când se achită restul? | h3 | 390 | 45 | 1154.50 | 255.17 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1157 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1157 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1157 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1157.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 1440 | 393 | 1205 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 1024 | 185 | 1205 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 768 | 57 | 1205 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Avansul se achită la semnarea contractului și bl | span | 390 | 45 | 1196.50 | 300 | 167.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 1219 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 1219 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 1219 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 1210.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 1440 | 393 | 1247 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 1024 | 185 | 1247 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 768 | 57 | 1247 | 486.22 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă dacă trebuie să amân evenimentul? | h3 | 390 | 45 | 1234.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1255 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1255 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1255 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1248.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 1440 | 393 | 1303 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 1024 | 185 | 1303 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 768 | 57 | 1303 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Amânarea se discută direct cu noi și se consemne | span | 390 | 45 | 1298.50 | 300 | 167.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 1317 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 1317 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 1317 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 1312.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 1440 | 393 | 1345 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 1024 | 185 | 1345 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 768 | 57 | 1345 | 439.70 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cu cât timp înainte ar trebui să vă contactez? | h3 | 390 | 45 | 1336.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1353 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1353 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1353 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1350.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 1440 | 393 | 1401 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 1024 | 185 | 1401 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 768 | 57 | 1401 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru nunțile din sezonul cald, ideal cu 8–12 l | span | 390 | 45 | 1400.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 1415 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 1415 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 1415 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 1414.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#rezervare-si-contract` | Rezervare și contract | div.motif-separator | 16 | 16 | 16 | 16 |
| `section#rezervare-si-contract` | div.motif-separator | [Cum rezerv data — avans și contract? Dat] | 32 | 32 | 32 | 28 |
| `div.space-y-4` | [Cum rezerv data — avans și contract? Dat] | [Cât este avansul și când se achită restu] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Cât este avansul și când se achită restu] | [Ce se întâmplă dacă trebuie să amân even] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Ce se întâmplă dacă trebuie să amân even] | [Cu cât timp înainte ar trebui să vă cont] | 16 | 16 | 16 | 16 |
| `details.group` | [Cum rezerv data — avans și contract?] | Data se blochează pe bază de contract și un avan | 0 | 0 | 0 | 0 |
| `summary.flex` | Cum rezerv data — avans și contract? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cât este avansul și când se achită restu] | [Răspuns de confirmatAvansul se achită la] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cât este avansul și când se achită restul? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Ce se întâmplă dacă trebuie să amân even] | [Răspuns de confirmatAmânarea se discută ] | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce se întâmplă dacă trebuie să amân evenimentul? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [Cu cât timp înainte ar trebui să vă cont] | [Răspuns de confirmatPentru nunțile din s] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cu cât timp înainte ar trebui să vă contactez? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 368.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 243.53 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 387.84 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 255.17 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 486.22 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 439.70 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |

---

## S5 — Prestația (#prestatia)

`section#prestatia` · clase: `mb-14 md:mb-20`

Eyebrow: «Răspuns de confirmat»

Titlu: «Prestația»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 586 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 586 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 586 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 548 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`div.motif-separator`) | 1440 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 1024 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 768 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 3** (`div.space-y-4`) | 1440 | 704 | 474 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 1024 | 704 | 474 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 768 | 704 | 474 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 390 | 342 | 450 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 5 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 5 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 5 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 5 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Prestația | h2 | 1440 | 368 | 1482 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Prestația | h2 | 1024 | 160 | 1482 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Prestația | h2 | 768 | 32 | 1482 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Prestația | h2 | 390 | 24 | 1457.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Ce tipuri de evenimente acoperă Ioana Balan? | h3 | 1440 | 393 | 1619 | 445.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce tipuri de evenimente acoperă Ioana Balan? | h3 | 1024 | 185 | 1619 | 445.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce tipuri de evenimente acoperă Ioana Balan? | h3 | 768 | 57 | 1619 | 445.58 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce tipuri de evenimente acoperă Ioana Balan? | h3 | 390 | 45 | 1576.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1627 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1627 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1627 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1590.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Oferim servicii muzicale complete pentru nunți,  | div | 1440 | 369 | 1675 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Oferim servicii muzicale complete pentru nunți,  | div | 1024 | 161 | 1675 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Oferim servicii muzicale complete pentru nunți,  | div | 768 | 33 | 1675 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Oferim servicii muzicale complete pentru nunți,  | div | 390 | 25 | 1640.50 | 340 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cât durează programul? | h3 | 1440 | 393 | 1717 | 243.48 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât durează programul? | h3 | 1024 | 185 | 1717 | 243.48 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât durează programul? | h3 | 768 | 57 | 1717 | 243.48 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cât durează programul? | h3 | 390 | 45 | 1678.50 | 162.77 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1725 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1725 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1725 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1681.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Programul standard acoperă seara întreagă, de la | div | 1440 | 369 | 1773 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Programul standard acoperă seara întreagă, de la | div | 1024 | 161 | 1773 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Programul standard acoperă seara întreagă, de la | div | 768 | 33 | 1773 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Programul standard acoperă seara întreagă, de la | div | 390 | 25 | 1720.50 | 340 | 144 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Pot cere o piesă anume pentru un moment special? | h3 | 1440 | 393 | 1815 | 491.92 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pot cere o piesă anume pentru un moment special? | h3 | 1024 | 185 | 1815 | 491.92 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pot cere o piesă anume pentru un moment special? | h3 | 768 | 57 | 1815 | 491.92 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Pot cere o piesă anume pentru un moment special? | h3 | 390 | 45 | 1758.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1823 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1823 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1823 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1772.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Trimiteți-ne lista pieselor care contează —  | span | 1440 | 393 | 1871 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Trimiteți-ne lista pieselor care contează —  | span | 1024 | 185 | 1871 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Trimiteți-ne lista pieselor care contează —  | span | 768 | 57 | 1871 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Trimiteți-ne lista pieselor care contează —  | span | 390 | 45 | 1822.50 | 300 | 167.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 1885 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 1885 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 1885 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 1836.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Cântați și muzică ușoară, sau doar populară? | h3 | 1440 | 393 | 1913 | 434.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și muzică ușoară, sau doar populară? | h3 | 1024 | 185 | 1913 | 434.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și muzică ușoară, sau doar populară? | h3 | 768 | 57 | 1913 | 434.59 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și muzică ușoară, sau doar populară? | h3 | 390 | 45 | 1860.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 1921 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 1921 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 1921 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1874.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Nucleul programului e muzica populară și de petr | span | 1440 | 393 | 1969 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Nucleul programului e muzica populară și de petr | span | 1024 | 185 | 1969 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Nucleul programului e muzica populară și de petr | span | 768 | 57 | 1969 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Nucleul programului e muzica populară și de petr | span | 390 | 45 | 1924.50 | 300 | 167.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 1983 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 1983 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 1983 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 1938.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Ce se întâmplă în pauzele formației? | h3 | 1440 | 393 | 2011 | 355.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă în pauzele formației? | h3 | 1024 | 185 | 2011 | 355.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă în pauzele formației? | h3 | 768 | 57 | 2011 | 355.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă în pauzele formației? | h3 | 390 | 45 | 1962.50 | 234.95 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2019 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2019 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2019 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 1965.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| DJ-ul preia fără pauză între momentele live, așa | div | 1440 | 369 | 2067 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ-ul preia fără pauză între momentele live, așa | div | 1024 | 161 | 2067 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ-ul preia fără pauză între momentele live, așa | div | 768 | 33 | 2067 | 702 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| DJ-ul preia fără pauză între momentele live, așa | div | 390 | 25 | 2004.50 | 340 | 120 | 16 | 24 | normal | 400 | #c6c6c6 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#prestatia` | Prestația | div.motif-separator | 16 | 16 | 16 | 16 |
| `section#prestatia` | div.motif-separator | [Ce tipuri de evenimente acoperă Ioana Ba] | 32 | 32 | 32 | 28 |
| `div.space-y-4` | [Ce tipuri de evenimente acoperă Ioana Ba] | [Cât durează programul? Programul standar] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Cât durează programul? Programul standar] | [Pot cere o piesă anume pentru un moment ] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Pot cere o piesă anume pentru un moment ] | [Cântați și muzică ușoară, sau doar popul] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Cântați și muzică ușoară, sau doar popul] | [Ce se întâmplă în pauzele formației? DJ-] | 16 | 16 | 16 | 16 |
| `details.group` | [Ce tipuri de evenimente acoperă Ioana Ba] | Oferim servicii muzicale complete pentru nunți,  | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce tipuri de evenimente acoperă Ioana Balan? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [Cât durează programul?] | Programul standard acoperă seara întreagă, de la | 0 | 0 | 0 | 0 |
| `summary.flex` | Cât durează programul? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Pot cere o piesă anume pentru un moment ] | [Răspuns de confirmatDa. Trimiteți-ne lis] | 0 | 0 | 0 | 0 |
| `summary.flex` | Pot cere o piesă anume pentru un moment special? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [Cântați și muzică ușoară, sau doar popul] | [Răspuns de confirmatNucleul programului ] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cântați și muzică ușoară, sau doar populară? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [Ce se întâmplă în pauzele formației?] | DJ-ul preia fără pauză între momentele live, așa | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce se întâmplă în pauzele formației? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 445.58 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 445.58 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 445.58 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 243.48 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 243.48 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 243.48 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 162.77 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 491.92 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 491.92 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 491.92 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 434.59 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 434.59 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 434.59 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 355.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 355.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 355.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 234.95 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |

---

## S6 — Tehnic și locație (#tehnic-si-locatie)

`section#tehnic-si-locatie` · clase: `mb-14 md:mb-20`

Eyebrow: «Răspuns de confirmat»

Titlu: «Tehnic și locație»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 488 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 424 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`div.motif-separator`) | 1440 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 1024 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 768 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 3** (`div.space-y-4`) | 1440 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 1024 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 768 | 704 | 376 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 390 | 342 | 326 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 4 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tehnic și locație | h2 | 1440 | 368 | 2148 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Tehnic și locație | h2 | 1024 | 160 | 2148 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Tehnic și locație | h2 | 768 | 32 | 2148 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Tehnic și locație | h2 | 390 | 24 | 2061.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Ce echipament aduceți și ce trebuie să asigure l | h3 | 1440 | 393 | 2285 | 518.03 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce echipament aduceți și ce trebuie să asigure l | h3 | 1024 | 185 | 2285 | 518.03 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce echipament aduceți și ce trebuie să asigure l | h3 | 768 | 57 | 2285 | 518.03 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce echipament aduceți și ce trebuie să asigure l | h3 | 390 | 45 | 2180.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2293 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2293 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2293 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2194.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Venim cu instrumentele, sonorizarea și luminile  | span | 1440 | 393 | 2341 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Venim cu instrumentele, sonorizarea și luminile  | span | 1024 | 185 | 2341 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Venim cu instrumentele, sonorizarea și luminile  | span | 768 | 57 | 2341 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Venim cu instrumentele, sonorizarea și luminile  | span | 390 | 45 | 2244.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 2355 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 2355 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 2355 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2258.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| De cât spațiu aveți nevoie pentru scenă? | h3 | 1440 | 393 | 2383 | 387.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| De cât spațiu aveți nevoie pentru scenă? | h3 | 1024 | 185 | 2383 | 387.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| De cât spațiu aveți nevoie pentru scenă? | h3 | 768 | 57 | 2383 | 387.80 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| De cât spațiu aveți nevoie pentru scenă? | h3 | 390 | 45 | 2282.50 | 255.58 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2391 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2391 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2391 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2285.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru formația completă, aproximativ 4×3 metri. | span | 1440 | 393 | 2439 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru formația completă, aproximativ 4×3 metri. | span | 1024 | 185 | 2439 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru formația completă, aproximativ 4×3 metri. | span | 768 | 57 | 2439 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pentru formația completă, aproximativ 4×3 metri. | span | 390 | 45 | 2324.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 2453 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 2453 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 2453 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2338.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Cântați și la evenimente în aer liber? | h3 | 1440 | 393 | 2481 | 356.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și la evenimente în aer liber? | h3 | 1024 | 185 | 2481 | 356.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și la evenimente în aer liber? | h3 | 768 | 57 | 2481 | 356.91 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și la evenimente în aer liber? | h3 | 390 | 45 | 2362.50 | 234.86 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2489 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2489 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2489 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2365.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, cu condiția să existe acoperire împotriva pl | span | 1440 | 393 | 2537 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, cu condiția să existe acoperire împotriva pl | span | 1024 | 185 | 2537 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, cu condiția să existe acoperire împotriva pl | span | 768 | 57 | 2537 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, cu condiția să existe acoperire împotriva pl | span | 390 | 45 | 2404.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 2551 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 2551 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 2551 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2418.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Aveți nevoie de masă pentru formație? | h3 | 1440 | 393 | 2579 | 375.23 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Aveți nevoie de masă pentru formație? | h3 | 1024 | 185 | 2579 | 375.23 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Aveți nevoie de masă pentru formație? | h3 | 768 | 57 | 2579 | 375.23 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Aveți nevoie de masă pentru formație? | h3 | 390 | 45 | 2442.50 | 247.63 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2587 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2587 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2587 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2445.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, o masă pentru echipă, în apropierea scenei.  | span | 1440 | 393 | 2635 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, o masă pentru echipă, în apropierea scenei.  | span | 1024 | 185 | 2635 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, o masă pentru echipă, în apropierea scenei.  | span | 768 | 57 | 2635 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da, o masă pentru echipă, în apropierea scenei.  | span | 390 | 45 | 2484.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 2649 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 2649 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 2649 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2498.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#tehnic-si-locatie` | Tehnic și locație | div.motif-separator | 16 | 16 | 16 | 16 |
| `section#tehnic-si-locatie` | div.motif-separator | [Ce echipament aduceți și ce trebuie să a] | 32 | 32 | 32 | 28 |
| `div.space-y-4` | [Ce echipament aduceți și ce trebuie să a] | [De cât spațiu aveți nevoie pentru scenă?] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [De cât spațiu aveți nevoie pentru scenă?] | [Cântați și la evenimente în aer liber? R] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Cântați și la evenimente în aer liber? R] | [Aveți nevoie de masă pentru formație? Ră] | 16 | 16 | 16 | 16 |
| `details.group` | [Ce echipament aduceți și ce trebuie să a] | [Răspuns de confirmatVenim cu instrumente] | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce echipament aduceți și ce trebuie să asigure l | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |
| `details.group` | [De cât spațiu aveți nevoie pentru scenă?] | [Răspuns de confirmatPentru formația comp] | 0 | 0 | 0 | 0 |
| `summary.flex` | De cât spațiu aveți nevoie pentru scenă? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cântați și la evenimente în aer liber?] | [Răspuns de confirmatDa, cu condiția să e] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cântați și la evenimente în aer liber? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Aveți nevoie de masă pentru formație?] | [Răspuns de confirmatDa, o masă pentru ec] | 0 | 0 | 0 | 0 |
| `summary.flex` | Aveți nevoie de masă pentru formație? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 518.03 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 518.03 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 518.03 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |
| `summary.flex` | 1440 | flex | 387.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 387.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 387.80 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 255.58 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 356.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 356.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 356.91 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 234.86 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 375.23 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 375.23 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 375.23 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 247.63 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |

---

## S7 — Deplasare (#deplasare)

`section#deplasare` · clase: `mb-14 md:mb-20`

Eyebrow: «Răspuns de confirmat»

Titlu: «Deplasare»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 390 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 704 | 390 | 0/0/0/0 | transparent | none |
| **section** | 768 | 704 | 390 | 0/0/0/0 | transparent | none |
| **section** | 390 | 342 | 344 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1440 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 1024 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 768 | 704 | 40 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-headline-lg`) | 390 | 342 | 30 | 0/0/0/0 | transparent | none |
| **container 2** (`div.motif-separator`) | 1440 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 1024 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 768 | 704 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.motif-separator`) | 390 | 342 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 3** (`div.space-y-4`) | 1440 | 704 | 278 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 1024 | 704 | 278 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 768 | 704 | 278 | 0/0/0/0 | transparent | none |
| **container 3** (`div.space-y-4`) | 390 | 342 | 246 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 1 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 2 (`div.faq-item`) | 390 | 342 | 64 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1440 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 1024 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 768 | 704 | 82 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| └ coloana 3 (`div.faq-item`) | 390 | 342 | 86 | 0/0/0/0 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Deplasare | h2 | 1440 | 368 | 2716 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Deplasare | h2 | 1024 | 160 | 2716 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Deplasare | h2 | 768 | 32 | 2716 | 704 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Deplasare | h2 | 390 | 24 | 2541.50 | 342 | 30 | 24 | 30 | normal | 400 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 1440 | 393 | 2853 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 1024 | 185 | 2853 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 768 | 57 | 2853 | 325.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cântați și în afara Bucureștiului? | h3 | 390 | 45 | 2660.50 | 215.09 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2861 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2861 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2861 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2663.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 1440 | 369 | 2909 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 1024 | 161 | 2909 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 768 | 33 | 2909 | 702 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Da. Cântăm cel mai des în București, Ploiești, B | div | 390 | 25 | 2702.50 | 340 | 192 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Cum se calculează costul deplasării? | h3 | 1440 | 393 | 2951 | 350.69 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum se calculează costul deplasării? | h3 | 1024 | 185 | 2951 | 350.69 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum se calculează costul deplasării? | h3 | 768 | 57 | 2951 | 350.69 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Cum se calculează costul deplasării? | h3 | 390 | 45 | 2740.50 | 232.41 | 22 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 2959 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 2959 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 2959 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2743.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pe kilometru, dus-întors, de la localitatea de r | span | 1440 | 393 | 3007 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pe kilometru, dus-întors, de la localitatea de r | span | 1024 | 185 | 3007 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pe kilometru, dus-întors, de la localitatea de r | span | 768 | 57 | 3007 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Pe kilometru, dus-întors, de la localitatea de r | span | 390 | 45 | 2782.50 | 300 | 143.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 3021 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 3021 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 3021 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2796.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Ce se întâmplă la distanțe mari, unde e nevoie d | h3 | 1440 | 393 | 3049 | 542.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă la distanțe mari, unde e nevoie d | h3 | 1024 | 185 | 3049 | 542.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă la distanțe mari, unde e nevoie d | h3 | 768 | 57 | 3049 | 542.78 | 32 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| Ce se întâmplă la distanțe mari, unde e nevoie d | h3 | 390 | 45 | 2820.50 | 268 | 44 | 16 | 22 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1440 | 1031 | 3057 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 823 | 3057 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 695 | 3057 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | 329 | 2834.50 | 16 | 16 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| La distanțele care cer deplasare cu o zi înainte | span | 1440 | 393 | 3105 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| La distanțele care cer deplasare cu o zi înainte | span | 1024 | 185 | 3105 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| La distanțele care cer deplasare cu o zi înainte | span | 768 | 57 | 3105 | 654 | 95.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| La distanțele care cer deplasare cu o zi înainte | span | 390 | 45 | 2884.50 | 300 | 167.19 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1440 | 409 | 3119 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 1024 | 201 | 3119 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 768 | 73 | 3119 | 622 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |
| Răspuns de confirmat | span | 390 | 61 | 2898.50 | 268 | 13.19 | 11 | 13.20 | 1.54 | 600 | #e5e2e1 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section#deplasare` | Deplasare | div.motif-separator | 16 | 16 | 16 | 16 |
| `section#deplasare` | div.motif-separator | [Cântați și în afara Bucureștiului? Da. C] | 32 | 32 | 32 | 28 |
| `div.space-y-4` | [Cântați și în afara Bucureștiului? Da. C] | [Cum se calculează costul deplasării? Răs] | 16 | 16 | 16 | 16 |
| `div.space-y-4` | [Cum se calculează costul deplasării? Răs] | [Ce se întâmplă la distanțe mari, unde e ] | 16 | 16 | 16 | 16 |
| `details.group` | [Cântați și în afara Bucureștiului?] | Da. Cântăm cel mai des în București, Ploiești, B | 0 | 0 | 0 | 0 |
| `summary.flex` | Cântați și în afara Bucureștiului? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Cum se calculează costul deplasării?] | [Răspuns de confirmatPe kilometru, dus-în] | 0 | 0 | 0 | 0 |
| `summary.flex` | Cum se calculează costul deplasării? | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -19 ¹ |
| `details.group` | [Ce se întâmplă la distanțe mari, unde e ] | [Răspuns de confirmatLa distanțele care c] | 0 | 0 | 0 | 0 |
| `summary.flex` | Ce se întâmplă la distanțe mari, unde e nevoie d | svg (icon) | -24 ¹ | -24 ¹ | -24 ¹ | -30 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `summary.flex` | 1440 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 325.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 215.09 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 350.69 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 350.69 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 350.69 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 232.41 + 16 | 16px | 16px | **NU** — 16…22, delta 6 |
| `summary.flex` | 1440 | flex | 542.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 1024 | flex | 542.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 768 | flex | 542.78 + 16 | 16px | 16px | **NU** — 16…32, delta 16 |
| `summary.flex` | 390 | flex | 268 + 16 | 16px | 16px | **NU** — 16…44, delta 28 |

---

## S8 — Nu ați găsit răspunsul?

`section` · clase: `border-t border-outline-variant/15 pt-12 md:pt-16 text-center`

Titlu: «Nu ați găsit răspunsul?»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 704 | 291 | 64/0/0/0 | transparent | T 1px #444748 @0.15 |
| **section** | 1024 | 704 | 291 | 64/0/0/0 | transparent | T 1px #444748 @0.15 |
| **section** | 768 | 704 | 291 | 64/0/0/0 | transparent | T 1px #444748 @0.15 |
| **section** | 390 | 342 | 305.50 | 48/0/0/0 | transparent | T 1px #444748 @0.15 |
| **container 1** (`h2.font-display-lg`) | 1440 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 1024 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 768 | 704 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 390 | 342 | 32.50 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-lg`) | 1440 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-lg`) | 1024 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-lg`) | 768 | 576 | 56 | 0/0/0/0 | transparent | none |
| **container 2** (`p.font-body-lg`) | 390 | 342 | 48 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1440 | 704 | 62 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1024 | 704 | 62 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 768 | 704 | 62 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 390 | 342 | 124 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.inline-block`) | 1440 | 305.94 | 62 | 20/48/20/48 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 1024 | 305.94 | 62 | 20/48/20/48 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 768 | 305.94 | 62 | 20/48/20/48 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.inline-block`) | 390 | 342 | 54 | 16/32/16/32 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 2 (`a.inline-block`) | 1440 | 230.73 | 62 | 20/48/20/48 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 1024 | 230.73 | 62 | 20/48/20/48 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 768 | 230.73 | 62 | 20/48/20/48 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.inline-block`) | 390 | 342 | 54 | 16/32/16/32 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nu ați găsit răspunsul? | h2 | 1440 | 368 | 3251 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Nu ați găsit răspunsul? | h2 | 1024 | 160 | 3251 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Nu ați găsit răspunsul? | h2 | 768 | 32 | 3251 | 704 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Nu ați găsit răspunsul? | h2 | 390 | 24 | 2990.50 | 342 | 32.50 | 26 | 32.50 | normal | 400 | #e5e2e1 | center |
| Spuneți-ne data și locația evenimentului. Vă răs | p | 1440 | 432 | 3323 | 576 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Spuneți-ne data și locația evenimentului. Vă răs | p | 1024 | 224 | 3323 | 576 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Spuneți-ne data și locația evenimentului. Vă răs | p | 768 | 96 | 3323 | 576 | 56 | 18 | 28 | normal | 400 | #c4c7c7 | center |
| Spuneți-ne data și locația evenimentului. Vă răs | p | 390 | 24 | 3039 | 342 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Întrebați pe WhatsApp | a | 1440 | 443.66 | 3415 | 305.94 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Întrebați pe WhatsApp | a | 1024 | 235.66 | 3415 | 305.94 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Întrebați pe WhatsApp | a | 768 | 107.66 | 3415 | 305.94 | 62 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Întrebați pe WhatsApp | a | 390 | 24 | 3123 | 342 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| +40 722 911 485 | a | 1440 | 765.59 | 3415 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 1024 | 557.59 | 3415 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 768 | 429.59 | 3415 | 230.73 | 62 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| +40 722 911 485 | a | 390 | 24 | 3193 | 342 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | Nu ați găsit răspunsul? | Spuneți-ne data și locația evenimentului. Vă răs | 16 | 16 | 16 | 16 |
| `section` | Spuneți-ne data și locația evenimentului. Vă răs | [Întrebați pe WhatsApp +40 722 911 485] | 36 | 36 | 36 | 36 |
| `div.flex` | Întrebați pe WhatsApp | +40 722 911 485 | -62 ¹ | -62 ¹ | -62 ¹ | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 305.94 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 1024 | flex | 305.94 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 768 | flex | 305.94 + 230.73 | 16px | 16px | da (62) |
| `div.flex` | 390 | flex | 342 + 342 | 16px | 16px | da (54) |

---

## Ce nu se vede din clase

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Ce ne întrebați cel mai des» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[30px]`; weight rezolvat 400/500, font-size masurat 30/48px
- `h2` «Preț» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Prețul unei formații pentru 2026-2027?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Rezervare și contract» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Cum rezerv data — avans și contract?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cât este avansul și când se achită restul?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Ce se întâmplă dacă trebuie să amân evenimentul?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cu cât timp înainte ar trebui să vă contactez?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Prestația» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Ce tipuri de evenimente acoperă Ioana Balan?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cât durează programul?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Pot cere o piesă anume pentru un moment special?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cântați și muzică ușoară, sau doar populară?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Ce se întâmplă în pauzele formației?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Tehnic și locație» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Ce echipament aduceți și ce trebuie să asigure l» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «De cât spațiu aveți nevoie pentru scenă?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cântați și la evenimente în aer liber?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Aveți nevoie de masă pentru formație?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Deplasare» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Cântați și în afara Bucureștiului?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Cum se calculează costul deplasării?» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h3` «Ce se întâmplă la distanțe mari, unde e nevoie d» — `font-headline-md` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400/500, font-size masurat 16/24px
- `h2` «Nu ați găsit răspunsul?» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[26px]`; weight rezolvat 400/500, font-size masurat 26/48px

### Borduri care vin din `assets/styles.css`, nu din clase

- `span.motif-rule__gem` «span.motif-rule__gem» — T 1px #800020, R 1px #800020, B 1px #800020, L 1px #800020, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Avansul se achită la semnarea contractului și bl» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Amânarea se discută direct cu noi și se consemne» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Pentru nunțile din sezonul cald, ideal cu 8–12 l» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Da. Trimiteți-ne lista pieselor care contează — » — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Nucleul programului e muzica populară și de petr» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Venim cu instrumentele, sonorizarea și luminile » — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Pentru formația completă, aproximativ 4×3 metri.» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Da, cu condiția să existe acoperire împotriva pl» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Da, o masă pentru echipă, în apropierea scenei. » — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «Pe kilometru, dus-întors, de la localitatea de r» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `span.answer-tbc` «La distanțele care cer deplasare cu o zi înainte» — T 2px #c41236, R 2px #c41236, B 2px #c41236, L 2px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.inline-block` «Întrebați pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Ce ne întrebați cel mai des | 220 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Preț | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 | x 8px / y 8px | in `ul.flex` (lat. 704 la 1440, flex):<br>75.48 + 243.73 + 123.77 + 190.84 + 128.94 |
| Preț (#pret) | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 702 la 1440, flex):<br>1440: 390.91 + 16 · 1024: 390.91 + 16 · 768: 390.91 + 16 · 390: 256.84 + 16 |
| Rezervare și contract (#rezervare-si-contract) | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 702 la 1440, flex):<br>1440: 368.70 + 16 · 1024: 368.70 + 16 · 768: 368.70 + 16 · 390: 243.53 + 16 |
| Prestația (#prestatia) | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 702 la 1440, flex):<br>1440: 445.58 + 16 · 1024: 445.58 + 16 · 768: 445.58 + 16 · 390: 268 + 16 |
| Tehnic și locație (#tehnic-si-locatie) | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 702 la 1440, flex):<br>1440: 518.03 + 16 · 1024: 518.03 + 16 · 768: 518.03 + 16 · 390: 268 + 16 |
| Deplasare (#deplasare) | 1440: 704 · 1024: 704 · 768: 704 · 390: 342 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | 0/0/0/0 / 0/16/0/0 | x 16px / y 16px | in `summary.flex` (lat. 702 la 1440, flex):<br>1440: 325.78 + 16 · 1024: 325.78 + 16 · 768: 325.78 + 16 · 390: 215.09 + 16 |
| Nu ați găsit răspunsul? | 1440: 576 · 1024: 576 · 768: 576 · 390: 342 | vert (sectiune): 1440: 64 sus / 0 jos · 1024: 64 sus / 0 jos · 768: 64 sus / 0 jos · 390: 48 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
