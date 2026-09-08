# SYNC-WP — verificare de paritate CSS și sincronizare cu serverul

Raport generat pe 8 septembrie 2026, pe baza fișierelor descărcate prin HTTP
de pe `www.ioana-balan.ro`. Doar constatări; nicio recomandare de implementare.

---

## STARE GIT

| | |
|---|---|
| Branch activ | `main` |
| Working tree la start | curat (`nothing to commit, working tree clean`) |
| HEAD | `001adb9 feat: child theme WordPress cu fonturi self-hosted` |
| `origin/main` | `001adb9` — identic cu HEAD |
| Commit-uri nepushate | **niciunul** |
| Upstream tracking | **neconfigurat** (`fatal: no upstream configured for branch 'main'`); comparația s-a făcut explicit față de `origin/main` după `git fetch` |
| Remote | `https://github.com/laur2198/ioana-balan` |

Niciun fișier `.html` din rădăcină nu a fost modificat de această rulare.

---

## SUMAR

| # | Severitate | Constatare |
|---|---|---|
| 1 | **CRITIC** | `body { background-color; color }` a fost eliminat din `site.css` și **nu e înlocuit nicăieri**. Kit-ul Elementor (`post-3498.css`) nu declară niciun `background-color` pentru `body`, iar culoarea de text rămasă e `#57534E` (moștenire Envato), cu `h1`–`h5` pe `#1C1917` și `h6` pe `#78716C`. Baza temei întunecate din prototip s-a pierdut la portare. |
| 2 | **CRITIC** | `.motif-list > li` lipsește complet din WP. E marcajul de listă derivat din broderie — ancora vizuală din CLAUDE.md §6. Folosit în 12 liste, pe 3 pagini. |
| 3 | **CRITIC** | `.silver-border` lipsește. Nu e cod mort: e folosit de 5 ori în `oferte.html`, pe cardurile de pachete. |
| 4 | **CRITIC** | `.ghost-border` lipsește. Nu e cod mort: e folosit de 9 ori în `blog.html`, pe cardurile de articol. |
| 5 | **BLOCANT** | Header WP: link-ul de logo nu are nume accesibil — `<img alt="">` fără `aria-label` pe `<a>`. În prototip: `aria-label="Ioana Balan Acasă"` + `alt="Ioana Balan"`. |
| 6 | MINOR | Header WP: breakpoint-ul de la care se schimbă înălțimea header-ului, înălțimea logo-ului și padding-ul lateral e 1024px, nu 768px ca în prototip. Între 768px și 1024px header-ul WP e 64px / logo 32px / padding 24px, față de 80px / 48px / 64px în prototip. |
| 7 | MINOR | Header WP: itemii de meniu și butonul CTA au pierdut `text-transform: uppercase`; CTA-ul a pierdut și `letter-spacing` 0,1em (are 0,05em din tipografia globală „accent"). Niciun `text-transform` în `post-3781.css`. |
| 8 | MINOR | Pagina randată conține **două** skip link-uri către `#content`: cel injectat de `functions.php` („Sari la continut", fără diacritice) și cel din tema Hello Elementor („Sari la conținut", `.screen-reader-text`). |
| 9 | MINOR | Butonul WhatsApp flotant injectat de `functions.php` are mesajul precompletat fără diacritice („Buna ziua! As dori mai multe informatii.") față de prototip („Bună ziua! Aș dori mai multe informații."). CTA-ul din header păstrează diacriticele corect. |
| 10 | MINOR | Două culori au derivat numeric la portare: `.glass-card:hover` background `rgb(34,33,33)` → `#221f1f`, iar `.video-card` background `#0d0d0d` → `--e-global-color-hairline` (`#0E0E0E`). Diferențe de 1–2 unități pe canal. |

---

# BLOC A — VERIFICARE DE PARITATE CSS

Sursă repo: `assets/styles.css` (93 reguli, fără cele 12 blocuri `@font-face`).
Sursă WP: `assets/site.css` + `assets/components.css` (96 reguli).

Comparația a fost făcută la nivel de selector **și** de proprietate, cu
normalizarea așteptată: `0.3s` ≡ `.3s`, `""` ≡ `''`, `rgb()` ≡ hex, iar
maparea hex → `var(--e-global-color-*)` / `color-mix()` din brief tratată ca
echivalentă. Cele 12 valori din mapare au fost verificate în kit-ul live
(`/wp-content/uploads/elementor/css/post-3498.css`) și **corespund exact** —
`color-mix()` are deci variabilele de care depinde.

Notă de context: variabilele sunt declarate pe `.elementor-kit-3498`, o clasă
de pe `<body>`, nu pe `:root`. Regulile pe `html` din `site.css` nu folosesc
culori, deci nu sunt afectate.

## A3 — Tabel de paritate, toți selectorii

| Selector | În repo | În WP | Verdict |
|---|---|---|---|
| `:root` | da | nu | LIPSA |
| `html` | da | da (site.css) | PORTAT |
| `html` @media (min-width: 768px) | da | da (site.css) | PORTAT |
| `html` @media (prefers-reduced-motion: reduce) | da | da (site.css) | PORTAT |
| `body` | da | da (site.css) | PORTAT |
| `.bg-accent` | da | nu | LIPSA |
| `.glass-card` | da | da (site.css) | PORTAT |
| `.glass-card:hover` | da | da (site.css) | PORTAT |
| `.glass-panel` | da | da (site.css) | PORTAT |
| `.silver-border` | da | nu | LIPSA |
| `.ghost-border` | da | nu | LIPSA |
| `.luxury-line` | da | da (site.css) | PORTAT |
| `.hairline-separator` | da | nu | LIPSA |
| `.motif-separator` | da | da (site.css) | PORTAT |
| `.motif-rule` | da | da (site.css) | PORTAT |
| `.motif-rule::before` | da | da (site.css) | PORTAT |
| `.motif-rule::after` | da | da (site.css) | PORTAT |
| `.motif-rule__gem` | da | da (site.css) | PORTAT |
| `.motif-list > li` | da | nu | LIPSA |
| `.motif-texture` | da | da (site.css) | PORTAT |
| `.price-tbc` | da | da (components.css) | PORTAT |
| `.price-tbc__flag` | da | da (components.css) | PORTAT |
| `.price-tbc__value` | da | da (components.css) | PORTAT |
| `.hero-photo-fade` | da | da (components.css) | PORTAT |
| `.hero-photo-fade` @media (min-width: 1024px) | da | da (components.css) | PORTAT |
| `.bento-grid` | da | da (components.css) | PORTAT |
| `.skip-link` | da | da (site.css) | PORTAT |
| `.skip-link:focus` | da | da (site.css) | PORTAT |
| `:focus-visible` | da | da (site.css) | PORTAT |
| `main[tabindex="-1"]:focus` | da | da (site.css) | PORTAT |
| `.no-scrollbar::-webkit-scrollbar` | da | da (components.css) | PORTAT |
| `.no-scrollbar` | da | da (components.css) | PORTAT |
| `.line-clamp-2` | da | da (components.css) | PORTAT |
| `input[type="date"]::-webkit-calendar-picker-indicator` | da | da (components.css) | PORTAT |
| `.whatsapp-float` | da | da (site.css) | PORTAT |
| `.whatsapp-float` @media (min-width: 768px) | da | da (site.css) | PORTAT |
| `.whatsapp-float` @media (prefers-reduced-motion: reduce) | da | da (site.css) | PORTAT |
| `.whatsapp-float:hover` | da | da (site.css) | PORTAT |
| `@keyframes whatsapp-pulse` | da | da (site.css) | PORTAT |
| `.legal-prose p` | da | da (components.css) | PORTAT |
| `.legal-prose ul` | da | da (components.css) | PORTAT |
| `.legal-prose ol` | da | da (components.css) | PORTAT |
| `.legal-prose p` @media (min-width: 768px) | da | da (components.css) | PORTAT |
| `.legal-prose ul` @media (min-width: 768px) | da | da (components.css) | PORTAT |
| `.legal-prose ol` @media (min-width: 768px) | da | da (components.css) | PORTAT |
| `.legal-prose li` | da | da (components.css) | PORTAT |
| `.legal-prose li:last-child` | da | da (components.css) | PORTAT |
| `.legal-prose strong` | da | da (components.css) | PORTAT |
| `.legal-prose a` | da | da (components.css) | PORTAT |
| `.legal-prose a:hover` | da | da (components.css) | PORTAT |
| `.legal-prose code` | da | da (components.css) | PORTAT |
| `.legal-note` | da | da (components.css) | PORTAT |
| `.legal-note p:last-child` | da | da (components.css) | PORTAT |
| `.legal-table` | da | da (components.css) | PORTAT |
| `.legal-table--wide` | da | da (components.css) | PORTAT |
| `.legal-table th` | da | da (components.css) | PORTAT |
| `.legal-table td` | da | da (components.css) | PORTAT |
| `.legal-table thead th` | da | da (components.css) | PORTAT |
| `.legal-table tbody td` | da | da (components.css) | PORTAT |
| `.legal-table tbody tr:nth-child(even) td` | da | da (components.css) | PORTAT |
| `.toc summary` | da | da (components.css) | PORTAT |
| `.toc summary::-webkit-details-marker` | da | da (components.css) | PORTAT |
| `.toc summary::after` | da | da (components.css) | PORTAT |
| `.toc[open] summary::after` | da | da (components.css) | PORTAT |
| `.legal-tbc` | da | nu | LIPSA |
| `.legal-draft-banner` | da | nu | LIPSA |
| `.answer-tbc` | da | nu | LIPSA |
| `.answer-tbc__flag` | da | nu | LIPSA |
| `.faq-item summary` | da | da (components.css) | PORTAT |
| `.faq-item summary::-webkit-details-marker` | da | da (components.css) | PORTAT |
| `.video-card` | da | da (components.css) | PORTAT |
| `.gallery-grid .video-card` | da | da (components.css) | PORTAT |
| `.video-card__thumb` | da | da (components.css) | PORTAT |
| `.video-card:hover .video-card__thumb` | da | da (components.css) | PORTAT |
| `.video-card:focus-visible .video-card__thumb` | da | da (components.css) | PORTAT |
| `.video-card__veil` | da | da (components.css) | PORTAT |
| `.video-card__play` | da | da (components.css) | PORTAT |
| `.video-card:hover .video-card__play` | da | da (components.css) | PORTAT |
| `.video-card:focus-visible .video-card__play` | da | da (components.css) | PORTAT |
| `.video-card__play svg` | da | da (components.css) | PORTAT |
| `.video-card__meta` | da | da (components.css) | PORTAT |
| `.video-card__eyebrow` | da | da (components.css) | PORTAT |
| `.video-card__title` | da | da (components.css) | PORTAT |
| `.video-card__title` @media (min-width: 640px) | da | da (components.css) | PORTAT |
| `.video-card.is-playing` | da | da (components.css) | PORTAT |
| `.video-card.is-playing:focus` | da | da (components.css) | PORTAT |
| `.video-card iframe` | da | da (components.css) | PORTAT |
| `.video-card__thumb` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.video-card__play` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.video-card:hover .video-card__thumb` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.video-card:focus-visible .video-card__thumb` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.video-card:hover .video-card__play` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.video-card:focus-visible .video-card__play` @media (prefers-reduced-motion: reduce) | da | da (components.css) | PORTAT |
| `.whatsapp-float__label` | nu | da (site.css) | NOU |
| `.whatsapp-float:hover .whatsapp-float__label` | nu | da (site.css) | NOU |
| `.whatsapp-float:focus-visible .whatsapp-float__label` | nu | da (site.css) | NOU |
| `.whatsapp-float__label` @media (max-width: 639px) | nu | da (site.css) | NOU |
| `.elementor-button.ib-cta-primary` | nu | da (components.css) | NOU |
| `.faq-item` | nu | da (components.css) | NOU |
| `.faq-item summary` @media (min-width: 768px) | nu | da (components.css) | NOU |
| `.faq-item summary svg` | nu | da (components.css) | NOU |
| `.faq-item details[open] summary svg` | nu | da (components.css) | NOU |
| `.faq-item__answer` | nu | da (components.css) | NOU |
| `.faq-item__answer` @media (min-width: 768px) | nu | da (components.css) | NOU |
| `.legal-table-wrap` | nu | da (components.css) | NOU |

Total: **83 PORTAT**, **10 LIPSA**, **12 NOU**.

Selectorii NOU sunt, în cea mai mare parte, reguli care în prototip erau
clase utilitare Tailwind pe element (`.faq-item summary` cu flex/padding,
`.legal-table-wrap` cu `overflow-x`, `.hero-photo-fade` cu
`position/inset/pointer-events`) și care, în lipsa Tailwind-ului, au trebuit
scrise explicit. `.elementor-button.ib-cta-primary` e succesorul lui
`.bg-accent`. `.whatsapp-float__label` e traducerea utilitarelor
`group-hover:max-w-xs` din prototip.

## A4 — Analiza selectorilor LIPSA

### Excluse intenționat — nu sunt probleme

| Selector | Motiv | Verificare |
|---|---|---|
| 12 blocuri `@font-face` | sunt în `style.css` al temei copil | confirmat: 12 în `assets/styles.css` (prototip), 12 identice în `wp-child-theme/ioana-balan-child/style.css` |
| `.legal-tbc` | marcaj de prototip pentru valori neconfirmate | folosit în `termeni-si-conditii.html`, `politica-cookie.html` — nu se portează |
| `.legal-draft-banner` | idem | folosit în `politica-cookie.html`, `termeni-si-conditii.html` |
| `.answer-tbc` | idem | folosit în `oferte.html`, `faq.html` |
| `.answer-tbc__flag` | idem | folosit în `oferte.html`, `faq.html` |
| `.hairline-separator` | de verificat dacă e cod mort | **confirmat cod mort** — zero apariții în oricare `.html` din repo |
| `.bg-accent` | a devenit `.ib-cta-primary` | confirmat: `.elementor-button.ib-cta-primary { border: 1px solid var(--e-global-color-500ff34) }` reproduce `border: 1px solid var(--accent-edge)` |
| `:root` | conținea doar `--accent-edge: #C41236` | benign: variabila e complet rezolvată în WP la `var(--e-global-color-500ff34, #C41236)`; zero referințe rămase la `--accent-edge` în CSS-ul de pe server |

Verificări cerute explicit, cu rezultat contrar așteptării:

- `.price-tbc` și variantele — **A FOST portat**, confirmat. `.price-tbc`,
  `.price-tbc__flag`, `.price-tbc__value` sunt toate în `components.css`.
- `.glass-card` — **este folosit** (`articol`, `discografie`, `oferte`,
  `politica-cookie`, `termeni-si-conditii`) și **a fost portat**. Nu e cod mort.
- `.silver-border`, `.ghost-border` — **NU sunt cod mort**, vezi mai jos.

### Probleme reale

#### `.motif-list > li` — CRITIC

Proprietăți pierdute:

```css
padding-left: 26px;
background-image: url("data:image/svg+xml,…<path d='M8 2 L14 8 L8 14 L2 8 Z' stroke='%23800020' stroke-width='1.5'/>…");
background-repeat: no-repeat;
background-position: left 0.2em;
background-size: 14px 14px;
```

Folosit în: `oferte.html` (5 liste), `termeni-si-conditii.html` (5 liste),
`politica-cookie.html` (2 liste).

Este rombul de broderie folosit ca marcaj de listă — unul dintre cele trei
roluri ale ancorei vizuale descrise în CLAUDE.md §6. Celelalte două roluri
(`.motif-separator`, `.motif-texture`) au fost portate; acesta nu.

#### `.silver-border` — CRITIC

Proprietăți pierdute: `border: 1px solid rgba(198, 198, 198, 0.2);`

Folosit de 5 ori în `oferte.html`, pe panoul de context și pe cardurile de
pachete (`class="glass-card … silver-border"`). `.glass-card` a fost portat și
aduce propriul `border: 1px solid color-mix(… bordodark 15% …)`, deci elementele
nu rămân fără bordură — dar bordura argintie mai deschisă, care distinge cardurile
de pachet de restul, dispare.

#### `.ghost-border` — CRITIC

Proprietăți pierdute: `border: 1px solid rgba(227, 226, 222, 0.15);`

Folosit de 9 ori în `blog.html`, pe cardurile de articol
(`class="flex flex-col bg-surface-container-low ghost-border overflow-hidden group"`).
Aici nu există `.glass-card` care să compenseze: cardurile rămân **complet fără
bordură**.

## A5 — Diferențe de proprietăți pe selectorii PORTAT

Diferențele pur cosmetice (`0.3s`/`.3s`, ghilimele, `rgb()`/hex, spații în
`rgba()`) și substituțiile de culoare din maparea agreată nu sunt listate.

### Diferențe care schimbă rezultatul vizual

| Selector | Diferență |
|---|---|
| `body` | **lipsesc 3 proprietăți**: `background-color: #131313`, `color: #e5e2e1`, `font-family: 'Inter', sans-serif` |
| `.glass-card:hover` | `background`: repo `rgb(34, 33, 33)` = `#222121` → WP `#221f1f`. Valoare numerică diferită, nu o substituție din mapare. |
| `.video-card` | `background`: repo `#0d0d0d` → WP `var(--e-global-color-hairline, #0E0E0E)`. Maparea acoperă `#0E0E0E`, dar sursa era `#0d0d0d`. |

Despre `body`:

- `font-family` este acoperit — kit-ul aplică
  `.elementor-kit-3498 { font-family: "Inter", Sans-serif }`.
- `background-color` **nu este acoperit**: singurul `background-color` din tot
  `post-3498.css` este `.elementor-kit-3498 e-page-transition{background-color:#FFBC7D}`.
  Nu există niciun fundal pentru `body`.
- `color` **nu este acoperit corect**: kit-ul declară `color:#57534E` pe
  `.elementor-kit-3498`, plus `h1`–`h5` pe `#1C1917` și `h6` pe `#78716C` —
  valori de temă deschisă, moștenite din kit-ul Envato, opuse sistemului din
  CLAUDE.md §5.

### Diferențe fără efect vizual (pentru completitudine)

| Selector | Diferență | De ce nu contează |
|---|---|---|
| `html` | WP adaugă `scroll-behavior: smooth` | mutat de pe `body` pe `html`, unde și funcționează efectiv |
| `.price-tbc__flag` | lipsește `color: #e5e2e1` | se moștenește de la `.price-tbc`, care are `color: var(--e-global-color-primary)` |
| `.price-tbc__value` | lipsește `color: #e5e2e1` | idem |
| `.hero-photo-fade` | WP adaugă `position: absolute`, `inset: 0`, `pointer-events: none` | în prototip erau clase Tailwind pe element |
| `.whatsapp-float` | WP adaugă `text-decoration: none` | compensează stilizarea de link din tema WP |
| `.whatsapp-float:hover` | WP adaugă `color: #fff` | idem |
| `.toc summary` | WP adaugă `display: flex`, `align-items: center` | erau clase Tailwind |
| `.faq-item summary` | WP adaugă `display`, `justify-content`, `align-items`, `gap: 16px`, `padding: 20px`, `cursor` | erau clase Tailwind |

## A6 — `@keyframes` și `prefers-reduced-motion`

### `@keyframes`

| Nume | Repo | WP | Verdict |
|---|---|---|---|
| `whatsapp-pulse` | `assets/styles.css:401` | `assets/site.css:139` | PORTAT, valori identice |

Un singur `@keyframes` în prototip, unul singur în WP. Cele trei
opriri (0% / 70% / 100%) au aceleași `box-shadow`, diferind doar prin
notația `0.3` / `.3`. O singură proprietate `animation:` în prototip
(`whatsapp-pulse 2.5s infinite`), prezentă identic în WP.

### `@media (prefers-reduced-motion: reduce)`

Două blocuri în repo, două în WP; toate cele 8 reguli au corespondent.

| Regulă | Repo | WP | Verdict |
|---|---|---|---|
| `.whatsapp-float { animation: none }` | styles.css:408 | site.css:145 | PORTAT |
| `html { scroll-behavior: auto }` | styles.css:408 | site.css:145 | PORTAT |
| `.video-card__thumb { transition: none }` | styles.css:749 | components.css:119 | PORTAT |
| `.video-card__play { transition: none }` | styles.css:749 | components.css:119 | PORTAT |
| `.video-card:hover .video-card__thumb { transform: none }` | styles.css:749 | components.css:119 | PORTAT |
| `.video-card:focus-visible .video-card__thumb { transform: none }` | styles.css:749 | components.css:119 | PORTAT |
| `.video-card:hover .video-card__play { transform: … }` | styles.css:749 | components.css:119 | PORTAT |
| `.video-card:focus-visible .video-card__play { transform: … }` | styles.css:749 | components.css:119 | PORTAT |

Constatare colaterală: regula nouă `.whatsapp-float__label` are
`transition: max-width .3s ease, margin-left .3s ease` și nu este acoperită
de niciunul dintre cele două blocuri `prefers-reduced-motion`.

---

# BLOC B — SINCRONIZARE REPO

## B1 — Fișiere descărcate și scrise în repo

Toate cele 5 au răspuns `HTTP 200` cu conținut valid (nu pagini de eroare).

| Fișier server | Octeți | Destinație în repo |
|---|---|---|
| `style.css` | 8 580 | `wp-child-theme/ioana-balan-child/style.css` |
| `assets/site.css` | 4 498 | `wp-child-theme/ioana-balan-child/assets/site.css` |
| `assets/components.css` | 9 615 | `wp-child-theme/ioana-balan-child/assets/components.css` |
| `assets/site.js` | 2 324 | `wp-child-theme/ioana-balan-child/assets/site.js` |
| `assets/motifs.svg` | 919 | `wp-child-theme/ioana-balan-child/assets/motifs.svg` |

`site.css`, `components.css`, `site.js` erau **absente** din repo — sunt fișiere
noi. `style.css` a fost suprascris (vezi B2). `motifs.svg` e nou în folderul
temei; e **identic octet cu octet** cu `assets/motifs.svg` din prototip.

Cele 12 fișiere din `assets/fonts/` nu au fost atinse.

## B2 — Diferențe `style.css` (repo, înainte de suprascriere) vs. server

Repo: 4 995 octeți. Server: 8 580 octeți.

Serverul conține **exact un bloc în plus**, la finalul fișierului; primele 115
linii sunt identice, inclusiv toate cele 12 `@font-face` pentru EB Garamond și
Inter. Nicio linie ștearsă, nicio linie modificată.

Blocul suplimentar: **`MONTSERRAT ALIAS - TEMPORAR`** — **confirmat prezent**.

- 19 declarații `@font-face` pentru familia `Montserrat`
  (greutățile 100–900 normal, plus italic 400, fiecare în variantă `latin` și
  `latin-ext`), care nu încarcă fișiere noi ci trimit către
  `inter-400-*.woff2` și `inter-600-*.woff2` deja prezente.
- Greutățile 100–500 primesc Inter 400; 600–900 primesc Inter 600.
- Comentariul din sursă explică motivul: paginile moștenite din kituri Envato
  (2022) cer `Montserrat` hardcodat în fiecare widget; fontul venea de la
  Google Fonts, pe care tema îl blochează; fără alias textele ar cădea pe
  sans-serif de sistem.
- Sursa îl marchează ea însăși: *„DE STERS dupa ce toate paginile sunt
  reconstruite cu token-uri globale."*

**Notat ca temporar, de șters după reconstrucția paginilor.** Numărul total de
`@font-face` în `style.css` de pe server e 31 = 12 reale + 19 alias.

## B3 — Arhivă regenerată

`wp-child-theme/ioana-balan-child.zip` regenerat din folderul actualizat.
Structură verificată: `ioana-balan-child/` la rădăcina arhivei.

```
ioana-balan-child/
├── style.css                     8 580
├── functions.php                 4 280   ← DEPĂȘIT, vezi B4
└── assets/
    ├── site.css                  4 498
    ├── components.css            9 615
    ├── site.js                   2 324
    ├── motifs.svg                  919
    └── fonts/                   12 fișiere .woff2
```

## B4 — `functions.php`

`functions.php` nu poate fi descărcat prin HTTP: PHP-ul se execută pe server,
nu se servește ca text. Nu a fost sincronizat.

Fișierul din repo (**4 280 octeți**, ≈4,2 KB) este **DEPĂȘIT** față de cel de
pe server (≈7,3 KB). Ce conține repo-ul acum: `ib_child_enqueue_styles`
(doar tema părinte + `style.css` al copilului), `ib_child_preload_fonts`,
`ib_child_dequeue_google_fonts`, `ib_child_filter_resource_hints`.

Diferența, confirmată prin inspecția paginii randate `/test-header/`, conține:

| Ce lipsește | Dovadă în pagina randată |
|---|---|
| `wp_enqueue_style` pentru `assets/site.css` | `<link>` către `…/ioana-balan-child/assets/site.css` |
| `wp_enqueue_style` pentru `assets/components.css` | `<link>` către `…/ioana-balan-child/assets/components.css` |
| `wp_enqueue_script` pentru `assets/site.js` | `<script>` către `…/ioana-balan-child/assets/site.js` |
| skip link injectat pe `wp_body_open` | `<a class="skip-link" href="#content">Sari la continut</a>` |
| buton WhatsApp flotant injectat pe `wp_footer` | `<a class="whatsapp-float" href="https://wa.me/40722911485?text=Buna%20ziua%21%20As%20dori%20mai%20multe%20informatii." target="_blank" rel="noopener" aria-label="Contact Ioana Balan pe WhatsApp">` cu `<span class="whatsapp-float__label">Salut! Scrie-mi pe WhatsApp</span>` |

**Marcat „de sincronizat manual".**

---

# BLOC C — HEADER-UL DIN THEME BUILDER

Sursă WP: `https://www.ioana-balan.ro/test-header/`, zona `<header>` (6 191
octeți), template Elementor `elementor_library` id **3781**, plus regulile din
`/wp-content/uploads/elementor/css/post-3781.css` (15 969 octeți).
Sursă prototip: `<header>` din `index.html`.

## C3 — Tabel de paritate

| Element | Prototip | WordPress | Potrivire |
|---|---|---|---|
| **Înălțime header, desktop** | `md:h-20` = 80px de la 768px | `--min-height: 80px` peste 1024px | ✅ identic peste 1024px |
| **Înălțime header, mobil** | `h-16` = 64px sub 768px | `--min-height: 64px` sub 1024px | ⚠️ **MINOR** — pragul e 1024px, nu 768px: între 768 și 1024px prototipul are 80px, WP are 64px |
| **Lățime conținut** | `max-w-[1200px]` | `--content-width: 1200px` de la 768px | ✅ |
| **Padding lateral** | 16px mobil / 64px de la 768px | 64px desktop / 24px ≤1024px / 16px ≤767px | ⚠️ **MINOR** — WP introduce o treaptă intermediară de 24px care nu există în prototip; între 768 și 1024px prototipul are 64px |
| **Fundal semi-transparent** | `bg-background/95` = `rgba(19,19,19,0.95)` | `background-color: color-mix(in srgb, var(--e-global-color-surface) 95%, transparent)` = același | ✅ |
| **`backdrop-filter`** | `backdrop-blur-md` = `blur(12px)` | `-webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px)` | ✅ (prefix `-webkit-` în plus, corect) |
| **Bordură inferioară** | `border-b border-outline-variant/20` = `rgba(68,71,72,0.2)` | `border-bottom: 1px solid color-mix(in srgb, var(--e-global-color-white) 20%, transparent)`, unde `--e-global-color-white` = `#444748` | ✅ |
| **Poziționare** | `fixed top-0 z-50` | Elementor sticky `top`, activ pe desktop + tablet + mobil, `sticky_offset: 0` | ⚠️ **MINOR** — sticky Elementor devine fix la scroll, nu din start; header-ul e primul element, deci comportamentul e practic echivalent |
| **Logo — fișier** | `assets/logo-alb-400w.png` | `/wp-content/uploads/2026/09/logo-alb-400w.png` (id media 3763) | ✅ același fișier |
| **Logo — `srcset`** | `400w 1x, 800w 2x` (sursă retina) | `400w` + `300x103 300w`, `sizes="(max-width: 400px) 100vw, 400px"` | ⚠️ **MINOR** — nu există sursă 2x; la 400×137 afișat pe 48px înălțime rezerva rămâne suficientă, dar varianta 800w din repo nu a fost urcată |
| **Logo — înălțime desktop** | `md:h-12` = 48px de la 768px | `height: 48px` peste 1024px | ✅ peste 1024px |
| **Logo — înălțime mobil** | `h-8` = 32px sub 768px | `height: 32px` sub 1024px | ⚠️ **MINOR** — același decalaj de prag 768 vs. 1024px |
| **Logo — `object-fit`/lățime** | `w-auto` | `object-fit: contain`, CSS custom `width: auto` | ✅ |
| **Logo — link** | `href="index.html"` | `href="https://www.ioana-balan.ro/"` | ✅ |
| **Logo — nume accesibil** | `aria-label="Ioana Balan Acasă"` pe `<a>`, `alt="Ioana Balan"` pe `<img>` | `<a>` fără `aria-label`, `<img alt="">` | 🔴 **BLOCANT** — link fără nume accesibil |
| **Număr itemi de meniu** | 7 | 5 | ⚠️ **AȘTEPTAT** — paginile noi nu există încă |
| **Ordinea itemilor** | Despre · Galerie · Discografie · Oferte · FAQ · Blog · Contact | acasa · despre mine · video clipuri · formatie nunta Bucuresti · termeni si conditii | ⚠️ **AȘTEPTAT** — meniul WP are încă itemii vechi |
| **„Acasă" în meniu** | **absent** — logo-ul e link-ul spre home | **prezent** (`menu-item-home`, „acasa") | ⚠️ **AȘTEPTAT** — parte din meniul vechi; de eliminat la reconstrucție, ca să nu dubleze logo-ul |
| **Meniu — majuscule** | `uppercase` pe fiecare item | niciun `text-transform` în `post-3781.css`; etichetele sunt scrise cu minuscule | ⚠️ **MINOR** — diferență de stilizare care persistă și după înlocuirea itemilor |
| **Meniu — tipografie** | `font-label-md text-label-md` | `--e-global-typography-accent-*`: Inter 14px / 600 / 1.4em / `letter-spacing: 0.05em` | ✅ echivalent |
| **Meniu — culoare** | `text-on-surface-variant` (`#c4c7c7`), hover `text-primary` | `var(--e-global-color-secondary)` (`#C6C6C6`), hover `var(--e-global-color-primary)` (`#E5E2E1`) | ✅ substituție din mapare |
| **CTA — text** | „Rezervă pe WhatsApp" | „Rezervă pe WhatsApp" | ✅ identic, cu diacritice |
| **CTA — destinație** | `https://wa.me/40722911485?text=Bun%C4%83%20ziua%21%20A%C8%99%20dori%20s%C4%83%20rezerv%20o%20dat%C4%83%20pentru%20evenimentul%20meu.` | identic, caracter cu caracter | ✅ mesaj precompletat identic |
| **CTA — `target`/`rel`** | `target="_blank" rel="noopener"` | `target="_blank"`, **fără `rel`** | ⚠️ **MINOR** |
| **CTA — vizibilitate** | `hidden lg:block` — ascuns sub 1024px | `elementor-hidden-tablet elementor-hidden-mobile` — ascuns ≤1024px | ✅ |
| **CTA — culori** | `bg-accent` (`#A01028`), hover `bg-accent-hover` | `background-color: var(--e-global-color-accent)` (`#A01028`), hover `var(--e-global-color-muted)` (`#800020`) | ✅ substituție din mapare |
| **CTA — majuscule / tracking** | `uppercase tracking-widest` (0,1em) | fără `text-transform`; `letter-spacing: 0.05em` din tipografia „accent" | ⚠️ **MINOR** |
| **CTA — colțuri** | fără `rounded` | `border-radius: 0px` | ✅ |
| **CTA — `white-space`** | `whitespace-nowrap` | CSS custom `white-space: nowrap` | ✅ |
| **Buton telefon pe mobil** | prezent, `lg:hidden` | prezent, `elementor-hidden-desktop` (widget `icon`, `fas fa-phone-alt`) | ✅ |
| **Buton telefon — link** | `tel:+40722911485` | `tel:+40722911485` | ✅ identic |
| **Buton telefon — nume accesibil** | `aria-label="Sună acum"` | `<a class="elementor-icon">` cu `<i aria-hidden="true">`, fără `aria-label` | 🔴 **BLOCANT** — al doilea link fără nume accesibil în header |
| **Buton telefon — dimensiune țintă** | `w-11 h-11` = 44×44px | `font-size: 22px` pe iconiță, fără padding declarat | ⚠️ **MINOR** — ținta de tap probabil sub 44px (quality floor CLAUDE.md §8) |
| **Breakpoint hamburger** | `hidden lg:flex` pe `<nav>` — hamburger sub 1024px | `elementor-nav-menu--dropdown-tablet`; breakpoint-urile din `post-3781.css` sunt `max-width: 1024px` / `max-width: 767px` / `min-width: 768px` | ✅ **1024px, corect** |
| **Hamburger — icon** | SVG inline | `eicon-menu-bar` / `eicon-close` (icon font Elementor) | ✅ echivalent funcțional |
| **Hamburger — accesibilitate** | `<button aria-label="Deschide Meniu" aria-expanded="false" aria-controls="mobile-menu">` | `<div role="button" tabindex="0" aria-label="Menu Toggle" aria-expanded="false">`, fără `aria-controls` | ⚠️ **MINOR** — eticheta e în engleză, lipsește `aria-controls` |
| **Dropdown mobil — fundal** | — | `background-color: var(--e-global-color-surfacealt)` (`#1C1B1B`) | ✅ conform sistemului |
| **Dropdown mobil — hover** | — | `background-color: var(--e-global-color-accent)`, `color: #FFFFFF` | ✅ |
| **`<nav>` — etichetă** | fără `aria-label` | `aria-label="Meniu"` | ✅ îmbunătățire față de prototip |

### Recapitulare severități, Bloc C

- **BLOCANT (2):** link-ul de logo și butonul de telefon nu au nume accesibil.
- **MINOR (9):** pragul 768→1024px pentru înălțime/logo/padding, treapta de
  padding 24px, lipsa sursei 2x pentru logo, lipsa majusculelor pe meniu și CTA,
  `letter-spacing` 0,05em vs. 0,1em pe CTA, `rel="noopener"` absent pe CTA,
  ținta de tap a butonului de telefon, eticheta „Menu Toggle" în engleză fără
  `aria-controls`, sticky vs. fixed.
- **AȘTEPTAT (3):** numărul itemilor de meniu, ordinea lor, prezența „Acasă" —
  toate pentru că paginile noi nu există încă.

## C4 — Footer: inventar de paritate

Footer-ul **nu există încă în WordPress** (nici template `elementor-location-footer`
în pagina randată). Inventarul de mai jos e extras din `<footer>` din `index.html`
și servește ca listă de verificare pentru când se construiește.

### Banda 1 — brand + social

| Element | Detalii |
|---|---|
| Logo | `assets/logo-alb-400w.png`, `srcset` 400w 1x / 800w 2x, `h-8 md:h-10` (32px → 40px de la 768px), link `index.html`, `aria-label="Ioana Balan Acasă"`, `alt="Ioana Balan"`, `loading="lazy"` |
| Descriere | „Muzică pentru evenimente care rămân în suflet. Calitate corporate cu pasiune artistică și profesionalism garantat." — **wording nedecis**, CLAUDE.md §9 îl listează ca deschis |
| Facebook | `https://www.facebook.com/ioanabalanoficial` |
| Instagram | `https://www.instagram.com/ioanabalanoficial/` |
| YouTube | `https://www.youtube.com/channel/UCNTWODu5imMryMhkbbw6vEQ` |
| TikTok | `https://www.tiktok.com/@ioanabalanmusic` |

Toate cele patru iconițe: SVG inline 20×20 `fill="currentColor"`, țintă de tap
`w-11 h-11` (44×44px), `aria-label` cu numele rețelei, `target="_blank" rel="noopener"`,
`<svg aria-hidden="true">`, într-un `<ul>` pe un singur rând inclusiv pe mobil.

### Banda 2 — contact + informații legale

| Element | Destinație |
|---|---|
| E-mail | `mailto:ioanabalanoficial@gmail.com` — adresa reală confirmată (CLAUDE.md §9) |
| Telefon | `tel:+40722911485`, afișat „+40 722 911 485" |
| ANPC | `https://anpc.ro`, `rel="noopener noreferrer"` |
| Separator | `·` cu `aria-hidden="true"`, `opacity-50` |
| SAL | `https://anpc.ro/ce-este-sal/`, `aria-label="SAL — Soluționarea alternativă a litigiilor"` |
| Termeni și condiții | `termeni-si-conditii.html` |
| Separator | `·` cu `aria-hidden="true"` |
| Politica de cookie-uri | `politica-cookie.html` |

Toate link-urile din această bandă au `min-h-[44px]` pentru țintă de tap.

### Banda 3 — juridic

| Element | Text |
|---|---|
| Copyright | „© 2026 Ioana Balan. Toate drepturile rezervate." |
| Separator | `·`, `hidden sm:inline` |
| Dezvoltator | „Proiect dezvoltat de **Grand Music Events**" → `https://grand-music.ro`, `target="_blank" rel="noopener"` |
| Separator | `·`, `hidden sm:inline` |
| Realizator | „Site realizat de Green Pheonix Concept" (fără link) |

Pe desktop cele trei elemente stau pe un rând separate prin punct median; pe
mobil se stivuiesc, centrate.

### Comentarii TODO din sursă, de transferat

1. **TODO client/juridic — SOL/ODR.** Platforma europeană SOL/ODR
   (`ec.europa.eu/consumers/odr`) a fost desființată prin Regulamentul (UE)
   2024/3228. Linkul echivalent în vigoare e SAL-ul ANPC; de confirmat cu
   juristul înainte de lansare.
2. **TODO client — rând de date de firmă, OBLIGATORIU înainte de lansare.**
   Rândul `Grand Music Events · CUI … · Reg. Com. …` este comentat în DOM.
   Concurența afișează CUI + Reg. Com.; pentru un site care încasează avans,
   legitimitatea juridică e argument de conversie. Se reactivează completând
   cele două valori. **Atenție: datele Grand Music Events (clientul), NU Green
   Pheonix Concept (furnizorul site-ului).**
3. **Notă de ortografie.** „Pheonix" este ortografia juridică înregistrată a
   firmei — nu se corectează.
4. **Notă de structură.** Benzile se separă prin spațiere, nu prin linie.
   Documentele de subsol stau în afara navigației din header.

---

# DE SINCRONIZAT MANUAL

| Fișier | De ce | Ce conține în plus față de repo |
|---|---|---|
| `wp-child-theme/ioana-balan-child/functions.php` | PHP-ul se execută pe server, nu se poate descărca prin HTTP | ≈3 KB: `wp_enqueue_style` pentru `assets/site.css` și `assets/components.css`, `wp_enqueue_script` pentru `assets/site.js`, skip link injectat pe `wp_body_open`, buton WhatsApp flotant injectat pe `wp_footer` (cu `.whatsapp-float__label`) |
| Header Theme Builder (id **3781**) | trăiește în baza de date ca post `elementor_library`, nu ca fișier în temă | structura completă a header-ului: containere `hdrwrap` / `hdrlogo` / `hdrright` / `hdrtel` / `hdrnav` / `hdrcta`, plus setările lor. Reconstituibil doar din export Elementor sau din `post-3781.css` (15 969 octeți), care conține doar CSS-ul generat, nu și conținutul |
| Kit global Elementor (id **3498**) | idem, în baza de date | cele 12 variabile `--e-global-color-*` și cele 8 seturi `--e-global-typography-*` de care depind `var()` și `color-mix()` din `site.css`/`components.css`. Reconstituibil din `post-3498.css` |
| Meniu WordPress | în baza de date (`nav_menu`) | cei 5 itemi actuali; de înlocuit când există paginile noi |
| Logo urcat în Media Library | id **3763**, `/wp-content/uploads/2026/09/logo-alb-400w.png` | varianta `logo-alb-800w.png` (sursa 2x din repo) nu e urcată |
