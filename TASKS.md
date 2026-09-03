# TASKS — ioana-balan.ro

> **Sursa de adevăr este [`CLAUDE.md`](CLAUDE.md).** Acest fișier traduce strategia din
> `CLAUDE.md` în taskuri executabile. Citește `CLAUDE.md` înainte de orice modificare de
> design sau structură. Vezi și `README.md` pentru stack/rulare.
>
> **Prototip static** (8 pagini HTML, Tailwind Play CDN, config inline per pagină) pentru
> validare cu clientul → apoi **reimplementare WordPress + Elementor** (destinație fermă).
> Codul de aici e de unică folosință: **fără build tools, fără npm, fără optimizare de
> producție**. Nu supra-ingineri.
>
> **Faza curentă (roadmap ▶1):** *Sistem de design unificat + logo vectorizat.*
>
> **Quality floor obligatoriu pe orice task de UI:** responsive până la **360px**, focus
> vizibil la tastatură, `prefers-reduced-motion` respectat, contrast **≥4.5:1**. Fiecare
> layout trebuie exprimabil în **containere flexbox** (constrângere Elementor).

---

## Decizii — starea lor (reconciliate cu CLAUDE.md)

| # | Subiect | Stare |
|---|---------|-------|
| ✅ D-domain-web | Domeniul web | **DECIS: `ioana-balan.ro`** (cu cratimă) |
| ✅ D-grand-music | „Grand Music Events" | **DECIS: se păstrează** — e umbrela reală a formației |
| ✅ D-design-dir | Direcția de design | **DECIS: live (EB Garamond/Inter + bordo)**. Aurul `#d4af37` din exportul Stitch (eliminat din repo, vezi commit-ul baseline `8026eb9`) = NU se folosește |
| ✅ D-email | Adresa de email oficială | **DECIS: `ioanabalanoficial@gmail.com`** — adresa reală, confirmată (Facebook, YouTube, site-ul actual) |
| 🟠 D-preturi | Dacă prețurile urcă pe homepage (poziționare, el e cel mai scump din piață) | **DESCHIS** — confirmă clientul |
| 🟠 D-adresa | Adresa fizică publică în footer/contact | **DESCHIS** — confirmă clientul |

---

## 🎨 Faza 1 — Sistem de design & identitate (PRIORITATE MAXIMĂ)

### T-D1 — Logo vectorizat (SVG semnătură)
- **Prioritate:** Critică · **Fișiere:** header + footer pe toate cele 8, favicon
- Logo-ul actual e bannerul de YouTube (conține fotografie). Se înlocuiește cu **semnătura
  scrisă de mână a artistei, vectorizată** — SVG alb pe transparent, fără casetă neagră.
  Variante: orizontal (header), compact (favicon/social). Client furnizează sursa.
- **Acceptare:** SVG semnătură în header/footer pe toate paginile; variantă compactă pentru favicon (leagă T-SEO1).

### T-D2 — Motiv de broderie (ie) ca element structural
- **Prioritate:** Înaltă · **Fișiere:** componente partajate (separatoare, liste, texturi)
- Ancora vizuală care face site-ul *al ei*, nu un template. Motive geometrice românești
  (romb, cruciuliță, linie frântă), extrase și vectorizate din pozele reale în ie:
  - **Separatoare de secțiune:** motiv de cusătură repetat, subțire, 15–20% opacitate (înlocuiește hairline-ul simplu)
  - **Ancore de secțiune + marcaje de listă:** derivate din același vocabular
  - **Textură de fundal foarte subtilă** în secțiunile importante
- Disciplină: un singur loc unde îndrăznești. Fără gradienți, glow, animații decorative.
- **Acceptare:** motivul apare ca separator/ancoră pe minim index + oferte; SVG reutilizabil; respectă `prefers-reduced-motion`.

### ✅ T-D3 — Verificare & normalizare tokeni de culoare — FĂCUT
- **Prioritate:** Medie · **Fișiere:** `assets/tailwind.config.js`, `assets/styles.css`, `blog`, `articol`
- **Coralul `#c95a5c` NU era eliminat — era folosit activ** ca al doilea sistem de accent
  (8 locuri): etichetele de categorie din blog, panoul de newsletter (fond maroniu
  `bg-tertiary-container` + text coral), badge-ul „Expertise" din articol. Convertite la
  sistemul neutru aprobat: `text-primary` pentru eyebrow-uri/etichete, `bg-surface-container`
  + `text-on-surface`/`on-surface-variant` pentru panou, stil de input identic cu formularul
  canonic din contact.
- **`.burgundy-btn` (`#410007`)** — CSS mort (0 utilizări), definea un al doilea bordo
  concurent cu accentul → eliminat din `assets/styles.css`.
- **Definiții de tokeni nefolosite eliminate din config** ca să nu poată fi refolosite:
  `on-tertiary-container` (#c95a5c), `on-error` (#690005), `on-tertiary-fixed` (#410007).
- `#4D0011` era deja absent. Argintiul `#c8c6c5` — verificat: apare doar ca linii
  despărțitoare, wash 3%, hover state și badge-uri cu text închis (`text-on-primary`),
  **nu ca fond de buton** unde „se topește în text" → conform.
- Outlierii galerie (`borderRadius:0`, `letterSpacing:0.15em`) — rezolvați deja prin
  config-ul unic din T-WP2.
- **Acceptare:** ✓ 0 apariții ale culorilor eliminate (markup + assets); config JS valid.
- **🟠 CONSTATARE NOUĂ, necesită decizie:** familia `tertiary` (`#ffb3b1`, roz deschis) e încă
  folosită ca accent în ~19 locuri — eyebrow „Articol & Inspirație" (blog), eyebrow „Arhivă"
  + linie (galerie), fundalurile badge-urilor de categorie, culori de selecție. Nu e pe lista
  explicită din CLAUDE.md, dar încalcă principiul „bordo = SINGURA culoare de accent".
  E o decizie de design pe ~19 utilizări — nu am schimbat-o unilateral.

### ✅ T-D4 — Ierarhie CTA & tipografie (audit) — FĂCUT
- **Prioritate:** Medie · **Fișiere:** toate
- **Ierarhie CTA — OK, fără încălcări reale.** Numărătoarea inițială (servicii 7, oferte 5)
  era umflată de utilizări decorative ale `bg-accent` (`bg-accent/10`, linii, badge-ul „Cel mai
  popular"). CTA-uri primare reale: max 1 per secțiune. Excepție acceptată: grila de prețuri
  din `oferte` are 2 primare (Standard + Premium) și 2 secundare (Botez) — ierarhie deliberată.
- **Vocabular unificat** (aceeași acțiune = același nume):
  - `servicii`: „Solicită Ofertă Nuntă" → **„Solicită Ofertă"** (se bătea cu cel din josul paginii)
  - `galerie`: „Contact Evenimente" → **„Contact"**
  - `articol`: „Contactează-ne" → **„Contact"**
- **Tipografie:**
  - Copyright footer: eliminat `uppercase tracking-tighter` de pe label lung (8 pagini) →
    „© 2010-2026 Ioana Balan. Toate drepturile rezervate."
  - Body sub 16px pe mobil corectat: badge rating (13px→16) ×3, citate testimoniale (15px→16) ×3,
    caption index (14px→16) ×1. Rămâne doar copyright-ul la 12px — microtext legal, acceptabil.
- **Acceptare:** ✓ zero uppercase pe text lung; zero body copy sub 16px; vocabular consecvent.
- **✔ Restanța „Vezi Serviciile" a fost rezolvată în T-C3:** e acum „Vezi Servicii", secundar
  și intern (`servicii.html`), identic cu cel de pe index. Vocabular CTA final, fără duplicate:
  primar = Contact / Rezervă Acum / Solicită Ofertă / Rezervă Standard / Rezervă Premium;
  secundar = Vezi Servicii ×2 / Solicită Detalii ×2 / Vezi Repertoriu Live / Vezi Ofertele.

---

## 🎯 Optimizare conversie (CRO)

### ✅ T-CRO1 — Social proof cu cifre reale: 5,0★ · 61 recenzii Google — FĂCUT (parțial: text recenzii = placeholder)
- **Prioritate:** Înaltă · **Fișiere:** `index.html` (hero/aproape de fold), `oferte.html`, `servicii.html`
- **Rezolvat:** badge „5,0★ · 61 recenzii Google" (stele monocrome `text-on-surface` — NU bordo,
  ca să treacă pragul de contrast pe fundal întunecat) în hero pe index/oferte/servicii;
  secțiune de recenzii pe index (3 carduri) între galerie și CTA; `aggregateRating` 5.0/61
  adăugat în JSON-LD `EntertainmentBusiness` din contact (validat).
- **RĂMÂNE (client):** textele celor 6–8 recenzii reale din Google Business Profile.
  Cardurile actuale sunt PLACEHOLDER marcate în cod (`<!-- NOTĂ ... -->`), cu atribuiri pe
  tip de eveniment/oraș (nu nume inventate). De înlocuit înainte de lansare.
- Activ subutilizat, diferențiator față de concurență. Afișează cifra **5,0★ / 61 recenzii**
  proeminent, sus. Selectiv 6–8 recenzii Google afișate. Adaugă `aggregateRating` în JSON-LD
  (leagă T-SEO2). Dovada socială în cifre, nu proză.
- **Acceptare:** „5,0★ · 61 recenzii" vizibil înainte de scroll pe index; 6–8 recenzii; `aggregateRating` valid.

### T-CRO2 — Preț vizibil devreme + justificare în același ecran 🟠 (ghidat de D-preturi)
- **Prioritate:** Înaltă · **Fișiere:** `index.html`, `oferte.html`
- Doar ~37% din concurență afișează prețuri; unul singur înainte de scroll → oportunitate.
  DAR pachetele (4.800–6.500 €) sunt în vârful pieței: cifra singură alungă. Dacă afișăm
  prețul devreme (după D-preturi), în **același ecran** trebuie și justificarea: recenzii,
  video, componența formației („6 instrumente + 3 interpreți").
- **Acceptare:** conform D-preturi — dacă da, preț + justificare în același viewport; dacă nu, prețul rămâne pe oferte.

### ✅ T-CRO3 — Contact la 1 tap: WhatsApp + telefon pe toate paginile — FĂCUT
- **Prioritate:** Înaltă · **Fișiere:** toate cele 8
- **Rezolvat:** `.whatsapp-float` canonic pe toate 8 paginile (verde `#25d366`, 56/60px,
  puls prin inel `box-shadow`, `z-index:50` sub meniul mobil `z-[60]`, `prefers-reduced-motion`
  respectat). Markup unificat (`class="whatsapp-float"` + `rel="noopener"`). Eliminate:
  widget-ul „Concierge" ne-verde din blog, `pulse-soft` din servicii, pozițiile inline
  divergente. Prefill `?text=` pe toate CTA-urile WhatsApp: generic pe flotant + contextual
  pe hero (index), header (contact), CTA (servicii); pachetele oferte aveau deja.
- Canalul dominant: WhatsApp, apoi telefon; formularul e secundar. `.whatsapp-float` există
  dar animația de puls e doar pe `servicii.html:485-491` — uniformizează pe toate paginile.
  Extinde mesajele WhatsApp pre-completate (`?text=`, deja pe `oferte.html:298/327/360/384`)
  la CTA-ul hero (`index.html:207`), header și contact, cu mesaj contextual.
- **Acceptare:** WhatsApp float + click-to-call pe toate paginile; mesaje pre-completate contextuale.

### ✅ T-CRO7 — Secțiune Evenimente cu clipuri YouTube — FĂCUT (ID-uri de completat)
- **Prioritate:** Înaltă · **Fișiere:** `galerie.html`, `index.html`
- **Constatare:** secțiunea „Clipuri YouTube" existentă pe galerie era **pur decorativă** —
  buton de play, thumbnail, `cursor-pointer`, dar **zero linkuri/embed-uri**. Clicul nu făcea
  nimic. A fost înlocuită, nu dublată.
- **Rezolvat:**
  - `galerie` → bento „Cum arată un eveniment": desktop mozaic 12 coloane (video 8 + poză 4 /
    poză 4 + video 8), mobil stivă pe 1 coloană. Poze + clipuri împreună.
  - `index` → „gustare": 2 clipuri + link „Vezi toate" spre galerie, plasată între galerie și
    recenzii (video-ul e tot dovadă socială).
  - **Facade pattern:** iframe-ul YouTube se încarcă **doar la click**, nu la load — 2 embed-uri
    grele evitate per pagină. Butoanele sunt `<button>` real (accesibile la tastatură).
  - Placeholder-ele (`data-yt="TODO"`) deschid canalul YouTube, ca să nu rămână butoane moarte.
  - Fără `backdrop-blur` pe butonul de play (CLAUDE.md: max 1 `backdrop-filter`/pagină).
- **ID real găsit în cod:** `hPACrfwibFw` = „Hai să nu ne mai mințim" (era în `discografie.html`).
- **🟠 RĂMÂNE (client):** ID-urile YouTube pentru celelalte 2 sloturi + titlurile reale.
- **🟠 DE CONFIRMAT:** dacă vrei o pagină separată „Evenimente" — **nu am creat-o**, fiindcă
  CLAUDE.md §9 listează structura de 8 pagini ca **decisă**, iar o a 9-a pagină crește costul
  migrării în Elementor.

### T-CRO4 — Video live în hero
- **Prioritate:** Medie · **Fișiere:** `index.html`
- Oportunitate mare (doar 1/8 concurenți îl are). Video live discret în hero (client
  furnizează). Respectă `prefers-reduced-motion` și mobile-first; nu blochează LCP.
- **Acceptare:** video în hero pe desktop+mobil, cu fallback imagine; reduced-motion respectat.

### 🟡 T-CRO5 — „Ce oferă / cât costă / cum contactez" în primele secunde — AUDITAT structural
- **Prioritate:** Medie · **Fișiere:** toate paginile
- Insight client: „oamenii nu au răbdare să citească, vor sumele și ofertele direct".
- **Rezultatul auditului (structural — ordinea în DOM, nu măsurători pixel):**
  - **„ce oferă"** ✓ — exact 1 `<h1>` descriptiv pe fiecare pagină
  - **„cum contactez"** ✓ — WhatsApp float e `position: fixed`, deci prezent în primul ecran
    pe toate cele 8 pagini, la 1 tap
  - **„cât costă"** ⚠️ — apare doar pe `oferte` (10 mențiuni). **`servicii` are ZERO mențiuni
    de preț**, iar pe `index` singura apariție e îngropată în FAQ.
- **🟠 RECOMANDARE, nu implementată (atinge poziționarea):** un semnal de preț pe `servicii`
  (ex. „Pachete de la 5.500 €" cu link spre oferte). Justificarea cerută de CLAUDE.md în același
  ecran există deja acolo — badge-ul 5,0★/61 din T-CRO1. D-preturi e formulat strict pentru
  *homepage*, deci `servicii` nu e blocat tehnic — dar e tot o decizie de poziționare, așa că
  aștept confirmare.
- **RĂMÂNE:** verificarea reală pe 360px necesită randare în browser.

### T-CRO6 — Formulare (secundare) 🟠 (ghidat de D5 din discuție)
- **Prioritate:** Joasă · **Fișiere:** `contact.html:268-304` (+JS `:341-355`), `blog.html:325-328`
- Booking form are submit fals (cosmetic); newsletter e complet inert. Backend real vine în
  WordPress (T-WP4). În prototip: fie serviciu temporar (Formspree) pentru testare, fie TODO documentat.
- **Acceptare:** submit real temporar SAU placeholder marcat clar în cod.

---

## 🔍 SEO & structură

### T-SEO1 — Favicon + apple-touch + manifest (lipsesc pe TOATE paginile)
- **Prioritate:** Înaltă · **Fișiere:** `<head>` toate cele 8
- Set complet de favicon din varianta compactă a logo-ului (T-D1), uniform pe toate paginile.
- **Acceptare:** favicon în tab pe toate paginile; 16/32/apple-touch/manifest.

### ✅ T-SEO2 — Extindere JSON-LD la toate paginile — FĂCUT
- **Prioritate:** Înaltă · **Fișiere:** `index`, `articol`, `blog`, `galerie`, `discografie`, `servicii`
- **Rezolvat:** toate cele 8 pagini au acum structured data (înainte doar contact + oferte):
  - `index` → **MusicGroup** + `aggregateRating` 5,0/61 + `sameAs` (4 rețele) + `areaServed` (5 orașe)
  - `articol` → **BlogPosting** (headline, datePublished 2024-08-15, author, publisher, mainEntityOfPage)
  - `blog` → **Blog** + **BreadcrumbList** (@graph)
  - `discografie` → **MusicAlbum ×3** (Hai să nu ne mai mințim 2025, Glasul Inimii 2021, Rădăcini 2018)
  - `galerie` → **ImageGallery** · `servicii` → **Service** + `areaServed` (5 orașe)
  - `contact` → EntertainmentBusiness (avea deja; +aggregateRating din T-CRO1) · `oferte` → Product+Offer
- Toate blocurile validate ca JSON parsabil (script Python, 8/8 OK).
- **RĂMÂNE:** validare finală cu Google Rich Results Test după publicare (necesită URL live).

### ✅ T-SEO3 — SEO local pe 5 orașe — FĂCUT
- **Prioritate:** Medie · **Fișiere:** `oferte`, `contact`, `galerie`, `servicii` (+ index/servicii aveau deja)
- Orașe țintă: **București, Ploiești, Brașov, Craiova, Pitești**.
- **Audit inițial:** Pitești aproape absent (1 mențiune pe tot site-ul); `oferte.html` avea
  **zero** geografie deși e pagina de prețuri (intenție locală maximă); contact fără Craiova/Pitești.
- **Rezolvat:**
  - `areaServed` (5 orașe) acum pe **4 pagini**: index (MusicGroup), servicii (Service),
    contact (EntertainmentBusiness), oferte (pe fiecare `Offer` — `Product` nu suportă `areaServed`).
  - Meta/OG/Twitter completate cu orașele lipsă pe contact, galerie, servicii.
  - `oferte`: adăugat un rând real de conținut („Cântăm în București, Ploiești, Brașov,
    Craiova și Pitești — și în restul țării, la cerere.") — informație care ajută decizia,
    nu keyword stuffing.
- **Acceptare:** ✓ toate cele 5 pagini cu relevanță locală acoperă toate cele 5 orașe;
  JSON-LD valid 8/8. Blog/articol/discografie lăsate intenționat fără geografie forțată.

### ✅ T-SEO4 — Fix meta description duplicat + title/OG mismatch — FĂCUT
- **Prioritate:** Joasă · **Fișiere:** `galerie.html`, `articol.html`
- **Description duplicat:** deja rezolvat între timp — verificat 1 `<meta name="description">`
  pe fiecare din cele 8 pagini.
- **Title/OG mismatch — rezolvat pe 2 pagini** (aliniate la varianta descriptivă cu keyword):
  - `galerie`: „Galerie | IOANA BALAN" → „Galerie | Ioana Balan — Formație Nuntă București"
  - `articol`: aliniat la „Importanța luminilor de scenă pentru show-ul formației | Ioana Balan"
- **Bonus:** corectat `image` din `BlogPosting` (folosea og:image-ul de pe index; acum folosește
  imaginea proprie a articolului) + `headline` aliniat la titlu.
- **Notă:** `articol.html` scrie meta cu atributele inversate (`content=` înaintea lui
  `property=`) și tag-uri self-closing XHTML — vezi T-C4 pentru normalizare structurală.
- **Acceptare:** ✓ 8/8 pagini cu title = og:title = twitter:title; JSON-LD valid pe toate.

---

## 🧹 Curățare & consistență

### ✅ T-C1 — Aliniere adresă email — FĂCUT
- **Fișiere:** toate paginile + JSON-LD din `contact.html`
- `contact@ioanabalan.ro` și `contact@ioana-balan.ro` (ambele inexistente) au fost
  înlocuite peste tot cu `ioanabalanoficial@gmail.com`.
- **Acceptare:** o singură adresă de email în tot proiectul, inclusiv în JSON-LD. ✅

### ✅ T-C2 — Conectare bloc social secundar din contact — FĂCUT (rezolvat între timp)
- **Prioritate:** Medie · **Fișiere:** `contact.html`
- **Verificat:** blocul social neconectat a dispărut; `contact.html` are acum cele 4 linkuri
  reale (Facebook / Instagram / YouTube / TikTok). Singurele `href="#"` rămase pe pagină sunt
  linkurile legale (Termeni, Politică) — așteptat, vezi T-C5.
- **🟠 RĂMÂNE (client, D4):** de confirmat că cele 4 handle-uri sunt conturi reale — folosesc
  patru stiluri diferite de denumire (`ioanabalan` / `iamioanabalan` / `@BalanIoana` /
  `@ioanabalanmusic`), ceea ce e suspect. Nu poate fi verificat din cod.
- **Acceptare:** fără `href="#"` în blocul social din contact; handle-uri confirmate.

### ✅ T-C3 — Linkuri externe grand-music.ro în articol — FĂCUT
- **Prioritate:** Joasă · **Fișiere:** `articol.html`
- Grand Music e brand real (D-grand-music: se păstrează), dar site-ul trebuie să rețină vizitatorul.
- **Rezolvat — toate 3 linkurile externe eliminate, brandul păstrat ca text:**
  - link SEO pe „lumini scena" în mijlocul textului → text simplu („lumini de scenă")
  - „La grand-music.ro, punem accent..." (copy scris din perspectiva altui site) →
    „La **Grand Music Events**, punem accent..." — brand păstrat, link scos
  - CTA „Vezi Serviciile" → `servicii.html`, redenumit **„Vezi Servicii"**, trecut pe
    **secundar**; „Contact" a devenit primarul acelei secțiuni (acțiunea dorită acolo e
    contactul) → rezolvă și restanța din T-D4.
  - Scos „pe site-ul nostru oficial" din copy, care trimitea în afara site-ului.
- **Acceptare:** ✓ zero linkuri externe reziduale pe tot site-ul (verificat și
  `oferta-nunta.ro` / `muzica-nunta.ro`).

### ✅ T-C4 — Normalizare `articol.html` (DOCTYPE + sintaxă) + selector mort — FĂCUT
- **Prioritate:** Joasă · **Fișiere:** `articol.html`
- **Rezolvat:** DOCTYPE era deja adăugat între timp; **19 tag-uri self-closing XHTML**
  (`meta`/`link`/`img`) normalizate la `>` (toate void elements — verificat că niciun element
  non-void nu era self-closed înainte de înlocuire); selectorul JS mort
  `img[src*="IMAGE_21"]` eliminat împreună cu listener-ul de parallax pe care îl făcea inert
  (și `CLAUDE.md` cere oricum limitarea parallax-ului).
- **Bonus:** eliminat linkul duplicat de font Material Symbols (era încărcat de 2 ori).
- **Acceptare:** ✓ DOCTYPE prezent, 0 tag-uri XHTML, 0 selectori morți, JS inline valid (node).

### T-C5 — Pagini legale + placeholdere `href="#"`
- **Prioritate:** Joasă · **Fișiere:** footer toate (Termeni/Politică/ANPC); `blog.html:281-282`, `:296-314`, `:372-373`
- Stub-uri acceptabile în prototip. Backlog WordPress: pagini legale reale, paginație și
  filtre funcționale. Opțional în static: pagini legale placeholder.
- **Acceptare:** documentat ca backlog WordPress.

---

## 🏗️ Pregătire migrare WordPress + Elementor (backlog rebuild)

> Nu se execută în prototipul static; documentate pentru faza Elementor. Constrângere
> transversală: fiecare layout **exprimabil în flexbox**; evită grid complex, overlap-uri,
> poziționare absolută elaborată. Efecte scumpe de limitat: `backdrop-filter: blur` (max 1
> element/pagină), tranziții grayscale→color pe imagini mari, parallax.

### T-WP1 — Re-găzduire imagini (risc de expirare)
- **Critică (rebuild)** · toate (~50 `<img>` din `lh3.googleusercontent.com/aida-public/...`, CDN Stitch efemer). Client furnizează originalele. Descarcă + încarcă în Media Library, re-mapează `src` (inclusiv 2 background-uri CSS `url()`).
- **Acceptare:** zero dependențe lh3/aida-public.

### 🟡 T-WP2 — Consolidare stilizare (8 configuri → 1 stylesheet) — FĂCUT parțial (în prototip)
- **Înaltă (rebuild)** · Paleta de ~55 tokeni + configul Tailwind erau duplicate pe fiecare
  pagină; blocurile custom (`.glass-card`, `.glass-panel`, `.whatsapp-float`,
  `.cinematic-vignette` etc.) inconsistente.
- **Rezolvat:** config extras în `assets/tailwind.config.js` (superset canonic, după CDN) +
  tot CSS-ul custom în `assets/styles.css` (reuniune reconciliată). Cele 8 pagini linkează
  ambele; zero blocuri inline rămase. Divergențe unificate: `.material-symbols-outlined`
  (wght 300), `.glass-card` (:hover + `-webkit-backdrop-filter`), `body`. Ca efect secundar
  s-au normalizat și outlierii galerie (`borderRadius:0`, `letterSpacing:0.15em`) → canonic.
  Validat: config JS parsabil (node), CSS echilibrat.
- **RĂMÂNE (rebuild):** înlocuirea Play CDN cu CSS compilat (build step — în WordPress);
  limita `backdrop-filter` max 1/pagină (Elementor).
- **DE VERIFICAT în browser:** deschide o pagină și confirmă că stilurile se aplică (Play CDN
  citește config-ul extern după CDN — pattern standard, dar merită o privire vizuală).

### T-WP3 — Formulare cu backend real
- **Înaltă (rebuild)** · Contact Form 7 / Fluent Forms + email pentru booking; serviciu newsletter. Anti-spam + validare.
- **Acceptare:** submit real cu notificare email.

### T-WP4 — Mapare slug-uri navigație (clean URLs)
- **Medie (rebuild)** · Slug-urile din exportul WordPress al clientului (fișier eliminat
  din repo, recuperabil din commit-ul baseline `8026eb9`): `/galerie`,
  `/discografie`, `/servicii-evenimente`, `/oferte-si-pachete`, `/contact`. Redirecturi 301 la migrare.
- **Acceptare:** URL-uri curate + 301 documentate.

### ✅ T-WP5 — Accesibilitate & quality floor — FĂCUT în prototip
> Notă: era listat ca „rebuild", dar CLAUDE.md §8 cere quality floor-ul **în prototip**.
- **Rezolvat pe toate cele 8 pagini:**
  - `aria-expanded="false"` + `aria-controls="mobile-menu"` pe butonul de meniu, **sincronizat
    din JS** la deschidere/închidere (și la închiderea prin click pe un link din meniu)
  - **skip-link** „Sari la conținut" → `<main id="continut" tabindex="-1">`; ascuns până
    primește focus de tastatură
  - **focus vizibil**: regulă globală `:focus-visible` (contur argintiu 2px) în `assets/styles.css`
  - `<label for>` real pe inputul de newsletter din blog (era placeholder-as-label);
    formularul din contact avea deja 5 label-uri pentru 5 câmpuri ✓
  - landmark-uri: `<main>` + `<nav>` prezente pe toate paginile ✓; **exact 1 `<h1>` per pagină** ✓
- **Contrast WCAG verificat programatic:** alb pe bordo **10,83:1** ✓ · text secundar 10,88:1 ✓ ·
  on-surface-variant pe card 9,58:1 ✓ · primary 10,92:1 ✓. Singurul FAIL: **bordo pe fundal
  închis 1,72:1** — motiv pentru care stelele de rating din T-CRO1 sunt monocrome, nu bordo.
- **Verificat:** JS inline valid pe 8/8 (node), CSS echilibrat.
- **RĂMÂNE (rebuild):** audit complet axe/Lighthouse pe site-ul live.

---

## Ordine de lucru recomandată (prototip)

1. **T-D1** — Logo vectorizat SVG *(deblochează T-SEO1 favicon)*
2. **T-D2** — Motiv broderie ie *(diferențiatorul de design)*
3. **T-CRO1** — Social proof 5,0★/61 recenzii
4. **T-CRO3** — WhatsApp/telefon 1-tap + mesaje pre-completate
5. **T-SEO1 + T-SEO2** — Favicon + JSON-LD extins
6. **T-D3 / T-D4** — Verificare tokeni + audit CTA/tipografie
7. **T-CRO4 / T-CRO5** — Video hero + audit fold mobil 360px
8. **T-SEO3 / T-SEO4** — SEO local 5 orașe + fix meta
9. **T-C1…T-C5** — curățare (după deciziile deschise)

> Secțiunea **WordPress** rămâne backlog pentru faza de rebuild.
> **Deschise, nu implementa fără client:** D-email, D-preturi, D-adresa.
