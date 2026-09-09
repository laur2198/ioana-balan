# RANDARE MOBIL — geometria randată sub 1024px, în pixeli

Valorile sunt **MĂSURATE** cu `getBoundingClientRect()`, `getComputedStyle()`
și `getBBox()` într-un Chromium real, nu deduse din clasele Tailwind.
Drawer-ul a fost deschis efectiv și măsurat în ambele stări. Nu conține
recomandări.

---

## STARE GIT

| Element | Valoare |
|---|---|
| Branch curent | `main` |
| Upstream | `origin/main` (https://github.com/laur2198/ioana-balan) |
| Working tree la start | curat — `nothing to commit, working tree clean` |
| Commit-uri nepushate la start | **0** — `git log origin/main..HEAD` returnează listă goală |
| HEAD la start | `420edd3` — *docs: geometrie randata, masurata in Chromium la trei viewport-uri* |

Fișier nou scris de această rulare: `RANDARE-MOBIL.md`. Niciun fișier
existent nu a fost modificat.

---

## METODĂ

**Playwright a putut rula.** Toate valorile din tabele sunt MĂSURATE. Unde un
element nu a putut fi măsurat, celula spune de ce; nicio valoare nu este
înlocuită cu un calcul din clase.

| Aspect | Valoare |
|---|---|
| Server local | `python3 -m http.server 8131 --bind 127.0.0.1`, servind rădăcina repo-ului |
| URL măsurat | `http://127.0.0.1:8131/index.html` |
| Playwright | `playwright@1.63.0` |
| **Chromium** | **Chrome for Testing 153.0.8010.12** (build Playwright `chromium-1243`) |
| Mod | headless, `deviceScaleFactor: 1` |
| Așteptare la încărcare | `waitUntil: 'networkidle'` |
| **Așteptare pentru Tailwind** | `waitForFunction` până când `getComputedStyle(document.querySelector('header')).position === 'fixed'` — Tailwind Play CDN injectează `<style>` la runtime |
| **Așteptare fonturi** | `await document.fonts.ready`, apoi verificat `document.fonts.status` |
| **`document.fonts.status` la măsurare** | **`loaded`** la toate patru viewport-urile |
| Tampon suplimentar | 400ms după `fonts.ready` |
| **Viewport-uri** | **390×844**, **414×896**, **768×1024**, **1023×768** |
| **Drawer testat deschis** | **da, la toate patru** — `page.click('#menu-toggle')`, 600ms de așteptare (tranziția e 300ms), măsurare, apoi `Escape` și măsurare din nou |
| Treceri | patru: (1) cutii, drawer și secțiuni; (2) praguri de breakpoint și suprapuneri pe toată înălțimea paginii; (3) și (4) geometria iconului hamburger |

### Detecția elementelor ascunse

Se face prin **`el.getClientRects().length > 0`**, nu prin
`getComputedStyle(el).display`. Motivul, verificat și în `RANDARE.md`: itemii
de nav au ei înșiși `display: block`; doar părintele `<nav>` este
`display: none`. Testat pe `display`, cei 7 itemi ar raporta cutii de 0×0 la
coordonata 0,0 — valori false, care arată ca măsurători.

În acest document criteriul contează și într-un al doilea fel: **drawer-ul
închis trece testul `getClientRects()`** — are un dreptunghi de randare, doar
că translatat integral în afara ecranului. Ce îl scoate din tab order este
`inert`, nu ascunderea. Cele două verificări nu sunt interschimbabile.

### Convenții

- Valorile sunt în px, cu două zecimale acolo unde nu sunt întregi.
- `y` este absolut în document (`rect.top + window.scrollY`).
- Culorile sunt convertite în hex; unde alfa < 1, e notat `#hex @ alfa`.
- `x`/`width`/`height` sunt de pe cutia de bord (border-box).

---

## CONSTATAREA PRINCIPALĂ

Contextul întrebării spune că, în reconstrucția WordPress, header-ul se rupe
pe două rânduri și butonul hamburger nu se randează. **În prototipul din acest
repo, măsurat, niciuna dintre cele două situații nu apare la niciunul dintre
cele patru viewport-uri:**

| Verificare | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| Butonul hamburger — prezent în DOM | da | da | da | da |
| Butonul hamburger — `getClientRects().length > 0` | **da** | **da** | **da** | **da** |
| Butonul hamburger — dimensiune randată | **46 × 46** | **46 × 46** | **46 × 46** | **46 × 46** |
| Header — înălțimea containerului interior | **63** | **63** | **79** | **79** |
| Header — necesar vs disponibil | 211.42 / 358 | 211.42 / 382 | 258.14 / 640 | 258.14 / 895 |
| Header — **spațiu liber rămas** | **146.58** | **170.58** | **381.86** | **636.86** |
| Header — depășire | **nu** | **nu** | **nu** | **nu** |

Header-ul stă pe un singur rând cu spațiu liber de rezervă la toate patru, iar
înălțimea containerului (63, respectiv 79 px) corespunde unui singur rând: la
două rânduri ar fi fost cel puțin dublă. Diferența față de implementarea
WordPress nu vine, așadar, din geometria prototipului. Valorile de mai jos
sunt cele pe care trebuie să le producă reconstrucția.

# BLOC A — HEADER SUB 1024px

## A1. `<header>` și containerul interior

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| `<header>` height | 64 | 64 | 80 | 80 |
| `<header>` position / z-index | fixed / 50 | fixed / 50 | fixed / 50 | fixed / 50 |
| `<header>` background | #131313 @ 0.95 | #131313 @ 0.95 | #131313 @ 0.95 | #131313 @ 0.95 |
| `<header>` bordură T/R/B/L | 0 / 0 / 1 / 0 | 0 / 0 / 1 / 0 | 0 / 0 / 1 / 0 | 0 / 0 / 1 / 0 |
| container height | 63 | 63 | 79 | 79 |
| container padding T/R/B/L | 0 / 16 / 0 / 16 | 0 / 16 / 0 / 16 | 0 / 64 / 0 / 64 | 0 / 64 / 0 / 64 |
| container width | 390 | 414 | 768 | 1023 |
| container lățime utilă | 358 | 382 | 640 | 895 |
| container gap | 16px | 16px | 16px | 16px |
| container flex-direction | row | row | row | row |

### Ce are `getClientRects().length > 0`

| Element | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| link logo | **vizibil** | **vizibil** | **vizibil** | **vizibil** |
| nav desktop | ascuns | ascuns | ascuns | ascuns |
| div dreapta (grup butoane) | **vizibil** | **vizibil** | **vizibil** | **vizibil** |
| CTA WhatsApp | ascuns | ascuns | ascuns | ascuns |
| link telefon | **vizibil** | **vizibil** | **vizibil** | **vizibil** |
| buton hamburger | **vizibil** | **vizibil** | **vizibil** | **vizibil** |

Niciun element nu lipsește din DOM la niciun viewport: `link telefon` și `buton hamburger` sunt prezente și randate la toate patru; `nav desktop` și `CTA WhatsApp` sunt în DOM dar au 0 dreptunghiuri de randare (`display:none` prin `lg:`).

## A2. Logo

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| `<img>` height | 32 | 32 | 48 | 48 |
| `<img>` width | 93.42 | 93.42 | 140.14 | 140.14 |
| `<img>` x | 16 | 16 | 64 | 64 |
| `<img>` y | 15.50 | 15.50 | 15.50 | 15.50 |
| link părinte height | 44 | 44 | 48 | 48 |
| link părinte width | 93.42 | 93.42 | 140.14 | 140.14 |
| link părinte x | 16 | 16 | 64 | 64 |
| link părinte y | 9.50 | 9.50 | 15.50 | 15.50 |
| link părinte min-height | 44px | 44px | 44px | 44px |

## A3. Butonul de telefon

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| prezent în DOM | **da** | **da** | **da** | **da** |
| randat (`getClientRects().length`) | **da** | **da** | **da** | **da** |
| width × height | **44 × 44** | **44 × 44** | **44 × 44** | **44 × 44** |
| x | 272 | 296 | 602 | 857 |
| y | 9.50 | 9.50 | 17.50 | 17.50 |
| padding T/R/B/L | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| margin T/R/B/L | 0 / -4 / 0 / 0 | 0 / -4 / 0 / 0 | 0 / -4 / 0 / 0 | 0 / -4 / 0 / 0 |
| culoare | #c8c6c5 | #c8c6c5 | #c8c6c5 | #c8c6c5 |
| background | #000000 @ 0 | #000000 @ 0 | #000000 @ 0 | #000000 @ 0 |

**SVG** (identic la toate patru viewport-urile): randat **24 × 24 px**, `viewBox="0 -960 960 960"`, atribute `width`/`height` = `24`/`24`, `fill: currentColor` → rezolvat la `rgb(200, 198, 197)`.

Atribute măsurate pe element:

| Atribut | Valoare |
|---|---|
| `aria-label` | `Sună acum` |
| `class` | `lg:hidden flex items-center justify-center w-11 h-11 -mr-1 text-primary hover:text-white transition-colors` |
| `href` | `tel:+40722911485` |

`path` complet:

```
M775.38-140Q669-140 556-193.69q-113-53.7-210.81-151.7-97.8-98-151.5-210.8Q140-669 140-775.38q0-19.12 12.64-31.87T184.23-820h114.13q15.64 0 26.41 10.19 10.77 10.2 15.15 26.35l23.85 107.18q2.08 15.13-1 27.2-3.08 12.08-11.69 20.31l-94.39 91.92q26.77 45.93 56.54 85.08t64.39 73.54q37.38 38.38 79.53 70.08 42.16 31.69 90.24 57.61l90.76-93.38q10-11 22.39-14.81 12.39-3.81 25.84-1.81l97.08 21.39q16.15 3.61 26.35 16.26Q820-310.24 820-294.23v110q0 18.95-12.75 31.59T775.38-140ZM234-578l82.54-80.08q1.54-1.53 2.11-4.23.58-2.69.2-5L297-768.46q-.38-3.08-2.5-4.62-2.11-1.53-5.19-1.53h-98.54q-2.31 0-3.85 1.53-1.53 1.54-1.53 3.85.84 41.62 12.92 88.69Q210.39-633.46 234-578Zm356.31 349.15q41 20.16 89.77 31.39 48.77 11.23 89.15 12.46 2.31 0 3.85-1.54 1.53-1.54 1.53-3.85v-98.15q0-3.08-1.53-5.19-1.54-2.12-4.62-2.5l-90.69-18.69q-2.31-.39-4.04.19-1.73.58-3.65 2.11l-79.77 83.77ZM234-578Zm356.31 349.15Z
```

## A4. Butonul hamburger

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| prezent în DOM | **da** | **da** | **da** | **da** |
| randat (`getClientRects().length`) | **da** | **da** | **da** | **da** |
| width × height | **46 × 46** | **46 × 46** | **46 × 46** | **46 × 46** |
| x | 328 | 352 | 658 | 913 |
| y | 8.50 | 8.50 | 16.50 | 16.50 |
| padding T/R/B/L | 8 / 8 / 8 / 8 | 8 / 8 / 8 / 8 | 8 / 8 / 8 / 8 | 8 / 8 / 8 / 8 |
| margin T/R/B/L | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| culoare | #c8c6c5 | #c8c6c5 | #c8c6c5 | #c8c6c5 |
| background | #000000 @ 0 | #000000 @ 0 | #000000 @ 0 | #000000 @ 0 |

**SVG** (identic la toate patru viewport-urile): randat **30 × 30 px**, `viewBox="0 -960 960 960"`, atribute `width`/`height` = `1em`/`1em`, clasă `text-3xl` → `font-size` măsurat **30px**, `fill: currentColor` → rezolvat la `rgb(200, 198, 197)`.

Atribute măsurate pe element:

| Atribut | Valoare |
|---|---|
| `aria-label` | `Deschide Meniu` |
| `aria-expanded` | `false` |
| `aria-controls` | `mobile-menu` |
| `class` | `lg:hidden text-primary p-2` |
| `id` | `menu-toggle` |

`path` complet:

```
M140-254.62V-300h680v45.38H140Zm0-202.69v-45.38h680v45.38H140ZM140-660v-45.38h680V-660H140Z
```

### A4b. Geometria randată a iconului hamburger

Bbox-ul căii este măsurat; cele trei bare sunt măsurate individual, reinjectând fiecare bară ca `<path>` temporar în același `<svg>` și citindu-i `getBoundingClientRect()`. Suma barelor plus spațiile reconstituie exact bbox-ul măsurat (**14.09** vs **14.09** px), deci descompunerea e verificată, nu presupusă.

| Măsurătoare | Valoare |
|---|---|
| Buton (cutie de tap) | **46 × 46 px** |
| `<svg>` | **30 × 30 px** |
| Desenul efectiv (bbox-ul căii) | **21.25 × 14.09 px** |
| Inset al desenului în `<svg>` — sus / stânga | 7.96 / 4.38 px |
| **Grosimea unei bare** | **1.42 px** |
| **Lățimea unei bare** | **21.25 px** |
| **Spațiu între bara de sus și cea din mijloc** | **4.92 px** |
| **Spațiu între bara din mijloc și cea de jos** | **4.92 px** |
| Scara viewBox → px | 21.25 / 680 = **0.03125** |

Cele trei bare nu sunt trasate cu `stroke`, ci sunt dreptunghiuri umplute: grosimea de 1.42px este înălțimea formei, nu o lățime de linie. La reproducere cu `border` sau `stroke` în Elementor, valoarea de setat este 1.42px, cu 4.92px între bare.


## A5. Ordinea vizuală a copiilor, de la stânga la dreapta (după `x`)

| Viewport | Ordine | `x` pentru fiecare |
|---|---|---|
| 390×844 | **link logo** → **link telefon** → **buton hamburger** | 16 · 272 · 328 |
| 414×896 | **link logo** → **link telefon** → **buton hamburger** | 16 · 296 · 352 |
| 768×1024 | **link logo** → **link telefon** → **buton hamburger** | 64 · 602 · 658 |
| 1023×768 | **link logo** → **link telefon** → **buton hamburger** | 64 · 857 · 913 |

Ordinea e identică la toate patru: **logo → link telefon → buton hamburger**. Nav-ul desktop și CTA-ul WhatsApp nu apar sub 1024px.

## A6. Distanțe orizontale reale între elementele consecutive

`rect.left` al următorului minus `rect.right` al precedentului.

| De la | Până la | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|---|
| link logo | link telefon | **162.58 px** | **186.58 px** | **397.86 px** | **652.86 px** |
| link telefon | buton hamburger | **12 px** | **12 px** | **12 px** | **12 px** |

Distanța logo → telefon nu este un `gap`: containerul are `justify-content: space-between`, deci e spațiul liber rămas. Distanța telefon → hamburger, **12 px**, este constantă la toate patru viewport-urile și vine din `gap: 16px` pe grupul din dreapta minus `margin-right: -4px` de pe linkul de telefon.

## A7. Încape header-ul?

| Măsurătoare | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| Lățime utilă a containerului | 358 | 382 | 640 | 895 |
| Suma lățimilor copiilor randați | 195.42 | 195.42 | 242.14 | 242.14 |
| Număr de copii randați | 2 | 2 | 2 | 2 |
| Necesar (sumă + gap-uri) | 211.42 | 211.42 | 258.14 | 258.14 |
| **Spațiu liber rămas** | **146.58 px** | **170.58 px** | **381.86 px** | **636.86 px** |
| **Depășire** | **nu** | **nu** | **nu** | **nu** |

**Header-ul încape la toate patru viewport-urile.** Cel mai strâns caz este 390×844, unde rămân **146.58 px** liberi din 358 disponibili. Containerul are `flex-direction: row` și `flex-wrap: nowrap` la toate patru, iar înălțimea lui măsurată (63 px la 390 și 414, 79 px la 768 și 1023) corespunde unui singur rând: la două rânduri ar fi fost cel puțin dublă. În prototip header-ul nu se rupe pe două rânduri la niciunul dintre cele patru viewport-uri măsurate.


### A7b. Pragul exact la care se schimbă header-ul

Măsurat separat, pe patru lățimi în jurul pragului `lg`:

| Lățime viewport | `<header>` height | nav desktop | CTA WhatsApp | link telefon | buton hamburger |
|---|---|---|---|---|---|
| 1022 | 80 | ascuns | ascuns | **vizibil** | **vizibil** |
| 1023 | 80 | ascuns | ascuns | **vizibil** | **vizibil** |
| 1024 | 80 | **vizibil** | **vizibil** | ascuns | ascuns |
| 1025 | 80 | **vizibil** | **vizibil** | ascuns | ascuns |

Comutarea are loc **exact la 1024px**: la 1023 se vede varianta mobilă (telefon + hamburger), la 1024 cea desktop (nav + CTA). Înălțimea header-ului nu se schimbă aici — trecerea 64 → 80px are loc la 768px.

# BLOC B — DRAWER-UL, ÎN AMBELE STĂRI

Drawer-ul a fost deschis efectiv prin `page.click('#menu-toggle')` la fiecare dintre cele patru viewport-uri, cu 600ms de așteptare după click (tranziția e de 300ms), și măsurat în starea deschisă. Apoi s-a apăsat `Escape` și s-a măsurat din nou.

## B1. Starea ÎNCHISĂ

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| position | fixed | fixed | fixed | fixed |
| z-index | 60 | 60 | 60 | 60 |
| width × height | 390 × 844 | 414 × 896 | 768 × 1024 | 1023 × 768 |
| x (stânga cutiei) | 390 | 414 | 768 | 1023 |
| **transform** | `matrix(1, 0, 0, 1, 390, 0)` | `matrix(1, 0, 0, 1, 414, 0)` | `matrix(1, 0, 0, 1, 768, 0)` | `matrix(1, 0, 0, 1, 1023, 0)` |
| transform, citit | translateX(**390px**) = 100% din lățime | translateX(**414px**) = 100% din lățime | translateX(**768px**) = 100% din lățime | translateX(**1023px**) = 100% din lățime |
| background | #131313 | #131313 | #131313 | #131313 |
| **`getClientRects().length > 0`** | **da** | **da** | **da** | **da** |
| **`inert` (proprietate)** | **True** | **True** | **True** | **True** |
| `inert` (atribut în HTML) | True | True | True | True |
| ocupă spațiu în layout | **nu** (`position: fixed`) | **nu** (`position: fixed`) | **nu** (`position: fixed`) | **nu** (`position: fixed`) |
| `aria-expanded` pe `#menu-toggle` | `false` | `false` | `false` | `false` |
| `aria-controls` pe `#menu-toggle` | `mobile-menu` | `mobile-menu` | `mobile-menu` | `mobile-menu` |
| `overflow` pe `<body>` | `hidden auto` | `hidden auto` | `hidden auto` | `hidden auto` |

În starea închisă drawer-ul **rămâne randat**: are un dreptunghi de randare, doar că translatat integral în afara ecranului, la `x` egal cu lățimea viewportului. Nu produce derulare orizontală pentru că `<body>` are `overflow-x: hidden`. Verificarea prin `getClientRects()` nu îl raportează ca ascuns — ceea ce îl scoate din tab order și din arborele de accesibilitate este exclusiv `inert`.

## B2. Starea DESCHISĂ

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| **transform** | `none` | `none` | `none` | `none` |
| x | 0 | 0 | 0 | 0 |
| width × height | **390 × 844** | **414 × 896** | **768 × 1024** | **1023 × 768** |
| z-index | 60 | 60 | 60 | 60 |
| **`overflow` pe `<body>`** | **`hidden`** | **`hidden`** | **`hidden`** | **`hidden`** |
| clasă adăugată pe `<body>` | `overflow-hidden` | `overflow-hidden` | `overflow-hidden` | `overflow-hidden` |
| `inert` | **False** | **False** | **False** | **False** |
| `aria-expanded` pe `#menu-toggle` | `true` | `true` | `true` | `true` |
| wrapper interior — padding | 32 / 32 / 32 / 32 | 32 / 32 / 32 / 32 | 32 / 32 / 32 / 32 | 32 / 32 / 32 / 32 |
| wrapper interior — width | 390 | 414 | 768 | 1023 |
| lățime utilă a conținutului | 326 | 350 | 704 | 959 |

Deschis, drawer-ul acoperă întreg viewportul la toate patru dimensiunile. `transform` devine `none` — clasa `translate-x-full` este eliminată, nu înlocuită cu `translate-x-0`. Pe `<body>` se adaugă clasa `overflow-hidden`, iar `overflow` calculat trece de la `hidden auto` la `hidden`, adică derularea paginii din spate se blochează.

## B3. Tranziția

| Proprietate | Valoare măsurată (identică la toate patru) |
|---|---|
| `transition-property` | **`transform`** |
| `transition-duration` | **`0.3s`** |
| `transition-timing-function` | **`cubic-bezier(0.4, 0, 0.2, 1)`** |
| Valoarea animată, închis | `transform: translateX(390px)` la 390×844 |
| Valoarea animată, deschis | `transform: none` |

Se animă o singură proprietate, `transform`. Nu se animă `opacity`, `left` sau `visibility`.

## B4. Antetul drawer-ului

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| rând antet — height | 36 | 36 | 36 | 36 |
| rând antet — margin T/R/B/L | 0 / 0 / 48 / 0 | 0 / 0 / 48 / 0 | 0 / 0 / 48 / 0 | 0 / 0 / 48 / 0 |
| logo — height | **32** | **32** | **32** | **32** |
| logo — width | 93.42 | 93.42 | 93.42 | 93.42 |
| logo — x / y | 32 / 34 | 32 / 34 | 32 / 34 | 32 / 34 |
| buton X — x / y | 322 / 32 | 346 / 32 | 700 / 32 | 955 / 32 |
| **buton X — width × height** | **36 × 36** | **36 × 36** | **36 × 36** | **36 × 36** |
| buton X — padding | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| buton X — culoare | #c8c6c5 | #c8c6c5 | #c8c6c5 | #c8c6c5 |
| SVG-ul din butonul X | 36 × 36 | 36 × 36 | 36 × 36 | 36 × 36 |
| **antet → primul item de nav** | **48 px** | **48 px** | **48 px** | **48 px** |

SVG-ul butonului de închidere: `viewBox="0 -960 960 960"`, clasă `text-4xl` → `font-size` măsurat **36px**, randat **36 × 36 px**. Butonul nu are padding, deci cutia lui de tap este egală cu SVG-ul: **36 × 36 px**.

Atribute măsurate pe buton:

| Atribut | Valoare |
|---|---|
| `aria-label` | `Închide Meniu` |
| `class` | `text-primary` |
| `id` | `menu-close` |

`path` complet:

```
m250.92-218.92-32-32L448-480 218.92-709.08l32-32L480-512l229.08-229.08 32 32L512-480l229.08 229.08-32 32L480-448 250.92-218.92Z
```

Distanța de la baza antetului până la primul item de nav este **48 px** la toate patru viewport-urile: cei 48px de `margin-bottom` de pe rândul de antet.

## B5. Itemii de nav din drawer, individual


### 390×844

| # | Text | x | y | width | height | font-size | line-height | letter-spacing | font-weight | culoare | text-transform | → următorul |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Acasă | 32 | 116 | 326 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | uppercase | **24 px** |
| 2 | Despre | 32 | 172 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 3 | Galerie | 32 | 228 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 4 | Discografie | 32 | 284 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 5 | Oferte | 32 | 340 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 6 | Întrebări frecvente | 32 | 396 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 7 | Blog | 32 | 452 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 8 | Contact | 32 | 508 | 326 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **40 px** |
| 9 | Rezervă pe WhatsApp | 32 | 580 | 326 | 66 | 24 | 32 | normal | 500 | #ffffff | uppercase | — |

### 414×896

| # | Text | x | y | width | height | font-size | line-height | letter-spacing | font-weight | culoare | text-transform | → următorul |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Acasă | 32 | 116 | 350 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | uppercase | **24 px** |
| 2 | Despre | 32 | 172 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 3 | Galerie | 32 | 228 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 4 | Discografie | 32 | 284 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 5 | Oferte | 32 | 340 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 6 | Întrebări frecvente | 32 | 396 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 7 | Blog | 32 | 452 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 8 | Contact | 32 | 508 | 350 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **40 px** |
| 9 | Rezervă pe WhatsApp | 32 | 580 | 350 | 66 | 24 | 32 | normal | 500 | #ffffff | uppercase | — |

### 768×1024

| # | Text | x | y | width | height | font-size | line-height | letter-spacing | font-weight | culoare | text-transform | → următorul |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Acasă | 32 | 116 | 704 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | uppercase | **24 px** |
| 2 | Despre | 32 | 172 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 3 | Galerie | 32 | 228 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 4 | Discografie | 32 | 284 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 5 | Oferte | 32 | 340 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 6 | Întrebări frecvente | 32 | 396 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 7 | Blog | 32 | 452 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 8 | Contact | 32 | 508 | 704 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **40 px** |
| 9 | Rezervă pe WhatsApp | 32 | 580 | 704 | 66 | 24 | 32 | normal | 500 | #ffffff | uppercase | — |

### 1023×768

| # | Text | x | y | width | height | font-size | line-height | letter-spacing | font-weight | culoare | text-transform | → următorul |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Acasă | 32 | 116 | 959 | 32 | 24 | 32 | normal | 500 | #c8c6c5 | uppercase | **24 px** |
| 2 | Despre | 32 | 172 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 3 | Galerie | 32 | 228 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 4 | Discografie | 32 | 284 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 5 | Oferte | 32 | 340 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 6 | Întrebări frecvente | 32 | 396 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 7 | Blog | 32 | 452 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **24 px** |
| 8 | Contact | 32 | 508 | 959 | 32 | 24 | 32 | normal | 500 | #c4c7c7 | uppercase | **40 px** |
| 9 | Rezervă pe WhatsApp | 32 | 580 | 959 | 66 | 24 | 32 | normal | 500 | #ffffff | uppercase | — |

**Primul item are altă culoare decât restul.** Măsurat: itemul 1, „Acasă”, este **#c8c6c5** (tokenul `primary`), iar itemii 2–8 sunt **#c4c7c7** (tokenul `on-surface-variant`). Diferența e de 4 puncte pe canalul R și 2 pe B. Culoarea nu depinde de pagina curentă: „Acasă” rămâne #c8c6c5 și pe `index.html`, unde ar fi pagina activă.

Toți cei 8 itemi de meniu au aceeași metrică: **24px / 32px**, greutate **500**, `letter-spacing: normal`, `text-transform: uppercase`, familia **EB Garamond**, înălțime de cutie **32px**, fără padding. Distanța dintre ei este constant **24 px** (gap-ul flex), cu excepția ultimului interval, înainte de CTA.

## B6. CTA-ul din josul drawer-ului

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| text | Rezervă pe WhatsApp | Rezervă pe WhatsApp | Rezervă pe WhatsApp | Rezervă pe WhatsApp |
| x / y | 32 / 580 | 32 / 580 | 32 / 580 | 32 / 580 |
| **width × height** | **326 × 66** | **350 × 66** | **704 × 66** | **959 × 66** |
| padding T/R/B/L | 16 / 0 / 16 / 0 | 16 / 0 / 16 / 0 | 16 / 0 / 16 / 0 | 16 / 0 / 16 / 0 |
| margin T/R/B/L | 16 / 0 / 0 / 0 | 16 / 0 / 0 / 0 | 16 / 0 / 0 / 0 | 16 / 0 / 0 / 0 |
| **background** | **#a01028** | **#a01028** | **#a01028** | **#a01028** |
| culoare text | #ffffff | #ffffff | #ffffff | #ffffff |
| **bordură T/R/B/L** | **1 / 1 / 1 / 1** | **1 / 1 / 1 / 1** | **1 / 1 / 1 / 1** | **1 / 1 / 1 / 1** |
| culoare bordură | #c41236 | #c41236 | #c41236 | #c41236 |
| border-radius | 0px | 0px | 0px | 0px |
| font-size / line-height | 24 / 32 | 24 / 32 | 24 / 32 | 24 / 32 |
| font-weight / familie | 500 / EB Garamond | 500 / EB Garamond | 500 / EB Garamond | 500 / EB Garamond |
| text-align | center | center | center | center |
| **distanța față de ultimul item de meniu** | **40 px** | **40 px** | **40 px** | **40 px** |

Înălțimea de 66px se compune din 32 (line-height) + 16 + 16 (padding) + 1 + 1 (bordură). Bordura de 1px **#c41236** nu apare în clase: vine din regula `.bg-accent { border: 1px solid var(--accent-edge) }` din `assets/styles.css`. Distanța de 40px față de ultimul item de meniu este gap-ul de 24px plus `margin-top: 16px`.

## B7. Comportamentul la tastatură

| Verificare | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| `transform` după Escape | `matrix(1, 0, 0, 1, 390, 0)` | `matrix(1, 0, 0, 1, 414, 0)` | `matrix(1, 0, 0, 1, 768, 0)` | `matrix(1, 0, 0, 1, 1023, 0)` |
| `inert` după Escape | **True** | **True** | **True** | **True** |
| `aria-expanded` după Escape | `false` | `false` | `false` | `false` |
| `overflow` pe `<body>` după Escape | `hidden auto` | `hidden auto` | `hidden auto` | `hidden auto` |
| **unde ajunge focusul** | **`#menu-toggle`** | **`#menu-toggle`** | **`#menu-toggle`** | **`#menu-toggle`** |
| drawer `inert` cât e închis | **True** | **True** | **True** | **True** |
| primul link — dreptunghiuri de randare | 1 | 1 | 1 | 1 |

Escape închide drawer-ul, îl readuce la `translateX(100%)`, îi pune `inert` înapoi, comută `aria-expanded` pe `false`, deblochează derularea pe `<body>` și mută focusul înapoi pe **`#menu-toggle`**, butonul care l-a deschis.

Cât drawer-ul e închis, primul link („Acasă”) **are** un dreptunghi de randare, deci nu este ascuns prin `display:none`. **Nu este însă în tab order**, pentru că `inert` este `true` pe containerul lui: `inert` scoate subarborele atât din ordinea de tabulare, cât și din arborele de accesibilitate. Aceasta este singura barieră — o implementare care copiază doar `transform: translateX(100%)` fără `inert` lasă cele 9 linkuri tabulabile în afara ecranului.

# BLOC C — HERO ȘI SECȚIUNI SUB 1024px

## C1. Hero

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| **flex-direction al rândului** | **column** | **column** | **column** | **column** |
| gap | 32px | 32px | 32px | 32px |
| **padding vertical al rândului** (T/R/B/L) | **80 / 0 / 56 / 0** | **80 / 0 / 56 / 0** | **112 / 0 / 80 / 0** | **112 / 0 / 80 / 0** |
| padding al `<section>` | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| padding al containerului cu max-width | 0 / 16 / 0 / 16 | 0 / 16 / 0 / 16 | 0 / 64 / 0 / 64 | 0 / 64 / 0 / 64 |
| **ordinea vizuală a coloanelor** | **text** → **imagine** | **text** → **imagine** | **text** → **imagine** | **text** → **imagine** |
| coloana de text — width | 358 | 382 | 640 | 895 |
| coloana de text — x / y | 16 / 80 | 16 / 80 | 64 / 112 | 64 / 112 |
| coloana de imagine — width | 358 | 382 | 640 | 895 |
| coloana de imagine — x / y | 16 / 569.39 | 16 / 569.39 | 64 / 565.17 | 64 / 514.78 |
| **baza header-ului → primul text (eyebrow)** | **16 px** | **16 px** | **32 px** | **32 px** |

La toate patru viewport-urile rândul este **`column`**, iar ordinea vizuală este **text, apoi imagine** — coloana de text vine prima. Cele două coloane au lățimi egale, cât toată lățimea utilă a containerului. Padding-ul vertical stă pe **rândul interior**, nu pe `<section>` și nu pe containerul cu `max-width`: ambele au padding vertical 0.

Distanța de la baza header-ului fix până la eyebrow este mică pentru că header-ul e `position: fixed` și nu împinge conținutul: cei 16 px la 390 și 414, respectiv 32 px la 768 și 1023, sunt diferența dintre padding-ul de sus al rândului (80, respectiv 112 px) și înălțimea header-ului (64, respectiv 80 px).

## C2. Imaginea din hero

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| **înălțime randată** | **300** | **300** | **420** | **420** |
| lățime randată | 358 | 382 | 640 | 895 |
| **`object-fit`** | **cover** | **cover** | **cover** | **cover** |
| **`object-position`** | **50% 6%** | **50% 6%** | **50% 6%** | **50% 6%** |
| `aspect-ratio` calculat | `auto 1440 / 1800` | `auto 1440 / 1800` | `auto 1440 / 1800` | `auto 1440 / 1800` |
| raport efectiv randat (L/Î) | 1.19 | 1.27 | 1.52 | 2.13 |
| fișierul ales din srcset | `ioana-balan-ie-cosita-impletita-800.webp` | `ioana-balan-ie-cosita-impletita-800.webp` | `ioana-balan-ie-cosita-impletita-800.webp` | `ioana-balan-ie-cosita-impletita-1440.webp` |
| dimensiune intrinsecă randată | 390 × 487 | 414 × 517 | 768 × 960 | 1023 × 1278 |

`aspect-ratio` calculat este `auto 1440 / 1800` — provine din atributele `width`/`height` de pe `<img>`, nu dintr-o regulă CSS `aspect-ratio`. Raportul efectiv randat diferă de 0.8 (adică 1440/1800) pentru că înălțimea e fixată prin clasă și `object-fit: cover` decupează sursa. Pragul de schimbare a înălțimii este 768px: 300px sub el, 420px de la el.

## C3. Secțiunile din index.html


### 390×844

| # | Primul heading | padding vertical (T/B) | padding orizontal container (R/L) | lățime utilă | grid: coloane | gap grid |
|---|---|---|---|---|---|---|
| 1 | Formație Nuntă București Premium: Muzică de  | 0 / 0 | 16 / 16 | 358 | — | — |
| 2 | Muzică pentru nuntă, botez și corporate | 64 / 64 | 16 / 16 | 358 | **1** | 24px |
| 3 | Pachete pentru 2026–2027 | 64 / 64 | 16 / 16 | 358 | — | — |
| 4 | Peste 15 ani pe scenă | 64 / 64 | 16 / 16 | 358 | **1** | 40px |
| 5 | Vezi cum arată un eveniment | 64 / 64 | 16 / 16 | 358 | **1** | 16px |
| 6 | Ce Spun Mirii și Gazdele | 64 / 64 | 16 / 16 | 358 | **1** | 16px |
| 7 | Ce ne întrebați cel mai des | 64 / 64 | 16 / 16 | 358 | — | — |
| 8 | Rezervă Formație Nuntă | 64 / 64 | 0 / 0 | 390 | — | — |

### 414×896

| # | Primul heading | padding vertical (T/B) | padding orizontal container (R/L) | lățime utilă | grid: coloane | gap grid |
|---|---|---|---|---|---|---|
| 1 | Formație Nuntă București Premium: Muzică de  | 0 / 0 | 16 / 16 | 382 | — | — |
| 2 | Muzică pentru nuntă, botez și corporate | 64 / 64 | 16 / 16 | 382 | **1** | 24px |
| 3 | Pachete pentru 2026–2027 | 64 / 64 | 16 / 16 | 382 | — | — |
| 4 | Peste 15 ani pe scenă | 64 / 64 | 16 / 16 | 382 | **1** | 40px |
| 5 | Vezi cum arată un eveniment | 64 / 64 | 16 / 16 | 382 | **1** | 16px |
| 6 | Ce Spun Mirii și Gazdele | 64 / 64 | 16 / 16 | 382 | **1** | 16px |
| 7 | Ce ne întrebați cel mai des | 64 / 64 | 16 / 16 | 382 | — | — |
| 8 | Rezervă Formație Nuntă | 64 / 64 | 0 / 0 | 414 | — | — |

### 768×1024

| # | Primul heading | padding vertical (T/B) | padding orizontal container (R/L) | lățime utilă | grid: coloane | gap grid |
|---|---|---|---|---|---|---|
| 1 | Formație Nuntă București Premium: Muzică de  | 0 / 0 | 64 / 64 | 640 | — | — |
| 2 | Muzică pentru nuntă, botez și corporate | 96 / 96 | 64 / 64 | 640 | **3** | 24px |
| 3 | Pachete pentru 2026–2027 | 96 / 96 | 64 / 64 | 640 | — | — |
| 4 | Peste 15 ani pe scenă | 96 / 96 | 64 / 64 | 640 | **12** | 24px |
| 5 | Vezi cum arată un eveniment | 96 / 96 | 64 / 64 | 640 | **2** | 24px |
| 6 | Ce Spun Mirii și Gazdele | 96 / 96 | 64 / 64 | 640 | **3** | 24px |
| 7 | Ce ne întrebați cel mai des | 96 / 96 | 64 / 64 | 640 | — | — |
| 8 | Rezervă Formație Nuntă | 128 / 128 | 0 / 0 | 768 | — | — |

### 1023×768

| # | Primul heading | padding vertical (T/B) | padding orizontal container (R/L) | lățime utilă | grid: coloane | gap grid |
|---|---|---|---|---|---|---|
| 1 | Formație Nuntă București Premium: Muzică de  | 0 / 0 | 64 / 64 | 895 | — | — |
| 2 | Muzică pentru nuntă, botez și corporate | 96 / 96 | 64 / 64 | 895 | **3** | 24px |
| 3 | Pachete pentru 2026–2027 | 96 / 96 | 64 / 64 | 895 | — | — |
| 4 | Peste 15 ani pe scenă | 96 / 96 | 64 / 64 | 895 | **12** | 24px |
| 5 | Vezi cum arată un eveniment | 96 / 96 | 64 / 64 | 895 | **2** | 24px |
| 6 | Ce Spun Mirii și Gazdele | 96 / 96 | 64 / 64 | 895 | **3** | 24px |
| 7 | Ce ne întrebați cel mai des | 96 / 96 | 64 / 64 | 895 | — | — |
| 8 | Rezervă Formație Nuntă | 128 / 128 | 0 / 0 | 1023 | — | — |

Secțiunea 1 (hero) are padding 0 pe `<section>`; padding-ul ei vertical stă pe rândul interior (vezi C1). Secțiunea 8 are padding vertical mai mare decât restul la 768 și 1023 (`md:py-32`). Secțiunea 4 raportează 12 coloane la 768 și 1023 pentru că folosește `md:grid-cols-12`, cu doi copii care ocupă 5 și 7 coloane.

## C4. Cardurile — la ce viewport trec pe o coloană

| Grup de carduri | Secțiune | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|---|
| Servicii (3 carduri) | 2 | **1 col** · gap 24px | **1 col** · gap 24px | **3 col** · gap 24px | **3 col** · gap 24px |
| Despre (imagine + text) | 4 | **1 col** · gap 40px | **1 col** · gap 40px | **12 col** · gap 24px | **12 col** · gap 24px |
| Clipuri (2 carduri) | 5 | **1 col** · gap 16px | **1 col** · gap 16px | **2 col** · gap 24px | **2 col** · gap 24px |
| Recenzii (3 carduri) | 6 | **1 col** · gap 16px | **1 col** · gap 16px | **3 col** · gap 24px | **3 col** · gap 24px |

Toate gridurile trec pe o coloană **sub 768px** și se desfac la 768px — pragul este `md`, nu `lg`. Între 390 și 414 nu se schimbă nimic. Lățimile măsurate ale cardurilor:

| Grup | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| Servicii (3 carduri) | 358 · 358 · 358 | 382 · 382 · 382 | 197.33 · 197.33 · 197.33 | 282.33 · 282.33 · 282.34 |
| Despre (imagine + text) | 358 · 358 | 382 · 382 | 252.66 · 363.34 | 358.91 · 512.08 |
| Clipuri (2 carduri) | 358 · 358 | 382 · 382 | 308 · 308 | 435.50 · 435.50 |
| Recenzii (3 carduri) | 358 · 358 · 358 | 382 · 382 · 382 | 197.33 · 197.33 · 197.33 | 282.33 · 282.33 · 282.34 |

## C5. Toate `font-size`-urile randate din hero și din secțiunea 1

### Hero

| Element | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| eyebrow | 12 / 24 / 400 | 12 / 24 / 400 | 14 / 20 / 600 | 14 / 20 / 600 |
| h1 | 36 / 37.80 / 400 | 36 / 37.80 / 400 | 48 / 50.40 / 400 | 48 / 50.40 / 400 |
| paragraf | 16 / 24 / 400 | 16 / 24 / 400 | 18 / 28 / 400 | 18 / 28 / 400 |
| buton 1 | 14 / 20 / 600 | 14 / 20 / 600 | 14 / 20 / 600 | 14 / 20 / 600 |

Format: `font-size / line-height / font-weight`, toate în px.

### Secțiunea 2 (prima secțiune după hero)

| Element | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| eyebrow | 12 / 24 / 400 | 12 / 24 / 400 | 14 / 20 / 600 | 14 / 20 / 600 |
| h2 | 28 / 24 / 400 | 28 / 24 / 400 | 32 / 40 / 500 | 32 / 40 / 500 |
| h3 card | 24 / 32 / 500 | 24 / 32 / 500 | 24 / 32 / 500 | 24 / 32 / 500 |
| paragraf card | 16 / 24 / 400 | 16 / 24 / 400 | 16 / 24 / 400 | 16 / 24 / 400 |
| link card | 16 / 24 / 400 | 16 / 24 / 400 | 16 / 24 / 400 | 16 / 24 / 400 |

**Toate scalele se schimbă la 768px, niciuna între 390 și 414 și niciuna între 768 și 1023.** Măsurat, cele două praguri `sm` (640) și `lg` (1024) nu mută nicio mărime de font din hero sau din secțiunea 2.

O valoare de reținut la reproducere: `h2` din secțiunea 2 se randează la **28px font-size cu 24px line-height** sub 768px — adică o cutie de linie mai mică decât corpul literei. Clasa `text-[28px]` setează doar `font-size`; `line-height` rămâne cel moștenit de la `<body>`. De la 768px, `md:text-headline-lg` setează ambele: 32 / 40, greutate 500.

La fel, `<h1>` se randează la greutatea **400**, nu 500: poartă `font-display-lg` (doar familia) plus mărimi arbitrare, fără `text-display-lg`, deci `fontWeight` din tokenul `display-lg` nu se aplică niciodată.


# BLOC D — ELEMENTE FLOTANTE

## D1. Butonul WhatsApp

| Proprietate | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| position | fixed | fixed | fixed | fixed |
| z-index | 50 | 50 | 50 | 50 |
| **width × height** | **56 × 56** | **56 × 56** | **64 × 60** | **64 × 60** |
| padding T/R/B/L | 0 / 16 / 0 / 16 | 0 / 16 / 0 / 16 | 0 / 16 / 0 / 16 | 0 / 16 / 0 / 16 |
| background | #25d366 | #25d366 | #25d366 | #25d366 |
| border-radius | 9999px | 9999px | 9999px | 9999px |
| **eticheta — randată?** | **nu** | **nu** | da, dar lățime 0 | da, dar lățime 0 |
| eticheta — width | 0 | 0 | 0 | 0 |

Decalajele față de colțul din dreapta-jos și dimensiunile, măsurate pe o serie de lățimi în jurul pragurilor:

| Lățime viewport | buton | SVG | dreapta / jos | min-width | eticheta: dreptunghiuri | `display` | width | max-width | font-size / line-height / weight |
|---|---|---|---|---|---|---|---|---|---|
| 389 | 56 × 56 | 24x24 | 24 / 24 | 56px | 0 | `none` | 0 | 0px | 12 / 24 / 400 |
| 390 | 56 × 56 | 24x24 | 24 / 24 | 56px | 0 | `none` | 0 | 0px | 12 / 24 / 400 |
| 414 | 56 × 56 | 24x24 | 24 / 24 | 56px | 0 | `none` | 0 | 0px | 12 / 24 / 400 |
| 639 | 56 × 56 | 24x24 | 24 / 24 | 56px | 0 | `none` | 0 | 0px | 12 / 24 / 400 |
| 640 | 56 × 56 | 24x24 | 24 / 24 | 56px | 1 | `block` | 0 | 0px | 12 / 24 / 400 |
| 641 | 56 × 56 | 24x24 | 24 / 24 | 56px | 1 | `block` | 0 | 0px | 12 / 24 / 400 |
| 767 | 56 × 56 | 24x24 | 24 / 24 | 56px | 1 | `block` | 0 | 0px | 12 / 24 / 400 |
| 768 | 64 × 60 | 32x32 | 30 / 30 | 60px | 1 | `block` | 0 | 0px | 14 / 20 / 600 |
| 1023 | 64 × 60 | 32x32 | 30 / 30 | 60px | 1 | `block` | 0 | 0px | 14 / 20 / 600 |
| 1024 | 64 × 60 | 32x32 | 30 / 30 | 60px | 1 | `block` | 0 | 0px | 14 / 20 / 600 |

Două praguri distincte, ambele măsurate:

- **640px** — eticheta trece din `display: none` în `display: block`. Nu devine însă vizibilă: `max-width` rămâne `0px` și lățimea măsurată rămâne **0** la toate lățimile testate. Eticheta se deschide doar la `hover`/`focus-visible` pe buton, stare care nu apare pe un dispozitiv tactil.
- **768px** — butonul crește de la **56 × 56** la **64 × 60**, SVG-ul de la **24 × 24** la **32 × 32**, decalajele de la **24** la **30** px, iar tipografia etichetei de la 12 / 24 / 400 la 14 / 20 / 600.

Lățimea de 64px de la 768 în sus depășește `min-width: 60px` pentru că iconul de 32px plus cei 2 × 16px de padding orizontal dau 64px.

## D2. Suprapuneri între butonul flotant și conținut

Butonul e `position: fixed`, iar pagina nu are padding-bottom sau margine care să-i rezerve loc. Verificarea s-a făcut derulând pagina în pași de o jumătate de viewport, de sus până jos, și intersectând dreptunghiul butonului cu toate elementele `a, button, h1, h2, h3, p, img, input, textarea, label` randate. Se raportează suprapunerea maximă găsită pentru fiecare element.


### 390×844 — 10 elemente suprapuse

| Element | Text / alt | Suprapunere L × Î | Arie | La `scrollY` |
|---|---|---|---|---|
| `<img>` | Ioana Balan în ie albă cu broderie aurie, cu | 56 × 56 | 3136 | 0 |
| `<button>` | Muzică populară Colaj de Moldova, live l | 56 × 56 | 3136 | 3376 |
| `<img>` |  | 56 × 56 | 3136 | 3376 |
| `<img>` | Ioana Balan cântând la microfon pe scenă, în | 55 × 56 | 3080 | 2532 |
| `<p>` | Program potrivit pentru botez: muzică de | 39 × 56 | 2184 | 844 |
| `<p>` | Pentru mine, cea mai mare răsplată este  | 56 × 37.61 | 2106.13 | 2110 |
| `<a>` | +40 722 911 485 | 56 × 18.14 | 1015.88 | 6330 |
| `<h2>` | Vezi cum arată un eveniment | 56 × 12.61 | 706.13 | 2954 |
| `<a>` | Vezi toate întrebările frecvente | 49.41 × 4.14 | 204.57 | 5486 |
| `<p>` | Muzica nu este doar o profesie pentru mi | 56 × 2.39 | 133.88 | 2110 |

### 414×896 — 8 elemente suprapuse

| Element | Text / alt | Suprapunere L × Î | Arie | La `scrollY` |
|---|---|---|---|---|
| `<button>` | Formație live Formație de nuntă în Bucur | 56 × 56 | 3136 | 3136 |
| `<img>` |  | 56 × 56 | 3136 | 3136 |
| `<img>` | Ioana Balan cântând la microfon pe scenă, în | 55 × 56 | 3080 | 2688 |
| `<img>` | Ioana Balan în ie albă cu broderie aurie, cu | 56 × 53.39 | 2989.88 | 0 |
| `<a>` | Vezi toate întrebările frecvente | 37.41 × 44 | 1645.88 | 5376 |
| `<p>` | Formație live și sonorizare proprie, cu  | 39 × 20.61 | 803.77 | 448 |
| `<a>` | +40 722 911 485 | 56 × 7.14 | 399.88 | 6272 |
| `<h2>` | Pachete pentru 2026–2027 | 56 × 1.61 | 90.13 | 1344 |

### 768×1024 — 6 elemente suprapuse

| Element | Text / alt | Suprapunere L × Î | Arie | La `scrollY` |
|---|---|---|---|---|
| `<img>` | Ioana Balan în ie albă cu broderie aurie, cu | 30 × 51.17 | 1535.16 | 0 |
| `<p>` | Termeni și condiții · Politica de cookie | 30 × 37.42 | 1122.66 | 5632 |
| `<h2>` | Peste 15 ani pe scenă | 30 × 20.17 | 605.16 | 1536 |
| `<p>` | Muzica nu este doar o profesie pentru mi | 30 × 7.83 | 234.84 | 1536 |
| `<p>` | Muzică live și DJ pentru gale și recepți | 4.98 × 38.83 | 193.53 | 512 |
| `<h2>` | Pachete pentru 2026–2027 | 30 × 0.17 | 5.16 | 1024 |

### 1023×768 — 7 elemente suprapuse

| Element | Text / alt | Suprapunere L × Î | Arie | La `scrollY` |
|---|---|---|---|---|
| `<img>` | Ioana Balan în ie albă cu broderie aurie, cu | 30 × 60 | 1800 | 0 |
| `<p>` | Pentru mine, cea mai mare răsplată este  | 29.98 × 56.34 | 1689.43 | 1920 |
| `<h2>` | Ce ne întrebați cel mai des | 30 × 40 | 1200 | 3840 |
| `<h2>` | Pachete pentru 2026–2027 | 30 × 29.78 | 893.44 | 1152 |
| `<h2>` | Vezi cum arată un eveniment | 30 × 29.09 | 872.81 | 2304 |
| `<a>` |  | 30 × 19.88 | 596.25 | 5376 |
| `<p>` | Muzică live și DJ pentru gale și recepți | 5 × 60 | 300 | 768 |

Suprapunerea există la toate patru viewport-urile. Cazurile în care elementul acoperit este el însuși interactiv:

| Viewport | Element interactiv acoperit | Suprapunere |
|---|---|---|
| 390×844 | `<button>` Muzică populară Colaj de Moldova, live l | 56 × 56 px |
| 390×844 | `<a>` +40 722 911 485 | 56 × 18.14 px |
| 390×844 | `<a>` Vezi toate întrebările frecvente | 49.41 × 4.14 px |
| 414×896 | `<button>` Formație live Formație de nuntă în Bucur | 56 × 56 px |
| 414×896 | `<a>` Vezi toate întrebările frecvente | 37.41 × 44 px |
| 414×896 | `<a>` +40 722 911 485 | 56 × 7.14 px |
| 1023×768 | `<a>`  | 30 × 19.88 px |

## D3. Derulare orizontală

| Măsurătoare | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| `document.body.scrollWidth` | 390 | 414 | 768 | 1023 |
| `documentElement.scrollWidth` | 390 | 414 | 768 | 1023 |
| `window.innerWidth` | 390 | 414 | 768 | 1023 |
| `documentElement.clientWidth` | 390 | 414 | 768 | 1023 |
| **Derulare orizontală** | **nu** | **nu** | **nu** | **nu** |

**Nu există derulare orizontală la niciunul dintre cele patru viewport-uri.** `body.scrollWidth` este egal cu `window.innerWidth` la toate patru, deci nu există element care să depășească. `<body>` are `overflow-x: hidden`, ceea ce ar masca oricum o depășire; măsurătoarea arată că nu are ce masca — inclusiv drawer-ul închis, care stă translatat exact la marginea dreaptă a viewportului.

# CE TREBUIE SĂ APARĂ ȘI CE NU

Listă de verificare rulabilă direct pe implementarea din WordPress. Criteriul folosit este `el.getClientRects().length > 0`, nu `display`, din motivul explicat în METODĂ.

Fragment de rulat în consola browserului pe pagina reconstruită:

```js
const vis = s => { const e = document.querySelector(s); return e ? e.getClientRects().length > 0 : 'LIPSEȘTE DIN DOM'; };
['header nav', 'header a[href*="wa.me"]', 'header a[href^="tel:"]', '#menu-toggle',
 '#mobile-menu', '.whatsapp-float', '.whatsapp-float span'].forEach(s => console.log(s, vis(s)));
```

## 390×844

**Vizibile, în ordine de la stânga la dreapta în header:**

| # | Element | Selector | Dimensiune randată | x |
|---|---|---|---|---|
| 1 | link logo | `header a[href="index.html"]` | 93.42 × 44 | 16 |
| 2 | link telefon | `header a[href^="tel:"]` | 44 × 44 | 272 |
| 3 | buton hamburger | `#menu-toggle` | 46 × 46 | 328 |

**Restul paginii, vizibile:**

| Element | Selector | Dimensiune randată |
|---|---|---|
| `<header>` | `header` | 390 × 64 |
| butonul WhatsApp flotant | `.whatsapp-float` | 56 × 56 |
| drawer, închis (translatat în afara ecranului) | `#mobile-menu` | 390 × 844, la x = 390 |

**Ascunse — trebuie să aibă 0 dreptunghiuri de randare:**

| Element | Selector | Mecanism |
|---|---|---|
| nav desktop | `header nav` | `hidden lg:flex` |
| CTA WhatsApp din header | `header a[href*="wa.me"]` | `hidden lg:block` |
| eticheta butonului WhatsApp | `.whatsapp-float span` | `hidden sm:inline` |

**Stări de verificat, nu doar prezență:**

| Verificare | Valoare așteptată |
|---|---|
| `#mobile-menu` — `inert` cât e închis | `true` |
| `#mobile-menu` — `transform` cât e închis | `matrix(1, 0, 0, 1, 390, 0)` |
| `#menu-toggle` — `aria-expanded` cât e închis | `false` |
| `#menu-toggle` — `aria-controls` | `mobile-menu` |
| `<body>` — `overflow` cât drawer-ul e închis | `hidden auto` |
| `<body>` — `overflow` cât drawer-ul e deschis | `hidden` |
| după `Escape` — `document.activeElement.id` | `menu-toggle` |
| `document.body.scrollWidth` | 390 (egal cu `innerWidth`) |
| `<header>` height | 64 |
| container header — un singur rând | height = 63 |

## 414×896

**Vizibile, în ordine de la stânga la dreapta în header:**

| # | Element | Selector | Dimensiune randată | x |
|---|---|---|---|---|
| 1 | link logo | `header a[href="index.html"]` | 93.42 × 44 | 16 |
| 2 | link telefon | `header a[href^="tel:"]` | 44 × 44 | 296 |
| 3 | buton hamburger | `#menu-toggle` | 46 × 46 | 352 |

**Restul paginii, vizibile:**

| Element | Selector | Dimensiune randată |
|---|---|---|
| `<header>` | `header` | 414 × 64 |
| butonul WhatsApp flotant | `.whatsapp-float` | 56 × 56 |
| drawer, închis (translatat în afara ecranului) | `#mobile-menu` | 414 × 896, la x = 414 |

**Ascunse — trebuie să aibă 0 dreptunghiuri de randare:**

| Element | Selector | Mecanism |
|---|---|---|
| nav desktop | `header nav` | `hidden lg:flex` |
| CTA WhatsApp din header | `header a[href*="wa.me"]` | `hidden lg:block` |
| eticheta butonului WhatsApp | `.whatsapp-float span` | `hidden sm:inline` |

**Stări de verificat, nu doar prezență:**

| Verificare | Valoare așteptată |
|---|---|
| `#mobile-menu` — `inert` cât e închis | `true` |
| `#mobile-menu` — `transform` cât e închis | `matrix(1, 0, 0, 1, 414, 0)` |
| `#menu-toggle` — `aria-expanded` cât e închis | `false` |
| `#menu-toggle` — `aria-controls` | `mobile-menu` |
| `<body>` — `overflow` cât drawer-ul e închis | `hidden auto` |
| `<body>` — `overflow` cât drawer-ul e deschis | `hidden` |
| după `Escape` — `document.activeElement.id` | `menu-toggle` |
| `document.body.scrollWidth` | 414 (egal cu `innerWidth`) |
| `<header>` height | 64 |
| container header — un singur rând | height = 63 |

## 768×1024

**Vizibile, în ordine de la stânga la dreapta în header:**

| # | Element | Selector | Dimensiune randată | x |
|---|---|---|---|---|
| 1 | link logo | `header a[href="index.html"]` | 140.14 × 48 | 64 |
| 2 | link telefon | `header a[href^="tel:"]` | 44 × 44 | 602 |
| 3 | buton hamburger | `#menu-toggle` | 46 × 46 | 658 |

**Restul paginii, vizibile:**

| Element | Selector | Dimensiune randată |
|---|---|---|
| `<header>` | `header` | 768 × 80 |
| butonul WhatsApp flotant | `.whatsapp-float` | 64 × 60 |
| eticheta WhatsApp (randată, dar lățime 0) | `.whatsapp-float span` | 0 × 20 |
| drawer, închis (translatat în afara ecranului) | `#mobile-menu` | 768 × 1024, la x = 768 |

**Ascunse — trebuie să aibă 0 dreptunghiuri de randare:**

| Element | Selector | Mecanism |
|---|---|---|
| nav desktop | `header nav` | `hidden lg:flex` |
| CTA WhatsApp din header | `header a[href*="wa.me"]` | `hidden lg:block` |

**Stări de verificat, nu doar prezență:**

| Verificare | Valoare așteptată |
|---|---|
| `#mobile-menu` — `inert` cât e închis | `true` |
| `#mobile-menu` — `transform` cât e închis | `matrix(1, 0, 0, 1, 768, 0)` |
| `#menu-toggle` — `aria-expanded` cât e închis | `false` |
| `#menu-toggle` — `aria-controls` | `mobile-menu` |
| `<body>` — `overflow` cât drawer-ul e închis | `hidden auto` |
| `<body>` — `overflow` cât drawer-ul e deschis | `hidden` |
| după `Escape` — `document.activeElement.id` | `menu-toggle` |
| `document.body.scrollWidth` | 768 (egal cu `innerWidth`) |
| `<header>` height | 80 |
| container header — un singur rând | height = 79 |

## 1023×768

**Vizibile, în ordine de la stânga la dreapta în header:**

| # | Element | Selector | Dimensiune randată | x |
|---|---|---|---|---|
| 1 | link logo | `header a[href="index.html"]` | 140.14 × 48 | 64 |
| 2 | link telefon | `header a[href^="tel:"]` | 44 × 44 | 857 |
| 3 | buton hamburger | `#menu-toggle` | 46 × 46 | 913 |

**Restul paginii, vizibile:**

| Element | Selector | Dimensiune randată |
|---|---|---|
| `<header>` | `header` | 1023 × 80 |
| butonul WhatsApp flotant | `.whatsapp-float` | 64 × 60 |
| eticheta WhatsApp (randată, dar lățime 0) | `.whatsapp-float span` | 0 × 20 |
| drawer, închis (translatat în afara ecranului) | `#mobile-menu` | 1023 × 768, la x = 1023 |

**Ascunse — trebuie să aibă 0 dreptunghiuri de randare:**

| Element | Selector | Mecanism |
|---|---|---|
| nav desktop | `header nav` | `hidden lg:flex` |
| CTA WhatsApp din header | `header a[href*="wa.me"]` | `hidden lg:block` |

**Stări de verificat, nu doar prezență:**

| Verificare | Valoare așteptată |
|---|---|
| `#mobile-menu` — `inert` cât e închis | `true` |
| `#mobile-menu` — `transform` cât e închis | `matrix(1, 0, 0, 1, 1023, 0)` |
| `#menu-toggle` — `aria-expanded` cât e închis | `false` |
| `#menu-toggle` — `aria-controls` | `mobile-menu` |
| `<body>` — `overflow` cât drawer-ul e închis | `hidden auto` |
| `<body>` — `overflow` cât drawer-ul e deschis | `hidden` |
| după `Escape` — `document.activeElement.id` | `menu-toggle` |
| `document.body.scrollWidth` | 1023 (egal cu `innerWidth`) |
| `<header>` height | 80 |
| container header — un singur rând | height = 79 |

## Rezumat pe cele patru viewport-uri

| Verificare | 390×844 | 414×896 | 768×1024 | 1023×768 |
|---|---|---|---|---|
| `header nav` vizibil | nu | nu | nu | nu |
| `header a[href*=wa.me]` vizibil | nu | nu | nu | nu |
| `header a[href^=tel:]` vizibil | **da** | **da** | **da** | **da** |
| `#menu-toggle` vizibil | **da** | **da** | **da** | **da** |
| `#menu-toggle` dimensiune | 46 × 46 | 46 × 46 | 46 × 46 | 46 × 46 |
| `<header>` height | 64 | 64 | 80 | 80 |
| header pe un singur rând | **da** | **da** | **da** | **da** |
| `.whatsapp-float` dimensiune | 56 × 56 | 56 × 56 | 64 × 60 | 64 × 60 |
| `.whatsapp-float span` randat | nu | nu | **da** (lățime 0) | **da** (lățime 0) |
| hero pe o coloană | **da** | **da** | **da** | **da** |
| ordinea în hero | text → imagine | text → imagine | text → imagine | text → imagine |
| griduri de carduri | 1 coloană | 1 coloană | 3 coloane | 3 coloane |
| derulare orizontală | nu | nu | nu | nu |