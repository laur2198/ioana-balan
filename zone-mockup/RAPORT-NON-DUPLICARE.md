# Non-duplicare — reparația testului și rescrierile (runda a șaptea)

Data: 2026-09-16. Paginile vechi (cele 11) nu au fost atinse. Header, drawer, footer,
`<head>` și `<style>` sunt identice byte cu byte cu starea de la începutul sesiunii, pe
toate 20 de pagini. Linkurile interne nu s-au schimbat (Partea 2 nu a început).

## Pasul 1 — ce s-a schimbat în test

| Fișier | Schimbare |
|---|---|
| `verify/_common.py` | `content_blocks()` citește tot textul din `main`: fiecare nod de text aparține celui mai apropiat element de tip bloc, deci nimic nu se numără de două ori. Exclude și `.ph-zone`. Parametri noi: `drop` (selectori scoși) și `ui_links=False` (scoate `<a>` care nu stă într-un `p`/`li`/heading și nu conține elemente bloc). `OLD_PAGES` s-a mutat aici. |
| `verify/non_duplicare.py` | Matricea completă: 20 × 19 perechi ordonate plus 20 × 11. Exclude recenziile (`figure blockquote`, `figure figcaption`), `.nota-productie` și linkurile de interfață. Eșec la orice potrivire > 85% **sau** la orice pereche zonă ↔ zonă > 75%. Tipărește matricea de maxime. |
| `zona-brasov.html`, `zona-constanta.html` | Clasa `nota-productie` adăugată pe paragraful „Exemplu de structură — se înlocuiește cu o recenzie…”. Nicio altă modificare de markup, nicio regulă CSS nouă. |

**Avertismentele revin sub prag:** „repertoriul repetă” are 0/12 zone peste 75%, iar
`nunta.html` față de `index`/`oferte` e sub 50% la paragraf și propoziție.

**Durata `run_all.sh`:** 59 de secunde.

## Pasul 2 — matricea înainte de rescriere

**Peste 85%:** 22 de potriviri, toate zonă ↔ zonă, pe 6 texte (#1–#6 de mai jos).

**Între 75% și 85%:** 20 de potriviri. 16 sunt aceleași texte, cu scor mai mic în
cealaltă trecere, iar 2 sunt #7 și #8. Restul de 4 sunt o pereche **nouă, care nu era
în lista de opt**: `eveniment-privat` ↔ `corporate`, 83,3%, „Dacă petrecerea e în afara
orașului” / „Dacă evenimentul e în afara orașului”. E eticheta unui card din secțiunea de
decizii. **Nerescrisă, aștept decizia.** Nu pică testul, pentru că e o pereche serviciu ↔
serviciu, nu zonă ↔ zonă.

```
Maxime per pereche (rând = A, coloană = B), cea mai mare valoare din trei metrici × două treceri.
'-' = sub 50% (prefiltru); '·' = aceeași pagină.

  [ 0] z-arges
  [ 1] z-brasov
  [ 2] z-buzau
  [ 3] z-calarasi
  [ 4] z-constanta
  [ 5] z-dambovita
  [ 6] z-dolj
  [ 7] z-giurgiu
  [ 8] z-ialomita
  [ 9] z-ilfov
  [10] z-prahova
  [11] z-teleorman
  [12] zone
  [13] repertoriu
  [14] formatia
  [15] folclor-si-manele
  [16] nunta
  [17] botez
  [18] eveniment-privat
  [19] corporate
  [20] index
  [21] oferte
  [22] despre
  [23] galerie
  [24] discografie
  [25] contact
  [26] blog
  [27] articol
  [28] faq
  [29] termeni-si-conditii
  [30] politica-cookie

                       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30
z-arges                ·  52  62  64  50  64  61  59  56  50  57  64   -   -   -   -  50  52   -   -   -   -   -   -   -   -   -   -   -   -   -
z-brasov              52   ·  50  55 100   -  87  92   -   -  52   -  69  50  73   -   -   -   -   -  60  70   -   -  56   -   -   -  60   -   -
z-buzau               62  50   ·  57  50  53  69  53  70  55  57  52   -   -  50   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-calarasi            64  55  57   ·  52  71  54  69  61  61  52  58   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-constanta           50 100  50  52   ·  58  55 100   -  55   -   -   -  57   -   -  56   -   -   -   -  53   -   -   -   -   -   -   -   -   -
z-dambovita           64   -  53  71  58   ·  55  54  50  76  67  62   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-dolj                61  87  69  52  55  62   ·   -  62  64  69   -  53   -  67  52   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-giurgiu             59  92  53  69 100  54   -   ·  54  56   -  54   -   -   -   -   -   -   -   -   -  55   -   -   -   -   -   -   -   -   -
z-ialomita            56   -  70  61   -  50  62   -   ·  61   -  56   -  50   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-ilfov               50   -  55  61  55  76  64  56  61   ·  62   -   -   -  57   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-prahova             57  52  57   -   -  67  69   -   -  62   ·   -   -   -   -   -   -  53   -   -   -   -   -   -   -   -   -   -   -   -   -
z-teleorman           64   -  52  58   -  62   -  54  50   -   -   ·   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
zone                   -  69   -   -   -   -  53   -   -   -   -   -   ·   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
repertoriu            50  50   -   -  57   -   -   -  50   -   -   -   -   ·   -  67   -   -  69   -   -  50   -   -   -   -   -   -   -   -   -
formatia               -  73  50   -   -   -  67   -   -  57   -   -   -   -   ·   -   -  57   -   -   -  70   -   -   -   -   -   -   -   -   -
folclor-si-manele      -   -   -   -   -   -  52   -   -   -   -   -   -  67   -   ·  50   -  57   -   -   -   -   -   -   -   -   -   -   -   -
nunta                 50   -   -   -  56   -   -   -   -   -   -   -   -   -   -  50   ·  54  67  57   -   -   -   -   -   -   -   -   -   -   -
botez                 52   -   -   -   -   -   -   -   -   -  53   -   -   -  57   -  54   ·  50  50   -  56   -   -   -   -   -   -   -   -   -
eveniment-privat       -   -   -   -   -   -   -   -   -   -   -   -   -  69   -  57  67  50   ·  83   -   -   -   -   -   -   -   -   -   -   -
corporate              -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  57  50  83   ·   -   -   -   -   -   -   -   -   -   -   -
```

## Pasul 3 — cele opt texte, înainte și după

Criteriul aplicat: dacă înlocuiești toponimul și fraza rămâne valabilă pentru altă pagină,
rescrierea nu e bună. Pentru H1 și H2, bag-of-words rămâne fără încălcări (verificat).

Pe lângă cele opt, am mai atins două fraze din aceleași paragrafe:

- **Constanța, #5:** și fraza de încheiere oglindea Brașovul („Un program construit pentru
  Ardeal funcționează la Constanța pe jumătate, exact ca invers.” / „Un program construit
  pe repertoriu muntenesc funcționează la Brașov pe jumătate…”). Am rescris-o pe cea de
  pe Constanța.
- **Giurgiu, #4:** „În al doilea rând, de cât timp…” a devenit „Apoi, de cât timp…”, pentru
  că fraza de dinainte nu mai începe cu „În primul rând”.

**Interdicția de pe Constanța e respectată.** Comentariul din pagină interzice orice
afirmație că artista a cântat pe litoral. Textele noi descriu tipul de locații și
condițiile de pe litoral, nu prestații.

**De confirmat la completarea cardurilor (#2):** noile H2-uri numesc tipuri de locații
(„Pensiuni la Bran și Moieciu, săli în oraș”, „Hoteluri pe litoral, terase pe faleză”).
Dacă locațiile din agenda clientei sunt altele, se ajustează heading-ul.

### #1 — H2 FAQ

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Întrebări frecvente despre evenimentele din Brașov | Predeal iarna, cazare după miezul nopții, sâmbete de vară |
| `zona-constanta` | Întrebări frecvente despre evenimentele din județul Constanța | Plajă, oră-limită la hotel și camere prinse înaintea sezonului |
| `zona-giurgiu` | Întrebări frecvente despre evenimentele din județul Giurgiu | Comune de pe Dunăre, invitați din București, niciun hotel pe deviz |

### #2 — H2 locații

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Locații și video din județul Brașov | Pensiuni la Bran și Moieciu, săli în oraș |
| `zona-constanta` | Locații și video din județul Constanța | Hoteluri pe litoral, terase pe faleză |

### #3 — Paragraf CTA final

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Scrieți-ne data, localitatea din județul Brașov și numărul aproximativ de invitați. Vă răspundem în aceeași zi cu disponibilitatea și cu prețul, transport și cazare incluse în calcul. | Între o sală din centrul Brașovului și o pensiune la Moieciu diferă drumul de urcare, nu doar adresa, așa că primul mesaj are nevoie de localitate, de dată și de cam câți invitați vin. Prețul care se întoarce are deja socotite drumul peste Predeal și noaptea de cazare a echipei. |
| `zona-dolj` | Scrieți-ne data, localitatea din Dolj și numărul estimat de invitați; primiți în aceeași zi o ofertă cu toate cele trei componente. | Cu data și localitatea — Craiova, Calafat sau Dăbuleni, în sud, spre Dunăre — oferta pleacă în aceeași zi, cu pachetul, drumul și cazarea pe rânduri separate. |

### #4 — Sursa de curent

| Pagină | Înainte | După |
|---|---|---|
| `zona-constanta` | Întâi, ce sursă de curent există la punctul de montaj și ce putere susține — [PUTERE ELECTRICĂ — de confirmat] — pentru că un generator improvizat în timpul petrecerii nu e o soluție. | Primul e curentul: în aer liber, și cu atât mai mult pe nisip, nu există o priză lângă scenă, deci trebuie știut dacă vine din rețeaua hotelului, a barului de pe plajă sau dintr-un generator al locației, și câtă putere dă — [PUTERE ELECTRICĂ — de confirmat]. Un generator adus în grabă, după ce a început petrecerea, nu mai salvează seara. |
| `zona-giurgiu` | În primul rând, ce sursă de curent există la punctul de montaj și ce putere susține — [PUTERE ELECTRICĂ — de confirmat]. | Într-o sală mică de comună sau sub un cort ridicat în curte, curentul vine des dintr-un singur circuit, împărțit cu bucătăria și cu luminile. De aceea întrebăm dacă echipamentul poate avea circuitul lui și ce putere suportă — [PUTERE ELECTRICĂ — de confirmat]. |
| `zona-giurgiu` | În al doilea rând, de cât timp dispunem pentru montaj | Apoi, de cât timp dispunem pentru montaj |

### #5 — Comparația de repertoriu

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Diferența față de repertoriul muntenesc e structurală, nu de nuanță. | La Brașov contrastul se aude în aceeași sală, pentru că rudele venite din sud și gazdele din Țara Bârsei nu joacă același joc. |
| `zona-constanta` | Diferența față de repertoriul ardelenesc e de ritm, nu de nuanță. | Ardealul e reperul cel mai util aici, pentru că stă la polul opus: nunta ardelenească e făcută pentru cei care știu pașii, cea dobrogeană pentru un public adunat din comunități diferite. |
| `zona-constanta` | Un program construit pentru Ardeal funcționează la Constanța pe jumătate, exact ca invers. | Așa că blocurile de joc pentru Constanța nu se împrumută dintr-un program ardelenesc: se scriu pentru un ring pe care intră toată lumea deodată. |

### #6 — H1

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Muzică de petrecere și folclor ardelenesc pentru nunți în Brașov | Nunți în Brașov și în Țara Bârsei, pe învârtită, bărbunc și muzică de petrecere |
| `zona-constanta` | Muzică de petrecere, folclor și repertoriu balcanic pentru nunți în Constanța | Hore, sârbe și ritmuri balcanice: folclor și petrecere la nunțile din Constanța |

### #7 — Fraza de hero

| Pagină | Înainte | După |
|---|---|---|
| `zona-brasov` | Solistă de muzică populară, cu formația, DJ-ul și sonorizarea într-o singură echipă. | Pentru o nuntă la Brașov, voce, formație, DJ și sunet vin cu un singur plan de drum peste Predeal, nu cu patru furnizori care și-l fac fiecare pe al lui. |
| `zona-constanta` | O singură echipă pentru toată seara — solistă de muzică populară, formația, DJ-ul și sonorizarea. | Pe litoral, unde cazarea și ora-limită de sonor se discută cu hotelul, muzica are un singur interlocutor: solista răspunde și pentru formație, pentru DJ și pentru tehnica de sunet. |

### #8 — Intervalul de distanță

| Pagină | Înainte | După |
|---|---|---|
| `zona-dambovita` | Titu și Răcari sunt la capătul apropiat al intervalului, Târgoviștea la cel de sus; Pucioasa și Voinești trec puțin de el. | Până la Titu și Răcari drumul rămâne pe câmpie și e cel mai scurt; Târgoviștea închide intervalul, iar Pucioasa și Voinești, urcate spre deal, îl depășesc cu puțin. |
| `zona-ilfov` | Voluntari și Pantelimon stau la capătul de jos al intervalului, Snagov la cel de sus. | Voluntari și Pantelimon sunt practic prelungiri ale orașului; Snagov, pe DN1 spre nord, e punctul cel mai îndepărtat. |

## Matricea după rescriere

```
Maxime per pereche (rând = A, coloană = B), cea mai mare valoare din trei metrici × două treceri.
'-' = sub 50% (prefiltru); '·' = aceeași pagină.

  [ 0] z-arges
  [ 1] z-brasov
  [ 2] z-buzau
  [ 3] z-calarasi
  [ 4] z-constanta
  [ 5] z-dambovita
  [ 6] z-dolj
  [ 7] z-giurgiu
  [ 8] z-ialomita
  [ 9] z-ilfov
  [10] z-prahova
  [11] z-teleorman
  [12] zone
  [13] repertoriu
  [14] formatia
  [15] folclor-si-manele
  [16] nunta
  [17] botez
  [18] eveniment-privat
  [19] corporate
  [20] index
  [21] oferte
  [22] despre
  [23] galerie
  [24] discografie
  [25] contact
  [26] blog
  [27] articol
  [28] faq
  [29] termeni-si-conditii
  [30] politica-cookie

                       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30
z-arges                ·   -  62  64   -  64  61  59  56  50  57  64   -   -   -   -  50  52   -   -   -   -   -   -   -   -   -   -   -   -   -
z-brasov               -   ·   -   -  70  50   -  73  50   -  52   -  69  50  50   -   -   -   -   -  60  70   -   -   -   -   -   -  60   -   -
z-buzau               62   -   ·  57   -  53  69  53  70  55  57  52   -   -  50   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-calarasi            64   -  57   ·   -  71  54  69  61  61  52  58   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-constanta            -  70   -   -   ·   -   -  75   -   -   -   -   -  57   -   -  56   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-dambovita           64  50  53  71   -   ·  55  50  50   -  67  62   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-dolj                61   -  69  52   -  62   ·   -  62  64  69   -  53   -   -  52   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-giurgiu             59  73  53  69  75  50   -   ·  54  56   -  54   -   -   -   -   -   -   -   -   -  55   -   -   -   -   -   -   -   -   -
z-ialomita            56  50  70  61   -  50  62   -   ·  61   -  56   -  50   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-ilfov               50   -  55  61   -   -  64  56  61   ·  62   -   -   -  57   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
z-prahova             57  52  57   -   -  67  69   -   -  62   ·   -   -   -   -   -   -  53   -   -   -   -   -   -   -   -   -   -   -   -   -
z-teleorman           64   -  52  58   -  62   -  54  50   -   -   ·   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
zone                   -  69   -   -   -   -  53   -   -   -   -   -   ·   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
repertoriu            50  50   -   -  57   -   -   -  50   -   -   -   -   ·   -  67   -   -  69   -   -  50   -   -   -   -   -   -   -   -   -
formatia               -  50  50   -   -   -   -   -   -  57   -   -   -   -   ·   -   -  57   -   -   -  70   -   -   -   -   -   -   -   -   -
folclor-si-manele      -   -   -   -   -   -  52   -   -   -   -   -   -  67   -   ·  50   -  57   -   -   -   -   -   -   -   -   -   -   -   -
nunta                 50   -   -   -  56   -   -   -   -   -   -   -   -   -   -  50   ·  54  67  57   -   -   -   -   -   -   -   -   -   -   -
botez                 52   -   -   -   -   -   -   -   -   -  53   -   -   -  57   -  54   ·  50  50   -  56   -   -   -   -   -   -   -   -   -
eveniment-privat       -   -   -   -   -   -   -   -   -   -   -   -   -  69   -  57  67  50   ·  83   -   -   -   -   -   -   -   -   -   -   -
corporate              -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  57  50  83   ·   -   -   -   -   -   -   -   -   -   -   -
```

## Pasul 4 — propagare pe cele 12 zone

Comparație pe grupuri, pe 66 de perechi, fără prag de lungime și fără prefiltru, cu
maximul dintre trecerea brută și cea mascată. „Înainte” = după Pasul 1; „după” = după rescriere.

| Grup | Max înainte → după | Mediană înainte → după | Distribuție după (<25 / 25–50 / 50–75 / 75–85 / >85) | Cea mai apropiată pereche după |
|---|---|---|---|---|
| H1 (mascat) | 86% → 70% | 52% → 49% | 10 / 23 / 33 / 0 / 0 | Buzău ↔ Ialomița: „…, la nunți și botezuri în Buzău” / „…: nunți și botezuri în Ialomița” |
| H2 FAQ | 100% → 59% | 15% → 13% | 59 / 5 / 2 / 0 / 0 | Dolj ↔ Ilfov: „Ce vor să știe cei care organizează în Oltenia” / „Ce ne întreabă cei care organizează lângă București” |
| H2 localități | 62% → 62% | 20% → 20% | 35 / 28 / 3 / 0 / 0 | Brașov ↔ Constanța: „Localități deservite în jurul Brașovului” / „Localități deservite în județul Constanța și pe litoral” |
| H2 logistică | 22% → 22% | 0% → 0% | 66 / 0 / 0 / 0 / 0 | — |
| H2 repertoriu | 50% → 50% | 14% → 14% | 42 / 22 / 2 / 0 / 0 | Buzău ↔ Ialomița: „Unde Muntenia se întâlnește cu Moldova” / „Bărăganul, cu drumul lui spre Moldova” |
| H2 CTA final | 75% → 75% | 0% → 0% | 60 / 5 / 0 / 1 / 0 | Argeș ↔ Prahova: „Pitești, Câmpulung sau Curtea de Argeș” / „Ploiești, podgorii sau Valea Prahovei?” |
| Paragraf CTA final | 56% → 37% | 13% → 13% | 62 / 4 / 0 / 0 / 0 | Constanța ↔ Giurgiu (37%) |
| Frază despre curent | 87% → 30% | 34% → 17% | 7 / 3 / 0 / 0 / 0 | Călărași ↔ Dâmbovița (30%) |

### Ce nu prinde testul, deși e aceeași problemă

Toate cele de mai jos trec testul. Nu le-am rescris: nu erau în lista de opt.

1. **Frază copiată, la exact 75,00%.** Constanța ↔ Giurgiu: „Primul duce sonorizarea,
   lumina și schela, împreună cu echipa tehnică de montaj, și pleacă devreme.” / „Primul
   duce sonorizarea, lumina și schela, cu echipa tehnică;”. Pragul e „peste 75%”, deci
   trece la limită.
2. **Propoziție de 14 cuvinte identică, diluată într-un bloc lung.** Brașov ↔ Giurgiu,
   73,5%: „…în măsuri de doi timpi care se prind din prima și care nu cer nimic de la
   invitat”. Shingle-6 măsoară ce fracție din bloc se regăsește în cealaltă pagină, așa că
   un fragment identic într-un paragraf lung iese sub prag.
3. **Headinguri sub 6 tokeni, pe care matricea nu le compară deloc.** „Pachete și prețuri”
   e identic pe Brașov, Constanța și Giurgiu. „Localități deservite în jurul Brașovului” are
   4 tokeni.
4. **Tipare de construcție propagate din șabloane, sub 75%:**
   - finalul „…, la/pentru nunți și botezuri în [județ]” apare în 10 H1-uri (mediana 49%);
   - „Ce vor să știe / Ce ne întreabă cei care organizează în/lângă…” (Dolj, Ilfov), plus
     „Ce se întreabă despre evenimentele de lângă Dunăre” (Călărași), care descinde
     direct din vechiul „Întrebări frecvente despre evenimentele din…”;
   - H2-urile de localități care încep cu numărul („Opt / Zece / Șapte / Unsprezece
     localități…”) pe 6 pagini;
   - H2-urile de CTA de forma „X, Y sau Z?” (Argeș, Prahova, Buzău).
5. **Alte note de producție fără clasă.** Pe Brașov și Constanța, două paragrafe sunt
   instrucțiuni pentru cine completează pagina, nu text pentru vizitator: intro-ul secțiunii
   de locații („…se completează din agenda clientei — nu se estimează”) și nota slotului
   video („De preferat un clip cu ringul plin pe învârtită / pe sârbă sau pe un ritm
   balcanic…”, 69,6% între ele). Candidate pentru `.nota-productie`.

## Verificare finală

| # | Verificare | Rezultat |
|---|---|---|
| 1 | `verify/run_all.sh` | **exit 0.** 0 potriviri > 85%, 0 perechi zonă ↔ zonă > 75%, 4 potriviri între 75% și 85% (doar `eveniment-privat` ↔ `corporate`) |
| 2 | Bag-of-words, 31 de pagini | 0 încălcări pe cele 20 noi. Pe toate 31: 11 câmpuri în încălcare înainte și după, 0 verdicte schimbate |
| 3 | Marcaje `.ph` | Ieșirea `marcaje.py` e identică cu baza. Nota de producție nu e `.ph` |
| 4 | Blocuri protejate | `integritate.py`: 0 pagini cu probleme. Header, drawer, footer, `<head>`, `<style>` și scripturile de după footer sunt byte-identice cu starea inițială, pe 20 de pagini |
| 5 | Ținte relative | Toate rezolvă (`integritate.py`) |
| 6 | Linkuri interne | Neschimbate pe toate 20 |
| 7 | Pagini modificate | `zona-brasov` (7 rânduri), `zona-constanta` (7), `zona-giurgiu` (3), `zona-dolj`, `zona-dambovita`, `zona-ilfov` (câte 1) |
| 8 | `git status` | `?? zone-mockup/`, niciun fișier urmărit modificat |
