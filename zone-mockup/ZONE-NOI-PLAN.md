# Cele 7 pagini de zonă noi — plan

Mehedinți, Olt, Brăila, Bacău, Vâlcea, Galați, Tulcea.

Document de pregătire. **Nicio pagină HTML nu s-a scris sau modificat în runda
asta.** Ieșirea rundei e acest plan, harness-ul de randare din
`verify/render/` și auditul din `verify/audit_zone_noi.py`.

Măsurat pe `ae8f8b0`.

---

## 0. Trei premise din brief care nu s-au confirmat

Le pun în față pentru că schimbă ce se poate livra.

**`verify/audit_keywords_v2.py` nu există.** În repo e `audit_keywords.py`, un
singur fișier, fără versiune. L-am folosit pe acela, fără să-l modific:
`audit_zone_noi.py` importă din el `bow()`, `page_fields()` și `terms_in()`.

**Domeniile live sunt inaccesibile din sandbox.** `grand-music.ro` și
`ioana-balan.ro` sunt amândouă blocate de proxy-ul de egress, prin `curl` și
prin WebFetch deopotrivă. Auditul din §2 e **parțial** și spune, pe fiecare
rând, de unde vine informația. Nimic nu e completat din presupuneri.

**Nu există „4 valori de accent etnografic”.** Există **una singură**,
`--accent-zona: var(--accent-edge)`, identică pe toate cele 20 de pagini, iar
blocul de stiluri explică de ce alegerea e deliberată. Vezi §4.

---

## 1. Ce e comun celor 7

| Aspect | Decizie |
|---|---|
| Layout | **C** pe toate șapte — niciuna nu are fotografie, clip sau recenzie locală |
| Transport | aceeași valoare ca pe cele 12: **6 lei/km, dus-întors**, formulată pe contextul județului. Verificată de `check_transport()` din `integritate.py` |
| Cazare | **deschis** pe toate; se folosesc marcajele `.ph` existente, nu se inventează o politică |
| `noindex` | rămâne cât timp pagina conține marcaje `[de confirmat]` |
| Preț | „de la **4.800 €**”, ca pe celelalte 12 |

Trei dintre ele (Mehedinți, Bacău, Tulcea) trec de 300 km dus. Formularea de
transport nu se schimbă — se schimbă doar contextul din jurul ei, iar cazarea
devine mai probabilă, deci marcajul de cazare e obligatoriu acolo.

---

## 2. Auditul de cuvinte cheie — PARȚIAL

### Ce s-a putut și ce nu

| Sursă | Stare | Ce oferă |
|---|---|---|
| `SURSE-LIVE.md` §3 | **completă**, extrasă 2026-09-17 | inventarul de URL-uri al ambelor domenii: 60 pe `grand-music.ro`, 13 pe `ioana-balan.ro` |
| WebSearch, cu domeniu restrâns | **parțială** | titlurile din indexul de căutare, nu conținutul live |
| Fetch direct pe cele două domenii | **eșuat** | `EGRESS_BLOCKED` pe amândouă |

**Nu s-au putut citi:** H1-urile, meta description-urile și corpul paginilor
live. Ce urmează se sprijină pe URL-uri (inventar de repo) și pe title-uri
(index de căutare). Rândurile marcate `—` sunt necunoscute, nu goale.

### 2.1 Pagini care țintesc cele 7 județe sau reședințele lor

`ioana-balan.ro`: **zero**. Cele 13 URL-uri din inventar sunt `/`, `/despre/`,
`/galerie/`, `/oferte/`, `/faq/`, `/blog/`, `/contact/`, `/video-clipuri/`,
`/politica-cookie/`, `/termeni-si-conditii/` și trei articole. **Niciuna
geografică.** Terenul e liber pe domeniul nostru, pe toate cele șapte.

`grand-music.ro`: **una singură**, pe Vâlcea.

| Județ / oraș | Pagină pe `grand-music.ro` | Title (index de căutare) | Modificată |
|---|---|---|---|
| **Vâlcea** / Râmnicu Vâlcea | `/formatie-nunta-valcea/` | „Formatii nunta Valcea \| suna acum pentru oferta 2025-2026” | 2025-06-13 |
| Mehedinți / Drobeta-Turnu Severin | — | — | — |
| Olt / Slatina | — | — | — |
| Brăila | — | — | — |
| Bacău | — | — | — |
| Galați | — | — | — |
| Tulcea | — | — | — |

Cele 16 pagini `/formatie-nunta-*` de pe `grand-music.ro` acoperă Alexandria,
Argeș, Brașov, București, Buzău, Călărași, Constanța, Craiova, Dâmbovița, Dolj,
Giurgiu, Ialomița, Ilfov, Pitești, Ploiești și Vâlcea. `SURSE-LIVE.md` le descrie
drept „șablon de județ, fără date”, cu același conținut pe toate.

### 2.2 Ce termeni folosesc cele două domenii

Din title-urile indexate:

| Termen | Unde apare |
|---|---|
| `formatii nunta [județ]` | tiparul dominant pe `grand-music.ro`: Argeș, Craiova, Călărași, Giurgiu, Constanța, Buzău, Brașov, Dâmbovița, **Vâlcea** |
| `Grand Music Events \| Muzica nunta` | sufixul standard al acelorași pagini |
| `formatii pentru nunta sau botez in [oraș]` | variantă, pe Ploiești |
| `recomandari formatie nunta [oraș]` | pe București |
| `cele mai bune formatii de muzica populara` | pagina de Muntenia, fără județ |
| `solist muzică populară` | `ioana-balan.ro/`, singurul title indexat al domeniului |

**Concluzia operațională:** `grand-music.ro` ocupă integral familia
`formatie nunta [zonă]`. `ioana-balan.ro` nu ocupă nimic geografic. Separarea
cerută în brief — `formatie nunta` rezervat celuilalt domeniu — e deci ușor de
ținut: nu trebuie eliberat nimic, doar să nu intrăm noi.

### 2.3 Tiparul real al celor 12 pagini existente

Brieful propune `formație muzică de petrecere [zonă]` sau
`formație folclor [zonă]`. Paginile existente **nu** folosesc tiparul ăsta decât
pe două din douăsprezece:

| Tipar | Pagini |
|---|---|
| `Formație Muzică de Petrecere [zonă] \| Folclor Live \| Ioana Balan` | `zona-brasov`, `zona-constanta` — 2 |
| `[element de folclor local] și Muzică de Petrecere în [oraș] și [județ] \| Nunți, Botezuri \| Ioana Balan` | celelalte 10 |

Motivul e regula bag-of-words din `bag_of_words.py`: **formație + nuntă +
toponim nu au voie simultan în același câmp.** Cele două title-uri cu „Formație”
n-au „Nunți”; celelalte zece au „Nunți” și n-au „Formație”. Nu e stil, e
constrângere.

Propunerile de mai jos urmează tiparul majoritar, cel cu elementul de folclor în
față. `audit_zone_noi.py --propuneri` verifică fiecare.

### 2.4 Propunerile

Toate trec: **0 încălcări de bag-of-words, 0 apariții de `formatie nunta`.**

| Județ | Title | H1 |
|---|---|---|
| **Mehedinți** | Folclor Oltenesc și Muzică de Petrecere în Drobeta-Turnu Severin și Mehedinți \| Nunți, Botezuri \| Ioana Balan | Folclor de Dunăre și cântec oltenesc, la nunți și botezuri în Mehedinți |
| **Olt** | Cântec Oltenesc și Muzică de Petrecere în Slatina și Olt \| Nunți, Botezuri \| Ioana Balan | Cântec oltenesc de câmpie, pentru nunți și botezuri în Slatina și Olt |
| **Brăila** | Horă de Baltă și Muzică de Petrecere în Brăila \| Nunți, Botezuri \| Ioana Balan | Hore de baltă și sârbe de Bărăgan, la nunți și botezuri în Brăila |
| **Bacău** | Folclor Moldovenesc și Muzică de Petrecere în Bacău \| Nunți, Botezuri \| Ioana Balan | Folclor moldovenesc de Siret și Trotuș, la nunți și botezuri în Bacău |
| **Vâlcea** | Cântec de Sub Carpați și Muzică de Petrecere în Râmnicu Vâlcea și Vâlcea \| Nunți, Botezuri \| Ioana Balan | Cântec de sub Carpați și joc oltenesc, la nunți și botezuri în Vâlcea |
| **Galați** | Folclor Moldovenesc și Muzică de Petrecere în Galați \| Nunți, Botezuri \| Ioana Balan | Folclor de Dunăre moldovenească, la nunți și botezuri în Galați |
| **Tulcea** | Folclor Dobrogean și Muzică de Petrecere în Tulcea și Delta Dunării \| Nunți, Botezuri \| Ioana Balan | Folclor dobrogean și ritmuri de Deltă, la nunți și botezuri în Tulcea |

**Vâlcea a fost rescrisă.** Prima variantă începea cu „Formație Folclor” și
încălca regula: formație + nuntă + toponim în același title. Scriptul a prins-o.
Vâlcea e și singurul județ din cele șapte unde `grand-music.ro` are deja pagină,
deci e exact locul unde ne ținem cel mai departe de vocabularul lor.

### 2.5 Conflicte

| Nivel | Ce | Unde |
|---|---|---|
| **Între domenii** | Vâlcea: `grand-music.ro/formatie-nunta-valcea/` există. Propunerea noastră nu folosește „formație” și nici „formatie nunta”; suprapunerea rămâne pe toponim, inevitabilă | `zona-valcea` |
| **Intern** | „Bărăgan” în H1-ul Brăilei apare deja pe `zona-calarasi` și `zona-ialomita` | non-duplicare, vezi §3 |
| **Intern** | „Folclor Moldovenesc” e propus identic pe Bacău și Galați. **De diferențiat la scriere** — două title-uri identice pe două județe vecine e exact tiparul pe care non-duplicarea îl penalizează | `zona-bacau`, `zona-galati` |

### 2.6 Limită de metodă

`find_toponyms()` citește toponimele din listele de localități ale paginilor de
zonă **existente**. Brăila, Bacău, Galați și Tulcea nu sunt încă acolo, deci
scriptul le raportează `toponim=—` în loc să le recunoască. Verificarea
bag-of-words pentru cele patru devine completă abia după ce paginile își
primesc lista de localități. Rezultatul de acum e un minim, nu un verdict final.

---

## 3. Fișele

### Mehedinți

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Oltenia** |
| Distanța de la București | `.ph` — `[de confirmat: ~350 km până la Drobeta-Turnu Severin]`. **Estimare, nu sursă.** Nu s-a putut verifica; se completează din aceeași sursă ca distanțele celor 12 |
| Localități principale | Drobeta-Turnu Severin, Orșova, Strehaia, Vânju Mare, Baia de Aramă |
| Locații confirmate | **0** |
| Layout și formă | C, **fără modul de locații și fără frază** |
| Cazare | deschis, marcaj `.ph`; la ~350 km e practic obligatorie, deci marcajul stă în cardul de cazare |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | `zona-dolj` (Oltenia, cel mai apropiat ca argument), apoi `zona-valcea` din acest set |
| Sursa de repertoriu | `repertoriu.html`, H3 „Oltenia: hore iuți și căluș” |
| Title/H1 | §2.4 |
| **Risc** | **una dintre cele mai slabe patru pagini ale setului** — zero dovadă locală |

### Olt

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Oltenia** |
| Distanța de la București | `.ph` — `[de confirmat: ~190 km până la Slatina]`. Estimare |
| Localități principale | Slatina, Caracal, Balș, Corabia, Drăgănești-Olt |
| Locații confirmate | **0** |
| Layout și formă | C, fără modul, fără frază |
| Cazare | deschis, marcaj `.ph` |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | **`zona-dolj`** — cel mai strâns cuplu al setului: același bloc de repertoriu, județe lipite, argument de drum aproape identic. Se scriu pe axe diferite (Olt: câmpie și Dunăre la Corabia; Dolj: Craiova ca oraș mare) |
| Sursa de repertoriu | `repertoriu.html`, H3 „Oltenia: hore iuți și căluș” |
| Title/H1 | §2.4 |
| **Risc** | pagină slabă, plus cel mai mare risc de duplicare din set |

### Brăila

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Muntenia** |
| Distanța de la București | `.ph` — `[de confirmat: ~200 km]`. Estimare |
| Localități principale | Brăila, Ianca, Însurăței, Făurei, Movila Miresii |
| Locații confirmate | **0** |
| Layout și formă | C, fără modul, fără frază |
| Cazare | deschis, marcaj `.ph` |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | **`zona-buzau` și `zona-ialomita`** — toate trei ating Bărăganul. Și `zona-galati` din acest set, vezi mai jos |
| Sursa de repertoriu | `repertoriu.html`, H3 „Muntenia: horă, sârbă, brâu” |
| Title/H1 | §2.4 |
| **Risc** | pagină slabă; „Bărăgan” e deja folosit pe două pagini existente |

### Bacău

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Moldova** |
| Distanța de la București | `.ph` — `[de confirmat: ~300 km]`. Estimare |
| Localități principale | Bacău, Onești, Moinești, Comănești, Buhuși |
| Locații confirmate | **0** |
| Layout și formă | C, fără modul, fără frază |
| Cazare | deschis, marcaj `.ph`; la ~300 km, obligatoriu de tratat |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | **`zona-galati`** din acest set — singurele două de Moldova, deci singurele care împart blocul de repertoriu moldovenesc. Se scriu pe axe distincte: Bacău pe văile Siretului și Trotușului, spre munte; Galați pe Dunăre |
| Sursa de repertoriu | `repertoriu.html`, H3 „Moldova: hore moldovenești și bătute” |
| Title/H1 | §2.4 |
| **Risc** | pagină slabă; plus prima pagină de Moldova, fără precedent de ton |

### Vâlcea

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Oltenia** |
| Distanța de la București | `.ph` — `[de confirmat: ~180 km până la Râmnicu Vâlcea]`. Estimare |
| Localități principale | Râmnicu Vâlcea, Drăgășani, Călimănești, Băbeni, Horezu |
| Locații confirmate | **2** — Stephany Ballroom (Râmnicu Vâlcea), Grand Imperial Deluxe (Râmnicu Vâlcea). **Neverificate pe surse publice**; se verifică înainte de scriere, ca cele 21 din `SURSE-LIVE.md` §6 |
| Layout și formă | C + **modul de locații** (≥2), imediat după „Localități deservite”, markup identic cu `zona-ilfov` / `zona-dambovita`. Un singur grup |
| Cazare | deschis, marcaj `.ph` |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | `zona-dolj`, `zona-arges` (ambele ating granița Olteniei), `zona-olt` din acest set |
| Sursa de repertoriu | `repertoriu.html`, H3 „Oltenia: hore iuți și căluș”; ambele locații fiind în reședință, accentul cade pe oraș, nu pe sat |
| Title/H1 | §2.4 |
| **Notă** | singurul județ din set cu pagină concurentă pe `grand-music.ro` |

### Galați

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Moldova** |
| Distanța de la București | `.ph` — `[de confirmat: ~230 km]`. Estimare |
| Localități principale | Galați, Tecuci, Târgu Bujor, Berești, Valea Mărului |
| Locații confirmate | **1** — Bacsoridana Events, cu `.ph`: `[de confirmat: Tecuci sau Valea Mărului]`. Rândul e deschis din `DECIZII-CLIENT-URGENT.md` (S4) |
| Layout și formă | C + **frază** în „Localități deservite” (o singură locație), nu secțiune |
| Cazare | deschis, marcaj `.ph` |
| Transport | 6 lei/km, dus-întors |
| Vecini de non-duplicare | **`zona-bacau`** (Moldova, același bloc de repertoriu) și **`zona-braila`** (județe lipite, amândouă pe Dunăre) — cuplu dublu, cel mai greu de scris din set |
| Sursa de repertoriu | `repertoriu.html`, H3 „Moldova: hore moldovenești și bătute” |
| Title/H1 | §2.4 |
| **Notă** | localitatea locației trebuie confirmată **înainte** de scriere: fraza o numește explicit |

### Tulcea

| Câmp | Conținut |
|---|---|
| Zona etnografică | **Dobrogea** |
| Distanța de la București | `.ph` — `[de confirmat: ~270 km]`. Estimare |
| Localități principale | Tulcea, Măcin, Babadag, Isaccea, Sulina |
| Locații confirmate | **2** — Hotel Delta (Tulcea), Apollo Ballroom (Tulcea). Neverificate pe surse publice; se verifică înainte de scriere |
| Layout și formă | C + **modul de locații** (≥2), un singur grup |
| Cazare | deschis, marcaj `.ph` |
| Transport | 6 lei/km, dus-întors. Sulina n-are acces rutier — de tratat explicit, e singurul caz din tot setul |
| Vecini de non-duplicare | **`zona-constanta`** — singura altă pagină de Dobrogea, cu același bloc de repertoriu. Constanța e litoral și stațiuni; Tulcea e Deltă și Dunăre |
| Sursa de repertoriu | `repertoriu.html`, H3 „Dobrogea: horă, sârbă și ritmuri balcanice” |
| Title/H1 | §2.4 |
| **Notă** | cea mai puternică pagină a setului: două locații plus un argument geografic pe care nicio altă pagină nu-l are |

### Vrancea — fără pagină

Ballroom President, Adjud. **Nu primește pagină în acest set.** Merge pe hub, în
blocul „Am mai cântat și în…”, în runda B2.

### Rezumatul setului

| Pagină | Locații | Formă | Putere |
|---|---|---|---|
| Tulcea | 2 | modul | cea mai puternică |
| Vâlcea | 2 | modul | puternică, dar cu concurență pe domeniul celălalt |
| Galați | 1 | frază | medie, cu localitatea nedecisă |
| Mehedinți | 0 | — | **slabă** |
| Olt | 0 | — | **slabă**, plus risc de duplicare cu Dolj |
| Brăila | 0 | — | **slabă** |
| Bacău | 0 | — | **slabă** |

**Patru din șapte pagini nu au nicio dovadă locală.** Sunt cele mai slabe pagini
pe care le-am produs până acum: se țin exclusiv pe acoperire geografică,
repertoriu și logistică. Merită întrebat clientul dacă are locații în Mehedinți,
Olt, Brăila sau Bacău înainte să se scrie — patru pagini fără dovadă publicate
deodată diluează setul existent.

---

## 4. Al cincilea accent etnografic — premisa nu se confirmă

**Brieful spune că sistemul are 4 valori de accent etnografic și că Bacău și
Galați cer a cincea. Nu există 4. Există una.**

Toate cele 20 de pagini declară identic:

```css
:root { --accent-zona: var(--accent-edge); }   /* #C41236 */
```

Iar blocul de stiluri, care se copiază byte-identic pe fiecare pagină, explică
de ce, pe larg:

> „CONSTANT pe toate zonele. Nu se schimbă per județ. Motivul e aritmetic:
> paleta are trei valori de bordo, toate din aceeași familie […] Trei valori
> vecine pe același ton nu produc patru accente perceptibil diferite pentru
> Ardeal / Muntenia / Oltenia / Dobrogea; ar produce patru nuanțe pe care nimeni
> nu le citește ca sistem […] Diferențierea vizuală între zone vine din altă
> parte: din compoziția de layout […] și din imaginea de hero specifică zonei.
> Acolo se investește, nu în culoare.”

Deci nu e o a cincea valoare care lipsește dintr-un set de patru. E **prima**
valoare diferențiată, într-un sistem care a decis explicit să nu aibă niciuna.

**Recomand să nu se adauge.** Adăugarea ar reporni exact problema pe care
comentariul o descrie, iar Moldova ar fi prima zonă cu culoare proprie într-un
sistem unde Ardealul, Muntenia, Oltenia și Dobrogea n-au — o inconsecvență mai
vizibilă decât lipsa pe care ar rezolva-o.

### Dar dacă se răstoarnă decizia: două variante

Contrastele de mai jos sunt calculate, nu estimate. Pragul pentru UI non-text
(borduri, separatoare, romburi) e **3:1**, WCAG 1.4.11.

| Valoare | pe `#131313` | pe `#1c1b1b` | pe `#20201f` (badge) | distanță față de `#C41236` |
|---|---|---|---|---|
| `#C41236` accent-edge, **actual** | 3,09 | 2,85 | **2,71** ✗ | — |
| **A: `#ffb3b1`** (`tertiary`, token existent) | 10,91 | 10,09 | 9,58 | **3,54** |
| **B: `#DB143C`** (același hue, L 0,42 → 0,47) | 3,70 | 3,42 | 3,24 | **1,20** |

**Varianta A — `tertiary #ffb3b1`.** Token care există deja în paletă, deci nu
se adaugă nicio culoare. Trece pragul cu marjă pe toate cele trei suprafețe și e
singura care se **citește** ca alt accent (3,54 față de bordo). Costul: e un roz
pal, nu bordo, iar CLAUDE.md §5 spune că bordo-ul e singura familie de accent.
Varianta asta cere modificarea regulii, nu doar a valorii.

**Varianta B — `#DB143C`.** Același hue ca `accent-edge`, doar mai deschis. Stă
în familia bordo, deci nu atinge §5. **Dar nu funcționează ca diferențiator:**
distanța față de `#C41236` e 1,20, adică se citește ca aceeași culoare puțin mai
deschisă, exact „nuanța pe care nimeni nu o citește ca sistem” din comentariu.

**Verdict: niciuna nu rezolvă problema pusă.** A funcționează vizual dar sparge
regula de brand; B respectă regula dar nu se vede. Asta e, de fapt, argumentul
comentariului existent, ajuns la aceeași concluzie pe cifre.

### O descoperire colaterală, mai importantă decât cererea

**`accent-edge #C41236` nu trece pragul de 3:1 pe fondul badge-ului.**

Blocul de stiluri afirmă că `accent-edge` e „singura din familie care trece
pragul de 3:1 pentru UI non-text (**3,93:1**)”. Valoarea calculată pe `#131313`
e **3,09**, nu 3,93. Pe fondul real al badge-ului, `#20201f`, e **2,71 — sub
prag.** Bordura lui `.zona-badge` e, azi, sub-conformă pe toate cele 20 de
pagini.

Nu am reparat: runda asta n-are voie să atingă HTML-ul, iar blocul e protejat și
comparat byte-cu-byte de `integritate.py`. **Se tratează separat, înaintea
rundei de pagini noi** — altfel cele 7 pagini noi moștenesc problema. Varianta B
de mai sus, `#DB143C`, o rezolvă exact (3,24 pe badge) fără să schimbe familia
de culoare și fără să pretindă că e un accent etnografic.

### Unde s-ar modifica, dacă se decide

| Fișier | Ce |
|---|---|
| `assets/tailwind.config.js` | valoarea nouă în `theme.extend.colors` |
| `assets/styles.css` | doar dacă valoarea se folosește în afara blocului de pagină; azi `--accent-zona` e declarat în `<style>`-ul fiecărei pagini, nu în `styles.css` |
| blocul `<style>` al fiecărei pagini | o linie, `--accent-zona`; dar blocul e **protejat**, deci modificarea trebuie făcută identic pe toate 20 + cele 7 noi |
| `verify/integritate.py` | regula „zero culori noi” compară față de `zona-brasov.html` și ar pica. Excepția se documentează acolo unde e deja documentat `FOOTER_DEMO`: un set numit, cu motivul și condiția de expirare |

Ultimul punct e cel scump: `integritate.py` derivă culorile permise din pagina
de referință, deci orice token nou trebuie să apară **întâi** acolo. Ordinea
corectă e `zona-brasov.html` → restul → excepția în `integritate.py`, nu invers.

---

## 5. Hub-ul — de la 12 la 19 carduri

**`zone.html` nu s-a modificat.** Ce urmează e măsurat pe grila actuală, cu
harness-ul din `verify/render/`.

### Grila actuală

Hub-ul are azi 12 carduri. Măsurat la 360 / 768 / 1024 / 1440:
`scrollWidth == clientWidth`, 0 px overflow la toate patru. Grila e flexbox /
grid simplu, fără poziționare absolută — adăugarea de carduri nu schimbă
mecanica, doar numărul de rânduri.

### Ce se schimbă la 19

| Lățime | Coloane | 12 carduri | 19 carduri | Efect |
|---|---|---|---|---|
| 360 px | 1 | 12 rânduri | 19 rânduri | +58% derulare verticală |
| 768 px | 2 | 6 rânduri | 10 rânduri | un rând incomplet la final |
| 1024 px | 3 | 4 rânduri | 7 rânduri | un rând incomplet la final |
| 1440 px | 3 | 4 rânduri | 7 rânduri | idem |

Nimic nu se rupe la layout: niciun overflow nou, iar cardurile în sine n-au
ținte sub prag. Măsurat azi pe cele patru lățimi, `zone.html` are 0 px overflow
peste tot. (Harness-ul semnalează două ținte sub 44 px pe hub, dar sunt
preexistente și n-au legătură cu grila — vezi `verify/render/README.md`.)

Problema e de lectură, nu de layout — **19 carduri pe o coloană, la 360 px, e o
listă prea lungă ca să fie scanată.** Recomandarea pentru B2: grupare pe regiune
(Muntenia / Oltenia / Moldova / Dobrogea / Ardeal), cu aceleași etichete de
subgrup ca la modulul de locații, nu heading-uri. Șapte rânduri pe desktop devin
cinci grupuri scurte.

**Se re-măsoară după scriere**, cu:

```bash
cd zone-mockup/verify/render
node build-tailwind.js
python3 measure.py --pagini zone.html --latimi 360,768,1024,1440 --tap
```

### Blocul „Am mai cântat și în…”

Intră **sub grilă**, ca listă de text, nu ca hub-uri. Conține locațiile
confirmate din județe care **nu** primesc pagină — azi doar Ballroom President
(Adjud, Vrancea). E singurul loc unde o locație confirmată poate apărea fără o
pagină de județ în spate, și exact de aceea nu ia formă de card: un card sugerează
o pagină care nu există.

Regula de creștere: când un județ din blocul ăsta ajunge la 2 locații
confirmate, devine candidat de pagină proprie și iese din bloc.

---

## 6. Ordinea de execuție pentru B2

1. **Întrebările către client, întâi.** Locațiile din Mehedinți, Olt, Brăila,
   Bacău; localitatea Bacsoridanei; confirmarea celor 4 locații din Vâlcea și
   Tulcea. Patru pagini fără dovadă se pot evita dacă răspunsul vine la timp.
2. **Verificarea celor 4 locații noi** pe surse publice, ca în `SURSE-LIVE.md`
   §6. Nicio locație nu intră pe pagină neverificată.
3. **Contrastul badge-ului** (§4), separat, înainte de paginile noi.
4. **Distanțele**, dintr-o sursă reală. Cele 7 estimări de mai sus sunt marcate
   `.ph` tocmai ca să nu ajungă pe pagină ca atare.
5. Paginile, în ordinea puterii: Tulcea, Vâlcea, Galați, apoi cele patru slabe.
6. Hub-ul, cu gruparea pe regiuni.
7. `run_all.sh` plus harness-ul, cu cifrele comparate față de
   `verify/BAZA-NON-DUPLICARE.md` și `verify/render/README.md`.
