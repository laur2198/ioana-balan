# `--accent-edge` pe suprafețe întunecate — audit complet

Măsurat pe `79f61be`, 19.09.2026. Acoperă **toate cele 38 de pagini HTML**: 11 în
rădăcină, 27 în `zone-mockup/`. Auditul e **doar citire** — nicio culoare, niciun
token și nicio regulă CSS nu s-au modificat în urma lui.

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
| 2b | `.btn-secundar-zona` — bordură 1px | idem, în interiorul unui card | card `#1c1b1b` | **2,85:1** | **NECONFORMITATE** |
| 3 | `.toc summary::after` — chevron 2px | indicator deschis/închis, **stare** | card `#1c1b1b` | **2,85:1** | **NECONFORMITATE** |
| 4 | `.legal-prose a` — `text-decoration-color` | sublinierea care identifică linkul | card `#1c1b1b` | **2,06:1** | **NECONFORMITATE** |
| 4b | `.legal-prose a:hover` — `text-decoration-color` | idem, la hover | card `#1c1b1b` | **2,85:1** | parte din #4 |
| 5 | `.video-card__play` — `border-color` la hover/focus | întărire vizuală | `#A01028` | 1,34:1 | conform — vezi §3.0 |
| 6 | `.zona-badge` — bordură 1px | etichetă de zonă, **decorativ** | badge `#20201f` | 2,71:1 | fără prag |
| 7 | `.zona-divider` — gradient | separator, **decorativ** | pagină `#131313` | 3,09:1 | fără prag |
| 8 | `.zona-gem` — bordură romb | ornament în `.motif-rule`, **decorativ** | pagină / card | 3,09 / 2,85:1 | fără prag |
| 9 | `.legal-tbc` — bordură 2px punctată | marcaj de valoare lipsă, **decorativ** | propriu `#331319` | 2,79:1 | fără prag |
| 10 | `.answer-tbc` — bordură 2px punctată | marcaj de răspuns neconfirmat, **decorativ** | propriu `#331319` | 2,79:1 | fără prag |
| 11 | `.legal-draft-banner` — bordură | casetă „document în lucru", **decorativ** | propriu `#2C1318` | 2,87:1 | fără prag |
| 12 | `.price-tbc` — bordură 2px punctată | **regulă moartă** | — | — | 0 apariții în HTML |

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

## 4. Ce nu s-a făcut, și de ce

**Nimic nu s-a reparat.** Cele trei propuneri sunt scrise, nu aplicate. Toate
trei ating `assets/styles.css`, care e partajat de toate cele 38 de pagini, iar
o modificare acolo se vede pe tot site-ul deodată — inclusiv pe cele 11 pagini
din rădăcină, care sunt în contractul de bază.

Ordinea recomandată, dacă se decid:

1. **§3.3, sublinierea legală.** Cea mai gravă, cea mai ieftină, zero risc
   vizual — `currentColor` nu adaugă nimic în paletă.
2. **§3.1, butonul secundar.** Cea mai vizibilă ca suprafață: 73 de instanțe.
   De decis împreună cu P1/P2 din `ZONE-NOI-PLAN.md` §4, pentru că P2 le-ar
   rezolva pe amândouă cu o singură schimbare de token.
3. **§3.2, chevronul.** Cea mai mică, și singura cu o atenuare reală.

Separat: **`.price-tbc` e o regulă moartă** — 0 apariții în HTML, pe toate cele
38 de pagini. Se șterge din `styles.css` la curățenia de dinaintea migrării,
odată cu celelalte marcaje de prototip.
