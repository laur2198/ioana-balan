# `--accent-edge` pe suprafețe întunecate — audit complet

Măsurat pe `79f61be`, 19.09.2026. Acoperă **toate cele 38 de pagini HTML**: 11 în
rădăcină, 27 în `zone-mockup/`.

> **STARE: cele trei neconformități sunt REPARATE** (`88ed6ae` → reparația de
> față). Regula moartă `.price-tbc` e ștearsă. Valoarea `--accent-edge` nu s-a
> schimbat și nu s-a adăugat nicio culoare. Cifrele de mai jos sunt păstrate ca
> „înainte", iar fiecare rând reparat poartă și valoarea de după, **măsurată pe
> elementul randat în browser**, nu doar calculată. Vezi §5.

`--accent-edge: #C41236` e definit o singură dată, în `assets/styles.css:146`.
Pe paginile de zonă e re-expus ca `--accent-zona`, în blocul de stiluri al
fiecărei pagini.

---

## 1. Metoda

Contrastul se calculează față de **fondul efectiv**, adică fondul pe care
elementul chiar apare, nu față de `#131313` din reflex. Trei suprafețe contează:

| Suprafață | Valoare | Unde |
|---|---|---|
| Pagina | `#131313` | fundalul general |
| Cardul | `#1c1b1b` | `.glass-card` — secțiuni, FAQ, casete de logistică |
| Badge-ul | `#20201f` | numai `.zona-badge` |

Fondurile semitransparente se compun înainte de măsurare: `rgba(196,18,54,0.18)`
peste pagină dă `#331319`, iar peste card `#3A1920`.

### Ce se marchează drept neconformitate

Numai trei categorii, exact ca în brief:

| Categorie | Prag | SC |
|---|---|---|
| Componente de interfață | 3:1 | 1.4.11 |
| Focus și stări | 3:1 | 1.4.11 |
| Text | 4,5:1 (3:1 la text mare) | 1.4.3 |

**Decorativul nu are prag.** Un element decorativ sub 3:1 e o observație de
design, nu o neconformitate, și e marcat ca atare.

---

## 2. Tabelul — 12 utilizări

| # | Element | Rol | Fond efectiv | Contrast | Verdict |
|---|---|---|---|---|---|
| 1 | `.bg-accent` — bordură 1px | CTA primar, **componentă** | pagină `#131313` | **3,09:1** | conform |
| 1b | `.bg-accent` — bordură 1px | idem, în interiorul unui card | card `#1c1b1b` | **2,85:1** | **la limită** — vezi §3.0 |
| 2 | `.btn-secundar-zona` — bordură 1px | CTA secundar, **componentă** | pagină `#131313` | **3,09:1** | conform |
| 2b | `.btn-secundar-zona` — bordură 1px | idem, în interiorul unui card | card `#1c1b1b` | 2,85:1 → **5,41:1** | **REPARAT** |
| 3 | `.toc summary::after` — chevron 2px | indicator deschis/închis, **stare** | card `#1c1b1b` | 2,85:1 → **10,06:1** | **REPARAT** |
| 4 | `.legal-prose a` — `text-decoration-color` | sublinierea care identifică linkul | card `#1c1b1b` | 2,06:1 → **13,34:1** | **REPARAT** |
| 4b | `.legal-prose a:hover` — `text-decoration-color` | întărire la hover, nu identificare | card `#1c1b1b` | 2,85:1 | nemodificat, intenționat |
| 5 | `.video-card__play` — `border-color` la hover/focus | întărire vizuală | `#A01028` | 1,34:1 | conform — vezi §3.0 |
| 6 | `.zona-badge` — bordură 1px | etichetă de zonă, **decorativ** | badge `#20201f` | 2,71:1 | fără prag |
| 7 | `.zona-divider` — gradient | separator, **decorativ** | pagină `#131313` | 3,09:1 | fără prag |
| 8 | `.zona-gem` — bordură romb | ornament în `.motif-rule`, **decorativ** | pagină / card | 3,09 / 2,85:1 | fără prag |
| 9 | `.legal-tbc` — bordură 2px punctată | marcaj de valoare lipsă, **decorativ** | propriu `#331319` | 2,79:1 | fără prag |
| 10 | `.answer-tbc` — bordură 2px punctată | marcaj de răspuns neconfirmat, **decorativ** | propriu `#331319` | 2,79:1 | fără prag |
| 11 | `.legal-draft-banner` — bordură | casetă „document în lucru", **decorativ** | propriu `#2C1318` | 2,87:1 | fără prag |
| 12 | `.price-tbc` — bordură 2px punctată | **regulă moartă** | — | — | **ȘTEARSĂ** |

### Unde apar, pe pagini

| Clasă | Apariții | Rădăcină | `zone-mockup/` |
|---|---|---|---|
| `.bg-accent` | 166 | 11 pagini | 27 pagini |
| `.btn-secundar-zona` | 73 | — | 27 pagini |
| `.zona-divider` | 115 | — | 27 pagini |
| `.zona-gem` | 48 | — | 21 pagini |
| `.zona-badge` | 27 | — | 27 pagini |
| `.legal-tbc` | 19 | 2 pagini | — |
| `.answer-tbc` | 14 | 2 pagini | — |
| `.video-card` | 9 | 2 pagini | — |
| `.legal-prose`, `.toc`, `.legal-draft-banner` | 2 fiecare | 2 pagini | — |
| `.price-tbc` | **0** | — | — |

---

## 3. Cele trei neconformități

### 3.0 Două care par neconformități și nu sunt

Le pun întâi, pentru că prima trecere a auditului le marcase greșit.

**`.video-card__play`, bordura la hover și `:focus-visible` — 1,34:1.** Pare
grav: un indicator de focus la 1,34:1. Nu e, pentru că **nu el e indicatorul de
focus.** `assets/styles.css:341` definește global `:focus-visible { outline: 2px
solid #c8c6c5 }`, adică **10,92:1 pe pagină** și **4,75:1 chiar peste `#A01028`**.
Bordura bordo e o întărire vizuală care se adaugă peste conturul de focus, nu
îl înlocuiește. Conform.

**`.bg-accent` în interiorul unui card — 2,85:1.** Butonul primar are umplutură
`#A01028` și text alb la **8,08:1**. Ce identifică butonul e blocul plin plus
eticheta, nu hairline-ul din jur. Sub o citire strictă a lui 1.4.11 s-ar putea
argumenta că bordura e conturul componentei și că 2,85:1 pică; sub citirea
obișnuită, un buton plin cu text peste 4,5:1 e identificabil fără bordură.
**Îl las „la limită", nu îl declar neconformitate** — dar semnalez că, dacă se
aplică P2 din `ZONE-NOI-PLAN.md` §4, se rezolvă și el, fără efort suplimentar.

Diferența față de cazul 2b de mai jos e esențială și merită spusă explicit:
**butonul primar are și altceva în afară de bordură. Cel secundar nu are.**

### 3.1 `.btn-secundar-zona` pe fond de card — 2,85:1

**Cea mai importantă din cele trei.** Butonul secundar are fond transparent:
singurul lucru care îl delimitează de restul paginii e bordura. Când stă pe
pagină, 3,09:1 — trece la limită. Când stă într-un `.glass-card`, 2,85:1 — pică.

Apare pe **toate cele 27 de pagini** din `zone-mockup/`, de 73 de ori. Cele mai
multe instanțe sunt în secțiunea „Pachete", care e chiar un `.glass-card`.

**Propunere, fără schimbarea token-ului global:** o regulă contextuală care
schimbă doar bordura, doar când butonul e într-un card.

```css
/* Pe fond de card (#1c1b1b) bordura bordo scade la 2,85:1, sub pragul de
   3:1 pentru componente. Butonul secundar nu are umplutură, deci bordura e
   singurul lui contur. Token existent, fără valoare nouă. */
.glass-card .btn-secundar-zona {
  border-color: var(--outline);   /* #8e9192 → 5,41:1 pe card */
}
```

`--outline` e deja în paletă. Costul vizual: butonul secundar din interiorul
cardurilor devine argintiu în loc de bordo. Alternativa care păstrează bordo-ul
e P2 (`#DB143C` → 3,42:1 pe card), dar aceea schimbă valoarea token-ului.

### 3.2 `.toc summary::after`, chevronul — 2,85:1

Indicator de stare deschis/închis, pe `.glass-card`, pe cele două pagini legale.

**Atenuare reală:** starea e comunicată și prin prezența sau absența
conținutului din `<details>`, nu doar prin săgeată. Nu e un indicator izolat.
Rămâne totuși sub prag ca element vizual de stare.

**Propunere:**

```css
.toc summary::after {
  border-right-color: var(--on-surface-variant);   /* #c6c6c6 → 10,06:1 */
  border-bottom-color: var(--on-surface-variant);
}
```

### 3.3 `.legal-prose a`, sublinierea — 2,06:1

**Cea mai slabă cifră din tot auditul**, mai slabă decât badge-ul.

Comentariul din `styles.css:448` spune: *„Linkurile din text se disting prin
subliniere, nu doar prin culoare."* Intenția e corectă — e chiar mecanismul cerut
de 1.4.1. Dar textul linkului e `#e5e2e1`, **identic cu textul din jur**, deci
sublinierea nu e o întărire: **e singurul lucru care identifică linkul.** Iar ea
e la `rgba(196,18,54,0.75)`, adică `#9A142F` compus, adică **2,06:1** pe card.

Un cititor cu vedere redusă nu distinge linkurile din Termeni și din Politica
de cookie — cele două pagini unde conținutul juridic depinde cel mai mult de
linkuri interne.

**Propunere, cea mai simplă din toate trei:**

```css
.legal-prose a {
  text-decoration-color: currentColor;   /* #e5e2e1 → 13,34:1 */
}
```

`currentColor` nu e o culoare nouă: e culoarea textului, deja aleasă. Bordo-ul
poate rămâne pe `:hover`, unde e întărire, nu identificare.

---

## 4. Ce s-a reparat

Toate trei, plus regula moartă. Modificările sunt **doar CSS**: niciun text de
pagină nu s-a atins, nicio valoare de token nu s-a schimbat.

| § | Unde | Ce | Contrast |
|---|---|---|---|
| 3.3 | `assets/styles.css` | `text-decoration-color: currentColor` | 2,06 → **13,34:1** |
| 3.1 | blocul `<style>`, ×27 pagini | regulă nouă `.glass-card .btn-secundar-zona { border-color: var(--outline) }` | 2,85 → **5,41:1** |
| 3.2 | `assets/styles.css` | `border-*-color: var(--on-surface-variant)` | 2,85 → **10,06:1** |
| — | `assets/styles.css` | `.price-tbc`, `__flag`, `__value` șterse | — |

### O corectură la propunerile din prima versiune a acestui audit

Propunerile scriau `var(--outline)` și `var(--on-surface-variant)` ca și cum ar
fi existat. **Nu existau.** Singura variabilă CSS din `:root` era
`--accent-edge`; restul paletei trăiește doar în `assets/tailwind.config.js`, ca
tokeni Tailwind. Scrise așa, cele două declarații ar fi fost invalide, iar
bordurile ar fi căzut pe `currentColor` — adică exact invers față de intenție.

Reparația a adăugat cele două variabile în `:root`, cu **valorile identice** din
`tailwind.config.js` (`#8e9192` și `#c6c6c6`). Nu e o culoare nouă și nu e o
valoare schimbată: sunt aceiași doi tokeni, expuși și ca variabile CSS. Fișierul
o cerea el însuși, în nota de deasupra lui `:root`: *„Variabile CSS reale, nu
doar fallback-uri: la migrarea în Elementor tokenii se mapează pe variabile
globale, iar unul care trăiește doar ca fallback într-o regulă se pierde."*

### Ce NU s-a reparat, deliberat

- **`.bg-accent` în card (2,85:1)** — rămâne „la limită", cum era clasificat.
  Butonul primar are umplutură și text alb la 8,08:1; nu depinde de bordură.
- **`.legal-prose a:hover` (2,85:1)** — la hover, sublinierea bordo e întărire,
  nu identificare. Identificarea o face acum `currentColor` în starea de bază.
- **Badge-ul (2,71:1)** — decorativ, vezi `ZONE-NOI-PLAN.md` §4.
- **Referințele la `.price-tbc` din comentarii** — rămân în `oferte.html:512`
  („Niciun .price-tbc rămas pe pagină", încă adevărat) și în comentariul din
  blocul `<style>` al celor 27 de pagini, care descrie familia de marcaje. Sunt
  în afara scopului acestei reparații.

---

## 5. Contrastul măsurat pe elementul randat

Nu calculat din CSS-ul sursă, ci citit din `getComputedStyle` într-un Chromium
real, cu Tailwind încărcat, la **360 px și 1440 px**. Identic la ambele lățimi.

| Element | Culoare randată | Fond randat | Contrast |
|---|---|---|---|
| `.legal-prose a`, subliniere, pe pagină | `rgb(229,226,225)` | `rgb(19,19,19)` | **14,42:1** |
| `.legal-prose a`, subliniere, în card | `rgb(229,226,225)` | `rgb(28,27,27)` | **13,34:1** |
| `.toc summary::after`, chevron | `rgb(198,198,198)` | `rgb(28,27,27)` | **10,06:1** |
| `.btn-secundar-zona` în `.glass-card` | `rgb(142,145,146)` | `rgb(28,27,27)` | **5,41:1** |
| `.btn-secundar-zona` în afara cardului | `rgb(196,18,54)` | `rgb(19,19,19)` | 3,09:1 |

Ultimul rând confirmă că reparația e **contextuală**: butonul secundar rămâne
bordo acolo unde bordo-ul trecea deja pragul, și devine argintiu doar pe card.
Valorile măsurate coincid cu cele calculate, până la a doua zecimală.
