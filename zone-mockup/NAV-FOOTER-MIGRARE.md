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

### Măsurat pe demonstrația de pe `index.html`

Chromium, fereastră de 800 px înălțime, înălțimea elementului `<footer>`.

- **Canonic** = footer-ul fără coloane.
- **Demo v1** = coloanele cu linkurile câte unul pe rând (`ab54ef9`).
- **Demo v2** = varianta actuală: sub `sm` (640 px), linkurile din fiecare coloană
  curg câte două pe rând.

| Lățime | Canonic | Demo v1 | Demo v2 (actual) | v2 față de canonic | v2, în ecrane de 800 px |
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

### Ordinea pe mobil, de rezolvat la migrare

Sub 640 px, footer-ul de demonstrație se citește în ordinea: **contact (e-mail,
telefon) → ANPC · SAL → Servicii → Repertoriu → documente**. Coloanele stau unde cere
punctul 6 de mai sus, sub contact și înaintea documentelor, dar rândul ANPC · SAL rămâne
între contact și ele.

Ordinea e consecința structurii existente a benzii 2. Contactul și ANPC · SAL sunt două
jumătăți ale aceluiași rând flex (`flex-col sm:flex-row`), care pe desktop stau
stânga–dreapta și pe mobil se stivuiesc. Coloanele sunt un container separat, sub acest
rând. Pe demo nu s-a mutat nimic: ar fi cerut restructurarea benzii 2.

**La migrare**, când footer-ul se rescrie ca template unic în Elementor, se decide
ordinea pe mobil. Dacă ANPC · SAL trebuie să stea lângă documente, rândul de contact și
cel juridic devin containere separate. În Elementor, pe containere flexbox, ordinea se
poate regla și per breakpoint.

**Pentru Elementor:** cifrele din tabelul de mai sus (coloana „Demo v2”) sunt ce trebuie
reverificat pe template-ul de footer, la aceleași patru lățimi.

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
