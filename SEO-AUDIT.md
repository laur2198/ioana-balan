# Audit SEO tehnic și on-page

**Obiect:** prototipul static din acest repo, 11 fișiere HTML.
**Data:** 3 septembrie 2026 · commit `dde9247` · branch `merge-oferte-servicii`
**Metodă:** parsare DOM (BeautifulSoup) pentru structură, meta și JSON-LD;
randare reală în Chromium headless la 375 / 768 / 1280 px, DPR 1, pentru
dimensiunile efective ale imaginilor și greutatea paginilor; shingles de 6
cuvinte pentru suprapunerea de conținut.

Fără scor numeric. Prototipul nu are domeniu propriu și nu are date de trafic;
orice cifră agregată ar fi inventată.

---

## Excluderi — semnalate o dată, nu se mai repetă

Următoarele sunt intenționate și **nu** sunt raportate ca erori:

1. **`canonical` și `og:url` indică `https://ioana-balan.ro/`** în timp ce
   prototipul rulează pe GitHub Pages. Corect pentru destinația finală.
2. **`noindex, follow` pe `politica-cookie.html` și `termeni-si-conditii.html`.**
   Corect: pagini juridice, fără valoare de căutare, dar care trebuie să
   transmită link equity.
3. **Prețurile lipsesc din grila de pachete** și **15 din 17 răspunsuri FAQ sunt
   provizorii.** Comentariul din `faq.html:32-35` documentează explicit că
   `FAQPage.mainEntity` conține doar cele 2 răspunsuri validate de client —
   decizie corectă, structured data se citește ca informație fermă.

Consecință tehnică a punctului 3, menționată aici o singură dată: blocul
`Product`/`Offer` din `oferte.html` nu poate fi valid cât timp `price` lipsește.
Reapare mai jos ca M2 doar fiindcă briefingul cere lista câmpurilor obligatorii
absente pentru fiecare tip declarat.

---

## 1. Ierarhie de titluri

Un singur `<h1>` pe fiecare din cele 11 pagini. Zero pagini fără H1, zero pagini
cu H1 multiplu. Un singur salt de nivel în tot site-ul.

### index.html
```
L121  H1  Formație Nuntă București Premium: Muzică de Petrecere Autentică
L148    H2  Muzică pentru nuntă, botez și corporate
L154      H3  Muzică Nuntă
L160      H3  Muzică Botez
L166      H3  Corporate
L182    H2  Pachete pentru 2026–2027
L214    H2  Peste 15 ani pe scenă
L238    H2  Vezi cum arată un eveniment
L273    H2  Ce Spun Mirii și Gazdele
L324    H2  Ce ne întrebați cel mai des
L331      H3  Prețul unei formații pentru 2026-2027?
L343      H3  Cântați și în afara Bucureștiului?
L355      H3  Cum rezerv data — avans și contract?
L372    H2  Rezervă Formație Nuntă
```

### despre.html
```
L118  H1  Despre mine
L150    H2  Rădăcini
L171    H2  Primii pași
L187    H2  Hai să ne cunoaștem
```

### galerie.html
```
L98   H1  Galerie de Spectacole
L109    H2  Cum arată un eveniment
L243    H2  Esența Tradiției în Imagini.
```

### discografie.html
```
L125  H1  Hai să nu ne mai mințim
L141    H2  Melodii noi Ioana Balan
L223    H2  Arhiva Sonoră Ioana Balan
L233      H3  Glasul Inimii
L248      H3  Rădăcini
L264    H2  Îți place ce auzi? Rezervă data ta.
```

### oferte.html
```
L115  H1  Pachete și prețuri pentru nuntă și botez
L124    H2  Condiții comerciale
L139    H2  Patru pachete, pentru nuntă și pentru botez
L147      H3  Pachet Standard
L177      H3  Pachet Premium
L217      H3  Pachet Standard        ← repetat (tab Botez)
L244      H3  Pachet Premium         ← repetat (tab Botez)
L285    H2  Acoperire
L297    H2  Preț, rezervare și contract
L304      H3  Prețul unei formații pentru 2026-2027?
L316      H3  Cum rezerv data — avans și contract?
L325      H3  Cât este avansul și când se achită restul?
L334      H3  Cu cât timp înainte ar trebui să vă contactez?
L343      H3  Ce se întâmplă dacă trebuie să amân evenimentul?
L359    H2  Verificați dacă data este liberă
```

### faq.html
```
L130  H1  Ce ne întrebați cel mai des
L146    H2  Preț
L152      H3  Prețul unei formații pentru 2026-2027?
L161    H2  Rezervare și contract
L170      H3  Cum rezerv data — avans și contract?
L179      H3  Cât este avansul și când se achită restul?
L188      H3  Ce se întâmplă dacă trebuie să amân evenimentul?
L197      H3  Cu cât timp înainte ar trebui să vă contactez?
L206    H2  Prestația
L212      H3  Ce tipuri de evenimente acoperă Ioana Balan?
L224      H3  Cât durează programul?
L233      H3  Pot cere o piesă anume pentru un moment special?
L242      H3  Cântați și muzică ușoară, sau doar populară?
L254      H3  Ce se întâmplă în pauzele formației?
L263    H2  Tehnic și locație
L269      H3  Ce echipament aduceți și ce trebuie să asigure locația?
L278      H3  De cât spațiu aveți nevoie pentru scenă?
L287      H3  Cântați și la evenimente în aer liber?
L296      H3  Aveți nevoie de masă pentru formație?
L305    H2  Deplasare
L314      H3  Cântați și în afara Bucureștiului?
L323      H3  Cum se calculează costul deplasării?
L332      H3  Ce se întâmplă la distanțe mari, unde e nevoie de cazare?
L343    H2  Nu ați găsit răspunsul?
```
Cea mai curată ierarhie din site: 6 categorii H2, întrebările ca H3 sub ele.

### contact.html
```
L116  H1  Rezervări și Contact Ioana Balan
L169    H2  Cere ofertă personalizată
```

### blog.html
```
L113  H1  Sfaturi și Inspirație pentru Evenimente Memorabile
L132    H2  Cum să alegi formația de nuntă perfectă în 2026
L148    H2  Muzica populară vs. Muzica ușoară la botez
L164    H2  Repertoriul de muzica populara nunta: Tendințe actuale
L180    H2  Cum transformi un eveniment privat într-un spectacol premium
L193      H3  Primește Noutăți        ← sidebar newsletter
L203      H3  Tag-uri SEO             ← sidebar, jargon vizibil publicului
```

### articol.html
```
L108  H1  Importanța luminilor de scenă pentru show-ul formației
L122    H3  „Lumina nu doar luminează, ea transformă spațiul..."   ← SALT H1→H3
L131    H2  Atmosfera și Dinamica Vizuală
L143    H2  Profesionalismul din Spatele pupitrului
L153    H2  Plănuiți un eveniment?
```

### politica-cookie.html
```
L105  H1  Politica de cookie-uri
L131..L249  H2 ×9 (1. … 9. Contact), cu H3 3.1–3.3 sub „3. Ce cookie-uri folosim"
```

### termeni-si-conditii.html
```
L106  H1  Termeni și condiții
L139..L381  H2 ×16 (1. … 16. Contact), cu H3 12.1–12.7 sub „12. Prelucrarea datelor"
```

**Constatări:**

- **Un singur salt de nivel:** `articol.html:122`, H1 → H3.
- **Titlu folosit pentru stilizare, nu pentru structură:** același
  `articol.html:122` — un citat decorativ din caseta glass, marcat H3 pentru
  dimensiunea fontului. Nu deschide nicio secțiune.
- **Titlu care nu descrie pagina:** `discografie.html:125` — H1 este numele
  albumului, nu subiectul paginii.
- **Jargon intern vizibil:** `blog.html:203` — H3 „Tag-uri SEO".
- **Titluri duplicate în aceeași pagină:** `oferte.html` — perechea „Pachet
  Standard" / „Pachet Premium" apare de două ori (L147/L177 pentru nuntă,
  L217/L244 pentru botez), fără ca H3-ul să conțină tipul de eveniment.

---

## 2. Meta

| Pagină | title | n | description | n | canonical | robots | lang |
|---|---|---:|---|---:|---|---|---|
| index.html | Ioana Balan \| Formație Nuntă București Premium & Muzică de Petrecere | **68** | Ioana Balan - Formație nuntă București premium… 2026-2027. | **171** | `/` | — | ro |
| despre.html | Despre mine \| Ioana Balan | **25** | Ioana Balan povestește de unde vine dragostea… | 159 | `/despre.html` | — | ro |
| galerie.html | Galerie \| Ioana Balan — Formație Nuntă București | 48 | Galerie foto și video Ioana Balan… Pitești. | **173** | `/galerie.html` | — | ro |
| discografie.html | Discografie \| IOANA BALAN - Muzică Populară și de Petrecere | 59 | Explorează discografia completă… „Rădăcini". | 153 | `/discografie.html` | — | ro |
| oferte.html | Pachete și Prețuri 2026-2027 \| Ioana Balan | 42 | Pachete de muzică pentru nuntă și botez… duminică. | **161** | `/oferte.html` | — | ro |
| faq.html | Întrebări frecvente \| Ioana Balan | 33 | Răspunsuri despre rezervare și contract… Ioana Balan. | **177** | `/faq.html` | — | ro |
| contact.html | Contact Ioana Balan \| Rezervări Evenimente și Colaborări Muzicale | **65** | Contactați-o pe Ioana Balan… Consultanță muzicală gratuită. | **174** | `/contact.html` | — | ro |
| blog.html | Blog \| Ioana Balan - Sfaturi și Inspirație pentru Evenimente Memorabile | **71** | Blog Ioana Balan: sfaturi pentru nunți… memorabile. | **162** | `/blog.html` | — | ro |
| articol.html | Importanța luminilor de scenă pentru show-ul formației \| Ioana Balan | **68** | Importanța luminilor de scenă… pentru evenimente. | 159 | `/articol.html` | — | ro |
| politica-cookie.html | Politica de cookie-uri \| Ioana Balan | 36 | Cum folosește site-ul ioana-balan.ro modulele cookie… | **181** | `/politica-cookie.html` | noindex, follow | ro |
| termeni-si-conditii.html | Termeni și condiții \| Ioana Balan | 33 | Condițiile de utilizare a site-ului… date cu caracter personal. | **191** | `/termeni-si-conditii.html` | noindex, follow | ro |

**Open Graph / Twitter — identic ca structură pe toate cele 11 pagini:**

| Câmp | Stare |
|---|---|
| `og:title` | prezent pe 11/11, identic cu `<title>` |
| `og:description` | prezent pe 11/11, identic cu `meta description` |
| `og:image` | prezent pe 11/11 — **același fișier peste tot**: `assets/og-ioana-balan.png` (43 KB) |
| `og:image:width` / `:height` / `:alt` | prezente pe 11/11 (1200×630) |
| `og:url` | prezent pe 11/11, egal cu `canonical` |
| `og:type` | `website` ×8, `article` (articol), `profile` (despre) — corect diferențiat |
| `og:locale` | `ro_RO` pe 11/11 |
| `og:site_name` | `Ioana Balan` pe 11/11 |
| `twitter:card` | `summary_large_image` pe 11/11 |
| `twitter:title` / `:description` | **absente pe `politica-cookie.html` și `termeni-si-conditii.html`** |
| `twitter:image` / `:image:alt` | prezente pe 11/11 |
| `hreflang` | absent peste tot — corect, site monolingv |
| `viewport` | `width=device-width, initial-scale=1.0` pe 11/11 |

**Constatări:** zero duplicate de title, zero duplicate de description, zero
lipsuri de canonical, zero lipsuri de lang. 4 titluri peste 60 de caractere, 1
sub 30, 8 descrieri peste 160.

---

## 3. Structured data

Toate cele 9 blocuri JSON-LD sunt **valide sintactic** (parsare `json.loads`
fără eroare). `politica-cookie.html` și `termeni-si-conditii.html` nu au JSON-LD
— corect pentru pagini `noindex`.

| Pagină | Linie | Tip | `@id` | Observație |
|---|---|---|---|---|
| index.html | 31 | `MusicGroup` | `https://ioana-balan.ro/#artist` | singurul loc cu `sameAs` |
| contact.html | 31 | `EntertainmentBusiness` | `https://ioana-balan.ro/#artist` | **același `@id`, alt `@type`** |
| despre.html | 32 | `AboutPage` | — | `mainEntity` → `#artist` ✓ |
| faq.html | 36 | `FAQPage` | `…/faq.html#faq` | `about` → `#artist` ✓ |
| oferte.html | 35 | `Product` + 4× `Offer` | — | fără `price`, fără `image` |
| galerie.html | 27 | `ImageGallery` | — | `about` = `MusicGroup` inline |
| discografie.html | 29 | `@graph`: 3× `MusicAlbum` | — | `byArtist` = 3 noduri anonime |
| blog.html | 28 | `@graph`: `Blog` + `BreadcrumbList` | `…/blog.html` | `publisher` = `Organization` |
| articol.html | 30 | `BlogPosting` | — | `mainEntityOfPage` → `articol.html` |

**`sameAs`:** prezent o singură dată, în `index.html:31`, cu 5 profiluri
(Facebook, Instagram, TikTok, YouTube, Pinterest). Corect — nu se repetă.

**`FAQPage`:** declarat exclusiv pe `faq.html`. Corect. Acordeoanele vizuale de
pe `index.html:324-368` și `oferte.html:297-355` nu poartă markup, deci nu
concurează.

### Câmpuri obligatorii / recomandate lipsă, pe tip

| Tip | Lipsă |
|---|---|
| `MusicGroup` (index) | `image`, `logo`, `aggregateRating` |
| `EntertainmentBusiness` (contact) | `openingHoursSpecification`, `geo`, `priceRange` e `"$$"` (nespecific pentru piața RO), `aggregateRating` |
| `Product` (oferte) | `image` (obligatoriu), `aggregateRating`/`review` |
| `Offer` ×4 (oferte) | **`price` sau `priceSpecification`** (obligatoriu), `url`, `validFrom`/`priceValidUntil` |
| `MusicAlbum` ×3 | `@id`, `url`, `image`, `byArtist` nelegat de `#artist` |
| `BlogPosting` (articol) | `publisher.logo` (`ImageObject`), `author.url`, `isPartOf` → `Blog` |
| `ImageGallery` (galerie) | `image` / `associatedMedia`, `about` nelegat de `#artist` |
| `Blog` (blog) | `blogPost` (lista articolelor) |

### Tipuri relevante care lipsesc complet

| Tip absent | De ce contează aici |
|---|---|
| `AggregateRating` + `Review` | 5,0★ / 61 recenzii Google e, conform CLAUDE.md §4, activul cel mai subutilizat. Nu apare nici ca text, nici ca markup. Atenție: politica Google interzice `aggregateRating` auto-declarat pe `LocalBusiness`/`Organization` pentru rich results, iar recenziile nu se copiază de pe Google. Locul corect e un `Review`/`AggregateRating` pe `Product` (pachete) sau afișare textuală + link către profilul Google. |
| `VideoObject` | 7 videoclipuri pe site (`index.html` ×2, `galerie.html` ×5), montate ca facade cu `data-yt`. Fără `VideoObject`, niciunul nu e eligibil pentru rezultate video. CLAUDE.md §4: video în hero e diferențiatorul pe care doar un concurent din 8 îl are. |
| `BreadcrumbList` | prezent doar pe `blog.html`. Absent pe celelalte 8 pagini indexabile. |
| `Service` / `OfferCatalog` | Ce vinde ea e un serviciu, nu un `Product`. `Service` cu `areaServed` pe cele 5 orașe leagă corect oferta de SEO-ul local din §9 CLAUDE.md. |
| `WebSite` | declarat doar ca `isPartOf` inline pe două pagini, fără `@id` propriu. Nod rădăcină lipsă. |
| `ContactPoint` | `contact.html` are telefon și e-mail în text, dar fără `contactPoint` cu `contactType`/`availableLanguage`. |
| `Person` | Ioana Balan e persoană publică. `MusicGroup` acoperă formația, nu artista. |

---

## 4. Linking intern

### Matrice (număr de linkuri, sursă → destinație)

| de la ↓ / către → | artic | blog | cont | desp | disc | faq | gal | index | ofer | cook | term |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| articol.html | – | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 |
| blog.html | **4** | – | 2 | 2 | 2 | 2 | 2 | 3 | 2 | 1 | 1 |
| contact.html | 0 | 2 | – | 2 | 2 | 2 | 2 | 3 | 2 | 1 | **2** |
| despre.html | 0 | 2 | 2 | – | 2 | 2 | 2 | 3 | 2 | 1 | 1 |
| discografie.html | 0 | 2 | 2 | 2 | – | 2 | 2 | 3 | 2 | 1 | 1 |
| faq.html | 0 | 2 | 2 | 2 | 2 | – | 2 | 3 | 2 | 1 | 1 |
| galerie.html | 0 | 2 | 2 | 2 | 2 | 2 | – | 3 | 2 | 1 | 1 |
| index.html | 0 | 2 | 2 | 2 | 2 | **3** | **3** | – | **7** | 1 | 1 |
| oferte.html | 0 | 2 | 2 | 2 | 2 | **3** | 2 | 3 | – | 1 | 1 |
| politica-cookie.html | 0 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | – | **2** |
| termeni-si-conditii.html | 0 | 2 | 2 | 2 | 2 | 2 | 2 | 3 | 2 | **2** | – |

Fundalul de 2–3 linkuri este header + footer, identic pe toate paginile. Cifrele
îngroșate sunt singurele linkuri redacționale.

### Linkuri redacționale (doar din `<main>`, fără header/footer/nav)

| Destinație | Inbound editorial | Din |
|---|---:|---|
| oferte.html | 5 | index.html |
| articol.html | 4 | blog.html |
| faq.html | 2 | index.html, oferte.html |
| termeni-si-conditii.html | 2 | contact.html, politica-cookie.html |
| galerie.html | 1 | index.html |
| politica-cookie.html | 1 | termeni-si-conditii.html |
| **index.html** | **0** | — |
| **blog.html** | **0** | — |
| **contact.html** | **0** | — |
| **despre.html** | **0** | — |
| **discografie.html** | **0** | — |

**Pagini orfane:** niciuna. Toate primesc linkuri din navigația globală, deci
sunt crawlabile.

**Pagini cu foarte puține linkuri primite:** `despre.html`, `discografie.html`
și `contact.html` nu primesc **niciun** link din corpul vreunei pagini. Există
doar în meniu. `blog.html` la fel. Pentru `contact.html` cauza e directă: după
commit-ul `dde9247`, toate CTA-urile „Cere ofertă" au fost rutate către
`wa.me`, deci pagina de contact nu mai e destinația niciunui buton.

**Adâncimea minimă de click de la homepage:** 1 pentru 9 pagini, **2** pentru
`articol.html` (index → blog → articol). Maximum 2 — structură plată, corectă.

**Ținte inexistente:** zero. Toate `href`-urile interne rezolvă la fișiere
existente, inclusiv ancorele `termeni-si-conditii.html#sectiunea-12` și
`galerie.html#clipuri` (ambele `id`-uri verificate ca prezente). Niciun
`href="#"` rămas.

**Text ancoră generic:**

| Fișier:linie | Text | Către |
|---|---|---|
| index.html:156, 162, 168 | „Detalii" ×3 | oferte.html |
| index.html:127, 382 | „Vezi ofertele" ×2 | oferte.html |
| index.html:263 | „Vezi toate videoclipurile" | galerie.html |
| index.html:363 | „Vezi toate întrebările frecvente" | faq.html |
| oferte.html | „Vezi toate întrebările frecvente" | faq.html |
| blog.html:135, 151, 167, 183 | „Citește Articolul Complet" ×4 | articol.html |

**Același text ancoră către destinații diferite:** **zero cazuri.** Verificat pe
toate cele 11 pagini.

**Invers — texte diferite către aceeași destinație:** `faq.html` e ancorat ca
„FAQ" (header) și „Întrebări frecvente" (footer). `oferte.html` primește
„Oferte", „Detalii" și „Vezi ofertele".

**CTA-uri WhatsApp — 7 formulări pentru aceeași acțiune:**

| Text | Ocurențe |
|---|---:|
| Rezervă pe WhatsApp | 28 |
| Salut! Scrie-mi pe WhatsApp (buton flotant) | 11 |
| Cere ofertă | 4 |
| Scrieți-ne pe WhatsApp | 4 |
| Scrieți-mi pe WhatsApp | 1 |
| Întrebați pe WhatsApp | 1 |
| Rezervă data ta | 1 |

Registrul oscilează între *tu* și *dumneavoastră* în aceeași funcție de buton.
CLAUDE.md §5 cere explicit vocabular consecvent și tratează „Rezervă Acum" și
„Cere ofertă" ca acțiuni **diferite** — acum ambele duc în același chat WhatsApp.

---

## 5. Imagini

Măsurători din randare reală în Chromium, DPR 1, cu scroll până la finalul
paginii pentru a declanșa `lazy`.

| Pagină:linie | Fișier | Nativ | Format | KB | alt | w/h | srcset | loading |
|---|---|---|---:|---:|---|---|---|---|
| toate (×3/pagină) | logo-alb-400w.png | 400×137 | PNG | 19 | da | da | da | eager/lazy |
| despre:112 | hora-nunta-invitati-1024 | 1024×683 | jpg+webp | 88/74 | da | da | da | — |
| despre:133 | ioana-balan-ie-broderie-aurie-1440 | 1440×1800 | jpg+webp | 209/194 | da | da | da | lazy |
| despre:146 | ioana-balan-ie-cosita-impletita-1440 | 1440×1800 | jpg+webp | 143/116 | da | da | da | lazy |
| despre:178 | ioana-balan-scena-costum-rosu-1440 | 1440×1800 | jpg+webp | 146/108 | da | da | da | lazy |
| index:133 | ioana-balan-ie-cosita-impletita-1440 | 1440×1800 | jpg+webp | 143/116 | da | da | da | eager |
| index:208 | ioana-balan-scena-costum-rosu-1440 | 1440×1800 | jpg+webp | 146/108 | da | da | da | lazy |
| index:244,253 | video-thumbs/XFdALRgk7Fg, hzOdwacBNN0 | 1280×720 | jpg | 94/96 | **gol** | da | nu | lazy |
| galerie:138,166,188,210,228 | video-thumbs ×5 | 1280×720 | jpg | 57–100 | **gol** | da | nu | lazy |
| galerie:149 | ioana-balan-hora-mireasa-1440 | 1440×954 | jpg+webp | 147/152 | da | da | da | lazy |
| galerie:156 | ioana-balan-portret-lumina-violet-1440 | 1440×1800 | jpg+webp | **245**/**235** | da | da | da | lazy |
| galerie:162 | ioana-balan-rochie-alba-imprimeu-694 | 694×705 | jpg+webp | 92/54 | da | da | da | lazy |
| galerie:177 | hora-nunta-invitati-1024 | 1024×683 | jpg+webp | 88/74 | da | da | da | lazy |
| galerie:183 | ioana-balan-sala-eveniment-480 | 480×640 | jpg+webp | 45/37 | da | da | da | lazy |
| galerie:199 | formatie-ring-dans-480 | 480×478 | jpg+webp | 41/34 | da | da | da | lazy |
| galerie:205 | formatie-sacouri-albe-480 | 480×640 | jpg+webp | 43/35 | da | da | da | lazy |
| galerie:224 | formatie-lumini-scena-480 | 480×320 | jpg+webp | 30/24 | da | da | da | lazy |
| oferte:274 | formatie-instrumentala-tambal-1304 | 1304×978 | jpg+webp | 167/161 | da | da | da | lazy |
| **articol:119** | **ioana-balan-and-band.jpg** | **512×341** | jpg | 55 | slab | **NU** | **nu** | **NU** |
| **blog:126** | **blog-cover.jpg** | **512×288** | jpg | 51 | **slab** | **NU** | **nu** | **NU** |
| **blog:142** | **blog-cover-2.jpg** | **512×341** | jpg | 69 | **slab** | **NU** | **nu** | **NU** |
| **blog:158** | **blog-cover-3.jpg** | **512×341** | jpg | 75 | **slab** | **NU** | **nu** | **NU** |
| **blog:174** | **blog-cover-4.jpg** | **512×341** | jpg | 55 | **slab** | **NU** | **nu** | **NU** |
| **contact:109** | **…portrait-artist-muzica-populara-s.jpg** | **410×512** | jpg | 54 | **stuffing** | **NU** | **nu** | **NU** |
| **discografie:118** | **…portrait-artist-muzica-populara-s.jpg** | **410×512** | jpg | 54 | **greșit** | **NU** | **nu** | **NU** |
| **oferte:110** | **ioana-balan-live-show.jpg** | **512×341** | jpg | 69 | ok | **NU** | **nu** | **NU** |
| **galerie:252** | **…portret-sesiune-foto-cal.jpg** | **512×511** | jpg | 52 | **slab** | **NU** | **nu** | lazy |

### Alt lipsă sau gol pe imagini de conținut

Niciun `alt` absent. Cele 7 miniaturi video au `alt=""`, dar **corect**:
fiecare stă într-un `<button>` cu `aria-label="Redă videoclipul: …"` și un
titlu vizibil în `.video-card__title` (`galerie.html:138-147`). Imaginea e
decorativă în raport cu numele accesibil al butonului. Verificat, nu e o
constatare.

### Alt problematic

| Fișier:linie | alt curent | Ce e greșit |
|---|---|---|
| blog:126,142,158,174 | „Blog cover" ×4 | identic pe 4 imagini distincte, în engleză, nu descrie nimic |
| articol:119 | „Ioana Balan and Band" | engleză, generic |
| discografie:118 | „Copertă Album Ioana Balan - Hai să nu ne mai mințim - Muzică de petrecere 2025" | fișierul e un **portret**, nu o copertă de album — alt-ul descrie altceva decât imaginea |
| contact:109 | „Ioana Balan - Portrait Artist Muzică Populară și Evenimente Private" | keyword stuffing, construcție de nume de fișier, „Portrait" în engleză |
| galerie:252 | „Ioana Balan - Portret Sesiune Foto Cal" | nume de fișier transcris, nu descriere |

Restul alt-urilor (fototeca clientei) sunt exemplare: descriptive, în română,
specifice — „Ioana Balan cântând la microfon, în ie cu broderie roșie și fustă
roșie cu bată tradițională".

### Fișiere peste 200 KB

| Fișier | KB |
|---|---:|
| `assets/img/discografie-album-radacini.png` | **344** — PNG pentru o fotografie; **nereferențiat de nicio pagină** |
| `assets/img/ioana-balan-portret-lumina-violet-1440.jpg` | **245** |
| `assets/img/ioana-balan-portret-lumina-violet-1440.webp` | **235** |
| `assets/img/ioana-balan-ie-broderie-aurie-1440.jpg` | **209** |

### Imagini servite peste rezoluția nativă (măsurat, DPR 1)

| Fișier:linie | Imagine | Nativ | @375 | @768 | @1280 |
|---|---|---|---|---|---|
| contact:109 | …portrait-artist-…-s.jpg | 410×512 | ascuns | ascuns | **2,56×** |
| oferte:110 | ioana-balan-live-show.jpg | 512×341 | **1,30×** | **1,50×** | **2,50×** |
| discografie:118 | …portrait-artist-…-s.jpg | 410×512 | 0,83× | **1,75×** | 1,05× |
| articol:119 | ioana-balan-and-band.jpg | 512×341 | **1,47×** | **1,47×** | **1,47×** |
| despre:112 | hora-nunta-invitati-1024 | 1024×683 | 1,06× | 1,00× | **1,25×** |

Toate celelalte imagini rămân sub 1,0× la toate trei lățimile — `srcset` +
`sizes` sunt calculate corect acolo unde există. Cele patru cazuri grave sunt
exact placeholderele Stitch de 512 px, servite fără `srcset`. Cazul
`despre:112` e deja documentat ca provizoriu în markup (`despre.html:105-109`)
și în CLAUDE.md.

---

## 6. Viteză și resurse

### Cereri externe

**Un singur domeniu extern pe întregul site: `cdn.tailwindcss.com`**, 2 cereri
pe fiecare pagină (o redirecționare 302 către `/3.4.17?plugins=forms@0.5.10,container-queries@0.1.1`,
apoi fișierul).

| Măsurat | Valoare |
|---|---:|
| Tailwind Play CDN, decomprimat | **409 KB** |
| pe fir, brotli | **127 KB** |
| pe fir, gzip | 124 KB |
| round-trips | **2** (302 + 200) |

Fonturile sunt **self-hosted** în `assets/fonts/` — zero cereri către Google
Fonts. `og:image`, logo și toate imaginile sunt locale. Nu există analytics,
pixeli sau widget-uri terțe. Din perspectiva GDPR și a politicii de cookie-uri
declarate, asta e corect și rar.

### Greutate totală (resurse locale, fără CDN-ul Tailwind)

| Pagină | @375 | @1280 | document | fonturi | imagini | css | js |
|---|---:|---:|---:|---:|---:|---:|---:|
| galerie.html | **1233 KB** | **1154 KB** | 37 | 204–283 | 885 | 24 | 4 |
| discografie.html | **866 KB** | 787 KB | 35 | 265–344 | 459 | 24 | 4 |
| index.html | 681 KB | 681 KB | 56 | 283 | 314 | 24 | 4 |
| despre.html | 610 KB | 632 KB | 30 | 283 | 269–292 | 24 | 4 |
| blog.html | 609 KB | 609 KB | 29 | 283 | 268 | 24 | 4 |
| oferte.html | 533 KB | 553 KB | 49 | 227–283 | 174–249 | 24 | 4 |
| termeni-si-conditii.html | 436 KB | 357 KB | 44 | 265–344 | 20 | 24 | 4 |
| articol.html | 431 KB | 431 KB | 27 | 302 | 74 | 24 | 4 |
| faq.html | 374 KB | 295 KB | 44 | 204–283 | 20 | 24 | 4 |
| politica-cookie.html | 365 KB | 286 KB | 35 | 204–283 | 20 | 24 | 4 |
| contact.html | 341 KB | 341 KB | 36 | 204 | 74 | 24 | 4 |

Adăugați **+127 KB pe fir** pentru Tailwind la fiecare pagină. Vârful e
`galerie.html` la ~1,36 MB.

### Resurse blocante de randare

`index.html:51-52` (identic pe toate paginile):

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script src="assets/tailwind.config.js"></script>
```

Ambele în `<head>`, **fără `defer` sau `async`**. Blochează parserul. În plus,
Play CDN-ul nu livrează CSS gata compilat: scanează DOM-ul și **generează CSS-ul
în browser, la runtime**, ceea ce adaugă lucru pe firul principal peste cei 409
KB de JavaScript parsat. `assets/styles.css` (24 KB) conține doar componentele
custom, nu utilitarele Tailwind.

### Fonturi

12 fișiere `.woff2` în `assets/fonts/`, subsetate corect pe `latin` și
`latin-ext` (EB Garamond 400/500/500-italic, Inter 400/400-italic/600).
Servite local, cu preload doar pe fața cerută de H1-ul de deasupra pliului:

```html
<link rel="preload" href="assets/fonts/eb-garamond-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/eb-garamond-400-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
```

Corect, cu o rezervă: la randare se descarcă **6–10 fișiere** (204–344 KB), nu
2. Pe `discografie.html` și `termeni-si-conditii.html` se ating 344 KB — mai
mult decât toate imaginile din `contact.html`.

`index.html:30` preîncarcă și imaginea LCP, cu `imagesrcset`/`imagesizes`
identice cu `<picture>`. Făcut corect.

---

## 7. Conținut

Numărătoare pe conținutul din `<main>`, cu `<header>`, `<footer>` și `<nav>`
eliminate din DOM.

| Pagină | Cuvinte |
|---|---:|
| termeni-si-conditii.html | 1524 |
| politica-cookie.html | 831 |
| oferte.html | 805 |
| faq.html | 561 |
| index.html | 519 |
| despre.html | 337 |
| articol.html | 310 |
| **blog.html** | **194** |
| **discografie.html** | **146** |
| **contact.html** | **126** |
| **galerie.html** | **118** |

**Sub 300 de cuvinte:** `blog.html`, `discografie.html`, `contact.html`,
`galerie.html`. Pentru galerie și contact e parțial firesc — sunt pagini de
imagine și de acțiune. Pentru `discografie.html` nu: pagina are trei albume,
un H1 și 146 de cuvinte, deci aproape nimic de indexat pentru interogări de
tip „Ioana Balan Rădăcini album" sau „melodii Ioana Balan".

### Suprapunere de conținut

Shingles de 6 cuvinte consecutive, pe textul principal.

| Pereche | Jaccard | din A | din B |
|---|---:|---:|---:|
| faq.html ↔ oferte.html | 13,3% | **27,5%** din faq | 20,6% din oferte |
| faq.html ↔ index.html | 10,9% | **19,1%** din faq | **20,3%** din index |
| index.html ↔ oferte.html | 5,4% | 12,5% din index | 8,7% din oferte |

Sursa e identificabilă exact: același bloc de întrebări frecvente, copiat
verbatim în trei locuri.

- `index.html:324-368` — 3 întrebări (preț, deplasare, rezervare)
- `oferte.html:297-355` — 5 întrebări (preț, rezervare, avans, termen, amânare)
- `faq.html:130-341` — toate 17, sursa originală

Textul întrebărilor **și** al răspunsurilor e identic caracter cu caracter.
Rezultatul: un sfert din pagina FAQ e conținut care există deja pe pagina de
oferte, iar o cincime din homepage e conținut care există deja pe FAQ. Cele trei
pagini concurează între ele pentru aceleași interogări („cât costă o formație de
nuntă", „cum rezerv data").

---

## 8. Tehnic

### robots.txt

**Absent.** Nu există în rădăcina repo-ului și nu e urmărit de git.

### sitemap.xml

**Absent.** Nu există în rădăcina repo-ului și nu e urmărit de git. Nu există
nici o referință `Sitemap:` (nu are unde, în lipsa `robots.txt`).

Alte fișiere de infrastructură absente: `404.html`, `CNAME`, `.nojekyll`.

### Schema de denumire a URL-urilor

| URL | Limbă | Observație |
|---|---|---|
| `/` | — | canonical fără `index.html` ✓ |
| `/despre.html` | ro | ✓ |
| `/galerie.html` | ro | ✓ |
| `/discografie.html` | ro | ✓ |
| `/oferte.html` | ro | ✓ |
| `/contact.html` | ro | ✓ |
| `/blog.html` | ro | ✓ |
| `/articol.html` | ro | **slug generic** — un singur articol-șablon pentru 4 carduri |
| `/faq.html` | **en** | singura abreviere engleză între slug-uri românești |
| `/politica-cookie.html` | ro | ✓ (singular „cookie", plural în H1 „cookie-uri") |
| `/termeni-si-conditii.html` | ro | ✓ diacritice transliterate corect |

Coerent: minuscule, cratime, fără underscore, fără parametri, fără majuscule,
fără diacritice în path. Două excepții: `faq` și `articol`.

### URL-uri care nu supraviețuiesc migrării fără redirect

**Toate cele 11.** WordPress nu servește `.html`; permalink-urile devin
`/despre/`, `/galerie/`, `/oferte/` etc. Trei consecințe concrete:

1. **33 de `href="index.html"`** în tot repo-ul trebuie rescrise la `/`.
   `index.html` nu va exista în WordPress.
2. **Cele 11 `<link rel="canonical">` și 11 `og:url` conțin `.html`.** Dacă
   sunt copiate ca atare în Elementor / Yoast, fiecare pagină își va declara un
   canonical către un URL care returnează 404.
3. `articol.html` devine `/blog/<slug-real>/`. Cele 4 carduri din `blog.html`
   trebuie să indice către 4 slug-uri distincte.

Prototipul în sine nu are nevoie de redirecturi — nu e indexat (canonical către
alt domeniu, găzduire temporară). Redirecturile din Faza 5 se scriu de la
**URL-urile site-ului vechi**, nu de la acestea.

---

## Constatări, sortate pe severitate

### CRITIC

---

**C1 — Două entități concurente sub același `@id`**
`index.html:31` și `contact.html:31`

`index.html` declară `{"@type": "MusicGroup", "@id": "https://ioana-balan.ro/#artist"}`.
`contact.html` declară `{"@type": "EntertainmentBusiness", "@id": "https://ioana-balan.ro/#artist"}`
— același identificator, alt tip, cu `description` și `image` diferite pentru
același nod.

*Impact:* `#artist` e nodul central al grafului — `despre.html` îl referențiază
prin `mainEntity`, `faq.html` prin `about`. Google primește două definiții
divergente ale entității principale și trebuie să aleagă una. Semnalele pentru
Knowledge Panel și pentru pachetul local se fragmentează exact pe entitatea care
ar trebui să fie cea mai stabilă.

*Ce ar trebui:* o singură definiție canonică a entității, într-un `@graph` unic
inclus pe toate paginile, cu tipuri multiple pe același nod dacă e nevoie
(`"@type": ["MusicGroup", "EntertainmentBusiness"]`) și **un singur** set de
`name`/`description`/`image`. Paginile individuale referențiază `{"@id": "…#artist"}`,
nu redeclară.

---

**C2 — Patru articole distincte, o singură destinație**
`blog.html:132,148,164,180` (titluri) și `blog.html:135,151,167,183` (linkuri)

Patru carduri cu H2, imagine de copertă și categorie proprii — „Cum să alegi
formația de nuntă perfectă în 2026", „Muzica populară vs. Muzica ușoară la
botez", „Repertoriul de muzica populara nunta", „Cum transformi un eveniment
privat într-un spectacol premium" — toate patru cu `href="articol.html"` și
ancora „Citește Articolul Complet". Articolul livrat are un al cincilea subiect:
„Importanța luminilor de scenă". `BlogPosting.headline` din `articol.html:30` nu
corespunde niciunuia dintre cele patru titluri.

*Impact:* patru promisiuni de conținut, un singur URL. Google vede o pagină cu
patru titluri contradictorii care duc la ea și un `headline` care le contrazice
pe toate. Cele patru interogări pe care le vizează cardurile nu au unde ateriza.

*Ce ar trebui:* patru URL-uri, fiecare cu `BlogPosting` propriu al cărui
`headline` coincide cu H1-ul paginii și cu titlul cardului. În prototip:
minimum, ancore distincte și un card marcat vizibil ca șablon.

---

### MAJOR

---

**M1 — `robots.txt` și `sitemap.xml` absente**
rădăcina repo-ului

Niciunul dintre cele două fișiere nu există.

*Impact:* la lansare, descoperirea paginilor depinde exclusiv de linkuri.
Nu există niciun mecanism de a semnala prioritatea sau prospețimea paginilor,
nici de a bloca resursele care nu trebuie crawlate. Pentru un site de 9 pagini
efectul e limitat, dar sitemap-ul e și canalul prin care Search Console
raportează starea de indexare — fără el, diagnosticul post-lansare e orb.

*Ce ar trebui:* `robots.txt` cu linia `Sitemap:` către URL-ul absolut, și un
`sitemap.xml` cu cele 9 pagini indexabile (fără cele două `noindex`).

---

**M2 — `Offer` fără `price`, `Product` fără `image`**
`oferte.html:35-48`

Cele patru `Offer` declară `priceCurrency: "EUR"` și `availability`, dar niciun
`price` sau `priceSpecification`. `Product` nu are `image`.

*Impact:* blocul e valid ca JSON, dar nu produce niciun rezultat îmbogățit —
`price` e obligatoriu pentru `Offer`, `image` pentru `Product`. Testul Google
pentru rezultate îmbogățite îl raportează ca eroare.

*Ce ar trebui:* completat la finalizarea grilei de prețuri. Consecință directă a
excluderii declarate mai sus — de rezolvat odată cu prețurile, nu înainte.

---

**M3 — 5,0★ / 61 de recenzii nu există nicăieri pe site**
`index.html:273-320`

Trei testimoniale, fiecare cu cinci stele desenate în SVG marcat
`aria-hidden="true"`. Textul „5,0", „61" și „recenzii" nu apare în niciunul
dintre cele 11 fișiere. Niciun `aggregateRating`, niciun `Review` în JSON-LD.

*Impact:* nici un crawler, nici un cititor de ecran nu percepe vreo evaluare.
CLAUDE.md §4 identifică asta drept activul cel mai subutilizat, iar §9 decide
afișarea a 6–8 recenzii „cu cifra 5,0★/61 proeminentă". Implementarea curentă
are 3 recenzii și zero cifre. Pentru poziționarea de preț din §4 — pachete în
vârful pieței — justificarea trebuie să apară pe același ecran cu prețul.

*Ce ar trebui:* cifra ca text vizibil („5,0★ · 61 de recenzii pe Google"), cu
link către profilul Google, plus stelele cu nume accesibil în loc de
`aria-hidden`. Atenție la markup: Google nu acordă rezultate îmbogățite pentru
`aggregateRating` auto-declarat pe `LocalBusiness`/`Organization`, iar
recenziile nu se copiază de pe platforme terțe. `Review` pe `Product` (pachete)
e calea conformă.

---

**M4 — Blocul FAQ copiat verbatim pe trei pagini**
`faq.html:130-341`, `oferte.html:297-355`, `index.html:324-368`

27,5% din textul paginii FAQ apare identic pe `oferte.html`; 20,3% din homepage
apare identic pe FAQ.

*Impact:* trei pagini din nouă concurează pentru aceleași interogări comerciale
(„cât costă formație nuntă", „cum rezerv data"). Google alege una și
deprioritizează celelalte două — fără control asupra alegerii.

*Ce ar trebui:* fiecare întrebare are un singur răspuns complet, pe `faq.html`.
Pe index și oferte, întrebarea plus 1–2 propoziții reformulate și link către
răspunsul integral, nu textul copiat.

---

**M5 — Patru pagini sub 300 de cuvinte**
`galerie.html` (118), `contact.html` (126), `discografie.html` (146),
`blog.html` (194)

*Impact:* `discografie.html` e cazul serios: trei albume, un an de lansare
fiecare, niciun context. Nu există text pentru „Ioana Balan Rădăcini", „album
Glasul Inimii" sau nume de melodii. Pentru galerie și contact, deficitul e mai
puțin grav — sunt pagini de imagine și de acțiune.

*Ce ar trebui:* pe discografie, un paragraf pe album (context, ce conține, unde
se ascultă) și lista pieselor. Pe galerie, legende reale sub grupurile de
imagini — CLAUDE.md §7: „textul e material de design, nu umplutură".

---

**M6 — Șase placeholdere Stitch de 512 px, servite până la 2,56×**
`articol.html:119`, `blog.html:126,142,158,174`, `contact.html:109`,
`discografie.html:118`, `oferte.html:110`, `galerie.html:252`

Niciuna dintre aceste nouă etichete `<img>` nu are `width`, `height`, `srcset`
sau `loading`. Măsurat: `contact.html:109` 2,56× la 1280 px; `oferte.html:110`
2,50× la 1280 px și 1,50× la 768 px; `discografie.html:118` 1,75× la 768 px;
`articol.html:119` 1,47× la toate lățimile.

*Impact:* imagini vizibil neclare pe fiecare ecran peste 768 px, exact pe
paginile de conversie (oferte, contact). Absența `width`/`height` produce
Cumulative Layout Shift. Absența `loading="lazy"` pe cele patru coperte de blog
înseamnă 250 KB descărcați înainte de primul paint.

*Ce ar trebui:* înlocuite cu material real la minimum 1440 px, cu `<picture>` +
`srcset` + `sizes` + `width`/`height`, exact ca imaginile din fototeca clientei
— care sunt implementate corect.

---

**M7 — H1 care nu descrie pagina**
`discografie.html:125`

H1 = „Hai să nu ne mai mințim" (numele albumului). `<title>` = „Discografie |
IOANA BALAN". `<h1>` și `<title>` descriu subiecte diferite.

*Impact:* semnalul on-page cel mai puternic al paginii indică un album, nu
discografia. Interogările de tip „discografie Ioana Balan" nu găsesc corespondent
în H1.

*Ce ar trebui:* H1 care numește pagina („Discografie" sau „Albumele Ioanei
Balan"), cu titlul albumului ca H2 în secțiunea de lansare nouă.

---

**M8 — Opt din unsprezece meta descrieri peste 160 de caractere**
`termeni-si-conditii.html` (191), `politica-cookie.html` (181), `faq.html`
(177), `contact.html` (174), `galerie.html` (173), `index.html` (171),
`blog.html` (162), `oferte.html` (162)

*Impact:* Google trunchiază. `contact.html` pierde exact partea utilă —
descrierea se termină cu „Consultanță muzicală gratuită", care cade sub prag.
Pe `galerie.html`, lista de cinci orașe (semnalul SEO local) e la coadă și
dispare.

*Ce ar trebui:* 120–155 de caractere, cu informația decisivă în primele 100.

---

**M9 — `BreadcrumbList` doar pe o pagină din nouă**
`blog.html:28` (singura care îl are)

*Impact:* fără breadcrumb, rezultatele afișează URL-ul brut în loc de calea
ierarhică. Pe mobil — canalul dominant conform CLAUDE.md §3 — asta costă
lățimea utilă a snippet-ului.

*Ce ar trebui:* `BreadcrumbList` pe toate paginile de nivel 1 și pe articol,
în același `@graph` cu entitatea principală.

---

**M10 — Șapte videoclipuri, zero `VideoObject`**
`index.html:244,253`, `galerie.html:138,166,188,210,228`

Videoclipurile sunt montate ca facade (`<button data-yt="…">` cu miniatură,
iframe injectat la click). Bun pentru performanță — zero cereri YouTube la
încărcare. Dar niciunul nu are markup.

*Impact:* zero eligibilitate pentru rezultate video, deși există miniaturi,
titluri (`.video-card__title`) și ID-uri YouTube — tot ce trebuie pentru
`VideoObject`. CLAUDE.md §4: video în hero e diferențiatorul pe care doar 1 din
8 concurenți îl are.

*Ce ar trebui:* `VideoObject` per clip, cu `name`, `description`,
`thumbnailUrl`, `uploadDate`, `embedUrl` și `contentUrl`.

---

**M11 — Tailwind Play CDN blocant, 409 KB, compilat în browser**
`index.html:51-52` și echivalentul pe toate cele 11 pagini

Două `<script>` fără `defer`/`async` în `<head>`. Play CDN-ul: 302 → 200 (două
round-trips), 409 KB decomprimat / 127 KB pe fir, apoi scanează DOM-ul și
generează CSS-ul la runtime.

*Impact:* Largest Contentful Paint amânat cu întreaga durată de descărcare,
parsare, execuție și compilare. Pe conexiune mobilă, asta domină bugetul de
performanță al fiecărei pagini. Publicul e majoritar mobil (CLAUDE.md §3).

*Ce ar trebui:* în prototip, acceptabil — e explicit un compromis de viteză de
iterație (CLAUDE.md §8: fără build tools). Dar înseamnă că **măsurătorile Core
Web Vitals de pe prototip nu prezic performanța WordPress-ului** și nu trebuie
folosite ca referință la validarea cu clientul.

---

**M12 — Trei pagini fără niciun link redacțional**
`despre.html`, `discografie.html`, `contact.html` (plus `blog.html`)

Niciuna nu primește vreun link din corpul altei pagini. Există exclusiv în
meniu. Pentru `contact.html` cauza e directă: după `dde9247`, toate butoanele
„Cere ofertă" trimit la `wa.me`.

*Impact:* linkurile din navigația globală transmit foarte puțin semnal —
sunt identice pe toate paginile. `despre.html` conține povestea artistei și trei
portrete, `discografie.html` conține catalogul; ambele sunt izolate de fluxul
editorial. `contact.html` a devenit o pagină pe care nimic nu o recomandă.

*Ce ar trebui:* linkuri contextuale — din `oferte.html` către `despre.html`
(cine cântă), din `index.html` către `discografie.html` (ce cântă), din
`galerie.html` către `contact.html`. Și cel puțin un CTA pe pagină care duce la
formular, nu la WhatsApp — WhatsApp e canalul preferat, dar nu poate fi singurul
punct de conversie indexabil.

---

**M13 — Alt text greșit, generic sau supraîncărcat pe nouă imagini**
`blog.html:126,142,158,174`; `articol.html:119`; `contact.html:109`;
`discografie.html:118`; `galerie.html:252`

| Locație | alt curent | Problemă |
|---|---|---|
| blog ×4 | „Blog cover" | identic pe 4 imagini diferite, în engleză |
| articol:119 | „Ioana Balan and Band" | engleză, nedescriptiv |
| contact:109 | „Ioana Balan - Portrait Artist Muzică Populară și Evenimente Private" | keyword stuffing |
| discografie:118 | „Copertă Album … Hai să nu ne mai mințim …" | fișierul e un portret, nu o copertă |
| galerie:252 | „Ioana Balan - Portret Sesiune Foto Cal" | nume de fișier transcris |

*Impact:* `discografie.html:118` e cel mai grav — alt-ul afirmă ceva fals despre
imagine, ceea ce e și o problemă de accesibilitate, nu doar de SEO. Restul pierd
Google Images pe interogări unde site-ul are material real.

*Ce ar trebui:* descrieri în română, specifice, ca cele din fototeca clientei
(care sunt corecte).

---

### MINOR

---

**m1 — Salt de nivel H1 → H3, titlu folosit pentru stilizare**
`articol.html:122`

Un citat decorativ marcat `<h3>` pentru dimensiunea fontului, plasat între H1 și
primul H2. Nu deschide nicio secțiune.

*Ce ar trebui:* `<blockquote>` sau `<p>` cu aceleași clase.

---

**m2 — „Tag-uri SEO" vizibil publicului**
`blog.html:203`

Titlu de secțiune în sidebar. Jargon intern afișat cititorilor.

*Ce ar trebui:* „Subiecte" sau „Etichete". Sau eliminat — cele cinci etichete de
dedesubt nu sunt clicabile, deci nu fac nimic.

---

**m3 — H1 construit ca șir de cuvinte-cheie**
`index.html:121`

„Formație Nuntă București Premium: Muzică de Petrecere Autentică" — aproape
identic cu `<title>`, cu majuscule pe fiecare cuvânt și două expresii de căutare
lipite cu două puncte.

*Impact:* funcționează pentru potrivire exactă, dar contrazice §7 din CLAUDE.md
(„ton cald și direct, fără superlative goale") și e primul lucru pe care îl
citește un mire. Restul site-ului e scris uman; acest H1 nu.

---

**m4 — Lungimi de title în afara intervalului**
Peste 60: `blog.html` (71), `articol.html` (68), `index.html` (68),
`contact.html` (65). Sub 30: `despre.html` (25).

`despre.html` — „Despre mine | Ioana Balan" — nu conține niciun cuvânt care să
diferențieze pagina în rezultate.

---

**m5 — Șapte formulări pentru același CTA WhatsApp**
`articol:67,97,156,302`; `oferte:171,211,238,265`; `despre:190`; `faq:346`;
`index:313,382`; `galerie:247`; `discografie:269` și altele

„Rezervă pe WhatsApp" (28×), „Salut! Scrie-mi pe WhatsApp" (11×), „Cere ofertă"
(4×), „Scrieți-ne pe WhatsApp" (4×), „Scrieți-mi pe WhatsApp", „Întrebați pe
WhatsApp", „Rezervă data ta". Registrul alternează *tu* / *dumneavoastră*.

*Impact:* CLAUDE.md §5 cere vocabular consecvent și tratează „Rezervă Acum" și
„Cere ofertă" ca acțiuni distincte. După `dde9247`, ambele duc în același chat.
Utilizatorul care apasă „Cere ofertă" așteaptă un formular și primește WhatsApp.

---

**m6 — Ancore generice**
`index.html:156,162,168` — „Detalii" ×3 către `oferte.html`;
`index.html:127,382` — „Vezi ofertele" ×2;
`blog.html:135,151,167,183` — „Citește Articolul Complet" ×4

*Ce ar trebui:* „Vezi pachetele pentru nuntă", „Vezi pachetele pentru botez" —
anchor text care descrie destinația.

---

**m7 — H3 duplicate în aceeași pagină**
`oferte.html:147,177,217,244`

„Pachet Standard" și „Pachet Premium" apar de două ori, fără ca titlul să
conțină tipul evenimentului.

*Ce ar trebui:* „Pachet Standard — Nuntă" / „Pachet Standard — Botez".

---

**m8 — Aceeași destinație, două ancore**
`faq.html` ancorat „FAQ" în header și „Întrebări frecvente" în footer.

---

**m9 — `MusicAlbum` nelegate de entitatea principală**
`discografie.html:29`

Cele trei albume au doar `name`, `datePublished` și un `byArtist` anonim de tip
`MusicGroup` — trei noduri separate, niciunul legat de `#artist`. Lipsesc `@id`,
`url`, `image`, `numTracks`, `track`.

---

**m10 — `twitter:title` și `twitter:description` absente pe paginile juridice**
`politica-cookie.html`, `termeni-si-conditii.html`

`twitter:card` și `twitter:image` sunt prezente, deci cardul se randează gol.
Impact real: aproape nul (pagini `noindex`), dar e o inconsecvență în șablon.

---

**m11 — Aceeași `og:image` pe toate cele 11 pagini**
`assets/og-ioana-balan.png` — semnătura pe fundal negru.

*Impact:* orice link partajat arată identic. Pentru `oferte.html` și
`galerie.html`, o imagine specifică ar converti mai bine.

---

**m12 — `BlogPosting` cu date vechi și publisher incomplet**
`articol.html:30`

`datePublished` și `dateModified` = `2024-08-15`, la peste doi ani în urmă.
`publisher` e un `Organization` fără `logo`. `author` e un `Person` fără `url`
sau `@id` către `#artist`.

---

**m13 — `ImageGallery` cu entitate inline în loc de referință**
`galerie.html:27`

`about` conține `{"@type": "MusicGroup", "name": "Ioana Balan"}` — un al treilea
nod anonim pentru aceeași artistă, în loc de `{"@id": "…#artist"}`.

---

**m14 — 6–10 fișiere de font pe pagină, 204–344 KB**
`assets/fonts/` — 12 fișiere

`discografie.html` și `termeni-si-conditii.html` ating 344 KB de fonturi la 375
px — mai mult decât toate imaginile de pe `contact.html`.

*Ce ar trebui:* verificat dacă `EB Garamond 500 italic` (76 KB, două fișiere) e
folosit efectiv; subsetare mai agresivă pe latin-ext.

---

**m15 — Banda hero de pe `despre.html` la 1,25× pe desktop**
`despre.html:112`

Măsurat 1,25× la 1280 px. Deja documentat ca provizoriu în comentariul din
`despre.html:105-109` și în CLAUDE.md — lipsește o fotografie peisaj de minimum
1440 px cu subiectul în treimea centrală. Repetat aici doar pentru completitudinea
măsurătorilor.

---

**m16 — `faq.html` — singurul slug în engleză**
Între zece slug-uri românești. `intrebari-frecvente` ar fi coerent și ar conține
expresia de căutare.

---

**m17 — Fișier de 344 KB nereferențiat**
`assets/img/discografie-album-radacini.png` — PNG de 344 KB pentru o fotografie
(ar trebui JPEG/WebP), care nu apare în nicio pagină. Cel mai mare fișier din
repo, mort.

---

## Ce e implementat corect

Merită consemnat, fiindcă schimbă unde se investește efortul:

- **Un singur H1 pe fiecare pagină**, un singur salt de nivel în tot site-ul.
- **Zero titluri sau descrieri duplicate** între pagini.
- **Canonical pe 11/11**, Open Graph complet cu `og:image:width/height/alt`.
- **Zero linkuri interne rupte**, zero `href="#"` rămase, ancorele de fragment
  verificate.
- **Zero cazuri de același text ancoră către destinații diferite.**
- **Toate linkurile externe au `target="_blank"` + `rel="noopener"`.** 0 excepții.
- **Fonturi self-hosted**, subsetate latin/latin-ext, cu preload țintit pe fața
  LCP; zero cereri către Google Fonts.
- **Preload al imaginii LCP** cu `imagesrcset`/`imagesizes` identice cu `<picture>`.
- **`srcset` + `sizes` corect calculate** pe toate imaginile din fototeca
  clientei — măsurat sub 1,0× la 375, 768 și 1280 px.
- **Alt text exemplar** pe aceleași imagini: descriptiv, în română, specific.
- **Miniaturi video cu `alt=""` corect**, fiindcă butonul-părinte poartă
  `aria-label` și titlul vizibil.
- **Facade video** în loc de iframe-uri YouTube: zero cereri terțe la încărcare.
- **`FAQPage` conține doar răspunsurile validate**, cu decizia documentată în
  cod — exact tratamentul corect pentru structured data.
- **Un singur domeniu extern** pe tot site-ul.

---

## Ce se rezolvă în prototip

Ordonat după raport impact / efort.

| # | Ce | Unde |
|---|---|---|
| 1 | Unificat `@id` `#artist` într-o singură definiție; `contact.html` referențiază, nu redeclară | C1 |
| 2 | Ancore distincte pe cele 4 carduri de blog; card marcat ca șablon | C2 |
| 3 | Rescris cele 8 meta descrieri peste 160 și cele 4 titluri peste 60 | M8, m4 |
| 4 | Deduplicat blocul FAQ: răspuns integral doar pe `faq.html`, rezumat + link pe index și oferte | M4 |
| 5 | Corectat cele 9 alt-uri greșite sau generice | M13 |
| 6 | Adăugat `width`/`height` + `loading="lazy"` pe cele 9 `<img>` fără ele (rezolvă CLS chiar cu placeholderele actuale) | M6 |
| 7 | H1 pe `discografie.html` schimbat pe subiectul paginii | M7 |
| 8 | `BreadcrumbList` pe toate paginile | M9 |
| 9 | `VideoObject` pe cele 7 clipuri — ID-urile, titlurile și miniaturile există deja | M10 |
| 10 | Cifra „5,0★ · 61 de recenzii" ca text vizibil, cu link către profilul Google; stele cu nume accesibil | M3 |
| 11 | Linkuri redacționale către `despre`, `discografie`, `contact` | M12 |
| 12 | Unificat vocabularul CTA; separat „Cere ofertă" (formular) de „Rezervă" (WhatsApp) | m5 |
| 13 | `blockquote` în loc de H3 în `articol.html:122`; „Tag-uri SEO" redenumit | m1, m2 |
| 14 | H3 din `oferte.html` diferențiate pe tip de eveniment | m7 |
| 15 | `MusicAlbum`, `ImageGallery`, `BlogPosting` legate de `#artist`; date `BlogPosting` actualizate | m9, m12, m13 |
| 16 | `twitter:title`/`:description` pe paginile juridice | m10 |
| 17 | Șters `discografie-album-radacini.png` (344 KB, nereferențiat) | m17 |

**`robots.txt` și `sitemap.xml` (M1):** se pot scrie și în prototip, dar cu
URL-uri `ioana-balan.ro`, deci nefuncționale până la lansare, și vor fi
suprascrise de pluginul SEO. Recomandarea e să rămână pe Faza 3 — cu condiția să
existe un element de checklist care să împiedice uitarea lor.

---

## Ce se rezolvă abia în WordPress, la Faza 3

| # | Ce | De ce nu acum |
|---|---|---|
| 1 | **`robots.txt` + `sitemap.xml`** | Yoast/RankMath le generează dinamic, cu `lastmod` real per pagină. Orice fișier scris manual acum ar fi înlocuit. Prototipul nu e indexat, deci absența lor nu costă nimic azi. |
| 2 | **Prețurile în `Offer`** (M2) | Blocate de decizia comercială a clientei, nu de implementare. CLAUDE.md §9 le listează ca deschise. Se completează odată cu grila reală. |
| 3 | **Înlocuirea celor 6 placeholdere Stitch** (M6) | CLAUDE.md §8 interzice explicit înlocuirea imaginilor — clienta furnizează originalele. Structura `<picture>`/`srcset` se poate pregăti acum; fișierele vin la Faza 3. |
| 4 | **Fotografia peisaj ≥1440 px pentru hero-ul `despre`** (m15) | Nu există în fototeca de 14 fișiere. Depinde de material nou de la clientă. |
| 5 | **Confirmarea identității în grupele B și C** | CLAUDE.md §10 blochează 7 fotografii până la confirmarea clientei. Nu se rezolvă tehnic. |
| 6 | **Eliminarea Tailwind Play CDN** (M11) | CLAUDE.md §8 interzice build tools în prototip. În WordPress problema dispare de la sine: Elementor livrează CSS compilat. **Consecință de reținut pentru Faza 2:** măsurătorile de performanță pe prototip nu prezic WordPress-ul și nu trebuie prezentate clientului ca atare. |
| 7 | **Rescrierea celor 33 de `href="index.html"`** și eliminarea `.html` din toate canonical/`og:url` | Depinde de structura reală de permalink-uri. Se face în migrare, nu înainte. |
| 8 | **Patru URL-uri reale de articol** în loc de `articol.html` | Are nevoie de patru texte scrise. Prototipul demonstrează șablonul; conținutul e Faza 3+. |
| 9 | **`faq.html` → `intrebari-frecvente`** | Redenumirea acum ar rupe linkurile din prototip fără câștig; slug-ul corect se stabilește direct în WordPress. |
| 10 | **Formularul de contact funcțional** și tabelul de destinatari din T&C 12.3 | CLAUDE.md §8 stabilește deja regulile. Alegerea pluginului e și decizie juridică — determină conținutul secțiunii 12.3. |
| 11 | **`aggregateRating` / `Review` conform politicii Google** (M3) | Cifra vizibilă se poate adăuga acum; markup-ul conform are nevoie de decizia despre unde stau recenziile (import cu acord, `Review` pe `Product`, sau doar link). Decizie de Faza 3. |
| 12 | **Logo vectorizat (SVG)** | CLAUDE.md §11 îl are pe Faza 1, dar consumatorul real e WordPress-ul. `og:image` și `logo` din `Organization` ar trebui să folosească SVG-ul, nu PNG-ul de 19 KB. |

---

*Audit realizat prin inspecție statică a codului și randare în Chromium
headless. Fără date de Search Console, fără date de trafic, fără crawl live —
prototipul nu e publicat pe domeniul canonic.*
