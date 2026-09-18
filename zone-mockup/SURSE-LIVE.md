# Surse pe live: verificarea blocantelor față de site-urile publicate

Verificare făcută pe **2026-09-17**. Întrebarea: care dintre cele 44 de rânduri blocante
din `DECIZII-CLIENT.md` (22 în A, 22 în B) sunt deja publicate pe `grand-music.ro` sau pe
`ioana-balan.ro`. Rezultatul e aplicat în coloana „Sursa pe live” din `DECIZII-CLIENT.md`
și în `DECIZII-CLIENT-URGENT.md`.

Citatele de mai jos sunt **verbatim**, cu greșelile de tipar ale originalului. Unde
textul era spart pe mai multe elemente HTML, fragmentele sunt unite cu un spațiu sau
separate cu „/”.

> **Actualizare 2026-09-17, după prima rundă de răspunsuri.** Clientul a confirmat ca ferme
> cifrele de nuntă de pe `/oferte/` (Standard 5.500 € sâmbătă / 4.800 € duminică, Premium
> 6.500 € / 5.500 €), valabile pentru București și Ilfov, tariful de **6 lei/km dus-întors** în
> celelalte județe și cazarea ca cost separat. Nu mai sunt „de validat”: marcajele `.price-tbc`
> au fost scoase de pe ele în prototip. **Prețurile de botez** (3.200 / 2.800 / 3.800 /
> 3.300 €) **nu** fac parte din confirmare și nu apar pe niciun domeniu verificat: rămân
> marcate. A24 și B75 rămân „de validat”, în a doua rundă. Verdictele din §4 sunt
> actualizate; restul documentului descrie verificarea față de live, așa cum a fost făcută.

---

## 1. Metodă

1. **Lista de pagini** vine din sitemap-urile Yoast (`/sitemap_index.xml`) ale celor două
   domenii, nu dintr-o parcurgere manuală a linkurilor. Au intrat toate paginile și
   articolele. Au fost excluse arhivele de etichete, categorii și autori
   (`/tag/`, `/category/`, `/author/`): listează articolele deja incluse.
2. **Descărcare** cu `curl` (HTTP 200 pe toate cele 73 de URL-uri). `ioana-balan.ro`
   redirecționează spre `www.ioana-balan.ro`.
3. **Extragere text**: containerul Elementor al paginii (`[data-elementor-type=wp-page]`
   sau `wp-post`), apoi `<main>`, după eliminarea `header`, `footer`, `nav`, `script`,
   `style`. Prima rulare, pe `<main>`, a prins pe `grand-music.ro/oferta-formatii-nunta/`
   doar prima secțiune (8,2k din 12,9k caractere); rularea finală folosește containerul
   Elementor.
4. **Data ultimei modificări**: `article:modified_time` sau `dateModified` din JSON-LD;
   unde lipsesc, `lastmod` din sitemap.
5. **Căutare**: pe informație, nu pe șir. Fiecare text extras a fost citit integral.
6. **Blocul repetat „Parteneri Grand Music Events”** (15 carduri „Formatie nunta
   [oraș]… Suna acum pentru evenimentul tau!”) apare pe aproape toate paginile
   `grand-music.ro` și nu conține date operaționale.

---

## 2. `ioana-balan.ro` nu e, în mare parte, o sursă independentă

Site-ul în producție a fost construit din prototipul din acest repo (child theme-ul e
în `wp-child-theme/`, paritatea e în `SYNC-WP.md`). Textul extras de pe live, comparat
rând cu rând cu textul paginilor din prototip:

| Pagină live | Rânduri de text (> 25 caractere) | Identice cu prototipul |
|---|---|---|
| `/oferte/` | 66 | 61 |
| `/faq/` | 37 | 23 |
| `/` | 26 | 20 |

Majoritatea diferențelor sunt de punctuație (— devenit –). **Diferențele de conținut,
adică textul editat direct pe live și absent din repo**, sunt doar acestea:

| Pagină | Text de pe live | În prototip |
|---|---|---|
| `/oferte/` | „Pentru evenimentele din afara localității se adaugă un tarif de deplasare de 6 RON/km calculat dus-întors.” | `__ RON/km`, marcat `.price-tbc` |
| `/termeni-si-conditii/` | „se percepe un tarif de deplasare de 6 lei/km, calculat dus-întors” | `[TARIF] lei/km` |
| `/termeni-si-conditii/` | operator GRAND MUSIC EVENTS SRL, sediu „sat Săftica, județul Ilfov”; găzduire „Host-Age (host-age.ro)” | placeholdere |
| `/faq/` | „Avansul este 25% din valoarea totală a pachetului, inclusiv tariful de deplasare, și se achită la semnarea contractului — din acel moment data este rezervată. Restul se plătește la finalul evenimentului.” | „Restul se plătește în ziua evenimentului, înainte de începerea programului.” (`answer-tbc`) |
| `/faq/` | „ne deplasăm pe o rază de circa 500 km” | „circa 300 km” |
| `/faq/` | „acoperim și manele, muzică ușoară românească și internațională” | fără manele |
| `/faq/` | „În funcție de disponibilitatea datei dorite, acceptăm și evenimente last minute.” | „Merită să întrebați și mai târziu: se mai eliberează date.” |

**Consecințe:**

- Tot restul textului de pe `ioana-balan.ro` e scris de noi. **Nu confirmă nimic**: grila
  de prețuri, „în aceeași zi primiți … oferta”, „costurile [cazării] se stabilesc separat”,
  „Locația asigură … alimentarea electrică la scenă” sunt formulările prototipului.
- Singura valoare blocantă care apare pe `ioana-balan.ro` în text independent de prototip
  e **tariful de 6 lei/km** (A2). Nu am putut verifica cine a completat-o: interogarea
  reviziilor WordPress (autor și dată pentru fiecare revizie) a fost refuzată în sesiune.
  Valoarea e identică cu cea de pe `grand-music.ro`, deci independența nu e demonstrabilă.
  De aceea A2 era `confirmat, de validat`, nu `confirmat`, până la răspunsul clientului din 2026-09-17.
- **Problemă separată, în afara acestei sarcini:** live-ul publică fără marcaj cifrele pe
  care prototipul le ține ca `.price-tbc` și răspunsul `answer-tbc` despre plata restului.
  Din 2026-09-17 cifrele de nuntă și tariful pe km sunt confirmate de client, deci pentru ele
  problema nu mai există; rămân publicate neconfirmat **prețurile de botez** și plata restului.
- **Anomalie de dată:** `/termeni-si-conditii/` declară `article:modified_time`
  2026-01-23, dar conținutul e șablonul adăugat în repo pe 2026-09-03 (commit `69d4557`).
  Data declarată de pe acest domeniu nu e de încredere.

---

## 3. Pagini verificate

### `grand-music.ro`: 60 de URL-uri, toate extrase

**Pagini (26)**

| URL | Modificată | Conținut relevant |
|---|---|---|
| `/` | 2026-01-03 | ghid generic; listă „Cheltuieli suplimetare(transport si cazare, unde este cazul)” |
| `/oferta-formatii-nunta/` | 2026-01-03 | **grila de pachete, valabilitate, 6 RON/km** |
| `/video/` | 2026-01-04 | doar embed-uri și blocul de parteneri |
| `/contact-pentru-formatie-de-nunta/` | 2025-07-18 | contact, adresă, „last-minutes” |
| `/cat-costa-o-nunta-cum-facem-intrebari-fecvente/` | 2025-06-13 | **FAQ: plată, avans, transport, cazare, sosire, program, piese, manele** |
| `/formatie-nunta-bucuresti/` | 2025-06-13 | ghid generic; „cheltuielile de transport si cazare(daca e cazul)” |
| `/formatii-nunta-bucuresti/` | 2025-06-13 | generic; excluderea melodiilor |
| `/formatii-nunta/` | 2025-06-13 | generic; excluderea melodiilor |
| `/formatii-pentru-nunta-2024-2025/` | 2025-06-13 | generic; lista de județe deservite |
| `/formatie-nunta-giurgiu/` | 2025-06-13 | șablon de județ, fără date |
| `/formatie-nunta-ialomita/` | 2025-06-13 | idem |
| `/formatie-nunta-valcea/` | 2025-06-13 | idem |
| `/formatie-nunta-buzau/` | 2025-06-13 | idem |
| `/formatie-nunta-dolj/` | 2025-06-13 | idem |
| `/formatie-nunta-pitesti/` | 2025-06-13 | idem |
| `/formatii-pentru-nunta-muzica-de-petrecere/` | 2024-11-02 | formular și listă de articole |
| `/formatie-nunta-ilfov/` | 2024-11-02 | șablon de județ, fără date |
| `/formatie-nunta-ploiesti/` | 2024-11-02 | idem |
| `/formatie-nunta-brasov/` | 2024-11-02 | idem |
| `/formatie-nunta-craiova/` | 2024-11-02 | idem |
| `/termeni-si-conditii/` | 2021-08-31 | politică de cookie și GDPR; fără condiții comerciale |
| `/formatie-nunta-arges/` | 2021-08-31 | șablon de județ, fără date |
| `/formatie-nunta-alexandria/` | 2021-08-31 | idem |
| `/formatie-nunta-dambovita/` | 2021-01-31 | idem |
| `/formatie-nunta-calarasi/` | 2021-01-31 | idem |
| `/formatie-nunta-constanta/` | 2021-01-31 | idem |

Cele 15 pagini `/formatie-nunta-*` au același conținut: blocul de parteneri, fără
nicio informație despre preț, transport, cazare sau montaj.

**Articole (34)**: toate text SEO generic, fără date operaționale, cu excepțiile notate.

| URL | Modificat | Notă |
|---|---|---|
| `/blog/` | 2025-06-06 (sitemap) | pagină-listă, un singur extras de articol |
| `/sfaturi-ce-te-vor-ajuta/` | 2025-06-06 | |
| `/cand-nu-se-fac-nunti-in-anul-2022/` | 2025-06-06 | calendar ortodox |
| `/muzica-pentru-evenimente-nunti-si-botezuri/` | 2022-06-10 | |
| `/cele-mai-bune-formatii-de-muzica/` | 2021-01-24 | |
| `/cele-mai-cautate-melodii-pentru-dansul-mirilor-2021/` | 2021-01-24 | interpretare live a valsului (B74, parțial) |
| `/cand-nu-se-fac-nunti-in-2021/` | 2020-06-26 | calendar ortodox |
| `/petrecerea-de-botez-si-bebelusul/` | 2020-06-13 | |
| `/muzica-pentru-nunti-si-botezuri/` | 2020-05-11 | |
| `/sfaturi-si-idei-pentru-un-botez-reusit/` | 2020-05-09 | |
| `/detaliile-care-fac-diferenta-la-botez/` | 2020-05-09 | |
| `/cum-sa-faci-fata-stresului/` | 2020-05-09 | |
| `/muzica-de-calitate-pentru-nunti-si-botezuri/` | 2020-05-09 | |
| `/solisti-de-muzica-populara-pentru-nunti/` | 2020-05-09 | |
| `/alegerea-unei-formatii-de-nunta-in-bucuresti/` | 2020-05-09 | |
| `/cantareti-de-muzica-populara/` | 2020-05-09 | „cele pe care nu vrei sa le auzi” (B75) |
| `/formatie-de-muzica-pentru-botez-in-bucuresti/` | 2020-05-09 | |
| `/grand-music-va-ofera-solisti/` | 2020-05-09 | |
| `/cea-mai-buna-solista-de-muzica-populara/` | 2020-05-09 | |
| `/cum-sa-alegi-o-formatie-de-muzica/` | 2020-05-09 | |
| `/solisti-de-muzica-populara-pentru-botezuri-in-bucuresti/` | 2020-05-09 | |
| `/trupa-muzica-usoara-cover-si-populara/` | 2020-05-09 | |
| `/formatie-muzica-populara-pentru-evenimente/` | 2020-05-09 | |
| `/formatie-muzica-nunta-repertoriu/` | 2020-05-09 | |
| `/cea-mai-buna-formatie-de-muzica-usoara/` | 2020-05-09 | |
| `/cele-mai-bune-trupe-pentru-coveruri-si-muzica-usoara-din-bucuresti/` | 2020-05-09 | |
| `/cele-mai-bune-formatii-de-muzica-populara-din-muntenia/` | 2020-05-09 | |
| `/trupe-pentru-muzica-de-botez/` | 2020-05-09 | |
| `/trupe-pentru-muzica-de-nunta-in-bucuresti/` | 2020-05-09 | |
| `/ioana-balan-interpreta-de-muzica-populara/` | 2020-05-09 | |
| `/muzica-populara-de-actualitate-pentru-botez/` | 2020-05-09 | |
| `/interpreta-de-muzica-populara-ioana-balan/` | 2020-05-09 | |
| `/formatii-de-nunta-in-dambovita-si-imprejurimi/` | 2020-05-09 | |
| `/formatii-de-muzica-usoara-si-coveruri-targoviste/` | 2020-05-09 | |

### `ioana-balan.ro`: 13 URL-uri, toate extrase

| URL | Modificată | Sursă independentă? |
|---|---|---|
| `/` | 2026-09-10 | nu: textul prototipului |
| `/video-clipuri/` | 2026-09-10 | nu conține date operaționale |
| `/hora-miresei/` | publicat 2026-09-10 | articol; fără valori blocante |
| `/sfaturi-nunta-fara-batai-de-cap/` | publicat 2026-09-09 | rescrierea articolului `grand-music.ro/sfaturi-ce-te-vor-ajuta/`; fără valori |
| `/despre/`, `/galerie/`, `/oferte/`, `/faq/`, `/blog/`, `/contact/`, `/politica-cookie/` | 2026-09-08 (sitemap; fără `modified_time`) | `/oferte/` și `/faq/`: doar rândurile din §2 |
| `/termeni-si-conditii/` | declarat 2026-01-23 (vezi anomalia din §2) | doar valorile completate din §2 |
| `/importanta-luminilor-de-scena/` | publicat 2024-08-15 | fără valori blocante |

**Eșecuri:** niciun URL eșuat. **Limită:** interogarea autorilor reviziilor de pe
`ioana-balan.ro` nu s-a putut face (§2).

---

## 4. Corespondențe, pe rând

Legendă: **C** = `confirmat` de client (2026-09-17) · **DV** = `confirmat, de validat` · **N** = `neconfirmat`, rămâne blocant.
La verificarea față de live niciun rând nu era `confirmat` fără rezervă; **C** vine din răspunsul clientului, nu dintr-o sursă publicată.

Surse citate des:
- **GM-OF** = `https://grand-music.ro/oferta-formatii-nunta/`, modificată 2026-01-03
- **GM-FAQ** = `https://grand-music.ro/cat-costa-o-nunta-cum-facem-intrebari-fecvente/`, modificată 2025-06-13
- **IB-TC** = `https://www.ioana-balan.ro/termeni-si-conditii/`, vezi §2

### A. Valori operaționale

| Rând | Verdict | Sursă | Citat verbatim | Motivul verdictului |
|---|---|---|---|---|
| A1, A3–A12, A14 (intervale de preț pe județ) | **C** (era DV) | GM-OF | „Configurația pachetelor și preturile sunt valabile doar pentru București și Ilfov pentru anul 2026-2027.” / „STANDARD / NUNTĂ / € / 5500 / PENTRU ZILELE DE SÂMBATĂ” / „PREȚ SPECIAL DUMINICĂ 4800EURO” / „PREMIUM / NUNTĂ / € / 6500” / „PREȚ SPECIAL DUMINICĂ  5500EURO” | Doar pe grand-music.ro (grila de pe `ioana-balan.ro/oferte/` e textul prototipului). Grila se aplică direct doar pentru Ilfov (A11); pentru celelalte 11 județe, intervalul nu e publicat ca cifră și rezultă din grilă plus A2. |
| A2 (tarif RON/km) | **C** (era DV) | GM-OF · GM-FAQ · IB-TC · `ioana-balan.ro/oferte/` | GM-OF: „Pentru deplasări în afara localităților menționate, se percepe un tarif de 6 RON/Km dus-întors.” · GM-FAQ: „percepem un cost suplimentar de transport (in suma de 6RON/km dus-întors) și cazare” · IB-TC: „se percepe un tarif de deplasare de 6 lei/km, calculat dus-întors” | Publicat pe ambele domenii, dar pe `ioana-balan.ro` e o completare în șablonul nostru, cu autor neverificat (§2). Vezi și contradicția C4. |
| A17–A21 (cine suportă cazarea) | **C** (era DV) | GM-FAQ · `grand-music.ro/` (2026-01-03) · `grand-music.ro/formatie-nunta-bucuresti/` (2025-06-13) | GM-FAQ: „Oferta acoperă toate costurile dacă evenimentul dumneavoastră are loc în București sau Județul Ilfov. Pentru deplasarea în afara localităților menționate percepem un cost suplimentar de transport (in suma de 6RON/km dus-întors) și cazare .” · homepage: „Cheltuieli suplimetare(transport si cazare, unde este cazul).” | Valoarea: cazarea e cost suplimentar, perceput separat de pachet. Doar pe grand-music.ro; fraza de pe `ioana-balan.ro` („costurile aferente se stabilesc separat”) e textul prototipului. Nu spune dacă gazdele pot asigura ele cazarea. |
| A24 (marjă montaj) | DV | GM-FAQ | „Staff-ul tehnic ajunge la locație cu aproximativ 4-5 ore inainte de începereea evenimentului.” | Doar pe grand-music.ro. Reperul e „începerea evenimentului”, nu „primul moment muzical”. |
| A25, A27 (putere electrică) | N | — | Nimic pe `grand-music.ro`. Pe `ioana-balan.ro/faq/` apare doar „Locația asigură spațiul convenit și alimentarea electrică la scenă.”, text din prototip, fără valoare. | |
| A26 (durată montaj) | N | GM-FAQ, parțial | „După instalarea echipamentelor formația efectuează probele de sunet, care durează între 30-60 de minute.” | Se publică ora de sosire și durata probei, nu durata montajului. |

### B. Afirmații despre modul de lucru

| Rând | Verdict | Sursă | Citat verbatim | Motivul verdictului |
|---|---|---|---|---|
| B4 (echipa rămâne peste noapte, demontează dimineața) | N | — | Nimic. GM-FAQ spune doar că cazarea e cost suplimentar. | |
| B9 (oferta în aceeași zi, cu preț final) | N | GM-FAQ, contrar | „Vă contactam telefonic sau prin email și stabilim de comun acord o întâlnire pentru a discuta termenii și condițiile.” | „În aceeași zi primiți confirmarea disponibilității și oferta” de pe `ioana-balan.ro` e textul prototipului. Tot textul prototipului, IB-TC, spune că prețurile afișate au „caracter orientativ” și „nu constituie ofertă fermă”, în tensiune cu „preț ferm”. |
| B10 (piese cerute se pregătesc înainte) | N | GM-FAQ, parțial | „Putem aborda anumite piese muzicale pe care doriți in mod excepțional.” | Nu spune că se pregătesc înainte. „Cu cel puțin două săptămâni înainte, ca să le pregătim” de pe `ioana-balan.ro/faq/` e textul prototipului. |
| B21 (momente înainte de ultimul bac) | N | — | Nimic. | |
| B26 (oră-limită de sonor) | N | — | Nimic. | |
| B37 (ancorare pe vânt) | N | — | Nimic. | |
| B42 (boxe într-o curte) | N | — | Nimic. | |
| B43 (salon vecin, panou mobil) | N | — | Nimic. | |
| B46 (momente mutate mai devreme) | N | — | Nimic. | |
| B48 (umbră, joc după apus) | N | — | Nimic. | |
| B49 (cămin cultural, volum) | N | — | Nimic. | |
| B55 (MC cu sala și fotograful; DJ în pauze) | N | GM-FAQ, parțial | „DJ/MC-ul este cel care anunță toate momentele din cadrul evenimentului. Este necesar să fie informat din timp, pentru a asigura un discurs fluent.” · „Pe aceste perioade scurte(aproximativ 15 minute) DJ-ul își va desfășura programul.” | Partea cu DJ-ul în pauze e publicată; coordonarea cu sala și cu fotograful, care e angajamentul blocant, nu. |
| B57 (manele doar la cerere) | N | GM-FAQ · GM-OF · `ioana-balan.ro/faq/` | GM-FAQ: „Nu abordăm genul muzical “manele”.” · GM-OF: „1 interpret de muzică balcanica/manele(optional)*” · `ioana-balan.ro/faq/`: „acoperim și manele, muzică ușoară românească și internațională, în funcție de public.” | Sursele se contrazic (C1). |
| B60 (MC verifică programul cu sala) | N | GM-FAQ, parțial | „Este necesar să fie informat din timp, pentru a asigura un discurs fluent.” | Verificarea cu sala la începutul serii nu apare. |
| B61 (decalajul sălii: set lungit sau DJ) | N | GM-FAQ, parțial | „Acesta își va continua programul până cand pe ringul de dans mai rămân câteva persoane.” | Despre ring, nu despre decalajele sălii. |
| B64 (muzica se oprește la ruptul turtei) | N | — | Nimic. | |
| B65 (boxe opuse copilului) | N | — | Nimic. | |
| B66 (muzica se oprește la toast) | N | — | Nimic. | |
| B68 (ordinea vorbitorilor, semnal de intrare) | N | — | Nimic. `grand-music.ro` menționează evenimentele corporate doar generic. | |
| B69 (volum redus la fiecare fel) | N | — | Nimic. | |
| B74 (dansul mirilor trimis din timp) | N | `grand-music.ro/cele-mai-cautate-melodii-pentru-dansul-mirilor-2021/` (2021-01-24), parțial | „Exista formatii pentru nunta care pot interpreta live melodia aleasa de miri pentru vals.” | Afirmație generică despre piață, nu angajament. |
| B75 (piesele nedorite nu se cântă) | DV | GM-FAQ · `grand-music.ro/formatii-nunta-bucuresti/` (2025-06-13) · `grand-music.ro/formatii-nunta/` (2025-06-13) | GM-FAQ: „Totodată, dacă există anumite melodii pe care nu le doriți în cadrul programului artistic, acestea se pot exclude.” · „sa excludeti melodiile care nu va plac” · „sa le excludeti pe cele care nu va plac” | Doar pe grand-music.ro. |

### Sumar

| | confirmat | confirmat, de validat | neconfirmat |
|---|---|---|---|
| A (22) | 0 | 19 | 3 |
| B (22) | 0 | 1 | 21 |
| **Total (44)** | **0** | **20** | **24** |

După răspunsul clientului (2026-09-17), pe aceleași rânduri: **A** — 18 confirmate (A1–A12, A14, A17–A21), A24 de validat, A25–A27 neconfirmate. **B** — toate confirmate sau reformulate ca decizie per eveniment, cu excepția B26 și B43 (neconfirmate) și B75 (de validat). Detaliul e în `DECIZII-CLIENT.md`.

---

## 5. Contradicții între surse

| # | Subiect | Ce spun sursele | Rânduri atinse |
|---|---|---|---|
| C1 | Manele | GM-FAQ (2025-06-13): „Nu abordăm genul muzical “manele”.” · GM-OF (2026-01-03): „1 interpret de muzică balcanica/manele(optional)*” · `ioana-balan.ro/faq/`, editat pe live: „acoperim și manele” | B57, A36; `folclor-si-manele` |
| C2 | Plata restului | GM-FAQ: „DIFERENȚA de plată se va realiza în termen de 24h de la terminarea evenimentului.” · `ioana-balan.ro/faq/`: „Restul se plătește la finalul evenimentului.” · `ioana-balan.ro/oferte/`: „Restul se plătește în ziua evenimentului, înainte de începerea programului.” (text `answer-tbc` al prototipului, publicat fără marcaj) | neblocant pentru paginile noi; contradicție pe același domeniu |
| C3 | Raza de deplasare | `ioana-balan.ro/faq/`: „circa 500 km” · `ioana-balan.ro/` și `/oferte/`: „circa 300 km” · GM-OF: „disponibilă pentru deplasări în toate judetele României” | neblocant; contradicție pe același domeniu |
| C4 | Unde nu se percepe transport | GM-OF și GM-FAQ: gratuit în „București și Ilfov” · IB-TC: tariful se aplică „în afara localității de reședință a Prestatorului”, cu sediul în „sat Săftica, județul Ilfov” · `ioana-balan.ro/oferte/`: „din afara localității” | A2, A11, B5; `zona-ilfov` |
| C5 | Unde e valabilă grila | GM-OF: „valabile doar pentru București și Ilfov” · `ioana-balan.ro/oferte/`: „valabile pentru evenimente din 2026 și 2027”, fără restricție geografică | A1, A3–A12, A14 |
| C6 | Ofertă ferm vs. întâlnire | GM-FAQ: rezervarea trece printr-o întâlnire · `ioana-balan.ro` (textul prototipului): ofertă în aceeași zi | B9 |

---

## 6. Locațiile din lista clientei (18.09.2026)

### Metodă și avertisment

Clienta a trimis o listă de săli unde a cântat formația. Lista **nu e în repo**:
a venit în briefing, deja rescrisă, cu mențiunea că fusese verificată pe
18.09.2026. Am verificat-o din nou, independent, pe surse publice — site-uri
proprii ale locațiilor, agregatoare de nunți, pagini de Facebook — pentru **un
singur lucru: locația administrativă**.

Ce **nu** verifică această secțiune: că artista a cântat efectiv acolo. Asta e
afirmația clientei și rămâne pe răspunderea ei. Nicio sursă publică nu o poate
confirma, iar paginile o preiau ca atare.

Trei numere din brief nu se închid și le consemnez ca atare:

| Brief | Realitate |
|---|---|
| „cele 20 de locații plasate pe pagini" | **21**: 14 pe Ilfov + 3 pe Dâmbovița + 4 singulare |
| „cele 30 de locații" în această secțiune | **29** ar fi 21 + 8; documentate aici sunt **21** |
| „cele 8 locații din afara paginilor actuale (Tulcea, Galați, Vrancea, Vâlcea)" | **nu au nume în brief.** Nu se pot documenta. Vezi mai jos. |

### 6.1 Verdicte, pe locație

Legendă: **✓** localitatea din tabelul de brief se confirmă pe sursă publică ·
**≠** sursa publică dă altă localitate · **~** nume oficial diferit de cel din brief.

#### Pe `zona-ilfov.html` — grupul Ilfov

| # | Locație | Localitate (brief) | Verdict | Sursă |
|---|---|---|---|---|
| L1 | Cernica Events | Cernica | **≠** adresa publicată e Str. Ștrandului 52, **Pantelimon**, pe malul lacului Cernica | cernicaevents.ro; bestmarkets.ro |
| L2 | Toya Concept Events | Pantelimon | ✓ Str. Ștrandului 101, Pantelimon | toyaconcept.ro |
| L3 | Domeniile Săftica | Săftica | ✓ Calea București 51, Săftica | domeniilesaftica.ro |
| L4 | Noor Events | Popești-Leordeni | ✓ Splaiul Unirii 9D, Popești-Leordeni | noor-events.ro |
| L5 | Palatul Snagov | Snagov | ✓ Siliștea Snagovului, com. Snagov, pe malul lacului | palatulsnagovoficial.ro |
| L6 | Jubile Concept | Voluntari | ✓ Str. Emil Racoviță 7, Voluntari | jubile.ro |
| L7 | Velveto Embassy | Mogoșoaia | ✓ Str. Chitila Pădure 2 bis, Mogoșoaia — **~** numele complet e „Velveto Embassy Lake View" | velvetolakeview.ro |
| L8 | Domeniul cu Cireși | 1 Decembrie | ✓ Str. Giurgiului 9, com. **1 Decembrie, Ilfov** | domeniulcuciresi.ro |

#### Pe `zona-ilfov.html` — grupul București

| # | Locație | Verdict | Sursă |
|---|---|---|---|
| L9 | Autentic Events Hall | ✓ Str. Avionului 9, București | autenticeventshall.ro |
| L10 | Burlesque Events | ✓ B-dul Bucureștii Noi 48, Sector 1 | burlesque-events.ro |
| L11 | Twins by the Lake | ✓ Sector 2, București | twins-bythelake.ro |
| L12 | Palatul Bragadiru | ✓ Calea Rahovei 147–159, Sector 5, București — monument istoric, **nu** orașul Bragadiru din Ilfov | ro.wikipedia.org; zilesinopti.ro |
| L13 | Terra Events Hall | ✓ B-dul Lacul Tei 1, București | terraevents.ro |
| L14 | Monarh | ✓ Calea Plevnei 46–48 și Șos. Pipera 48, București | locatiilemonarh.ro |

#### Pe `zona-dambovita.html`

| # | Locație | Localitate (brief) | Verdict | Sursă |
|---|---|---|---|---|
| L15 | Cireșul Sălbatic | Butimanu | ✓ Pădurea Lucianca, DN1A, Butimanu, Dâmbovița — agregatoarele îl indexează sub „Buftea", care e doar reperul de drum | ciresulsalbatic.ro |
| L16 | Heritage Ballroom | Fieni | ✓ DC3, Fieni, Dâmbovița | heritageballroom.ro |
| L17 | Hanul Vlăsia | Gulia (Tărtășești) | ✓ Gulia, com. Tărtășești, pe DN7 — marcat `.ph` pe pagină, vezi 6.3 | restaurantguru.com; ghidul.ro |

#### Câte una pe pagină

| # | Pagină | Locație | Localitate | Verdict | Sursă |
|---|---|---|---|---|---|
| L18 | `zona-giurgiu` | TreeHouse Cosoba | Cosoba | ✓ Str. Principală, com. Cosoba, Giurgiu — **~** brieful scrie „Tree House", forma oficială e „TreeHouse", într-un cuvânt | treehouse.ro |
| L19 | `zona-arges` | Premier Ballroom | Curtea de Argeș | ✓ Str. Valea Iașului 99, Curtea de Argeș | firmania.ro; pagina oficială de Facebook |
| L20 | `zona-calarasi` | Hestia Park Lounge | Călărași | ✓ Șos. Chiciului 2a, Călărași, în complexul Hestia Hotel | hestia-hotel.ro |
| L21 | `zona-constanta` | Nuba Beach Club | Mamaia | ✓ Aleea Lamia, Mamaia, Constanța | nuba.ro |

### 6.2 Cele două corecturi de județ din brief — ambele se confirmă

| Locație | Clienta a spus | Corect | De ce a greșit |
|---|---|---|---|
| Domeniul cu Cireși | Giurgiu | **Ilfov** (com. 1 Decembrie) | strada se numește Giurgiului, iar comuna e lipită de granița cu județul Giurgiu |
| Hanul Vlăsia | Ilfov | **Dâmbovița** (Gulia, Tărtășești) | există un **Hanul Vlăsiei în Snagov, Ilfov** — altă firmă, alt loc |

### 6.3 Ce rămâne de confirmat cu clienta

| # | Item | De ce |
|---|---|---|
| S1 | **Cernica Events — Cernica sau Pantelimon?** | Toate sursele publice dau Pantelimon, Str. Ștrandului 52. Numele firmei și lacul sunt „Cernica", dar comuna Cernica e altă unitate administrativă. Pagina afișează **Cernica**, conform tabelului din brief. Dacă adresa publicată e cea corectă, rândul se schimbă în Pantelimon — și atunci L1 și L2 sunt două săli pe aceeași stradă, la 50 de numere distanță. |
| S2 | **Hanul Vlăsia — care dintre ele?** | Marcat `.ph` pe `zona-dambovita.html`: `[de confirmat: locația de pe DN7]`. Brieful indică drept risc un local omonim din Mamaia; riscul real, găsit la verificare, e **Hanul Vlăsiei din Snagov** — e și explicația pentru „Ilfov" din lista clientei. |
| S3 | **TreeHouse sau Tree House?** | Pagina scrie **TreeHouse Cosoba**, forma de pe site-ul propriu al locației, nu forma din brief. Un nume de firmă scris greșit pe o pagină publică e o eroare vizibilă pentru locație. |
| S4 | **Bacsoridana — Tecuci sau Valea Mărului?** | Ambele sunt în județul Galați. Nu e pe nicio pagină actuală. |
| S5 | **Brașov nu are nicio locație în lista clientei** | `zona-brasov.html` e layout A, construit pe trei carduri de locație plus card video plus recenzie — adică pagina care cere cel mai mult material și singura care n-a primit niciun nume. |
| S6 | **Cele 8 locații din Tulcea, Galați, Vrancea și Vâlcea** | Brieful le numără, dar nu le numește. Fără nume, nu pot fi nici verificate, nici documentate, nici folosite în runda următoare. **E nevoie de listă.** |

### 6.4 Notă de conținut, nu de verificare

`Nuba Beach Club` e beach club și destinație de nightlife, nu sală de nunți în
sensul celorlalte douăzeci. Locația găzduiește evenimente private („Events by
Nuba"), deci afirmația stă în picioare, dar registrul ei diferă de restul listei
și de tonul paginii, care e despre nunți și botezuri. De revăzut cu clienta dacă
e evenimentul pe care vrea să-l reprezinte pe `zona-constanta.html`.
