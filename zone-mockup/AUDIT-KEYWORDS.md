# Audit de cuvinte cheie — 11 pagini existente față de 20 noi

Data: 2026-09-16. Doar constatări: nicio pagină nu a fost modificată pentru acest audit.

**Reproducere:** `python3 zone-mockup/verify/audit_keywords.py` (câmpuri, JSON) și
`python3 zone-mockup/verify/audit_keywords.py --matrice` (non-duplicare 20 × 11).
Scriptul refolosește funcțiile din `bag_of_words.py` și `non_duplicare.py`, deci
toponimele, plierea diacriticelor și pragurile sunt aceleași cu verificările existente.

**Metodă pentru „termen targetat”.** Un termen e targetat de o pagină dacă apare în
title sau H1, în ordine, cu cel mult două cuvinte între elemente („formația de
nuntă” contează pentru „formatie nunta”). Apariția doar în meta, JSON-LD sau
headinguri e marcată *secundar*. Corpul paginii a fost scanat separat: nu schimbă
niciun verdict, dar e citat unde contează.

---

## Pe scurt

1. **„formatie nunta” e targetat de 4 pagini vechi, toate cu București:** `index`
   (title, H1, meta, JSON-LD), `galerie` (title), `blog` și `articol` (meta, JSON-LD).
   Nicio pagină nouă nu îl atinge.
2. **`index` și `oferte` nu se bat pe „formatie nunta”:** `oferte` nu are termenul
   în title sau H1. Se suprapun totuși prin **FAQ**: două întrebări și răspunsuri identice
   cu `index`, iar cu `faq.html` cinci.
3. **„oferta formatie nunta” nu e targetat de nicio pagină**, nici măcar de `oferte`:
   cuvântul „ofertă” nu apare în title, H1 sau în vreun heading.
4. **„formatie folclor si manele” nu e targetat de nicio pagină.** `folclor-si-manele`
   are „folclor și manele”, dar niciun „formație” în câmpurile SEO sau în headinguri.
5. **„recomandari formatii nunta” și „top formatii nunta”: nicio pagină nu încearcă.**
6. **Bag-of-words pe paginile vechi:** 4 din 11 încalcă regula (`index`, `galerie`,
   `blog`, `articol`), în 11 câmpuri în total.
7. **Non-duplicare 20 × 11:** 20 de potriviri peste 85%, toate din **două recenzii Google
   citate identic** pe `zona-brasov` și `zona-constanta` și preluate de pe `index`.
   Niciun text propriu nu trece de 70%.

---

## A. Canibalizare

### Pe termenii clientului

| Termen | Pagini care îl targetează | Canibalizare? |
|---|---|---|
| formatie nunta / formatii nunta | `index` (title, H1, meta, JSON-LD, H2) · `galerie` (title) · `blog` (meta, JSON-LD, H2) · `articol` (meta, JSON-LD) | **Da, 4 pagini.** Toate patru au și „București”, deci se bat pe aceeași variantă locală, „formație nuntă București”. `galerie` e cea mai serioasă, pentru că are termenul în title, la fel ca `index`. |
| oferta formatie nunta | — | Nu. Neacoperit (vezi B). |
| recomandari formatii nunta | — | Nu. Neacoperit (vezi B). |
| top formatii nunta | — | Nu. Neacoperit (vezi B). |
| formatie folclor si manele | — | Nu. Neacoperit (vezi B). |
| formatie muzica de petrecere | `zona-brasov` (title) · `zona-constanta` (title) · `galerie` (meta, JSON-LD) · `index` (title și H1 au ambele părți, dar nu alăturate) | **Parțial.** Brașov și Constanța au toponime diferite, deci nu se bat între ele. `galerie` pune „formația de muzică populară și de petrecere” lângă Brașov, Ploiești, Craiova și Pitești, în meta, și se suprapune cu 4 pagini de zonă (vezi C). Varianta fără toponim nu are un proprietar clar. |

### `index.html` față de `oferte.html` pe „formatie nunta”

**Pe title și H1 nu se bat.** `oferte` are title-ul „Pachete și Prețuri 2026-2027” și
H1-ul „Pachete și prețuri pentru nuntă și botez”. „Formație” apare numai în meta și
JSON-LD („formație live”), la distanță de „nuntă”. Asta e un semnal slab, nu o țintire.

Suprapunerea reală e în altă parte, și ține de paginile vechi, nu de munca pe cele noi:

- **Intenția „pachete/prețuri”:** `index` are H2 „Pachete pentru 2026–2027”, iar
  `oferte` are H1 „Pachete și prețuri…”.
- **FAQ duplicat:** două întrebări sunt identice pe `index`, `oferte` și `faq`,
  împreună cu răspunsurile: „Prețul unei formații pentru 2026-2027?” și „Cum rezerv
  data — avans și contract?”. Între `oferte` și `faq` se repetă **cinci** perechi
  întrebare-răspuns, identice caracter cu caracter. Răspunsurile stau într-un `<div>`,
  pe care `non_duplicare.py` nu îl citește (vezi E), deci au fost comparate separat.
- **Headingul `faq` = H2 pe `index`:** „Ce ne întrebați cel mai des” e H1 pe `faq` și
  H2 pe `index`.

### Headinguri comune între vechi și noi

Singurul heading identic între o pagină veche și una nouă este „Verificați dacă data este
liberă”, H2 pe `oferte` și pe `zona-brasov`. Separat, „Pachete și prețuri” e H2 pe
`zona-brasov`, `zona-constanta` și `zona-giurgiu`, iar pe `oferte` e începutul H1-ului.
Niciunul nu e termen din lista clientului.

---

## B. Termeni neacoperiți

| Termen | Stare | Detalii |
|---|---|---|
| oferta formatie nunta | **Neacoperit** | Pagina din maparea intenționată, `oferte`, nu conține „ofertă” în title, H1 sau în vreun heading. În corp apare de 4 ori, ca verb/substantiv funcțional („oferta pentru configurația…”). |
| recomandari formatii nunta | **Neacoperit; nicio pagină nu încearcă** | „Recomand” apare doar **în citatul unei recenzii** („Recomand 🙌🏻 Formația a fost super…”, pe `index` și `zona-constanta`) și în sintagma „termenul recomandat”, pe `nunta` și `corporate`. Niciuna nu e targetare. |
| top formatii nunta | **Neacoperit; nicio pagină nu încearcă** | Scanarea după tokenul „top” găsește 5 apariții pe `zona-arges`. Toate sunt din „Topoloveni”, deci fals pozitive. |
| formatie folclor si manele | **Neacoperit** | Pe `folclor-si-manele`, „folclor și manele” apare în title și H1, dar „formație” lipsește din title, H1, meta, JSON-LD, H2 și H3 (în corp apare de 2 ori). Nicio pagină veche nu conține „manele”. |

**Cel mai aproape de intenția de tip listicle:** H2-ul de teaser de pe `blog.html`,
„Cum să alegi formația de nuntă perfectă în 2026”. E un ghid de alegere, nu un
clasament sau o listă de recomandări, deci nu încearcă „top” sau „recomandări”. Îl
semnalez pentru că e singurul text de pe site care atinge intenția comparativă.

**Pe maparea intenționată:**

- **Termen principal:** `index` își îndeplinește rolul. `oferte` nu îl îndeplinește pe al său („formatie nunta” și „oferta formatie nunta”).
- **Zone:** 2 din 12 pagini au „formație” în title (Brașov și Constanța), 0 din 12 în H1. Hub-ul nu conține niciun termen din listă.
- **Petrecere:** `folclor-si-manele` nu conține „formație” în niciun câmp, deci niciunul dintre cei doi termeni atribuiți nu e targetat integral.

**Tensiune structurală pe zone.** 10 din 12 title-uri și toate cele 12 H1-uri conțin
„nunți” și un toponim. Dacă se adaugă „formație” în aceste câmpuri, regula bag-of-words e
încălcată automat. Brașov și Constanța sunt singurele cu „Formație” în title și singurele
fără „nunți” acolo. Title-urile de zonă pot deci purta „formație” sau „nunți”, nu pe
amândouă.

---

## C. `index` / `oferte` față de paginile de zonă

Căutat: „muzică de petrecere [oraș]” sau „folclor [oraș]” în title, H1, H2 și H3, cu
aceleași toponime ca `bag_of_words.py`.

| Pagină | Câmp | Text | Suprapunere cu zonele |
|---|---|---|---|
| `index` | title | Formație Nuntă **București** Premium & **Muzică de Petrecere** | **Parțială, cu `zona-ilfov`.** București nu are pagină de zonă, dar title-ul Ilfov se termină cu „…Muzică de Petrecere în Ilfov \| Nunți și Botezuri **lângă București**”. |
| `index` | H1 | Formație Nuntă **București** Premium: **Muzică de Petrecere** Autentică | Idem |
| `index` | H3 | Cântați și în afara Bucureștiului? | Nu (nu conține termen) |
| `oferte` | title, H1, H2, H3 | — | **Nu.** Niciun toponim în headinguri. Singura listă de orașe (București, Ploiești, Brașov, Craiova, Pitești) e un paragraf din secțiunea „Acoperire”, fără „muzică de petrecere” sau „folclor”. |

**Nicio pagină de zonă nu e dublată în title, H1 sau headinguri de `index` sau `oferte`**
pe toponimul ei (Ploiești, Pitești, Brașov, Craiova, Constanța etc.).

**Dincolo de `index` și `oferte`, tot pe paginile vechi:**

- `galerie`, meta și JSON-LD: „…formația de muzică populară și de petrecere din București,
  **Ploiești, Brașov, Craiova și Pitești**”. Se suprapune în meta cu `zona-prahova`,
  `zona-brasov`, `zona-dolj` și `zona-arges`. Nu apare în title sau H1.
- `contact`, meta: „rezervări nunți … în București, Ploiești, Brașov, Craiova și Pitești”,
  fără „muzică de petrecere” sau „folclor”. Suprapunere doar geografică.

---

## D. Bag-of-words pe cele 11 pagini vechi

Aceeași funcție ca `bag_of_words.py`: după eliminarea prepozițiilor, câmpul nu are voie
să conțină simultan un token `formati*`, un token `nunt*` și un toponim.

| Pagină | title | H1 | meta | JSON-LD | slug | Toponim |
|---|---|---|---|---|---|---|
| `index` | ✗ | ✗ | ✗ | ✗ | ok | București |
| `galerie` | ✗ | ok | ✗ | ✗ | ok | București (title); București, Ploiești, Brașov, Craiova, Pitești (meta, JSON-LD) |
| `blog` | ok | ok | ✗ | ✗ | ok | București |
| `articol` | ok | ok | ✗ | ✗ | ok | București |
| `oferte` | ok | ok | ok | ok | ok | — (formație + nuntă fără toponim) |
| `contact` | ok | ok | ok | ok | ok | — (nunți + 5 orașe fără formație) |
| `despre`, `discografie`, `faq`, `termeni-si-conditii`, `politica-cookie` | ok | ok | ok | ok | ok | — |

**4 pagini și 11 câmpuri în încălcare.** Pe `index`, încălcarea e chiar termenul-țintă
din JSON-LD („Formație nuntă București premium”), deci e consecventă cu rolul paginii. Pe
`galerie`, `blog` și `articol`, aceeași combinație concurează cu `index` (vezi A). Nu am
reparat nimic: `index` și `oferte` țin de contractul de bază al Fazei 3.

---

## E. Non-duplicare: 20 noi × 11 vechi

**Acoperire:** 220 de perechi (fiecare pagină nouă față de fiecare pagină veche), în două
treceri (text brut și text cu toponime mascate), cu cele trei metrici din
`non_duplicare.py` (paragraf, propoziție, shingle-6). Total: 440 de comparații.

**Rezultat: 20 de potriviri peste 85%, în 2 perechi.**

| Pagină nouă | Pagină veche | Treceri | Metrici | Text |
|---|---|---|---|---|
| `zona-brasov` | `index` | brut + mascat | paragraf 100%, propoziție 100% (×3), shingle-6 100% | Recenzie Google (Alexandru Dimov): „Ne-au oferit o nunta de nota 10. Pe lângă show-ul unic, sunt niste oameni minunați. I-am simțit aproape de noi și cu sufletul, nu doar artistic. Mulțumim!” |
| `zona-constanta` | `index` | brut + mascat | paragraf 100%, propoziție 100% (×3), shingle-6 100% | Recenzie Google: „Recomand 🙌🏻 Formația a fost super la nunta noastră! Silvia are o voce foarte frumoasă, Ioana ne-a cucerit pe toți – superba – iar Ionuț a fost de nota 10, a ținut atmosfera sus toată seara. Ne-am simțit minunat și va mulțumim că ati contribuit la o petrecere așa cum ne-am dorit! 🫶🏻” |

Ambele sunt **citate de la terți, nu text propriu**. Fiecare apare de 10 ori în raport:
5 metrici × 2 treceri.

**Limita extracției și a doua rulare.** `content_blocks()` din `_common.py` citește doar
`p`, `li`, `h1`–`h4`, `blockquote`, `figcaption`, `dd` și `dt`. Pe paginile noi scapă
3–4% din text (butoane și etichete). Pe cele vechi scapă mult mai mult, pentru că
răspunsurile FAQ și unele carduri stau direct în `<div>`: `faq` 70%, `contact` 53%,
`galerie` 45%, `index` 30%, `oferte` 27%, `blog` 20%, `discografie` 13%, `termeni` 9%.
Matricea a fost deci rulată a doua oară, cu textul liber din `div`, `summary`, `a` și
ceilalți containeri (de atunci, `content_blocks()` a fost reparată și flagul provizoriu
`--complet` a fost scos). **Rezultatul e identic:** aceleași 20 de
potriviri și aceleași maxime sub prag. Singura pereche nouă în top 15 e `zona-brasov` ↔
`faq`, cu 60% la propoziție.

**Sub prag, cele mai mari maxime pe pereche** (identice brut și mascat):

| Pereche | Maxim | Ce se potrivește |
|---|---|---|
| `formatia` ↔ `oferte` | 70,0% propoziție | „Ioana Balan cântă muzica populară și pe cea de petrecere.” ↔ „Ioana Balan este solistă de muzică populară și de petrecere.” |
| `zona-brasov` ↔ `oferte` | 69,6% propoziție | „Cu sonorizare proprie, inclusă în pachet și dimensionată după sală și numărul de invitați.” ↔ „Sonorizare profesională, dimensionată după sală și numărul de invitați” |
| `zona-brasov` ↔ `discografie` | 55,6% paragraf | H1 Brașov ↔ „Lansat în 2025 • Muzică de petrecere și folclor” |
| `botez` ↔ `oferte` | 55,6% propoziție | „Un interpret acoperă și muzica populară, și pe cea ușoară.” ↔ „Un interpret de muzică populară și de petrecere” |
| `zona-giurgiu` ↔ `oferte` | 54,5% propoziție | fraza despre sonorizare dimensionată după sală |

**Niciun text propriu nu intră în intervalul 75–85%.** Mascarea toponimelor nu ridică
niciun scor, deci nu există un șablon comun ascuns sub nume de locuri.

---

## Decizii de luat cu clientul

1. **Cine deține „formație nuntă (București)”?** Maparea spune `index`. Același termen
   stă însă și în title-ul `galerie` și în meta/JSON-LD pe `blog` și `articol`, toate
   pagini din contractul de bază. Rămân așa sau se aliniază, ca schimbare de scope?
2. **Rolul `oferte.html`.** Maparea îi atribuie „formatie nunta” și „oferta formatie
   nunta”, dar pagina nu conține niciunul în title sau H1. Dacă i se atribuie, `index` și
   `oferte` vor ținti același termen, deci trebuie ales **un singur** proprietar pentru
   „formatie nunta”. Varianta naturală: `index` pe „formatie nunta”, `oferte` pe „oferta
   formatie nunta”.
3. **FAQ-ul triplat.** Cinci întrebări cu răspunsuri identice pe `oferte` și `faq`, două
   dintre ele și pe `index`. Rămâne conținut dublat sau se păstrează pe o singură pagină?
4. **„Formație” sau „nunți” în title-urile de zonă.** Sub regula bag-of-words nu pot
   coexista. Acum 2 pagini au „formație” și 10 au „nunți”. Care e mai valoros pentru
   client?
5. **„formatie folclor si manele”.** `folclor-si-manele` are „folclor și manele” fără
   „formație”. Se acceptă forma fără „formație” sau se adaugă? Pagina e nouă, deci
   schimbarea nu iese din scope.
6. **„formatie muzica de petrecere”, fără toponim.** Nu are un proprietar clar: `index`
   îl atinge doar parțial, `galerie` doar în meta, iar `folclor-si-manele`, pagina din
   mapare, nu îl conține. Care pagină îl deține?
7. **„recomandari formatii nunta” și „top formatii nunta”.** Confirmare că nu se
   urmăresc pe site, ci eventual în afara lui (articole de tip „top” de pe alte site-uri,
   directoare de furnizori).
8. **Recenziile de pe paginile de zonă.** Cele două recenzii de pe `zona-brasov` și
   `zona-constanta` sunt aceleași ca pe `index`. Plasate pe o pagină de județ, sugerează
   că evenimentul a avut loc acolo. Clientul confirmă că recenziile sunt de la
   evenimente din Brașov și Constanța, sau se înlocuiesc cu recenzii locale?
   Separat, recenzia de pe Constanța numește o „Silvia” cu „o voce foarte frumoasă”,
   alături de Ioana și Ionuț. De confirmat cine e, înainte ca textul să ruleze pe mai
   multe pagini.

---

### Sinteză

| # | Pagină | Tip | Termen din lista clientului | Bag-of-words (formație + nunt* + toponim) |
|---|---|---|---|---|
| 1 | `index.html` | veche | **formatie nunta** — title, H1, meta, JSON-LD, H2 („Rezervă Formație Nuntă”). Parțial „muzică de petrecere” în title/H1, fără „formație” alăturat | **ÎNCĂLCARE** — title, h1, meta, jsonld |
| 2 | `oferte.html` | veche | niciunul — „ofertă” lipsește din title/H1/headinguri; „formație” și „nuntă” apar doar separat, în meta și JSON-LD | ok |
| 3 | `despre.html` | veche | niciunul | ok |
| 4 | `galerie.html` | veche | **formatie nunta** — title („Formație Nuntă București”); **formatie muzica de petrecere** — meta și JSON-LD („formația de muzică populară și de petrecere din București, Ploiești, Brașov, Craiova și Pitești”) | **ÎNCĂLCARE** — title, meta, jsonld |
| 5 | `discografie.html` | veche | niciunul („Muzică Populară și de Petrecere” în title, fără „formație”) | ok |
| 6 | `contact.html` | veche | niciunul | ok |
| 7 | `blog.html` | veche | **formatie nunta**, secundar — meta, JSON-LD, H2 de teaser („formația de nuntă”) | **ÎNCĂLCARE** — meta, jsonld |
| 8 | `articol.html` | veche | **formatie nunta**, secundar — meta și JSON-LD („formații de nuntă în București”), pe un articol despre lumini de scenă | **ÎNCĂLCARE** — meta, jsonld |
| 9 | `faq.html` | veche | niciunul | ok |
| 10 | `termeni-si-conditii.html` | veche | niciunul | ok |
| 11 | `politica-cookie.html` | veche | niciunul | ok |
| 12 | `zona-arges.html` | nouă | parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor” | ok |
| 13 | `zona-brasov.html` | nouă | **formatie muzica de petrecere [zonă]** — title. „folclor” în title, separat | ok |
| 14 | `zona-buzau.html` | nouă | parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor” | ok |
| 15 | `zona-calarasi.html` | nouă | parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor” | ok |
| 16 | `zona-constanta.html` | nouă | **formatie muzica de petrecere [zonă]** — title. „folclor” în title, separat | ok |
| 17 | `zona-dambovita.html` | nouă | parțial: „folclor [zonă]” în title, fără „formație”; fără „muzică de petrecere” în title | ok |
| 18 | `zona-dolj.html` | nouă | parțial: „muzică … de petrecere [zonă]” în title („Muzică Oltenească și de Petrecere”), fără „formație” | ok |
| 19 | `zona-giurgiu.html` | nouă | parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație” | ok |
| 20 | `zona-ialomita.html` | nouă | parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație” | ok |
| 21 | `zona-ilfov.html` | nouă | parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație” | ok |
| 22 | `zona-prahova.html` | nouă | parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație” | ok |
| 23 | `zona-teleorman.html` | nouă | parțial: „folclor [zonă]” în title, fără „formație”; fără „muzică de petrecere” în title | ok |
| 24 | `zone.html` | nouă | niciunul | ok |
| 25 | `repertoriu.html` | nouă | niciunul din lista clientului (cluster: repertoriu) | ok |
| 26 | `formatia.html` | nouă | niciunul din lista clientului (cluster: componență; „formație” fără „nuntă”) | ok |
| 27 | `folclor-si-manele.html` | nouă | parțial: „folclor și manele” în title/H1, **fără „formație”** în niciun câmp SEO sau heading; „muzică de petrecere” doar într-un H3 | ok |
| 28 | `nunta.html` | nouă | niciunul („nuntă” fără „formație”; intenție de ghid) | ok |
| 29 | `botez.html` | nouă | niciunul | ok |
| 30 | `eveniment-privat.html` | nouă | niciunul | ok |
| 31 | `corporate.html` | nouă | niciunul | ok |

### Câmpuri și headinguri, per pagină

Textul e copiat din markup, după normalizarea spațiilor. „—” = câmp absent.

#### 1. `index.html` (veche)

- **title:** Ioana Balan | Formație Nuntă București Premium & Muzică de Petrecere
- **h1:** Formație Nuntă București Premium: Muzică de Petrecere Autentică
- **meta description:** Ioana Balan - Formație nuntă București premium. Muzică de petrecere autentică, solistă nuntă cu repertoriu variat pentru nunți, botezuri și evenimente corporate 2026-2027.
- **JSON-LD description:** Formație nuntă București premium — muzică populară autentică și de petrecere pentru nunți, botezuri și evenimente corporate.
- **Termen targetat:** **formatie nunta** — title, H1, meta, JSON-LD, H2 („Rezervă Formație Nuntă”). Parțial „muzică de petrecere” în title/H1, fără „formație” alăturat
- **Bag-of-words:** **ÎNCĂLCARE** — title, h1, meta, jsonld <sub>(formație·nunt*·toponime: title: 1·1·1 ✗; h1: 1·1·1 ✗; meta: 1·3·1 ✗; JSON-LD: 1·2·1 ✗)</sub>
- **H2** (7):
  - Muzică pentru nuntă, botez și corporate
  - Pachete pentru 2026–2027
  - Peste 15 ani pe scenă
  - Vezi cum arată un eveniment
  - Ce Spun Mirii și Gazdele
  - Ce ne întrebați cel mai des
  - Rezervă Formație Nuntă
- **H3** (6):
  - Muzică Nuntă
  - Muzică Botez
  - Corporate
  - Prețul unei formații pentru 2026-2027?
  - Cântați și în afara Bucureștiului?
  - Cum rezerv data — avans și contract?

#### 2. `oferte.html` (veche)

- **title:** Pachete și Prețuri 2026-2027 | Ioana Balan
- **h1:** Pachete și prețuri pentru nuntă și botez
- **meta description:** Pachete de muzică pentru nuntă și botez cu solista Ioana Balan: formație live, interpreți, DJ și producție tehnică. Prețuri distincte pentru sâmbătă și duminică.
- **JSON-LD description:** Pachete pentru nuntă și botez cu solista Ioana Balan: formație live, interpreți, DJ/MC, sonorizare și producție tehnică, pentru evenimente din 2026 și 2027.
- **Termen targetat:** niciunul — „ofertă” lipsește din title/H1/headinguri; „formație” și „nuntă” apar doar separat, în meta și JSON-LD
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: h1: 0·1·0; meta: 1·1·0; JSON-LD: 1·1·0)</sub>
- **H2** (5):
  - Condiții comerciale
  - Patru pachete, pentru nuntă și pentru botez
  - Acoperire
  - Preț, rezervare și contract
  - Verificați dacă data este liberă
- **H3** (9):
  - Pachet Standard
  - Pachet Premium
  - Pachet Standard
  - Pachet Premium
  - Prețul unei formații pentru 2026-2027?
  - Cum rezerv data — avans și contract?
  - Cât este avansul și când se achită restul?
  - Cu cât timp înainte ar trebui să vă contactez?
  - Ce se întâmplă dacă trebuie să amân evenimentul?

#### 3. `despre.html` (veche)

- **title:** Despre mine | Ioana Balan
- **h1:** Despre mine
- **meta description:** Ioana Balan povestește de unde vine dragostea ei pentru folclorul românesc, cine i-a îndrumat primii pași în muzica populară și cum arată munca ei de zi cu zi.
- **JSON-LD description:** —
- **Termen targetat:** niciunul
- **Bag-of-words:** ok
- **H2** (3):
  - Rădăcini
  - Primii pași
  - Hai să ne cunoaștem
- **H3** (0):
  - —

#### 4. `galerie.html` (veche)

- **title:** Galerie | Ioana Balan — Formație Nuntă București
- **h1:** Galerie de Spectacole
- **meta description:** Galerie foto și video Ioana Balan: momente live de la nunți și evenimente cu formația de muzică populară și de petrecere din București, Ploiești, Brașov, Craiova și Pitești.
- **JSON-LD description:** Galerie foto și video Ioana Balan: momente live de la nunți și evenimente cu formația de muzică populară și de petrecere din București, Ploiești, Brașov, Craiova și Pitești.
- **Termen targetat:** **formatie nunta** — title („Formație Nuntă București”); **formatie muzica de petrecere** — meta și JSON-LD („formația de muzică populară și de petrecere din București, Ploiești, Brașov, Craiova și Pitești”)
- **Bag-of-words:** **ÎNCĂLCARE** — title, meta, jsonld <sub>(formație·nunt*·toponime: title: 1·1·1 ✗; meta: 1·1·5 ✗; JSON-LD: 1·1·5 ✗)</sub>
- **H2** (2):
  - Cum arată un eveniment
  - Esența Tradiției în Imagini.
- **H3** (0):
  - —

#### 5. `discografie.html` (veche)

- **title:** Discografie | IOANA BALAN - Muzică Populară și de Petrecere
- **h1:** Hai să nu ne mai mințim
- **meta description:** Explorează discografia completă a artistei Ioana Balan. De la noul album 'Hai să nu ne mai mințim' la colecțiile de arhivă 'Glasul Inimii' și 'Rădăcini'.
- **JSON-LD description:** —
- **Termen targetat:** niciunul („Muzică Populară și de Petrecere” în title, fără „formație”)
- **Bag-of-words:** ok
- **H2** (3):
  - Melodii noi Ioana Balan
  - Arhiva Sonoră Ioana Balan
  - Îți place ce auzi? Rezervă data ta.
- **H3** (2):
  - Glasul Inimii
  - Rădăcini

#### 6. `contact.html` (veche)

- **title:** Contact Ioana Balan | Rezervări Evenimente și Colaborări Muzicale
- **h1:** Rezervări și Contact Ioana Balan
- **meta description:** Contactați-o pe Ioana Balan pentru rezervări nunți, evenimente corporate și spectacole live în București, Ploiești, Brașov, Craiova și Pitești. Consultanță muzicală gratuită.
- **JSON-LD description:** Interpretă profesionistă de muzică populară și de petrecere, disponibilă pentru evenimente private și corporate în toată România.
- **Termen targetat:** niciunul
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: meta: 0·1·5; JSON-LD: 0·0·1)</sub>
- **H2** (1):
  - Cere ofertă personalizată
- **H3** (0):
  - —

#### 7. `blog.html` (veche)

- **title:** Blog | Ioana Balan - Sfaturi și Inspirație pentru Evenimente Memorabile
- **h1:** Sfaturi și Inspirație pentru Evenimente Memorabile
- **meta description:** Blog Ioana Balan: sfaturi pentru nunți și botezuri — cum alegi formația de nuntă în București, repertoriu de muzică populară și idei pentru evenimente memorabile.
- **JSON-LD description:** Blog Ioana Balan: sfaturi pentru nunți și botezuri — cum alegi formația de nuntă în București, repertoriu de muzică populară și idei pentru evenimente memorabile.
- **Termen targetat:** **formatie nunta**, secundar — meta, JSON-LD, H2 de teaser („formația de nuntă”)
- **Bag-of-words:** **ÎNCĂLCARE** — meta, jsonld <sub>(formație·nunt*·toponime: meta: 1·2·1 ✗; JSON-LD: 1·2·1 ✗)</sub>
- **H2** (4):
  - Cum să alegi formația de nuntă perfectă în 2026
  - Muzica populară vs. Muzica ușoară la botez
  - Repertoriul de muzica populara nunta: Tendințe actuale
  - Cum transformi un eveniment privat într-un spectacol premium
- **H3** (2):
  - Primește Noutăți
  - Tag-uri SEO

#### 8. `articol.html` (veche)

- **title:** Importanța luminilor de scenă pentru show-ul formației | Ioana Balan
- **h1:** Importanța luminilor de scenă pentru show-ul formației
- **meta description:** Importanța luminilor de scenă pentru show-ul unei formații de nuntă în București. Sfaturi de la Ioana Balan, muzică populară și de petrecere pentru evenimente.
- **JSON-LD description:** Importanța luminilor de scenă pentru show-ul unei formații de nuntă în București. Sfaturi de la Ioana Balan, muzică populară și de petrecere pentru evenimente.
- **Termen targetat:** **formatie nunta**, secundar — meta și JSON-LD („formații de nuntă în București”), pe un articol despre lumini de scenă
- **Bag-of-words:** **ÎNCĂLCARE** — meta, jsonld <sub>(formație·nunt*·toponime: title: 1·0·0; h1: 1·0·0; meta: 1·1·1 ✗; JSON-LD: 1·1·1 ✗)</sub>
- **H2** (3):
  - Atmosfera și Dinamica Vizuală
  - Profesionalismul din Spatele pupitrului
  - Plănuiți un eveniment?
- **H3** (1):
  - "Lumina nu doar luminează, ea transformă spațiul într-o experiență emoțională."

#### 9. `faq.html` (veche)

- **title:** Întrebări frecvente | Ioana Balan
- **h1:** Ce ne întrebați cel mai des
- **meta description:** Răspunsuri despre rezervare și contract, programul artistic, cerințele tehnice ale locației, deplasare și prețuri, pentru nunți, botezuri și evenimente corporate cu Ioana Balan.
- **JSON-LD description:** —
- **Termen targetat:** niciunul
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: meta: 0·1·0)</sub>
- **H2** (6):
  - Preț
  - Rezervare și contract
  - Prestația
  - Tehnic și locație
  - Deplasare
  - Nu ați găsit răspunsul?
- **H3** (17):
  - Prețul unei formații pentru 2026-2027?
  - Cum rezerv data — avans și contract?
  - Cât este avansul și când se achită restul?
  - Ce se întâmplă dacă trebuie să amân evenimentul?
  - Cu cât timp înainte ar trebui să vă contactez?
  - Ce tipuri de evenimente acoperă Ioana Balan?
  - Cât durează programul?
  - Pot cere o piesă anume pentru un moment special?
  - Cântați și muzică ușoară, sau doar populară?
  - Ce se întâmplă în pauzele formației?
  - Ce echipament aduceți și ce trebuie să asigure locația?
  - De cât spațiu aveți nevoie pentru scenă?
  - Cântați și la evenimente în aer liber?
  - Aveți nevoie de masă pentru formație?
  - Cântați și în afara Bucureștiului?
  - Cum se calculează costul deplasării?
  - Ce se întâmplă la distanțe mari, unde e nevoie de cazare?

#### 10. `termeni-si-conditii.html` (veche)

- **title:** Termeni și condiții | Ioana Balan
- **h1:** Termeni și condiții
- **meta description:** Condițiile de utilizare a site-ului ioana-balan.ro: identificarea operatorului, rezervarea evenimentelor, drepturi de autor, limitarea răspunderii și prelucrarea datelor cu caracter personal.
- **JSON-LD description:** —
- **Termen targetat:** niciunul
- **Bag-of-words:** ok
- **H2** (16):
  - 1. Identificarea operatorului
  - 2. Obiectul site-ului
  - 3. Acceptarea termenilor
  - 4. Informațiile publicate. Prețuri
  - 5. Rezervarea și încheierea contractului
  - 6. Deplasarea
  - 7. Modificarea și anularea rezervării
  - 8. Drepturi de proprietate intelectuală
  - 9. Materiale audio-video de la evenimente
  - 10. Limitarea răspunderii
  - 11. Linkuri către site-uri terțe
  - 12. Prelucrarea datelor cu caracter personal
  - 13. Cookie-uri
  - 14. Soluționarea litigiilor
  - 15. Modificarea termenilor
  - 16. Contact
- **H3** (7):
  - 12.1 Operatorul
  - 12.2 Ce date prelucrăm, în ce scop și în ce temei
  - 12.3 Cui transmitem datele
  - 12.4 Transferuri în afara Spațiului Economic European
  - 12.5 Drepturile dumneavoastră
  - 12.6 Dreptul de a depune plângere
  - 12.7 Caracterul obligatoriu al furnizării datelor

#### 11. `politica-cookie.html` (veche)

- **title:** Politica de cookie-uri | Ioana Balan
- **h1:** Politica de cookie-uri
- **meta description:** Cum folosește site-ul ioana-balan.ro modulele cookie și tehnologiile similare de stocare locală: temeiul legal, conținutul încorporat de la terți și controlul setărilor din browser.
- **JSON-LD description:** —
- **Termen targetat:** niciunul
- **Bag-of-words:** ok
- **H2** (9):
  - 1. Ce sunt cookie-urile
  - 2. Temeiul legal
  - 3. Ce cookie-uri folosim
  - 4. Conținut încorporat de la terți
  - 5. Cum vă puteți retrage consimțământul
  - 6. Cum puteți controla cookie-urile din browser
  - 7. Drepturile dumneavoastră
  - 8. Modificarea acestei politici
  - 9. Contact
- **H3** (3):
  - 3.1 Cookie-uri strict necesare
  - 3.2 Cookie-uri de analiză
  - 3.3 Cookie-uri de publicitate

#### 12. `zona-arges.html` (nouă)

- **title:** Brâu de Muscel și Muzică de Petrecere în Pitești și Argeș | Nunți, Botezuri | Ioana Balan
- **h1:** Brâuri de Muscel și sârbe de câmpie, pentru nunți și botezuri în Argeș
- **meta description:** Brâuri de Muscel, sârbe și muzică de petrecere live la nunți și botezuri în Pitești, Câmpulung, Curtea de Argeș și în tot județul Argeș. Sonorizare proprie.
- **JSON-LD description:** Brâuri de Muscel, sârbe și muzică de petrecere live pentru nunți, botezuri și evenimente corporate în Pitești, Câmpulung, Curtea de Argeș și în județul Argeș, cu sonorizare proprie.
- **Termen targetat:** parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·3; h1: 0·1·2; meta: 0·1·4; JSON-LD: 0·1·4; slug: 0·0·1)</sub>
- **H2** (6):
  - Opt localități, din jurul Piteștiului până în Muscel
  - Muscel, Argeș și granița cu Oltenia
  - Autostradă până la Pitești, deal după
  - Un pachet, două segmente de drum
  - Muscel, autostradă, localitate: întrebări practice
  - Pitești, Câmpulung sau Curtea de Argeș
- **H3** (6):
  - Spre vest, primele jocuri oltenești
  - Nunta e la Câmpulung. Poate solista să poarte un costum de Muscel?
  - Ce se întâmplă dacă, în ziua nunții, A1 e blocată de un accident?
  - Încă alegem între o sală în Pitești și una la Curtea de Argeș. Putem bloca data până decidem?
  - Putem face o probă de sunet cu o zi înainte, în sala din Pitești?
  - Botezul e la prânz, la Topoloveni. Ajută că e un eveniment de zi?

#### 13. `zona-brasov.html` (nouă)

- **title:** Formație Muzică de Petrecere Brașov | Folclor Live | Ioana Balan
- **h1:** Muzică de petrecere și folclor ardelenesc pentru nunți în Brașov
- **meta description:** Muzică de petrecere și folclor live pentru nunți și botezuri în Brașov și Țara Bârsei: repertoriu ardelenesc, sonorizare proprie, deplasare din București.
- **JSON-LD description:** Muzică de petrecere și folclor live pentru nunți, botezuri și evenimente corporate în Brașov și în localitățile din Țara Bârsei, cu repertoriu ardelenesc și sonorizare proprie.
- **Termen targetat:** **formatie muzica de petrecere [zonă]** — title. „folclor” în title, separat
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 1·0·1; h1: 0·1·1; meta: 0·1·3; JSON-LD: 0·1·2; slug: 0·0·1)</sub>
- **H2** (8):
  - Repertoriul ardelenesc, așa cum se cere la nunțile din Țara Bârsei
  - Locații și video din județul Brașov
  - Deplasare și logistică
  - Ce au spus mirii
  - Localități deservite în jurul Brașovului
  - Pachete și prețuri
  - Întrebări frecvente despre evenimentele din Brașov
  - Verificați dacă data este liberă
- **H3** (9):
  - Ce deosebește repertoriul ardelenesc de cel muntenesc
  - [NUME LOCAȚIE 1 — de confirmat]
  - [NUME LOCAȚIE 2 — de confirmat]
  - [NUME LOCAȚIE 3 — de confirmat]
  - Video din zona Brașovului
  - Ajungeți la Brașov și iarna, dacă se circulă greu prin Predeal?
  - Cine se ocupă de cazare pentru o nuntă de seară în Brașov?
  - Veniți cu sonorizare proprie sau folosiți echipamentul sălii?
  - Mai aveți date libere în weekendurile de vârf de sezon la Brașov?

#### 14. `zona-buzau.html` (nouă)

- **title:** Cântec Muntenesc și Moldovenesc, Muzică de Petrecere în Buzău | Nunți, Botezuri | Ioana Balan
- **h1:** Cântec muntenesc cu ecou moldovenesc, la nunți și botezuri în Buzău
- **meta description:** Cântec muntenesc cu influențe moldovenești, live la nunți și botezuri în Buzău, Râmnicu Sărat și pe valea Buzăului, până la Nehoiu. Sonorizare proprie.
- **JSON-LD description:** Cântec muntenesc cu influențe moldovenești și muzică de petrecere live pentru nunți, botezuri și evenimente corporate în Buzău, Râmnicu Sărat și pe valea Buzăului, cu sonorizare proprie.
- **Termen targetat:** parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·1; h1: 0·1·1; meta: 0·1·4; JSON-LD: 0·1·3; slug: 0·0·1)</sub>
- **H2** (6):
  - Câmpie, deal și munte, în opt localități
  - Unde Muntenia se întâlnește cu Moldova
  - Câmpia e simplă, valea cere planificare
  - De la oraș la munte, același pachet
  - Întrebări despre vale, câmpie și Râmnicu Sărat
  - Oraș, câmpie sau vale? Scrieți-ne
- **H3** (6):
  - Cum arată asta într-un program de nuntă
  - Familia mirelui e din Vrancea. Puteți cânta moldovenește fără să pierdem partea muntenească?
  - Petrecerea e la o pensiune de pe valea Buzăului, spre Nehoiu. Încape sonorizarea?
  - La noi, prima parte a serii e cu cântece la masă, nu cu joc. Cât ține?
  - Sala e la Râmnicu Sărat, pe DN2, unde circulă multe camioane. Ajungeți la timp?
  - Cât e diferența de preț între o nuntă în orașul Buzău și una la Nehoiu?

#### 15. `zona-calarasi.html` (nouă)

- **title:** Horă, Sârbă și Muzică de Petrecere în Călărași și Oltenița | Nunți, Botezuri | Ioana Balan
- **h1:** Horă și sârbă de Bărăgan, pentru nunți și botezuri în județul Călărași
- **meta description:** Horă și sârbă de Bărăgan, live la nunți și botezuri în Călărași, Oltenița și în tot județul, până la Dunăre. Sonorizare proprie, preț calculat pe localitate.
- **JSON-LD description:** Horă și sârbă de Bărăgan, live, pentru nunți, botezuri și evenimente corporate în Călărași, Oltenița și în localitățile din județ, cu sonorizare proprie și ofertă calculată după axa de drum a localității.
- **Termen targetat:** parțial: „muzică de petrecere [zonă]” în title, fără „formație” și fără „folclor”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·2; meta: 0·1·4; JSON-LD: 0·1·3; slug: 0·0·1)</sub>
- **H2** (6):
  - Între Oltenița și brațul Borcea
  - Bărăgan și Dunăre: muzica unei câmpii deschise
  - Două axe, două calcule
  - Același pachet, pe două distanțe posibile
  - Ce se întreabă despre evenimentele de lângă Dunăre
  - Pe care dintre cele două drumuri e locația?
- **H3** (6):
  - Ce aduce vecinătatea cu Dobrogea
  - O parte dintre invitați vin din Dobrogea, cu bacul de la Ostrov. Poate programul să țină cont de ultima cursă?
  - Locația e în lunca Dunării, cu terasă lângă apă. La ce să fim atenți seara?
  - Suntem din Fundulea, aproape de Ilfov. Plătim transportul ca pentru orașul Călărași?
  - Nunta e în noiembrie, iar în câmpie ceața e deasă noaptea. Cum vă întoarceți după demontare?
  - E un botez mic, cu puțini invitați, la Călărași. Mai are sens să veniți de la peste o sută de kilometri?

#### 16. `zona-constanta.html` (nouă)

- **title:** Formație Muzică de Petrecere Constanța | Folclor Live | Ioana Balan
- **h1:** Muzică de petrecere, folclor și repertoriu balcanic pentru nunți în Constanța
- **meta description:** Muzică de petrecere și folclor live pentru nunți în Constanța și pe litoral: repertoriu dobrogean și balcanic, sonorizare proprie, deplasare din București.
- **JSON-LD description:** Muzică de petrecere și folclor live pentru nunți, botezuri și evenimente corporate în Constanța și în stațiunile de pe litoral, cu repertoriu dobrogean și balcanic și sonorizare proprie.
- **Termen targetat:** **formatie muzica de petrecere [zonă]** — title. „folclor” în title, separat
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 1·0·1; h1: 0·1·1; meta: 0·1·3; JSON-LD: 0·1·2; slug: 0·0·1)</sub>
- **H2** (8):
  - Deplasarea pe litoral și constrângerile de sezon
  - Repertoriul dobrogean, între folclor românesc și ritmuri balcanice
  - Locații și video din județul Constanța
  - Ce au spus mirii
  - Localități deservite în județul Constanța și pe litoral
  - Pachete și prețuri
  - Întrebări frecvente despre evenimentele din județul Constanța
  - Spuneți-ne data și vedem dacă e liberă
- **H3** (9):
  - Ce cere ringul la o petrecere dobrogeană
  - [NUME LOCAȚIE 1 — de confirmat]
  - [NUME LOCAȚIE 2 — de confirmat]
  - [NUME LOCAȚIE 3 — de confirmat]
  - Video din județul Constanța
  - Petrecerea e pe plajă sau în aer liber. Ce trebuie să vă spunem înainte?
  - Hotelul are oră-limită de sonor. Cum se construiește programul pe ea?
  - Mai sunt sâmbete libere în iulie și august pentru litoral?
  - De ce trebuie stabilită cazarea echipei chiar de la rezervarea datei?

#### 17. `zona-dambovita.html` (nouă)

- **title:** Horă, Sârbă și Folclor în Târgoviște și Dâmbovița | Nunți și Botezuri | Ioana Balan
- **h1:** Sârbe de câmpie și brâuri de deal, pentru nunți și botezuri în Târgoviște și Dâmbovița
- **meta description:** Horă, sârbă și cântec de deal live la nunți și botezuri în Târgoviște și în tot județul Dâmbovița, la o oră pe DN7 sau A1, fără cazare adăugată la preț.
- **JSON-LD description:** Horă, sârbă și cântec de deal live pentru nunți, botezuri și evenimente corporate în Târgoviște și în județul Dâmbovița, cu program adaptat localității, de la câmpie până la deal, și sonorizare proprie.
- **Termen targetat:** parțial: „folclor [zonă]” în title, fără „formație”; fără „muzică de petrecere” în title
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·2; meta: 0·1·2; JSON-LD: 0·1·2; slug: 0·0·1)</sub>
- **H2** (6):
  - Zece localități, de la Titu până în dealuri
  - Un județ care urcă de la câmpie spre Muscel
  - Scurt pe DN7 sau pe A1
  - Prețul crește spre nord, și numai din transport
  - De la luatul miresei la sala din comună
  - De la Titu la Pucioasa, un singur mesaj
- **H3** (6):
  - Unde se așază accentul, după localitate
  - Vrem muzică și la luatul miresei, acasă la ea, într-o comună de lângă Târgoviște. Se poate, pe lângă petrecerea de seară?
  - Și dacă nunta e sus, la Moroeni, sub Bucegi — tot fără cazare?
  - Organizăm la Târgoviște un eveniment de firmă și vrem folclorul ca recital, nu ca petrecere. Se poate?
  - Petrecerea e în curte, într-un sat de lângă Voinești, la final de septembrie. La ce să ne gândim?
  - Sala din comuna noastră e mică pentru câți invitați avem. E mai bine să mutăm petrecerea la Târgoviște?

#### 18. `zona-dolj.html` (nouă)

- **title:** Muzică Oltenească și de Petrecere în Craiova și Dolj | Nunți, Botezuri | Ioana Balan
- **h1:** Hore oltenești și cântec de petrecere, la nunți și botezuri în Craiova și Dolj
- **meta description:** Muzică oltenească și de petrecere live la nunți și botezuri în Craiova și în tot județul Dolj, până la Calafat: hore de mână, sârbe iuți, cazare planificată.
- **JSON-LD description:** Muzică oltenească și de petrecere live pentru nunți, botezuri și evenimente corporate în Craiova și în județul Dolj, cu repertoriu oltenesc, sonorizare proprie, transport și cazare planificate de la rezervare.
- **Termen targetat:** parțial: „muzică … de petrecere [zonă]” în title („Muzică Oltenească și de Petrecere”), fără „formație”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·2; meta: 0·1·3; JSON-LD: 0·1·2; slug: 0·0·1)</sub>
- **H2** (6):
  - Craiova, Dunărea și câmpia dintre ele
  - Oltenia are alt pas de joc
  - Două sute treizeci de kilometri, planificați de la rezervare
  - Pachet, transport și cazare, vizibile separat
  - Ce vor să știe cei care organizează în Oltenia
  - Pentru Craiova, planificarea începe cu data
- **H3** (6):
  - Ce înseamnă asta pentru o nuntă la Craiova
  - Cântați oltenește cu adevărat, sau câteva piese adaptate pentru Craiova?
  - Vrem călușari la nuntă. Îi aduceți voi?
  - Echipa rămâne oricum peste noapte. Se poate cânta și a doua zi, la o masă în familie?
  - La Craiova sunt destule formații oltenești. De ce am aduce muzica din București?
  - Invitații bucureșteni n-au jucat niciodată oltenește. Rămân pe margine?

#### 19. `zona-giurgiu.html` (nouă)

- **title:** Muzică de Petrecere și Folclor Giurgiu | Nunți și Botezuri | Ioana Balan
- **h1:** La o oră de București: muzică live pentru nunți și botezuri în județul Giurgiu
- **meta description:** Muzică de petrecere și folclor live pentru nunți și botezuri în județul Giurgiu, la o oră de București: repertoriu muntenesc, sonorizare proprie, fără cazare.
- **JSON-LD description:** Muzică de petrecere și folclor live pentru nunți, botezuri și evenimente corporate în Giurgiu și în localitățile din județ, cu repertoriu muntenesc și sonorizare proprie, la mai puțin de o oră și jumătate de București.
- **Termen targetat:** parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·1; h1: 0·1·2; meta: 0·1·2; JSON-LD: 0·1·2; slug: 0·0·1)</sub>
- **H2** (6):
  - Tot județul Giurgiu, la mai puțin de o oră și jumătate
  - Ce se cântă la o nuntă de câmpie din sudul Munteniei
  - Trei date operaționale, atât
  - Pachete și prețuri
  - Întrebări frecvente despre evenimentele din județul Giurgiu
  - Trei informații și primiți prețul final
- **H3** (6):
  - De ce nu e nevoie de un bloc regional separat
  - Veniți și în comunele din județ, nu doar în orașul Giurgiu?
  - Trebuie să plătim și cazarea echipei?
  - Sala e mică sau evenimentul e sub cort — de ce aveți nevoie de la locație?
  - Cât de târziu se mai poate prinde o dată la Giurgiu?
  - Jumătate dintre invitați vin din București, jumătate din județ. Cum se împarte programul?

#### 20. `zona-ialomita.html` (nouă)

- **title:** Folclor de Bărăgan și Muzică de Petrecere în Slobozia și Ialomița | Nunți | Ioana Balan
- **h1:** Folclorul Bărăganului, de la Urziceni la Fetești: nunți și botezuri în Ialomița
- **meta description:** Folclor de Bărăgan și muzică de petrecere live la nunți și botezuri în Slobozia, Urziceni, Fetești și în tot județul Ialomița. Ofertă calculată pe localitate.
- **JSON-LD description:** Folclor de Bărăgan și muzică de petrecere live pentru nunți, botezuri și evenimente corporate în Slobozia, Urziceni, Fetești și în localitățile din județul Ialomița, cu sonorizare proprie și ofertă calculată pe localitate.
- **Termen targetat:** parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·3; h1: 0·1·4; meta: 0·1·5; JSON-LD: 0·1·5; slug: 0·0·1)</sub>
- **H2** (6):
  - Șapte localități, de la vest la est
  - Bărăganul, cu drumul lui spre Moldova
  - Același județ, distanțe foarte diferite
  - Localitatea stabilește suplimentul, nu județul
  - Bărăgan, vânt și drumuri lungi
  - Întâi localitatea, apoi data
- **H3** (6):
  - De ce contează DN2 pentru program
  - Masa se face sub cort, pe un teren deschis din Bărăgan. Vântul e o problemă?
  - Localitatea noastră e între Slobozia și Fetești. De unde știm dacă intră la discuția despre cazare?
  - Suntem o familie de mocani, cu rădăcini ardelenești. Puteți cânta și ceva de-al nostru la o nuntă în Bărăgan?
  - La nunțile de la țară, la noi, lăutarii cântă și printre mese, nu doar pe scenă. Se poate?
  - Sala din Țăndărei e liberă pentru montaj doar cu puțin înainte de eveniment. Ajunge timpul?

#### 21. `zona-ilfov.html` (nouă)

- **title:** Folclor și Muzică de Petrecere în Ilfov | Nunți și Botezuri lângă București | Ioana Balan
- **h1:** Folclor și petrecere la marginea Capitalei: nunți și botezuri în Ilfov
- **meta description:** Folclor și muzică de petrecere live la nunți și botezuri în Ilfov, de la Voluntari la Snagov: program construit pe originea invitaților, sonorizare proprie.
- **JSON-LD description:** Folclor și muzică de petrecere live pentru nunți, botezuri și evenimente corporate în localitățile din jurul Bucureștiului, cu program construit pe originea invitaților și sonorizare proprie, fără cazare.
- **Termen targetat:** parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·2; meta: 0·1·3; JSON-LD: 0·1·1; slug: 0·0·1)</sub>
- **H2** (6):
  - Unsprezece localități lipite de București
  - Un județ muntenesc cu invitați din toată țara
  - Contează ora plecării, nu distanța
  - Aceleași pachete, fără supliment de transport
  - Ce ne întreabă cei care organizează lângă București
  - Localitatea, data și de unde vin familiile
- **H3** (6):
  - Programul pornește de la lista de invitați
  - Ne gândim să mutăm petrecerea din București în Ilfov, ca să fie mai ieftin. Se schimbă ceva la muzică?
  - O parte dintre invitați aterizează la Otopeni chiar în ziua nunții. Putem muta momentele importante mai târziu?
  - Cununia civilă e la Buftea, iar petrecerea în altă localitate din Ilfov. Puteți cânta la amândouă?
  - Facem petrecerea în grădina unei vile, într-un cartier rezidențial din Corbeanca. Pot apărea probleme cu vecinii?
  - Complexul are două saloane, iar în aceeași seară mai e un eveniment alături. Se aude de la unii la alții?

#### 22. `zona-prahova.html` (nouă)

- **title:** Folclor de Sub Munte și Muzică de Petrecere în Ploiești și Prahova | Nunți, Botezuri | Ioana Balan
- **h1:** Folclor de sub munte și muzică de petrecere: nunți și botezuri în Ploiești și Prahova
- **meta description:** Folclor de sub munte și muzică de petrecere live la nunți și botezuri în Ploiești, în podgoriile Dealu Mare și pe Valea Prahovei, la o oră pe DN1, fără cazare.
- **JSON-LD description:** Folclor de sub munte și muzică de petrecere live pentru nunți, botezuri și evenimente corporate în Ploiești, în podgoriile din Dealu Mare și pe Valea Prahovei, cu sonorizare proprie și fără cazare adăugată.
- **Termen targetat:** parțial: „muzică de petrecere” și „folclor” + zonă în title, fără „formație”
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·2; meta: 0·1·3; JSON-LD: 0·1·3; slug: 0·0·1)</sub>
- **H2** (6):
  - De la Ploiești la Sinaia, trei grupuri de localități
  - Între câmpie și munte, în același județ
  - O oră pe DN1, plus marja văii
  - Un singur supliment, oriunde pe DN1
  - De la podgorii până la Sinaia
  - Ploiești, podgorii sau Valea Prahovei?
- **H3** (6):
  - Cum se împart cele două registre într-o seară
  - Evenimentul e la o cramă din Dealu Mare, iar o parte din seară vrem s-o petrecem pe terasă. Ce verificăm?
  - Nunta e la Sinaia, iar invitații rămân cazați la hotel. Se poate prelungi petrecerea?
  - Organizăm la Ploiești o petrecere de firmă, într-o zi lucrătoare. Ajungeți la timp, cu traficul de după program?
  - Suntem din Câmpina, iar invitații știu jocurile de pe vale. Cum aflați ce se joacă la noi?
  - Mulți invitați conduc înapoi spre București după petrecere. Cum ținem momentele importante înainte să plece?

#### 23. `zona-teleorman.html` (nouă)

- **title:** Jocuri de Câmpie și Folclor în Teleorman | Nunți, Botezuri în Alexandria | Ioana Balan
- **h1:** Jocuri de câmpie cu tempo apăsat, pentru nunți și botezuri în Teleorman
- **meta description:** Hore și sârbe de câmpie live la nunți și botezuri în Alexandria și în tot Teleormanul, până la Dunăre: repertoriu muntenesc, cu jocuri oltenești la cerere.
- **JSON-LD description:** Hore, sârbe și jocuri de câmpie live pentru nunți, botezuri și evenimente corporate în Alexandria și în județul Teleorman, până la Dunăre, cu repertoriu muntenesc, jocuri oltenești la cerere și sonorizare proprie.
- **Termen targetat:** parțial: „folclor [zonă]” în title, fără „formație”; fără „muzică de petrecere” în title
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·2; h1: 0·1·1; meta: 0·1·3; JSON-LD: 0·1·3; slug: 0·0·1)</sub>
- **H2** (6):
  - Opt localități, pe drumurile care pleacă din Alexandria
  - Câmpia de sud, cu Oltenia la un râu distanță
  - Drum lung și în interiorul județului
  - Transport întotdeauna, cazare doar uneori
  - Rude de peste Olt, căldură, cămin cultural
  - Aflați din primul mesaj dacă apare cazarea
- **H3** (6):
  - Unde are loc nunta schimbă dozajul
  - Nunta e la Turnu Măgurele, iar familia mirelui e de peste Olt. Puteți cânta și oltenește?
  - Dacă petrecerea de la Zimnicea se termină la 5 dimineața, cazarea devine obligatorie?
  - Evenimentul e în iulie, în curte, iar la câmpie căldura e mare. E o problemă pentru echipament?
  - Masa se face la căminul cultural din comună. E în regulă pentru voi?
  - Mulți invitați lucrează în străinătate și vin acasă doar în august. Are sens o nuntă în timpul săptămânii?

#### 24. `zone.html` (nouă)

- **title:** Zone Deservite — 12 Județe | Muzică Live pentru Evenimente | Ioana Balan
- **h1:** Unde cântăm: 12 județe din patru zone etnografice
- **meta description:** Douăsprezece județe din Muntenia, Ardeal, Dobrogea și Oltenia, cu plecare din București. Repertoriul se construiește pe zona în care are loc evenimentul.
- **JSON-LD description:** Muzică de petrecere și folclor live pentru nunți, botezuri și evenimente corporate, cu deplasare din București în douăsprezece județe din Muntenia, Ardeal, Dobrogea și Oltenia.
- **Termen targetat:** niciunul
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: meta: 0·0·5; JSON-LD: 0·1·5)</sub>
- **H2** (3):
  - Cele douăsprezece județe, grupate pe zonă etnografică
  - Cum ajunge distanța în preț
  - Nu vedeți județul în listă?
- **H3** (12):
  - Ilfov
  - Giurgiu
  - Prahova / Ploiești
  - Dâmbovița
  - Teleorman
  - Călărași
  - Ialomița
  - Buzău
  - Argeș / Pitești
  - Brașov
  - Constanța
  - Dolj / Craiova

#### 25. `repertoriu.html` (nouă)

- **title:** Repertoriu de Folclor pe Zone Etnografice | Ioana Balan
- **h1:** Repertoriu de folclor, pe cinci zone etnografice
- **meta description:** Ce se cântă în Muntenia, Ardeal, Oltenia, Dobrogea și Moldova: jocuri, măsuri și instrumente pe zone etnografice, plus ordinea momentelor dintr-o seară.
- **JSON-LD description:** Repertoriu de muzică populară și de petrecere organizat pe cinci zone etnografice — Muntenia, Ardeal, Oltenia, Dobrogea, Moldova —, cu jocurile, măsurile și instrumentele fiecăreia și cu locul lor într-un program de eveniment.
- **Termen targetat:** niciunul din lista clientului (cluster: repertoriu)
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: meta: 0·0·5; JSON-LD: 0·0·5)</sub>
- **H2** (5):
  - Cum se construiește un program
  - Cinci zone, cinci feluri de a juca
  - Ce se cântă în fiecare moment al serii
  - Dincolo de folclor
  - De unde sunt cele două familii?
- **H3** (11):
  - Muntenia: horă, sârbă, brâu
  - Ardeal: învârtită, joc de doi, bărbunc
  - Oltenia: hore iuți și căluș
  - Dobrogea: horă, sârbă și ritmuri balcanice
  - Moldova: hore moldovenești și bătute
  - Primirea invitaților
  - Momentul mirilor
  - Blocul regional
  - Hora mare
  - Tortul
  - Petrecerea târzie

#### 26. `formatia.html` (nouă)

- **title:** Formația: Instrumente, Interpreți și Producție Tehnică | Ioana Balan
- **h1:** Cine urcă pe scenă: instrumente, voci, DJ și echipa tehnică
- **meta description:** Componența formației Ioanei Balan pe roluri — instrumente, interpreți, DJ și MC —, configurațiile de la botez la pachetul extins și producția tehnică.
- **JSON-LD description:** Solistă de muzică populară și de petrecere, cu formație live de trei până la șase instrumente, interpreți pentru muzică ușoară și balcanică, DJ, MC și producție tehnică proprie: sonorizare, lumini și efecte de scenă.
- **Termen targetat:** niciunul din lista clientului (cluster: componență; „formație” fără „nuntă”)
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 1·0·0; meta: 1·0·0; JSON-LD: 1·0·0; slug: 1·0·0)</sub>
- **H2** (4):
  - Roluri pe scenă
  - Cum se schimbă componența de la un pachet la altul
  - Sunet, lumini și efecte
  - Ce configurație vi se potrivește?
- **H3** (14):
  - Instrumente melodice
  - Ritm și armonie
  - Interpreți
  - DJ și MC
  - Lăutar (opțional)
  - Standard
  - Premium
  - Standard
  - Premium
  - Sonorizare
  - Efecte
  - Lumini și imagine
  - Cabină foto
  - Montaj și demontaj

#### 27. `folclor-si-manele.html` (nouă)

- **title:** Folclor și manele în aceeași seară, la cerere | Ioana Balan
- **h1:** Folclor și manele în aceeași seară: cum se construiește blocul de petrecere
- **meta description:** Cum intră manelele în programul serii: în blocul de petrecere, la cererea gazdelor, după jocurile populare și hora mare, stabilite la discuția de organizare.
- **JSON-LD description:** Program muzical care pune în aceeași seară jocurile populare și blocul de petrecere, în care intră la cererea gazdelor manele, muzică balcanică și muzică ușoară de ring, stabilite la discuția de organizare.
- **Termen targetat:** parțial: „folclor și manele” în title/H1, **fără „formație”** în niciun câmp SEO sau heading; „muzică de petrecere” doar într-un H3
- **Bag-of-words:** ok
- **H2** (6):
  - Un strat de program, nu un program separat
  - Ce conține blocul de petrecere
  - Ce se stabilește la telefon
  - Momentul lăutăresc (opțional)
  - Întrebări despre manele în programul serii
  - Ce vreți în blocul de petrecere?
- **H3** (13):
  - Muzică de petrecere românească
  - Manele
  - Balcanic
  - Muzică ușoară de ring
  - Decizii despre blocul de petrecere
  - Pachetul pe care se sprijină blocul
  - Ce rămâne pentru jocurile populare
  - Cine cântă și ce se poate adăuga
  - Dacă evenimentul e departe
  - Manelele fac parte din program oricum sau doar la cerere?
  - Se cântă live sau le pune DJ-ul?
  - Dacă vrem manele, mai rămâne loc pentru jocurile populare?
  - O parte din familie nu vrea manele. Cum se împacă cele două tabere?

#### 28. `nunta.html` (nouă)

- **title:** Cum se organizează muzica la nuntă, pas cu pas | Ioana Balan
- **h1:** Cum se organizează muzica la o nuntă: ordinea momentelor și deciziile de dinainte
- **meta description:** Ghid de organizare a muzicii la nuntă: ordinea momentelor, ce se hotărăște cu luni înainte și ce în ultimele săptămâni, cu trimiteri spre pachete și repertoriu.
- **JSON-LD description:** Ghid de organizare a muzicii la nuntă: ordinea momentelor serii, deciziile care se iau înainte de eveniment și termenul de rezervare, cu trimiteri către pachete, repertoriu, componență și acoperire.
- **Termen targetat:** niciunul („nuntă” fără „formație”; intenție de ghid)
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: title: 0·1·0; h1: 0·1·0; meta: 0·1·0; JSON-LD: 0·1·0; slug: 0·1·0)</sub>
- **H2** (6):
  - Trei etape, de la rezervare până în seara nunții
  - Momentele unei nunți și ce trebuie hotărât pentru fiecare
  - Patru hotărâri care se iau înainte de lista de piese
  - Organizați alt tip de eveniment?
  - Întrebări despre organizarea muzicii la nuntă
  - Primul pas e data
- **H3** (17):
  - Primirea invitaților
  - Intrarea mirilor și primul dans
  - Masa și primul bloc de jocuri
  - Momentele de familie
  - Tortul
  - Finalul serii
  - Cât de mare e scena
  - Ce jocuri recunoaște sala
  - Cine urcă pe scenă
  - Ce adaugă drumul
  - Program scurt, sală cu copii
  - Aniversări, cumetrii, onomastici
  - Gale și petreceri de firmă
  - Cu cât timp înainte se rezervă muzica pentru nuntă?
  - Cine anunță momentele și ține legătura cu fotograful în seara nunții?
  - Trebuie să alegem toate piesele dinainte?
  - Ce se întâmplă dacă programul sălii se decalează în seara nunții?

#### 29. `botez.html` (nouă)

- **title:** Muzica la botez: program, momente și organizare | Ioana Balan
- **h1:** Muzica la botez: un program mai scurt, pentru o sală cu copii
- **meta description:** Cum se organizează muzica la un botez: două seturi live de câte 45 de minute, DJ, început mai devreme decât la nuntă și o sală cu invitați de toate vârstele.
- **JSON-LD description:** Organizarea muzicii la botez: două programe live de câte 45 de minute, DJ pe toată durata evenimentului, program care începe și se încheie mai devreme, într-o sală cu invitați de toate vârstele.
- **Termen targetat:** niciunul
- **Bag-of-words:** ok <sub>(formație·nunt*·toponime: meta: 0·1·0)</sub>
- **H2** (6):
  - O petrecere construită în jurul a două seturi live
  - Momentele unui botez, de la biserică până la final
  - Ce hotărâți înainte de ziua botezului
  - Botez față de nuntă: ce nu se transferă
  - Întrebări despre muzica la botez
  - Verificați data botezului
- **H3** (19):
  - Sosirea de la biserică
  - Intrarea părinților cu copilul
  - Primul set live
  - Momentul de virtuozitate
  - Tortul și obiceiurile familiei
  - Al doilea set și finalul
  - Trei sau patru instrumente
  - Ce intră în 90 de minute live
  - Unde stă formația în salon
  - Ce adaugă drumul
  - Timpul live
  - O singură voce
  - Fără MC
  - Efectele de scenă
  - Ora și sala
  - Nu e muzica prea tare pentru un bebeluș?
  - Cine anunță momentele, dacă pachetul nu include MC?
  - Se poate adăuga un al treilea set live?
  - Botezul are loc la prânz. Se schimbă ceva?

#### 30. `eveniment-privat.html` (nouă)

- **title:** Muzică pentru aniversări, cumetrii și onomastici | Ioana Balan
- **h1:** Aniversări, cumetrii, onomastici: muzica pentru o petrecere de familie
- **meta description:** Cum se organizează muzica la o aniversare, o cumetrie sau o onomastică: configurație redusă, program flexibil și repertoriu ales după invitați și după local.
- **JSON-LD description:** Organizarea muzicii la evenimente private — aniversări, cumetrii, onomastici, petreceri de familie —, cu configurație redusă, program flexibil și repertoriu ales după invitați.
- **Termen targetat:** niciunul
- **Bag-of-words:** ok
- **H2** (6):
  - Gazda decide forma serii
  - Momentele care revin la cele mai multe petreceri de familie
  - Ce stabiliți înainte de petrecere
  - Unde se desparte o petrecere de familie de o nuntă
  - Întrebări despre muzica la o petrecere de familie
  - Spuneți-ne cum vreți să arate seara
- **H3** (19):
  - Sosirea
  - Toastul sau discursul
  - Masa
  - Piesa sărbătoritului
  - Tortul
  - Petrecerea
  - Cât buget pentru muzică
  - Ce generații sunt în sală
  - Cât de mare poate fi formația
  - Ce adaugă drumul
  - Programul
  - Configurația
  - Durata
  - Locul
  - Protagoniștii
  - Poate fi seara doar cu muzică de ascultare, fără petrecere?
  - Cât durează programul la o aniversare?
  - Se poate organiza petrecerea acasă sau în curte?
  - Cu cât timp înainte se rezervă un eveniment privat?

#### 31. `corporate.html` (nouă)

- **title:** Evenimente corporate cu temă românească | Ioana Balan
- **h1:** Evenimente corporate cu temă românească: gale, petreceri de Crăciun, delegații străine
- **meta description:** Folclor live și muzică de petrecere pentru evenimente de firmă: gale, petreceri de Crăciun, delegații străine. Program fix, coordonare cu agenția, factură.
- **JSON-LD description:** Folclor live și muzică de petrecere pentru evenimente de firmă cu temă românească — seri de gală, petreceri de Crăciun, evenimente pentru delegații străine —, cu program fix și coordonare cu organizatorul.
- **Termen targetat:** niciunul
- **Bag-of-words:** ok
- **H2** (6):
  - Alt cumpărător, alt proces
  - Momentele unei seri de firmă, pe semnalele organizatorului
  - Ce stabilește organizatorul înainte de ofertă
  - Evenimentul de firmă, pus lângă o nuntă
  - Întrebări despre evenimentele de firmă
  - Trimiteți-ne brieful
- **H3** (19):
  - Sosirea și networkingul
  - Deschiderea oficială
  - Setul românesc
  - Cina
  - Premieri și momente de protocol
  - Petrecerea
  - Ordinul de mărime al bugetului
  - Ce imagine a României arătați
  - Ce permite sala tehnic
  - Ce adaugă deplasarea
  - Cine cumpără
  - Cum se decide
  - Cum se plătește
  - Programul
  - Publicul și rolul folclorului
  - Se poate contracta prin agenția de evenimente?
  - Pot fi prezentate piesele pentru invitați care nu vorbesc română?
  - Cu cât timp înainte se cere oferta pentru o petrecere de Crăciun?
  - Se poate comanda doar un set scurt, fără petrecere?

