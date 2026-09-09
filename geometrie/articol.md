# Geometrie randata — `articol.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/articol.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1200 | 2448 | 160/64/96/64 | transparent | none |
| `<main>` | 1024 | 1024 | 2448 | 160/64/96/64 | transparent | none |
| `<main>` | 768 | 768 | 2574 | 160/64/96/64 | transparent | none |
| `<main>` | 390 | 390 | 3550 | 128/16/64/16 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 2885px, 1024 → 2885px, 768 → 3063px, 390 → 4155px.

Sectiuni masurate: **4**.

---

## S1 — Importanța luminilor de scenă pentru show-ul formați

`header` · clase: `mb-16`

Eyebrow: «Tehnică de scenă»

Titlu: «Importanța luminilor de scenă pentru show-ul formației»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1072 | 224 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 896 | 224 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 224 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 344 | 0/0/0/0 | transparent | none |
| **container 1** (`div.flex`) | 1440 | 1072 | 28 | 0/0/0/0 | transparent | none |
| **container 1** (`div.flex`) | 1024 | 896 | 28 | 0/0/0/0 | transparent | none |
| **container 1** (`div.flex`) | 768 | 640 | 28 | 0/0/0/0 | transparent | none |
| **container 1** (`div.flex`) | 390 | 358 | 28 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`span.font-label-md`) | 1440 | 172.72 | 28 | 4/12/4/12 | #2a2a2a | none |
| └ coloana 1 (`span.font-label-md`) | 1024 | 172.72 | 28 | 4/12/4/12 | #2a2a2a | none |
| └ coloana 1 (`span.font-label-md`) | 768 | 172.72 | 28 | 4/12/4/12 | #2a2a2a | none |
| └ coloana 1 (`span.font-label-md`) | 390 | 172.72 | 28 | 4/12/4/12 | #2a2a2a | none |
| └ coloana 2 (`span.text-outline`) | 1440 | 115.86 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`span.text-outline`) | 1024 | 115.86 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`span.text-outline`) | 768 | 115.86 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`span.text-outline`) | 390 | 115.86 | 20 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1440 | 896 | 120 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 1024 | 896 | 120 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 768 | 640 | 120 | 0/0/0/0 | transparent | none |
| **container 2** (`h1.font-display-lg`) | 390 | 358 | 240 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1440 | 1072 | 20 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1024 | 896 | 20 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 768 | 640 | 20 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 390 | 358 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.h-[1px]`) | 1440 | 48 | 1 | 0/0/0/0 | #c8c6c5 | none |
| └ coloana 1 (`div.h-[1px]`) | 1024 | 48 | 1 | 0/0/0/0 | #c8c6c5 | none |
| └ coloana 1 (`div.h-[1px]`) | 768 | 48 | 1 | 0/0/0/0 | #c8c6c5 | none |
| └ coloana 1 (`div.h-[1px]`) | 390 | 48 | 1 | 0/0/0/0 | #c8c6c5 | none |
| └ coloana 2 (`p.font-label-md`) | 1440 | 214.64 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-label-md`) | 1024 | 214.64 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-label-md`) | 768 | 214.64 | 20 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.font-label-md`) | 390 | 214.64 | 20 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Tehnică de scenă | span | 1440 | 184 | 160 | 172.72 | 28 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Tehnică de scenă | span | 1024 | 64 | 160 | 172.72 | 28 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Tehnică de scenă | span | 768 | 64 | 160 | 172.72 | 28 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Tehnică de scenă | span | 390 | 16 | 128 | 172.72 | 28 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| 15 August 2024 | span | 1440 | 372.72 | 164 | 115.86 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 15 August 2024 | span | 1024 | 252.72 | 164 | 115.86 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 15 August 2024 | span | 768 | 252.72 | 164 | 115.86 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 15 August 2024 | span | 390 | 204.72 | 132 | 115.86 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| Importanța luminilor de scenă pentru show-ul for | h1 | 1440 | 184 | 212 | 896 | 120 | 48 | 60 | -0.96 | 500 | #e5e2e1 | start |
| Importanța luminilor de scenă pentru show-ul for | h1 | 1024 | 64 | 212 | 896 | 120 | 48 | 60 | -0.96 | 500 | #e5e2e1 | start |
| Importanța luminilor de scenă pentru show-ul for | h1 | 768 | 64 | 212 | 640 | 120 | 48 | 60 | -0.96 | 500 | #e5e2e1 | start |
| Importanța luminilor de scenă pentru show-ul for | h1 | 390 | 16 | 180 | 358 | 240 | 48 | 60 | -0.96 | 500 | #e5e2e1 | start |
| Articol de Ioana Balan | p | 1440 | 248 | 364 | 214.64 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Articol de Ioana Balan | p | 1024 | 128 | 364 | 214.64 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Articol de Ioana Balan | p | 768 | 128 | 364 | 214.64 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Articol de Ioana Balan | p | 390 | 80 | 452 | 214.64 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `header.mb-16` | [Tehnică de scenă 15 August 2024] | Importanța luminilor de scenă pentru show-ul for | 24 | 24 | 24 | 24 |
| `header.mb-16` | Importanța luminilor de scenă pentru show-ul for | [Articol de Ioana Balan] | 32 | 32 | 32 | 32 |
| `div.flex` | Tehnică de scenă | 15 August 2024 | -24 ¹ | -24 ¹ | -24 ¹ | -24 ¹ |
| `div.flex` | div.h-[1px] | Articol de Ioana Balan | -10.50 ¹ | -10.50 ¹ | -10.50 ¹ | -10.50 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 172.72 + 115.86 | 16px | 16px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 172.72 + 115.86 | 16px | 16px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 172.72 + 115.86 | 16px | 16px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 172.72 + 115.86 | 16px | 16px | **NU** — 20…28, delta 8 |
| `div.flex` | 1440 | flex | 48 + 214.64 | 16px | 16px | **NU** — 1…20, delta 19 |
| `div.flex` | 1024 | flex | 48 + 214.64 | 16px | 16px | **NU** — 1…20, delta 19 |
| `div.flex` | 768 | flex | 48 + 214.64 | 16px | 16px | **NU** — 1…20, delta 19 |
| `div.flex` | 390 | flex | 48 + 214.64 | 16px | 16px | **NU** — 1…20, delta 19 |

---

## S2 — "Lumina nu doar luminează, ea transformă spațiul înt

`div` · clase: `bento-grid mb-24`

Titlu: «"Lumina nu doar luminează, ea transformă spațiul într-o experiență emoțională."»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1072 | 500 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 896 | 500 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 546 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 822 | 0/0/0/0 | transparent | none |
| **container 1** (`div.col-span-12`) | 1440 | 706.66 | 500 | 0/0/0/0 | transparent | none |
| **container 1** (`div.col-span-12`) | 1024 | 589.33 | 500 | 0/0/0/0 | transparent | none |
| **container 1** (`div.col-span-12`) | 768 | 418.66 | 546 | 0/0/0/0 | transparent | none |
| **container 1** (`div.col-span-12`) | 390 | 358 | 500 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 1440 | 706.66 | 500 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 1024 | 589.33 | 500 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 768 | 418.66 | 500 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`img.w-full`) | 390 | 358 | 500 | 0/0/0/0 | transparent | none |
| **container 2** (`div.col-span-12`) | 1440 | 341.34 | 500 | 40/40/40/40 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **container 2** (`div.col-span-12`) | 1024 | 282.67 | 500 | 40/40/40/40 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **container 2** (`div.col-span-12`) | 768 | 197.34 | 546 | 40/40/40/40 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| **container 2** (`div.col-span-12`) | 390 | 358 | 298 | 40/40/40/40 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`h3.font-headline-md`) | 1440 | 259.34 | 128 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h3.font-headline-md`) | 1024 | 200.67 | 160 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h3.font-headline-md`) | 768 | 115.34 | 256 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h3.font-headline-md`) | 390 | 276 | 128 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.text-on-surface-variant`) | 1440 | 259.34 | 96 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.text-on-surface-variant`) | 1024 | 200.67 | 120 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.text-on-surface-variant`) | 768 | 115.34 | 192 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`p.text-on-surface-variant`) | 390 | 276 | 72 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-and-band.jpg | img | 1440 | 184 | 448 | 706.66 | 500 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-and-band.jpg | img | 1024 | 64 | 448 | 589.33 | 500 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-and-band.jpg | img | 768 | 64 | 448 | 418.66 | 500 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-and-band.jpg | img | 390 | 16 | 536 | 358 | 500 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| "Lumina nu doar luminează, ea transformă spațiul | h3 | 1440 | 955.66 | 578 | 259.34 | 128 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| "Lumina nu doar luminează, ea transformă spațiul | h3 | 1024 | 718.33 | 550 | 200.67 | 160 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| "Lumina nu doar luminează, ea transformă spațiul | h3 | 768 | 547.66 | 489 | 115.34 | 256 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| "Lumina nu doar luminează, ea transformă spațiul | h3 | 390 | 57 | 1101 | 276 | 128 | 24 | 32 | normal | 500 | #c8c6c5 | start |
| O seară reușită începe cu atmosfera potrivită. D | p | 1440 | 955.66 | 722 | 259.34 | 96 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| O seară reușită începe cu atmosfera potrivită. D | p | 1024 | 718.33 | 726 | 200.67 | 120 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| O seară reușită începe cu atmosfera potrivită. D | p | 768 | 547.66 | 761 | 115.34 | 192 | 16 | 24 | normal | 400 | #c4c7c7 | start |
| O seară reușită începe cu atmosfera potrivită. D | p | 390 | 57 | 1245 | 276 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.bento-grid` | div.col-span-12 | ["Lumina nu doar luminează, ea transformă] | -500 ¹ | -500 ¹ | -546 ¹ | 24 |
| `div.col-span-12` | "Lumina nu doar luminează, ea transformă spațiul | O seară reușită începe cu atmosfera potrivită. D | 16 | 16 | 16 | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.bento-grid` | 1440 | grid | 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px | 24px | 24px | da (500) |
| `div.bento-grid` | 1024 | grid | 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px | 24px | 24px | da (500) |
| `div.bento-grid` | 768 | grid | 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px 31.3281px | 24px | 24px | da (546) |
| `div.bento-grid` | 390 | grid | 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px 7.82812px | 24px | 24px | **NU** — 298…500, delta 202 |

---

## S3 — Atmosfera și Dinamica Vizuală

`article` · clase: `max-w-3xl mx-auto space-y-8 leading-relaxed text-on-surface-variant`

Titlu: «Atmosfera și Dinamica Vizuală»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 768 | 900 | 0/0/0/0 | transparent | none |
| **section** | 1024 | 768 | 900 | 0/0/0/0 | transparent | none |
| **section** | 768 | 640 | 980 | 0/0/0/0 | transparent | none |
| **section** | 390 | 358 | 1514 | 0/0/0/0 | transparent | none |
| **container 1** (`p.font-body-lg`) | 1440 | 768 | 84 | 0/0/0/0 | transparent | none |
| **container 1** (`p.font-body-lg`) | 1024 | 768 | 84 | 0/0/0/0 | transparent | none |
| **container 1** (`p.font-body-lg`) | 768 | 640 | 112 | 0/0/0/0 | transparent | none |
| **container 1** (`p.font-body-lg`) | 390 | 358 | 196 | 0/0/0/0 | transparent | none |
| **container 2** (`h2.font-headline-lg`) | 1440 | 768 | 40 | 0/0/0/0 | transparent | none |
| **container 2** (`h2.font-headline-lg`) | 1024 | 768 | 40 | 0/0/0/0 | transparent | none |
| **container 2** (`h2.font-headline-lg`) | 768 | 640 | 40 | 0/0/0/0 | transparent | none |
| **container 2** (`h2.font-headline-lg`) | 390 | 358 | 80 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1440 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 1024 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 768 | 640 | 130 | 0/0/0/0 | transparent | none |
| **container 3** (`p`) | 390 | 358 | 208 | 0/0/0/0 | transparent | none |
| **container 4** (`div.my-12`) | 1440 | 768 | 96 | 16/0/16/32 | transparent | L 2px #c8c6c5 |
| **container 4** (`div.my-12`) | 1024 | 768 | 96 | 16/0/16/32 | transparent | L 2px #c8c6c5 |
| **container 4** (`div.my-12`) | 768 | 640 | 96 | 16/0/16/32 | transparent | L 2px #c8c6c5 |
| **container 4** (`div.my-12`) | 390 | 358 | 128 | 16/0/16/32 | transparent | L 2px #c8c6c5 |
| └ coloana 1 (`p.italic`) | 1440 | 734 | 64 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p.italic`) | 1024 | 734 | 64 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p.italic`) | 768 | 606 | 64 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`p.italic`) | 390 | 324 | 96 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1440 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 1024 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 768 | 640 | 130 | 0/0/0/0 | transparent | none |
| **container 5** (`p`) | 390 | 358 | 208 | 0/0/0/0 | transparent | none |
| **container 6** (`h2.font-headline-lg`) | 1440 | 768 | 40 | 0/0/0/0 | transparent | none |
| **container 6** (`h2.font-headline-lg`) | 1024 | 768 | 40 | 0/0/0/0 | transparent | none |
| **container 6** (`h2.font-headline-lg`) | 768 | 640 | 40 | 0/0/0/0 | transparent | none |
| **container 6** (`h2.font-headline-lg`) | 390 | 358 | 80 | 0/0/0/0 | transparent | none |
| **container 7** (`p`) | 1440 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 7** (`p`) | 1024 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 7** (`p`) | 768 | 640 | 104 | 0/0/0/0 | transparent | none |
| **container 7** (`p`) | 390 | 358 | 208 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 1440 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 1024 | 768 | 104 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 768 | 640 | 104 | 0/0/0/0 | transparent | none |
| **container 8** (`p`) | 390 | 358 | 182 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| La o formație de nuntă, calitatea sunetului se s | p | 1440 | 336 | 1044 | 768 | 84 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| La o formație de nuntă, calitatea sunetului se s | p | 1024 | 128 | 1044 | 768 | 84 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| La o formație de nuntă, calitatea sunetului se s | p | 768 | 64 | 1090 | 640 | 112 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| La o formație de nuntă, calitatea sunetului se s | p | 390 | 16 | 1454 | 358 | 196 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Atmosfera și Dinamica Vizuală | h2 | 1440 | 336 | 1160 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Atmosfera și Dinamica Vizuală | h2 | 1024 | 128 | 1160 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Atmosfera și Dinamica Vizuală | h2 | 768 | 64 | 1234 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Atmosfera și Dinamica Vizuală | h2 | 390 | 16 | 1682 | 358 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Luminile de scenă nu sunt doar accesorii estetic | p | 1440 | 336 | 1232 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Luminile de scenă nu sunt doar accesorii estetic | p | 1024 | 128 | 1232 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Luminile de scenă nu sunt doar accesorii estetic | p | 768 | 64 | 1306 | 640 | 130 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Luminile de scenă nu sunt doar accesorii estetic | p | 390 | 16 | 1794 | 358 | 208 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| "Un show fără lumini este ca un tablou fără culo | p | 1440 | 370 | 1384 | 734 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| "Un show fără lumini este ca un tablou fără culo | p | 1024 | 162 | 1384 | 734 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| "Un show fără lumini este ca un tablou fără culo | p | 768 | 98 | 1484 | 606 | 64 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| "Un show fără lumini este ca un tablou fără culo | p | 390 | 50 | 2050 | 324 | 96 | 24 | 32 | normal | 500 | #e5e2e1 | start |
| La Grand Music Events, punem un accent deosebit  | p | 1440 | 336 | 1496 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| La Grand Music Events, punem un accent deosebit  | p | 1024 | 128 | 1496 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| La Grand Music Events, punem un accent deosebit  | p | 768 | 64 | 1596 | 640 | 130 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| La Grand Music Events, punem un accent deosebit  | p | 390 | 16 | 2194 | 358 | 208 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Profesionalismul din Spatele pupitrului | h2 | 1440 | 336 | 1632 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Profesionalismul din Spatele pupitrului | h2 | 1024 | 128 | 1632 | 768 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Profesionalismul din Spatele pupitrului | h2 | 768 | 64 | 1758 | 640 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Profesionalismul din Spatele pupitrului | h2 | 390 | 16 | 2434 | 358 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Importanța unui tehnician de lumini dedicat este | p | 1440 | 336 | 1704 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Importanța unui tehnician de lumini dedicat este | p | 1024 | 128 | 1704 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Importanța unui tehnician de lumini dedicat este | p | 768 | 64 | 1830 | 640 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| Importanța unui tehnician de lumini dedicat este | p | 390 | 16 | 2546 | 358 | 208 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| În concluzie, investiția în aspectul vizual este | p | 1440 | 336 | 1840 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| În concluzie, investiția în aspectul vizual este | p | 1024 | 128 | 1840 | 768 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| În concluzie, investiția în aspectul vizual este | p | 768 | 64 | 1966 | 640 | 104 | 16 | 26 | normal | 400 | #c4c7c7 | start |
| În concluzie, investiția în aspectul vizual este | p | 390 | 16 | 2786 | 358 | 182 | 16 | 26 | normal | 400 | #c4c7c7 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `article.max-w-3xl` | La o formație de nuntă, calitatea sunetului se s | Atmosfera și Dinamica Vizuală | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | Atmosfera și Dinamica Vizuală | Luminile de scenă nu sunt doar accesorii estetic | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | Luminile de scenă nu sunt doar accesorii estetic | ["Un show fără lumini este ca un tablou f] | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | ["Un show fără lumini este ca un tablou f] | La Grand Music Events, punem un accent deosebit  | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | La Grand Music Events, punem un accent deosebit  | Profesionalismul din Spatele pupitrului | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | Profesionalismul din Spatele pupitrului | Importanța unui tehnician de lumini dedicat este | 32 | 32 | 32 | 32 |
| `article.max-w-3xl` | Importanța unui tehnician de lumini dedicat este | În concluzie, investiția în aspectul vizual este | 32 | 32 | 32 | 32 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

---

## S4 — Plănuiți un eveniment?

`section` · clase: `mt-24 glass-card p-6 md:p-12 text-center border border-outline-variant/30`

Titlu: «Plănuiți un eveniment?»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1072 | 312 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| **section** | 1024 | 896 | 312 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| **section** | 768 | 640 | 312 | 48/48/48/48 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| **section** | 390 | 358 | 422 | 24/24/24/24 | #1c1b1b | T 1px #444748 @0.3, R 1px #444748 @0.3, B 1px #444748 @0.3, L 1px #444748 @0.3 |
| **container 1** (`h2.font-display-lg`) | 1440 | 974 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 1024 | 798 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 768 | 542 | 56 | 0/0/0/0 | transparent | none |
| **container 1** (`h2.font-display-lg`) | 390 | 308 | 112 | 0/0/0/0 | transparent | none |
| **container 2** (`p.text-on-surface-variant`) | 1440 | 576 | 48 | 0/0/0/0 | transparent | none |
| **container 2** (`p.text-on-surface-variant`) | 1024 | 576 | 48 | 0/0/0/0 | transparent | none |
| **container 2** (`p.text-on-surface-variant`) | 768 | 542 | 48 | 0/0/0/0 | transparent | none |
| **container 2** (`p.text-on-surface-variant`) | 390 | 308 | 72 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1440 | 974 | 54 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 1024 | 798 | 54 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 768 | 542 | 54 | 0/0/0/0 | transparent | none |
| **container 3** (`div.flex`) | 390 | 308 | 132 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`a.bg-accent`) | 1440 | 277.72 | 54 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.bg-accent`) | 1024 | 277.72 | 54 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.bg-accent`) | 768 | 277.72 | 54 | 16/40/16/40 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 1 (`a.bg-accent`) | 390 | 308 | 54 | 16/32/16/32 | #a01028 | T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236 |
| └ coloana 2 (`a.border`) | 1440 | 193.36 | 54 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.border`) | 1024 | 193.36 | 54 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.border`) | 768 | 193.36 | 54 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |
| └ coloana 2 (`a.border`) | 390 | 308 | 54 | 16/40/16/40 | transparent | T 1px #8e9192, R 1px #8e9192, B 1px #8e9192, L 1px #8e9192 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plănuiți un eveniment? | h2 | 1440 | 233 | 2089 | 974 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Plănuiți un eveniment? | h2 | 1024 | 113 | 2089 | 798 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Plănuiți un eveniment? | h2 | 768 | 113 | 2215 | 542 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Plănuiți un eveniment? | h2 | 390 | 41 | 3089 | 308 | 112 | 48 | 56 | -0.96 | 500 | #e5e2e1 | center |
| Descoperiți ofertele noastre personalizate pentr | p | 1440 | 432 | 2161 | 576 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Descoperiți ofertele noastre personalizate pentr | p | 1024 | 224 | 2161 | 576 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Descoperiți ofertele noastre personalizate pentr | p | 768 | 113 | 2287 | 542 | 48 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Descoperiți ofertele noastre personalizate pentr | p | 390 | 41 | 3217 | 308 | 72 | 16 | 24 | normal | 400 | #c4c7c7 | center |
| Rezervă pe WhatsApp | a | 1440 | 472.45 | 2249 | 277.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 1024 | 264.45 | 2249 | 277.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 768 | 136.45 | 2375 | 277.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 390 | 41 | 3329 | 308 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Cere ofertă | a | 1440 | 774.17 | 2249 | 193.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 1024 | 566.17 | 2249 | 193.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 768 | 438.17 | 2375 | 193.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 390 | 41 | 3407 | 308 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | Plănuiți un eveniment? | Descoperiți ofertele noastre personalizate pentr | 16 | 16 | 16 | 16 |
| `section` | Descoperiți ofertele noastre personalizate pentr | [Rezervă pe WhatsApp Cere ofertă] | 40 | 40 | 40 | 40 |
| `div.flex` | Rezervă pe WhatsApp | Cere ofertă | -54 ¹ | -54 ¹ | -54 ¹ | 24 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 277.72 + 193.36 | 24px | 24px | da (54) |
| `div.flex` | 1024 | flex | 277.72 + 193.36 | 24px | 24px | da (54) |
| `div.flex` | 768 | flex | 277.72 + 193.36 | 24px | 24px | da (54) |
| `div.flex` | 390 | flex | 308 + 308 | 24px | 24px | da (54) |

---

## Ce nu se vede din clase

### Borduri care vin din `assets/styles.css`, nu din clase

- `div.col-span-12` «["Lumina nu doar luminează, ea transformă]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.bg-accent` «Rezervă pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «Atmosfera și Dinamica Vizuală» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Luminile de scenă nu sunt doar accesorii estetic» e 32px la 1440
- «Profesionalismul din Spatele pupitrului» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Importanța unui tehnician de lumini dedicat este» e 32px la 1440
- «Atmosfera și Dinamica Vizuală» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Luminile de scenă nu sunt doar accesorii estetic» e 32px la 1024
- «Profesionalismul din Spatele pupitrului» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Importanța unui tehnician de lumini dedicat este» e 32px la 1024
- «Atmosfera și Dinamica Vizuală» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Luminile de scenă nu sunt doar accesorii estetic» e 32px la 768
- «Profesionalismul din Spatele pupitrului» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Importanța unui tehnician de lumini dedicat este» e 32px la 768
- «Atmosfera și Dinamica Vizuală» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Luminile de scenă nu sunt doar accesorii estetic» e 32px la 390
- «Profesionalismul din Spatele pupitrului» declara `mb-*` ∈ {16}px, dar distanta reala pana la «Importanța unui tehnician de lumini dedicat este» e 32px la 390


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Importanța luminilor de scenă pentru show-ul formați | 1440: 896 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| "Lumina nu doar luminează, ea transformă spațiul înt | 1440: 706.66 · 1024: 589.33 · 768: 418.66 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Atmosfera și Dinamica Vizuală | 1440: 768 · 1024: 768 · 768: 640 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
| Plănuiți un eveniment? | 1440: 576 · 1024: 576 · 768: 542 · 390: 308 | vert (sectiune): 1440: 48 sus / 48 jos · 1024: 48 sus / 48 jos · 768: 48 sus / 48 jos · 390: 24 sus / 24 jos<br>oriz (container): 0 L / 0 R | — | — | o singura coloana |
