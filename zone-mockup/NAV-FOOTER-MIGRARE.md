# Nav și footer — ce se schimbă la migrare

Specificație pentru template-ul de header și footer din Elementor Theme Builder.
Se aplică **o singură dată, în WordPress**. În prototip nu se face nicio modificare.

**De ce nu în prototip.** Header-ul și footer-ul sunt identice byte cu byte pe cele 20
de pagini din `zone-mockup/`, iar `verify/integritate.py` verifică asta. La migrare
devin un singur template. Orice modificare făcută acum ar trebui repetată pe 20 de
pagini, iar munca s-ar arunca la migrare.

Data: 2026-09-16.

---

## 1. Nav: „Zone” intră, „Blog” iese

| | |
|---|---|
| Etichetă | **Zone** |
| Țintă | hub-ul, `zone.html` în prototip; slug propus `/zone/` |
| Unde | nav desktop și drawer mobil, în ambele, **în locul lui „Blog”**, care trece în footer (§1.1, §2) |
| Ce **nu** intră în nav | `repertoriu`, `formatia`, `folclor-si-manele` și cele patru pagini de serviciu (`nunta`, `botez`, `eveniment-privat`, `corporate`). Ajung la ele prin footer (§2) și prin linkurile contextuale din corpul paginilor. |

### 1.1 Constrângerea de geometrie și compensarea aleasă

**Istoric.** Commit-ul `47a6265` a măsurat CTA-ul „Rezervă pe WhatsApp” ieșind din
container cu **229 px la 1024** și cu 101 px la 1440. Depășirea era ascunsă de
`body{overflow-x:hidden}`. Pentru a recupera spațiu, logo-ul a fost decupat la semnătură,
iar **„Acasă” a fost scos din nav-ul desktop** (rolul lui l-a preluat logo-ul). Nav-ul are
de atunci 7 intrări: Despre, Galerie, Discografie, Oferte, FAQ, Blog, Contact.

**Măsurătoarea de acum.** Chromium (Playwright), cu fonturile încărcate
(`document.fonts.status = loaded`), pe o copie a `zona-ilfov.html` din afara repo-ului. În
copie s-a adăugat în nav un link „Zone” cu clasele celorlalte intrări, în două poziții:
după „Oferte” și la final. **Cele două poziții dau aceleași cifre**, pentru că lățimea
totală e aceeași.

„Depășire conținut” = cât trece marginea dreaptă a CTA-ului de marginea dreaptă a zonei
de conținut (containerul interior minus `padding-right`). „Depășire viewport” = cât iese
CTA-ul din fereastră. O valoare negativă e spațiu rămas liber.

| Lățime | Nav acum (7) | CTA acum, depășire conținut / viewport | Nav cu „Zone” (8) | CTA cu „Zone”, depășire conținut / viewport |
|---|---|---|---|---|
| **1024** | 220,14 → 742,69 | **+28,41** / −35,59 | 220,14 → 800,02 | **+85,73 / +21,73** |
| 1100 | 243,94 → 766,48 | 0 / −64 | 220,14 → 800,02 | +9,73 / −54,27 |
| 1180 | 283,94 → 806,48 | 0 / −64 | 255,28 → 835,16 | 0 / −64 |
| 1280 | 277,94 → 896,48 | 0 / −104 | 276,14 → 968,02 | +69,73 / −34,27 |
| 1440 | 357,94 → 976,48 | 0 / −184 | 356,14 → 1048,02 | +69,73 / −114,27 |

„Zone” are 41,33 px lățime. Distanța dintre nav și CTA e 16 px sub `xl` și 32 px de la
`xl` în sus. La 1024, cu „Zone”, nav-ul și CTA-ul ajung la acest minim de 16 px, iar
nimic nu se mai comprimă.

**Ce înseamnă:**

1. **La 1024, header-ul actual e deja peste marginea zonei de conținut, cu 28 px.** CTA-ul
   intră în padding-ul din dreapta, dar rămâne în fereastră, cu 36 px liberi. E starea de
   la limită pe care o descrie brief-ul.
2. **Cu „Zone” adăugat ca atare, la 1024 CTA-ul iese din fereastră cu 21,73 px.**
   `overflow-x:hidden` îl taie fără bară de derulare, deci butonul principal de conversie
   apare trunchiat. E exact defectul reparat în `47a6265`.
3. **Problema nu e doar la 1024.** La 1100, 1280 și 1440, CTA-ul trece peste marginea de
   conținut cu 10–70 px. Dintre lățimile măsurate, doar la 1180 încap toate.
4. **Poziția intrării nu schimbă nimic**, deci nu există un loc în nav unde „Zone” să
   încapă gratuit.

**Consecință: „Zone” nu se adaugă fără o compensare.**

> **Compensarea aleasă: „Blog” trece din nav în footer, iar „Zone” îi ia locul.**
> Nav-ul rămâne la 7 intrări, deci lățimea e cea măsurată azi și nu apare nicio
> depășire nouă. Celelalte trei variante au fost respinse: hamburgerul până la 1280 nu
> rezolvă 1280 și 1440 și taie nav-ul pe laptopurile de 1024–1279; eticheta scurtată pe
> CTA sub `xl` sparge vocabularul CTA-ului pe o plajă de lățimi (CLAUDE.md §5); gap-ul
> redus la `xl` nu ajunge singur la nicio lățime.
>
> „Blog” și nu „FAQ”: blogul are patru carduri și un singur articol demonstrativ, iar
> FAQ-ul răspunde la obiecții comerciale. „Zone” duce la 13 pagini cu intenție
> comercială.
>
> Header-ul rămâne de măsurat în WordPress, dar condiția de acceptare e deja
> îndeplinită prin construcție: numărul de intrări nu crește.

**Varianta aleasă, măsurată.** Aceeași metodă, pe aceeași copie, cu „Zone” pus în locul
lui „Blog” în nav:

| Lățime | Nav azi (cu „Blog”) | Nav cu „Zone” în loc | CTA, depășire conținut / viewport: azi → cu „Zone” |
|---|---|---|---|
| **1024** | 220,14 → 742,69 | 220,14 → 743,22 | +28,41 / −35,59 → **+28,94 / −35,06** |
| 1100 | 243,94 → 766,48 | 243,67 → 766,75 | 0 / −64 → 0 / −64 |
| 1180 | 283,94 → 806,48 | 283,67 → 806,75 | 0 / −64 → 0 / −64 |
| 1280 | 277,94 → 896,48 | 277,67 → 896,75 | 0 / −104 → 0 / −104 |
| 1440 | 357,94 → 976,48 | 357,67 → 976,75 | 0 / −184 → 0 / −184 |
| 1920 | 597,94 → 1216,48 | 597,67 → 1216,75 | 0 / −424 → 0 / −424 |

„Zone” are 41,33 px, iar „Blog” ~40,8 px, cu ~0,5 px mai puțin. La 1100–1920 diferența
se absoarbe în centrarea nav-ului. La 1024, CTA-ul se mută cu 0,53 px spre dreapta și
rămâne în fereastră, cu 35 px liberi. **Depășirea de 28–29 px peste marginea de conținut
la 1024 exista deja și nu o produce schimbarea asta.** De aceea condiția de acceptare
pentru măsurătoarea din WordPress e: **nicio depășire în afara ferestrei, între 1024 și
1920, și nicio creștere față de header-ul de dinainte de migrare.** Condiția de pe
versiunea anterioară a acestui document („CTA-ul nu trece de marginea de conținut”) era
mai strictă decât header-ul de azi și nu era îndeplinită nici fără „Zone”.

**Istoricul analizei: variantele cântărite**, neordonate:

| Variantă | Ce câștigă | Ce costă |
|---|---|---|
| Hamburger până la `xl` (1280) în loc de `lg` (1024) | Rezolvă 1024–1279 fără să atingă intrările | Nu rezolvă 1280 și 1440 (+70 px). Laptopurile de 1024–1279 pierd nav-ul vizibil |
| Etichetă mai scurtă pentru CTA sub `xl` (de ex. „WhatsApp”) | ~100 px recuperați la 1024 | Vocabularul CTA-ului se schimbă pe o plajă de lățimi (CLAUDE.md §5, vocabular consecvent) |
| O intrare existentă trece în footer (candidat natural: FAQ sau Blog) | Lățimea rămâne cea de azi (7 intrări) | Decizie de arhitectură pe paginile din contractul de bază |
| `gap` mai mic între intrările din nav la `xl` (32 → 24 px) | ~56 px la 1280 și 1440 (7 spații × 8 px) | Rămân ~14 px peste marginea de conținut la 1280 și 1440, deci singur nu ajunge. Nu atinge 1024 |

Valorile din coloana „Ce câștigă” sunt **estimări** pornind de la lățimile măsurate, nu
măsurători. Nu se folosesc ca dovadă că o variantă încape.

**Nota despre sursă.** `RANDARE.md` dă, pentru paginile din rădăcină, nav-ul până la
735,98 și CTA-ul de 227,61 px la 1024. Pe paginile din `zone-mockup/` am măsurat 742,69 și
229,72. Diferența, de ~7 px, vine din pagini diferite, nu din metodă. De aceea
măsurătoarea finală se face pe template, nu pe prototip.

### 1.2 Drawer-ul mobil

„Blog” iese și din drawer, iar „Zone” îi ia locul. Drawer-ul rămâne la 8 itemi („Acasă” +
7), deci geometria din `RANDARE-MOBIL.md`, B5, rămâne valabilă: CTA-ul din josul
drawer-ului se termină la y = 646 la 390×844. Riscul din versiunea anterioară (un al
nouălea item care împingea CTA-ul la ~702 px) dispare. **De verificat oricum în
WordPress:** la 360×640, cel mai mic ecran din quality floor, 646 px depășesc deja
înălțimea ferestrei, deci drawer-ul trebuie să se deruleze, iar CTA-ul să rămână
accesibil, inclusiv la tastatură.

---

## 2. Footer, banda 2

### Starea de acum

Banda 2 are contactul în stânga (e-mail, telefon), ANPC · SAL în dreapta și, dedesubt, un
rând de documente: „Termeni și condiții · Politica de cookie-uri · **Zone deservite**”. Pe
toate cele 20 de pagini, „Zone deservite” are `href="#"`, pentru că hub-ul nu exista când
a fost scris footer-ul.

**Două familii de footer, nu una.** Cele 11 pagini din rădăcină au footer-ul canonic
fără „Zone deservite” (rândul de documente se oprește la „Politica de cookie-uri”), cu
căi fără `../`. Cele 20 din `zone-mockup/` îl au cu `href="#"`. Fiecare familie e
identică în interiorul ei. `verify/integritate.py` le verifică separat: paginile noi față
de `zona-brasov.html`, iar paginile din rădăcină între ele.

**Excepție: `index.html` are footer-ul de demonstrație** (2026-09-17, la cererea
clientului), cu tot ce descrie tabelul de mai jos. Celelalte 10 pagini din rădăcină și
cele 20 din `zone-mockup/` rămân pe footer-ul canonic. `integritate.py` tratează
diferența prin `FOOTER_DEMO`, marcată ca excepție temporară: la migrare footer-ul devine
un template unic, excepția se șterge, iar dacă `index.html` revine la footer-ul canonic
înainte de asta, verificarea pică și cere scoaterea excepției.

### Ce se adaugă

| Element | Linkuri | Slug propus |
|---|---|---|
| Coloană **„Servicii”** | Nuntă · Botez · Eveniment privat · Corporate | `/nunta/`, `/botez/`, `/eveniment-privat/`, `/corporate/` |
| Coloană **„Repertoriu”** | Repertoriu · Componența formației · Folclor și petrecere | `/repertoriu/`, `/formatia/`, `/folclor-si-manele/` |
| **„Zone deservite”** | hub-ul. **Înlocuiește `href="#"`** din rândul de documente | `/zone/` |
| **„Blog”** | arhiva de articole, adăugată **la finalul rândului de documente**, după „Zone deservite” | `/blog/` |

**De ce „Blog” stă în rândul de documente, nu într-o coloană.** Rândul acela e deja locul
linkurilor secundare care nu au intrare în nav: „Zone deservite” stă acolo din același
motiv. O coloană „Blog” ar avea un singur link sub un titlu, iar în coloanele „Servicii”
sau „Repertoriu” ar amesteca o arhivă de articole cu pagini de ofertă. Rândul devine:
„Termeni și condiții · Politica de cookie-uri · Zone deservite · Blog”. Ordinea pune
întâi documentele juridice, care erau deja acolo, apoi linkurile de navigație.

**Nu intră în footer:** cele 12 pagini de zonă, individual. Hub-ul le acoperă, iar 12
linkuri sitewide către pagini din aceeași categorie ar fi footer stuffing.

### De știut înainte de implementare

1. **Coloanele inversează o decizie anterioară.** Commit-ul `aedc92e` („Compact the
   footer and drop its navigation”) a scos navigația din footer, iar comentariul din banda
   2 spune explicit „fără titluri de coloană”. Titlurile „Servicii” și „Repertoriu” se
   marchează ca text (`p` sau `span`), **nu ca heading**, ca să nu apară în outline-ul
   fiecărei pagini.
2. **Etichetele urmează vocabularul paginilor:** „Folclor și petrecere” duce la
   `folclor-si-manele`, iar „Componența formației” la `formatia`. Pe paginile noi,
   linkurile contextuale folosesc aceleași formulări.
3. **„Corporate” depinde de un răspuns al clientului.** Nu e confirmat că se fac
   evenimente de firmă (`DECIZII-CLIENT.md`, D8). Dacă răspunsul e nu, linkul iese din
   footer, iar pagina și linkurile contextuale către ea se scot.
4. **Slug-urile paginilor de serviciu nu sunt confirmate.** Depind de D9 din
   `DECIZII-CLIENT.md` (specificația de 700 € și cele 7 slug-uri din Faza 3).
5. **Ținte de tap ≥ 44 px**, ca în restul footer-ului (`min-h-[44px]`).
6. **Pe mobil**, cele două coloane se stivuiesc sub contact, înaintea rândului de
   documente. Structura rămâne containere flexbox, fără grid.

### Demo v4 (actual): trei benzi, spațiere ajustată

Măsurat pe `index.html`, în Chromium. v3 a pus aceleași elemente pe trei benzi, doar cu
containere flexbox. v4 păstrează structura și ajustează spațierea din banda 1:
proporția coloanelor, înălțimea linkurilor pe desktop și marcajul D8.

```
Banda 1:  Logo + descriere (40%)   │  SERVICII            │  REPERTORIU
          E-mail                      Nuntă                  Repertoriu
          Telefon                     Botez                  Componența formației
                                      Eveniment privat       Folclor și petrecere
                                      Corporate *
                                      * de confirmat (D8)

Banda 2:  Social (4 iconițe)                                  ANPC · SAL

Banda 3:  Termeni · Cookie-uri · Zone deservite · Blog
          © 2026 · Proiect dezvoltat de · Site realizat de
```

Banda 2 și banda 3 sunt neschimbate față de v3. Rândul juridic e centrat, nu cu grupuri
la capete.

#### Pragurile alese

| Interval | Banda 1 | Linkuri din banda 1 | Banda 2 |
|---|---|---|---|
| ≥ 1024 (`lg`) | trei coloane pe un rând: brandul are 40% (`lg:basis-[40%]`), iar „Servicii” și „Repertoriu” sunt late cât conținutul (`lg:flex-none`). Restul de 60% se împarte în două goluri egale (`lg:justify-between`, cu `gap-x-16` ca minim) | 36 px (`lg:min-h-9`) | social stânga, ANPC · SAL dreapta |
| 640–1023 (`sm`, `md`) | brandul pe toată lățimea (`sm:basis-full`), „Servicii” și „Repertoriu” alăturate dedesubt | 44 px | la capete opuse |
| < 640 | totul stivuit; linkurile din fiecare secțiune câte două pe rând (`basis-1/2 sm:basis-auto`) | 44 px | stivuite, social deasupra |

**Proporția: de ce nu trei coloane 40 / 30 / 30.** Varianta literală (`lg:flex-[2]` pe
brand și `lg:flex-[1.5]` pe celelalte două coloane) s-a implementat și s-a măsurat. Golul
din dreapta a scăzut, dar golurile vizibile dintre coloane au ieșit inegale:

| La 1440 | v3 (coloane egale) | 40 / 30 / 30 | **v4 (40% + conținut)** |
|---|---|---|---|
| Brand: x / lățime | 184 / 314,7 | 184 / 377,6 | **184 / 428,8** |
| Servicii: x / lățime | 562,7 / 314,7 | 625,6 / 283,2 | **787 / 126,5** |
| Repertoriu: x / lățime | 941,3 / 314,7 | 972,8 / 283,2 | **1087,7 / 168,3** |
| Gol între coloane (între cutii) | 64 / 64 | 64 / 64 | **174,2 / 174,2** |
| Gol vizibil (textul coloanei → coloana următoare) | 70,4 / 144,6 | 82 / 220,7 | **181,8 / 174,2** |
| Gol vizibil la dreapta benzii 1 | 146,4 | 114,9 | **0** |

Cauza inegalității e **proporția**, nu `max-w-md` și nici `gap`. `gap-x-16` era uniform,
iar `max-w-md` (448 px) nu mai limitează nimic de la 1024 în sus, pentru că descrierea e
mai îngustă decât coloana. Golul apare pentru că „Servicii” folosește doar 126,5 px
(„Eveniment privat”) dintr-o coloană de 283 px, pe când textul brandului își umple
coloana. Cu coloanele aliniate la stânga, orice lățime fixă a coloanelor de linkuri
lasă gol după conținutul lor.

Ajustarea: brandul păstrează 40%, iar coloanele de linkuri se strâng la conținut. Cei
60% rămași se împart în două goluri egale între cutii. Diferența de 7,5 px dintre
golurile vizibile de la 1280 și 1440 vine din marginea dreaptă neregulată a descrierii
(descrierea se oprește la 421 px din 428,8). „Repertoriu” se termină exact la marginea
containerului, aliniat cu „SAL” din banda 2. Când „Componența formației” se scurtează la
„Formația”, golurile se reechilibrează singure.

| Coloane, x / lățime | 1024 | 1280 | 1440 |
|---|---|---|---|
| Brand | 64 / 358,4 | 104 / 428,8 | 184 / 428,8 |
| Servicii | 543,8 / 126,5 | 707 / 126,5 | 787 / 126,5 |
| Repertoriu | 791,7 / 168,3 | 1007,7 / 168,3 | 1087,7 / 168,3 |
| Goluri între cutii, 1→2 / 2→3 | 121,4 / 121,4 | 174,2 / 174,2 | 174,2 / 174,2 |
| Goluri vizibile, 1→2 / 2→3 | 124,6 / 121,4 | 181,8 / 174,2 | 181,8 / 174,2 |

În Elementor: containerul brandului are lățimea 40%, containerele de linkuri au lățime
automată, iar containerul-părinte are `justify-content: space-between` și gap de 64 px.

**Linkurile pe desktop: 36 px.** Cei 44 px sunt dimensiunea pentru ținta de tap. De la
1024 în sus, linkurile din banda 1 (e-mail, telefon, „Servicii”, „Repertoriu”) coboară la
36 px, cu `lg:min-h-9` din scara de spațiere implicită. Logo-ul și banda 2 rămân la
44 px. Sub 1024, toate linkurile au 44 px.

**Tranziția 1023 → 1024.** Pasul dintre linkuri trece de la 44 la 36 px exact la pragul
unde brandul urcă lângă coloane. Nu există nicio lățime cu linkuri de 36 px în aranjamentul
cu brandul deasupra sau cu linkuri de 44 px în aranjamentul pe trei coloane. Schimbarea de
ritm coincide cu schimbarea de aranjament (footer: 761 → 517 px), deci nu apare ca salt
separat.

**Marcajul D8, reformulat.** În v3, marcajul era un bloc mono cu contur, de 234 × 22,5 px:
`[CORPORATE — de confirmat, D8]`. Citea ca eroare și bloca trei coloane sub 1024. În v4,
linkul e „Corporate *”, iar sub ultimul link din coloană stă nota `* de confirmat (D8)`:
un `<p>` de 12 px (cea mai mică dimensiune din footer), `leading-5`, `text-secondary`.
Nota ocupă 20 px pe verticală. Rămâne vizibilă ca element de confirmat.

**Trei coloane de la 768: nu intră, pragul rămâne 1024.** Fără marcajul lat, lățimea
minimă a benzii 1 pe trei coloane e dată de e-mail, de cele două coloane de linkuri și de
goluri:

- v4 la 768: 40% × 640 = 256 px pentru brand + 126,5 + 168,3 + 2 × 64 = **678,8 px**,
  într-un container de 640 px. „Repertoriu” trece pe rândul următor. Verificat în
  randare, pe o copie temporară cu pragul mutat pe `md`: trei coloane pe un rând abia de
  la **833 px**.
- Coloane egale la 768: 170,7 px, sub lățimea e-mailului (220,9 px).
- 40 / 30 / 30 literal la 768: 153,6 px pe coloanele de linkuri, sub „Componența
  formației” (168,3 px).

Între 768 și 1024 nu există alt breakpoint (`tailwind.config.js` nu redefinește
`screens`), deci pragul rămâne la 1024. Blocajul nu mai e marcajul D8, ci suma
conținuturilor. Cu „Formația” în loc de „Componența formației”, pragul minim ar coborî la
aproximativ 794 px, tot peste 768.

**`max-w-md` rămâne pe descriere, nu pe coloana de brand** (din v3): pe coloană,
împiedica `basis-full` să ocupe rândul, iar între 640 și 1023 „Servicii” urca lângă brand.

#### Ritmul vertical

Benzile sunt separate de `gap-8` pe containerul footer-ului: 32 px între cutii, la toate
lățimile. Distanța vizibilă se măsoară de la ultimul element pictat dintr-o bandă (text,
imagine, SVG) până la primul element pictat din banda următoare:

| Distanță vizibilă | < 640 | 640–1023 | ≥ 1024 (v3) | **≥ 1024 (v4)** |
|---|---|---|---|---|
| Banda 1 → banda 2 | 56 | 47 | 56 la 1024, 49,5 la 1280/1440 | **52** |
| Banda 2 → banda 3 (rândul de documente) | 58 | 58 | 58 | **58** |
| Documente → juridic | 50 | 50 | 50 | **50** |

Banda 2 nu stă mai departe de banda 1 decât stă banda 3 de banda 2: 52 față de 58 px, cu
aceeași cutie de 32 px. **Clasa de spațiere nu s-a schimbat.** Dacă gap-ul ar scădea,
banda 1 → 2 ar coborî sub referința de 58 px și ritmul ar deveni inegal în sens invers.

Cei „~90 px” percepuți se măsoară de la **ultimul link din coloanele de linkuri**, nu de la
bandă. Coloanele sunt mai scurte decât brandul, care e cel mai înalt element din bandă
(212 px). La 1440, ultimul element pictat din fiecare coloană stă la:

| Până la banda 2 | Brand | Servicii | Repertoriu |
|---|---|---|---|
| v3 | 56 | 49,5 (marcajul D8); 84 de la „Corporate” | 128 |
| v4 | 52 | 71 (nota D8); 96 de la „Corporate *” | 132 |

Diferența vine din conținut: „Servicii” are 188 px și „Repertoriu” 132 px, față de 212 px
la brand. De la „Corporate *” până la iconițe sunt acum 96 px, cu 12 px mai mult decât în
v3: banda s-a scurtat cu 16 px, dar „Servicii” a pierdut 34,5 px (linkurile de 36 px și
nota în locul marcajului). Spațierea benzilor nu poate închide golul fără să strice
ritmul dintre ele.

#### Înălțimea footer-ului

Chromium, fereastră de 800 px înălțime, înălțimea elementului `<footer>` de pe
`index.html` (canonic = `e3c3a95`, v1 = `ab54ef9`, v2 = `29adebc`, v3 = `d8b0351`).

| Lățime | Canonic | Demo v1 | Demo v2 | Demo v3 | **Demo v4** | v4 față de v3 | v4 față de canonic |
|---|---|---|---|---|---|---|---|
| 360 | 605 | 1059,5 | 931,5 | 943,5 | **941** | −2,5 | +336 (+56%) |
| 768 | 489 | 727,5 | 727,5 | 791,5 | **789** | −2,5 | +300 (+61%) |
| 1024 | 437 | 675,5 | 675,5 | 557 | **517** | −40 | +80 (+18%) |
| 1280 | 437 | 675,5 | 675,5 | 533 | **517** | −16 | +80 (+18%) |
| 1440 | 437 | 675,5 | 675,5 | 533 | **517** | −16 | +80 (+18%) |

Pe capetele de interval, v4 măsoară: 869 px la 639, 757 px la 640 și 767, 761 px la 1023
(v3: 871,5 / 759,5 / 763,5). La 768, înălțimea (789) e peste cea de la 1023, pentru că
rândul juridic din banda 3 trece pe două linii.

- **Sub 1024: −2,5 px.** Nota D8 (20 px) înlocuiește marcajul (22,5 px). Pragul nu s-a
  mutat, deci aranjamentul e cel din v3.
- **1024: −40 px.** Brandul dă înălțimea benzii 1: două linkuri × 8 px, plus un rând de
  descriere (24 px). La 358 px, descrierea are trei rânduri în loc de patru (256 px în v3).
- **1280 și 1440: −16 px.** Brandul (212 px) dă înălțimea benzii 1: două linkuri × 8 px.

#### Celelalte verificări, v4

- Fără overflow orizontal (`scrollWidth` = `clientWidth`, deficit 0) la 360, 639, 640, 767,
  768, 1023, 1024, 1280 și 1440. Niciun element din footer nu trece de marginea dreaptă.
  Singurele elemente peste margine sunt în afara footer-ului, neatinse: drawer-ul mobil
  (fix, în afara ecranului) și decorul `absolute -bottom-6 -right-6` din conținut, cu 8 px,
  sub 768. Ambele sunt decupate.
- Ținte de tap: sub 1024, toate linkurile din footer au 44 px pe verticală. De la 1024,
  linkurile din banda 1 au 36 px, iar restul au 44 px. Excepție la toate lățimile:
  „Grand Music Events” din rândul juridic, cu 15 px, preexistent (D12).
- Titlurile rămân `<p>`; outline-ul paginii are aceleași 14 heading-uri.
- Zero tokeni sau culori noi. Clasele noi sunt utilitare flex și de spațiere din scara
  implicită (`lg:basis-[40%]`, `lg:flex-none`, `lg:justify-between`, `lg:min-h-9`,
  `leading-5`). Culoarea notei D8 e `text-secondary`, deja folosită în footer.
  `assets/styles.css` și `tailwind.config.js` au hash-uri identice.
- Header-ul, JSON-LD, tot ce e înainte de `<footer>` și după `</footer>`, banda 3: hash-uri
  identice față de v3.
- Ordinea pe mobil, neschimbată: brand (logo, descriere, e-mail, telefon) → Servicii →
  Repertoriu → social → ANPC · SAL → documente → juridic.

#### De rezolvat la migrare

1. **„Componența formației” se scurtează la „Formația”**, cum se numește și pagina.
   Pe demo nu s-a schimbat. La 360 ar evita ruperea pe două rânduri (+4 px). Pe desktop,
   coloana „Repertoriu” s-ar îngusta de la 168,3 la 145,2 px („Folclor și petrecere”), iar
   golurile egale se recalculează singure.
2. **Punctul median rămâne la capăt de rând.** În banda 3, la 360, rândul de documente se
   rupe după „Politica de cookie-uri ·”; la 768, rândul juridic se rupe după
   „Grand Music Events ·”. Separatorii sunt `<span>` între linkuri și nu dispar la rupere.
3. **„Grand Music Events” are 15 px ca țintă de tap** (rândul juridic, fără
   `min-h-[44px]`). Preexistent, pe toate cele 31 de pagini. Se repară o dată, în
   template-ul unic: `DECIZII-CLIENT.md`, D12.
4. **Iconițele sociale par decalate cu 12 px** față de textul de deasupra, acum că stau
   la stânga: fiecare link are `w-11` (44 px), cu iconița de 20 px centrată. În footer-ul
   canonic erau aliniate la dreapta, unde decalajul nu se vedea.
5. **Între 640 și 1023 footer-ul rămâne mai înalt decât în v2** (vezi tabelul). Marcajul D8
   nu mai e cauza: trei coloane cer minimum 833 px (794 px cu „Formația”). Dacă înălțimea
   contează pe tabletă, variantele sunt un gap mai mic sub 1024 sau un breakpoint
   intermediar în Elementor.

### Istoric: demo v1 și v2 (coloanele sub contact)

Chromium, fereastră de 800 px înălțime, înălțimea elementului `<footer>`.

- **Canonic** = footer-ul fără coloane.
- **Demo v1** = coloanele cu linkurile câte unul pe rând (`ab54ef9`).
- **Demo v2** = sub `sm` (640 px), linkurile din fiecare coloană
  curg câte două pe rând.

| Lățime | Canonic | Demo v1 | Demo v2 | v2 față de canonic | v2, în ecrane de 800 px |
|---|---|---|---|---|---|
| 360 | 605 px | 1059,5 px | **931,5 px** | +326,5 px (+54%) | 1,16 |
| 768 | 489 px | 727,5 px | 727,5 px | +238,5 px (+49%) | 0,91 |
| 1024 | 437 px | 675,5 px | 675,5 px | +238,5 px (+55%) | 0,84 |
| 1440 | 437 px | 675,5 px | 675,5 px | +238,5 px (+55%) | 0,84 |

Între 360 și 640, v2 măsoară: 927,5 px la 375–430 și 859,5 px la 480–639. La 480 px
rândul de documente încape pe o singură linie.

**Structura v2, sub 640 px.** „Servicii” și „Repertoriu” rămân blocuri stivuite unul sub
altul. În fiecare, containerul de linkuri e `flex flex-row flex-wrap sm:flex-col`, iar
fiecare link are `basis-1/2 sm:basis-auto`: „Servicii” 2×2, „Repertoriu” 2+1. S-a ales
`flex-wrap` în locul a două containere pe coloană, pentru că păstrează ordinea din DOM
(Nuntă, Botez, Eveniment privat, Corporate) și se anulează la `sm` cu o singură clasă.
Fără `<details>`: conținutul se scanează oricum, iar un accordion ar adăuga JS de
întreținut la migrare. De la 640 px, comportamentul e cel din v1.

**Ținta de sub 900 px la 360 nu e atinsă: 931,5 px.** Ce adaugă v2 peste footer-ul
canonic la 360:

| Element | px |
|---|---|
| „Servicii”: titlu 24 + 2 rânduri de linkuri 88 + marcaj D8 22,5 | 134,5 |
| gap între cele două blocuri | 16 |
| „Repertoriu”: titlu 24 + 2 rânduri de linkuri 92 | 116 |
| gap-ul benzii 2, înaintea blocului de coloane | 16 |
| al doilea rând de documente („Zone deservite · Blog”) | 44 |
| **Total** | **326,5** |

Rândurile de linkuri dau 4 × 44 px = 176 px, ca în calcul. Restul vine din titluri,
marcajul D8, cele două gap-uri și rândul de documente care se rupe. În plus, la 360 px
„Componența formației” nu încape în jumătatea de 164 px și trece pe două rânduri, deci
rândul ei are 48 px în loc de 44 (la 320 px se întâmplă la fel și cu „Folclor și
petrecere”). Fără ruperea asta, înălțimea ar fi 927,5 px, tot peste 900.

- La trecerea 639 → 640, linkurile trec direct de la două pe rând la unul pe rând, cu
  coloanele alăturate. Nu există o lățime intermediară cu aspect rupt. Între 480 și 639,
  a doua coloană de linkuri pornește de la jumătatea lățimii, deci aspectul e aerisit.
- La 360 px, rândul de documente se rupe după „Politica de cookie-uri ·”: punctul median
  rămâne la capătul primului rând.
- De la `sm`, creșterea e fixă (+238,5 px): înălțimea coloanei „Servicii” (titlu,
  4 linkuri, marcaj).
- Fiecare link nou are minimum 44 px pe verticală, la toate lățimile: 44 px, sau 48 px
  unde eticheta trece pe două rânduri.
- Titlurile „Servicii” și „Repertoriu” sunt `<p>`: outline-ul paginii are aceleași 14
  heading-uri ca înainte.
- Fără overflow orizontal la nicio lățime (`scrollWidth` = `clientWidth`).
- Marcajul `[CORPORATE — de confirmat, D8]` folosește tokeni existenți (`text-outline`,
  `bg-surface-container`, `border-outline/40`), pentru că `.ph` e definită doar în
  `<style>`-ul paginilor din `zone-mockup/`.

**Pentru Elementor:** cifrele din tabelul de înălțimi v4 sunt ce trebuie reverificat pe
template-ul de footer, la aceleași cinci lățimi, plus golurile egale dintre coloane
(174,2 px la 1440) și golul de 0 px din dreapta benzii 1.

---

## 3. Starea de activ

| Pagină | În prototip | La migrare |
|---|---|---|
| Hub (`zone`) | nicio intrare activă | **„Zone” activ** |
| Cele 12 pagini de zonă | nicio intrare activă | **„Zone” activ** |
| Cele 4 pagini de serviciu | nicio intrare activă | nicio intrare activă (nu au intrare în nav) |
| `repertoriu`, `formatia`, `folclor-si-manele` | nicio intrare activă | nicio intrare activă (nu au intrare în nav) |
| `blog`, `articol` (contract de bază) | „Blog” activ | **nicio intrare activă**: „Blog” nu mai e în nav. Linkul din footer nu primește stare de activ |

**În prototip nu se schimbă nimic.** Pe paginile noi, abaterea documentată în comentariul
de deasupra header-ului („Oferte” și-a pierdut starea de activ) rămâne cum e.

**Marcarea în WordPress.** Starea de activ trebuie să apară și pe hub, și pe cele 12
pagini de zonă, deci nu ajunge potrivirea exactă de URL. Două căi, de ales la
implementare:

- **Paginile de zonă ca pagini-copil ale hub-ului.** WordPress adaugă atunci clase de
  strămoș pe intrarea din meniu. **De verificat** că widget-ul de nav din Elementor aplică
  stilul de activ și pe aceste clase, nu doar pe `current-menu-item`. Varianta leagă
  structura de URL-uri de navigație (`/zone/brasov/` în loc de `/zona-brasov/`), deci e
  și o decizie de SEO și de redirecționări (Faza 5).
- **O clasă adăugată pe template-ul paginilor de zonă.** Nu leagă URL-urile, dar adaugă
  CSS custom, pe care CLAUDE.md §8 îl limitează.

Drawer-ul mobil primește aceeași stare ca nav-ul desktop.

---

## 4. Verificare înainte de publicarea template-ului

- [ ] Mutarea „Blog” confirmată în scris de client (D10 — modifică header-ul canonic, contract de bază)
- [ ] „Blog” scos din nav-ul desktop și din drawer; „Zone” în locul lui, în ambele
- [ ] „Blog” adăugat la finalul rândului de documente din footer, cu țintă de tap ≥ 44 px
- [ ] Pe `blog` și `articol`, nicio intrare de nav activă
- [ ] Header măsurat la 1024, 1100, 1280, 1440 și 1920: CTA-ul nu iese din fereastră, iar depășirea peste marginea de conținut nu crește față de header-ul de dinainte (azi: +28,41 px la 1024, 0 în rest)
- [ ] Nicio bară de derulare orizontală, verificat cu `overflow-x:hidden` scos temporar
- [ ] Drawer la 360×640, cu 8 itemi: se derulează, CTA-ul se atinge și se ajunge la el cu tastatura
- [ ] „Zone deservite” din footer duce la hub, nu la `#`
- [ ] Coloanele din footer au titluri care nu sunt heading-uri
- [ ] „Zone” activ pe hub și pe toate cele 12 zone; inactiv pe servicii și pe cluster
- [ ] „Corporate” și slug-urile de serviciu, confirmate (D8, D9)

---

## 5. Modulul de locații — pattern de migrare

Adăugat pe 18.09.2026, odată cu lista de locații trimisă de clientă. Documentat
aici, nu într-un fișier nou, pentru că e al treilea bloc care se repetă
byte-identic pe mai multe pagini de zonă, după nav și footer.

### Ce e

O secțiune care listează sălile unde a cântat formația, în județul paginii.
Conține **doar nume și localitate** — atât avem. Fără an, fără tip de eveniment,
fără fotografie, clip sau recenzie legată de locație, fără link către site-ul
sălii.

### Regula de formă

| Locații pe pagină | Ce primește pagina |
|---|---|
| 2 sau mai multe | secțiune dedicată, cu listă, imediat după „Localități deservite” |
| exact 1 | o frază în „Localități deservite”; fără secțiune |
| 0 | nimic |

Pragul nu e estetic. O secțiune cu titlu, eyebrow și card pentru un singur nume
citește ca un slot gol, exact efectul pe care layout-ul C a fost construit să-l
evite („patru sloturi punctate goale nu comunică «urmează material», ci «nu avem
nimic aici»", `zona-giurgiu.html`).

### Unde e implementat azi

- **Secțiune:** `zona-ilfov.html` (14 locații, două subgrupuri) și
  `zona-dambovita.html` (3). Markup **identic** între ele; diferă doar
  eticheta de subgrup, titlul, intro-ul, nota și rândurile din listă.
- **Frază:** `zona-giurgiu.html`, `zona-arges.html`, `zona-calarasi.html`,
  `zona-constanta.html` — câte o locație fiecare.

Pe `zona-constanta.html` (layout B) cardurile `.ph-zone` de la secțiunea 4
**rămân goale**: un nume nu umple un card care cere fotografie sau clip.

### Consecință pentru exemplele de layout C

`zona-giurgiu.html` a fost până acum exemplul canonic de layout C — zonă fără
niciun material de dovadă. Nu mai e: pagina numește acum TreeHouse Cosoba.
Exemplul curat de layout C **trece pe `zona-prahova.html`**, singura pagină care
păstrează toate cele trei absențe (fără locații, fără card video, fără recenzie)
și zero `.ph-zone`. Referința rămâne valabilă pentru structura de secțiuni,
nu pentru „zero locații".

### În Elementor

Modulul devine un **repeater ACF** pe template-ul de zonă:

| Câmp | Tip | Obligatoriu | Note |
|---|---|---|---|
| `nume` | text | da | numele sălii, exact cum îl scrie ea |
| `localitate` | text | da | localitatea administrativă, nu cea de pe firmă |
| `grup` | select | nu | eticheta de subgrup; gol = un singur grup |

Randarea: un container flexbox per grup, cu eticheta ca `<p>` (nu heading — vezi
mai jos), și lista ca `<ul>`. Nimic din modul nu cere grid complex, overlap sau
poziționare absolută, deci trece în containere flexbox fără CSS custom
(CLAUDE.md §8).

### Trei reguli care trebuie să supraviețuiască migrării

1. **Etichetele de subgrup nu sunt heading-uri.** Pe `zona-ilfov.html`,
   „Ilfov" și „București" sunt `<p>` cu stil de label. Un `<h3>București</h3>`
   ar băga termenul principal al site-ului în outline-ul unei pagini de județ.
   Modulul adaugă paginii **un singur H2**.
2. **Localitatea e cea administrativă.** `Domeniul cu Cireși` e la 1 Decembrie,
   Ilfov, deși strada se numește Giurgiului și comuna e lipită de județul
   Giurgiu. Numele străzii și cel al firmei nu decid județul.
3. **Nimic nu se completează din memorie.** Dacă lipsește localitatea, rândul
   primește `.ph`, nu o presupunere. Vezi `Hanul Vlăsia` pe
   `zona-dambovita.html`.

### Verificare

`verify/integritate.py` nu validează conținutul modulului — numele de săli nu
sunt verificabile programatic. Verdictele per locație stau în `SURSE-LIVE.md`,
§6.
