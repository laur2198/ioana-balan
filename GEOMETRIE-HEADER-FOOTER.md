# GEOMETRIE HEADER & FOOTER — valori rezolvate în px

Extract de geometrie pentru reconstrucția header-ului și footer-ului în
WordPress + Elementor. Toate valorile sunt rezolvate în px. Nu conține
recomandări.

---

## STARE GIT

| Element | Valoare |
|---|---|
| Branch curent | `main` |
| Upstream | `origin/main` (https://github.com/laur2198/ioana-balan) |
| Working tree | curat — `nothing to commit, working tree clean` |
| Commit-uri nepushate | **0** — `git log origin/main..HEAD` returnează listă goală |
| HEAD la start | `df2d425` — *sync: aliniere wp-child-theme cu serverul + raport de paritate CSS* |

Fișier nou scris de această rulare: `GEOMETRIE-HEADER-FOOTER.md`. Niciun
fișier existent nu a fost modificat.

---

## METODĂ

### Fișiere scanate

| Fișier | Rol în extract |
|---|---|
| `index.html` | sursa canonică pentru header, drawer, footer, skip-link, buton WhatsApp |
| `articol.html`, `blog.html`, `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` | verificare de paritate (diff pe blocurile `<header>`, drawer, `<footer>`, skip-link, `.whatsapp-float`) |
| `assets/tailwind.config.js` | tokeni de culoare, spacing, fontFamily, fontSize — citiți la runtime, nu hardcodați |
| `assets/styles.css` | CSS custom: `.skip-link`, `.whatsapp-float`, `.bg-accent`, `scroll-padding-top` |
| `https://cdn.tailwindcss.com?plugins=forms,container-queries` | descărcat la runtime (418 973 B) pentru a citi din bundle scala implicită, Preflight-ul și **ordinea plugin-urilor** — de ea depinde ce utilitară câștigă la conflict |

### Echivalențe folosite

- spacing implicit: `n` = n × 4px; `px` = 1px; `-n` = −n × 4px
- tokeni proprii de spacing (din `assets/tailwind.config.js`):
  `margin-desktop` = 64px, `margin-mobile` = 16px, `gutter` = 24px,
  `unit` = 8px, `max-width` = 1200px
- 1rem = 16px
- breakpoint-uri: sm 640 / md 768 / lg 1024 / xl 1280
- format al valorilor: `bază / md / lg / xl`, cu breakpoint-ul numit unde
  saltul e la altul decât md

### Tokeni de fontSize proprii (toate cele patru proprietăți)

Citite din `theme.extend.fontSize`. Utilitara `text-<token>` emite toate
patru simultan.

| Token | font-size | line-height | letter-spacing | font-weight |
|---|---|---|---|---|
| `display-lg` | 48px | 56px | −0.02em (−0,96px) | 500 |
| `headline-lg` | 32px | 40px | normal (neprecizat) | 500 |
| `headline-lg-mobile` | 28px | 36px | normal (neprecizat) | 500 |
| `headline-md` | 24px | 32px | normal (neprecizat) | 500 |
| `body-lg` | 18px | 28px | normal (neprecizat) | 400 |
| `body-md` | 16px | 24px | normal (neprecizat) | 400 |
| `label-md` | 14px | 20px | 0.05em (0,70px) | 600 |

Familiile: `font-label-md`/`font-body-md`/`font-body-lg` → **Inter**;
`font-headline-md`/`font-headline-lg`/`font-display-lg` → **EB Garamond**.
Ambele sunt self-hosted din `assets/fonts/` (fără cerere la Google Fonts).

### Reguli de cascadă verificate în bundle-ul CDN

Contează pentru trei conflicte reale din header/footer, deci le-am
verificat în sursă, nu din memorie. Ordinea plugin-urilor din bundle este:

`… "fontFamily", "fontSize", "fontWeight", "textTransform", "fontStyle", "fontVariantNumeric", "lineHeight", "letterSpacing", "textColor" … "transitionProperty", "transitionDelay", "transitionDuration", "transitionTimingFunction" …`

Consecințe:

1. `letterSpacing` se generează **după** `fontSize` → pe elementele cu
   `text-label-md tracking-widest`, letter-spacing-ul final este
   **0.1em (1,40px)**, nu 0.05em din token.
2. `transitionDuration` după `transitionProperty` → `duration-300`
   suprascrie cele 150ms implicite ale lui `transition-transform`.
3. Preflight setează `*,::after,::before { box-sizing: border-box }`,
   `svg { display: block; vertical-align: middle }` și
   `button { font-size:100%; line-height:inherit; letter-spacing:inherit; padding:0; margin:0 }`.
   `svg{display:block}` schimbă calculul de înălțime al butoanelor cu icon:
   se adună cutia blocului SVG, nu line-box-ul.

### Confirmare de paritate pe cele 11 pagini

| Bloc | Rezultat |
|---|---|
| `<footer>` | **identic la caracter** pe toate cele 11 pagini |
| drawer mobil `#mobile-menu` | **identic la caracter** pe toate cele 11 pagini |
| `.whatsapp-float` | **identic la caracter** pe toate cele 11 pagini |
| skip-link | **identic la caracter** pe toate cele 11 pagini |
| `<header>` — structură, container, logo, CTA, buton telefon, hamburger | **identice** pe toate cele 11 pagini |
| `<header>` — nav | **diferă doar prin marcajul paginii active** (vezi mai jos) |

Singura diferență reală în header: linkul paginii curente schimbă clasele
din
`text-on-surface-variant … hover:text-primary transition-colors duration-300 uppercase`
în
`text-primary border-b border-primary pb-1 … uppercase`
— adică: culoare `#c8c6c5` în loc de `#c4c7c7`, bordură inferioară 1px
`#c8c6c5`, padding-bottom 4px, și **fără** tranziție/hover.

| Fișier | Item marcat activ |
|---|---|
| `index.html` | niciunul |
| `despre.html` | **două** — `despre.html` „Despre" **și** `oferte.html` „Oferte" |
| `galerie.html` | `galerie.html` |
| `discografie.html` | `discografie.html` |
| `oferte.html` | `oferte.html` |
| `faq.html` | `faq.html` |
| `blog.html` | `blog.html` |
| `articol.html` | `blog.html` |
| `contact.html` | `contact.html` |
| `politica-cookie.html` | niciunul |
| `termeni-si-conditii.html` | niciunul |

### Excluderi

- `articol.html`, `faq.html`, `politica-cookie.html`,
  `termeni-si-conditii.html` conțin un **al doilea element `<header>`** în
  corpul paginii (antet de articol / de document legal). Nu face parte din
  header-ul de site și este exclus din acest extract.
- Lățimile randate ale textelor (butoane, itemi de nav) depind de metrica
  fontului la randare și sunt marcate NEDETERMINAT unde apar.

---

# BLOC A — HEADER

## A1. Elementul `<header>`

Clase: `fixed top-0 w-full z-50 bg-background/95 backdrop-blur-md border-b border-outline-variant/20 h-16 md:h-20`

| Proprietate | Bază (0–767) | md (≥768) |
|---|---|---|
| position | `fixed` | `fixed` |
| top / left | 0px / 0px (`top-0`, implicit stânga prin `w-full`) | idem |
| width | 100% din `<body>` | 100% |
| z-index | 50 | 50 |
| height | **64px** | **80px** |
| background | token `background` `#131313` la 95% → `rgba(19, 19, 19, 0.95)` | idem |
| backdrop-filter | `blur(12px)` (`backdrop-blur-md`) | idem |
| bordură | **jos**, 1px solid, token `outline-variant` `#444748` la 20% → `rgba(68, 71, 72, 0.2)` | idem |
| border-radius | 0px (nicio clasă `rounded-*`) | idem |
| padding propriu | 0px | 0px |

Înălțimea totală ocupată vizual, cu bordură inclusă (box-sizing
border-box → bordura e **în** cei 64/80px): **64px / 80px**.

## A2. Containerul interior al header-ului

Clase: `max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop flex justify-between items-center gap-4 xl:gap-8 h-full`

### Cele patru lățimi (box-sizing: border-box)

| Breakpoint | Lățime declarată | Padding lateral | **Lățime utilă a conținutului** | **Lățime totală ocupată** |
|---|---|---|---|---|
| bază (0–767) | `max-width: 1200px` | 16px + 16px = **32px** | `min(1200, L) − 32` | `min(1200px, L)` |
| md (≥768) | `max-width: 1200px` | 64px + 64px = **128px** | `min(1200, L) − 128` | `min(1200px, L)` |

`L` = lățimea disponibilă a `<body>` (viewport-ul, `body` are `overflow-x-hidden`).
Valori concrete:

| Viewport | Lățime declarată | Padding lateral | Lățime utilă conținut | Lățime totală ocupată |
|---|---|---|---|---|
| 360px | 1200px | 32px | **328px** | 360px |
| 768px | 1200px | 128px | **640px** | 768px |
| 1024px | 1200px | 128px | **896px** | 1024px |
| 1200px | 1200px | 128px | **1072px** | 1200px |
| 1280px | 1200px | 128px | **1072px** | 1200px (centrat, 40px margine auto/parte) |
| 1440px | 1200px | 128px | **1072px** | 1200px (centrat, 120px margine auto/parte) |

### Restul proprietăților containerului

| Proprietate | Bază | md (≥768) | xl (≥1280) |
|---|---|---|---|
| display | `flex` | `flex` | `flex` |
| flex-direction | `row` (implicit) | idem | idem |
| align-items | `center` | idem | idem |
| justify-content | `space-between` | idem | idem |
| gap | **16px** | 16px | **32px** |
| height | 100% din header → **64px** | **80px** | 80px |
| margin | `0 auto` (mx-auto) | idem | idem |

Ordinea celor trei flex-item-uri: `[link logo] · [nav desktop] · [grup dreapta]`.
Sub 1024px nav-ul e `display:none`, deci `justify-content: space-between`
împinge logo-ul la stânga și grupul de butoane la dreapta.

## A3. Logo

| Proprietate | Valoare |
|---|---|
| Fișier `src` | `assets/logo-alb-400w.png` |
| `srcset` | `assets/logo-alb-400w.png 1x, assets/logo-alb-800w.png 2x` |
| Dimensiuni native `400w` | **400 × 137 px** (19 208 B) |
| Dimensiuni native `800w` | **800 × 274 px** (38 317 B) |
| Raport nativ | 400 : 137 = **2,9197 : 1** |
| Atribute `width`/`height` din markup | 400 / 137 |
| `alt` | `Ioana Balan` |
| `loading` / `decoding` | `eager` / `async` |

| Proprietate | Bază (0–767) | md (≥768) |
|---|---|---|
| Înălțime afișată (`h-8` / `md:h-12`) | **32px** | **48px** |
| Lățime | `auto` (`w-auto`) → **93,43px** | **140,15px** |
| display | `block` (Preflight `img{display:block}`) | idem |

Linkul care îl înconjoară:

| Proprietate | Valoare |
|---|---|
| Clase | `shrink-0 flex items-center min-h-[44px]` |
| `href` | `index.html` |
| `aria-label` | `Ioana Balan Acasă` |
| display | `flex` |
| align-items | `center` |
| flex-shrink | 0 |
| **min-height** | **44px** |
| Înălțime efectivă | max(44px, 32px) = **44px** bază; max(44px, 48px) = **48px** de la md |
| padding | 0px |
| Lățime | egală cu a imaginii: 93,43px / 140,15px |

## A4. Nav desktop

| Proprietate | Valoare |
|---|---|
| Clase pe `<nav>` | `hidden lg:flex items-center gap-4 xl:gap-8` |
| Vizibil de la | **lg = 1024px**. Sub 1024px: `display: none` |
| display | `flex` (row) de la 1024px |
| align-items | `center` |
| **gap** | **16px** la 1024–1279px · **32px** de la 1280px |

### Sursa spațierii dintre itemi — important pentru Elementor

Spațierea vine **exclusiv din `gap` pe părinte** (`gap-4 xl:gap-8` pe
`<nav>`). Itemii de nav au **padding 0px** pe toate laturile — singura
excepție e linkul paginii active, care primește `pb-1` = **padding-bottom
4px**, și acela nu pentru spațiere, ci ca distanță până la bordura
inferioară de marcaj.

În Elementor: se mapează pe `gap` (Space Between) al containerului de
meniu, **nu** pe padding-ul itemului. Padding pe item ar dubla
distanța la capete și ar mări zona de tap, ceea ce prototipul nu face.

### Proprietățile unui link de nav (stare normală, pagină inactivă)

Clase: `text-on-surface-variant font-label-md text-label-md hover:text-primary transition-colors duration-300 uppercase`

| Proprietate | Valoare |
|---|---|
| Culoare normală | token `on-surface-variant` → **#c4c7c7** |
| Culoare hover | token `primary` → **#c8c6c5** |
| Tranziție | `color, background-color, border-color, text-decoration-color, fill, stroke` — 300ms, `cubic-bezier(0.4, 0, 0.2, 1)` |
| font-family | **Inter** |
| font-size | **14px** |
| line-height | **20px** |
| letter-spacing | **0,70px** (0.05em din tokenul `label-md`; nu există `tracking-*` care să-l suprascrie) |
| font-weight | **600** |
| text-transform | **uppercase** |
| padding | **0px** pe toate laturile |
| margin | 0px |
| bordură | niciuna |
| Înălțime cutie | 20px (line-height) |

### Link de nav — starea „pagină activă"

Clase: `text-primary border-b border-primary pb-1 font-label-md text-label-md uppercase`

| Proprietate | Valoare |
|---|---|
| Culoare | **#c8c6c5** (token `primary`) |
| Culoare hover | identică — **nu are `hover:`**, nici `transition` |
| Bordură | **jos**, 1px solid **#c8c6c5** (opacitate 100%) |
| padding-bottom | **4px** |
| padding restul laturilor | 0px |
| Înălțime cutie | 20 + 4 + 1 = **25px** |
| Tipografie | identică cu starea normală (Inter 14/20, 0,70px, 600, uppercase) |

### Itemii nav-ului desktop, în ordine

| # | Text | Destinație |
|---|---|---|
| 1 | Despre | `despre.html` |
| 2 | Galerie | `galerie.html` |
| 3 | Discografie | `discografie.html` |
| 4 | Oferte | `oferte.html` |
| 5 | FAQ | `faq.html` |
| 6 | Blog | `blog.html` |
| 7 | Contact | `contact.html` |

## A5. Butonul CTA din header

Clase: `hidden lg:block whitespace-nowrap shrink-0 bg-accent text-white px-4 xl:px-6 py-2 font-label-md text-label-md uppercase tracking-widest hover:bg-accent-hover transition-all`

| Proprietate | Valoare |
|---|---|
| Text exact | **Rezervă pe WhatsApp** |
| `href` | `https://wa.me/40722911485?text=Bun%C4%83%20ziua%21%20A%C8%99%20dori%20s%C4%83%20rezerv%20o%20dat%C4%83%20pentru%20evenimentul%20meu.` |
| Număr apelat | `40722911485` |
| **Mesaj precompletat, decodat** | **„Bună ziua! Aș dori să rezerv o dată pentru evenimentul meu."** |
| `target` / `rel` | `_blank` / `noopener` |
| Vizibil de la | **lg = 1024px** (`hidden lg:block`); sub 1024px `display:none` |
| display | `block` |
| flex-shrink | 0 |
| white-space | `nowrap` |

| Proprietate | Bază (ascuns) | lg (1024–1279) | xl (≥1280) |
|---|---|---|---|
| padding stânga/dreapta | — | **16px** | **24px** |
| padding sus/jos | — | **8px** | **8px** |

| Proprietate | Valoare |
|---|---|
| background normal | token `accent` → **#A01028** |
| background hover | token `accent-hover` → **#800020** |
| Culoare text | **#ffffff** |
| **Bordură** | **1px solid #C41236** — vine din `assets/styles.css`: `.bg-accent { border: 1px solid var(--accent-edge) }`, cu `--accent-edge: #C41236` pe `:root`. Nu e vizibilă în clase. |
| border-radius | **0px** (nicio clasă `rounded-*`; `borderRadius.DEFAULT` din config = 4px se aplică doar cu clasa `rounded`) |
| font-family | **Inter** |
| font-size | **14px** |
| line-height | **20px** |
| letter-spacing | **1,40px** (0.1em din `tracking-widest`, care suprascrie 0.05em al tokenului — vezi METODĂ) |
| font-weight | **600** |
| text-transform | **uppercase** |
| text-align | `start` (moștenit) |
| Tranziție | `transition-all` — toate proprietățile, 150ms, `cubic-bezier(0.4, 0, 0.2, 1)` |
| **Înălțime totală** | 20 (line-height) + 8 + 8 (padding) + 1 + 1 (bordură) = **38px** |
| Lățime totală | NEDETERMINAT — `width` nu e declarată, iar cutia e dictată de avansul textului „Rezervă pe WhatsApp" în Inter 600 / 14px / 1,40px letter-spacing. Determinabilă doar la randare. Părțile fixe sunt 16+16+1+1 = **34px** (lg) și 24+24+1+1 = **50px** (xl) adăugate peste lățimea textului. |

## A6. Butonul de telefon (mobil)

Clase: `lg:hidden flex items-center justify-center w-11 h-11 -mr-1 text-primary hover:text-white transition-colors`

| Proprietate | Valoare |
|---|---|
| Vizibil | de la 0 până la **1023px**; `display:none` de la lg = 1024px |
| display | `flex`, `align-items:center`, `justify-content:center` |
| Lățime × înălțime | **44 × 44 px** |
| margin-right | **−4px** (`-mr-1`) |
| padding | 0px |
| Culoare normală | token `primary` → **#c8c6c5** |
| Culoare hover | **#ffffff** |
| Tranziție | `transition-colors`, 150ms, `cubic-bezier(0.4, 0, 0.2, 1)` |
| `href` | `tel:+40722911485` |
| `aria-label` | **Sună acum** |
| Icon | **SVG inline** (nu font de icoane) |
| `viewBox` | `0 -960 960 960` |
| Dimensiune SVG | `width="24" height="24"` → **24 × 24 px**, fill `currentColor` |
| `aria-hidden` pe SVG | `true` |

`path` (`d`), integral:

```
M775.38-140Q669-140 556-193.69q-113-53.7-210.81-151.7-97.8-98-151.5-210.8Q140-669 140-775.38q0-19.12 12.64-31.87T184.23-820h114.13q15.64 0 26.41 10.19 10.77 10.2 15.15 26.35l23.85 107.18q2.08 15.13-1 27.2-3.08 12.08-11.69 20.31l-94.39 91.92q26.77 45.93 56.54 85.08t64.39 73.54q37.38 38.38 79.53 70.08 42.16 31.69 90.24 57.61l90.76-93.38q10-11 22.39-14.81 12.39-3.81 25.84-1.81l97.08 21.39q16.15 3.61 26.35 16.26Q820-310.24 820-294.23v110q0 18.95-12.75 31.59T775.38-140ZM234-578l82.54-80.08q1.54-1.53 2.11-4.23.58-2.69.2-5L297-768.46q-.38-3.08-2.5-4.62-2.11-1.53-5.19-1.53h-98.54q-2.31 0-3.85 1.53-1.53 1.54-1.53 3.85.84 41.62 12.92 88.69Q210.39-633.46 234-578Zm356.31 349.15q41 20.16 89.77 31.39 48.77 11.23 89.15 12.46 2.31 0 3.85-1.54 1.53-1.54 1.53-3.85v-98.15q0-3.08-1.53-5.19-1.54-2.12-4.62-2.5l-90.69-18.69q-2.31-.39-4.04.19-1.73.58-3.65 2.11l-79.77 83.77ZM234-578Zm356.31 349.15Z
```

Comentariul din DOM, imediat înaintea butonului:

```html
<!-- Contact la 1 tap pe mobil: sub lg butonul WhatsApp e ascuns, iar telefonul
     era doar în footer. Părinții/nașii sună, nu scriu pe WhatsApp. -->
```

## A7. Butonul hamburger

Clase: `lg:hidden text-primary p-2`, `id="menu-toggle"`

| Proprietate | Valoare |
|---|---|
| Vizibil | 0 → **1023px**; `display:none` de la lg = 1024px |
| padding | **8px** pe toate laturile |
| Culoare | token `primary` → **#c8c6c5** |
| background | transparent (Preflight: `button{background-color:transparent}`) |
| bordură | 0px (Preflight `*{border-width:0}`) |
| border-radius | 0px |
| cursor | `pointer` (Preflight) |
| Icon | SVG inline, clasă `text-3xl` → font-size **30px**; `width="1em" height="1em"` → **30 × 30 px** |
| `viewBox` | `0 -960 960 960` |
| Cutie SVG | `display:block` (Preflight) → 30 × 30 px, fără line-box |
| **Dimensiune buton** | 30 + 8 + 8 = **46 × 46 px** |
| `aria-label` | **Deschide Meniu** |
| `aria-expanded` | **`false`** în markup; comutat pe `"true"`/`"false"` de `setMenu()` |
| `aria-controls` | **`mobile-menu`** |
| `aria-hidden` pe SVG | `true` |

`path` (`d`): `M140-254.62V-300h680v45.38H140Zm0-202.69v-45.38h680v45.38H140ZM140-660v-45.38h680V-660H140Z`

Grupul care conține telefonul și hamburgerul: `<div class="flex items-center gap-4">`
→ display `flex`, align-items `center`, **gap 16px**. La lg conține și CTA-ul,
tot la gap 16px.

---

# BLOC B — DRAWER-UL MOBIL

## B1. Containerul drawer-ului

Clase: `fixed inset-0 z-[60] bg-background translate-x-full transition-transform duration-300 lg:hidden`, `id="mobile-menu"`, atribut `inert`

| Proprietate | Valoare |
|---|---|
| position | `fixed` |
| inset | `top:0; right:0; bottom:0; left:0` → acoperă tot viewport-ul |
| Dimensiune | 100vw × 100vh |
| **z-index** | **60** (peste header-ul cu z-index 50) |
| background | token `background` → **#131313**, opacitate **100%** (fără `/95` ca la header) |
| Vizibil | 0 → **1023px**; `display:none` de la lg = 1024px |
| **Transform la ieșire (închis)** | `translateX(100%)` — clasa `translate-x-full` prezentă |
| **Transform la intrare (deschis)** | `none` — clasa `translate-x-full` este **eliminată**, nu înlocuită cu `translate-x-0` |
| transition-property | `transform` |
| **transition-duration** | **300ms** (`duration-300` bate cele 150ms implicite ale lui `transition-transform`) |
| transition-timing-function | `cubic-bezier(0.4, 0, 0.2, 1)` |
| padding propriu | 0px (padding-ul e pe wrapper-ul interior) |

Atributul `inert`:

| Aspect | Valoare |
|---|---|
| În markup | prezent, fără valoare → drawer-ul pornește inert |
| Comutare | `mobileMenu.inert = !open` în `setMenu()` |
| Efect | scoate drawer-ul din tab order **și** din arborele de accesibilitate cât e ascuns |
| Efect secundar la deschidere | `document.body.classList.toggle('overflow-hidden', open)` → `overflow:hidden` pe `<body>` |
| Închidere | click pe `#menu-close` (cu refocus pe `#menu-toggle`), tasta `Escape` (cu refocus), sau click pe orice link din drawer (fără refocus) |

Wrapper-ul interior: `<div class="flex flex-col h-full p-8">`

| Proprietate | Valoare |
|---|---|
| display | `flex`, direcție `column` |
| height | 100% → 100vh |
| **padding** | **32px** pe toate cele patru laturi |
| Lățime utilă a conținutului | `100vw − 64px` (ex. la 360px viewport: **296px**) |
| gap | niciunul declarat (spațierea vine din `mb-12` și din `gap-6` pe `<nav>`) |

## B2. Antetul din drawer

Clase pe rând: `flex justify-between items-center mb-12`

| Proprietate | Valoare |
|---|---|
| display | `flex`, row |
| justify-content | `space-between` |
| align-items | `center` |
| **margin-bottom** | **48px** |

Logo:

| Proprietate | Valoare |
|---|---|
| Clase | `h-8 w-auto` |
| **Înălțime afișată** | **32px** — constantă, fără variantă la md |
| Lățime | auto → **93,43px** |
| `src` / `srcset` | `assets/logo-alb-400w.png` / `…-400w.png 1x, …-800w.png 2x` |
| Native | 400 × 137 |
| `loading` / `decoding` | `eager` / `async` |
| Link în jur | **niciunul** — logo-ul din drawer nu e clicabil (spre deosebire de header și footer) |

Butonul de închidere:

| Proprietate | Valoare |
|---|---|
| `id` | `menu-close` |
| Clase | `text-primary` |
| `aria-label` | **Închide Meniu** |
| Culoare | **#c8c6c5** |
| padding | **0px** (Preflight; nicio clasă de padding) |
| Icon | SVG inline, `text-4xl` → font-size **36px**, `width="1em" height="1em"` → **36 × 36 px** |
| `viewBox` | `0 -960 960 960` |
| **Dimensiune buton** | **36 × 36 px** |
| `aria-hidden` pe SVG | `true` |
| `path` | `m250.92-218.92-32-32L448-480 218.92-709.08l32-32L480-512l229.08-229.08 32 32L512-480l229.08 229.08-32 32L480-448 250.92-218.92Z` |

## B3. Nav vertical din drawer

Clase pe `<nav>`: `flex flex-col gap-6 text-center`

| Proprietate | Valoare |
|---|---|
| display | `flex`, direcție `column` |
| **gap între itemi** | **24px** |
| align-items | `stretch` (implicit) → fiecare link ocupă toată lățimea utilă |
| text-align | **center** |
| Lățimea unui item | `100vw − 64px` |

Proprietăți tipografice, identice pentru toți itemii:

| Proprietate | Valoare |
|---|---|
| font-family | **EB Garamond** (`font-headline-md`) |
| font-size | **24px** |
| line-height | **32px** |
| letter-spacing | **normal** (tokenul `headline-md` nu declară letterSpacing, nicio clasă `tracking-*`) |
| font-weight | **500** |
| text-transform | **uppercase** |
| padding | **0px** |
| margin | 0px |
| Tranziție / hover | **niciuna** — itemii din drawer nu au stare de hover declarată |
| Înălțime cutie | **32px** |

Culorile — primul item diferă de restul:

| Item | Clasă de culoare | Token | Hex |
|---|---|---|---|
| **„Acasă" (primul)** | `text-primary` | `primary` | **#c8c6c5** |
| Toate celelalte 7 | `text-on-surface-variant` | `on-surface-variant` | **#c4c7c7** |

Diferența dintre cele două este de 4 puncte pe R și 2 pe B
(`#c8c6c5` vs `#c4c7c7`).

## B4. CTA-ul din josul drawer-ului

Clase: `text-headline-md font-headline-md text-white uppercase bg-accent py-4 mt-4`

| Proprietate | Valoare |
|---|---|
| Text exact | **Rezervă pe WhatsApp** |
| `href` | `https://wa.me/40722911485?text=Bun%C4%83%20ziua%21%20A%C8%99%20dori%20s%C4%83%20rezerv%20o%20dat%C4%83%20pentru%20evenimentul%20meu.` |
| Mesaj decodat | **„Bună ziua! Aș dori să rezerv o dată pentru evenimentul meu."** — **identic** cu CTA-ul din header |
| `target` / `rel` | `_blank` / `noopener` |
| Poziție | ultimul copil al `<nav>`-ului din drawer |
| background | token `accent` → **#A01028** |
| background hover | **niciun hover declarat** (spre deosebire de CTA-ul din header) |
| **Bordură** | **1px solid #C41236** — din `.bg-accent` în `assets/styles.css` |
| border-radius | **0px** |
| Culoare text | **#ffffff** |
| font-family | **EB Garamond** |
| font-size | **24px** |
| line-height | **32px** |
| letter-spacing | normal |
| font-weight | **500** |
| text-transform | uppercase |
| text-align | **center** (moștenit din `text-center` al `<nav>`) |
| padding sus/jos | **16px** |
| padding stânga/dreapta | **0px** |
| margin-top | **16px** |
| **Distanța reală față de „Contact"** | 24px (gap-ul flex) + 16px (`mt-4`) = **40px** |
| **Înălțime totală** | 32 + 16 + 16 + 1 + 1 = **66px** |
| Lățime | întinsă pe lățimea utilă a drawer-ului: `100vw − 64px` |

## B5. Lista completă a itemilor din drawer și comparația cu nav-ul desktop

| # | Text exact în drawer | Destinație | Există în nav-ul desktop? |
|---|---|---|---|
| 1 | **Acasă** | `index.html` | **NU** |
| 2 | Despre | `despre.html` | da (poz. 1) |
| 3 | Galerie | `galerie.html` | da (poz. 2) |
| 4 | Discografie | `discografie.html` | da (poz. 3) |
| 5 | Oferte | `oferte.html` | da (poz. 4) |
| 6 | **Întrebări frecvente** | `faq.html` | da (poz. 5), dar cu textul **„FAQ"** |
| 7 | Blog | `blog.html` | da (poz. 6) |
| 8 | Contact | `contact.html` | da (poz. 7) |
| 9 | **Rezervă pe WhatsApp** | `https://wa.me/40722911485?text=…` | există ca CTA, dar **în afara** `<nav>` |

Diferențele, explicit:

| Aspect | Desktop | Drawer |
|---|---|---|
| **Număr de itemi în `<nav>`** | 7 | **9** (8 de meniu + CTA) |
| **„Acasă"** | absent — rolul e preluat de linkul din jurul logo-ului (`aria-label="Ioana Balan Acasă"`) | prezent ca item de meniu, primul |
| **Formularea pentru `faq.html`** | **„FAQ"** | **„Întrebări frecvente"** |
| **CTA-ul WhatsApp** | element separat, frate al `<nav>`, în grupul din dreapta | **înăuntrul** `<nav>`, ultimul copil |
| **Ordinea celor 7 itemi comuni** | identică (Despre → Galerie → Discografie → Oferte → FAQ → Blog → Contact) | identică |
| **Marcaj de pagină activă** | da (`text-primary` + bordură inferioară, per pagină) | **nu** — „Acasă" e `text-primary` pe **toate** paginile, nu doar pe `index.html` |

---

# BLOC C — FOOTER

## C1. Elementul `<footer>`

Clase: `w-full bg-surface-container-lowest border-t border-outline-variant/10`

| Proprietate | Valoare |
|---|---|
| width | 100% |
| position | `static` |
| background | token `surface-container-lowest` → **#0e0e0e** (opac) |
| **Bordură sus** | 1px solid, token `outline-variant` `#444748` la **10%** → `rgba(68, 71, 72, 0.1)` |
| Bordură pe celelalte laturi | 0px |
| border-radius | 0px |
| padding propriu | 0px |

Notă: header-ul folosește `outline-variant/20`, footer-ul `outline-variant/10`
— aceeași culoare, opacități diferite (0,2 vs 0,1).

## C2. Containerul interior al footer-ului

Clase: `max-w-[1200px] mx-auto px-margin-mobile md:px-margin-desktop py-8 md:py-12 flex flex-col gap-8`

### Cele patru lățimi (box-sizing: border-box)

| Breakpoint | Lățime declarată | Padding lateral | **Lățime utilă a conținutului** | **Lățime totală ocupată** |
|---|---|---|---|---|
| bază (0–767) | `max-width: 1200px` | 16px + 16px = **32px** | `min(1200, L) − 32` | `min(1200px, L)` |
| md (≥768) | `max-width: 1200px` | 64px + 64px = **128px** | `min(1200, L) − 128` | `min(1200px, L)` |

Valori concrete — identice cu ale header-ului:

| Viewport | Lățime declarată | Padding lateral | Lățime utilă conținut | Lățime totală ocupată |
|---|---|---|---|---|
| 360px | 1200px | 32px | **328px** | 360px |
| 768px | 1200px | 128px | **640px** | 768px |
| 1024px | 1200px | 128px | **896px** | 1024px |
| ≥1200px | 1200px | 128px | **1072px** | 1200px (centrat) |

### Padding vertical și gap

| Proprietate | Bază (0–767) | md (≥768) |
|---|---|---|
| padding-top | **32px** | **48px** |
| padding-bottom | **32px** | **48px** |
| padding stânga/dreapta | **16px** | **64px** |
| display | `flex`, `column` | idem |
| **gap între benzi** | **32px** | **32px** (constant) |
| margin | `0 auto` | idem |

Trei benzi (copii direcți), separate de gap-ul de 32px. Între banda 2 și
banda 3 stă un bloc **comentat** (rândul CUI / Reg. Com. — vezi C9); fiind
comentariu, nu consumă gap.

## C3. Benzile, în ordine

| Bandă | Conținut | display | flex-direction bază | flex-direction sm (≥640) | flex-direction md (≥768) | align-items | justify-content | gap bază | gap sm | gap md |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | brand (logo + descriere) + listă de iconițe social | `flex` | `column` | `column` | **`row`** | `stretch` bază → **`center`** de la md | `flex-start` bază → **`space-between`** de la md | **16px** | 16px | **24px** |
| **2** | wrapper: contact + ANPC/SAL, apoi documente legale | `flex` | `column` | `column` | `column` | `stretch` | `flex-start` | **16px** | 16px | 16px |
| **2a** | (în banda 2) e-mail + telefon · ANPC + SAL | `flex` | `column` | **`row`** | `row` | `stretch` | `flex-start` bază → **`space-between`** de la sm | **16px** | **32px** | 32px |
| **2b** | (în banda 2) Termeni și condiții · Politica de cookie-uri | `flex` | `row` + `wrap` | idem | idem | **`center`** | `flex-start` | column-gap **8px**, row-gap 0px | idem | idem |
| **3** | trei paragrafe juridice + două separatoare | `flex` | `column` | **`row` + `wrap`** | idem | `stretch` bază → **`center`** de la sm | **`center`** | x **8px** / y **4px** | idem | idem |

Banda 3 are în plus `text-center` la toate breakpoint-urile.
Banda 2a: pe mobil e coloană (contact deasupra, ANPC/SAL dedesubt); de la
640px devine rând cu cele două grupuri împinse la extreme.

## C4. Zona de brand

Clase pe container: `flex flex-col gap-3 max-w-md`

| Proprietate | Valoare |
|---|---|
| display | `flex`, `column` |
| **max-width** | `max-w-md` = 28rem = **448px** |
| **gap intern** | **12px** (între link-logo și paragraf) |
| flex-shrink | implicit 1 |

Logo:

| Proprietate | Bază (0–767) | md (≥768) |
|---|---|---|
| **Înălțime afișată** (`h-8` / `md:h-10`) | **32px** | **40px** |
| Lățime (`w-auto`) | **93,43px** | **116,79px** |

| Proprietate | Valoare |
|---|---|
| `src` / `srcset` | `assets/logo-alb-400w.png` / `…-400w.png 1x, …-800w.png 2x` |
| Native | 400 × 137 |
| `loading` / `decoding` | `lazy` / `async` |
| Clase pe link | `inline-flex items-center min-h-[44px] self-start` |
| `href` / `aria-label` | `index.html` / `Ioana Balan Acasă` |
| display link | `inline-flex`, align-items `center` |
| **min-height link** | **44px** |
| align-self | `flex-start` — linkul nu se întinde pe cele 448px |
| Înălțime efectivă link | max(44, 32) = **44px** bază; max(44, 40) = **44px** de la md |

Paragraful de descriere:

| Proprietate | Valoare |
|---|---|
| Clase | `font-body-md text-body-md text-on-surface-variant opacity-80` |
| **Text exact** | „Muzică pentru evenimente care rămân în suflet. Calitate corporate cu pasiune artistică și profesionalism garantat." |
| Culoare | token `on-surface-variant` → **#c4c7c7** |
| **opacity** | **0.8** → randat efectiv ≈ `#a6a8a8` peste fundalul `#0e0e0e` |
| font-family | **Inter** |
| font-size | **16px** |
| line-height | **24px** |
| letter-spacing | **normal** |
| font-weight | **400** |
| text-transform | none |
| margin | 0px (Preflight resetează marginile la `p`) |
| Lățime maximă | 448px (moștenită din `max-w-md`) |

## C5. Iconițele social

Container `<ul class="flex flex-row items-center gap-1 shrink-0">`

| Proprietate | Valoare |
|---|---|
| display | `flex`, `row` |
| align-items | `center` |
| **gap între iconițe** | **4px** |
| flex-shrink | 0 |
| list-style | none (Preflight resetează `ul`) |
| padding/margin `ul` | 0px |

Fiecare `<a>`: `flex items-center justify-center w-11 h-11 text-on-surface-variant hover:text-primary transition-colors`

| Proprietate | Valoare |
|---|---|
| **Zona de tap** | **44 × 44 px** |
| display | `flex`, centrat pe ambele axe |
| padding | 0px |
| **Culoare normală** | token `on-surface-variant` → **#c4c7c7** |
| **Culoare hover** | token `primary` → **#c8c6c5** |
| Tranziție | `transition-colors`, 150ms, `cubic-bezier(0.4, 0, 0.2, 1)` |
| **Dimensiune SVG** | `width="20" height="20"` → **20 × 20 px** |
| `viewBox` SVG | `0 0 24 24` (toate patru) |
| fill | `currentColor` |
| `aria-hidden` pe SVG | `true` |
| `target` / `rel` | `_blank` / `noopener` (toate patru) |
| Lățime totală a listei | 4 × 44 + 3 × 4 = **188px** |

| # | Rețea | `aria-label` | URL complet |
|---|---|---|---|
| 1 | Facebook | `Facebook` | `https://www.facebook.com/ioanabalanoficial` |
| 2 | Instagram | `Instagram` | `https://www.instagram.com/ioanabalanoficial/` |
| 3 | YouTube | `YouTube` | `https://www.youtube.com/channel/UCNTWODu5imMryMhkbbw6vEQ` |
| 4 | TikTok | `TikTok` | `https://www.tiktok.com/@ioanabalanmusic` |

## C6. Zona de contact și ANPC/SAL

Wrapper: `<div class="flex flex-col sm:flex-row sm:justify-between gap-4 sm:gap-8">`

| Proprietate | Bază (0–639) | sm (≥640) |
|---|---|---|
| flex-direction | `column` | **`row`** |
| justify-content | `flex-start` | **`space-between`** |
| gap | **16px** | **32px** |
| align-items | `stretch` | `stretch` |

### Grupul de contact (stânga)

`<div class="flex flex-col">` — fără gap; spațierea vine exclusiv din
`min-h-[44px]` pe fiecare link.

| # | Text exact | Destinație |
|---|---|---|
| 1 | `ioanabalanoficial@gmail.com` | `mailto:ioanabalanoficial@gmail.com` |
| 2 | `+40 722 911 485` | `tel:+40722911485` |

Clase pe fiecare: `font-body-md text-on-surface-variant hover:text-primary transition-colors flex items-center min-h-[44px]`

| Proprietate | Valoare |
|---|---|
| Culoare normală | **#c4c7c7** |
| Culoare hover | **#c8c6c5** |
| Tranziție | `transition-colors`, 150ms |
| font-family | **Inter** (`font-body-md` setează doar familia) |
| **font-size** | **16px** — **moștenit de la `<body>`** (`text-body-md`), nu declarat pe link. Nu există clasă `text-body-md` aici, doar `font-body-md`. |
| line-height | **24px** (moștenit) |
| letter-spacing | normal (moștenit) |
| font-weight | **400** (moștenit) |
| **min-height** | **44px** |
| display | `flex`, `align-items:center` |
| padding | 0px |
| Înălțimea grupului | 2 × 44 = **88px** |

### Grupul ANPC/SAL (dreapta)

`<div class="flex flex-row items-center gap-2 sm:justify-end">`

| Proprietate | Bază (0–639) | sm (≥640) |
|---|---|---|
| flex-direction | `row` (deja rând pe mobil) | `row` |
| align-items | `center` | `center` |
| **gap** | **8px** | **8px** |
| justify-content | `flex-start` | **`flex-end`** |

| Element | Text exact | Destinație | `aria-label` |
|---|---|---|---|
| Link 1 | **ANPC** | `https://anpc.ro` | — (fără) |
| Separator | **`·`** (U+00B7, MIDDLE DOT) | — | — |
| Link 2 | **SAL** | `https://anpc.ro/ce-este-sal/` | `SAL — Soluționarea alternativă a litigiilor` |

Clase pe ambele linkuri: `font-body-md text-on-surface-variant hover:text-primary transition-colors inline-flex items-center min-h-[44px]`

| Proprietate | Valoare |
|---|---|
| Culoare normală / hover | **#c4c7c7** / **#c8c6c5** |
| font-family | Inter |
| font-size / line-height / weight | **16px / 24px / 400** — moștenite de la `<body>` |
| **min-height** | **44px** |
| display | `inline-flex`, `align-items:center` |
| padding | 0px |
| `target` / `rel` | `_blank` / `noopener noreferrer` (ambele) |

**Separatorul dintre ANPC și SAL:**

```html
<span aria-hidden="true" class="font-body-md text-on-surface-variant opacity-50">·</span>
```

| Proprietate | Valoare |
|---|---|
| Caracter | `·` (U+00B7) |
| **`aria-hidden`** | **`true`** — da, are |
| Culoare | **#c4c7c7** la **opacity 0.5** |
| font-family | Inter |
| font-size | 16px (moștenit) |
| Distanța până la fiecare link | 8px (gap-ul părintelui) de fiecare parte |

Între separator și linkul SAL, în DOM, stă acest comentariu:

```html
<!-- TODO client/juridic: platforma europeană SOL/ODR (ec.europa.eu/consumers/odr)
     a fost desființată prin Regulamentul (UE) 2024/3228. Linkul echivalent în
     vigoare e SAL-ul ANPC; de confirmat cu juristul înainte de lansare. -->
```

## C7. Rândul de documente legale

```html
<p class="font-body-md text-[13px] text-secondary flex flex-row flex-wrap items-center gap-x-2">
```

| Proprietate | Valoare |
|---|---|
| display | `flex`, `row`, `flex-wrap: wrap` |
| align-items | `center` |
| **column-gap** | **8px** |
| row-gap | 0px |
| **font-size** | **13px** (arbitrar `text-[13px]`) |
| line-height | **24px** — moștenit de la `<body>`, nu recalculat de valoarea arbitrară |
| letter-spacing | normal |
| font-weight | 400 |
| font-family | **Inter** |
| **Culoare** | token `secondary` → **#c6c6c6** |
| margin | 0px |

| Element | Text exact | Destinație |
|---|---|---|
| Link 1 | **Termeni și condiții** | `termeni-si-conditii.html` |
| **Separator** | **`·`** (U+00B7), `aria-hidden="true"`, `class="opacity-50"` → **#c6c6c6 la opacity 0.5**, 13px | — |
| Link 2 | **Politica de cookie-uri** | `politica-cookie.html` |

Clase pe ambele linkuri: `hover:text-primary transition-colors inline-flex items-center min-h-[44px]`
→ culoare normală **#c6c6c6** (moștenită din `<p>`), hover **#c8c6c5**,
`min-height` **44px**, `display:inline-flex`, padding 0px.

Comentariul din DOM, deasupra rândului:

```html
<!-- Documente de subsol: linkuri reale, în afara navigației din header.
     Aceeași stilizare discretă ca înainte; min-h-[44px] pentru țintă de tap,
     ca la rândul ANPC/SAL de deasupra. -->
```

## C8. Rândul juridic de jos (banda 3)

```html
<div class="flex flex-col sm:flex-row sm:flex-wrap sm:items-center justify-center gap-x-2 gap-y-1 text-center">
```

| Proprietate | Bază (0–639) | sm (≥640) |
|---|---|---|
| display | `flex` | `flex` |
| flex-direction | **`column`** | **`row`** |
| flex-wrap | `nowrap` | **`wrap`** |
| align-items | `stretch` | **`center`** |
| justify-content | `center` (pe axa verticală — fără efect orizontal) | **`center`** (pe axa orizontală) |
| **column-gap** | **8px** | **8px** |
| **row-gap** | **4px** | **4px** |
| text-align | **center** | **center** |

Comportament: pe mobil cele trei paragrafe se stivuiesc, fiecare pe lățime
plină, centrate prin `text-align:center`, la 4px distanță pe verticală, iar
cele două separatoare sunt **ascunse** (`hidden`). De la 640px cele trei
paragrafe și cele două separatoare stau pe un rând (cu wrap la nevoie),
centrate orizontal, la 8px distanță.

| # | Tip | Text exact | Vizibil bază | Vizibil sm |
|---|---|---|---|---|
| 1 | `<p>` | **© 2026 Ioana Balan. Toate drepturile rezervate.** | da | da |
| 2 | `<span>` separator | **`·`** (U+00B7) | **nu** (`hidden`) | **da** (`sm:inline`) |
| 3 | `<p>` | **Proiect dezvoltat de Grand Music Events** — „Grand Music Events" este link către `https://grand-music.ro` (`target="_blank" rel="noopener"`) | da | da |
| 4 | `<span>` separator | **`·`** (U+00B7) | **nu** (`hidden`) | **da** (`sm:inline`) |
| 5 | `<p>` | **Site realizat de Green Pheonix Concept** | da | da |

| Proprietate | Cele trei `<p>` | Cele două separatoare |
|---|---|---|
| Clase | `font-body-md text-[12px] text-secondary` | `hidden sm:inline font-body-md text-[12px] text-secondary opacity-50` |
| **font-size** | **12px** | **12px** |
| line-height | **24px** (moștenit de la `<body>`) | 24px |
| letter-spacing | normal | normal |
| font-weight | 400 | 400 |
| font-family | **Inter** | **Inter** |
| **Culoare** | token `secondary` → **#c6c6c6** | **#c6c6c6** la **opacity 0.5** |
| `aria-hidden` | — | **`true`** |
| margin | 0px | 0px |

Linkul „Grand Music Events" din paragraful 3: clase
`hover:text-primary transition-colors` → normal **#c6c6c6** (moștenit),
hover **#c8c6c5**, fără `min-height`, fără padding, 12px.

Comentariul din DOM, deasupra benzii:

```html
<!-- Banda 3: juridic. Benzile se separă prin spațiere, nu prin linie.
     Pe desktop cele trei elemente stau pe un rând, separate prin punct median
     (separatorul deja folosit în proiect); pe mobil se stivuiesc, centrate.
     „Pheonix" este ortografia juridică înregistrată a firmei — nu se corectează. -->
```

## C9. Elemente comentate în DOM

### C9.1 — Rândul cu CUI și Reg. Com. (între banda 2 și banda 3)

Blocul, reprodus **integral**, cu tot cu comentariul explicativ:

```html
<!-- TODO client — rând de date de firmă, OBLIGATORIU înainte de lansare.
     Concurența afișează CUI + Reg. Com.; pentru un site care încasează avans,
     legitimitatea juridică e argument de conversie.
     Scos din DOM doar cât ține demo-ul: un placeholder vizibil citește ca
     lucru neterminat, nu ca dependență de client. Se reactivează completând
     cele două valori și ștergând comentariul din jurul rândului de mai jos.
     ATENȚIE: datele Grand Music Events (clientul), NU Green Pheonix Concept
     (furnizorul site-ului).
<p class="font-body-md text-[12px] text-secondary opacity-80">Grand Music Events · CUI ... · Reg. Com. ...</p>
-->
```

Geometria pe care ar avea-o la reactivare:

| Proprietate | Valoare |
|---|---|
| Poziție | copil direct al containerului footer-ului, **între banda 2 și banda 3** → primește gap-ul de 32px de ambele părți |
| font-family | **Inter** |
| font-size | **12px** |
| line-height | 24px (moștenit) |
| font-weight | 400 |
| Culoare | token `secondary` **#c6c6c6** la **opacity 0.8** |
| Text placeholder | `Grand Music Events · CUI ... · Reg. Com. ...` (cu `·` U+00B7 ca separator) |
| margin | 0px |
| Lățime | 100% din lățimea utilă a containerului |

### C9.2 — Celelalte comentarii din footer

| Poziție | Comentariu |
|---|---|
| Deasupra benzii 1 | `<!-- Banda 1: brand + social (iconuri, un singur rând și pe mobil) -->` |
| Deasupra benzii 2 | `<!-- Banda 2: contact (stânga) + informații legale (dreapta), fără titluri de coloană -->` |
| În grupul ANPC/SAL | TODO SOL/ODR — reprodus la C6 |
| Deasupra rândului de documente legale | reprodus la C7 |
| Deasupra benzii 3 | reprodus la C8 |

### C9.3 — Comentariu din header

| Poziție | Comentariu |
|---|---|
| Deasupra `<header>` | `<!-- TopNavBar -->` urmat de `<!-- TopNavBar (canonic) -->` |
| Înaintea butonului de telefon | reprodus la A6 |

---

# BLOC D — ELEMENTE GLOBALE

## D1. Skip link

Markup (identic pe toate cele 11 pagini, primul element din `<body>`):

```html
<a class="skip-link" href="#continut">Sari la conținut</a>
```

Definiție CSS (`assets/styles.css`), fără nicio clasă Tailwind:

| Proprietate | Stare ascunsă (implicit) | Stare `:focus` |
|---|---|---|
| position | `absolute` | `absolute` |
| **left** | **−9999px** | **8px** |
| **top** | **0px** | **8px** |
| **z-index** | **100** | 100 |
| background-color | **#A01028** (valoare literală în CSS, egală cu tokenul `accent`) | idem |
| color | **#ffffff** | idem |
| **padding** | **12px sus/jos, 20px stânga/dreapta** | idem |
| font-family | **Inter** | idem |
| font-size | **16px** | idem |
| line-height | 24px (moștenit de la `<body>`) | idem |
| font-weight | 400 (moștenit) | idem |
| text-decoration | **none** | idem |
| border / border-radius | 0px / 0px | idem |
| **Înălțime cutie** | 24 + 12 + 12 = **48px** | **48px** |

| Proprietate | Valoare |
|---|---|
| **Text exact** | **Sari la conținut** |
| Țintă | `#continut` → `<main id="continut" tabindex="-1">` |
| Contur la focus | `outline: 2px solid #c8c6c5; outline-offset: 2px` (regula globală `:focus-visible`) |
| Ținta la focus | `main[tabindex="-1"]:focus { outline: none }` — fără contur la focus programatic |

Ascunderea se face prin deplasare în afara ecranului (`left:-9999px`), nu
prin `display:none`.

## D2. Butonul WhatsApp flotant

Markup: `<a aria-label="Contact Ioana Balan pe WhatsApp" class="whatsapp-float group" href="…" target="_blank" rel="noopener">`

| Proprietate | Valoare |
|---|---|
| `aria-label` | **Contact Ioana Balan pe WhatsApp** |
| `href` | `https://wa.me/40722911485?text=Bun%C4%83%20ziua%21%20A%C8%99%20dori%20mai%20multe%20informa%C8%9Bii.` |
| Număr | `40722911485` |
| **Mesaj precompletat, decodat** | **„Bună ziua! Aș dori mai multe informații."** — **diferit** de mesajul CTA-urilor din header și drawer |
| `target` / `rel` | `_blank` / `noopener` |

### Geometrie (`.whatsapp-float`)

| Proprietate | Bază (0–767) | md (≥768) |
|---|---|---|
| position | `fixed` | `fixed` |
| **bottom** | **24px** | **30px** |
| **right** | **24px** | **30px** |
| **z-index** | **50** | 50 |
| width | `auto` | `auto` |
| **min-width** | **56px** | **60px** |
| **height** | **56px** | **60px** |
| padding | **0px sus/jos, 16px stânga/dreapta** | idem (nesuprascris la md) |
| display | `flex`, `align-items:center`, `justify-content:center` | idem |
| background-color | **#25d366** (verde WhatsApp, literal în CSS — nu e token de proiect) | idem |
| color | **#ffffff** | idem |
| **border-radius** | **9999px** | 9999px |
| box-shadow (repaus) | `0 4px 12px rgba(0, 0, 0, 0.3)` | idem |
| transition | `transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)` | idem |
| **hover** | `transform: scale(1.1)` → 61,6px înălțime randată | `scale(1.1)` → 66px |

**Nu dispare la niciun breakpoint** — butonul e vizibil pe toată gama de
lățimi. Doar **eticheta** din interior dispare (vezi mai jos).

### Animația

| Proprietate | Valoare |
|---|---|
| Nume | **`whatsapp-pulse`** |
| Durată | **2,5s** |
| Iterații | `infinite` |
| Timing-function | implicit `ease` (nedeclarat) |

Keyframes, rezolvate:

| Etapă | `box-shadow` |
|---|---|
| **0%** | `0 4px 12px rgba(0, 0, 0, 0.3), 0 0 0 0 rgba(37, 211, 102, 0.45)` |
| **70%** | `0 4px 12px rgba(0, 0, 0, 0.3), 0 0 0 14px rgba(37, 211, 102, 0)` |
| **100%** | `0 4px 12px rgba(0, 0, 0, 0.3), 0 0 0 0 rgba(37, 211, 102, 0)` |

Inelul crește de la **0px la 14px** rază de răspândire și se stinge la 0
opacitate până la 70% din ciclu; restul de 30% e pauză.

`@media (prefers-reduced-motion: reduce)` → `.whatsapp-float { animation: none }`
și `html { scroll-behavior: auto }`.

### Iconul

| Proprietate | Valoare |
|---|---|
| Clase | `shrink-0 md:w-8 md:h-8` |
| Atribute | `width="24" height="24"` |
| **Dimensiune** | **24 × 24 px** bază · **32 × 32 px** de la md (clasele `md:w-8 md:h-8` bat atributele) |
| `viewBox` | `0 0 16 16` |
| fill | `currentColor` → #ffffff |
| `aria-hidden` | `true` |
| flex-shrink | 0 |

### Eticheta care se extinde

Clase: `max-w-0 overflow-hidden group-hover:max-w-xs group-focus-visible:max-w-xs group-hover:ml-2 group-focus-visible:ml-2 transition-all duration-300 font-label-md text-[12px] md:text-label-md uppercase whitespace-nowrap hidden sm:inline`

| Proprietate | Valoare |
|---|---|
| **Text exact** | **Salut! Scrie-mi pe WhatsApp** |
| **Dispare sub** | **sm = 640px** (`hidden sm:inline`). Sub 640px butonul rămâne cerc de 56px. |
| display | `none` sub 640px; de la 640px `inline`, blocificat în `block` de contextul flex al părintelui |
| **max-width repaus** | **0px** (`max-w-0`) |
| **max-width la hover / focus-visible pe `.group`** | **320px** (`max-w-xs` = 20rem) |
| overflow | `hidden` |
| margin-left repaus | **0px** |
| margin-left la hover / focus-visible | **8px** (`ml-2`) |
| **Tranziție** | `transition-all` — **300ms**, `cubic-bezier(0.4, 0, 0.2, 1)`; animă simultan `max-width` și `margin-left` |
| Declanșator | `group-hover` **și** `group-focus-visible` — se extinde și la navigare cu tastatura |
| white-space | `nowrap` |
| text-transform | uppercase |
| font-family | **Inter** |
| font-size | **12px** bază · **14px** de la md |
| line-height | **24px** (moștenit) bază · **20px** de la md |
| letter-spacing | **normal** bază · **0,70px** (0.05em) de la md |
| font-weight | **400** (moștenit) bază · **600** de la md |

Notă: sub 768px, `text-[12px]` setează **doar** font-size; line-height,
letter-spacing și font-weight rămân moștenite de la `<body>`
(24px / normal / 400). De la 768px, `md:text-label-md` le setează pe toate
patru.

### Lățimea totală a butonului

| Stare | Lățime |
|---|---|
| Repaus, <640px | `max(56, 0 + 24 + 32)` = **56px** (min-width câștigă) |
| Repaus, 640–767px | eticheta are max-width 0 → **56px** |
| Repaus, ≥768px | **60px** |
| Extins (hover/focus) | 32 (icon) + 8 (ml) + lățimea textului (≤320px) + 32 (padding) — NEDETERMINAT ca valoare exactă: depinde de avansul textului „Salut! Scrie-mi pe WhatsApp" la randare, plafonat de `max-width:320px` pe etichetă |

## D3. `scroll-padding-top`

```css
html { scroll-padding-top: 64px; }
@media (min-width: 768px) { html { scroll-padding-top: 80px; } }
```

| Breakpoint | `scroll-padding-top` | Înălțimea header-ului | Relație |
|---|---|---|---|
| bază (0–767) | **64px** | **64px** (`h-16`) | **egale** |
| md (≥768) | **80px** | **80px** (`md:h-20`) | **egale** |

Legătura: header-ul e `position: fixed`, deci e scos din fluxul documentului
și nu împinge conținutul. Fără `scroll-padding-top`, orice salt la o ancoră
(`#continut` din skip-link, ancorele din pagini) ar poziționa ținta la
`top: 0` al viewport-ului, **sub** header, ascunzând primii 64/80px ai
țintei. Valoarea este calibrată exact pe înălțimea header-ului la fiecare
breakpoint, iar breakpoint-ul regulii (768px) este **același** cu cel la
care header-ul trece de la `h-16` la `h-20`.

La migrare: dacă înălțimea header-ului se schimbă în Elementor, cele două
valori trebuie schimbate odată cu ea, altfel ancorele se dezaliniază.

---

# MAPARE ELEMENTOR

## Corecția de box-sizing

**Prototip (Tailwind, `box-sizing: border-box`):** pe
`max-w-[1200px] px-margin-desktop`, cei 1200px includ padding-ul. Lățimea
utilă a conținutului = 1200 − 128 = **1072px**.

**Elementor (container „Boxed"):** valoarea din câmpul **Content Width**
(`boxed_width`) se aplică wrapper-ului **interior**; padding-ul containerului
se adaugă **în afara** ei.

Rezultă regula de conversie:

```
boxed_width_Elementor = latime_declarata_Tailwind − (padding_stanga + padding_dreapta)
padding_Elementor     = padding_Tailwind (neschimbat)
```

Verificare la trei lățimi de viewport, cu `boxed_width = 1072` și `padding = 64`:

| Viewport | Prototip: lățime conținut | Elementor: `min(1072, viewport − 128)` | Coincid |
|---|---|---|---|
| 900px | 900 − 128 = 772px | min(1072, 772) = 772px | da |
| 1200px | 1200 − 128 = 1072px | min(1072, 1072) = 1072px | da |
| 1440px | 1200 − 128 = 1072px | min(1072, 1312) = 1072px | da |

## Corespondența breakpoint-urilor

| Tailwind | Elementor (implicit) | Interval |
|---|---|---|
| bază (0–767) | **Mobile** | ≤ 767px |
| md (768–1023) | **Tablet** | 768–1024px |
| md/lg/xl (≥1024) | **Desktop** | > 1024px |

Pragul Tailwind `md` = 768 coincide cu pragul Elementor Mobile/Tablet = 768.
Pragurile `lg` (1024) și `xl` (1280) **nu** au corespondent implicit în
Elementor: pentru nav, CTA și gap-uri e nevoie de breakpoint-uri
suplimentare activate în *Site Settings → Layout → Breakpoints*
(„Tablet Extra" / „Desktop") sau de CSS custom.

## Tabelul de mapare

| Container | Breakpoint Elementor | `boxed_width` | `padding` (sus / dreapta / jos / stânga) | Lățime totală rezultată |
|---|---|---|---|---|
| **Header — container interior** | Mobile (≤767) | **1168px** | 0 / **16px** / 0 / **16px** | min(1200, viewport) |
| | Tablet (768–1024) | **1072px** | 0 / **64px** / 0 / **64px** | min(1200, viewport) |
| | Desktop (>1024) | **1072px** | 0 / **64px** / 0 / **64px** | min(1200, viewport) |
| **Footer — container interior** | Mobile (≤767) | **1168px** | **32px** / **16px** / **32px** / **16px** | min(1200, viewport) |
| | Tablet (768–1024) | **1072px** | **48px** / **64px** / **48px** / **64px** | min(1200, viewport) |
| | Desktop (>1024) | **1072px** | **48px** / **64px** / **48px** / **64px** | min(1200, viewport) |
| **Drawer mobil — wrapper interior** | Mobile + Tablet (≤1024) | **Full Width** (nu boxed) | **32px** pe toate laturile | 100vw |

## Restul containerelor (Flexbox, fără lățime declarată)

Acestea sunt containere „Full Width" în Elementor — nu au `max-width`, deci
corecția de box-sizing nu se aplică. Se mapează 1:1.

| Container | Direcție | Align items | Justify | Gap | Padding | Alte valori |
|---|---|---|---|---|---|---|
| Header — rând principal | Row (toate) | Center | Space Between | 16px · **32px de la 1280** | 0 | height 64px / 80px de la 768 |
| Header — `<nav>` desktop | Row | Center | Start | 16px · **32px de la 1280** | 0 | ascuns sub 1024 |
| Header — grup dreapta | Row | Center | Start | **16px** | 0 | — |
| Drawer — antet | Row | Center | Space Between | 0 | 0 | **margin-bottom 48px** |
| Drawer — `<nav>` | Column | Stretch | Start | **24px** | 0 | text-align center |
| Footer — banda 1 | Column → **Row de la 768** | Stretch → **Center de la 768** | Start → **Space Between de la 768** | 16px → **24px de la 768** | 0 | — |
| Footer — zona de brand | Column | Stretch | Start | **12px** | 0 | **max-width 448px** |
| Footer — listă social | Row | Center | Start | **4px** | 0 | flex-shrink 0; lățime totală 188px |
| Footer — banda 2 | Column | Stretch | Start | **16px** | 0 | — |
| Footer — banda 2a | Column → **Row de la 640** | Stretch | Start → **Space Between de la 640** | 16px → **32px de la 640** | 0 | — |
| Footer — grup contact | Column | Stretch | Start | **0px** | 0 | spațierea vine din min-height 44px pe linkuri |
| Footer — grup ANPC/SAL | Row | Center | Start → **End de la 640** | **8px** | 0 | — |
| Footer — rând documente legale | Row + Wrap | Center | Start | x **8px** / y 0 | 0 | — |
| Footer — banda 3 | Column → **Row + Wrap de la 640** | Stretch → **Center de la 640** | **Center** | x **8px** / y **4px** | 0 | text-align center |
| Footer — container exterior (`<footer>`) | — | — | — | — | 0 | bg #0e0e0e; border-top 1px rgba(68,71,72,0.1) |

## Valori care nu se exprimă în câmpurile standard Elementor

| Element | Valoare | Unde ajunge |
|---|---|---|
| `.bg-accent { border: 1px solid #C41236 }` | bordură 1px pe **ambele** CTA-uri WhatsApp (header + drawer) | câmpul Border al butonului, sau CSS custom — nu e vizibilă în clasele din markup |
| `backdrop-filter: blur(12px)` pe header | singurul `backdrop-filter` din proiect | CSS custom pe container |
| `.whatsapp-float` + `@keyframes whatsapp-pulse` | poziționare fixă, puls 2,5s, etichetă cu `max-width` animat | CSS custom integral |
| `.skip-link` (`left:-9999px` → `left:8px` la focus) | z-index 100, deasupra drawer-ului (60) și header-ului (50) | CSS custom integral |
| `html { scroll-padding-top: 64px / 80px }` | calibrat pe înălțimea header-ului | CSS custom, *Site Settings → Custom CSS* |
| `inert` pe drawer + `overflow-hidden` pe `<body>` | comportament de accesibilitate al meniului | JS custom |
| `translate-x-full` → `none`, 300ms | tranziția de intrare/ieșire a drawer-ului | CSS/JS custom |
| `min-h-[44px]` pe 9 linkuri (logo header, logo footer, e-mail, telefon, ANPC, SAL, 2 documente legale) | ținte de tap | Min Height per element |
