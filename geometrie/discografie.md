# Geometrie randata — `discografie.html`

Toate valorile de mai jos sunt **masurate in browser**, nu deduse din clase.

- Unealta: Playwright 1.55 + Chromium 1243 (`chrome-linux64`), headless, `deviceScaleFactor: 1`, `reducedMotion: no-preference`.
- Sursa: repo servit local pe `http://127.0.0.1:8099/discografie.html`.
- Asteptare inainte de citire: evenimentul `load`, apoi **injectia Tailwind Play CDN** confirmata prin `getComputedStyle(header).position === "fixed"`, apoi `document.fonts.ready`, apoi toate `<img>` cu `complete === true`.
- Nerandarea se detecteaza prin `getClientRects().length === 0`, nu prin `display` (itemii de nav au `display:block` chiar si cand parintele e ascuns).
- Viewport-uri: **1440×900, 1024×768, 768×1024, 390×844**; in tabele coloana Viewport poarta doar latimea.
- Culorile sunt convertite in hex; unde alfa < 1 se noteaza `@alfa`.
- `y` este pozitia absoluta in document (pagina nu e derulata, deci `scrollY = 0`).
- Se masoara doar continutul din `<main>`: header-ul si footer-ul sunt masurate in `RANDARE.md` / `RANDARE-MOBIL.md`.

## Cadrul paginii — `<main>`

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border |
|---|---|---|---|---|---|---|
| `<main>` | 1440 | 1440 | 2026 | 160/0/96/0 | transparent | none |
| `<main>` | 1024 | 1024 | 2066 | 160/0/96/0 | transparent | none |
| `<main>` | 768 | 768 | 3010 | 160/0/96/0 | transparent | none |
| `<main>` | 390 | 390 | 2797 | 128/0/64/0 | transparent | none |

`<body>`: font-family `Inter`, font-size `16px`, line-height `24px`, background `rgb(19, 19, 19)`.

`document.documentElement.scrollHeight`: 1440 → 2463px, 1024 → 2503px, 768 → 3499px, 390 → 3402px.

Sectiuni masurate: **3**.

---

## S1 — Hai să nu ne mai mințim

`section` · clase: `max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-margin-desktop mb-16 sm:mb-32`

Eyebrow: «Lansare Nouă 2025»

Titlu: «Hai să nu ne mai mințim»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 771 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 771 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 1653 | 0/24/0/24 | transparent | none |
| **section** | 390 | 390 | 1236 | 0/16/0/16 | transparent | none |
| **container interior** | 1440 | 1072 | 771 | 0/0/0/0 | transparent | none |
| **container interior** | 1024 | 896 | 771 | 0/0/0/0 | transparent | none |
| **container interior** | 768 | 720 | 1653 | 0/0/0/0 | transparent | none |
| **container interior** | 390 | 358 | 1236 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.lg:col-span-5`) | 1440 | 432.66 | 722.66 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.lg:col-span-5`) | 1024 | 359.33 | 677.33 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.lg:col-span-5`) | 768 | 720 | 954 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.lg:col-span-5`) | 390 | 358 | 609 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.lg:col-span-7`) | 1440 | 615.34 | 771 | 96/0/0/48 | transparent | none |
| └ coloana 2 (`div.lg:col-span-7`) | 1024 | 512.67 | 771 | 96/0/0/48 | transparent | none |
| └ coloana 2 (`div.lg:col-span-7`) | 768 | 720 | 675 | 32/0/0/0 | transparent | none |
| └ coloana 2 (`div.lg:col-span-7`) | 390 | 358 | 603 | 32/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 1440 | 185 | 161 | 430.66 | 430.66 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 1024 | 65 | 161 | 357.33 | 357.33 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 768 | 25 | 161 | 718 | 718 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| img ioana-balan-portrait-artist-muzica-populara-s.jpg | img | 390 | 17 | 129 | 356 | 356 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| Lansare Nouă 2025 | span | 1440 | 184 | 626.66 | 197.28 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Lansare Nouă 2025 | span | 1024 | 64 | 553.33 | 197.28 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Lansare Nouă 2025 | span | 768 | 24 | 914 | 197.28 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Lansare Nouă 2025 | span | 390 | 16 | 520 | 197.28 | 20 | 14 | 20 | 2.80 | 600 | #c8c6c5 | start |
| Hai să nu ne mai mințim | h1 | 1440 | 184 | 656.66 | 432.66 | 112 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Hai să nu ne mai mințim | h1 | 1024 | 64 | 583.33 | 359.33 | 112 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Hai să nu ne mai mințim | h1 | 768 | 24 | 944 | 720 | 56 | 48 | 56 | -0.96 | 500 | #e5e2e1 | start |
| Hai să nu ne mai mințim | h1 | 390 | 16 | 550 | 358 | 45 | 36 | 45 | normal | 400 | #e5e2e1 | start |
| Lansat în 2025 • Muzică de petrecere și folclor | p | 1440 | 184 | 776.66 | 432.66 | 28 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Lansat în 2025 • Muzică de petrecere și folclor | p | 1024 | 64 | 703.33 | 359.33 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Lansat în 2025 • Muzică de petrecere și folclor | p | 768 | 24 | 1008 | 720 | 28 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Lansat în 2025 • Muzică de petrecere și folclor | p | 390 | 16 | 603 | 358 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | start |
| Vezi pe YouTube | a | 1440 | 184 | 836.66 | 232.98 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| Vezi pe YouTube | a | 1024 | 64 | 791.33 | 232.98 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| Vezi pe YouTube | a | 768 | 24 | 1068 | 232.98 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| Vezi pe YouTube | a | 390 | 16 | 691 | 358 | 46 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| svg (icon) | svg | 1440 | 217 | 852.66 | 14 | 14 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| svg (icon) | svg | 1024 | 97 | 807.33 | 14 | 14 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| svg (icon) | svg | 768 | 57 | 1084 | 14 | 14 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| svg (icon) | svg | 390 | 111.50 | 707 | 14 | 14 | 14 | 20 | 1.40 | 600 | #ffffff | start |
| svg (icon) | svg | 1440 | 665.66 | 233 | 120 | 120 | 120 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 1024 | 472.33 | 233 | 120 | 120 | 120 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 768 | 1 | 1147 | 120 | 120 | 120 | 24 | normal | 400 | #e5e2e1 | start |
| svg (icon) | svg | 390 | -7 | 770 | 80 | 80 | 80 | 24 | normal | 400 | #e5e2e1 | start |
| Melodii noi Ioana Balan | h2 | 1440 | 737.66 | 305 | 469.34 | 57 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Melodii noi Ioana Balan | h2 | 1024 | 544.33 | 305 | 366.67 | 57 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Melodii noi Ioana Balan | h2 | 768 | 57 | 1203 | 654 | 57 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Melodii noi Ioana Balan | h2 | 390 | 41 | 818 | 308 | 41 | 24 | 24 | normal | 400 | #e5e2e1 | start |
| 01 | span | 1440 | 745.66 | 414 | 16.56 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 01 | span | 1024 | 552.33 | 414 | 16.56 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 01 | span | 768 | 65 | 1312 | 16.56 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 01 | span | 390 | 49 | 901 | 16.56 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Hai să nu ne mai mințim | span | 1440 | 786.22 | 410 | 202.19 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai să nu ne mai mințim | span | 1024 | 592.89 | 410 | 202.19 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai să nu ne mai mințim | span | 768 | 105.56 | 1308 | 202.19 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai să nu ne mai mințim | span | 390 | 81.56 | 899 | 179.72 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 04:15 | span | 1440 | 1157.98 | 414 | 41.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:15 | span | 1024 | 861.98 | 414 | 41.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:15 | span | 768 | 661.98 | 1312 | 41.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:15 | span | 390 | 299.98 | 901 | 41.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 02 | span | 1440 | 745.66 | 475 | 19.36 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 02 | span | 1024 | 552.33 | 475 | 19.36 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 02 | span | 768 | 65 | 1373 | 19.36 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 02 | span | 390 | 49 | 958 | 19.36 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Bărbățelul meu | span | 1440 | 789.02 | 471 | 127.80 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Bărbățelul meu | span | 1024 | 595.69 | 471 | 127.80 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Bărbățelul meu | span | 768 | 108.36 | 1369 | 127.80 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Bărbățelul meu | span | 390 | 84.36 | 956 | 113.59 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 04:22 | span | 1440 | 1155.03 | 475 | 43.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:22 | span | 1024 | 859.03 | 475 | 43.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:22 | span | 768 | 659.03 | 1373 | 43.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:22 | span | 390 | 297.03 | 958 | 43.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03 | span | 1440 | 745.66 | 536 | 19.55 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 03 | span | 1024 | 552.33 | 536 | 19.55 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 03 | span | 768 | 65 | 1434 | 19.55 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 03 | span | 390 | 49 | 1015 | 19.55 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Fratele rămâne frate | span | 1440 | 789.20 | 532 | 171.81 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Fratele rămâne frate | span | 1024 | 595.88 | 532 | 171.81 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Fratele rămâne frate | span | 768 | 108.55 | 1430 | 171.81 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Fratele rămâne frate | span | 390 | 84.55 | 1013 | 152.72 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 04:12 | span | 1440 | 1157.83 | 536 | 41.17 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:12 | span | 1024 | 861.83 | 536 | 41.17 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:12 | span | 768 | 661.83 | 1434 | 41.17 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:12 | span | 390 | 299.83 | 1015 | 41.17 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04 | span | 1440 | 745.66 | 597 | 19.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 04 | span | 1024 | 552.33 | 597 | 19.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 04 | span | 768 | 65 | 1495 | 19.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 04 | span | 390 | 49 | 1072 | 19.97 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Ține minte omule | span | 1440 | 789.63 | 593 | 146.27 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Ține minte omule | span | 1024 | 596.30 | 593 | 146.27 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Ține minte omule | span | 768 | 108.97 | 1491 | 146.27 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Ține minte omule | span | 390 | 84.97 | 1070 | 130.02 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 03:28 | span | 1440 | 1155.20 | 597 | 43.80 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:28 | span | 1024 | 859.20 | 597 | 43.80 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:28 | span | 768 | 659.20 | 1495 | 43.80 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:28 | span | 390 | 297.20 | 1072 | 43.80 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 05 | span | 1440 | 745.66 | 658 | 19.22 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 05 | span | 1024 | 552.33 | 658 | 19.22 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 05 | span | 768 | 65 | 1556 | 19.22 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 05 | span | 390 | 49 | 1129 | 19.22 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Varsă țara lacrimi grele | span | 1440 | 788.88 | 654 | 195.13 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Varsă țara lacrimi grele | span | 1024 | 595.55 | 654 | 195.13 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Varsă țara lacrimi grele | span | 768 | 108.22 | 1552 | 195.13 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Varsă țara lacrimi grele | span | 390 | 84.22 | 1127 | 173.44 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 03:45 | span | 1440 | 1154.98 | 658 | 44.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:45 | span | 1024 | 858.98 | 658 | 44.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:45 | span | 768 | 658.98 | 1556 | 44.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:45 | span | 390 | 296.98 | 1129 | 44.02 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 06 | span | 1440 | 745.66 | 719 | 19.59 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 06 | span | 1024 | 552.33 | 719 | 19.59 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 06 | span | 768 | 65 | 1617 | 19.59 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 06 | span | 390 | 49 | 1186 | 19.59 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Dragoste mare | span | 1440 | 789.25 | 715 | 125.33 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Dragoste mare | span | 1024 | 595.92 | 715 | 125.33 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Dragoste mare | span | 768 | 108.59 | 1613 | 125.33 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Dragoste mare | span | 390 | 84.59 | 1184 | 111.41 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 04:58 | span | 1440 | 1154.94 | 719 | 44.06 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:58 | span | 1024 | 858.94 | 719 | 44.06 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:58 | span | 768 | 658.94 | 1617 | 44.06 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:58 | span | 390 | 296.94 | 1186 | 44.06 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 07 | span | 1440 | 745.66 | 780 | 18.44 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 07 | span | 1024 | 552.33 | 780 | 18.44 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 07 | span | 768 | 65 | 1678 | 18.44 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 07 | span | 390 | 49 | 1243 | 18.44 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Hai murgule-n vale | span | 1440 | 788.09 | 776 | 161.30 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai murgule-n vale | span | 1024 | 594.77 | 776 | 161.30 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai murgule-n vale | span | 768 | 107.44 | 1674 | 161.30 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Hai murgule-n vale | span | 390 | 83.44 | 1241 | 143.38 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 03:50 | span | 1440 | 1155.08 | 780 | 43.92 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:50 | span | 1024 | 859.08 | 780 | 43.92 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:50 | span | 768 | 659.08 | 1678 | 43.92 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 03:50 | span | 390 | 297.08 | 1243 | 43.92 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 08 | span | 1440 | 745.66 | 841 | 19.61 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 08 | span | 1024 | 552.33 | 841 | 19.61 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 08 | span | 768 | 65 | 1739 | 19.61 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| 08 | span | 390 | 49 | 1300 | 19.61 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 @0.5 | start |
| Să merg la părinți acasă | span | 1440 | 789.27 | 837 | 203.77 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Să merg la părinți acasă | span | 1024 | 595.94 | 837 | 203.77 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Să merg la părinți acasă | span | 768 | 108.61 | 1735 | 203.77 | 28 | 18 | 28 | normal | 400 | #e5e2e1 | start |
| Să merg la părinți acasă | span | 390 | 84.61 | 1298 | 181.13 | 24 | 16 | 24 | normal | 400 | #e5e2e1 | start |
| 04:05 | span | 1440 | 1154.66 | 841 | 44.34 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:05 | span | 1024 | 858.66 | 841 | 44.34 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:05 | span | 768 | 658.66 | 1739 | 44.34 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |
| 04:05 | span | 390 | 296.66 | 1300 | 44.34 | 20 | 14 | 20 | 0.70 | 600 | #8e9192 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.grid` | [Lansare Nouă 2025 Hai să nu ne mai minți] | [Melodii noi Ioana Balan 01 Hai să nu ne ] | -722.66 ¹ | -677.33 ¹ | 24 | 24 |
| `div.lg:col-span-5` | div.aspect-square | [Lansare Nouă 2025 Hai să nu ne mai minți] | 32 | 32 | 32 | 32 |
| `div.mt-8` | [Lansare Nouă 2025] | Hai să nu ne mai mințim | 8 | 8 | 8 | 8 |
| `div.mt-8` | Hai să nu ne mai mințim | Lansat în 2025 • Muzică de petrecere și folclor | 8 | 8 | 8 | 8 |
| `div.mt-8` | Lansat în 2025 • Muzică de petrecere și folclor | [Vezi pe YouTube] | 32 | 32 | 32 | 32 |
| `div.flex` | Lansare Nouă 2025 | div.motif-separator | -22 ¹ | -22 ¹ | -22 ¹ | -22 ¹ |
| `div.glass-card` | div.absolute | Melodii noi Ioana Balan | -48 | -48 | -64 | -32 |
| `div.glass-card` | Melodii noi Ioana Balan | [01 Hai să nu ne mai mințim 04:15 02 Bărb] | 32 | 32 | 32 | 24 |
| `ul.space-y-0` | [01 Hai să nu ne mai mințim 04:15] | [02 Bărbățelul meu 04:22] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [02 Bărbățelul meu 04:22] | [03 Fratele rămâne frate 04:12] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [03 Fratele rămâne frate 04:12] | [04 Ține minte omule 03:28] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [04 Ține minte omule 03:28] | [05 Varsă țara lacrimi grele 03:45] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [05 Varsă țara lacrimi grele 03:45] | [06 Dragoste mare 04:58] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [06 Dragoste mare 04:58] | [07 Hai murgule-n vale 03:50] | 0 | 0 | 0 | 0 |
| `ul.space-y-0` | [07 Hai murgule-n vale 03:50] | [08 Să merg la părinți acasă 04:05] | 0 | 0 | 0 | 0 |
| `li.flex` | [01 Hai să nu ne mai mințim] | 04:15 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 01 | Hai să nu ne mai mințim | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [02 Bărbățelul meu] | 04:22 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 02 | Bărbățelul meu | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [03 Fratele rămâne frate] | 04:12 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 03 | Fratele rămâne frate | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [04 Ține minte omule] | 03:28 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 04 | Ține minte omule | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [05 Varsă țara lacrimi grele] | 03:45 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 05 | Varsă țara lacrimi grele | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [06 Dragoste mare] | 04:58 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 06 | Dragoste mare | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [07 Hai murgule-n vale] | 03:50 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 07 | Hai murgule-n vale | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `li.flex` | [08 Să merg la părinți acasă] | 04:05 | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |
| `div.flex` | 08 | Să merg la părinți acasă | -24 ¹ | -24 ¹ | -24 ¹ | -22 ¹ |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px 67.3281px | 24px | 24px | **NU** — 722.66…771, delta 48.34 |
| `div.grid` | 1024 | grid | 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px 52.6562px | 24px | 24px | **NU** — 677.33…771, delta 93.67 |
| `div.grid` | 768 | grid | 720px | 24px | 24px | **NU** — 675…954, delta 279 |
| `div.grid` | 390 | grid | 358px | 24px | 24px | **NU** — 603…609, delta 6 |
| `div.flex` | 1440 | flex | 197.28 + 219.38 | 16px | 16px | **NU** — 20…24, delta 4 |
| `div.flex` | 1024 | flex | 197.28 + 146.05 | 16px | 16px | **NU** — 20…24, delta 4 |
| `div.flex` | 768 | flex | 197.28 + 506.72 | 16px | 16px | **NU** — 20…24, delta 4 |
| `div.flex` | 390 | flex | 197.28 + 144.72 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 242.75 + 41.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 242.75 + 41.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 242.75 + 41.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 212.28 + 41.02 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 16.56 + 202.19 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 16.56 + 202.19 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 16.56 + 202.19 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 16.56 + 179.72 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 171.16 + 43.97 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 171.16 + 43.97 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 171.16 + 43.97 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 148.95 + 43.97 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.36 + 127.80 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.36 + 127.80 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.36 + 127.80 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.36 + 113.59 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 215.36 + 41.17 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 215.36 + 41.17 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 215.36 + 41.17 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 188.27 + 41.17 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.55 + 171.81 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.55 + 171.81 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.55 + 171.81 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.55 + 152.72 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 190.23 + 43.80 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 190.23 + 43.80 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 190.23 + 43.80 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 165.98 + 43.80 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.97 + 146.27 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.97 + 146.27 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.97 + 146.27 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.97 + 130.02 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 238.34 + 44.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 238.34 + 44.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 238.34 + 44.02 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 208.66 + 44.02 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.22 + 195.13 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.22 + 195.13 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.22 + 195.13 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.22 + 173.44 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 168.92 + 44.06 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 168.92 + 44.06 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 168.92 + 44.06 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 147 + 44.06 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.59 + 125.33 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.59 + 125.33 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.59 + 125.33 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.59 + 111.41 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 203.73 + 43.92 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 203.73 + 43.92 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 203.73 + 43.92 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 177.81 + 43.92 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 18.44 + 161.30 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 18.44 + 161.30 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 18.44 + 161.30 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 18.44 + 143.38 | 16px | 16px | **NU** — 20…24, delta 4 |
| `li.flex` | 1440 | flex | 247.38 + 44.34 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 1024 | flex | 247.38 + 44.34 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 768 | flex | 247.38 + 44.34 | 0px | 0px | **NU** — 20…28, delta 8 |
| `li.flex` | 390 | flex | 216.73 + 44.34 | 0px | 0px | **NU** — 20…24, delta 4 |
| `div.flex` | 1440 | flex | 19.61 + 203.77 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 1024 | flex | 19.61 + 203.77 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 768 | flex | 19.61 + 203.77 | 24px | 24px | **NU** — 20…28, delta 8 |
| `div.flex` | 390 | flex | 19.61 + 181.13 | 16px | 16px | **NU** — 20…24, delta 4 |

---

## S2 — Arhiva Sonoră Ioana Balan

`section` · clase: `max-w-[1200px] mx-auto px-4 sm:px-6 lg:px-margin-desktop`

Eyebrow: «Colecție 2021»

Titlu: «Arhiva Sonoră Ioana Balan»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1200 | 570 | 0/64/0/64 | transparent | none |
| **section** | 1024 | 1024 | 570 | 0/64/0/64 | transparent | none |
| **section** | 768 | 768 | 570 | 0/24/0/24 | transparent | none |
| **section** | 390 | 390 | 936 | 0/16/0/16 | transparent | none |
| **container 1** (`div.mb-12`) | 1440 | 1072 | 72 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-12`) | 1024 | 896 | 72 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-12`) | 768 | 720 | 72 | 0/0/0/0 | transparent | none |
| **container 1** (`div.mb-12`) | 390 | 358 | 56 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-headline-lg`) | 1440 | 337.92 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-headline-lg`) | 1024 | 337.92 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-headline-lg`) | 768 | 337.92 | 40 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`h2.font-headline-lg`) | 390 | 286.11 | 24 | 0/0/0/0 | transparent | none |
| └ coloana 2 (`div.motif-separator`) | 1440 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.motif-separator`) | 1024 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.motif-separator`) | 768 | 144 | 24 | 0/0/0/0 |  +bg-image | none |
| └ coloana 2 (`div.motif-separator`) | 390 | 96 | 24 | 0/0/0/0 |  +bg-image | none |
| **container 2** (`div.grid`) | 1440 | 1072 | 450 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 1024 | 896 | 450 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 768 | 720 | 450 | 0/0/0/0 | transparent | none |
| **container 2** (`div.grid`) | 390 | 358 | 832 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.glass-card`) | 1440 | 520 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-card`) | 1024 | 432 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-card`) | 768 | 344 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 1 (`div.glass-card`) | 390 | 358 | 400 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 2 (`div.glass-card`) | 1440 | 520 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 2 (`div.glass-card`) | 1024 | 432 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 2 (`div.glass-card`) | 768 | 344 | 450 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |
| └ coloana 2 (`div.glass-card`) | 390 | 358 | 400 | 0/0/0/0 | #1c1b1b | T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15 |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arhiva Sonoră Ioana Balan | h2 | 1440 | 551.03 | 1059 | 337.92 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Arhiva Sonoră Ioana Balan | h2 | 1024 | 343.03 | 1059 | 337.92 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Arhiva Sonoră Ioana Balan | h2 | 768 | 215.03 | 1941 | 337.92 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Arhiva Sonoră Ioana Balan | h2 | 390 | 51.94 | 1428 | 286.11 | 24 | 28 | 24 | normal | 400 | #e5e2e1 | center |
| Colecție 2021 | span | 1440 | 225 | 1408 | 438 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Colecție 2021 | span | 1024 | 105 | 1384 | 350 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Colecție 2021 | span | 768 | 65 | 2242 | 262 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Colecție 2021 | span | 390 | 41 | 1719 | 308 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Glasul Inimii | h3 | 1440 | 225 | 1436 | 438 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Glasul Inimii | h3 | 1024 | 105 | 1412 | 350 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Glasul Inimii | h3 | 768 | 65 | 2270 | 262 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Glasul Inimii | h3 | 390 | 41 | 1747 | 308 | 24 | 24 | 24 | normal | 400 | #e5e2e1 | start |
| O explorare intimă a doinelor tradiționale român | p | 1440 | 225 | 1492 | 438 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| O explorare intimă a doinelor tradiționale român | p | 1024 | 105 | 1468 | 350 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| O explorare intimă a doinelor tradiționale român | p | 768 | 65 | 2326 | 262 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| O explorare intimă a doinelor tradiționale român | p | 390 | 41 | 1787 | 308 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Vezi Colecția | a | 1440 | 225 | 1567 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 1024 | 105 | 1567 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 768 | 65 | 2449 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 390 | 41 | 1886 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1440 | 348.39 | 1570 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 228.39 | 1570 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 188.39 | 2452 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 164.39 | 1889 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Debut 2018 | span | 1440 | 777 | 1408 | 438 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Debut 2018 | span | 1024 | 569 | 1384 | 350 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Debut 2018 | span | 768 | 441 | 2242 | 262 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Debut 2018 | span | 390 | 41 | 2151 | 308 | 20 | 14 | 20 | 1.40 | 600 | #c8c6c5 | start |
| Rădăcini | h3 | 1440 | 777 | 1436 | 438 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h3 | 1024 | 569 | 1412 | 350 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h3 | 768 | 441 | 2270 | 262 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | start |
| Rădăcini | h3 | 390 | 41 | 2179 | 308 | 24 | 24 | 24 | normal | 400 | #e5e2e1 | start |
| Albumul de debut care a definit o nouă eră a int | p | 1440 | 777 | 1492 | 438 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Albumul de debut care a definit o nouă eră a int | p | 1024 | 569 | 1468 | 350 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Albumul de debut care a definit o nouă eră a int | p | 768 | 441 | 2326 | 262 | 96 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Albumul de debut care a definit o nouă eră a int | p | 390 | 41 | 2219 | 308 | 72 | 16 | 24 | normal | 400 | #c6c6c6 | start |
| Vezi Colecția | a | 1440 | 777 | 1567 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 1024 | 569 | 1567 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 768 | 441 | 2449 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| Vezi Colecția | a | 390 | 41 | 2318 | 137.39 | 20 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1440 | 900.39 | 1570 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 1024 | 692.39 | 1570 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 768 | 564.39 | 2452 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |
| svg (icon) | svg | 390 | 164.39 | 2321 | 14 | 14 | 14 | 20 | 0.70 | 600 | #c8c6c5 | start |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `section` | [Arhiva Sonoră Ioana Balan] | [Colecție 2021 Glasul Inimii O explorare ] | 48 | 48 | 48 | 48 |
| `div.mb-12` | Arhiva Sonoră Ioana Balan | div.motif-separator | 8 | 8 | 8 | 8 |
| `div.grid` | [Colecție 2021 Glasul Inimii O explorare ] | [Debut 2018 Rădăcini Albumul de debut car] | -450 ¹ | -450 ¹ | -450 ¹ | 32 |
| `div.glass-card` | div.absolute | div.absolute | -448 | -448 | -448 | -398 |
| `div.glass-card` | div.absolute | [Colecție 2021 Glasul Inimii O explorare ] | -260 | -284 | -308 | -236 |
| `div.absolute` | Colecție 2021 | Glasul Inimii | 8 | 8 | 8 | 8 |
| `div.absolute` | Glasul Inimii | O explorare intimă a doinelor tradiționale român | 16 | 16 | 16 | 16 |
| `div.absolute` | O explorare intimă a doinelor tradiționale român | Vezi Colecția | 27 | 27 | 27 | 27 |
| `div.glass-card` | div.absolute | div.absolute | -448 | -448 | -448 | -398 |
| `div.glass-card` | div.absolute | [Debut 2018 Rădăcini Albumul de debut car] | -260 | -284 | -308 | -236 |
| `div.absolute` | Debut 2018 | Rădăcini | 8 | 8 | 8 | 8 |
| `div.absolute` | Rădăcini | Albumul de debut care a definit o nouă eră a int | 16 | 16 | 16 | 16 |
| `div.absolute` | Albumul de debut care a definit o nouă eră a int | Vezi Colecția | 27 | 27 | 27 | 27 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.grid` | 1440 | grid | 520px 520px | 32px | 32px | da (450) |
| `div.grid` | 1024 | grid | 432px 432px | 32px | 32px | da (450) |
| `div.grid` | 768 | grid | 344px 344px | 32px | 32px | da (450) |
| `div.grid` | 390 | grid | 358px | 32px | 32px | da (400) |

---

## S3 — Îți place ce auzi? Rezervă data ta.

`section` · clase: `py-16 md:py-24 bg-surface-container-low border-t border-outline-variant/10`

Titlu: «Îți place ce auzi? Rezervă data ta.»

**Tabel 1 — cutia**

| Nivel | Viewport | width | height | pad T/R/B/L | bg | border (latura, latime, culoare rezolvata) |
|---|---|---|---|---|---|---|
| **section** | 1440 | 1440 | 301 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 1024 | 1024 | 341 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 768 | 768 | 403 | 96/0/96/0 | #1c1b1b | T 1px #444748 @0.1 |
| **section** | 390 | 390 | 369 | 64/0/64/0 | #1c1b1b | T 1px #444748 @0.1 |
| **container interior** | 1440 | 1200 | 108 | 0/64/0/64 | transparent | none |
| **container interior** | 1024 | 1024 | 148 | 0/64/0/64 | transparent | none |
| **container interior** | 768 | 768 | 210 | 0/64/0/64 | transparent | none |
| **container interior** | 390 | 390 | 240 | 0/16/0/16 | transparent | none |
| └ coloana 1 (`div.flex`) | 1440 | 1072 | 108 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 1024 | 896 | 148 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 768 | 640 | 210 | 0/0/0/0 | transparent | none |
| └ coloana 1 (`div.flex`) | 390 | 358 | 240 | 0/0/0/0 | transparent | none |

**Tabel 2 — elementele, in ordinea documentului**

| Element | Tag | Viewport | x | y | width | height | font-size | line-height | letter-spacing | font-weight | color | text-align |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Îți place ce auzi? Rezervă data ta. | h2 | 1440 | 184 | 1726 | 568.92 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | left |
| Îți place ce auzi? Rezervă data ta. | h2 | 1024 | 64 | 1726 | 392.92 | 80 | 32 | 40 | normal | 500 | #e5e2e1 | left |
| Îți place ce auzi? Rezervă data ta. | h2 | 768 | 64 | 2608 | 576 | 40 | 32 | 40 | normal | 500 | #e5e2e1 | center |
| Îți place ce auzi? Rezervă data ta. | h2 | 390 | 16 | 2429 | 358 | 24 | 26 | 24 | normal | 400 | #e5e2e1 | center |
| Spuneți-ne data și locația — revenim în aceeași  | p | 1440 | 184 | 1778 | 568.92 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | left |
| Spuneți-ne data și locația — revenim în aceeași  | p | 1024 | 64 | 1818 | 392.92 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | left |
| Spuneți-ne data și locația — revenim în aceeași  | p | 768 | 64 | 2660 | 576 | 56 | 18 | 28 | normal | 400 | #c6c6c6 | center |
| Spuneți-ne data și locația — revenim în aceeași  | p | 390 | 16 | 2465 | 358 | 48 | 16 | 24 | normal | 400 | #c6c6c6 | center |
| Rezervă pe WhatsApp | a | 1440 | 800.92 | 1753 | 261.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 1024 | 504.92 | 1773 | 261.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 768 | 64 | 2764 | 261.72 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Rezervă pe WhatsApp | a | 390 | 16 | 2545 | 358 | 54 | 14 | 20 | 1.40 | 600 | #ffffff | center |
| Cere ofertă | a | 1440 | 1078.64 | 1753 | 177.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 1024 | 782.64 | 1773 | 177.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 768 | 341.72 | 2764 | 177.36 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |
| Cere ofertă | a | 390 | 16 | 2615 | 358 | 54 | 14 | 20 | 1.40 | 600 | #e5e2e1 | center |

**Tabel 3 — distantele reale** (`rect.top` al urmatorului − `rect.bottom` al precedentului, intre frati consecutivi)

| Container | De la | Pana la | 1440 | 1024 | 768 | 390 |
|---|---|---|---|---|---|---|
| `div.flex` | [Îți place ce auzi? Rezervă data ta. Spun] | [Rezervă pe WhatsApp Cere ofertă] | -81 ¹ | -101 ¹ | 48 | 32 |
| `div.max-w-xl` | Îți place ce auzi? Rezervă data ta. | Spuneți-ne data și locația — revenim în aceeași  | 12 | 12 | 12 | 12 |
| `div.flex` | Rezervă pe WhatsApp | Cere ofertă | -54 ¹ | -54 ¹ | -54 ¹ | 16 |

¹ = cele doua elemente sunt asezate **alaturi**, nu una sub alta (fara suprapunere orizontala); diferenta verticala nu e o distanta de flux.

**Tabel 4 — grile**

| Container | Viewport | display | coloane rezolvate (px) | gap x | gap y | inaltimi egale? |
|---|---|---|---|---|---|---|
| `div.flex` | 1440 | flex | 568.92 + 455.08 | 48px | 48px | **NU** — 54…108, delta 54 |
| `div.flex` | 1024 | flex | 392.92 + 455.08 | 48px | 48px | **NU** — 54…148, delta 94 |
| `div.flex` | 768 | flex | 576 + 640 | 48px | 48px | **NU** — 54…108, delta 54 |
| `div.flex` | 390 | flex | 358 + 358 | 32px | 32px | **NU** — 84…124, delta 40 |
| `div.flex` | 1440 | flex | 261.72 + 177.36 | 16px | 16px | da (54) |
| `div.flex` | 1024 | flex | 261.72 + 177.36 | 16px | 16px | da (54) |
| `div.flex` | 768 | flex | 261.72 + 177.36 | 16px | 16px | da (54) |
| `div.flex` | 390 | flex | 358 + 358 | 16px | 16px | da (54) |

---

## Ce nu se vede din clase

### `line-height` mostenit de la `<body>`, nu setat pe element

- `h2` «Melodii noi Ioana Balan» la 390 — font-size 24px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 1.00)
- `h2` «Arhiva Sonoră Ioana Balan» la 390 — font-size 28px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.86)
- `h3` «Glasul Inimii» la 390 — font-size 24px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 1.00)
- `h3` «Rădăcini» la 390 — font-size 24px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 1.00)
- `h2` «Îți place ce auzi? Rezervă data ta.» la 390 — font-size 26px dar line-height 24px, adica exact valoarea mostenita de la `<body>`; nu e setata pe element (raport 0.92)

### `font-weight` diferit de ce sugereaza numele clasei

- `h1` «Hai să nu ne mai mințim» — `font-display-lg` (tokenul poarta weight) + marime arbitrara `text-[36px]`; weight rezolvat 400/500, font-size masurat 36/48px
- `h2` «Melodii noi Ioana Balan» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `span` «Hai să nu ne mai mințim» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Bărbățelul meu» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Fratele rămâne frate» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Ține minte omule» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Varsă țara lacrimi grele» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Dragoste mare» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Hai murgule-n vale» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `span` «Să merg la părinți acasă» — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px
- `h2` «Arhiva Sonoră Ioana Balan» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[28px]`; weight rezolvat 400/500, font-size masurat 28/32px
- `h3` «Glasul Inimii» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h3` «Rădăcini» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[24px]`; weight rezolvat 400/500, font-size masurat 24/32px
- `h2` «Îți place ce auzi? Rezervă data ta.» — `font-headline-lg` (tokenul poarta weight) + marime arbitrara `text-[26px]`; weight rezolvat 400/500, font-size masurat 26/32px
- `p` «Spuneți-ne data și locația — revenim în aceeași » — `font-body-lg` (tokenul poarta weight) + marime arbitrara `text-[16px]`; weight rezolvat 400, font-size masurat 16/18px

### Borduri care vin din `assets/styles.css`, nu din clase

- `a.w-full` «Vezi pe YouTube» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `div.glass-card` «[Melodii noi Ioana Balan 01 Hai să nu ne ]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `div.glass-card` «[Colecție 2021 Glasul Inimii O explorare ]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `div.glass-card` «[Debut 2018 Rădăcini Albumul de debut car]» — T 1px #8e9192 @0.15, R 1px #8e9192 @0.15, B 1px #8e9192 @0.15, L 1px #8e9192 @0.15, fara nicio clasa `border-*`; vine din `assets/styles.css`
- `a.bg-accent` «Rezervă pe WhatsApp» — T 1px #c41236, R 1px #c41236, B 1px #c41236, L 1px #c41236, fara nicio clasa `border-*`; vine din `assets/styles.css`

### Distante reale diferite de marginile declarate

- «O explorare intimă a doinelor tradiționale român» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 1440
- «O explorare intimă a doinelor tradiționale român» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 1024
- «O explorare intimă a doinelor tradiționale român» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 768
- «O explorare intimă a doinelor tradiționale român» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 390
- «Albumul de debut care a definit o nouă eră a int» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 1440
- «Albumul de debut care a definit o nouă eră a int» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 1024
- «Albumul de debut care a definit o nouă eră a int» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 768
- «Albumul de debut care a definit o nouă eră a int» declara `mb-*` ∈ {24}px, dar distanta reala pana la «Vezi Colecția» e 27px la 390

### Suprapuneri intre elemente

- in `div.glass-card`: «div.absolute» si «Melodii noi Ioana Balan» se suprapun pe verticala cu 48px la 1440 (suprapunere orizontala 48px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «Melodii noi Ioana Balan» se suprapun pe verticala cu 48px la 1024 (suprapunere orizontala 48px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «Melodii noi Ioana Balan» se suprapun pe verticala cu 64px la 768 (suprapunere orizontala 64px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «Melodii noi Ioana Balan» se suprapun pe verticala cu 32px la 390 (suprapunere orizontala 32px, position absolute/static) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «div.absolute» se suprapun pe verticala cu 448px la 1440 (suprapunere orizontala 518px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Colecție 2021 Glasul Inimii O explorare ]» se suprapun pe verticala cu 260px la 1440 (suprapunere orizontala 518px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «div.absolute» se suprapun pe verticala cu 448px la 1024 (suprapunere orizontala 430px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Colecție 2021 Glasul Inimii O explorare ]» se suprapun pe verticala cu 284px la 1024 (suprapunere orizontala 430px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «div.absolute» se suprapun pe verticala cu 448px la 768 (suprapunere orizontala 342px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Colecție 2021 Glasul Inimii O explorare ]» se suprapun pe verticala cu 308px la 768 (suprapunere orizontala 342px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «div.absolute» se suprapun pe verticala cu 398px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Colecție 2021 Glasul Inimii O explorare ]» se suprapun pe verticala cu 236px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Debut 2018 Rădăcini Albumul de debut car]» se suprapun pe verticala cu 260px la 1440 (suprapunere orizontala 518px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Debut 2018 Rădăcini Albumul de debut car]» se suprapun pe verticala cu 284px la 1024 (suprapunere orizontala 430px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Debut 2018 Rădăcini Albumul de debut car]» se suprapun pe verticala cu 308px la 768 (suprapunere orizontala 342px, position absolute/absolute) — stratificare intentionata (`position: absolute`)
- in `div.glass-card`: «div.absolute» si «[Debut 2018 Rădăcini Albumul de debut car]» se suprapun pe verticala cu 236px la 390 (suprapunere orizontala 356px, position absolute/absolute) — stratificare intentionata (`position: absolute`)


## Mapare Elementor

In Tailwind `box-sizing: border-box` — padding-ul e **inclus** in latimea masurata. In Elementor `boxed_width` e latimea **continutului**, iar padding-ul se adauga **in afara** ei.

Coloana `boxed_width` de mai jos e deja convertita: `width masurat − padding-left − padding-right`. Verificare: `boxed_width + padding-L + padding-R` = latimea masurata a containerului.

| Sectiune | boxed_width | padding container | padding coloane | flex_gap | latimi coloane |
|---|---|---|---|---|---|
| Hai să nu ne mai mințim | 1440: 1072 · 1024: 896 · 768: 720 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 24 L / 24 R · 390: 16 L / 16 R | 1440: 0/0/0/0 / 96/0/0/48<br>1024: 0/0/0/0 / 96/0/0/48<br>768: 0/0/0/0 / 32/0/0/0<br>390: 0/0/0/0 / 32/0/0/0 | x 24px / y 24px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 432.66 + 615.34 · 1024: 359.33 + 512.67 · 768: 720 + 720 · 390: 358 + 358 |
| Arhiva Sonoră Ioana Balan | 1440: 1072 · 1024: 896 · 768: 720 · 390: 358 | vert (sectiune): 0 sus / 0 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 24 L / 24 R · 390: 16 L / 16 R | 0/0/0/0 | x 32px / y 32px | in `div.grid` (lat. 1072 la 1440, grid):<br>1440: 520 + 520 · 1024: 432 + 432 · 768: 344 + 344 · 390: 358 + 358 |
| Îți place ce auzi? Rezervă data ta. | 1440: 1072 · 1024: 896 · 768: 640 · 390: 358 | vert (sectiune): 1440: 96 sus / 96 jos · 1024: 96 sus / 96 jos · 768: 96 sus / 96 jos · 390: 64 sus / 64 jos<br>oriz (container): 1440: 64 L / 64 R · 1024: 64 L / 64 R · 768: 64 L / 64 R · 390: 16 L / 16 R | 0/0/0/0 | 1440: x 48px / y 48px · 1024: x 48px / y 48px · 768: x 48px / y 48px · 390: x 32px / y 32px | in `div.flex` (lat. 1072 la 1440, flex):<br>1440: 568.92 + 455.08 · 1024: 392.92 + 455.08 · 768: 576 + 640 · 390: 358 + 358 |
