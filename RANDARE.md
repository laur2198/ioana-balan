# RANDARE — geometrie măsurată în browser, în pixeli

Valorile din acest document sunt **MĂSURATE** cu `getBoundingClientRect()` și
`getComputedStyle()` într-un Chromium real, nu deduse din clasele Tailwind.
Nu conține recomandări.

---

## STARE GIT

| Element | Valoare |
|---|---|
| Branch curent | `main` |
| Upstream | `origin/main` (https://github.com/laur2198/ioana-balan) |
| Working tree la start | curat — `nothing to commit, working tree clean` |
| Commit-uri nepushate la start | **0** — `git log origin/main..HEAD` returnează listă goală |
| HEAD la start | `64ab119` — *docs: geometrie rezolvata in px pentru header si footer* |

Fișier nou scris de această rulare: `RANDARE.md`. Niciun fișier existent nu
a fost modificat.

---

## METODĂ

**Playwright a putut fi instalat.** Toate valorile din tabele sunt MĂSURATE.
Nicio valoare nu este dedusă din clase; unde un element nu a putut fi
măsurat, celula spune **nerandat** și motivul e explicat, nu înlocuit cu un
calcul.

| Aspect | Valoare |
|---|---|
| Server local | `python3 -m http.server 8127 --bind 127.0.0.1`, servind rădăcina repo-ului |
| URL măsurat | `http://127.0.0.1:8127/index.html` |
| Playwright | `playwright@1.63.0` (`npx playwright install --with-deps chromium`) |
| **Chromium** | **Chrome for Testing 153.0.8010.12** (build Playwright `chromium-1243`) |
| Mod | headless, `deviceScaleFactor: 1` |
| Așteptare la încărcare | `waitUntil: 'networkidle'` |
| Așteptare pentru Tailwind | `waitForFunction` până când `getComputedStyle(header).position === 'fixed'` — Tailwind Play CDN injectează `<style>` la runtime, iar fără această așteptare toate cutiile s-ar fi măsurat pe HTML nestilizat |
| **Așteptare fonturi** | **`await document.fonts.ready`**, apoi verificat `document.fonts.status` |
| **`document.fonts.status` la măsurare** | **`loaded`** la toate trei viewport-urile |
| Tampon suplimentar | 400ms după `fonts.ready` |
| Rulări | două treceri cu aceeași configurație: una pentru cutii și distanțe, a doua pentru perechile de distanțe și padding-urile de container care lipseau din prima |
| Viewport-uri | **1440×900**, **1024×768**, **390×844** |
| Bară de derulare verticală | 0px la toate trei (`window.innerWidth − documentElement.clientWidth`), deci `clientWidth` = lățimea viewportului: 1440 / 1024 / 390 |

Fonturile sunt self-hostate din `assets/fonts/`, deci `fonts.ready` s-a
rezolvat pe fișiere locale — lățimile de text de mai jos sunt cele finale,
nu cele de fallback.

### Ce înseamnă „nerandat"

Celulele marcate **nerandat** sunt elemente pentru care
`el.getClientRects().length === 0` — nu au cutie de randare. Detecția se
face pe `getClientRects()`, nu pe `getComputedStyle(el).display`, pentru că
itemii de nav au ei înșiși `display: block`; doar părintele `<nav>` e
`display: none` sub 1024px. Verificat pe `display` singur, cei 7 itemi ar fi
raportat cutii de 0×0 la coordonata 0,0 — valori false, care arată ca
măsurători.

| Viewport | Elemente nerandate |
|---|---|
| 1440×900 | link telefon (header), buton hamburger |
| 1024×768 | link telefon (header), buton hamburger |
| 390×844 | `<nav>` desktop, cei 7 itemi de nav, CTA WhatsApp (header) |

### Convenții

- Valorile sunt în px, cu două zecimale acolo unde nu sunt întregi.
- `y` este absolut în document (`rect.top + window.scrollY`), nu relativ la viewport.
- Culorile sunt convertite din `rgb()`/`rgba()` în hex; unde alfa < 1, e notat `#hex @ alfa`.
- `transparent` = `rgba(0,0,0,0)`.
- `x`/`width`/`height` sunt de pe cutia de bord (border-box), ca `getBoundingClientRect()`.

---

# CUTIILE ELEMENTELOR

### Header

| Element | Viewport | x | y | width | height | pad T/R/B/L | margin T/R/B/L | font-size | line-height | letter-spacing | font-weight | color | background |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `<header>` | 1440×900 | 0 | 0 | 1440 | 80 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #131313 @ 0.95 |
| `<header>` | 1024×768 | 0 | 0 | 1024 | 80 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #131313 @ 0.95 |
| `<header>` | 390×844 | 0 | 0 | 390 | 64 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #131313 @ 0.95 |
| container interior header | 1440×900 | 120 | 0 | 1200 | 79 | 0 / 64 / 0 / 64 | 0 / 120 / 0 / 120 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container interior header | 1024×768 | 0 | 0 | 1024 | 79 | 0 / 64 / 0 / 64 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container interior header | 390×844 | 0 | 0 | 390 | 63 | 0 / 16 / 0 / 16 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (header) | 1440×900 | 184 | 15.50 | 140.14 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (header) | 1024×768 | 64 | 15.50 | 140.14 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (header) | 390×844 | 16 | 9.50 | 93.42 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (header) | 1440×900 | 184 | 15.50 | 140.14 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (header) | 1024×768 | 64 | 15.50 | 140.14 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (header) | 390×844 | 16 | 15.50 | 93.42 | 32 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<nav>` desktop | 1440×900 | 362.34 | 29.50 | 611.84 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<nav>` desktop | 1024×768 | 220.14 | 29.50 | 515.84 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<nav>` desktop | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 1 — Despre | 1440×900 | 362.34 | 29.50 | 57.20 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 1 — Despre | 1024×768 | 220.14 | 29.50 | 57.20 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 1 — Despre | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 2 — Galerie | 1440×900 | 451.55 | 29.50 | 61.91 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 2 — Galerie | 1024×768 | 293.34 | 29.50 | 61.91 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 2 — Galerie | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 3 — Discografie | 1440×900 | 545.45 | 29.50 | 100.70 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 3 — Discografie | 1024×768 | 371.25 | 29.50 | 100.70 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 3 — Discografie | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 4 — Oferte | 1440×900 | 678.16 | 29.50 | 57.20 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 4 — Oferte | 1024×768 | 487.95 | 29.50 | 57.20 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 4 — Oferte | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 5 — FAQ | 1440×900 | 767.36 | 29.50 | 29.11 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 5 — FAQ | 1024×768 | 561.16 | 29.50 | 29.11 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 5 — FAQ | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 6 — Blog | 1440×900 | 828.47 | 29.50 | 40.81 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 6 — Blog | 1024×768 | 606.27 | 29.50 | 40.81 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 6 — Blog | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| nav 7 — Contact | 1440×900 | 901.28 | 29.50 | 72.91 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 7 — Contact | 1024×768 | 663.08 | 29.50 | 72.91 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 14 | 20 | 0.70 | 600 | #c4c7c7 | transparent |
| nav 7 — Contact | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| div dreapta (grup butoane) | 1440×900 | 1012.39 | 20.50 | 243.61 | 38 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| div dreapta (grup butoane) | 1024×768 | 751.98 | 20.50 | 227.61 | 38 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| div dreapta (grup butoane) | 390×844 | 272 | 8.50 | 102 | 46 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| CTA WhatsApp (header) | 1440×900 | 1012.39 | 20.50 | 243.61 | 38 | 8 / 24 / 8 / 24 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #ffffff | #a01028 |
| CTA WhatsApp (header) | 1024×768 | 751.98 | 20.50 | 227.61 | 38 | 8 / 16 / 8 / 16 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #ffffff | #a01028 |
| CTA WhatsApp (header) | 390×844 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 1440×900 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 1024×768 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 390×844 | 272 | 9.50 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / -4 / 0 / 0 | 16 | 24 | normal | 400 | #c8c6c5 | transparent |
| buton hamburger | 1440×900 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| buton hamburger | 1024×768 | — | — | — | — | — | — | — | — | — | — | — | **nerandat** |
| buton hamburger | 390×844 | 328 | 8.50 | 46 | 46 | 8 / 8 / 8 / 8 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c8c6c5 | transparent |

### Hero (index.html)

| Element | Viewport | x | y | width | height | pad T/R/B/L | margin T/R/B/L | font-size | line-height | letter-spacing | font-weight | color | background |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `<section>` hero | 1440×900 | 0 | 0 | 1440 | 744 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<section>` hero | 1024×768 | 0 | 0 | 1024 | 757.19 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<section>` hero | 390×844 | 0 | 0 | 390 | 925.39 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container hero | 1440×900 | 120 | 0 | 1200 | 744 | 0 / 64 / 0 / 64 | 0 / 120 / 0 / 120 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container hero | 1024×768 | 0 | 0 | 1024 | 757.19 | 0 / 64 / 0 / 64 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container hero | 390×844 | 0 | 0 | 390 | 925.39 | 0 / 16 / 0 / 16 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| rândul pe 2 coloane | 1440×900 | 184 | 0 | 1072 | 744 | 128 / 0 / 96 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| rândul pe 2 coloane | 1024×768 | 64 | 0 | 896 | 757.19 | 128 / 0 / 96 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| rândul pe 2 coloane | 390×844 | 16 | 0 | 358 | 925.39 | 80 / 0 / 56 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de text | 1440×900 | 184 | 164.80 | 600.31 | 446.39 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de text | 1024×768 | 64 | 128 | 501.75 | 533.19 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de text | 390×844 | 16 | 80 | 358 | 457.39 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de imagine | 1440×900 | 848.31 | 128 | 407.69 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de imagine | 1024×768 | 629.75 | 134.59 | 330.25 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| coloana de imagine | 390×844 | 16 | 569.39 | 358 | 300 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| eyebrow | 1440×900 | 184 | 164.80 | 600.31 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 16 / 0 | 14 | 20 | 0.70 | 600 | #c8c6c5 | transparent |
| eyebrow | 1024×768 | 64 | 128 | 501.75 | 20 | 0 / 0 / 0 / 0 | 0 / 0 / 16 / 0 | 14 | 20 | 0.70 | 600 | #c8c6c5 | transparent |
| eyebrow | 390×844 | 16 | 80 | 358 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 16 / 0 | 12 | 24 | 3.60 | 400 | #c8c6c5 | transparent |
| `<h1>` | 1440×900 | 184 | 200.80 | 600.31 | 176.39 | 0 / 0 / 0 / 0 | 0 / 0 / 28 / 0 | 56 | 58.80 | -0.56 | 400 | #e5e2e1 | transparent |
| `<h1>` | 1024×768 | 64 | 164 | 501.75 | 235.19 | 0 / 0 / 0 / 0 | 0 / 0 / 28 / 0 | 56 | 58.80 | -0.56 | 400 | #e5e2e1 | transparent |
| `<h1>` | 390×844 | 16 | 120 | 358 | 113.39 | 0 / 0 / 0 / 0 | 0 / 0 / 24 / 0 | 36 | 37.80 | -0.36 | 400 | #e5e2e1 | transparent |
| `.motif-rule` | 1440×900 | 184 | 405.19 | 320 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 32 / 0 | 16 | 24 | normal | 400 | #c6c6c6 @ 0.28 | transparent |
| `.motif-rule` | 1024×768 | 64 | 427.19 | 320 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 32 / 0 | 16 | 24 | normal | 400 | #c6c6c6 @ 0.28 | transparent |
| `.motif-rule` | 390×844 | 16 | 257.39 | 320 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 28 / 0 | 16 | 24 | normal | 400 | #c6c6c6 @ 0.28 | transparent |
| paragraf hero | 1440×900 | 184 | 461.19 | 576 | 56 | 0 / 0 / 0 / 0 | 0 / 0 / 40 / 0 | 18 | 28 | normal | 400 | #c6c6c6 | transparent |
| paragraf hero | 1024×768 | 64 | 483.19 | 501.75 | 84 | 0 / 0 / 0 / 0 | 0 / 0 / 40 / 0 | 18 | 28 | normal | 400 | #c6c6c6 | transparent |
| paragraf hero | 390×844 | 16 | 309.39 | 358 | 72 | 0 / 0 / 0 / 0 | 0 / 0 / 32 / 0 | 16 | 24 | normal | 400 | #c6c6c6 | transparent |
| container butoane | 1440×900 | 184 | 557.19 | 600.31 | 54 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container butoane | 1024×768 | 64 | 607.19 | 501.75 | 54 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container butoane | 390×844 | 16 | 413.39 | 358 | 124 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| buton 1 — Rezervă pe WhatsApp | 1440×900 | 184 | 557.19 | 275.61 | 54 | 16 / 40 / 16 / 40 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #ffffff | #a01028 |
| buton 1 — Rezervă pe WhatsApp | 1024×768 | 64 | 607.19 | 259.61 | 54 | 16 / 32 / 16 / 32 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #ffffff | #a01028 |
| buton 1 — Rezervă pe WhatsApp | 390×844 | 16 | 413.39 | 358 | 54 | 16 / 32 / 16 / 32 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #ffffff | #a01028 |
| buton 2 — Vezi ofertele | 1440×900 | 483.61 | 557.19 | 204.20 | 54 | 16 / 40 / 16 / 40 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #e5e2e1 | transparent |
| buton 2 — Vezi ofertele | 1024×768 | 347.61 | 607.19 | 188.20 | 54 | 16 / 32 / 16 / 32 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #e5e2e1 | transparent |
| buton 2 — Vezi ofertele | 390×844 | 16 | 483.39 | 358 | 54 | 16 / 32 / 16 / 32 | 0 / 0 / 0 / 0 | 14 | 20 | 1.40 | 600 | #e5e2e1 | transparent |
| `<img>` hero | 1440×900 | 848.31 | 128 | 407.69 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` hero | 1024×768 | 629.75 | 134.59 | 330.25 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` hero | 390×844 | 16 | 569.39 | 358 | 300 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `.hero-photo-fade` | 1440×900 | 848.31 | 128 | 407.69 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `.hero-photo-fade` | 1024×768 | 629.75 | 134.59 | 330.25 | 520 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `.hero-photo-fade` | 390×844 | 16 | 569.39 | 358 | 300 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |

### Footer

| Element | Viewport | x | y | width | height | pad T/R/B/L | margin T/R/B/L | font-size | line-height | letter-spacing | font-weight | color | background |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `<footer>` | 1440×900 | 0 | 5512.06 | 1440 | 437 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #0e0e0e |
| `<footer>` | 1024×768 | 0 | 5513.09 | 1024 | 437 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #0e0e0e |
| `<footer>` | 390×844 | 0 | 6771.14 | 390 | 605 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | #0e0e0e |
| container interior footer | 1440×900 | 120 | 5513.06 | 1200 | 436 | 48 / 64 / 48 / 64 | 0 / 120 / 0 / 120 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container interior footer | 1024×768 | 0 | 5514.09 | 1024 | 436 | 48 / 64 / 48 / 64 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| container interior footer | 390×844 | 0 | 6772.14 | 390 | 604 | 32 / 16 / 32 / 16 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 1 (brand + social) | 1440×900 | 184 | 5561.06 | 1072 | 104 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 1 (brand + social) | 1024×768 | 64 | 5562.09 | 896 | 104 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 1 (brand + social) | 390×844 | 16 | 6804.14 | 358 | 188 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 2 (contact + legal) | 1440×900 | 184 | 5697.06 | 1072 | 148 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 2 (contact + legal) | 1024×768 | 64 | 5698.09 | 896 | 148 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 2 (contact + legal) | 390×844 | 16 | 7024.14 | 358 | 208 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 3 (juridic) | 1440×900 | 184 | 5877.06 | 1072 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 3 (juridic) | 1024×768 | 64 | 5878.09 | 896 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 3 (juridic) | 390×844 | 16 | 7264.14 | 358 | 80 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de brand | 1440×900 | 184 | 5561.06 | 448 | 104 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de brand | 1024×768 | 64 | 5562.09 | 448 | 104 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de brand | 390×844 | 16 | 6804.14 | 358 | 128 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (footer) | 1440×900 | 184 | 5561.06 | 116.78 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (footer) | 1024×768 | 64 | 5562.09 | 116.78 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link logo (footer) | 390×844 | 16 | 6804.14 | 93.42 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (footer) | 1440×900 | 184 | 5563.06 | 116.78 | 40 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (footer) | 1024×768 | 64 | 5564.09 | 116.78 | 40 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<img>` logo (footer) | 390×844 | 16 | 6810.14 | 93.42 | 32 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| paragraf descriere | 1440×900 | 184 | 5617.06 | 448 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.8) | transparent |
| paragraf descriere | 1024×768 | 64 | 5618.09 | 448 | 48 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.8) | transparent |
| paragraf descriere | 390×844 | 16 | 6860.14 | 358 | 72 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.8) | transparent |
| `<ul>` social | 1440×900 | 1068 | 5591.06 | 188 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<ul>` social | 1024×768 | 772 | 5592.09 | 188 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| `<ul>` social | 390×844 | 16 | 6948.14 | 358 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| social 1 — Facebook | 1440×900 | 1068 | 5591.06 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 1 — Facebook | 1024×768 | 772 | 5592.09 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 1 — Facebook | 390×844 | 16 | 6948.14 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 2 — Instagram | 1440×900 | 1116 | 5591.06 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 2 — Instagram | 1024×768 | 820 | 5592.09 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 2 — Instagram | 390×844 | 64 | 6948.14 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 3 — YouTube | 1440×900 | 1164 | 5591.06 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 3 — YouTube | 1024×768 | 868 | 5592.09 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 3 — YouTube | 390×844 | 112 | 6948.14 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 4 — TikTok | 1440×900 | 1212 | 5591.06 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 4 — TikTok | 1024×768 | 916 | 5592.09 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| social 4 — TikTok | 390×844 | 160 | 6948.14 | 44 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| banda 2a (contact + ANPC/SAL) | 1440×900 | 184 | 5697.06 | 1072 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 2a (contact + ANPC/SAL) | 1024×768 | 64 | 5698.09 | 896 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| banda 2a (contact + ANPC/SAL) | 390×844 | 16 | 7024.14 | 358 | 148 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de contact | 1440×900 | 184 | 5697.06 | 222 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de contact | 1024×768 | 64 | 5698.09 | 222 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona de contact | 390×844 | 16 | 7024.14 | 358 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link e-mail | 1440×900 | 184 | 5697.06 | 222 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link e-mail | 1024×768 | 64 | 5698.09 | 222 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link e-mail | 390×844 | 16 | 7024.14 | 358 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link telefon (footer) | 1440×900 | 184 | 5741.06 | 222 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link telefon (footer) | 1024×768 | 64 | 5742.09 | 222 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link telefon (footer) | 390×844 | 16 | 7068.14 | 358 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| zona ANPC/SAL | 1440×900 | 1160 | 5697.06 | 96 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona ANPC/SAL | 1024×768 | 864 | 5698.09 | 96 | 88 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| zona ANPC/SAL | 390×844 | 16 | 7128.14 | 358 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #e5e2e1 | transparent |
| link ANPC | 1440×900 | 1160 | 5719.06 | 45 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link ANPC | 1024×768 | 864 | 5720.09 | 45 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link ANPC | 390×844 | 16 | 7128.14 | 45 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| separator ANPC/SAL | 1440×900 | 1213 | 5729.06 | 5 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.5) | transparent |
| separator ANPC/SAL | 1024×768 | 917 | 5730.09 | 5 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.5) | transparent |
| separator ANPC/SAL | 390×844 | 69 | 7138.14 | 5 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 (opacity 0.5) | transparent |
| link SAL | 1440×900 | 1226 | 5719.06 | 30 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link SAL | 1024×768 | 930 | 5720.09 | 30 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| link SAL | 390×844 | 82 | 7128.14 | 30 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 16 | 24 | normal | 400 | #c4c7c7 | transparent |
| paragraf documente legale | 1440×900 | 184 | 5801.06 | 1072 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| paragraf documente legale | 1024×768 | 64 | 5802.09 | 896 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| paragraf documente legale | 390×844 | 16 | 7188.14 | 358 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| link Termeni și condiții | 1440×900 | 184 | 5801.06 | 112 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| link Termeni și condiții | 1024×768 | 64 | 5802.09 | 112 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| link Termeni și condiții | 390×844 | 16 | 7188.14 | 112 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| separator documente legale | 1440×900 | 304 | 5811.06 | 4 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 (opacity 0.5) | transparent |
| separator documente legale | 1024×768 | 184 | 5812.09 | 4 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 (opacity 0.5) | transparent |
| separator documente legale | 390×844 | 136 | 7198.14 | 4 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 (opacity 0.5) | transparent |
| link Politica de cookie-uri | 1440×900 | 316 | 5801.06 | 130 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| link Politica de cookie-uri | 1024×768 | 196 | 5802.09 | 130 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| link Politica de cookie-uri | 390×844 | 148 | 7188.14 | 130 | 44 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 13 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 1 — © | 1440×900 | 339.50 | 5877.06 | 270 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 1 — © | 1024×768 | 131.50 | 5878.09 | 270 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 1 — © | 390×844 | 16 | 7264.14 | 358 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 2 — dezvoltat de | 1440×900 | 628.50 | 5877.06 | 230 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 2 — dezvoltat de | 1024×768 | 420.50 | 5878.09 | 230 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 2 — dezvoltat de | 390×844 | 16 | 7292.14 | 358 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 3 — realizat de | 1440×900 | 877.50 | 5877.06 | 223 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 3 — realizat de | 1024×768 | 669.50 | 5878.09 | 223 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |
| juridic 3 — realizat de | 390×844 | 16 | 7320.14 | 358 | 24 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 12 | 24 | normal | 400 | #c6c6c6 | transparent |


## DISTANȚE VERTICALE REALE

`rect.top` al celui de-al doilea minus `rect.bottom` al primului. Unde perechea ajunge pe **același rând** la un viewport, distanța verticală nu se aplică și e dată în schimb cea orizontală.

| Grup | De la | Până la | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|---|---|
| Hero | eyebrow | `<h1>` | **16 px** | **16 px** | **16 px** |
| Hero | `<h1>` | `.motif-rule` | **28 px** | **28 px** | **24 px** |
| Hero | `.motif-rule` | paragraf hero | **32 px** | **32 px** | **28 px** |
| Hero | paragraf hero | container butoane | **40 px** | **40 px** | **32 px** |
| Hero | coloana de text | coloana de imagine | același rând → **64 px** pe orizontală | același rând → **64 px** pe orizontală | **32 px** |
| Footer benzi | banda 1 (brand + social) | banda 2 (contact + legal) | **32 px** | **32 px** | **32 px** |
| Footer benzi | banda 2 (contact + legal) | banda 3 (juridic) | **32 px** | **32 px** | **32 px** |
| Footer brand | link logo (footer) | paragraf descriere | **12 px** | **12 px** | **12 px** |
| Footer brand | zona de brand | `<ul>` social | același rând → **436 px** pe orizontală | același rând → **260 px** pe orizontală | **16 px** |
| Footer banda 2 | banda 2a (contact + ANPC/SAL) | paragraf documente legale | **16 px** | **16 px** | **16 px** |
| Footer contact | link e-mail | link telefon (footer) | **0 px** | **0 px** | **0 px** |
| Footer juridic | juridic 1 — © | juridic 2 — dezvoltat de | același rând → **19 px** pe orizontală | același rând → **19 px** pe orizontală | **4 px** |
| Footer juridic | juridic 2 — dezvoltat de | juridic 3 — realizat de | același rând → **19 px** pe orizontală | același rând → **19 px** pe orizontală | **4 px** |


## DISTANȚE ORIZONTALE REALE

`rect.left` al celui de-al doilea minus `rect.right` al primului.

| De la (margine dreapta) | Până la (margine stânga) | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|---|
| link logo (header) | nav 1 — Despre | **38.20 px** | **16 px** | n/a (nerandat) |
| nav 1 — Despre | nav 2 — Galerie | **32 px** | **16 px** | n/a (nerandat) |
| nav 2 — Galerie | nav 3 — Discografie | **32 px** | **16 px** | n/a (nerandat) |
| nav 3 — Discografie | nav 4 — Oferte | **32 px** | **16 px** | n/a (nerandat) |
| nav 4 — Oferte | nav 5 — FAQ | **32 px** | **16 px** | n/a (nerandat) |
| nav 5 — FAQ | nav 6 — Blog | **32 px** | **16 px** | n/a (nerandat) |
| nav 6 — Blog | nav 7 — Contact | **32 px** | **16 px** | n/a (nerandat) |
| nav 7 — Contact | CTA WhatsApp (header) | **38.20 px** | **16 px** | n/a (nerandat) |
| CTA WhatsApp (header) | link telefon (header) | n/a (nerandat) | n/a (nerandat) | n/a (nerandat) |
| link telefon (header) | buton hamburger | n/a (nerandat) | n/a (nerandat) | **12 px** |
| zona de brand | `<ul>` social | **436 px** | **260 px** | **-358 px** |
| social 1 — Facebook | social 2 — Instagram | **4 px** | **4 px** | **4 px** |
| social 2 — Instagram | social 3 — YouTube | **4 px** | **4 px** | **4 px** |
| social 3 — YouTube | social 4 — TikTok | **4 px** | **4 px** | **4 px** |
| zona de contact | zona ANPC/SAL | **754 px** | **578 px** | **-358 px** |
| link ANPC | separator ANPC/SAL | **8 px** | **8 px** | **8 px** |
| separator ANPC/SAL | link SAL | **8 px** | **8 px** | **8 px** |
| link Termeni și condiții | separator documente legale | **8 px** | **8 px** | **8 px** |
| separator documente legale | link Politica de cookie-uri | **8 px** | **8 px** | **8 px** |
| juridic 1 — © | juridic 2 — dezvoltat de | **19 px** | **19 px** | **-358 px** |
| juridic 2 — dezvoltat de | juridic 3 — realizat de | **19 px** | **19 px** | **-358 px** |
| coloana de text | coloana de imagine | **64 px** | **64 px** | **-358 px** |
| buton 1 — Rezervă pe WhatsApp | buton 2 — Vezi ofertele | **24 px** | **24 px** | **-358 px** |


## ALINIERE

| Reper | x @ 1440×900 | x @ 1024×768 | x @ 390×844 |
|---|---|---|---|
| link logo (header) | 184 | 64 | 16 |
| `<img>` logo (header) | 184 | 64 | 16 |
| `<h1>` | 184 | 64 | 16 |
| eyebrow | 184 | 64 | 16 |
| paragraf hero | 184 | 64 | 16 |
| link logo (footer) | 184 | 64 | 16 |
| `<img>` logo (footer) | 184 | 64 | 16 |
| paragraf descriere | 184 | 64 | 16 |
| link e-mail | 184 | 64 | 16 |
| juridic 1 — © | 339.50 | 131.50 | 16 |

| Reper (margine dreapta) | right @ 1440×900 | right @ 1024×768 | right @ 390×844 |
|---|---|---|---|
| CTA WhatsApp (header) | 1256 | 979.59 | nerandat |
| buton hamburger | nerandat | nerandat | 374 |
| container interior header | 1320 | 1024 | 390 |
| container interior footer | 1320 | 1024 | 390 |
| `<ul>` social | 1256 | 960 | 374 |
| social 4 — TikTok | 1256 | 960 | 204 |
| link SAL | 1256 | 960 | 112 |
| juridic 3 — realizat de | 1100.50 | 892.50 | 374 |
| coloana de imagine | 1256 | 960 | 374 |


## LĂȚIMEA CONTAINERELOR — ce o limitează

| Container | Viewport | width măsurat | max-width | padding L+R | lățime utilă conținut | margin L / R | Limitat de |
|---|---|---|---|---|---|---|---|
| container interior header | 1440×900 | 1200 | 1200px | 128 | **1072** | 120 / 120 | **max-width (1200px)** |
| container interior header | 1024×768 | 1024 | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| container interior header | 390×844 | 390 | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |
| container hero | 1440×900 | 1200 | 1200px | 128 | **1072** | 120 / 120 | **max-width (1200px)** |
| container hero | 1024×768 | 1024 | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| container hero | 390×844 | 390 | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |
| container interior footer | 1440×900 | 1200 | 1200px | 128 | **1072** | 120 / 120 | **max-width (1200px)** |
| container interior footer | 1024×768 | 1024 | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| container interior footer | 390×844 | 390 | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |


## VALORI SUPLIMENTARE MĂSURATE

| Element | Viewport | border T/R/B/L | culoare bordură sus / jos | max-width | min-height | gap | position | z-index | font-family | text-transform |
|---|---|---|---|---|---|---|---|---|---|---|
| `<header>` | 1440×900 | 0 / 0 / 1 / 0 | #444748 @ 0.2 / #444748 @ 0.2 | none | 0px | normal | fixed | 50 | Inter | none |
| `<header>` | 1024×768 | 0 / 0 / 1 / 0 | #444748 @ 0.2 / #444748 @ 0.2 | none | 0px | normal | fixed | 50 | Inter | none |
| `<header>` | 390×844 | 0 / 0 / 1 / 0 | #444748 @ 0.2 / #444748 @ 0.2 | none | 0px | normal | fixed | 50 | Inter | none |
| container interior header | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 32px | static | auto | Inter | none |
| container interior header | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 16px | static | auto | Inter | none |
| container interior header | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 16px | static | auto | Inter | none |
| link logo (header) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link logo (header) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link logo (header) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| `<nav>` desktop | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 32px | static | auto | Inter | none |
| `<nav>` desktop | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| `<nav>` desktop | 390×844 | — | — | — | — | — | — | — | — | **nerandat** |
| nav 1 — Despre | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | uppercase |
| nav 1 — Despre | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | uppercase |
| nav 1 — Despre | 390×844 | — | — | — | — | — | — | — | — | **nerandat** |
| div dreapta (grup butoane) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| div dreapta (grup butoane) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| div dreapta (grup butoane) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| CTA WhatsApp (header) | 1440×900 | 1 / 1 / 1 / 1 | #c41236 / #c41236 | none | auto | normal | static | auto | Inter | uppercase |
| CTA WhatsApp (header) | 1024×768 | 1 / 1 / 1 / 1 | #c41236 / #c41236 | none | auto | normal | static | auto | Inter | uppercase |
| CTA WhatsApp (header) | 390×844 | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 1440×900 | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 1024×768 | — | — | — | — | — | — | — | — | **nerandat** |
| link telefon (header) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| buton hamburger | 1440×900 | — | — | — | — | — | — | — | — | **nerandat** |
| buton hamburger | 1024×768 | — | — | — | — | — | — | — | — | **nerandat** |
| buton hamburger | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| `<section>` hero | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | relative | auto | Inter | none |
| `<section>` hero | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | relative | auto | Inter | none |
| `<section>` hero | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | relative | auto | Inter | none |
| container hero | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | normal | static | auto | Inter | none |
| container hero | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | normal | static | auto | Inter | none |
| container hero | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | normal | static | auto | Inter | none |
| rândul pe 2 coloane | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 64px | static | auto | Inter | none |
| rândul pe 2 coloane | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 64px | static | auto | Inter | none |
| rândul pe 2 coloane | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 32px | static | auto | Inter | none |
| coloana de text | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| coloana de text | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| coloana de text | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| coloana de imagine | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | relative | auto | Inter | none |
| coloana de imagine | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | relative | auto | Inter | none |
| coloana de imagine | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | relative | auto | Inter | none |
| eyebrow | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | uppercase |
| eyebrow | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | uppercase |
| eyebrow | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | uppercase |
| `.motif-rule` | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 320px | 0px | 16px | static | auto | Inter | none |
| `.motif-rule` | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 320px | 0px | 16px | static | auto | Inter | none |
| `.motif-rule` | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 320px | 0px | 16px | static | auto | Inter | none |
| container butoane | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 24px | static | auto | Inter | none |
| container butoane | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 24px | static | auto | Inter | none |
| container butoane | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | 16px | static | auto | Inter | none |
| buton 1 — Rezervă pe WhatsApp | 1440×900 | 1 / 1 / 1 / 1 | #c41236 / #c41236 | none | auto | normal | static | auto | Inter | uppercase |
| buton 1 — Rezervă pe WhatsApp | 1024×768 | 1 / 1 / 1 / 1 | #c41236 / #c41236 | none | auto | normal | static | auto | Inter | uppercase |
| buton 1 — Rezervă pe WhatsApp | 390×844 | 1 / 1 / 1 / 1 | #c41236 / #c41236 | none | auto | normal | static | auto | Inter | uppercase |
| buton 2 — Vezi ofertele | 1440×900 | 1 / 1 / 1 / 1 | #8e9192 / #8e9192 | none | auto | normal | static | auto | Inter | uppercase |
| buton 2 — Vezi ofertele | 1024×768 | 1 / 1 / 1 / 1 | #8e9192 / #8e9192 | none | auto | normal | static | auto | Inter | uppercase |
| buton 2 — Vezi ofertele | 390×844 | 1 / 1 / 1 / 1 | #8e9192 / #8e9192 | none | auto | normal | static | auto | Inter | uppercase |
| `<img>` hero | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 100% | 0px | normal | static | auto | Inter | none |
| `<img>` hero | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 100% | 0px | normal | static | auto | Inter | none |
| `<img>` hero | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 100% | 0px | normal | static | auto | Inter | none |
| `.hero-photo-fade` | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | absolute | auto | Inter | none |
| `.hero-photo-fade` | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | absolute | auto | Inter | none |
| `.hero-photo-fade` | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | absolute | auto | Inter | none |
| `<footer>` | 1440×900 | 1 / 0 / 0 / 0 | #444748 @ 0.1 / #444748 @ 0.1 | none | 0px | normal | static | auto | Inter | none |
| `<footer>` | 1024×768 | 1 / 0 / 0 / 0 | #444748 @ 0.1 / #444748 @ 0.1 | none | 0px | normal | static | auto | Inter | none |
| `<footer>` | 390×844 | 1 / 0 / 0 / 0 | #444748 @ 0.1 / #444748 @ 0.1 | none | 0px | normal | static | auto | Inter | none |
| container interior footer | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 32px | static | auto | Inter | none |
| container interior footer | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 32px | static | auto | Inter | none |
| container interior footer | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 1200px | 0px | 32px | static | auto | Inter | none |
| banda 1 (brand + social) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 24px | static | auto | Inter | none |
| banda 1 (brand + social) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 24px | static | auto | Inter | none |
| banda 1 (brand + social) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| banda 2 (contact + legal) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| banda 2 (contact + legal) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| banda 2 (contact + legal) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| banda 2a (contact + ANPC/SAL) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 32px | static | auto | Inter | none |
| banda 2a (contact + ANPC/SAL) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 32px | static | auto | Inter | none |
| banda 2a (contact + ANPC/SAL) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 16px | static | auto | Inter | none |
| banda 3 (juridic) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px 8px | static | auto | Inter | none |
| banda 3 (juridic) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px 8px | static | auto | Inter | none |
| banda 3 (juridic) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px 8px | static | auto | Inter | none |
| zona de brand | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 448px | auto | 12px | static | auto | Inter | none |
| zona de brand | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 448px | auto | 12px | static | auto | Inter | none |
| zona de brand | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | 448px | auto | 12px | static | auto | Inter | none |
| link logo (footer) | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link logo (footer) | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link logo (footer) | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| `<ul>` social | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px | static | auto | Inter | none |
| `<ul>` social | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px | static | auto | Inter | none |
| `<ul>` social | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 4px | static | auto | Inter | none |
| social 1 — Facebook | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | none |
| social 1 — Facebook | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | none |
| social 1 — Facebook | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 0px | normal | static | auto | Inter | none |
| zona de contact | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| zona de contact | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| zona de contact | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| link e-mail | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link e-mail | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link e-mail | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| zona ANPC/SAL | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 8px | static | auto | Inter | none |
| zona ANPC/SAL | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 8px | static | auto | Inter | none |
| zona ANPC/SAL | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | 8px | static | auto | Inter | none |
| link ANPC | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link ANPC | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link ANPC | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| paragraf documente legale | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal 8px | static | auto | Inter | none |
| paragraf documente legale | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal 8px | static | auto | Inter | none |
| paragraf documente legale | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal 8px | static | auto | Inter | none |
| link Termeni și condiții | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link Termeni și condiții | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| link Termeni și condiții | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | 44px | normal | static | auto | Inter | none |
| juridic 1 — © | 1440×900 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| juridic 1 — © | 1024×768 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |
| juridic 1 — © | 390×844 | 0 / 0 / 0 / 0 | #e5e7eb / #e5e7eb | none | auto | normal | static | auto | Inter | none |

---

# CONSTATĂRI DIN MĂSURARE

Numere care diferă de ce ar da citirea claselor. Fără interpretare.

## 1. Containerul interior e cu 1px mai scund decât header-ul

| Viewport | `<header>` height | container interior height | diferență |
|---|---|---|---|
| 1440×900 | **80** | **79** | 1px |
| 1024×768 | **80** | **79** | 1px |
| 390×844 | **64** | **63** | 1px |

`h-full` = 100% din **cutia de conținut** a header-ului. Header-ul are
`box-sizing: border-box` și 1px bordură jos, deci cutia lui de conținut e
79px (respectiv 63px), nu 80/64.

Aceeași relație la footer: `<footer>` 437px / container 436px la 1440 și
1024 (1px bordură sus); 605px / 604px la 390.

## 2. La 1024×768 conținutul header-ului depășește padding-ul dreapta

| Măsurătoare @ 1024×768 | Valoare |
|---|---|
| Zona de conținut a containerului | 64 … **960** (lățime 896) |
| link logo — width | 140.14 |
| `<nav>` — width | 515.84 |
| div dreapta — width | 227.61 |
| Suma celor 3 copii | 883.59 |
| Plus 2 × gap 16px | **915.59** |
| Spațiu disponibil | **896** |
| **Depășire** | **19.59 px** |
| `right` măsurat al CTA-ului | **979.59** (în loc de 960) |
| Distanța rămasă până la marginea viewportului | 44.41 px |

Nu produce bară de derulare orizontală (979.59 < 1024): conținutul intră în
padding-ul dreapta, nu în afara viewportului. Logo-ul și CTA-ul au
`shrink-0`, deci nu se comprimă.

Pentru comparație, la 1440×900 suma e 995.59 + 2×32 = 1059.59 în 1072
disponibili → **nu** depășește, iar `right` al CTA-ului e exact 1256, adică
fix marginea de conținut.

## 3. `<h1>` din hero se randează la font-weight 400, nu 500

| Viewport | font-size măsurat | line-height măsurat | letter-spacing măsurat | **font-weight măsurat** |
|---|---|---|---|---|
| 1440×900 | **56** | **58.80** | **−0.56** | **400** |
| 1024×768 | **56** | **58.80** | **−0.56** | **400** |
| 390×844 | **36** | **37.80** | **−0.36** | **400** |

Tokenul `display-lg` din `assets/tailwind.config.js` declară
`fontWeight: 500`, dar `<h1>` nu poartă clasa `text-display-lg` — poartă
`font-display-lg` (doar familia) plus mărimi arbitrare
`text-[36px] md:text-[48px] lg:text-[56px]`. Greutatea rămâne cea moștenită
de la `<body>`: **400**.

Line-height-ul măsurat vine din `leading-[1.05]` (56 × 1.05 = 58.80) și
letter-spacing-ul din `tracking-[-0.01em]` (56 × −0.01 = −0.56), nu din token.

## 4. Distanțele din nav nu sunt egale cu `gap`

La 1440×900, `gap-8` = 32px este respectat **între itemii de nav**, dar
distanțele de la logo la primul item și de la ultimul item la CTA sunt
**38.20px** — `justify-content: space-between` distribuie spațiul liber
rămas în cele două intervale dintre cei trei copii ai containerului.

| Interval | 1440×900 | 1024×768 |
|---|---|---|
| logo → nav 1 | **38.20** | **16** |
| nav 1..7, între itemi consecutivi | **32** (constant) | **16** (constant) |
| nav 7 → CTA | **38.20** | **16** |

La 1024×768 nu mai există spațiu liber de distribuit (vezi constatarea 2),
deci intervalele cad exact pe valoarea `gap`, 16px.

## 5. Distanțele verticale din hero coincid cu marginile din CSS

Măsurate, nu presupuse — nu a apărut colapsare de margini și nici surplus
din line-height:

| Pereche | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|
| eyebrow → `<h1>` | **16** | **16** | **16** |
| `<h1>` → `.motif-rule` | **28** | **28** | **24** |
| `.motif-rule` → paragraf | **32** | **32** | **28** |
| paragraf → container butoane | **40** | **40** | **32** |

## 6. Spațierea din zona de contact a footerului nu vine din margini

Distanța măsurată între linkul de e-mail și cel de telefon este **0 px** la
toate trei viewport-urile. Cutiile lor sunt lipite: fiecare are `height` 44px
(din `min-height: 44px`), iar textul e centrat vertical în ele. Nu există
margine între cele două.

## 7. Butoanele din hero au 54px înălțime, CTA-ul din header 38px

| Element | Viewport | height măsurat | Compunere |
|---|---|---|---|
| CTA WhatsApp (header) | 1440 / 1024 | **38** | 20 (line-height) + 8 + 8 (padding) + 1 + 1 (bordură) |
| buton 1 hero | toate trei | **54** | 20 + 16 + 16 + 1 + 1 |
| buton 2 hero | toate trei | **54** | 20 + 16 + 16 + 1 + 1 |
| buton hamburger | 390 | **46 × 46** | 30 (cutia SVG) + 8 + 8 |
| link telefon (header) | 390 | **44 × 44** | lățime/înălțime fixe |

Bordura de 1px de pe butoanele bordo vine din `.bg-accent` în
`assets/styles.css`, nu din clase.

## 8. Lățimile de text, măsurate după `fonts.ready`

Valori care nu se pot obține din clase:

| Element | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|
| CTA WhatsApp (header) — width | **243.61** | **227.61** | nerandat |
| buton 1 hero — width | **275.61** | **259.61** | **358** (întins) |
| buton 2 hero — width | **204.20** | **188.20** | **358** (întins) |
| `<h1>` — width × height | 600.31 × **176.39** | 501.75 × **235.19** | 358 × **113.39** |
| `<nav>` — width | **611.84** | **515.84** | nerandat |
| link e-mail — width | **222** | **222** | 358 (întins) |
| `<img>` hero — width × height | 407.69 × **520** | 330.25 × **520** | 358 × **300** |

Diferența de 16px la CTA și la butoanele hero între 1440 și 1024 vine din
`xl:px-6` vs `px-4` / `xl:px-10` vs `md:px-10` — pragul `xl` = 1280.

---

# ALINIERE — verificare explicită

## Marginea stângă

| Reper | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|
| `x` logo header | **184** | **64** | **16** |
| `x` `<h1>` hero | **184** | **64** | **16** |
| `x` logo footer | **184** | **64** | **16** |

**Coincid exact la toate trei viewport-urile. Diferență: 0.00 px.**

Se aliniază pe aceeași valoare și eyebrow-ul, paragraful din hero,
paragraful de descriere din footer și linkul de e-mail — toate la
184 / 64 / 16.

Singura excepție măsurată este banda 3 juridică, care e centrată
(`justify-content: center`), nu aliniată la stânga: `x` = 339.50 la 1440,
131.50 la 1024, 16 la 390 (la 390 devine coloană pe lățime plină).

## Marginea dreaptă

| Reper | 1440×900 | 1024×768 | 390×844 |
|---|---|---|---|
| `right` CTA header | **1256** | **979.59** | nerandat |
| `right` `<ul>` social (ultimul element din banda 1 a footerului) | **1256** | **960** | 374 |
| `right` social 4 — TikTok | **1256** | **960** | 204 |
| `right` link SAL | **1256** | **960** | 112 |
| `right` coloana de imagine (hero) | **1256** | **960** | 374 |

| Viewport | Verdict |
|---|---|
| 1440×900 | **Coincid exact — toate la 1256. Diferență: 0.00 px.** |
| 1024×768 | **NU coincid.** CTA-ul din header e la 979.59, restul la 960. **Diferență: 19.59 px** (CTA-ul e cu atât mai la dreapta). Cauza măsurată: constatarea 2. |
| 390×844 | CTA-ul e nerandat. Marginea dreaptă a hamburgerului e 374, egală cu marginea de conținut a containerului (390 − 16). |

## Lățimea reală a containerelor și ce o limitează

| Container | Viewport | width | max-width | padding L+R | lățime utilă | margin L / R | Limitat de |
|---|---|---|---|---|---|---|---|
| header | 1440×900 | **1200** | 1200px | 128 | **1072** | 120 / 120 | **max-width** |
| header | 1024×768 | **1024** | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| header | 390×844 | **390** | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |
| hero | 1440×900 | **1200** | 1200px | 128 | **1072** | 120 / 120 | **max-width** |
| hero | 1024×768 | **1024** | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| hero | 390×844 | **390** | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |
| footer | 1440×900 | **1200** | 1200px | 128 | **1072** | 120 / 120 | **max-width** |
| footer | 1024×768 | **1024** | 1200px | 128 | **896** | 0 / 0 | **lățimea viewportului** |
| footer | 390×844 | **390** | 1200px | 32 | **358** | 0 / 0 | **lățimea viewportului** |

`max-width` devine constrângerea activă doar peste 1200px lățime de
viewport. La 1024 și 390 lățimea e dictată de viewport, iar padding-ul
scade din ea.

---

# MAPARE ELEMENTOR

## Corecția de box-sizing, verificată pe valori măsurate

În prototip, `box-sizing: border-box`: containerul măsoară **1200px** cu tot
cu cei 128px de padding, iar conținutul are **1072px** (măsurat la 1440×900).

În Elementor, la un container „Boxed", valoarea din **Content Width**
(`boxed_width`) se aplică wrapper-ului interior, iar padding-ul se adaugă
**în afara** ei. Deci:

```
boxed_width_Elementor = latime_utila_masurata
padding_Elementor     = padding_masurat
```

Verificare pe cele trei viewport-uri măsurate, cu `boxed_width = 1072` și
`padding = 64`:

| Viewport | Lățime utilă **măsurată** în prototip | Elementor: `min(1072, viewport − 128)` | Coincid |
|---|---|---|---|
| 1440×900 | **1072** | min(1072, 1312) = **1072** | da |
| 1024×768 | **896** | min(1072, 896) = **896** | da |

Pentru 390×844, unde padding-ul măsurat e 16px de fiecare parte, cu
`boxed_width = 1168` și `padding = 16`:

| Viewport | Lățime utilă **măsurată** | Elementor: `min(1168, 390 − 32)` | Coincid |
|---|---|---|---|
| 390×844 | **358** | min(1168, 358) = **358** | da |

## Tabelul de mapare

Breakpoint-urile Elementor implicite: Mobile ≤ 767, Tablet 768–1024,
Desktop > 1024. Viewport-ul măsurat de 1024×768 cade în Tablet, 1440×900 în
Desktop, 390×844 în Mobile.

| Container | Breakpoint Elementor | `boxed_width` | `padding` T / R / B / L | Lățime utilă rezultată |
|---|---|---|---|---|
| **Header — container interior** | Mobile (≤767) | **1168px** | 0 / **16** / 0 / **16** | 358px @ 390 |
| | Tablet (768–1024) | **1072px** | 0 / **64** / 0 / **64** | 896px @ 1024 |
| | Desktop (>1024) | **1072px** | 0 / **64** / 0 / **64** | 1072px @ 1440 |
| **Hero — container** | Mobile (≤767) | **1168px** | 0 / **16** / 0 / **16** | 358px @ 390 |
| | Tablet (768–1024) | **1072px** | 0 / **64** / 0 / **64** | 896px @ 1024 |
| | Desktop (>1024) | **1072px** | 0 / **64** / 0 / **64** | 1072px @ 1440 |
| **Footer — container interior** | Mobile (≤767) | **1168px** | **32** / **16** / **32** / **16** | 358px @ 390 |
| | Tablet (768–1024) | **1072px** | **48** / **64** / **48** / **64** | 896px @ 1024 |
| | Desktop (>1024) | **1072px** | **48** / **64** / **48** / **64** | 1072px @ 1440 |

Padding-ul vertical al footerului este cel măsurat pe container: 32px sus și
jos la 390×844, 48px sus și jos la 1024×768 și 1440×900.

## Înălțimi fixe de setat

| Element | Mobile (390) | Tablet (1024) | Desktop (1440) |
|---|---|---|---|
| `<header>` — Min Height | **64** | **80** | **80** |
| Rândul interior al header-ului — Min Height | **63** | **79** | **79** |
| link logo header — Min Height | **44** | **48** | **48** |
| `<img>` logo header — Height | **32** | **48** | **48** |
| `<img>` logo footer — Height | **32** | **40** | **40** |
| link telefon header | **44 × 44** | nerandat | nerandat |
| buton hamburger | **46 × 46** | nerandat | nerandat |
| CTA WhatsApp header — Height | nerandat | **38** | **38** |
| butoane hero — Height | **54** | **54** | **54** |
| linkuri social footer | **44 × 44** | **44 × 44** | **44 × 44** |
| linkuri e-mail / telefon / ANPC / SAL / documente legale — Min Height | **44** | **44** | **44** |
| `<img>` hero — Height | **300** | **520** | **520** |

Cei 79px de la rândul interior al header-ului sunt cei 80px minus bordura de
1px — vezi constatarea 1. În Elementor, unde bordura containerului se
adaugă în afara înălțimii setate, cele două valori se setează separat:
înălțime 79 + bordură jos 1px = 80 ocupați.

## Gap-uri de setat (Space Between)

Valori măsurate ca distanță reală între cutii consecutive.

| Container | Mobile (390) | Tablet (1024) | Desktop (1440) |
|---|---|---|---|
| Rândul header (între cei 3 copii) | — | **16** | **32** nominal, **38.20** efectiv la capete |
| `<nav>` — între itemi | nerandat | **16** | **32** |
| Grup dreapta header (telefon → hamburger) | **12** | nerandat | nerandat |
| Hero — coloana text → coloana imagine | **32** (vertical) | **64** (orizontal) | **64** (orizontal) |
| Hero — buton 1 → buton 2 | **16** (vertical) | **24** (orizontal) | **24** (orizontal) |
| Footer — între cele 3 benzi | **32** | **32** | **32** |
| Footer — zona de brand (logo → paragraf) | **12** | **12** | **12** |
| Footer — brand → `<ul>` social | **16** (vertical) | **260** (orizontal, space-between) | **436** (orizontal, space-between) |
| Footer — între iconițele social | **4** | **4** | **4** |
| Footer — banda 2a → paragraf documente legale | **16** | **16** | **16** |
| Footer — contact → ANPC/SAL | **16** (vertical) | **578** (orizontal, space-between) | **754** (orizontal, space-between) |
| Footer — e-mail → telefon | **0** | **0** | **0** |
| Footer — ANPC → separator → SAL | **8** / **8** | **8** / **8** | **8** / **8** |
| Footer — Termeni → separator → Politica | **8** / **8** | **8** / **8** | **8** / **8** |
| Footer — între paragrafele juridice | **4** (vertical) | **19** (orizontal, cu separator între ele) | **19** (orizontal, cu separator între ele) |

Valorile marcate „space-between" nu sunt gap-uri de setat: sunt spațiul
liber distribuit de `justify-content: space-between`. Gap-ul declarat pe
acele containere este 24px (banda 1) și 32px (banda 2a); distanța măsurată
e mai mare pentru că elementele sunt împinse la extreme.

Cei 19px dintre paragrafele juridice sunt 8px gap + lățimea separatorului
`·` + 8px gap.

## Padding-uri verticale măsurate pe containere

Măsurate cu `getComputedStyle()`, nu citite din clase.

| Container | Mobile (390) | Tablet (1024) | Desktop (1440) |
|---|---|---|---|
| Rândul hero (padding T / R / B / L) | **80 / 0 / 56 / 0** | **128 / 0 / 96 / 0** | **128 / 0 / 96 / 0** |
| Container interior footer (padding T / R / B / L) | **32 / 16 / 32 / 16** | **48 / 64 / 48 / 64** | **48 / 64 / 48 / 64** |

Padding-ul vertical al hero-ului stă pe **rândul interior** (`div`-ul cu cele
două coloane), nu pe `<section>` și nu pe containerul cu `max-width` — ambele
au padding vertical 0. În Elementor, cele trei niveluri trebuie păstrate
separate, altfel padding-ul de 128/96 ajunge pe containerul boxed și
deplasează marginile laterale.
