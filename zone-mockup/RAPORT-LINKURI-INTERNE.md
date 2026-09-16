# Linkuri interne contextuale — runda a opta

Data: 2026-09-16. Cele 11 pagini existente nu au fost atinse. Header-ul, drawer-ul,
footer-ul, `<head>`, `<style>`, JSON-LD și scripturile de după footer sunt identice byte cu
byte cu starea de la începutul sesiunii, pe toate 20 de pagini. `noindex` e neatins.
Nimic nu e în commit.

Documentele de specificație din runda asta: `NAV-FOOTER-MIGRARE.md` și `DECIZII-CLIENT.md`.

## Ce s-a modificat

| Pagină | Adăugat | Unde |
|---|---|---|
| 12 × `zona-*` | un paragraf cu 2–3 zone vecine | finalul secțiunii de localități, înainte de „Toate zonele deservite” |
| 12 × `zona-*` | un paragraf cu cele 4 pagini de serviciu | secțiunea de pachete, după paragraful de introducere |
| `zone` | un paragraf cu cele 4 servicii + `repertoriu` + `formatia` | sub grila de județe |
| `nunta`, `botez`, `eveniment-privat`, `corporate` | **nimic** | linkul către hub exista deja în secțiunea de decizii („Vezi zonele deservite”) |
| `folclor-si-manele` | **nimic** | linkul către hub exista deja („Vezi zonele deservite”) |
| `repertoriu`, `formatia` | nimic | nu erau în brief |

Fiecare paragraf nou e un `<p>` cu linkuri în frază, cu clasa de link din proză pe care
paginile o folosesc deja (`text-primary underline underline-offset-4 …`). Nu am adăugat
nicio regulă CSS nouă. Deasupra fiecărui paragraf e un comentariu de o linie.

Pe zone: +4 linii pe pagină (2 comentarii, 2 paragrafe), zero linii șterse. Pe hub: +2.

## 1. Zonele vecine

### Relațiile și sursele lor

Fiecare legătură a fost verificată înainte de scriere. **Prima variantă pentru
Ilfov ↔ Dâmbovița era greșită:** o legătură prin Buftea spre Răcari. În realitate, DN71
se desprinde din **DN7** la Bâldana, nu din DN1A. Am corectat-o înainte de scriere.

| Relație | Sursă |
|---|---|
| DN7 București – Chitila – Bâldana – Titu – Găești – Topoloveni – Pitești | [CNAIR, DN7 Bâldana–Titu](https://www.cnadnr.ro/ro/comunicare/comunicate-de-presa/interes-general/largire-la-4-benzi-dn7-baldana-titu-km-30950-km-52300) |
| DN71 pleacă din DN7 la Bâldana, prin Răcari, spre Târgoviște | [CNAIR, DN71 Bâldana–Târgoviște–Sinaia](https://www.cnadnr.ro/ro/proiecte/modernizare-dn71-baldana-targoviste-sinaia-km-0000-km-44130-largire-la-4-benzi-de) |
| Bâldana, sat în comuna Tărtășești, Dâmbovița; în Ilfov între 1968 și 1981 | [Wikipedia, Bâldana](https://ro.wikipedia.org/wiki/B%C3%A2ldana,_D%C3%A2mbovi%C8%9Ba) |
| DN5 București – Jilava – Adunații-Copăceni – Giurgiu | [CNAIR, DN5](https://www.cnadnr.ro/ro/proiecte/modernizare-dn5-bucuresti-adunatii-copaceni-sector-km-7573-19220) |
| Județul Vlașca, reședința la Giurgiu, desființat în 1950; Drăgănești-Vlașca azi în Teleorman | [Wikipedia, Județul Vlașca](https://ro.wikipedia.org/wiki/Jude%C8%9Bul_Vla%C8%99ca_(antebelic)) |
| Barajul Mihăilești, pe Argeș, la granița Giurgiu–Ilfov; Argeșul se varsă în Dunăre la Oltenița | [Wikipedia, Barajul Mihăilești](https://ro.wikipedia.org/wiki/Barajul_Mih%C4%83ile%C8%99ti), [Wikipedia, Râul Argeș](https://ro.wikipedia.org/wiki/R%C3%A2ul_Arge%C8%99) |
| Podgoria Dealu Mare, în Prahova și Buzău; centre la Valea Călugărească, Urlați, Merei | [Wikipedia, Podgoria Dealu Mare](https://ro.wikipedia.org/wiki/Podgoria_Dealu_Mare) |
| DN72 Găești – Târgoviște – Ploiești, prin Filipeștii de Târg | [Wikipedia, DN72](https://ro.wikipedia.org/wiki/DN72) |
| Vedea izvorăște din Podișul Cotmeana, trece prin Roșiorii de Vede și Alexandria | [Wikipedia, Râul Vedea](https://ro.wikipedia.org/wiki/R%C3%A2ul_Vedea) |
| DN6 prin Ghimpați, Drăgănești-Vlașca, Alexandria, Roșiorii de Vede, Caracal, Craiova | [Wikipedia, DN6](https://en.wikipedia.org/wiki/DN6) |
| Bacul Chiciu–Ostrov, suspendat temporar la ape scăzute (august 2026) | [Poliția de Frontieră](https://www.politiadefrontiera.ro/ro/giurgiu/i-update--informare-privind-suspendarea-temporara-a-activitatii-bacului-chiciuostrov-si-a-ferryboatului-calarasiaidemir-42765.html), [dunare.ro](https://dunare.ro/program-bac-calarasi-chiciu/) |
| DN21 Brăila – Slobozia – Dragalina – Călărași | [Wikipedia, DN21](https://en.wikipedia.org/wiki/DN21) |
| DN2C Buzău – Slobozia, prin Pogoanele; Pogoanele în Câmpia Bărăganului | [Primăria Pogoanele](https://www.primariepogoanele.ro/orasul/asezare-geografica/) |
| DN10 Buzău – Nehoiu – Întorsura Buzăului – Brașov | [Wikipedia, DN10](https://en.wikipedia.org/wiki/DN10) |
| DN65 Pitești – Slatina – Craiova | [Wikipedia, DN65](https://ro.wikipedia.org/wiki/DN65) |
| Ialomița izvorăște pe versantul sudic al Bucegilor, trece prin Pucioasa și Târgoviște; Dâmbovița se învecinează cu Brașov | [Wikipedia, Râul Ialomița](https://ro.wikipedia.org/wiki/R%C3%A2ul_Ialomi%C8%9Ba), [Primăria Moroeni](https://primariamoroeni.ro/resursele-si-factorii-naturali/) |
| DN1 prin Snagov și Otopeni spre Ploiești; A2 cu podurile Fetești–Cernavodă; DN2 Urziceni–Buzău; DN1 Predeal–Valea Prahovei | deja pe paginile de zonă; rute cunoscute, necontestate |

**Două perechi din tabelul brief-ului nu sunt vecine geografic:** Dolj nu se învecinează
nici cu Teleorman, nici cu Argeș, pentru că între ele e județul Olt. Legătura reală e
drumul: DN6 (Teleorman) și DN65 (Pitești). Rândul de pe `zona-dolj` spune explicit asta,
în loc să sugereze o graniță comună. Același lucru pentru Teleorman → Dolj și Argeș →
Dolj: textul vorbește de drum, nu de vecinătate.

### Textele

Semnătura = numărul de linkuri din fiecare frază. `0111` înseamnă o frază-cadru fără link,
apoi câte o frază pe vecin.

| Zonă | Tipar declarat | Semnătură | Text |
|---|---|---|---|
| `zona-ilfov` | radialele ca subiect: frază-cadru, apoi câte un drum pe vecin | `0111` | Trei dintre radialele care pleacă din inel ies direct în alt județ. DN1 trece pe lângă Snagov și continuă spre Ploiești, în **Prahova**. DN7, care părăsește orașul pe la Chitila, ajunge la Titu, în **Dâmbovița**. DN5 lasă în urmă Jilava și intră în **Giurgiu** la Adunații-Copăceni. |
| `zona-giurgiu` | istoric-administrativ, apoi apa ca legătură comună | `12` | Până la reorganizarea din 1950, Giurgiu a fost reședința județului Vlașca, din care făcea parte și Drăgăneștiul de pe DN6, azi în **Teleorman**. Celelalte două vecine le leagă apa: barajul de la Mihăilești, pe Argeș, stă chiar pe granița cu **Ilfov**, iar râul își încheie cursul în Dunăre la Oltenița, în **Călărași**. |
| `zona-prahova` | peisaj care trece granița, fără frază-cadru | `111` | Podgoria Dealu Mare nu se oprește la granița județului: după Mizil, dealurile cu vie continuă în **Buzău**, unde Merei e unul dintre centrele ei. Spre vest, DN72 leagă Ploieștiul de Târgoviște, în **Dâmbovița**, pe la Filipeștii de Târg. Invitații care aterizează la Otopeni, în **Ilfov**, sunt deja pe DN1, la mai puțin de o oră de Ploiești. |
| `zona-dambovita` | după originea invitaților; două vecine într-o frază, a treia cu reper istoric | `21` | Familiile din **Argeș** ajung pe DN7, prin Topoloveni, direct la Găești, iar cele din **Prahova** intră în Târgoviște pe DN72, dinspre Ploiești. Pentru invitații din **Ilfov**, reperul e Bâldana, satul unde DN71 se desprinde spre Răcari și care a aparținut el însuși de Ilfov între 1968 și 1981. |
| `zona-teleorman` | râul ca fir, apoi drumul care taie județul | `12` | Vedea, râul pe care stau Roșiorii de Vede și Alexandria, izvorăște în **Argeș**, pe Podișul Cotmeana. DN6 taie județul pe orizontală: vine dinspre Ghimpați, din **Giurgiu**, trece prin Drăgănești-Vlașca și Alexandria și pleacă mai departe, pe la Caracal, spre Craiova, în **Dolj**. |
| `zona-calarasi` | traversări, cu durata și condiția lor | `111` | De la Chiciu, lângă oraș, platformele de bac trec Dunărea la Ostrov, în **Constanța**, în mai puțin de un sfert de oră, când vremea și nivelul apei o permit. Pe uscat, DN21 urcă prin Dragalina până la Slobozia, în **Ialomița**. Iar Oltenița e locul unde se termină Argeșul, după ce a străbătut **Giurgiu**. |
| `zona-ialomita` | o singură frază: regula de cazare de dincolo de fiecare graniță | `3` | Regula de cazare se schimbă la fiecare graniță: după podurile A2 de la Fetești, Cernavodă e deja în **Constanța**, unde camera pentru echipă e obligatorie; pe DN2, dincolo de Urziceni, în **județul Buzău** ea contează doar pe valea spre Nehoiu; iar pe DN21, coborând din Slobozia în **Călărași**, o hotărăște ora de final, la fel ca în estul Ialomiței. |
| `zona-buzau` | localitățile din listă ca porți: frază-cadru, apoi câte o localitate pe vecin | `0111` | Trei localități de pe listă deschid, fiecare, drumul spre alt județ. Nehoiu e pe DN10, care urcă valea, trece munții și coboară în Țara Bârsei, spre **Brașov**. Merei ține de Dealu Mare, podgoria împărțită cu **Prahova**, cu Urlați și Valea Călugărească pe partea cealaltă. Pogoanele stă pe DN2C, șoseaua de câmpie care duce la Slobozia, în **Ialomița**. |
| `zona-arges` | județul ca etapă de drum; un vecin, apoi două într-o frază | `12` | Piteștiul e și etapă spre Craiova, în **Dolj**: acolo drumul lasă A1 și continuă pe DN65, prin Slatina. Tot din județ pleacă spre sud-est DN7, pe la Topoloveni, către Găești, în **Dâmbovița**, și Vedea, izvorâtă pe Podișul Cotmeana, care curge până la Alexandria, în **Teleorman**. |
| `zona-brasov` | munte ca graniță: cadru, două vecine într-o frază, a treia separat | `021` | Dincolo de munții care închid Țara Bârsei spre sud și spre est, drumurile și apele coboară în alte județe. Din Predeal, DN1 urmează Valea Prahovei spre Sinaia, în **Prahova**, iar pe versantul sudic al Bucegilor izvorăște Ialomița, râul Pucioasei și al Târgoviștei, în **Dâmbovița**. Spre **Buzău** se trece pe DN10, pe la Întorsura Buzăului, până la Nehoiu. |
| `zona-constanta` | drumul spre mare trece prin vecine | `11` | Drumul de la București traversează ambele județe vecine înainte să ajungă la mare: A2 trece prin **Ialomița** și intră aici pe podurile de la Fetești la Cernavodă. Cine pornește din **Călărași** are și o scurtătură fără autostradă, bacul care leagă Chiciu de Ostrov, în sud-vestul județului, cu excepția zilelor cu Dunărea prea scăzută. |
| `zona-dolj` | negație: fără graniță comună, legătura e drumul | `02` | Niciun alt județ de pe această listă nu se învecinează cu Doljul, între ele stă Oltul. Cele două drumuri spre Craiova pornesc totuși din zone pe care le acoperim: DN6 din **Teleorman**, pe la Roșiorii de Vede și Caracal, și DN65 din Pitești, capătul autostrăzii în **Argeș**, pe la Slatina. |

**Primul set de texte nu trecea de propria mea verificare.** Șase din douăsprezece rânduri
aveau aceeași construcție: frază-cadru, apoi o frază pe vecin (Ilfov, Dâmbovița, Ialomița,
Buzău, Argeș, Brașov). Scorurile de similaritate erau mici (maxim 37%), deci testul de
text nu le-ar fi prins. Am restructurat Dâmbovița, Ialomița, Argeș și Brașov înainte de a
scrie în pagini.

## 2. Rândurile către servicii

| Pagină | Tipar declarat | Semnătură | Text |
|---|---|---|---|
| `zona-ilfov` | fie… fie…, cu descriptori; alegerea la final | `4` | Suplimentul rămâne la fel de mic oricare ar fi ocazia, fie o **nuntă** cu familii din mai multe regiuni, fie **botezul** dintr-o grădină din Corbeanca, fie o **cumetrie** sau **seara pentru colegii de firmă**; pagina de citit o alegeți după ce sărbătoriți. |
| `zona-giurgiu` | fără cazare → diferă ordinea serii, cu „pentru” repetat | `04` | Fără noapte de hotel, drumul până la Comana sau Bolintin-Vale arată la fel indiferent de eveniment. Diferă ordinea serii, descrisă separat pentru **botez**, pentru **nuntă**, pentru **o gală sau o petrecere de Crăciun a firmei** și pentru **o onomastică sau o zi de naștere rotundă**. |
| `zona-prahova` | perechi eveniment–locație cu același calcul | `22` | O **nuntă** într-o cramă din Dealu Mare și un **eveniment corporate** într-un hotel din Sinaia au același calcul de transport. La fel un **botez** la un restaurant din Ploiești sau o **petrecere în familie** la Câmpina, chiar dacă programul fiecăruia arată altfel. |
| `zona-dambovita` | contează mai puțin X decât Y; celelalte au altă durată | `13` | Pentru programul muzical contează mai puțin dacă sala e la Pucioasa sau la Titu decât dacă organizați o **nuntă**. Un **botez**, o **cumetrie** și o **seară corporate** au fiecare altă durată și altă ordine a momentelor. |
| `zona-teleorman` | cazarea ține de oră, ora ține de ocazie | `22` | Cazarea se decide după ora de final, iar ora ține de ocazie: un **botez** are un program mai scurt, o **nuntă** la Zimnicea poate ține până dimineața. Pentru **petrecerile de familie** și pentru **evenimentele de firmă**, durata se fixează la organizare. |
| `zona-calarasi` | aceeași distanță, alt program; excepția la final | `31` | Pe axa Olteniței sau pe cea dinspre Borcea, o **nuntă**, un **botez** și o **aniversare** se calculează la fel ca distanță, dar nu și ca program. Iar dacă locația găzduiește o **gală a firmei**, pagina ei explică ce se schimbă față de o petrecere privată. |
| `zona-ialomita` | paralelism „Între X și Y se schimbă…” | `022` | Între Urziceni și Fetești se schimbă transportul. Între o **nuntă** și un **botez** se schimbă durata, numărul de voci și ordinea momentelor. O **petrecere de familie** sau o **gală de firmă** au, la rândul lor, altă construcție. |
| `zona-buzau` | întrebarea care urmează după localitate, listă în incidentă | `4` | La Nehoiu sau la Pogoanele, după localitate vine întrebarea ce anume sărbătoriți — **un botez**, **o nuntă**, **o zi de naștere în familie** sau **un eveniment al firmei** —, pentru că de răspuns depinde cât durează programul și, la munte, dacă mai e nevoie de cazare. |
| `zona-arges` | specificul local nu ține de județ, ci de ocazie; paginile ca subiect | `04` | Cât loc primește jocul de Muscel într-o seară nu ține de județ, ci de ocazie. Paginile despre **petrecerile corporate**, **nunți**, **aniversări** și **botezuri** arată cum e construit fiecare program. |
| `zona-brasov` | ocazia înaintea locației; cea mai lungă seară, apoi restul | `13` | Înainte de pensiunea din Bran sau de sala din oraș, alegeți ocazia, pentru că de ea depinde lungimea serii, iar cea mai lungă e la o **nuntă**. **Botezul**, **cumetria** și **vizita unei delegații străine** au programe proprii, fiecare pe pagina lui. |
| `zona-constanta` | regula nu face diferența între A și B, nici între C și D | `04` | În iulie și august, camera pentru echipă se caută odată cu data. Regula nu face diferența între o **gală a firmei** și o **nuntă**, nici între un **botez** și o **petrecere în familie**; diferă doar ce se cântă, descris pe pagina fiecăruia. |
| `zona-dolj` | din trei rânduri ale ofertei, doar primul depinde de ocazie | `22` | Din cele trei rânduri ale ofertei, doar pachetul depinde de ocazie: e altul pentru o **nuntă** decât pentru un **botez**. Transportul și cazarea spre Craiova se calculează identic și pentru o **onomastică**, și pentru un **eveniment corporate**. |
| `zone` | județul dă jocurile, ocazia dă forma serii; plus clusterul | `042` | Județul spune ce jocuri se cer, dar forma serii o dă ocazia. Cum arată ea la o **nuntă**, la un **botez**, la o **petrecere de familie** sau la un **eveniment de firmă** e explicat pe pagini separate. Ce se cântă în fiecare regiune e pe pagina de **repertoriu**, iar cine urcă pe scenă, pe cea despre **componența formației**. |

**Și aici, primul set avea un tipar dominant:** 11 din 13 rânduri se terminau cu două
puncte urmate de o listă goală („…: nuntă, botez, X, Y.”), adică o listă de linkuri
deghizată. Le-am rescris înainte de inserare. Ordinea celor patru linkuri variază de la un
rând la altul, iar ancorele numesc ocazia („cumetrie”, „gală a firmei”, „vizita unei
delegații străine”), fără toponime.

**Ancorele către `corporate.html` depind de D8** din `DECIZII-CLIENT.md`: nu e confirmat
că se fac evenimente de firmă.

## 3. Verificare

`verify/run_all.sh` rulează acum și `linkuri_noi.py`. **Exit 0, în 75 de secunde.**
Fișierul nu e executabil (nu era nici înainte), așa că se rulează cu `bash run_all.sh`.
Permisiunile nu le-am schimbat.

### Ce s-a schimbat în test

| Fișier | Schimbare |
|---|---|
| `verify/linkuri_noi.py` | **nou.** Citește rândurile din pagini după poziție (secțiunea de localități, respectiv de pachete sau de județe), nu dintr-o listă ținută de mână. Acoperă verificările 1–4 și 9, plus structura: exact un rând pe pagină, vecinii corecți, toate cele 4 servicii. |
| `verify/bag_of_words.py` | raportează, informativ, și cele 11 pagini existente. Codul de ieșire rămâne legat doar de cele 20 noi. |
| `verify/run_all.sh` | adaugă `linkuri_noi.py` |

**Tiparul de construcție e măsurat pe două căi.** (a) Semnătura linkuri-per-frază, pe care
se aplică limita de 4. (b) Scheletul de cuvinte funcționale: conținutul e înlocuit cu `_`,
toponimele cu `TOPO`, iar perechile se compară între ele. Acesta e informativ. Niciuna
nu înlocuiește cititul: semnătura n-ar deosebi „fie… fie…” de o listă după două puncte,
dacă ambele au 4 linkuri într-o frază. De aceea tabelele de mai sus au și coloana de tipar
declarat.

| # | Verificare | Rezultat |
|---|---|---|
| 1 | Zone vecine, 12 × 12, brut și mascat | **0 perechi ≥ 75%.** Maxim 36,2% (Ialomița ↔ Prahova, mascat). Distribuția maximelor pe rând: <25% **1** · 25–50% **11** · 50–75% **0** · ≥75% **0**, mediană 29,7%. |
| 2 | Tipar de construcție, vecine | Cel mai mare grup: **3** (`12`: Argeș, Giurgiu, Teleorman). Apoi `0111` × 2, `111` × 2 și cinci semnături unice. Schelet: 0 perechi ≥ 75%, maxim 53,5%. |
| 3 | Servicii, 13 × 13 | **0 perechi ≥ 75%.** Maxim 28,0% (Constanța ↔ hub). Distribuție: <25% **7** · 25–50% **6** · 50–75% **0** · ≥75% **0**, mediană 23,5%. Tipar: cel mai mare grup **3** (`04` și `22`). Schelet: maxim 61,9%. |
| 4 | Fragment identic ≥ 10 cuvinte, între cele 25 de rânduri noi | **0 perechi**, brut și mascat. Cea mai lungă secvență comună: 5 cuvinte. Informativ: niciun rând nou nu are un fragment de 10+ cuvinte comun cu restul textului de pe cele 31 de pagini (1.922 de blocuri). |
| 5 | Non-duplicare completă, 20 × 20 și 20 × 11 | 0 potriviri > 85%. 0 perechi zonă ↔ zonă > 75%. Matricea de maxime e **identică celulă cu celulă** cu cea de la finalul rundei a șaptea: frazele noi nu au mutat niciun maxim. Rămân 4 potriviri între 75% și 85%, **preexistente**: `eveniment-privat` ↔ `corporate`, „Dacă petrecerea / evenimentul e în afara orașului”, 83,3%. Tot preexistentă, Constanța ↔ Giurgiu la exact 75% (nu depășește pragul). |
| 6 | Bag-of-words, 31 de pagini | 0 încălcări pe cele 20 noi. 11 pe cele existente (`index` ×4, `galerie` ×3, `blog` ×2, `articol` ×2), neschimbate, vezi D1. |
| 7 | Ținte relative, 20 de pagini | Toate rezolvă (`integritate.py`: 0 pagini cu probleme) |
| 8 | Blocuri protejate | `integritate.py`: 0 probleme. Comparație byte cu byte cu copia de la începutul sesiunii: `<head>`, `<style>`, header, drawer, footer, JSON-LD și tot ce e după `</footer>` sunt identice pe toate 20. `repertoriu`, `formatia`, `folclor-si-manele` și cele 4 servicii sunt identice integral. Pe celelalte 13 pagini, diff-ul are doar linii adăugate. |
| 9 | Linkuri interne în `<main>`, înainte → după | 10 zone: 6 → 13 (+7). Constanța și Dolj: 6 → 12 (+6, câte 2 vecine). Hub: 14 → 20 (+6). Celelalte 7 pagini: neschimbate. Pe tot documentul: zonele de la 25 la 31–32, hub-ul de la 33 la 39. |
| 10 | `git status` | `?? zone-mockup/`. Niciun fișier urmărit modificat. |

## 4. De semnalat

1. **„Zone” nu încape în nav fără compensare** (măsurat, `NAV-FOOTER-MIGRARE.md` §1.1). La
   1024, CTA-ul ar ieși din fereastră cu 21,73 px, iar peste marginea de conținut trece și
   la 1100, 1280 și 1440. Varianta de compensare e o decizie deschisă.
2. **Secțiunile B și C din `DECIZII-CLIENT.md` au 70, respectiv 41 de rânduri**, nu ~25 și
   ~36. Le-am extras din toate cele 20 de pagini, inclusiv din cluster și din serviciile pe
   care probabil nu le acoperea numărătoarea anterioară. Am exclus ce e deja publicat pe
   `oferte.html`. Toate cele 82 de citate au fost verificate automat că apar în pagini.
3. **„7 din 8 marcaje comerciale” pe `corporate`:** pagina are 7 marcaje de text plus
   fotografia. După conținut, 5 sunt condiții comerciale sau contractuale și 2 țin de
   capacitate (limbi străine, colinde). Am scris în D8 clasificarea pe care o văd.
4. **Specificația de 700 € (D9)** nu există în repo. Punctul rămâne o întrebare.
5. **`zona-calarasi` și `zona-constanta` pomenesc acum bacul Chiciu–Ostrov**, cu condiția
   nivelului apei. Traversarea era suspendată în august 2026 din cauza apelor scăzute.
   Dacă suspendarea devine regulă, frazele se ajustează.
