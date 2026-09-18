# Baza de non-duplicare — cifrele față de care compară runda următoare

Măsurat pe `bf2f5e4` + corecturile din 19.09.2026, cu `bash verify/run_all.sh`.
Scriptul care produce cifrele: `non_duplicare.py`.

Documentul există pentru că runda din 18.09.2026 a primit ca reper „grupul de
câmpie, medie 67%”, o cifră care **nu se regăsea nicăieri în repo** și nu s-a
putut reproduce. De aici încolo, reperul e aici, cu metoda lângă el.

---

## 1. Metoda

### Ce se compară

Blocuri de conținut, nu fișiere. `_common.py → content_blocks()` ia tot textul
din `<main>` și îl atribuie celui mai apropiat element de tip bloc, ca nimic să
nu se numere de două ori. Se scot înainte de comparație:

- comentariile HTML (`<!-- ... -->`) — documentația internă nu e conținut;
- `<script>`, `<style>`, `<svg>`;
- `.ph` și `.ph-zone` — marcajele de „de confirmat” sunt schelă, nu text.

### Cele două treceri

| Trecere | Ce face |
|---|---|
| **brut** | textul ca atare |
| **mascat** | toponimele înlocuite cu un simbol unic (`mask()`) |

Trecerea mascată e cea care contează. Fără ea, două pagini de județ ar părea
diferite doar pentru că una zice „Prahova” și cealaltă „Dolj”. Cu ea, rămâne
întrebarea reală: **e aceeași frază cu alt nume de județ?**

Maximul unei perechi = cea mai mare valoare din **trei metrici × două treceri**.

### Prefiltrul de 50%

Perechile sub 50% nu se raportează individual; apar în matrice ca `-`. E un
prefiltru de cost, nu un prag de calitate.

**Consecința, și motivul pentru care mai jos sunt două medii:** o pereche `-`
nu are valoare cunoscută, doar o limită superioară. Media se poate calcula în
două feluri, și amândouă mint puțin, în direcții opuse:

| Metodă | Cum tratează `-` | Ce deformează |
|---|---|---|
| **A — toate perechile** | ca 0 | subestimează; o pereche la 49% intră ca 0 |
| **B — peste prefiltru** | le ignoră, împarte la câte au rămas | supraestimează; media urcă pe măsură ce perechile slabe dispar din numitor |

Se raportează **amândouă**. O mișcare într-una singură nu înseamnă nimic până
nu te uiți și la cealaltă — vezi capcana din §3.

### Praguri

| Prag | Sens |
|---|---|
| ≥ 85% | inacceptabil, se rescrie |
| ≥ 75% | raportat explicit de script (`Perechi ≥ 75%`) |
| 50–75% | acceptabil pentru pagini din aceeași familie geografică |
| < 50% | sub prefiltru |

---

## 2. Grupul de câmpie

Cele șase pagini de zonă din câmpia munteană — familia cu cel mai mare risc de
duplicare, pentru că împart relief, distanțe și repertoriu:

`zona-giurgiu` · `zona-calarasi` · `zona-ialomita` · `zona-teleorman` ·
`zona-ilfov` · `zona-dambovita`

15 perechi (C(6,2)).

### Cifrele de referință — 19.09.2026

| Măsură | Valoare |
|---|---|
| **Metoda A** — toate cele 15 perechi, `-` numărat ca 0 | **51,3%** |
| **Metoda B** — doar cele 13 perechi peste prefiltru | **59,2%** |
| **Maximul grupului** | **71%** |
| Perechi ≥ 75% | 0 |
| Perechi ≥ 85% | 0 |

Runda următoare compară față de **aceste trei cifre**, prin ambele metode.

---

## 2bis. Grupul Oltenia — bază nouă, 19.09.2026

Adăugat odată cu `zona-olt` și `zona-mehedinti`. E acum grupul cu cel mai mare
risc structural din site: **patru pagini care pleacă din același bloc de
repertoriu**, „Oltenia: hore iuți și căluș” din `repertoriu.html`.

`zona-dolj` · `zona-valcea` · `zona-olt` · `zona-mehedinti` — 6 perechi.

| Măsură | Valoare |
|---|---|
| **Metoda A** — toate cele 6 perechi | **65,3%** |
| **Metoda B** — peste prefiltru (toate 6 sunt) | **65,3%** |
| **Maximul grupului** | **71%** (`dolj ↔ valcea`) |
| Perechi ≥ 75% | 0 |

Cele două metode coincid aici pentru că **nicio pereche nu e sub prefiltru** —
patru pagini de aceeași regiune nu ajung niciodată sub 50%. Asta face grupul mai
ușor de urmărit decât câmpia: o singură cifră spune totul.

### Cum s-a ajuns aici

Prima variantă a paginilor Olt și Mehedinți a dat **max 100%**, cu trei perechi
peste 85%. Cauza nu era conținutul, ci refolosirea verbatim a frazelor de
serviciu — transport, montaj, cazare — de pe o pagină pe alta. Paginile vechi le
variau deja, fiecare pe județul ei; noi le copiaserăm.

Ce a scos grupul din zona roșie, în ordinea impactului:

1. **Frazele de logistică, rescrise ca structură, nu ca sinonime.** „Sonorizarea
   pleacă prima…” a devenit o propoziție construită altfel pe fiecare pagină, nu
   aceeași propoziție cu alte cuvinte. Un sinonim schimbă 15 puncte; o
   construcție diferită schimbă 40.
2. **Titlurile de secțiune, deparalelizate.** Patru H2 de forma „Nouă localități,
   de la X până la Y” se mascau în același șablon și dădeau 100% la trecerea
   mascată.
3. **Citatele din `repertoriu.html`, reformulate.** Vezi mai jos.

### Regula care lipsea

**Quoting-ul din `repertoriu.html` e limitat de aceeași măsură.** Brieful cere
ca afirmațiile de folclor să vină exclusiv din blocul regional; non-duplicarea
interzice preluarea lui verbatim. Cele două nu se contrazic: **faptul se ia din
sursă, formularea e a paginii.** Trei pagini au depășit 75% față de
`repertoriu.html` exact pentru că au citat prea aproape de literă.

Pragul se verifică automat, în ieșirea lui `non_duplicare.py`:
„Pagini de zonă cu maxim > 75% față de repertoriu.html”. Ținta e **0**.

---

## 3. Istoric, și capcana pe care o arată

| Dată | Metoda A | Metoda B | Max | Ce se întâmplase |
|---|---|---|---|---|
| 18.09, înainte de modulul de locații | 51,3% | 59,2% | 71% | linia de pornire |
| 18.09, după modul | 54,8% | 58,7% | 71% | Ilfov și Dâmbovița au primit modulul, cu markup identic |
| 19.09, după mutarea Hanul Vlăsiei | **51,3%** | **59,2%** | **71%** | Dâmbovița a rămas cu 2 locații; titlul și intro-ul rescrise |

**Citirea corectă a rândului din mijloc.** Metoda A a urcat cu 3,5 puncte, metoda
B a coborât cu 0,5. Nu e o contradicție: perechea `ilfov ↔ dambovita` a trecut de
la „sub 50%” la 53%, deci a intrat în numitorul lui B ca valoare mică — ceea ce
trage media B în jos — și a înlocuit un 0 în A, ceea ce trage media A în sus.
Nicio pagină nu devenise mai duplicată; o pereche devenise doar **măsurabilă**.

Dacă te uitai numai la A, raportai o regresie inexistentă. Dacă te uitai numai la
B, raportai o îmbunătățire inexistentă. De aceea se raportează amândouă, plus
maximul — singura cifră care nu s-a clintit în tot intervalul.

Pe 19.09 perechea a coborât din nou sub prefiltru, iar grupul e exact pe cifrele
de pornire.

**19.09.2026, runda de șapte pagini noi.** Câmpia a rămas neschimbată —
51,3% / 59,2%, max 71% — deși site-ul a trecut de la 12 la 19 pagini de zonă.
Era și testul principal al rundei: dacă adăugarea a șapte pagini ar fi mișcat
grupul de câmpie, ar fi însemnat că noile pagini împrumută din cele vechi.

---

## 4. Cum reproduci

```bash
pip install -r zone-mockup/verify/requirements.txt
bash zone-mockup/verify/run_all.sh
```

Matricea e în ieșirea lui `non_duplicare.py`, sub „Maxime per pereche”. Mediile
de grup nu sunt tipărite de script: se calculează din matrice, pe cele 15 perechi
ale grupului de mai sus.
