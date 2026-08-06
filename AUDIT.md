# AUDIT — prototip ioana-balan.ro

*Audit read-only, 2026-08-05. Nu s-a modificat niciun fișier. Evaluat ca
prototip de vânzare, nu ca producție.*

## Rezumat

Prototipul e solid tehnic: nav unificat pe 8 pagini cu stare activă corectă,
meniu mobil funcțional (aria-expanded gestionat, scroll-lock), footer identic
byte-cu-byte, formular cu handling grațios, contrast excelent pe textul
principal (butonul primar alb/bordo = 10.83:1), zero culori vechi de paletă
supraviețuitoare (#c95a5c, #690005, #4D0011 — eliminate complet). Sistemul de
CTA e disciplinat: „Rezervă pe WhatsApp" (primar) și „Cere ofertă" (secundar,
→ contact) sunt folosite consecvent ca acțiuni distincte.

**Cele mai grave 3 probleme:**
1. **Recenziile — chiar argumentul de vânzare — sunt sabotate.** Pe homepage
   textul mărturiilor e placeholder vizibil („[Recenzie reală Google — de
   completat.] Text de probă…"), iar cifra „5,0 · 61 recenzii" apare **doar
   pe index**, absentă de pe oferte/servicii/contact — exact ecranele unde
   justifică prețul premium (CLAUDE.md §4).
2. **Preț contradictoriu pe aceeași pagină:** homepage spune „Pachete de la
   4.800 €" (index.html:170) și, mai jos, „Prețurile încep de la 5500€"
   (index.html:380).
3. **Blogul e orfan** — nicio pagină nu linkează spre blog.html; blog și
   articol sunt inaccesibile din navigație.

**Verdict:** se poate arăta clientului ca **direcție de design**, dar NU ca
„aproape gata". Reparând BLOCANTELE (recenzii + preț) prototipul devine o
demonstrație convingătoare; lăsate așa, ele subminează exact teza „preț
premium justificat de dovada socială".

---

## BLOCANT — nu arăta clientului până nu se rezolvă

**Recenzii placeholder pe homepage** — `index.html:298`, `index.html:309`,
`index.html:320`. Cele 3 mărturii afișează literal „*[Recenzie reală Google —
de completat.] Text de probă pentru a valida macheta…*". Secțiunea recenzii e
inima pitch-ului (5,0★/61 recenzii, CLAUDE.md §4/§7); afișată cu text de probă
îl face pe client să vadă un site neterminat, nu poziționarea premium.

**Preț de intrare contradictoriu pe homepage** — `index.html:170` afișează
„Pachete de la **4.800 €**", iar FAQ-ul de pe aceeași pagină, `index.html:380`,
spune „Prețurile încep de la **5500€** pentru pachetul Standard". Clientul e
decidentul pe preț; două cifre de start diferite în același ecran creează
confuzie exact pe subiectul lui.

---

## IMPORTANT — de rezolvat înainte de faza WordPress

**Dovada socială lipsește de pe paginile de conversie.** „5,0 · 61 de recenzii
pe Google" apare doar pe `index.html` (liniile 132, 185, 226, 286). Pe
`oferte.html` (pagina de preț, 4.800–6.500 €), `servicii.html`, `galerie.html`
și `contact.html` nu apare deloc. CLAUDE.md §4: cine afișează prețul devreme
trebuie să afișeze justificarea în același ecran. Oferte are componența
formației în carduri, dar nu cifra recenziilor.

**Blog + articol orfane.** Nav-ul e identic pe toate 8 paginile (ex.
`index.html:71-78`) și **nu conține „Blog"**. Nimic din nav/footer/corp nu
linkează spre `blog.html`; `articol.html` e accesibil doar din blog. Practic
două pagini construite, dar invizibile.

**Logo încă bannerul foto YouTube.** Header-ul (`index.html:65`, identic pe
toate paginile) folosește `<img>` cu o poză googleusercontent, nu semnătura
vectorizată SVG cerută în CLAUDE.md §6/§10. E elementul de brand, greșit pe
fiecare pagină.

**54 de imagini sunt URL-uri Stitch temporare** (toate `lh3.googleusercontent.com/aida-public/…`).
Testate acum: răspund 200, dar sunt linkuri care expiră. Dacă mor înainte/în
timpul demo-ului, toate cele 8 pagini afișează imagini rupte. Verifică-le
imediat înainte de întâlnire.

**Embed-uri video placeholder.** `data-yt="TODO"` pe `index.html:234` și
`galerie.html:165` — click-ul pe facade-ul video deschide canalul YouTube, nu
clipul. Un singur clip real în tot repo-ul (`youtu.be/hPACrfwibFw`). Videoul
live în hero era oportunitatea #1 din analiza de piață (CLAUDE.md §4).

**Formularul cere prea mult de la un public nerăbdător.** `contact.html:161-196`:
5 câmpuri, **toate obligatorii** (nume, email, dată exactă, tip, mesaj liber).
CLAUDE.md §3: „oamenii nu au răbdare… vor sumele direct", canalul preferat e
WhatsApp. Data exactă + mesaj liber obligatorii sunt friction inutil.
(Formularul trimite corect nicăieri — `preventDefault` + succes fals
„VĂ MULȚUMIM", `contact.html:234-249` — de conectat în WordPress.)

**Email pe alt domeniu decât site-ul.** `mailto:contact@ioanabalan.ro`
(9 apariții) — fără cratimă, în timp ce domeniul canonic e `ioana-balan.ro`
(cu cratimă). E un mailto live care poate suna a greșeală sau poate bounce.
(CLAUDE.md §9 îl marchează deschis — vezi DECIZII.)

**Structured data incompletă/inconsistentă.** Doar cardurile Nuntă au
`itemprop="price"` (`oferte.html:147`, `oferte.html:164`); cardurile Botez și
DJ (liniile ~189-232) nu au deloc markup Offer. În plus `itemprop="price"` la
Standard Nuntă = 5500 (Sâmbătă), deci nu reflectă prețul „de la 4800" (Duminică)
afișat vizual.

---

## MINOR — de reținut, nu urgent

- **Linkuri moarte în blog:** paginația și cardurile-sidebar duc la `href="#"`
  — `blog.html:188`, `189`, `203`, `209`, `215`, `221`. (Legalele Termeni/
  Confidențialitate la `#` sunt așteptate, CLAUDE.md §8.)
- **Silver-fill în afara sistemului CTA.** `bg-primary` (#c8c6c5, argintiu)
  folosit ca fond de badge/paginație: `oferte.html:235-237` (Foto Booth / Dry
  Ice / Full FX), `blog.html:187` (pagina activă). Lizibil (text închis
  #313030 pe argintiu ≈ 7.9:1), dar e un al treilea tratament de fond pe lângă
  bordo(primar)/outline(secundar) documentat. CLAUDE.md §5 cerea eliminarea
  argintiului „ca fond de buton".
- **3 imagini cu `alt=""`** — `galerie.html:178`, `galerie.html:198`,
  `index.html:247`. Sunt postere sub butoane video-facade (decorative,
  borderline OK), dar în galerie sunt conținut și ar merita alt real.
- **Formularul de newsletter din blog nu are handler** — `blog.html:232`;
  la submit reîncarcă pagina (spre deosebire de formularul din contact).
- **og:image duplicat** între `contact.html` și `discografie.html` (aceeași
  imagine AB6AXuBroZ6…).
- **Încărcarea fonturilor variază per pagină** — EB Garamond cerut cu spec
  diferit (`index.html` variabil 400..800; `discografie.html` 400;500;600;700;
  `oferte.html` …;800). Inofensiv, dar contrazice ideea de „sursă unică" pe
  care o sugerează configul partajat.
- **EB Garamond pe corp de text** — drop-cap (`articol.html:114`) și un
  pull-quote `<p>` (`articol.html:122`). Deviații stilistice mici de la
  „Garamond doar pe H1–H3".
- **WhatsApp float:** iconul alb pe verde #25d366 = **1.98:1** (pică la
  non-text contrast WCAG 1.4.11). E culoarea de brand WhatsApp și e doar icon
  cu `aria-label`, deci acceptabil, dar de știut.
- **Legende galerie placeholder** — comentarii TODO la `galerie.html:136`,
  `144`, `157` („nume eveniment real").

---

## OBSERVAȚII — lucruri care necesită decizia mea

**Contrast — toate combinațiile reale trec.** Cifre WCAG măsurate:

| Combinație | Raport | Verdict |
|---|---|---|
| alb / bordo #800020 (buton primar) | 10.83:1 | AA + AAA ✓ |
| on-surface #e5e2e1 / fundal #131313 | 14.42:1 | AAA ✓ |
| secondary #c6c6c6 / #131313 | 10.88:1 | AAA ✓ |
| secondary #c6c6c6 / surface-container #20201f | 9.55:1 | AAA ✓ |
| on-surface-variant #c4c7c7 / #131313 | 10.92:1 | AAA ✓ |
| outline #8e9192 ca text (date) / #131313 | 5.85:1 | AA ✓ (nu AAA) |
| primary #c8c6c5 (linkuri/nav) / #131313 | 10.92:1 | AAA ✓ |
| bordo #800020 **ca text** / #131313 | 1.72:1 | ar pica — **dar nefolosit** (0 apariții `text-accent`) |
| alb / WhatsApp #25d366 | 1.98:1 | pică (icon brand, vezi Minor) |

**Config vs. documentație.** CLAUDE.md §5 descrie o paletă curată de 7 tokeni,
dar `assets/tailwind.config.js` e un dump Material de ~55 tokeni cu valori
divergente: `outline` = #8e9192 (spec: `rgba(255,255,255,.10)`),
`surface-container` = #20201f (spec: #1c1b1b), `on-surface-variant` = #c4c7c7
(spec: #c6c6c6). Nu produce probleme vizibile de contrast, dar reconstrucția
WordPress va moșteni numele/valorile greșite dacă nu le aliniezi întâi.

**Config partajat, nu inline.** CLAUDE.md §8 spune „config inline pe fiecare
pagină", dar implementarea le-a consolidat în `assets/tailwind.config.js` +
`assets/styles.css` (mai bine pentru mentenanță). E o îmbunătățire, dar
contrazice documentul — de actualizat CLAUDE.md sau de confirmat abordarea.

**Legături verificate (OK):** toate href-urile interne `.html` din nav/footer/
corp rezolvă la fișiere existente; telefonul e consecvent și valid
(`tel:+40722911485` = `wa.me/40722911485`, E.164 RO); mesajele WhatsApp
pre-completate sunt coerente (5 variante, toate pe același număr);
`_stitch-export/` nu e referit de nicio pagină.

---

## PREGĂTIRE PENTRU ELEMENTOR

**Se traduc direct (widget-uri standard):**
- Header/nav + footer (flexbox simplu, identice pe toate paginile).
- **Galeria** — `galerie.html:106` e un grid CSS responsiv **fără filtre pe
  categorii** (nu există butoane/tab-uri/JS de filtrare). Se face din Image
  Gallery / Galerie Elementor Pro standard. *Îngrijorarea din brief („galerie
  cu filtre → plugin cu taxonomii") nu se aplică — nu există filtre de
  reprodus.*
- Cardurile de preț (oferte) — coloane flexbox + liste.
- FAQ (`index.html:372…`) — `<details>`/`<summary>` → widget Accordion/Toggle.
- Formularul de contact → Elementor Forms (adaugă backendul lipsă).

**Necesită CSS custom:**
- Broderia (motiv de secțiune/listă/textură) — `.motif-separator`, `.motif-rule`,
  `.motif-list`, `.motif-texture` din `assets/styles.css` folosesc pseudo-
  elemente și `background-image` cu SVG. Elementul de identitate → CSS custom
  în WordPress (cost documentat în CLAUDE.md §6/§8).
- Video-facade (lazy-load iframe la click, `index.html:507`) — comportament JS
  ce nu vine din widget standard; fie plugin video-lazy, fie snippet custom.
- Butonul WhatsApp flotant cu puls (`.whatsapp-float`) — CSS/animație custom.
- Badge „Cel mai căutat" poziționat absolut pe cardul Premium
  (`oferte.html:161`).

**Trebuie regândit pentru Elementor:**
- Item-urile „bento" din galerie care se întind pe 2 coloane
  (`lg:col-span-2 lg:aspect-video`, `galerie.html:108`, `154`) — grid cu
  span-uri variabile nu iese curat din galeria standard Elementor; ori
  Elementor Pro Gallery (masonry, dar fără col-span arbitrar), ori layout
  manual pe coloane.
- Secțiunile hero cu imagine + vignetă + textură broderie suprapuse
  (`index.html:104-111`) — mai multe straturi absolute; reproductibil, dar cu
  atenție la ordinea de stivuire în Elementor.

---

## DECIZII CARE ÎMI APARȚIN

1. **Preț pe homepage:** CLAUDE.md §9 spune că afișarea prețului pe homepage e
   decizia ta. Acum e afișat în două locuri (hero „de la 4.800 €" + FAQ
   „5500€"). Îl păstrăm pe homepage? Și **care e prețul de intrare corect** —
   4.800 (Duminică) sau 5.500?
2. **Politica Sâmbătă/Duminică** (4.800–6.500 €) o afișăm public așa cum e în
   oferte, sau doar „de la X"?
3. **Email oficial:** `contact@ioanabalan.ro` (fără cratimă) vs. domeniul
   `ioana-balan.ro` (cu cratimă). Care rămâne adresa live?
4. **Conturi sociale:** `facebook.com/ioanabalan`, `instagram.com/iamioanabalan`,
   `tiktok.com/@ioanabalanmusic`, `youtube.com/@BalanIoana` — patru convenții
   de nume diferite. Sunt toate conturile reale ale artistei sau presupuse?
5. **Blog:** îl adăugăm în meniu acum (îl expunem clientului) sau îl scoatem din
   prototip până la faza SEO?
6. **Recenzii:** îmi dai 6–8 recenzii reale Google (text + autor) ca să
   înlocuiesc placeholderele, sau le lăsăm marcate ca mockup pentru validare?
7. **Active de la client:** numele reale ale evenimentelor din galerie și
   ID-urile YouTube reale (`data-yt`) — le furnizezi tu?
