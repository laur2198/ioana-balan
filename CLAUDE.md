# ioana-balan.ro — context de proiect

Document de referință pentru dezvoltarea site-ului. Citește-l înainte de
orice modificare de design sau structură.

---

## 1. Proiectul

Redesign complet pentru site-ul unei soliste de muzică populară / formație
de nuntă. Livrat de **Green Pheonix Concept SRL**.

**Fluxul de lucru:**

1. Prototip static (acest repo) — HTML + Tailwind CDN, pentru validare cu clientul
2. După validare → reimplementare în **WordPress + Elementor** (cerință fermă a clientului, nenegociabilă)

Codul din acest repo este **de unică folosință**. Scopul lui e să arate
clientului cum va arăta site-ul și să permită iterații ieftine. Nu
supra-ingineri, nu adăuga build tools, nu optimiza pentru producție.

**Domeniu canonic:** `ioana-balan.ro` (cu cratimă)

---

## 2. Cine e artista

Ioana Balan — solistă de muzică populară și folclor, activă de peste 15 ani,
cu discografie proprie (albume „Rădăcini" 2018, „Glasul Inimii" 2021, lansare
nouă 2025). Cântă la nunți, botezuri și evenimente corporate, împreună cu
formația, sub umbrela **Grand Music Events**.

**Tensiunea de brand — cea mai importantă decizie de design:**

Materialele oscilează între două identități:

- **Folclor autentic** — poartă ie tradițională, repertoriu de doine și
  cântece de petrecere, „Esența Tradiției", „Rădăcini"
- **Premium corporate** — „excelență artistică", „experiență curatoriată",
  estetică inspirată de Mercedes (fișierele WordPress folosesc chiar fontul
  Mercedes, Corporate A BQ)

**Rezolvarea:** nu alegem una și o eliminăm pe cealaltă. Site-ul trebuie să
fie *tradiție prezentată premium* — nu folclor rustic, nu lux generic. Asta e
diferențiatorul ei real: e singura care poate fi și autentică, și scumpă.

---

## 3. Publicul și comportamentul lui

- Miri, nași, părinți care organizează botezuri, firme care fac gale
- **Caută predominant de pe mobil**
- Insight direct de la client: *„oamenii nu au răbdare să citească, vor
  sumele și ofertele direct"*
- Canalul preferat de contact: **WhatsApp**, apoi telefon. Formularul e secundar
- Decizia se ia rapid și se validează social (recenzii, video, recomandări)

**Consecință de design:** fiecare pagină trebuie să răspundă la trei
întrebări în primele secunde — *ce oferă*, *cât costă*, *cum o contactez*.

---

## 4. Piața (concluzii din analiza de competiție)

8 site-uri de formații/soliste analizate, pe mobil.

| Constatare | Implicație |
|---|---|
| Doar ~37% afișează prețuri; unul singur îl are înainte de scroll | Prețul vizibil devreme = **diferențiator**, nu standard |
| WhatsApp + telefon la 1 tap = mecanism dominant | Obligatoriu, pe toate paginile |
| Video live în hero — doar unul îl are | Oportunitate mare |
| Recenzii cu număr, vizibile sus — doar unul le exploatează | Ioana are **5,0★ / 61 recenzii** — activ subutilizat |
| Majoritatea randează desktop pe mobil, text mic | Mobile-first real = avantaj competitiv |
| 6 din 8 folosesc sans-serif pe body | Serif pe body e împotriva curentului |

**Poziționarea de preț:** pachetele Ioanei (4.800–6.500 €) sunt în **vârful
pieței** — concurența pornește de la 500–1.499 €. Consecință: dacă afișezi
prețul devreme, trebuie să afișezi **și justificarea** în același ecran
(recenzii, video, componența formației). Cifra singură alungă.

---

## 5. Sistemul de design

### Culoare

```
--surface           #131313   fundal principal
--surface-container #1c1b1b   carduri, secțiuni alternante
--on-surface        #e5e2e1   text principal
--on-surface-var    #c6c6c6   text secundar
--outline           rgba(255,255,255,0.10)   borduri hairline
--accent            #800020   bordo — SINGURA culoare de accent
--accent-hover      #600018
```

**Bordo-ul nu e ales estetic, ci semantic:** e roșul din costumul popular
românesc, din ia pe care o poartă. Leagă accentul de subiect, nu de o modă.

**Eliminate complet:** coralul `#c95a5c` (derivat din paleta de eroare),
roșul `#690005` (token de eroare folosit ca CTA), bordo-ul hardcodat
`#4D0011`, argintiul `#c8c6c5` ca fond de buton (se topește în text).

### Tipografie

- **EB Garamond** — H1–H3, cifre mari de preț, nume de brand. Se leagă
  natural cu logo-ul-semnătură.
- **Inter** — body, label-uri, butoane, nav, prețuri mici, formular,
  liste de caracteristici.

Minim 16px pe body. Uppercase + letter-spacing extins doar pe eyebrow-uri
scurte, niciodată pe paragrafe sau label-uri lungi.

### Ierarhie CTA (fără excepții)

- **Primar:** fond bordo, text alb. Maxim unul per secțiune vizibilă.
- **Secundar:** contur argintiu, fond transparent.

Vocabular consecvent: aceeași acțiune poartă mereu același nume. „Rezervă
Acum" și „Cere ofertă" sunt acțiuni **diferite** — nu le folosi interschimbabil.

### Logo

Semnătura scrisă de mână a artistei, **vectorizată** — SVG alb pe transparent.
Fără fotografie, fără casetă neagră. Variante: orizontal (header), compact
(favicon, social).

---

## 6. Ce face site-ul *al ei*, nu un template

**Riscul de evitat:** „fundal negru + un accent saturat + serif elegant" e
un look implicit, produs identic pentru orice brand de lux. Corect, dar
anonim. Dacă site-ul ar putea fi al unui restaurant sau al unei case de
modă schimbând doar textul, am greșit.

**Ancora vizuală: broderia de pe ie.**

Motivele geometrice românești (romb, cruciuliță, linie frântă) devin
**elementul structural** al site-ului — nu ornament aplicat pe deasupra:

- Separatoarele dintre secțiuni: în loc de linie hairline simplă, un motiv
  de cusătură repetat, subțire, la 15–20% opacitate
- Ancorele de secțiune și marcajele de listă: derivate din același vocabular
- Un motiv discret ca textură de fundal în secțiunile importante (foarte subtil)

Sursa e reală: pozele existente ale artistei în ie conțin exact aceste
motive. Se extrag și se vectorizează.

**Restul rămâne disciplinat.** Un singur loc unde îndrăznești. Fotografia
alb-negru (deja folosită) contrastează cu accentul bordo și dă seriozitate.
Nu adăuga gradienți, glow-uri, sau animații decorative.

**Fotografia** e al doilea activ: alb-negru pentru portrete și atmosferă,
color doar acolo unde costumul popular trebuie să se vadă. Contrastul dintre
cele două e o decizie, nu o inconsecvență.

---

## 7. Reguli de conținut

- Textul e material de design, nu umplutură. Dacă un paragraf nu ajută
  la decizie, taie-l.
- Specific bate generic: „formație 6 instrumente + 3 interpreți" bate
  „echipă profesionistă".
- Cifrele se scriu ca cifre, vizibile, nu îngropate în proză.
- Ton: cald și direct, fără superlative goale. Fără „excelență",
  „experiență de neuitat", „momente magice" — sunt clișee de industrie.
- Dovada socială se exprimă în cifre: **5,0★ · 61 de recenzii pe Google**.

---

## 8. Constrângeri tehnice (prototip)

- HTML static + Tailwind prin CDN, config inline pe fiecare pagină
- **Nu** adăuga build tools, npm, bundlere — codul se aruncă la migrare
- **Nu** înlocui imaginile (sunt placeholdere Stitch care vor expira;
  clientul furnizează originalele)
- Formularele nu au backend (se rezolvă în WordPress)
- Paginile legale (Termeni, Confidențialitate) nu există — `href="#"`
- Quality floor obligatoriu: responsive până la 360px, focus vizibil la
  tastatură, `prefers-reduced-motion` respectat, contrast ≥4.5:1

### Cu ochii pe Elementor

Fiecare decizie de design trebuie să fie **exprimabilă în containere
flexbox**. Ce nu încape acolo ajunge CSS custom în WordPress — cost
suplimentar și pierdere de editabilitate pentru client. Evită layout-uri
care depind de grid complex, overlap-uri sau poziționare absolută
elaborată.

Efecte scumpe de limitat: `backdrop-filter: blur` (maxim un element per
pagină), tranziții grayscale→color pe imagini mari, parallax.

---

## 9. Ce e decis vs. ce e deschis

**Decis:**
- WordPress + Elementor ca destinație finală
- Structura de 8 pagini + blog
- Sistemul de culoare și tipografie de mai sus
- Logo = semnătura existentă, vectorizată
- WhatsApp ca mecanism principal de conversie
- SEO local pe 5 orașe: București, Ploiești, Brașov, Craiova, Pitești
- Recenziile Google se afișează selectiv (6–8), cu cifra 5,0★/61 proeminentă
- Emailul oficial: `ioanabalanoficial@gmail.com` — adresa reală, confirmată
  (aceeași pe Facebook, YouTube și site-ul actual). `contact@ioanabalan.ro`
  și `contact@ioana-balan.ro` nu există; nu se mai folosesc.

**Deschis — nu implementa fără confirmarea clientului:**
- Dacă prețurile urcă pe homepage (el e cel mai scump din piață —
  decizie de poziționare, nu de UX)
- Wording-ul descrierii din footer
- Adresa fizică publică (există în Google Business Profile)

---

## 10. Starea repo-ului

8 pagini: `index`, `galerie`, `discografie`, `servicii`, `oferte`,
`contact`, `blog`, `articol`.

Fragmentele WordPress primite de la client (header/footer, styles.css,
export Discografie) au fost eliminate din repo: nu făceau parte din site și
conțineau patru handle-uri sociale false plus `ioanablanoficial@gmail.com`,
la un caracter distanță de adresa reală — risc de copy-paste la handoff.
Rămân recuperabile din istoricul git, în commit-ul baseline `8026eb9`.

**Făcut:** navigație unificată, contacte normalizate, CTA-uri funcționale,
WhatsApp pe toate paginile, meta tags + Open Graph, header/footer canonice.

**Probleme cunoscute:** imaginile sunt placeholdere temporare; formularele
nu trimit; paginile legale lipsesc; logo-ul e semnătura curată (PNG cu fundal
transparent, `assets/logo-alb-*.png`), nu încă SVG — vectorizarea rămâne de
făcut înainte de migrarea în WordPress.

---

## 11. Roadmap

| Fază | Conținut |
|---|---|
| ✅ 0 | Analiză de competiție |
| ▶ 1 | Sistem de design unificat + logo vectorizat |
| 2 | Validare cu clientul pe prototip |
| 3 | Implementare WordPress + Elementor |
| 4 | SEO local (5 orașe), AEO, performanță |
| 5 | Migrare, redirecționări 301, lansare |
| 6 | Predare + instruire pentru administrarea blogului |
