# TOKENS.md — extragere de design tokens

Extragere mecanică a culorilor, tipografiei și spațierii din prototipul static,
ca intrare pentru **Global Colors** și **Global Fonts** din Elementor Site Settings.

Data extragerii: **2026-09-08**. Toate cifrele sunt obținute prin script, pe
codul din repo. Nicio valoare nu este estimată sau rotunjită.

---

## STARE GIT

| | |
|---|---|
| Branch activ | `main` |
| Working tree la start | curat (`nothing to commit, working tree clean`) |
| Commit-uri nepushate la start | **niciunul** — `git rev-list --left-right --count origin/main...HEAD` = `0 0` |
| HEAD la start | `18db472 docs: audit de pre-migrare înainte de Faza 3` |
| Remote | `origin` → `https://github.com/laur2198/ioana-balan` |

Singurul fișier scris de acest task este `TOKENS.md`. Niciun fișier existent
nu a fost modificat.

---

## METODĂ

### Fișiere scanate — lista exactă

| Fișier | Linii | Octeți |
|---|---|---|
| `index.html` | 586 | 57 420 |
| `oferte.html` | 535 | 49 682 |
| `termeni-si-conditii.html` | 534 | 45 212 |
| `faq.html` | 494 | 44 785 |
| `galerie.html` | 437 | 37 758 |
| `contact.html` | 418 | 36 474 |
| `discografie.html` | 422 | 35 845 |
| `politica-cookie.html` | 397 | 35 588 |
| `blog.html` | 357 | 30 134 |
| `despre.html` | 329 | 30 828 |
| `articol.html` | 308 | 28 099 |
| `assets/styles.css` | 762 | 24 805 |
| `assets/tailwind.config.js` | 97 | 3 863 |
| **Total** | **5 676** | **460 493** |

`assets/tailwind.config.js` este inclus pentru că **definește tokenii**
(`colors`, `fontSize`, `fontFamily`, `spacing`) fără de care o clasă
`text-headline-md` sau `bg-accent` nu poate fi tradusă într-o valoare.
Valorile din el sunt citite din fișier la fiecare rulare, nu hardcodate în script.

### Ce a fost exclus și de ce

| Exclus | Motiv |
|---|---|
| `node_modules/`, `_stitch-export/` | **nu există în repo** (verificat cu `ls`) |
| `assets/img/`, `assets/video-thumbs/`, `assets/fonts/` | fișiere binare; `assets/fonts/` este totuși inventariat la §2.6 |
| `assets/motifs.svg` | conform regulii 4 (doar `.html` din rădăcină + CSS propriu); conține 2 apariții de `#c6c6c6` care **nu** sunt numărate mai jos |
| `https://cdn.tailwindcss.com` | bibliotecă terță, încărcată la runtime |
| conținutul blocurilor `<script>` și `<style>` | exclus din analiza **de markup**; culorile scrise literal în JS **sunt** numărate, cu contextul `script/atribut` |
| **264 de blocuri de comentariu HTML** | excluse din analiza de markup; culorile din ele sunt numărate separat, cu contextul `comentariu`, ca să nu contamineze totalurile |
| clase cu variantă de stare (`hover:`, `group-hover:`, `focus:`, `first-letter:` …) | excluse din tabelele de dimensiune și spațiere, pentru că nu descriu starea de repaus. **27 din 733** de clase de spațiere au fost excluse pe acest criteriu. La culori sunt păstrate și marcate. |

### Cum au fost citite fișierele HTML

Fiecare pagină e parsată cu `html.parser` într-un **arbore DOM real**, nu cu
regex pe linii. Rezultatul: **2 777 de elemente** pe cele 11 pagini. Numărul
coincide element cu element cu o a doua extragere independentă, prin regex —
verificare încrucișată per fișier:

| Fișier | Regex | DOM |
|---|---|---|
| `articol.html` | 147 | 147 |
| `blog.html` | 182 | 182 |
| `contact.html` | 194 | 194 |
| `despre.html` | 167 | 167 |
| `discografie.html` | 221 | 221 |
| `faq.html` | 304 | 304 |
| `galerie.html` | 222 | 222 |
| `index.html` | 336 | 336 |
| `oferte.html` | 330 | 330 |
| `politica-cookie.html` | 272 | 272 |
| `termeni-si-conditii.html` | 402 | 402 |
| **Total** | **2 777** | **2 777** |

Arborele permite rezolvarea **moștenirii** (font-family, font-size, weight,
line-height, letter-spacing, culoare de text) și a **fundalului efectiv**
(strat peste strat, cu compozitare alpha) — necesare la §1.5 și §2.3.

### Echivalențe Tailwind → px folosite

**Scala implicită `fontSize` (Tailwind v3):**

| Clasă | font-size | line-height |
|---|---|---|
| `text-xs` | 12px | 16px |
| `text-sm` | 14px | 20px |
| `text-base` | 16px | 24px |
| `text-lg` | 18px | 28px |
| `text-xl` | 20px | 28px |
| `text-2xl` | 24px | 32px |
| `text-3xl` | 30px | 36px |
| `text-4xl` | 36px | 40px |
| `text-5xl` | 48px | 1 |
| `text-6xl` | 60px | 1 |
| `text-7xl` | 72px | 1 |
| `text-8xl` | 96px | 1 |
| `text-9xl` | 128px | 1 |

**`fontWeight`:** `thin` 100 · `extralight` 200 · `light` 300 · `normal` 400 ·
`medium` 500 · `semibold` 600 · `bold` 700 · `extrabold` 800 · `black` 900

**`lineHeight`:** `none` 1 · `tight` 1.25 · `snug` 1.375 · `normal` 1.5 ·
`relaxed` 1.625 · `loose` 2 · `leading-3…10` = 12/16/20/24/28/32/36/40 px

**`letterSpacing`:** `tighter` −0.05em · `tight` −0.025em · `normal` 0em ·
`wide` 0.025em · `wider` 0.05em · `widest` 0.1em

**`spacing`** (padding, gap): `n` = n × 4px; `px` = 1px. Peste acestea,
`assets/tailwind.config.js` adaugă: `margin-desktop` 64px · `margin-mobile` 16px ·
`gutter` 24px · `unit` 8px · `max-width` 1200px.

**`maxWidth` implicit:** `xs` 320 · `sm` 384 · `md` 448 · `lg` 512 · `xl` 576 ·
`2xl` 672 · `3xl` 768 · `4xl` 896 · `5xl` 1024 · `6xl` 1152 · `7xl` 1280 px.

**`rem` → px:** 1rem = 16px (nicio regulă din repo nu schimbă `font-size` pe `html`).

**Tokenii proprii de `fontSize`** (din `assets/tailwind.config.js`) poartă și
`lineHeight`, `letterSpacing` și `fontWeight`. O clasă ca `md:text-headline-lg`
aplică **toate patru** proprietățile, dar numai de la breakpoint-ul `md` în sus.
Scriptul modelează asta: greutatea, line-height-ul și tracking-ul sunt urmărite
**per breakpoint**, exact ca dimensiunea.

| Token | font-size | line-height | letter-spacing | font-weight | Familie |
|---|---|---|---|---|---|
| `display-lg` | 48px | 56px | −0.02em | 500 | EB Garamond |
| `headline-lg` | 32px | 40px | — | 500 | EB Garamond |
| `headline-lg-mobile` | 28px | 36px | — | 500 | EB Garamond |
| `headline-md` | 24px | 32px | — | 500 | EB Garamond |
| `body-lg` | 18px | 28px | — | 400 | Inter |
| `body-md` | 16px | 24px | — | 400 | Inter |
| `label-md` | 14px | 20px | 0.05em | 600 | Inter |

### Valori de plecare pentru moștenire

- `assets/styles.css:161-168` → `body { background-color: #131313; color: #e5e2e1; font-family: 'Inter', sans-serif }`
- **`body` nu are `font-size` în CSS.** Acolo unde clasa de pe `<body>` nu îl
  setează, dimensiunea de bază este cea implicită a browserului, **16px**.
  Pe `articol`, `blog`, `discografie`, `index` clasa `text-body-md` de pe `<body>`
  fixează 16px **și** `line-height: 24px`, care se moștenește ca lungime fixă.
- `line-height` de plecare: `1.5` (Preflight, `html { line-height: 1.5 }`).
- Greutate de plecare: 400. Preflight resetează `h1`–`h6` la `font-weight: inherit`,
  deci un heading fără clasă de greutate rămâne la 400.

### Normalizare a culorilor

- `#RGB` → `#RRGGBB`, `#RGBA` → `#RRGGBBAA`, totul în **majuscule**.
  În repo **nu există** nicio valoare pe 8 caractere (`#RRGGBBAA`).
- `rgb()` / `rgba()` sunt păstrate ca atare, cu spațiile eliminate. **Nu** sunt
  colapsate în hex, pentru că alpha-ul e informație de token.
- Culorile sunt numărate pe **trei straturi**, ținute distinct în coloana „Strat":
  - **literal** — hex/rgb scris în clar în `assets/styles.css`, într-un
    atribut `style="…"` sau într-un șir din JS;
  - **TW arbitrar** — `bg-[#…]`, `text-[#…]`, `marker:text-[#…]` etc.;
  - **TW token** — utilitar cu nume rezolvat prin `tailwind.config.js`
    (`bg-accent` → `#A01028`), plus `white`/`black` din paleta implicită.
- Utilitarele scanate pentru culoare: `bg-` `text-` `border-` `from-` `via-`
  `to-` `ring-` `shadow-` `fill-` `stroke-` `decoration-` `divide-` `outline-`
  `accent-` `caret-` `placeholder-`, cu sau fără sufix de opacitate (`/10`, `/50`).
- `bg-transparent` / `to-transparent` (**22 apariții**) sunt raportate separat,
  nu ca valori de culoare.
- Umbrele implicite Tailwind (`shadow-lg`, `shadow-2xl`) folosesc negru cu alpha
  din bibliotecă, nu un token de proiect — **nu** sunt numărate.

---

## BLOC 1 — CULORI

### 1.1 / 1.2 — toate valorile, cu frecvență, fișiere și contexte

**49 de valori distincte**, **1 441 de apariții** pe 12 fișiere
(cele 11 `.html` + `assets/styles.css`).

Coloana „Contexte" numără proprietățile pe care apare valoarea.
`comentariu` = apariție într-un comentariu HTML sau CSS (nu se randează).
`script/atribut` = valoare scrisă într-un șir din JS sau într-un atribut
non-`style`.

| Valoare | Apariții | Fișiere | Contexte | Strat |
|---|---|---|---|---|
| `#C8C6C5` | **363** | 12 | text 321 · border 40 · background 2 | TW token 361 · literal 1 · TW arbitrar 1 |
| `#C4C7C7` | **351** | 12 | text 351 | TW token 349 · literal 2 |
| `#444748` | **115** | 11 | border 114 · background 1 | TW token 115 |
| `#C6C6C6` | **110** | 11 | text 110 | TW token 110 |
| `#E5E2E1` | **104** | 12 | text 104 | TW token 93 · literal 11 |
| `#FFFFFF` | **104** | 12 | text 90 · background 13 · fill/stroke 1 | TW token 99 · literal 5 |
| `#131313` | **54** | 12 | background 41 · gradient 12 · comentariu 1 | TW token 50 · literal 4 |
| `#A01028` | **42** | 12 | background 39 · comentariu 2 · text 1 | TW token 38 · literal 4 |
| `#1C1B1B` | **39** | 9 | background 39 | TW token 37 · literal 2 |
| `#8E9192` | **32** | 8 | text 17 · border 15 | TW token 32 |
| `#800020` | **30** | 12 | background 26 · border 2 · comentariu 2 | TW token 26 · literal 4 |
| `#20201F` | **16** | 5 | background 16 | TW token 14 · literal 2 |
| `#0E0E0E` | **13** | 11 | background 13 | TW token 13 |
| `#2A2A2A` | **10** | 3 | background 10 | TW token 10 |
| `#C41236` | **7** | 3 | border 3 · text 2 · comentariu 1 · variabilă CSS 1 | literal 5 · TW arbitrar 1 · TW token 1 |
| `#2F0004` | **5** | 1 | background 5 | TW token 5 |
| `rgba(0,0,0,0.3)` | **4** | 1 | shadow 4 | literal 4 |
| `rgba(142,145,146,0.15)` | **3** | 2 | border 2 · script/atribut 1 | literal 3 |
| `rgba(196,18,54,0.18)` | **3** | 1 | background 3 | literal 3 |
| `rgba(200,198,197,0.4)` | **3** | 3 | script/atribut 2 · border 1 | literal 3 |
| `rgba(19,19,19,0)` | **2** | 1 | gradient 2 | literal 2 |
| `rgba(227,226,222,0.15)` | **2** | 2 | border 1 · script/atribut 1 | literal 2 |
| `rgba(28,27,27,0.6)` | **2** | 1 | script/atribut 2 | literal 2 |
| `rgba(37,211,102,0)` | **2** | 1 | shadow 2 | literal 2 |
| `#0D0D0D` | **1** | 1 | background 1 | literal 1 |
| `#161615` | **1** | 1 | background 1 | literal 1 |
| `#25D366` | **1** | 1 | background 1 | literal 1 |
| `#353535` | **1** | 1 | background 1 | TW token 1 |
| `#FFB3B1` | **1** | 1 | text 1 | TW token 1 |
| `#FFB4AB` | **1** | 1 | text 1 | TW token 1 |
| `rgb(28,27,27)` | **1** | 1 | background 1 | literal 1 |
| `rgb(34,33,33)` | **1** | 1 | background 1 | literal 1 |
| `rgba(0,0,0,0.10)` | **1** | 1 | gradient 1 | literal 1 |
| `rgba(0,0,0,0.28)` | **1** | 1 | gradient 1 | literal 1 |
| `rgba(0,0,0,0.78)` | **1** | 1 | gradient 1 | literal 1 |
| `rgba(142,145,146,0.2)` | **1** | 1 | gradient 1 | literal 1 |
| `rgba(142,145,146,0.3)` | **1** | 1 | gradient 1 | literal 1 |
| `rgba(19,19,19,0.55)` | **1** | 1 | background 1 | literal 1 |
| `rgba(196,18,54,0.14)` | **1** | 1 | background 1 | literal 1 |
| `rgba(196,18,54,0.75)` | **1** | 1 | text 1 | literal 1 |
| `rgba(198,198,198,0.18)` | **1** | 1 | border 1 | literal 1 |
| `rgba(198,198,198,0.2)` | **1** | 1 | border 1 | literal 1 |
| `rgba(198,198,198,0.28)` | **1** | 1 | text 1 | literal 1 |
| `rgba(200,198,197,0.08)` | **1** | 1 | script/atribut 1 | literal 1 |
| `rgba(255,255,255,0.8)` | **1** | 1 | text 1 | literal 1 |
| `rgba(255,255,255,0.85)` | **1** | 1 | border 1 | literal 1 |
| `rgba(28,27,27,0.85)` | **1** | 1 | background 1 | literal 1 |
| `rgba(37,211,102,0.45)` | **1** | 1 | shadow 1 | literal 1 |
| `rgba(68,71,72,0.2)` | **1** | 1 | border 1 | literal 1 |
| **TOTAL** | **1441** | | | |

**Cuvinte-cheie de culoare, raportate separat:** `transparent` — **22 apariții**
(20 pe `background`, 2 în `gradient`). Nicio apariție de `currentColor` ca
utilitar (SVG-urile folosesc atributul `fill="currentColor"`, care moștenește
culoarea de text și e deja numărat prin `text-*`).

### 1.3 — culori cu mai puțin de 5 apariții, fiecare cu fișier și linie

Culori cu **mai puțin de 5 apariții**: **33** valori distincte, 46 apariții în total.

| Valoare | N | Fișier:linie | Context | Cod (40 car.) |
|---|---|---|---|---|
| `rgba(0,0,0,0.3)` | 4 | `assets/styles.css:386` | shadow | `box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3` |
|  |  | `assets/styles.css:402` | shadow | `0%   { box-shadow: 0 4px 12px rgba(0, 0,` |
|  |  | `assets/styles.css:403` | shadow | `70%  { box-shadow: 0 4px 12px rgba(0, 0,` |
|  |  | `assets/styles.css:404` | shadow | `100% { box-shadow: 0 4px 12px rgba(0, 0,` |
| `rgba(142,145,146,0.15)` | 3 | `assets/styles.css:187` | border | `border: 1px solid rgba(142, 145, 146, 0.` |
|  |  | `assets/styles.css:196` | border | `border: 1px solid rgba(142, 145, 146, 0.` |
|  |  | `index.html:523` | script/atribut | `item.style.borderColor = 'rgba(142, 145,` |
| `rgba(196,18,54,0.18)` | 3 | `assets/styles.css:280` | background | `background-color: rgba(196, 18, 54, 0.18` |
|  |  | `assets/styles.css:551` | background | `background-color: rgba(196, 18, 54, 0.18` |
|  |  | `assets/styles.css:578` | background | `background-color: rgba(196, 18, 54, 0.18` |
| `rgba(200,198,197,0.4)` | 3 | `assets/styles.css:191` | border | `border-color: rgba(200, 198, 197, 0.4);` |
|  |  | `blog.html:342` | script/atribut | `card.style.borderColor = 'rgba(200, 198,` |
|  |  | `index.html:518` | script/atribut | `item.style.borderColor = 'rgba(200, 198,` |
| `rgba(19,19,19,0)` | 2 | `assets/styles.css:306` | gradient | `background-image: linear-gradient(to top` |
|  |  | `assets/styles.css:310` | gradient | `background-image: linear-gradient(to rig` |
| `rgba(227,226,222,0.15)` | 2 | `assets/styles.css:202` | border | `border: 1px solid rgba(227, 226, 222, 0.` |
|  |  | `blog.html:345` | script/atribut | `card.style.borderColor = 'rgba(227, 226,` |
| `rgba(28,27,27,0.6)` | 2 | `articol.html:294` | script/atribut | `card.style.background = `radial-gradient` |
|  |  | `articol.html:297` | script/atribut | `card.style.background = `rgba(28, 27, 27` |
| `rgba(37,211,102,0)` | 2 | `assets/styles.css:403` | shadow | `70%  { box-shadow: 0 4px 12px rgba(0, 0,` |
|  |  | `assets/styles.css:404` | shadow | `100% { box-shadow: 0 4px 12px rgba(0, 0,` |
| `#0D0D0D` | 1 | `assets/styles.css:624` | background | `background: #0d0d0d;` |
| `#161615` | 1 | `assets/styles.css:514` | background | `background-color: #161615;` |
| `#25D366` | 1 | `assets/styles.css:383` | background | `background-color: #25d366;` |
| `#353535` | 1 | `index.html:177` | background · TW token | `<section class="py-16 md:py-24 bg-surfac` |
| `#FFB3B1` | 1 | `blog.html:54` | text · TW token | `<body class="font-body-md text-body-md s` |
| `#FFB4AB` | 1 | `contact.html:215` | text · TW token | `<p class="font-body-md text-[15px] text-` |
| `rgb(28,27,27)` | 1 | `assets/styles.css:186` | background | `background: rgb(28, 27, 27);` |
| `rgb(34,33,33)` | 1 | `assets/styles.css:192` | background | `background: rgb(34, 33, 33);` |
| `rgba(0,0,0,0.10)` | 1 | `assets/styles.css:662` | gradient | `rgba(0, 0, 0, 0.10) 100%` |
| `rgba(0,0,0,0.28)` | 1 | `assets/styles.css:661` | gradient | `rgba(0, 0, 0, 0.28) 42%,` |
| `rgba(0,0,0,0.78)` | 1 | `assets/styles.css:660` | gradient | `rgba(0, 0, 0, 0.78) 0%,` |
| `rgba(142,145,146,0.2)` | 1 | `assets/styles.css:213` | gradient | `background: linear-gradient(90deg, trans` |
| `rgba(142,145,146,0.3)` | 1 | `assets/styles.css:208` | gradient | `background: linear-gradient(90deg, trans` |
| `rgba(19,19,19,0.55)` | 1 | `assets/styles.css:678` | background | `background: rgba(19, 19, 19, 0.55);` |
| `rgba(196,18,54,0.14)` | 1 | `assets/styles.css:563` | background | `background-color: rgba(196, 18, 54, 0.14` |
| `rgba(196,18,54,0.75)` | 1 | `assets/styles.css:454` | text | `text-decoration-color: rgba(196, 18, 54,` |
| `rgba(198,198,198,0.18)` | 1 | `assets/styles.css:498` | border | `border: 1px solid rgba(198, 198, 198, 0.` |
| `rgba(198,198,198,0.2)` | 1 | `assets/styles.css:199` | border | `border: 1px solid rgba(198, 198, 198, 0.` |
| `rgba(198,198,198,0.28)` | 1 | `assets/styles.css:233` | text | `color: rgba(198, 198, 198, 0.28);` |
| `rgba(200,198,197,0.08)` | 1 | `articol.html:294` | script/atribut | `card.style.background = `radial-gradient` |
| `rgba(255,255,255,0.8)` | 1 | `assets/styles.css:713` | text | `color: rgba(255, 255, 255, 0.8);` |
| `rgba(255,255,255,0.85)` | 1 | `assets/styles.css:676` | border | `border: 2px solid rgba(255, 255, 255, 0.` |
| `rgba(28,27,27,0.85)` | 1 | `assets/styles.css:195` | background | `background: rgba(28, 27, 27, 0.85);` |
| `rgba(37,211,102,0.45)` | 1 | `assets/styles.css:402` | shadow | `0%   { box-shadow: 0 4px 12px rgba(0, 0,` |
| `rgba(68,71,72,0.2)` | 1 | `assets/styles.css:625` | border | `border: 1px solid rgba(68, 71, 72, 0.2);` |

### 1.4 — verificare încrucișată cu CLAUDE.md §5

Blocul de tokeni din CLAUDE.md §5, reprodus verbatim:

```
--surface           #131313   fundal principal
--surface-container #1c1b1b   carduri, secțiuni alternante
--on-surface        #e5e2e1   text principal
--on-surface-var    #c6c6c6   text secundar
--outline           rgba(255,255,255,0.10)   borduri hairline
--accent            #800020   bordo — SINGURA culoare de accent
--accent-hover      #600018
```

plus lista „Eliminate complet": `#c95a5c`, `#690005`, `#4D0011`, `#c8c6c5`.

„Apariții vii" = fără cele din comentarii.

#### Declarate ca tokeni în CLAUDE.md §5

| Culoare | În CLAUDE.md | În cod (apariții vii / total cu comentarii) | Verdict |
|---|---|---|---|
| `#131313` | `--surface` — fundal principal | 53 / 54 | folosită |
| `#1C1B1B` | `--surface-container` — carduri, secțiuni alternante | 39 / 39 | folosită |
| `#E5E2E1` | `--on-surface` — text principal | 104 / 104 | folosită |
| `#C6C6C6` | `--on-surface-var` — text secundar | 110 / 110 | folosită |
| `rgba(255,255,255,0.10)` | `--outline` — borduri hairline | 0 / 0 | **declarată, nefolosită** |
| `#800020` | `--accent` — bordo — SINGURA culoare de accent | 28 / 30 | folosită |
| `#600018` | `--accent-hover` — hover accent | 0 / 0 | **declarată, nefolosită** |

#### Declarate ca „eliminate complet" în CLAUDE.md §5

| Culoare | În CLAUDE.md | În cod (apariții vii / total) | Verdict |
|---|---|---|---|
| `#C95A5C` | eliminată — coral, derivat din paleta de eroare | 0 / 0 | absentă, conform |
| `#690005` | eliminată — roșu, token de eroare folosit ca CTA | 0 / 0 | absentă, conform |
| `#4D0011` | eliminată — bordo hardcodat | 0 / 0 | absentă, conform |
| `#C8C6C5` | eliminată — argintiu ca fond de buton | 363 / 363 | **prezentă, contrar declarației** |

#### Folosite în cod, nedeclarate în CLAUDE.md §5

| Valoare | Apariții vii | Fișiere | Contexte |
|---|---|---|---|
| `#C4C7C7` | 351 | 12 | text 351 |
| `#444748` | 115 | 11 | border 114 · background 1 |
| `#FFFFFF` | 104 | 12 | text 90 · background 13 · fill/stroke 1 |
| `#A01028` | 40 | 12 | background 39 · text 1 |
| `#8E9192` | 32 | 8 | text 17 · border 15 |
| `#20201F` | 16 | 5 | background 16 |
| `#0E0E0E` | 13 | 11 | background 13 |
| `#2A2A2A` | 10 | 3 | background 10 |
| `#C41236` | 6 | 3 | border 3 · text 2 · variabilă CSS 1 |
| `#2F0004` | 5 | 1 | background 5 |
| `rgba(0,0,0,0.3)` | 4 | 1 | shadow 4 |
| `rgba(142,145,146,0.15)` | 3 | 2 | border 2 · script/atribut 1 |
| `rgba(196,18,54,0.18)` | 3 | 1 | background 3 |
| `rgba(200,198,197,0.4)` | 3 | 3 | script/atribut 2 · border 1 |
| `rgba(19,19,19,0)` | 2 | 1 | gradient 2 |
| `rgba(227,226,222,0.15)` | 2 | 2 | border 1 · script/atribut 1 |
| `rgba(28,27,27,0.6)` | 2 | 1 | script/atribut 2 |
| `rgba(37,211,102,0)` | 2 | 1 | shadow 2 |
| `#0D0D0D` | 1 | 1 | background 1 |
| `#161615` | 1 | 1 | background 1 |
| `#25D366` | 1 | 1 | background 1 |
| `#353535` | 1 | 1 | background 1 |
| `#FFB3B1` | 1 | 1 | text 1 |
| `#FFB4AB` | 1 | 1 | text 1 |
| `rgb(28,27,27)` | 1 | 1 | background 1 |
| `rgb(34,33,33)` | 1 | 1 | background 1 |
| `rgba(0,0,0,0.10)` | 1 | 1 | gradient 1 |
| `rgba(0,0,0,0.28)` | 1 | 1 | gradient 1 |
| `rgba(0,0,0,0.78)` | 1 | 1 | gradient 1 |
| `rgba(142,145,146,0.2)` | 1 | 1 | gradient 1 |
| `rgba(142,145,146,0.3)` | 1 | 1 | gradient 1 |
| `rgba(19,19,19,0.55)` | 1 | 1 | background 1 |
| `rgba(196,18,54,0.14)` | 1 | 1 | background 1 |
| `rgba(196,18,54,0.75)` | 1 | 1 | text 1 |
| `rgba(198,198,198,0.18)` | 1 | 1 | border 1 |
| `rgba(198,198,198,0.2)` | 1 | 1 | border 1 |
| `rgba(198,198,198,0.28)` | 1 | 1 | text 1 |
| `rgba(200,198,197,0.08)` | 1 | 1 | script/atribut 1 |
| `rgba(255,255,255,0.8)` | 1 | 1 | text 1 |
| `rgba(255,255,255,0.85)` | 1 | 1 | border 1 |
| `rgba(28,27,27,0.85)` | 1 | 1 | background 1 |
| `rgba(37,211,102,0.45)` | 1 | 1 | shadow 1 |
| `rgba(68,71,72,0.2)` | 1 | 1 | border 1 |

**Total valori nedeclarate: 43**, însumând **738** apariții vii.

#### Observații de corespondență (constatări, nu recomandări)

- `#C8C6C5` este declarat „eliminat **ca fond de buton**". Din cele 363 de
  apariții, repartiția pe contexte este: **text 321 · border 40 · background 2**.
  Cele două apariții pe fundal sunt `articol.html:112` (`<div class="h-[1px] w-12 bg-primary">`,
  o linie de 1px) și `index.html:369` (`<div class="absolute inset-0 bg-primary opacity-[0.03]">`,
  o textură la 3% opacitate). Niciuna nu este fond de buton. A treia apariție
  non-text este `assets/styles.css:342`, `outline: 2px solid #c8c6c5` (inel de focus).
- `--on-surface-var` este declarat `#c6c6c6` în CLAUDE.md. În
  `assets/tailwind.config.js` există **două** tokene distincte cu rol similar:
  `on-surface-variant` = `#C4C7C7` (351 apariții) și `secondary` /
  `secondary-fixed-dim` = `#C6C6C6` (110 apariții).
- `rgba(255,255,255,0.10)` (`--outline`) și `#600018` (`--accent-hover`) au
  **0 apariții** în cod, în orice notație.
- Familia de accent efectiv implementată are patru valori, documentate în
  antetul lui `assets/tailwind.config.js` (liniile 6-8):
  `accent` `#A01028` · `accent-hover` `#800020` · `accent-deep` `#800020` ·
  `accent-edge` `#C41236`.


### 1.5 — raport de contrast WCAG, pe perechile efectiv folosite

**Metodă.** Fundalul **nu** este presupus. Pentru fiecare nod cu text propriu,
scriptul urcă pe arborele DOM până la primul strămoș cu fundal, compozitează
straturile semitransparente unul peste altul și se oprește la `body`
(`#131313`, `assets/styles.css:162`). Prim-planul se rezolvă la fel, prin
moștenire, pornind de la `color: #e5e2e1` (`assets/styles.css:163`).
Clasele `opacity-*` de pe nod și de pe strămoși se înmulțesc și se aplică
prim-planului înainte de calcul.

Praguri WCAG 2.1 AA: **4.5:1** pentru text normal, **3.0:1** pentru text mare
(≥ 24px, sau ≥ 18.66px la weight ≥ 700). Coloana „px"/"weight" e valoarea la
breakpoint-ul de bază.

Coloana „Ascuns de la citire" = nodul sau un strămoș are `aria-hidden="true"`
sau clasa `sr-only`.


#### Toate perechile prim-plan / fundal efectiv, pe noduri cu text propriu

| Prim-plan | Fundal | Raport | AA normal (≥4.5) | AA large (≥3.0) | px | weight | Ascuns de la citire | N | Exemple |
|---|---|---|---|---|---|---|---|---|---|
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 16 | 400 | nu | 285 | `articol.html:49` · `blog.html:55` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 24 | 500 | nu | 78 | `articol.html:89` · `articol.html:90` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 14 | 600 | nu | 77 | `articol.html:58` · `articol.html:59` |
| `#E5E2E1` | `#1C1B1B` | **13.34:1** | ✅ | ✅ | 16 | 400 | nu | 67 | `faq.html:152` · `faq.html:170` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 16 | 400 | nu | 53 | `articol.html:123` · `articol.html:132` |
| `#C4C7C7` | `#0E0E0E` | **11.34:1** | ✅ | ✅ | 16 | 400 | nu | 45 | `articol.html:200` · `articol.html:201` |
| `#C6C6C6` | `#0E0E0E` | **11.30:1** | ✅ | ✅ | 12 | 400 | nu | 44 | `articol.html:238` · `articol.html:240` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 24 | 400 | nu | 36 | `despre.html:171` · `discografie.html:141` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 14 | 600 | nu | 34 | `articol.html:63` · `articol.html:113` |
| `#FFFFFF` | `#A01028` | **8.08:1** | ✅ | ✅ | 14 | 600 | nu | 24 | `articol.html:67` · `articol.html:156` |
| `#6A6A6A` | `#0E0E0E` | **3.57:1** | ❌ | ✅ | 12 | 400 | da | 22 | `articol.html:239` · `articol.html:241` |
| `#C6C6C6` | `#0E0E0E` | **11.30:1** | ✅ | ✅ | 13 | 400 | nu | 22 | `articol.html:216` · `articol.html:218` |
| `#C6C6C6` | `#1C1B1B` | **10.06:1** | ✅ | ✅ | 16 | 400 | nu | 21 | `contact.html:173` · `contact.html:177` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 20 | 400 | nu | 19 | `index.html:379` · `oferte.html:147` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 16 | 400 | da | 15 | `politica-cookie.html:171` · `politica-cookie.html:173` |
| `#C6C6C6` | `#131313` | **10.88:1** | ✅ | ✅ | 16 | 400 | nu | 13 | `contact.html:117` · `contact.html:139` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 12 | 400 | nu | 12 | `articol.html:306` · `blog.html:355` |
| `#696A6A` | `#0E0E0E` | **3.56:1** | ❌ | ✅ | 16 | 400 | da | 11 | `articol.html:205` · `blog.html:259` |
| `#6A6A6A` | `#0E0E0E` | **3.57:1** | ❌ | ✅ | 13 | 400 | da | 11 | `articol.html:217` · `blog.html:271` |
| `#A0A2A2` | `#0E0E0E` | **7.52:1** | ✅ | ✅ | 16 | 400 | nu | 11 | `articol.html:170` · `blog.html:224` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 24 | 500 | nu | 11 | `articol.html:95` · `articol.html:122` |
| `#FFFFFF` | `#A01028` | **8.08:1** | ✅ | ✅ | 24 | 500 | nu | 11 | `articol.html:97` · `blog.html:103` |
| `#C8C6C5` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 14 | 600 | nu | 10 | `blog.html:135` · `blog.html:151` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 14 | 600 | nu | 10 | `articol.html:157` · `contact.html:130` |
| `#8E9192` | `#131313` | **5.85:1** | ✅ | ✅ | 14 | 600 | nu | 9 | `articol.html:106` · `discografie.html:149` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 30 | 400 | nu | 9 | `despre.html:118` · `faq.html:130` |
| `#505252` | `#131313` | **2.36:1** | ❌ | ❌ | 14 | 600 | nu | 8 | `discografie.html:146` · `discografie.html:155` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 12 | 400 | nu | 8 | `oferte.html:149` · `oferte.html:167` |
| `#E5E2E1` | `#1C1B1B` | **13.34:1** | ✅ | ✅ | 24 | 500 | nu | 8 | `blog.html:132` · `blog.html:148` |
| `#C4C7C7` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 16 | 400 | nu | 6 | `blog.html:133` · `blog.html:149` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 11 | 400 | nu | 5 | `blog.html:205` · `blog.html:206` |
| `#E5E2E1` | `#1C1B1B` | **13.34:1** | ✅ | ✅ | 28 | 400 | nu | 5 | `despre.html:187` · `index.html:148` |
| `#C8C6C5` | `#2F0004` | **10.99:1** | ✅ | ✅ | 10 | 400 | nu | 4 | `blog.html:128` · `blog.html:144` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 28 | 400 | nu | 4 | `discografie.html:223` · `index.html:214` |
| `#C6C6C6` | `#353535` | **7.18:1** | ✅ | ✅ | 16 | 400 | nu | 3 | `index.html:183` · `index.html:189` |
| `#C8C6C5` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 16 | 400 | nu | 3 | `index.html:156` · `index.html:162` |
| `#E5E2E1` | `#1C1B1B` | **13.34:1** | ✅ | ✅ | 14 | 600 | nu | 3 | `despre.html:191` · `discografie.html:269` |
| `#929393` | `#1C1B1B` | **5.58:1** | ✅ | ✅ | 16 | 400 | nu | 2 | `contact.html:198` · `contact.html:202` |
| `#A2A2A2` | `#131313` | **7.28:1** | ✅ | ✅ | 16 | 400 | nu | 2 | `galerie.html:99` · `galerie.html:244` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 18 | 400 | nu | 2 | `blog.html:114` · `oferte.html:130` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 16 | 400 | da | 2 | `politica-cookie.html:106` · `termeni-si-conditii.html:107` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 14 | 400 | nu | 2 | `politica-cookie.html:157` · `termeni-si-conditii.html:262` |
| `#C6C6C6` | `#131313` | **10.88:1** | ✅ | ✅ | 12 | 400 | nu | 2 | `index.html:221` · `index.html:225` |
| `#C6C6C6` | `#20201F` | **9.55:1** | ✅ | ✅ | 11 | 400 | nu | 2 | `oferte.html:145` · `oferte.html:215` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 30 | 400 | nu | 2 | `galerie.html:98` · `galerie.html:243` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 28 | 400 | nu | 2 | `index.html:220` · `index.html:224` |
| `#C8C6C5` | `#0E0E0E` | **11.34:1** | ✅ | ✅ | 14 | 600 | nu | 2 | `index.html:323` · `index.html:363` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 48 | 500 | nu | 2 | `articol.html:108` · `articol.html:153` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 32 | 500 | nu | 2 | `articol.html:131` · `articol.html:143` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 26 | 400 | nu | 2 | `despre.html:163` · `faq.html:343` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 36 | 400 | nu | 2 | `discografie.html:125` · `index.html:121` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 16 | 600 | nu | 2 | `politica-cookie.html:106` · `termeni-si-conditii.html:107` |
| `#FFFFFF` | `#800020` | **10.83:1** | ✅ | ✅ | 11 | 400 | nu | 2 | `oferte.html:175` · `oferte.html:242` |
| `#FFFFFF` | `#131313` | **18.58:1** | ✅ | ✅ | 14 | 600 | nu | 2 | `politica-cookie.html:98` · `termeni-si-conditii.html:99` |
| `#C4C7C7` | `#20201F` | **9.58:1** | ✅ | ✅ | 16 | 400 | nu | 1 | `blog.html:194` |
| `#C4C7C7` | `#2A2A2A` | **8.44:1** | ✅ | ✅ | 16 | 400 | nu | 1 | `contact.html:122` |
| `#C4C7C7` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 15 | 400 | nu | 1 | `contact.html:213` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 13 | 400 | nu | 1 | `oferte.html:205` |
| `#C4C7C7` | `#131313` | **10.92:1** | ✅ | ✅ | 15 | 400 | nu | 1 | `termeni-si-conditii.html:388` |
| `#C6C6C6` | `#131313` | **10.88:1** | ✅ | ✅ | 18 | 400 | nu | 1 | `discografie.html:126` |
| `#C6C6C6` | `#131313` | **10.88:1** | ✅ | ✅ | 14 | 400 | nu | 1 | `galerie.html:256` |
| `#C8C6C5` | `#2A2A2A` | **8.43:1** | ✅ | ✅ | 14 | 600 | nu | 1 | `articol.html:105` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 28 | 500 | nu | 1 | `contact.html:116` |
| `#C8C6C5` | `#2A2A2A` | **8.43:1** | ✅ | ✅ | 16 | 400 | nu | 1 | `contact.html:121` |
| `#C8C6C5` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 24 | 500 | nu | 1 | `contact.html:169` |
| `#C8C6C5` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 15 | 400 | nu | 1 | `contact.html:213` |
| `#C8C6C5` | `#131313` | **10.92:1** | ✅ | ✅ | 12 | 400 | nu | 1 | `index.html:120` |
| `#C8C6C5` | `#1C1B1B` | **10.10:1** | ✅ | ✅ | 12 | 400 | nu | 1 | `index.html:147` |
| `#C8C6C5` | `#353535` | **7.21:1** | ✅ | ✅ | 12 | 400 | nu | 1 | `index.html:181` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 18 | 400 | nu | 1 | `articol.html:128` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 24 | 500 | nu | 1 | `articol.html:136` |
| `#E5E2E1` | `#131313` | **14.42:1** | ✅ | ✅ | 32 | 400 | nu | 1 | `blog.html:113` |
| `#E5E2E1` | `#20201F` | **12.66:1** | ✅ | ✅ | 24 | 500 | nu | 1 | `blog.html:193` |
| `#E5E2E1` | `#20201F` | **12.66:1** | ✅ | ✅ | 16 | 400 | da | 1 | `blog.html:196` |
| `#E5E2E1` | `#0E0E0E` | **14.98:1** | ✅ | ✅ | 24 | 400 | nu | 1 | `despre.html:150` |
| `#E5E2E1` | `#1C1B1B` | **13.34:1** | ✅ | ✅ | 26 | 400 | nu | 1 | `discografie.html:264` |
| `#E5E2E1` | `#353535` | **9.52:1** | ✅ | ✅ | 32 | 400 | nu | 1 | `index.html:182` |
| `#E5E2E1` | `#0E0E0E` | **14.98:1** | ✅ | ✅ | 28 | 400 | nu | 1 | `index.html:324` |
| `#FFB4AB` | `#1C1B1B` | **10.12:1** | ✅ | ✅ | 15 | 400 | nu | 1 | `contact.html:215` |

**Total noduri de text analizate: 1076**

#### Elemente `<button>` / `<a>` cu fundal propriu (CTA)

| Prim-plan | Fundal | Raport | AA normal (≥4.5) | AA large (≥3.0) | px | weight | Ascuns de la citire | N | Exemple |
|---|---|---|---|---|---|---|---|---|---|
| `#FFFFFF` | `#A01028` | **8.08:1** | ✅ | ✅ | 14 | 600 | nu | 24 | `articol.html:67` · `articol.html:156` |
| `#FFFFFF` | `#A01028` | **8.08:1** | ✅ | ✅ | 24 | 500 | nu | 11 | `articol.html:97` · `blog.html:103` |

**Total noduri de text analizate: 35**

**Perechile care nu ating 4.5:1 — detaliu:**

| Prim-plan | Fundal | Raport | Cauza compozitării | Exemple | N |
|---|---|---|---|---|---|
| `#6A6A6A` pe `#0E0E0E` | 3.57:1 | `text-secondary` (`#C6C6C6`) × `opacity-50` peste `bg-surface-container-lowest` | separatorul `·` din footer, `aria-hidden="true"` | `articol.html:239`, `articol.html:241`, `blog.html:293` | 22 (12px) + 11 (13px) |
| `#696A6A` pe `#0E0E0E` | 3.56:1 | `text-on-surface-variant` (`#C4C7C7`) × `opacity-50` peste `bg-surface-container-lowest` | separatorul `·` din footer, `aria-hidden="true"` | `articol.html:205`, `blog.html:259`, `contact.html:274` | 11 |
| `#505252` pe `#131313` | **2.36:1** | `text-outline/50` — token `outline` `#8E9192` la 50% peste `body` | **numerele de piesă „01"–„08"**, text vizibil, fără `aria-hidden` | `discografie.html:146`, `:155`, `:164`, `:173`, `:182`, `:191`, `:200`, `:209` | 8 |

Primele două grupuri (44 de noduri) sunt separatoare `·` marcate
`aria-hidden="true"`. Al treilea grup (8 noduri) este text citibil.

---

## BLOC 2 — TIPOGRAFIE

### 2.1 — dimensiuni de font, pe cele trei surse, ținute separat

#### (a) Valori arbitrare — `text-[Npx]` / `text-[Nrem]`

| Clasă | px | Apariții | Fișiere |
|---|---|---|---|
| `text-[12px]` | 12 | 80 | toate 11 |
| `text-[16px]` | 16 | 37 | `discografie.html`, `faq.html`, `index.html`, `oferte.html` |
| `text-[24px]` | 24 | 33 | `discografie.html`, `faq.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-[20px]` | 20 | 13 | `index.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-[28px]` | 28 | 12 | `despre.html`, `discografie.html`, `index.html`, `oferte.html` |
| `text-[13px]` | 13 | 12 | toate 11 |
| `text-[11px]` | 11 | 9 | `blog.html`, `oferte.html` |
| `text-[18px]` | 18 | 8 | `galerie.html`, `index.html`, `oferte.html` |
| `text-[36px]` | 36 | 5 | `despre.html`, `discografie.html`, `index.html` |
| `text-[10px]` | 10 | 4 | `blog.html` |
| `text-[30px]` | 30 | 3 | `faq.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-[26px]` | 26 | 3 | `despre.html`, `discografie.html`, `faq.html` |
| `text-[15px]` | 15 | 3 | `contact.html`, `termeni-si-conditii.html` |
| `text-[56px]` | 56 | 2 | `blog.html`, `index.html` |
| `text-[48px]` | 48 | 2 | `blog.html`, `index.html` |
| `text-[32px]` | 32 | 2 | `blog.html`, `index.html` |
| `text-[14px]` | 14 | 2 | `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-[120px]` | 120 | 1 | `discografie.html` |
| `text-[80px]` | 80 | 1 | `discografie.html` |
| **TOTAL** | | **232** | 19 valori distincte |

#### (b) Clase Tailwind implicite (scala default `fontSize`)

| Clasă | px (echivalență declarată) | line-height implicit | Apariții | Fișiere |
|---|---|---|---|---|
| `text-3xl` | 30 | 36px | 19 | toate 11 |
| `text-4xl` | 36 | 40px | 18 | toate 11 |
| `text-base` | 16 | 24px | 16 | `contact.html`, `despre.html`, `faq.html`, `oferte.html` |
| `text-xl` | 20 | 28px | 9 | `index.html`, `oferte.html` |
| `text-2xl` | 24 | 32px | 8 | `despre.html`, `oferte.html` |
| `text-5xl` | 48 | 1 | 1 | `articol.html` |
| `text-lg` | 18 | 28px | 1 | `oferte.html` |
| `text-sm` | 14 | 20px | 1 | `galerie.html` |
| **TOTAL** | | | **73** | 8 clase distincte |

#### (b-bis) Tokeni proprii din `assets/tailwind.config.js` (`fontSize` extins)

| Clasă | px | line-height | letter-spacing | font-weight | Apariții | Fișiere |
|---|---|---|---|---|---|---|
| `text-label-md` | 14px | 20px | 0.05em | 600 | 197 | toate 11 |
| `text-headline-md` | 24px | 32px | — | 500 | 151 | toate 11 |
| `text-body-md` | 16px | 24px | — | 400 | 120 | toate 11 |
| `text-headline-lg` | 32px | 40px | — | 500 | 48 | `articol.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-body-lg` | 18px | 28px | — | 400 | 28 | `articol.html`, `blog.html`, `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html` |
| `text-display-lg` | 48px | 56px | -0.02em | 500 | 16 | `articol.html`, `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `text-headline-lg-mobile` | 28px | 36px | — | 500 | 1 | `contact.html` |
| **TOTAL** | | | | | **561** | 7 tokeni distincți |

#### (c) CSS propriu — `font-size` în `assets/styles.css`

| Linie | Valoare | px echivalent | Selector |
|---|---|---|---|
| `assets/styles.css:287` | `11px` | 11 | `.price-tbc__flag` |
| `assets/styles.css:332` | `16px` | 16 | `.skip-link` |
| `assets/styles.css:426` | `16px` | 16 | `.legal-prose ol` |
| `assets/styles.css:435` | `17px` | 17 | `.legal-prose ol` |
| `assets/styles.css:465` | `0.92em` | relativ la părinte | `.legal-prose code` |
| `assets/styles.css:489` | `16px` | 16 | `.legal-table` |
| `assets/styles.css:505` | `14px` | 14 | `.legal-table thead th` |
| `assets/styles.css:586` | `11px` | 11 | `.answer-tbc__flag` |
| `assets/styles.css:706` | `0.625rem` | 10 | `.video-card__eyebrow` |
| `assets/styles.css:719` | `1.125rem` | 18 | `.video-card__title` |
| `assets/styles.css:728` | `1.375rem` | 22 | `.video-card__title` |
| **TOTAL** | | | **11 declarații** |

**Recapitulare pe surse:** tokeni proprii **561** · arbitrare **232** ·
clase implicite **73** · CSS propriu **11 declarații**.

Valori px care apar **exclusiv** prin CSS propriu, niciodată prin clasă:
**17px** (`assets/styles.css:435`) și **22px** (`assets/styles.css:728`).
Valoarea `0.92em` (`assets/styles.css:465`, `.legal-prose code`) este relativă
și **NEDETERMINABILĂ în px** fără contextul de randare — părintele are 16px la
bază și 17px de la 768px în sus, deci ar da 14,72px / 15,64px, dar asta
presupune că `code` nu e imbricat în alt element cu font-size propriu.

### 2.2 — distribuția completă a dimensiunilor

O „apariție" = o dimensiune aplicată efectiv unui element, la un breakpoint.
`text-[28px] md:text-headline-lg` produce două apariții: 28 la bază, 32 la `md`.
Sunt numărate **numai** clasele de pe element, nu și valorile moștenite.
Sursa `variantă de stare` = dimensiune activă doar într-o pseudo-stare
(`first-letter:text-5xl`).

| Dimensiune (px) | Apariții | Sursă | Pe ce elemente |
|---|---|---|---|
| **14** | 200 | token config 197 · arbitrar 2 · clasă implicită 1 | `a` 127 · `span` 56 · `p` 8 · `figcaption` 3 · `button` 2 · `summary` 2 · `h2` 1 · `h3` 1 |
| **24** | 192 | token config 151 · arbitrar 33 · clasă implicită 8 | `a` 99 · `h3` 46 · `h2` 41 · `span` 5 · `p` 1 |
| **16** | 172 | token config 119 · arbitrar 37 · clasă implicită 16 | `li` 46 · `p` 44 · `a` 25 · `h3` 25 · `span` 12 · `label` 6 · `body` 4 · `input` 4 · `blockquote` 3 · `figcaption` 1 · `select` 1 · `textarea` 1 |
| **12** | 80 | arbitrar 80 | `span` 46 · `p` 33 · `a` 1 |
| **32** | 50 | token config 48 · arbitrar 2 | `h2` 47 · `h3` 2 · `h1` 1 |
| **18** | 37 | token config 28 · arbitrar 8 · clasă implicită 1 | `p` 20 · `span` 9 · `svg` 8 |
| **36** | 23 | clasă implicită 18 · arbitrar 5 | `svg` 14 · `span` 6 · `h1` 2 · `blockquote` 1 |
| **30** | 22 | clasă implicită 19 · arbitrar 3 | `svg` 11 · `h1` 6 · `span` 4 · `h2` 1 |
| **20** | 22 | arbitrar 13 · clasă implicită 9 | `h3` 14 · `span` 5 · `svg` 3 |
| **48** | 19 | token config 16 · arbitrar 2 · variantă de stare 1 | `h1` 11 · `h2` 7 · `p` 1 |
| **28** | 13 | arbitrar 12 · token config 1 | `h2` 10 · `span` 2 · `h1` 1 |
| **13** | 12 | arbitrar 12 | `p` 12 |
| **11** | 9 | arbitrar 9 | `span` 9 |
| **10** | 4 | arbitrar 4 | `span` 4 |
| **26** | 3 | arbitrar 3 | `h2` 2 · `blockquote` 1 |
| **15** | 3 | arbitrar 3 | `p` 2 · `label` 1 |
| **56** | 2 | arbitrar 2 | `h1` 2 |
| **120** | 1 | arbitrar 1 | `svg` 1 |
| **80** | 1 | arbitrar 1 | `svg` 1 |
| **TOTAL** | **865** | | |

**19 valori distincte** din markup, plus **17px** și **22px** din CSS propriu →
**21 de dimensiuni distincte** în total (`0.92em` neinclusă, fiind relativă).

### 2.3 — grupare pe rol semantic

Valorile sunt cele **efective**, după moștenire pe arborele DOM. Notația
`a → b (md)` înseamnă: `a` de la bază, `b` de la breakpoint-ul `md` în sus.
Un `font-weight` de forma `400 → 500 (md)` apare când tokenul de dimensiune
este aplicat doar la `md:` — tokenul poartă și greutatea, deci sub `md`
elementul rămâne la greutatea moștenită.


#### `<h1>` — 11 apariții, 7 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| EB Garamond | 30 → 48 (md) | 400 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 5 | `despre.html:118` · `faq.html:130` |
| EB Garamond | 28 → 48 (md) | 500 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 1 | `contact.html:116` |
| EB Garamond | 30 → 48 (md) | 400 → 500 (md) | 1.5 → 56px (md) | -0.02em (md) | — | 1 | `galerie.html:98` |
| EB Garamond | 32 → 48 (md) → 56 (lg) | 400 | 1.1 | — | — | 1 | `blog.html:113` |
| EB Garamond | 36 → 48 (md) → 56 (lg) | 400 | 1.05 | -0.01em | — | 1 | `index.html:121` |
| EB Garamond | 36 → 48 (sm) | 400 → 500 (sm) | 1.25 → 56px (sm) | -0.02em (sm) | — | 1 | `discografie.html:125` |
| EB Garamond | 48 | 500 | 1.25 | -0.02em | — | 1 | `articol.html:108` |

#### `<h2>` — 59 apariții, 17 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| EB Garamond | 24 → 32 (md) | 400 → 500 (md) | 1.25 → 40px (md) | — | — | 30 | `faq.html:146` · `faq.html:161` |
| EB Garamond | 24 | 500 | 32px | — | — | 5 | `blog.html:132` · `blog.html:148` |
| EB Garamond | 28 → 32 (md) | 400 → 500 (md) | 24px → 40px (md) | — | — | 5 | `index.html:148` · `index.html:214` |
| EB Garamond | 24 → 32 (md) | 400 → 500 (md) | 1.5 → 40px (md) | — | — | 4 | `despre.html:150` · `despre.html:171` |
| EB Garamond | 28 → 48 (md) | 400 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 2 | `despre.html:187` · `oferte.html:359` |
| EB Garamond | 32 | 500 | 40px | — | — | 2 | `articol.html:131` · `articol.html:143` |
| Inter | 14 | 600 | 20px | 0.2em | UPPERCASE | 1 | `oferte.html:124` |
| EB Garamond | 24 → 32 (md) | 500 → 500 (md) | 32px → 40px (md) | — | — | 1 | `galerie.html:109` |
| EB Garamond | 24 → 32 (sm) | 400 → 500 (sm) | 24px → 40px (sm) | — | — | 1 | `discografie.html:141` |
| EB Garamond | 26 → 32 (md) | 400 → 500 (md) | 24px → 40px (md) | — | — | 1 | `discografie.html:264` |
| EB Garamond | 26 → 48 (md) | 400 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 1 | `faq.html:343` |
| EB Garamond | 28 → 32 (md) | 400 → 500 (md) | 1.5 → 40px (md) | — | — | 1 | `oferte.html:297` |
| EB Garamond | 28 → 32 (sm) | 400 → 500 (sm) | 24px → 40px (sm) | — | — | 1 | `discografie.html:223` |
| EB Garamond | 28 → 48 (md) | 400 → 500 (md) | 24px → 56px (md) | -0.02em (md) | — | 1 | `index.html:372` |
| EB Garamond | 30 → 48 (md) | 400 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 1 | `galerie.html:243` |
| EB Garamond | 32 → 48 (md) | 400 → 500 (md) | 1.25 → 56px (md) | -0.02em (md) | — | 1 | `index.html:182` |
| EB Garamond | 48 | 500 | 56px | -0.02em | — | 1 | `articol.html:153` |

#### `<h3>` — 47 apariții, 5 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| EB Garamond | 16 → 24 (md) | 400 → 500 (md) | 1.375 → 32px (md) | — | — | 25 | `faq.html:152` · `faq.html:170` |
| EB Garamond | 20 → 24 (md) | 400 → 500 (md) | 1.5 → 32px (md) | — | — | 14 | `oferte.html:147` · `oferte.html:177` |
| EB Garamond | 24 | 500 | 32px | — | — | 5 | `articol.html:122` · `blog.html:193` |
| EB Garamond | 24 → 32 (sm) | 400 → 500 (sm) | 24px → 40px (sm) | — | — | 2 | `discografie.html:233` · `discografie.html:248` |
| Inter | 14 | 600 | 20px | 0.1em | UPPERCASE | 1 | `blog.html:203` |

#### `<h4>` — **0 apariții: niciun element de acest tip în repo**

#### `<h5>` — **0 apariții: niciun element de acest tip în repo**

#### `<h6>` — **0 apariții: niciun element de acest tip în repo**

#### `<p>` — 191 apariții, 19 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 1.5 | — | — | 75 | `politica-cookie.html:132` · `politica-cookie.html:133` |
| Inter | 16 | 400 | 24px | — | — | 32 | `articol.html:123` · `articol.html:154` |
| Inter | 12 | 400 | 1.5 | — | — | 21 | `contact.html:307` · `contact.html:309` |
| Inter | 12 | 400 | 24px | — | — | 12 | `articol.html:238` · `articol.html:240` |
| Inter | 13 | 400 | 1.5 | — | — | 8 | `contact.html:284` · `despre.html:251` |
| Inter | 16 | 400 | 1.625 | — | — | 8 | `articol.html:132` · `articol.html:140` |
| Inter | 16 → 18 (md) | 400 → 400 (md) | 24px → 28px (md) | — | — | 7 | `contact.html:117` · `discografie.html:265` |
| Inter | 16 → 18 (md) | 400 → 400 (md) | 1.625 → 28px (md) | — | — | 6 | `despre.html:127` · `despre.html:128` |
| Inter | 13 | 400 | 24px | — | — | 4 | `articol.html:215` · `blog.html:269` |
| Inter | 16 → 18 (md) | 400 → 400 (md) | 1.5 → 28px (md) | — | — | 4 | `despre.html:188` · `faq.html:344` |
| Inter | 18 | 400 | 28px | — | — | 3 | `articol.html:128` · `blog.html:114` |
| Inter | 14 | 600 | 20px | 0.1em | UPPERCASE | 2 | `articol.html:113` · `contact.html:156` |
| Inter | 14 | 600 | 20px | 0.18em | UPPERCASE | 2 | `politica-cookie.html:98` · `termeni-si-conditii.html:99` |
| Inter | 14 | 400 | 1.5 | — | — | 2 | `politica-cookie.html:157` · `termeni-si-conditii.html:262` |
| Inter | 14 | 600 | 20px | 0.05em | — | 1 | `galerie.html:255` |
| Inter | 14 | 400 | 24px | — | — | 1 | `galerie.html:256` |
| Inter | 15 | 400 | 1.5 | — | — | 1 | `contact.html:215` |
| Inter | 15 → 16 (md) | 400 → 400 (md) | 1.625 → 24px (md) | — | — | 1 | `termeni-si-conditii.html:388` |
| EB Garamond | 24 | 500 | 32px | — | — | 1 | `articol.html:136` |

#### `<li>` — 166 apariții, 2 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 1.5 | — | — | 94 | `contact.html:242` · `contact.html:247` |
| Inter | 16 | 400 | 24px | — | — | 72 | `articol.html:173` · `articol.html:178` |

#### `<a>` — 455 apariții, 12 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 1.5 | — | — | 106 | `contact.html:53` · `contact.html:58` |
| EB Garamond | 24 | 500 | 32px | — | UPPERCASE | 99 | `articol.html:89` · `articol.html:90` |
| Inter | 16 | 400 | 24px | — | — | 86 | `articol.html:49` · `articol.html:54` |
| Inter | 14 | 600 | 20px | 0.05em | UPPERCASE | 79 | `articol.html:58` · `articol.html:59` |
| Inter | 14 | 600 | 20px | 0.1em | UPPERCASE | 47 | `articol.html:67` · `articol.html:156` |
| Inter | 13 | 400 | 1.5 | — | — | 14 | `contact.html:285` · `contact.html:287` |
| Inter | 13 | 400 | 24px | — | — | 8 | `articol.html:216` · `articol.html:218` |
| Inter | 12 | 400 | 1.5 | — | — | 7 | `contact.html:309` · `despre.html:276` |
| Inter | 12 | 400 | 24px | — | — | 4 | `articol.html:240` · `blog.html:294` |
| Inter | 16 | 400 | 24px | 0.1em | UPPERCASE | 3 | `index.html:156` · `index.html:162` |
| Inter | 12 → 14 (md) | 400 → 600 (md) | 24px → 20px (md) | 0.1em → 0.05em (md) | UPPERCASE | 1 | `index.html:382` |
| Inter | 15 | 400 | 1.625 | — | — | 1 | `contact.html:213` |

#### `<button>` — 31 apariții, 4 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 1.5 | — | — | 19 | `contact.html:77` · `contact.html:88` |
| Inter | 16 | 400 | 24px | — | — | 10 | `articol.html:73` · `articol.html:84` |
| Inter | 14 | 600 | 20px | 0.1em | UPPERCASE | 1 | `blog.html:198` |
| Inter | 14 | 600 | 20px | 0.2em | UPPERCASE | 1 | `contact.html:220` |

#### `<label>` — 8 apariții, 2 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 24px | — | — | 7 | `blog.html:196` · `contact.html:173` |
| Inter | 15 | 400 | 1.625 | — | — | 1 | `contact.html:213` |

#### `<small>` — **0 apariții: niciun element de acest tip în repo**

#### `<blockquote>` — 6 apariții, 3 combinații distincte

| font-family | font-size (px) | font-weight | line-height | letter-spacing | Alte | N | Exemple (fișier:linie) |
|---|---|---|---|---|---|---|---|
| Inter | 16 | 400 | 24px | — | — | 3 | `index.html:286` · `index.html:297` |
| Inter | 16 | 400 | 1.5 | — | — | 2 | `politica-cookie.html:180` · `politica-cookie.html:186` |
| EB Garamond | 26 → 36 (md) | 400 | 1.3 → 1.25 (md) | — | — | 1 | `despre.html:163` |

### 2.4 — variație responsive

Tabelul listează **elementele care își declară propria dimensiune** (705 din
2 777); cele care doar moștenesc nu apar. „—" = niciun override la acel
breakpoint (valoarea rămâne cea de la breakpoint-ul anterior).

| Element | Bază | sm | md | lg | xl | 2xl | N | Fișiere |
|---|---|---|---|---|---|---|---|---|
| `a` | 24 | — | — | — | — | — | 99 | toate 11 |
| `a` | 16 | — | — | — | — | — | 25 | `politica-cookie.html`, `termeni-si-conditii.html` |
| `a` | 14 | — | — | — | — | — | 126 | toate 11 |
| `a` | 12 | — | 14 | — | — | — | 1 | `index.html` |
| `blockquote` | 26 | — | 36 | — | — | — | 1 | `despre.html` |
| `blockquote` | 16 | — | — | — | — | — | 3 | `index.html` |
| `body` | 16 | — | — | — | — | — | 4 | `articol.html`, `blog.html`, `discografie.html`, `index.html` |
| `button` | 14 | — | — | — | — | — | 2 | `blog.html`, `contact.html` |
| `figcaption` | 16 | — | — | — | — | — | 1 | `oferte.html` |
| `figcaption` | 14 | — | — | — | — | — | 3 | `index.html` |
| `h1` | 48 | — | — | — | — | — | 1 | `articol.html` |
| `h1` | 36 | 48 | — | — | — | — | 1 | `discografie.html` |
| `h1` | 36 | — | 48 | 56 | — | — | 1 | `index.html` |
| `h1` | 32 | — | 48 | 56 | — | — | 1 | `blog.html` |
| `h1` | 30 | — | 48 | — | — | — | 6 | `despre.html`, `faq.html`, `galerie.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `h1` | 28 | — | 48 | — | — | — | 1 | `contact.html` |
| `h2` | 48 | — | — | — | — | — | 1 | `articol.html` |
| `h2` | 32 | — | — | — | — | — | 2 | `articol.html` |
| `h2` | 32 | — | 48 | — | — | — | 1 | `index.html` |
| `h2` | 30 | — | 48 | — | — | — | 1 | `galerie.html` |
| `h2` | 28 | — | 48 | — | — | — | 3 | `despre.html`, `index.html`, `oferte.html` |
| `h2` | 28 | 32 | — | — | — | — | 1 | `discografie.html` |
| `h2` | 28 | — | 32 | — | — | — | 6 | `index.html`, `oferte.html` |
| `h2` | 26 | — | 32 | — | — | — | 1 | `discografie.html` |
| `h2` | 26 | — | 48 | — | — | — | 1 | `faq.html` |
| `h2` | 24 | — | — | — | — | — | 5 | `blog.html`, `contact.html` |
| `h2` | 24 | — | 32 | — | — | — | 35 | `despre.html`, `faq.html`, `galerie.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `h2` | 24 | 32 | — | — | — | — | 1 | `discografie.html` |
| `h2` | 14 | — | — | — | — | — | 1 | `oferte.html` |
| `h3` | 24 | — | — | — | — | — | 5 | `articol.html`, `blog.html`, `index.html` |
| `h3` | 24 | 32 | — | — | — | — | 2 | `discografie.html` |
| `h3` | 20 | — | 24 | — | — | — | 14 | `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `h3` | 16 | — | 24 | — | — | — | 25 | `faq.html`, `index.html`, `oferte.html` |
| `h3` | 14 | — | — | — | — | — | 1 | `blog.html` |
| `input` | 16 | — | — | — | — | — | 4 | `contact.html` |
| `label` | 16 | — | — | — | — | — | 6 | `contact.html` |
| `label` | 15 | — | — | — | — | — | 1 | `contact.html` |
| `li` | 16 | — | — | — | — | — | 46 | `oferte.html` |
| `p` | 24 | — | — | — | — | — | 1 | `articol.html` |
| `p` | 18 | — | — | — | — | — | 3 | `articol.html`, `blog.html`, `discografie.html` |
| `p` | 16 | — | — | — | — | — | 26 | toate 11 |
| `p` | 16 | — | 18 | — | — | — | 17 | `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html` |
| `p` | 15 | — | — | — | — | — | 1 | `contact.html` |
| `p` | 15 | — | 16 | — | — | — | 1 | `termeni-si-conditii.html` |
| `p` | 14 | — | — | — | — | — | 8 | `articol.html`, `contact.html`, `galerie.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `p` | 13 | — | — | — | — | — | 12 | toate 11 |
| `p` | 12 | — | — | — | — | — | 33 | toate 11 |
| `select` | 16 | — | — | — | — | — | 1 | `contact.html` |
| `span` | 30 | — | 36 | — | — | — | 4 | `oferte.html` |
| `span` | 28 | — | 36 | — | — | — | 2 | `index.html` |
| `span` | 20 | — | 24 | — | — | — | 5 | `index.html`, `oferte.html` |
| `span` | 18 | — | — | — | — | — | 1 | `oferte.html` |
| `span` | 16 | — | — | — | — | — | 4 | `contact.html`, `index.html` |
| `span` | 16 | 18 | — | — | — | — | 8 | `discografie.html` |
| `span` | 14 | — | — | — | — | — | 40 | toate 11 |
| `span` | 12 | — | — | — | — | — | 30 | toate 11 |
| `span` | 12 | — | 14 | — | — | — | 16 | toate 11 |
| `span` | 11 | — | — | — | — | — | 9 | `blog.html`, `oferte.html` |
| `span` | 10 | — | — | — | — | — | 4 | `blog.html` |
| `summary` | 14 | — | — | — | — | — | 2 | `politica-cookie.html`, `termeni-si-conditii.html` |
| `svg` | 80 | 120 | — | — | — | — | 1 | `discografie.html` |
| `svg` | 36 | — | — | — | — | — | 14 | toate 11 |
| `svg` | 30 | — | — | — | — | — | 11 | toate 11 |
| `svg` | 20 | — | — | — | — | — | 3 | `index.html` |
| `svg` | 18 | — | — | — | — | — | 8 | `galerie.html`, `index.html`, `oferte.html` |
| `textarea` | 16 | — | — | — | — | — | 1 | `contact.html` |
| **TOTAL** | | | | | | | **705** | 66 combinații |

### 2.4b — dimensiune de bază > 32px, fără nicio variantă responsive

| Fișier:linie | Element | Bază (px) | Clase | Text |
|---|---|---|---|---|
| `articol.html:85` | `svg` | **36** | `text-4xl` | — |
| `articol.html:108` | `h1` | **48** | `font-display-lg text-display-lg text-on-surface mb-8 max-w-4xl l` | Importanța luminilor de scenă pentru show- |
| `articol.html:153` | `h2` | **48** | `font-display-lg text-display-lg text-on-surface mb-4` | Plănuiți un eveniment? |
| `blog.html:91` | `svg` | **36** | `text-4xl` | — |
| `contact.html:89` | `svg` | **36** | `text-4xl` | — |
| `despre.html:81` | `svg` | **36** | `text-4xl` | — |
| `discografie.html:95` | `svg` | **36** | `text-4xl` | — |
| `faq.html:109` | `svg` | **36** | `text-4xl` | — |
| `galerie.html:78` | `svg` | **36** | `text-4xl` | — |
| `index.html:92` | `svg` | **36** | `text-4xl` | — |
| `index.html:153` | `svg` | **36** | `text-primary text-4xl mb-6 md:mb-4 lg:mb-6` | — |
| `index.html:159` | `svg` | **36** | `text-primary text-4xl mb-6 md:mb-4 lg:mb-6` | — |
| `index.html:165` | `svg` | **36** | `text-primary text-4xl mb-6 md:mb-4 lg:mb-6` | — |
| `oferte.html:89` | `svg` | **36** | `text-4xl` | — |
| `politica-cookie.html:70` | `svg` | **36** | `text-4xl` | — |
| `termeni-si-conditii.html:71` | `svg` | **36** | `text-4xl` | — |

**Total: 16**

Cele 14 elemente `svg` de 36px sunt iconul de meniu hamburger (`text-4xl`),
prezent pe toate cele 11 pagini, plus 3 iconuri de card pe `index.html`.
Elementele de **text** din această categorie sunt două: `articol.html:108`
(`h1`) și `articol.html:153` (`h2`), ambele la 48px fix, fără variantă
responsive — singura pagină pe care `text-display-lg` e folosit fără o
dimensiune de bază mai mică.

### 2.5 — inversiuni de ierarhie

Dimensiunile sunt cele efective la fiecare breakpoint. O aceeași pereche
raportată la mai multe breakpoint-uri înseamnă că relația se menține pe toate.

### 2.5a — `h2` cu dimensiune ≥ dimensiunea `h1` din aceeași pagină

| Fișier | h2 linie | Text h2 | h2 px | h1 linie | h1 px | Breakpoint | Relație |
|---|---|---|---|---|---|---|---|
| `articol.html` | 153 | Plănuiți un eveniment? | **48** | 108 | 48 | `base` | = |
| `articol.html` | 153 | Plănuiți un eveniment? | **48** | 108 | 48 | `sm` | = |
| `articol.html` | 153 | Plănuiți un eveniment? | **48** | 108 | 48 | `md` | = |
| `articol.html` | 153 | Plănuiți un eveniment? | **48** | 108 | 48 | `lg` | = |
| `despre.html` | 187 | Hai să ne cunoaștem | **48** | 118 | 48 | `md` | = |
| `despre.html` | 187 | Hai să ne cunoaștem | **48** | 118 | 48 | `lg` | = |
| `faq.html` | 343 | Nu ați găsit răspunsul? | **48** | 130 | 48 | `md` | = |
| `faq.html` | 343 | Nu ați găsit răspunsul? | **48** | 130 | 48 | `lg` | = |
| `galerie.html` | 243 | Esența Tradiției în Imagini. | **30** | 98 | 30 | `base` | = |
| `galerie.html` | 243 | Esența Tradiției în Imagini. | **30** | 98 | 30 | `sm` | = |
| `galerie.html` | 243 | Esența Tradiției în Imagini. | **48** | 98 | 48 | `md` | = |
| `galerie.html` | 243 | Esența Tradiției în Imagini. | **48** | 98 | 48 | `lg` | = |
| `index.html` | 182 | Pachete pentru 2026–2027 | **48** | 121 | 48 | `md` | = |
| `index.html` | 372 | Rezervă Formație Nuntă | **48** | 121 | 48 | `md` | = |
| `oferte.html` | 359 | Verificați dacă data este liberă | **48** | 115 | 48 | `md` | = |
| `oferte.html` | 359 | Verificați dacă data este liberă | **48** | 115 | 48 | `lg` | = |

**Total apariții: 16**

### 2.5b — `h3` cu dimensiune ≥ `h2` din aceeași secțiune

_Secțiune = intervalul dintre un `h2` și următorul `h2` din același fișier._

| Fișier | h3 linie | Text h3 | h3 px | h2 secțiunii (linie) | h2 px | Breakpoint | Relație |
|---|---|---|---|---|---|---|---|
| `blog.html` | 193 | Primește Noutăți | **24** | 180 | 24 | `base` | = |
| `blog.html` | 193 | Primește Noutăți | **24** | 180 | 24 | `sm` | = |
| `blog.html` | 193 | Primește Noutăți | **24** | 180 | 24 | `md` | = |
| `blog.html` | 193 | Primește Noutăți | **24** | 180 | 24 | `lg` | = |
| `discografie.html` | 233 | Glasul Inimii | **32** | 223 | 32 | `sm` | = |
| `discografie.html` | 233 | Glasul Inimii | **32** | 223 | 32 | `md` | = |
| `discografie.html` | 233 | Glasul Inimii | **32** | 223 | 32 | `lg` | = |
| `discografie.html` | 248 | Rădăcini | **32** | 223 | 32 | `sm` | = |
| `discografie.html` | 248 | Rădăcini | **32** | 223 | 32 | `md` | = |
| `discografie.html` | 248 | Rădăcini | **32** | 223 | 32 | `lg` | = |

**Total apariții: 10**

### 2.5c — `h2` cu dimensiune mai mică decât un `h3` din aceeași secțiune

| Fișier | h2 linie | Text h2 | h2 px | h3 linie | Text h3 | h3 px | Breakpoint |
|---|---|---|---|---|---|---|---|

**Total apariții: 0**

### 2.5d — heading sub 16px

| Fișier:linie | Tag | px | Breakpoint | Clase | Text |
|---|---|---|---|---|---|
| `blog.html:203` | `h3` | **14** | `base` | `font-label-md text-label-md uppercase tracking-widest text` | Tag-uri SEO |
| `blog.html:203` | `h3` | **14** | `sm` | `font-label-md text-label-md uppercase tracking-widest text` | Tag-uri SEO |
| `blog.html:203` | `h3` | **14** | `md` | `font-label-md text-label-md uppercase tracking-widest text` | Tag-uri SEO |
| `blog.html:203` | `h3` | **14** | `lg` | `font-label-md text-label-md uppercase tracking-widest text` | Tag-uri SEO |
| `oferte.html:124` | `h2` | **14** | `base` | `font-label-md text-label-md text-primary uppercase trackin` | Condiții comerciale |
| `oferte.html:124` | `h2` | **14** | `sm` | `font-label-md text-label-md text-primary uppercase trackin` | Condiții comerciale |
| `oferte.html:124` | `h2` | **14** | `md` | `font-label-md text-label-md text-primary uppercase trackin` | Condiții comerciale |
| `oferte.html:124` | `h2` | **14** | `lg` | `font-label-md text-label-md text-primary uppercase trackin` | Condiții comerciale |

**Total apariții: 8**

#### 2.5c-bis — `h2` mai mic decât un `h3` de oriunde din **aceeași pagină**

Definiția strictă de la 2.5c („aceeași secțiune") dă 0 rezultate, pentru că
`oferte.html:124` este urmat imediat de un alt `h2` (linia 139) înainte de
orice `h3`. Relaxând criteriul la nivel de pagină:

| Fișier | h2 (linie) | Text h2 | h2 px | h3 (linie) | Text h3 | h3 px | Breakpoint-uri |
|---|---|---|---|---|---|---|---|
| `discografie.html` | 264 | Îți place ce auzi? Rezervă data ta. | **26** | 233 | Glasul Inimii | 32 | `sm` |
| `discografie.html` | 264 | Îți place ce auzi? Rezervă data ta. | **26** | 248 | Rădăcini | 32 | `sm` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 147 | Pachet Standard | 20 / 20 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 177 | Pachet Premium | 20 / 20 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 217 | Pachet Standard | 20 / 20 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 244 | Pachet Premium | 20 / 20 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 304 | Prețul unei formații pentru 2026-2027? | 16 / 16 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 316 | Cum rezerv data — avans și contract? | 16 / 16 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 325 | Cât este avansul și când se achită restul? | 16 / 16 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 334 | Cu cât timp înainte ar trebui să vă contac | 16 / 16 / 24 / 24 | `base`, `sm`, `md`, `lg` |
| `oferte.html` | 124 | Condiții comerciale | **14 / 14 / 14 / 14** | 343 | Ce se întâmplă dacă trebuie să amân evenim | 16 / 16 / 24 / 24 | `base`, `sm`, `md`, `lg` |

**Total perechi h2/h3 distincte: 11**

#### Anexă 2.5 — toate heading-urile din repo, în ordinea documentului

**117 de heading-uri** pe 11 pagini: 11 × `h1`, 59 × `h2`, 47 × `h3`,
0 × `h4`/`h5`/`h6`. Valorile sunt cele efective, după moștenire.


| Fișier | Linie | Tag | Bază | sm | md | lg | Text |
|---|---|---|---|---|---|---|---|
| `articol.html` | 108 | `h1` | 48 | 48 | 48 | 48 | Importanța luminilor de scenă pentru show-ul formați |
| `articol.html` | 122 | `h3` | 24 | 24 | 24 | 24 | "Lumina nu doar luminează, ea transformă spațiul înt |
| `articol.html` | 131 | `h2` | 32 | 32 | 32 | 32 | Atmosfera și Dinamica Vizuală |
| `articol.html` | 143 | `h2` | 32 | 32 | 32 | 32 | Profesionalismul din Spatele pupitrului |
| `articol.html` | 153 | `h2` | 48 | 48 | 48 | 48 | Plănuiți un eveniment? |
| `blog.html` | 113 | `h1` | 32 | 32 | 48 | 56 | Sfaturi și Inspirație pentru Evenimente Memorabile |
| `blog.html` | 132 | `h2` | 24 | 24 | 24 | 24 | Cum să alegi formația de nuntă perfectă în 2026 |
| `blog.html` | 148 | `h2` | 24 | 24 | 24 | 24 | Muzica populară vs. Muzica ușoară la botez |
| `blog.html` | 164 | `h2` | 24 | 24 | 24 | 24 | Repertoriul de muzica populara nunta: Tendințe actua |
| `blog.html` | 180 | `h2` | 24 | 24 | 24 | 24 | Cum transformi un eveniment privat într-un spectacol |
| `blog.html` | 193 | `h3` | 24 | 24 | 24 | 24 | Primește Noutăți |
| `blog.html` | 203 | `h3` | 14 | 14 | 14 | 14 | Tag-uri SEO |
| `contact.html` | 116 | `h1` | 28 | 28 | 48 | 48 | Rezervări și Contact Ioana Balan |
| `contact.html` | 169 | `h2` | 24 | 24 | 24 | 24 | Cere ofertă personalizată |
| `despre.html` | 118 | `h1` | 30 | 30 | 48 | 48 | Despre mine |
| `despre.html` | 150 | `h2` | 24 | 24 | 32 | 32 | Rădăcini |
| `despre.html` | 171 | `h2` | 24 | 24 | 32 | 32 | Primii pași |
| `despre.html` | 187 | `h2` | 28 | 28 | 48 | 48 | Hai să ne cunoaștem |
| `discografie.html` | 125 | `h1` | 36 | 48 | 48 | 48 | Hai să nu ne mai mințim |
| `discografie.html` | 141 | `h2` | 24 | 32 | 32 | 32 | Melodii noi Ioana Balan |
| `discografie.html` | 223 | `h2` | 28 | 32 | 32 | 32 | Arhiva Sonoră Ioana Balan |
| `discografie.html` | 233 | `h3` | 24 | 32 | 32 | 32 | Glasul Inimii |
| `discografie.html` | 248 | `h3` | 24 | 32 | 32 | 32 | Rădăcini |
| `discografie.html` | 264 | `h2` | 26 | 26 | 32 | 32 | Îți place ce auzi? Rezervă data ta. |
| `faq.html` | 130 | `h1` | 30 | 30 | 48 | 48 | Ce ne întrebați cel mai des |
| `faq.html` | 146 | `h2` | 24 | 24 | 32 | 32 | Preț |
| `faq.html` | 152 | `h3` | 16 | 16 | 24 | 24 | Prețul unei formații pentru 2026-2027? |
| `faq.html` | 161 | `h2` | 24 | 24 | 32 | 32 | Rezervare și contract |
| `faq.html` | 170 | `h3` | 16 | 16 | 24 | 24 | Cum rezerv data — avans și contract? |
| `faq.html` | 179 | `h3` | 16 | 16 | 24 | 24 | Cât este avansul și când se achită restul? |
| `faq.html` | 188 | `h3` | 16 | 16 | 24 | 24 | Ce se întâmplă dacă trebuie să amân evenimentul? |
| `faq.html` | 197 | `h3` | 16 | 16 | 24 | 24 | Cu cât timp înainte ar trebui să vă contactez? |
| `faq.html` | 206 | `h2` | 24 | 24 | 32 | 32 | Prestația |
| `faq.html` | 212 | `h3` | 16 | 16 | 24 | 24 | Ce tipuri de evenimente acoperă Ioana Balan? |
| `faq.html` | 224 | `h3` | 16 | 16 | 24 | 24 | Cât durează programul? |
| `faq.html` | 233 | `h3` | 16 | 16 | 24 | 24 | Pot cere o piesă anume pentru un moment special? |
| `faq.html` | 242 | `h3` | 16 | 16 | 24 | 24 | Cântați și muzică ușoară, sau doar populară? |
| `faq.html` | 254 | `h3` | 16 | 16 | 24 | 24 | Ce se întâmplă în pauzele formației? |
| `faq.html` | 263 | `h2` | 24 | 24 | 32 | 32 | Tehnic și locație |
| `faq.html` | 269 | `h3` | 16 | 16 | 24 | 24 | Ce echipament aduceți și ce trebuie să asigure locaț |
| `faq.html` | 278 | `h3` | 16 | 16 | 24 | 24 | De cât spațiu aveți nevoie pentru scenă? |
| `faq.html` | 287 | `h3` | 16 | 16 | 24 | 24 | Cântați și la evenimente în aer liber? |
| `faq.html` | 296 | `h3` | 16 | 16 | 24 | 24 | Aveți nevoie de masă pentru formație? |
| `faq.html` | 305 | `h2` | 24 | 24 | 32 | 32 | Deplasare |
| `faq.html` | 314 | `h3` | 16 | 16 | 24 | 24 | Cântați și în afara Bucureștiului? |
| `faq.html` | 323 | `h3` | 16 | 16 | 24 | 24 | Cum se calculează costul deplasării? |
| `faq.html` | 332 | `h3` | 16 | 16 | 24 | 24 | Ce se întâmplă la distanțe mari, unde e nevoie de ca |
| `faq.html` | 343 | `h2` | 26 | 26 | 48 | 48 | Nu ați găsit răspunsul? |
| `galerie.html` | 98 | `h1` | 30 | 30 | 48 | 48 | Galerie de Spectacole |
| `galerie.html` | 109 | `h2` | 24 | 24 | 32 | 32 | Cum arată un eveniment |
| `galerie.html` | 243 | `h2` | 30 | 30 | 48 | 48 | Esența Tradiției în Imagini. |
| `index.html` | 121 | `h1` | 36 | 36 | 48 | 56 | Formație Nuntă București Premium: Muzică de Petrecer |
| `index.html` | 148 | `h2` | 28 | 28 | 32 | 32 | Muzică pentru nuntă, botez și corporate |
| `index.html` | 154 | `h3` | 24 | 24 | 24 | 24 | Muzică Nuntă |
| `index.html` | 160 | `h3` | 24 | 24 | 24 | 24 | Muzică Botez |
| `index.html` | 166 | `h3` | 24 | 24 | 24 | 24 | Corporate |
| `index.html` | 182 | `h2` | 32 | 32 | 48 | 48 | Pachete pentru 2026–2027 |
| `index.html` | 214 | `h2` | 28 | 28 | 32 | 32 | Peste 15 ani pe scenă |
| `index.html` | 238 | `h2` | 28 | 28 | 32 | 32 | Vezi cum arată un eveniment |
| `index.html` | 273 | `h2` | 28 | 28 | 32 | 32 | Ce Spun Mirii și Gazdele |
| `index.html` | 324 | `h2` | 28 | 28 | 32 | 32 | Ce ne întrebați cel mai des |
| `index.html` | 331 | `h3` | 16 | 16 | 24 | 24 | Prețul unei formații pentru 2026-2027? |
| `index.html` | 343 | `h3` | 16 | 16 | 24 | 24 | Cântați și în afara Bucureștiului? |
| `index.html` | 355 | `h3` | 16 | 16 | 24 | 24 | Cum rezerv data — avans și contract? |
| `index.html` | 372 | `h2` | 28 | 28 | 48 | 48 | Rezervă Formație Nuntă |
| `oferte.html` | 115 | `h1` | 30 | 30 | 48 | 48 | Pachete și prețuri pentru nuntă și botez |
| `oferte.html` | 124 | `h2` | 14 | 14 | 14 | 14 | Condiții comerciale |
| `oferte.html` | 139 | `h2` | 24 | 24 | 32 | 32 | Patru pachete, pentru nuntă și pentru botez |
| `oferte.html` | 147 | `h3` | 20 | 20 | 24 | 24 | Pachet Standard |
| `oferte.html` | 177 | `h3` | 20 | 20 | 24 | 24 | Pachet Premium |
| `oferte.html` | 217 | `h3` | 20 | 20 | 24 | 24 | Pachet Standard |
| `oferte.html` | 244 | `h3` | 20 | 20 | 24 | 24 | Pachet Premium |
| `oferte.html` | 285 | `h2` | 24 | 24 | 32 | 32 | Acoperire |
| `oferte.html` | 297 | `h2` | 28 | 28 | 32 | 32 | Preț, rezervare și contract |
| `oferte.html` | 304 | `h3` | 16 | 16 | 24 | 24 | Prețul unei formații pentru 2026-2027? |
| `oferte.html` | 316 | `h3` | 16 | 16 | 24 | 24 | Cum rezerv data — avans și contract? |
| `oferte.html` | 325 | `h3` | 16 | 16 | 24 | 24 | Cât este avansul și când se achită restul? |
| `oferte.html` | 334 | `h3` | 16 | 16 | 24 | 24 | Cu cât timp înainte ar trebui să vă contactez? |
| `oferte.html` | 343 | `h3` | 16 | 16 | 24 | 24 | Ce se întâmplă dacă trebuie să amân evenimentul? |
| `oferte.html` | 359 | `h2` | 28 | 28 | 48 | 48 | Verificați dacă data este liberă |
| `politica-cookie.html` | 105 | `h1` | 30 | 30 | 48 | 48 | Politica de cookie-uri |
| `politica-cookie.html` | 131 | `h2` | 24 | 24 | 32 | 32 | 1. Ce sunt cookie-urile |
| `politica-cookie.html` | 140 | `h2` | 24 | 24 | 32 | 32 | 2. Temeiul legal |
| `politica-cookie.html` | 153 | `h2` | 24 | 24 | 32 | 32 | 3. Ce cookie-uri folosim |
| `politica-cookie.html` | 155 | `h3` | 20 | 20 | 24 | 24 | 3.1 Cookie-uri strict necesare |
| `politica-cookie.html` | 184 | `h3` | 20 | 20 | 24 | 24 | 3.2 Cookie-uri de analiză |
| `politica-cookie.html` | 190 | `h3` | 20 | 20 | 24 | 24 | 3.3 Cookie-uri de publicitate |
| `politica-cookie.html` | 198 | `h2` | 24 | 24 | 32 | 32 | 4. Conținut încorporat de la terți |
| `politica-cookie.html` | 210 | `h2` | 24 | 24 | 32 | 32 | 5. Cum vă puteți retrage consimțământul |
| `politica-cookie.html` | 218 | `h2` | 24 | 24 | 32 | 32 | 6. Cum puteți controla cookie-urile din browser |
| `politica-cookie.html` | 233 | `h2` | 24 | 24 | 32 | 32 | 7. Drepturile dumneavoastră |
| `politica-cookie.html` | 242 | `h2` | 24 | 24 | 32 | 32 | 8. Modificarea acestei politici |
| `politica-cookie.html` | 249 | `h2` | 24 | 24 | 32 | 32 | 9. Contact |
| `termeni-si-conditii.html` | 106 | `h1` | 30 | 30 | 48 | 48 | Termeni și condiții |
| `termeni-si-conditii.html` | 139 | `h2` | 24 | 24 | 32 | 32 | 1. Identificarea operatorului |
| `termeni-si-conditii.html` | 156 | `h2` | 24 | 24 | 32 | 32 | 2. Obiectul site-ului |
| `termeni-si-conditii.html` | 164 | `h2` | 24 | 24 | 32 | 32 | 3. Acceptarea termenilor |
| `termeni-si-conditii.html` | 172 | `h2` | 24 | 24 | 32 | 32 | 4. Informațiile publicate. Prețuri |
| `termeni-si-conditii.html` | 188 | `h2` | 24 | 24 | 32 | 32 | 5. Rezervarea și încheierea contractului |
| `termeni-si-conditii.html` | 202 | `h2` | 24 | 24 | 32 | 32 | 6. Deplasarea |
| `termeni-si-conditii.html` | 211 | `h2` | 24 | 24 | 32 | 32 | 7. Modificarea și anularea rezervării |
| `termeni-si-conditii.html` | 219 | `h2` | 24 | 24 | 32 | 32 | 8. Drepturi de proprietate intelectuală |
| `termeni-si-conditii.html` | 229 | `h2` | 24 | 24 | 32 | 32 | 9. Materiale audio-video de la evenimente |
| `termeni-si-conditii.html` | 238 | `h2` | 24 | 24 | 32 | 32 | 10. Limitarea răspunderii |
| `termeni-si-conditii.html` | 247 | `h2` | 24 | 24 | 32 | 32 | 11. Linkuri către site-uri terțe |
| `termeni-si-conditii.html` | 255 | `h2` | 24 | 24 | 32 | 32 | 12. Prelucrarea datelor cu caracter personal |
| `termeni-si-conditii.html` | 258 | `h3` | 20 | 20 | 24 | 24 | 12.1 Operatorul |
| `termeni-si-conditii.html` | 261 | `h3` | 20 | 20 | 24 | 24 | 12.2 Ce date prelucrăm, în ce scop și în ce temei |
| `termeni-si-conditii.html` | 308 | `h3` | 20 | 20 | 24 | 24 | 12.3 Cui transmitem datele |
| `termeni-si-conditii.html` | 318 | `h3` | 20 | 20 | 24 | 24 | 12.4 Transferuri în afara Spațiului Economic Europea |
| `termeni-si-conditii.html` | 321 | `h3` | 20 | 20 | 24 | 24 | 12.5 Drepturile dumneavoastră |
| `termeni-si-conditii.html` | 336 | `h3` | 20 | 20 | 24 | 24 | 12.6 Dreptul de a depune plângere |
| `termeni-si-conditii.html` | 345 | `h3` | 20 | 20 | 24 | 24 | 12.7 Caracterul obligatoriu al furnizării datelor |
| `termeni-si-conditii.html` | 352 | `h2` | 24 | 24 | 32 | 32 | 13. Cookie-uri |
| `termeni-si-conditii.html` | 359 | `h2` | 24 | 24 | 32 | 32 | 14. Soluționarea litigiilor |
| `termeni-si-conditii.html` | 373 | `h2` | 24 | 24 | 32 | 32 | 15. Modificarea termenilor |
| `termeni-si-conditii.html` | 381 | `h2` | 24 | 24 | 32 | 32 | 16. Contact |

### 2.6 — fonturi

#### 2.6a — familii declarate prin clase `font-*`, apariții

| Clasă | Familie | Apariții | Fișiere |
|---|---|---|---|
| `font-body-md` | Inter | 273 | toate 11 |
| `font-label-md` | Inter | 227 | toate 11 |
| `font-headline-md` | EB Garamond | 152 | toate 11 |
| `font-headline-lg` | EB Garamond | 48 | `articol.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `font-display-lg` | EB Garamond | 30 | toate 11 |
| `font-body-lg` | Inter | 28 | `articol.html`, `blog.html`, `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html` |
| **TOTAL** | | **758** | |

#### 2.6b — familii efective pe elementele cu text (după moștenire)

| Familie | Noduri de text |
|---|---|
| Inter | 848 |
| EB Garamond | 228 |
| **TOTAL** | **1076** |

#### 2.6c — combinații familie × greutate × stil efectiv folosite

| Familie | Greutate | Stil | Apariții |
|---|---|---|---|
| EB Garamond | 400 | normal | 112 |
| EB Garamond | 500 | italic | 2 |
| EB Garamond | 500 | normal | 214 |
| Inter | 400 | italic | 3 |
| Inter | 400 | normal | 689 |
| Inter | 600 | normal | 199 |

#### 2.6d — fișiere de font prezente fizic în repo

| Fișier | Format | Familie | Weight | Style | KB | Referențiat în `@font-face` (linia) |
|---|---|---|---|---|---|---|
| `eb-garamond-400-latin-ext.woff2` | woff2 | EB Garamond | 400 | normal | 55.6 | da — `assets/styles.css:60` |
| `eb-garamond-400-latin.woff2` | woff2 | EB Garamond | 400 | normal | 23.3 | da — `assets/styles.css:51` |
| `eb-garamond-500-italic-latin-ext.woff2` | woff2 | EB Garamond | 500 | italic | 48.1 | da — `assets/styles.css:42` |
| `eb-garamond-500-italic-latin.woff2` | woff2 | EB Garamond | 500 | italic | 26.3 | da — `assets/styles.css:33` |
| `eb-garamond-500-latin-ext.woff2` | woff2 | EB Garamond | 500 | normal | 62.6 | da — `assets/styles.css:78` |
| `eb-garamond-500-latin.woff2` | woff2 | EB Garamond | 500 | normal | 24.7 | da — `assets/styles.css:69` |
| `inter-400-italic-latin-ext.woff2` | woff2 | Inter | 400 | italic | 36.7 | da — `assets/styles.css:96` |
| `inter-400-italic-latin.woff2` | woff2 | Inter | 400 | italic | 24.5 | da — `assets/styles.css:87` |
| `inter-400-latin-ext.woff2` | woff2 | Inter | 400 | normal | 34.2 | da — `assets/styles.css:114` |
| `inter-400-latin.woff2` | woff2 | Inter | 400 | normal | 23.1 | da — `assets/styles.css:105` |
| `inter-600-latin-ext.woff2` | woff2 | Inter | 600 | normal | 35.4 | da — `assets/styles.css:132` |
| `inter-600-latin.woff2` | woff2 | Inter | 600 | normal | 23.9 | da — `assets/styles.css:123` |
| **TOTAL 12 fișiere** | | | | | **418.3 KB** | 12 referențiate |

Fișiere `@font-face` care nu există pe disc: **niciunul**

Fișiere pe disc fără `@font-face`: **niciunul**

#### 2.6e — acoperire: greutăți folosite în cod vs. fișiere existente

| Familie | Greutate + stil folosite în cod | Există fișier | Subseturi |
|---|---|---|---|
| EB Garamond | 400 normal | da | `eb-garamond-400-latin.woff2`, `eb-garamond-400-latin-ext.woff2` |
| EB Garamond | 500 italic | da | `eb-garamond-500-italic-latin.woff2`, `eb-garamond-500-italic-latin-ext.woff2` |
| EB Garamond | 500 normal | da | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| Inter | 400 italic | da | `inter-400-italic-latin.woff2`, `inter-400-italic-latin-ext.woff2` |
| Inter | 400 normal | da | `inter-400-latin.woff2`, `inter-400-latin-ext.woff2` |
| Inter | 600 normal | da | `inter-600-latin.woff2`, `inter-600-latin-ext.woff2` |

**Fonturi încărcate dar nefolosite: niciunul.**
**Greutăți folosite în cod fără fișier corespondent: niciuna.**

Toate cele 12 fișiere sunt `woff2`; **nu există niciun `.woff`, `.ttf` sau
`.otf`** în repo. Fiecare familie × greutate × stil are două fișiere —
subseturile `latin` și `latin-ext` ale Google Fonts, cu `unicode-range`
identic cu al lor. Diacriticele românești `ă`, `ș`, `ț` sunt în `latin-ext`.

**Preîncărcare (`<link rel="preload">`), per pagină:**

| Pagină | Fișiere preîncărcate |
|---|---|
| `index.html` | `eb-garamond-400-latin.woff2`, `eb-garamond-400-latin-ext.woff2` |
| `blog.html` | `eb-garamond-400-latin.woff2`, `eb-garamond-400-latin-ext.woff2` |
| `articol.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `contact.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `discografie.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `faq.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `oferte.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `termeni-si-conditii.html` | `eb-garamond-500-latin.woff2`, `eb-garamond-500-latin-ext.woff2` |
| `despre.html` | `eb-garamond-500-latin.woff2` **(fără `-latin-ext`)** |
| `galerie.html` | `eb-garamond-500-latin.woff2` **(fără `-latin-ext`)** |
| `politica-cookie.html` | `eb-garamond-500-latin.woff2` **(fără `-latin-ext`)** |

Niciun fișier `Inter` nu este preîncărcat pe nicio pagină.

---

## BLOC 3 — SPAȚIERE ȘI LAYOUT

Scanate: **733 de clase** `py-*` / `pt-*` / `pb-*` / `max-w-*` / `gap-*` /
`gap-x-*` / `gap-y-*` pe cele 11 pagini. Din ele, **27** poartă o variantă de
stare și sunt excluse din tabelele de mai jos, pentru că descriu o tranziție,
nu geometria de repaus: `group-hover:max-w-xs` (11),
`group-focus-visible:max-w-xs` (11), `group-hover:gap-4` (5).

Rămân **706** clase de repaus, distribuite 278 + 106 + 322 în cele trei tabele
de mai jos. Nicio clasă nu a rămas netradusă.

Traducerea în px folosește scala Tailwind (`n` = n × 4px) plus tokenii proprii
de `spacing` din `assets/tailwind.config.js`.

### 3.1 — padding vertical (`py-*`, `pt-*`, `pb-*`)

| Proprietate | Valoare (px) | Breakpoint | Apariții | Fișiere |
|---|---|---|---|---|
| `py` | **16px** | — (bază) | 41 | toate 11 |
| `py` | **8px** | — (bază) | 37 | toate 11 |
| `pb` | **24px** | — (bază) | 25 | `faq.html`, `index.html`, `oferte.html` |
| `pb` | **4px** | — (bază) | 13 | `articol.html`, `blog.html`, `contact.html`, `despre.html`, `discografie.html`, `faq.html`, `galerie.html`, `oferte.html` |
| `py` | **32px** | — (bază) | 13 | toate 11 |
| `py` | **64px** | — (bază) | 13 | `despre.html`, `discografie.html`, `galerie.html`, `index.html`, `oferte.html` |
| `py` | **4px** | — (bază) | 12 | `articol.html`, `blog.html`, `contact.html` |
| `py` | **48px** | `md:` | 11 | toate 11 |
| `py` | **96px** | `md:` | 11 | `despre.html`, `discografie.html`, `galerie.html`, `index.html`, `oferte.html` |
| `py` | **12px** | — (bază) | 9 | `blog.html`, `contact.html`, `discografie.html`, `index.html` |
| `pb` | **64px** | — (bază) | 7 | `articol.html`, `blog.html`, `discografie.html`, `faq.html`, `galerie.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `pb` | **96px** | `md:` | 7 | `articol.html`, `blog.html`, `discografie.html`, `faq.html`, `galerie.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `pt` | **20px** | — (bază) | 6 | `oferte.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `py` | **20px** | `md:` | 6 | `despre.html`, `faq.html`, `oferte.html` |
| `py` | **8px** | `md:` | 6 | `contact.html` |
| `pt` | **128px** | — (bază) | 5 | `articol.html`, `blog.html`, `contact.html`, `discografie.html`, `galerie.html` |
| `pt` | **160px** | `md:` | 5 | `articol.html`, `blog.html`, `contact.html`, `discografie.html`, `galerie.html` |
| `pt` | **48px** | — (bază) | 5 | `faq.html`, `oferte.html` |
| `pt` | **56px** | `md:` | 4 | `oferte.html` |
| `py` | **6px** | — (bază) | 4 | `oferte.html` |
| `pt` | **128px** | `lg:` | 3 | `despre.html`, `index.html`, `oferte.html` |
| `pt` | **128px** | `md:` | 3 | `faq.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `pt` | **80px** | — (bază) | 3 | `despre.html`, `index.html`, `oferte.html` |
| `pt` | **96px** | — (bază) | 3 | `faq.html`, `politica-cookie.html`, `termeni-si-conditii.html` |
| `pb` | **16px** | — (bază) | 2 | `blog.html`, `discografie.html` |
| `pt` | **24px** | — (bază) | 2 | `index.html` |
| `py` | **128px** | `md:` | 2 | `galerie.html`, `index.html` |
| `py` | **40px** | `md:` | 2 | `despre.html`, `oferte.html` |
| `py` | **40px** | — (bază) | 2 | `despre.html`, `oferte.html` |
| `pb` | **56px** | — (bază) | 1 | `index.html` |
| `pb` | **80px** | `md:` | 1 | `index.html` |
| `pb` | **96px** | `lg:` | 1 | `index.html` |
| `pt` | **112px** | `md:` | 1 | `index.html` |
| `pt` | **16px** | — (bază) | 1 | `contact.html` |
| `pt` | **32px** | — (bază) | 1 | `discografie.html` |
| `pt` | **64px** | `md:` | 1 | `faq.html` |
| `pt` | **8px** | — (bază) | 1 | `contact.html` |
| `pt` | **96px** | `lg:` | 1 | `discografie.html` |
| `py` | **12px** | `md:` | 1 | `contact.html` |
| `py` | **16px** | `md:` | 1 | `contact.html` |
| `py` | **20px** | — (bază) | 1 | `contact.html` |
| `py` | **48px** | — (bază) | 1 | `contact.html` |
| `py` | **72px** | `md:` | 1 | `despre.html` |
| `py` | **80px** | `md:` | 1 | `contact.html` |
| `py` | **80px** | — (bază) | 1 | `galerie.html` |

**Total apariții: 278** · **45 combinații distincte**

### 3.2 — lățimi de container (`max-w-*`)

| Clasă | Valoare | Breakpoint | Apariții | Fișiere |
|---|---|---|---|---|
| `[1200px]` | **1200px** | — (bază) | 40 | toate 11 |
| `md` | **448px** | — (bază) | 14 | toate 11 |
| `0` | **0px** | — (bază) | 11 | toate 11 |
| `3xl` | **768px** | — (bază) | 8 | `articol.html`, `despre.html`, `faq.html`, `galerie.html`, `index.html`, `oferte.html` |
| `max-width` | **1200px (token propriu)** | — (bază) | 7 | `despre.html`, `oferte.html` |
| `[220px]` | **220px** | — (bază) | 6 | `faq.html`, `index.html`, `oferte.html` |
| `xl` | **576px** | — (bază) | 6 | `articol.html`, `discografie.html`, `faq.html`, `index.html` |
| `2xl` | **672px** | — (bază) | 4 | `blog.html`, `despre.html`, `oferte.html` |
| `5xl` | **1024px** | — (bază) | 3 | `oferte.html` |
| `[40rem]` | **40rem** | — (bază) | 2 | `politica-cookie.html`, `termeni-si-conditii.html` |
| `xs` | **320px** | — (bază) | 2 | `galerie.html`, `index.html` |
| `4xl` | **896px** | — (bază) | 1 | `articol.html` |
| `[30rem]` | **30rem** | — (bază) | 1 | `despre.html` |
| `sm` | **384px** | `lg:` | 1 | `index.html` |

**Total apariții: 106** · **14 combinații distincte**

### 3.3 — gap-uri de grid/flex (`gap-*`, `gap-x-*`, `gap-y-*`)

| Proprietate | Valoare (px) | Breakpoint | Apariții | Fișiere |
|---|---|---|---|---|
| `gap` | **16px** | — (bază) | 118 | toate 11 |
| `gap` | **8px** | — (bază) | 24 | toate 11 |
| `gap` | **32px** | `xl:` | 22 | toate 11 |
| `gap-x` | **8px** | — (bază) | 22 | toate 11 |
| `gap` | **24px** | — (bază) | 21 | toate 11 |
| `gap` | **24px** | `md:` | 20 | toate 11 |
| `gap` | **12px** | — (bază) | 17 | toate 11 |
| `gap` | **32px** | — (bază) | 16 | toate 11 |
| `gap` | **32px** | `sm:` | 11 | toate 11 |
| `gap` | **4px** | — (bază) | 11 | toate 11 |
| `gap-y` | **4px** | — (bază) | 11 | toate 11 |
| `gap` | **24px** | `sm:` | 8 | `discografie.html` |
| `gap` | **40px** | — (bază) | 5 | `despre.html`, `index.html` |
| `gap` | **64px** | `md:` | 4 | `despre.html`, `index.html` |
| `gap` | **2px** | — (bază) | 3 | `index.html` |
| `gap` | **40px** | `md:` | 3 | `contact.html`, `index.html` |
| `gap` | **48px** | — (bază) | 2 | `blog.html`, `galerie.html` |
| `gap` | **32px** | `md:` | 1 | `index.html` |
| `gap` | **48px** | `md:` | 1 | `discografie.html` |
| `gap` | **64px** | `lg:` | 1 | `index.html` |
| `gap-y` | **48px** | — (bază) | 1 | `contact.html` |

**Total apariții: 322** · **21 combinații distincte**

Clase de spațiere netraductibile în px (ignorate): niciuna

**Note pe tabele:**

- `max-w-max-width` (7 apariții) folosește tokenul propriu `spacing.max-width`
  = `1200px` — aceeași valoare cu `max-w-[1200px]` (40 apariții), scrisă altfel.
  Împreună: **47 de apariții ale aceleiași lățimi de container**, prin două
  clase diferite.
- `max-w-0` (11 apariții) și `max-w-xs` sunt perechea de deschidere/închidere a
  etichetei „înapoi sus" din footer: `max-w-0` la repaus, `group-hover:max-w-xs`
  și `group-focus-visible:max-w-xs` la interacțiune. Cele 22 de apariții cu
  variantă de stare sunt excluse mai sus; `max-w-xs` apare de **2** ori ca
  clasă de repaus, pe `galerie.html` și `index.html`.
- **Padding-urile verticale nu folosesc niciun token propriu de `spacing`** —
  toate cele 278 de apariții provin din scala implicită (multipli de 4px).
- Singurul token propriu de `spacing` folosit în afara lățimilor este
  `gap-gutter` (24px): **9 apariții** — 3 fără breakpoint, 6 sub `md:`. În
  tabelul 3.3 ele apar contopite cu `gap-6` / `md:gap-6`, pentru că valoarea
  randată e identică.
- `max-w-[40rem]` = 640px și `max-w-[30rem]` = 480px, la 1rem = 16px.
