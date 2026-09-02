# LINKS.md — audit read-only al linkurilor externe și de contact

**Data:** 2026-09-02 · **Metodă:** analiză statică (grep + parsare regex a
tag-urilor `<a>`, `<meta>`, `<link>` și a blocurilor JSON-LD).
**Nicio verificare HTTP live** — nu s-a testat dacă URL-urile răspund 200.

**Fișiere scanate (10):** `index.html`, `galerie.html`, `discografie.html`,
`servicii.html`, `oferte.html`, `contact.html`, `blog.html`, `articol.html`,
`assets/styles.css`, `assets/tailwind.config.js`.

`_stitch-export/` este exclus din scope (nu face parte din site) — vezi
Anexa 1 pentru o singură constatare de acolo, relevantă pentru capitolul B.

**Volum total găsit:**

| Categorie | Ocurențe |
|---|---|
| `https://wa.me/...` | 32 |
| `tel:` | 18 |
| `mailto:` | 9 |
| Linkuri sociale (footer) | 32 (4 × 8 pagini) |
| Linkuri YouTube în conținut | 12 |
| Google Maps / recenzii | 16 |
| ANPC / SAL | 16 |
| JSON-LD (blocuri `application/ld+json`) | 8 (câte unul per pagină) |
| `href="#"`, `href=""`, `javascript:void(0)` **reale** | **0** |

Nu există `twitter:site`, `twitter:creator`, `linkedin`, `x.com` sau
`twitter.com` nicăieri în cele 10 fișiere. `assets/styles.css` și
`assets/tailwind.config.js` nu conțin niciun link extern, social sau de
contact (singurele `url()` din CSS sunt `motifs.svg` local și un SVG inline
`data:` — [styles.css:92](assets/styles.css#L92), [:109](assets/styles.css#L109),
[:124](assets/styles.css#L124), [:132](assets/styles.css#L132)).

---

## 1. WhatsApp — `https://wa.me/40722911485`

Numărul este identic în toate cele 32 de linkuri: `40722911485` (fără `+`,
fără spații). Diferă doar parametrul `?text=`.

| fișier | linia | href (mesaj prefill, decodat) | text ancoră / aria-label | target | rel | context |
|---|---|---|---|---|---|---|
| [index.html:53](index.html#L53) | 53 | `…?text=Bună ziua! Aș dori mai multe informații.` | „Salut! Scrie-mi pe WhatsApp" / `aria-label="Contact Ioana Balan pe WhatsApp"` | `_blank` | `noopener` | widget flotant |
| [index.html:75](index.html#L75) | 75 | `…?text=Bună ziua! Aș dori să rezerv o dată pentru evenimentul meu.` | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [index.html:104](index.html#L104) | 104 | idem (rezerv o dată) | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [index.html:126](index.html#L126) | 126 | idem (rezerv o dată) | „Rezervă pe WhatsApp" | `_blank` | `noopener` | hero |
| [index.html:330](index.html#L330) | 330 | `…?text=Bună ziua! Aș dori **o ofertă** pentru evenimentul meu.` | **„Rezervă data ta"** | `_blank` | `noopener` | finalul secțiunii „Recomandări" |
| [galerie.html:44](galerie.html#L44) | 44 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [galerie.html:66](galerie.html#L66) | 66 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [galerie.html:95](galerie.html#L95) | 95 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [galerie.html:202](galerie.html#L202) | 202 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | secțiune CTA final |
| [discografie.html:60](discografie.html#L60) | 60 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [discografie.html:82](discografie.html#L82) | 82 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [discografie.html:111](discografie.html#L111) | 111 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [discografie.html:272](discografie.html#L272) | 272 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | secțiune CTA final |
| [servicii.html:45](servicii.html#L45) | 45 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [servicii.html:67](servicii.html#L67) | 67 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [servicii.html:96](servicii.html#L96) | 96 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [servicii.html:241](servicii.html#L241) | 241 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | secțiune CTA final |
| [oferte.html:64](oferte.html#L64) | 64 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [oferte.html:86](oferte.html#L86) | 86 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [oferte.html:115](oferte.html#L115) | 115 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [oferte.html:179](oferte.html#L179) | 179 | `…?text=Bună ziua**,** mă interesează pachetul Standard Nuntă` | „Rezervă pe WhatsApp" | `_blank` | `noopener` | card pachet „Standard Nuntă" |
| [oferte.html:196](oferte.html#L196) | 196 | `…?text=Bună ziua**,** mă interesează pachetul Premium Nuntă` | „Rezervă pe WhatsApp" | `_blank` | `noopener` | card pachet „Premium Nuntă" |
| [contact.html:69](contact.html#L69) | 69 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [contact.html:98](contact.html#L98) | 98 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [contact.html:103](contact.html#L103) | 103 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [blog.html:71](blog.html#L71) | 71 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [blog.html:100](blog.html#L100) | 100 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [blog.html:213](blog.html#L213) | 213 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |
| [articol.html:65](articol.html#L65) | 65 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | header, CTA desktop |
| [articol.html:94](articol.html#L94) | 94 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | meniu mobil |
| [articol.html:153](articol.html#L153) | 153 | rezerv o dată | „Rezervă pe WhatsApp" | `_blank` | `noopener` | casetă CTA la finalul articolului |
| [articol.html:231](articol.html#L231) | 231 | mai multe informații | „Salut! Scrie-mi pe WhatsApp" / aria-label | `_blank` | `noopener` | widget flotant |

### 1.1 Variante distincte de mesaj prefill (5)

| # | `text=` (decodat) | Ocurențe | Unde |
|---|---|---|---|
| 1 | `Bună ziua! Aș dori mai multe informații.` | 8 | widgetul flotant, pe toate paginile |
| 2 | `Bună ziua! Aș dori să rezerv o dată pentru evenimentul meu.` | 21 | header, meniu mobil, hero, CTA-uri de secțiune |
| 3 | `Bună ziua! Aș dori o ofertă pentru evenimentul meu.` | 1 | [index.html:330](index.html#L330) |
| 4 | `Bună ziua, mă interesează pachetul Standard Nuntă` | 1 | [oferte.html:179](oferte.html#L179) |
| 5 | `Bună ziua, mă interesează pachetul Premium Nuntă` | 1 | [oferte.html:196](oferte.html#L196) |

Variantele 4 și 5 folosesc virgulă în loc de semnul exclamării și nu au punct
final; variantele 1–3 au `!` și punct final.

---

## 2. Telefon — `tel:+40722911485`

Toate cele 18 linkuri folosesc exact `tel:+40722911485`. Niciunul nu are
`target` sau `rel` (corect pentru protocol de contact).

| fișier | linia | href | text ancoră / aria-label | context |
|---|---|---|---|---|
| [index.html:78](index.html#L78) | 78 | `tel:+40722911485` | *fără text vizibil* — icon SVG + `aria-label="Sună acum"` | header, buton telefon vizibil doar sub `lg` |
| [index.html:342](index.html#L342) | 342 | `tel:+40722911485` | „+40 722 911 485" | secțiune „Booking CTA" |
| [index.html:495](index.html#L495) | 495 | `tel:+40722911485` | „+40 722 911 485" | footer, coloană contact |
| [galerie.html:69](galerie.html#L69) | 69 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [galerie.html:281](galerie.html#L281) | 281 | idem | „+40 722 911 485" | footer |
| [discografie.html:85](discografie.html#L85) | 85 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [discografie.html:331](discografie.html#L331) | 331 | idem | „+40 722 911 485" | footer |
| [servicii.html:70](servicii.html#L70) | 70 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [servicii.html:310](servicii.html#L310) | 310 | idem | „+40 722 911 485" | footer |
| [oferte.html:89](oferte.html#L89) | 89 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [oferte.html:350](oferte.html#L350) | 350 | idem | „+40 722 911 485" | footer |
| [contact.html:72](contact.html#L72) | 72 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [contact.html:139](contact.html#L139) | 139 | idem | „Telefon Rezervări / +40 722 911 485" | bloc `<address>`, secțiune contact |
| [contact.html:276](contact.html#L276) | 276 | idem | „+40 722 911 485" | footer |
| [blog.html:74](blog.html#L74) | 74 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [blog.html:271](blog.html#L271) | 271 | idem | „+40 722 911 485" | footer |
| [articol.html:68](articol.html#L68) | 68 | idem | icon-only + `aria-label="Sună acum"` | header mobil |
| [articol.html:210](articol.html#L210) | 210 | idem | „+40 722 911 485" | footer |

**Mențiuni text ale numărului (nu în `href`):** formatul afișat este
întotdeauna `+40 722 911 485` (cu spații), în 10 locuri —
[index.html:346](index.html#L346), [index.html:495](index.html#L495),
[galerie.html:281](galerie.html#L281), [discografie.html:331](discografie.html#L331),
[servicii.html:310](servicii.html#L310), [oferte.html:350](oferte.html#L350),
[contact.html:145](contact.html#L145), [contact.html:276](contact.html#L276),
[blog.html:271](blog.html#L271), [articol.html:210](articol.html#L210).
Numărul **nu** apare în niciun `meta description`, `og:description`, `alt`
sau `title`.

Un singur alt loc conține numărul: JSON-LD, [contact.html:42](contact.html#L42) —
`"telephone": "+40722911485"`.

---

## 3. Email — `mailto:`

| fișier | linia | href | text ancoră | target | rel | context |
|---|---|---|---|---|---|---|
| [index.html:494](index.html#L494) | 494 | `mailto:contact@ioanabalan.ro` | „contact@ioanabalan.ro" | — | — | footer, coloană contact |
| [galerie.html:280](galerie.html#L280) | 280 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [discografie.html:330](discografie.html#L330) | 330 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [servicii.html:309](servicii.html#L309) | 309 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [oferte.html:349](oferte.html#L349) | 349 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [contact.html:130](contact.html#L130) | 130 | idem | „Email Oficial / contact@ioanabalan.ro" (text la [:136](contact.html#L136)) | — | — | bloc `<address>`, secțiune contact |
| [contact.html:275](contact.html#L275) | 275 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [blog.html:270](blog.html#L270) | 270 | idem | „contact@ioanabalan.ro" | — | — | footer |
| [articol.html:209](articol.html#L209) | 209 | idem | „contact@ioanabalan.ro" | — | — | footer |

**Mențiuni text ale unui email, în afara `mailto:`:**

| fișier | linia | valoare | context |
|---|---|---|---|
| [contact.html:43](contact.html#L43) | 43 | `contact@ioana-balan.ro` | JSON-LD, `"email"` — **singura apariție a variantei cu cratimă** |
| [contact.html:136](contact.html#L136) | 136 | `contact@ioanabalan.ro` | text vizibil al linkului de la :130 |
| [contact.html:196](contact.html#L196) | 196 | `email@exemplu.ro` | `placeholder` pe `<input type="email">` din formular |
| [blog.html:194](blog.html#L194) | 194 | *(fără adresă)* `placeholder="Email-ul tău"` | input newsletter |

Emailul nu apare în niciun `meta`, `alt`, `title` sau `aria-label`.

---

## 4. Linkuri sociale

### 4.1 Bloc social din footer — identic pe toate cele 8 pagini

Aceleași 4 linkuri, în aceeași ordine (Facebook → Instagram → YouTube →
TikTok), cu aceeași clasă și același text ancoră. **Toate au
`target="_blank"` și niciunul nu are `rel`.** Text-only, fără iconuri.

| fișier | linii | href-uri | text ancoră | target | rel | context |
|---|---|---|---|---|---|---|
| [index.html:473-476](index.html#L473-L476) | 473 / 474 / 475 / 476 | `https://facebook.com/ioanabalan` / `https://instagram.com/iamioanabalan` / `https://youtube.com/@BalanIoana` / `https://tiktok.com/@ioanabalanmusic` | Facebook / Instagram / YouTube / TikTok | `_blank` | **lipsă** | footer, coloană „Social" |
| [galerie.html:259-262](galerie.html#L259-L262) | 259–262 | idem | idem | `_blank` | **lipsă** | footer |
| [discografie.html:309-312](discografie.html#L309-L312) | 309–312 | idem | idem | `_blank` | **lipsă** | footer |
| [servicii.html:288-291](servicii.html#L288-L291) | 288–291 | idem | idem | `_blank` | **lipsă** | footer |
| [oferte.html:328-331](oferte.html#L328-L331) | 328–331 | idem | idem | `_blank` | **lipsă** | footer |
| [contact.html:254-257](contact.html#L254-L257) | 254–257 | idem | idem | `_blank` | **lipsă** | footer |
| [blog.html:249-252](blog.html#L249-L252) | 249–252 | idem | idem | `_blank` | **lipsă** | footer |
| [articol.html:188-191](articol.html#L188-L191) | 188–191 | idem | idem | `_blank` | **lipsă** | footer |

### 4.2 Linkuri YouTube în conținut

| fișier | linia | href | text ancoră | target | rel | context |
|---|---|---|---|---|---|---|
| [galerie.html:180](galerie.html#L180) | 180 | `https://youtube.com/@BalanIoana` | „Vezi canalul YouTube" | `_blank` | `noopener` | secțiune video |
| [discografie.html:132](discografie.html#L132) | 132 | `https://youtube.com/@BalanIoana/videos` | „Vezi pe YouTube" | `_blank` | `noopener` | hero discografie |
| [discografie.html:147](discografie.html#L147) | 147 | `https://youtu.be/hPACrfwibFw` | „01 · Hai să nu ne mai mințim · 04:15" | `_blank` | `noopener` | tracklist album |
| [discografie.html:156](discografie.html#L156) | 156 | `https://youtube.com/@BalanIoana` | „02 · Bărbățelul meu · 04:22" | `_blank` | `noopener` | tracklist |
| [discografie.html:165](discografie.html#L165) | 165 | `https://youtube.com/@BalanIoana` | „03 · Fratele rămâne frate · 04:12" | `_blank` | `noopener` | tracklist |
| [discografie.html:174](discografie.html#L174) | 174 | `https://youtube.com/@BalanIoana` | „04 · Ține minte omule · 03:28" | `_blank` | `noopener` | tracklist |
| [discografie.html:183](discografie.html#L183) | 183 | `https://youtube.com/@BalanIoana` | „05 · Varsă țara lacrimi grele · 03:45" | `_blank` | `noopener` | tracklist |
| [discografie.html:192](discografie.html#L192) | 192 | `https://youtube.com/@BalanIoana` | „06 · Dragoste mare · 04:58" | `_blank` | `noopener` | tracklist |
| [discografie.html:201](discografie.html#L201) | 201 | `https://youtube.com/@BalanIoana` | „07 · Hai murgule-n vale · 03:50" | `_blank` | `noopener` | tracklist |
| [discografie.html:210](discografie.html#L210) | 210 | `https://youtube.com/@BalanIoana` | „08 · Să merg la părinți acasă · 04:05" | `_blank` | `noopener` | tracklist |
| [discografie.html:241](discografie.html#L241) | 241 | `https://youtube.com/@BalanIoana` | „Vezi Colecția" | `_blank` | `noopener` | card album |
| [discografie.html:256](discografie.html#L256) | 256 | `https://youtube.com/@BalanIoana` | „Vezi Colecția" | `_blank` | `noopener` | card album |

**Referințe YouTube în JavaScript** ([index.html](index.html)):

| linia | valoare | context |
|---|---|---|
| [index.html:251](index.html#L251) | `data-yt="hPACrfwibFw"` | atributul de pe butonul video-facade din hero |
| [index.html:574](index.html#L574) | `window.open('https://youtube.com/@BalanIoana', '_blank', 'noopener')` | fallback când `data-yt` lipsește sau e `'TODO'` |
| [index.html:578](index.html#L578) | `frame.src = 'https://www.youtube.com/embed/' + id + '?autoplay=1&rel=0'` | iframe construit la click; `frame.title` = `data-title` sau „Clip video Ioana Balan" ([:579](index.html#L579)) |

`hPACrfwibFw` este singurul ID video concret din proiect și apare de două ori:
`data-yt` în [index.html:251](index.html#L251) și `youtu.be/hPACrfwibFw` în
[discografie.html:147](discografie.html#L147).

---

## 5. Alte linkuri externe

### 5.1 Google Maps / recenzii (16)

Toate folosesc URL identic:
`https://www.google.com/maps/place/?q=place_id:ChIJGxv0gfr-sUARlkjS2WERmRs`,
cu `target="_blank"` și `rel="noopener noreferrer"`.

| fișier | linia | text ancoră | context |
|---|---|---|---|
| [index.html:130](index.html#L130) | 130 | „5,0 · 61 de recenzii Google · Grand Music Events" | hero |
| [index.html:191](index.html#L191) | 191 | „5,0 · 61 de recenzii Google · Grand Music Events" | secțiune |
| [index.html:230](index.html#L230) | 230 | **„5,0 · 61 de recenzii Google"** (fără „Grand Music Events") | secțiune |
| [index.html:283](index.html#L283) | 283 | „5,0 · 61 de recenzii Google · Grand Music Events" | antet secțiune „Recomandări" |
| [index.html:453](index.html#L453) | 453 | „5,0 · 61 de recenzii Google · Grand Music Events" | footer, coloană brand |
| [galerie.html:206](galerie.html#L206) | 206 | idem (variantă lungă) | secțiune CTA |
| [galerie.html:239](galerie.html#L239) | 239 | idem | footer |
| [discografie.html:289](discografie.html#L289) | 289 | idem | footer |
| [servicii.html:245](servicii.html#L245) | 245 | idem | secțiune CTA |
| [servicii.html:268](servicii.html#L268) | 268 | idem | footer |
| [oferte.html:153](oferte.html#L153) | 153 | idem | secțiune pachete |
| [oferte.html:308](oferte.html#L308) | 308 | idem | footer |
| [contact.html:204](contact.html#L204) | 204 | idem | secțiune |
| [contact.html:234](contact.html#L234) | 234 | idem | footer |
| [blog.html:229](blog.html#L229) | 229 | idem | footer |
| [articol.html:168](articol.html#L168) | 168 | idem | footer |

### 5.2 ANPC / SAL (16 — 2 per pagină, în footer)

| href | text ancoră | aria-label | target | rel | linii |
|---|---|---|---|---|---|
| `https://anpc.ro` | „ANPC" | — | `_blank` | `noopener noreferrer` | [index:486](index.html#L486), [galerie:272](galerie.html#L272), [discografie:322](discografie.html#L322), [servicii:301](servicii.html#L301), [oferte:341](oferte.html#L341), [contact:267](contact.html#L267), [blog:262](blog.html#L262), [articol:201](articol.html#L201) |
| `https://anpc.ro/ce-este-sal/` | „SAL" | „SAL — Soluționarea alternativă a litigiilor" | `_blank` | `noopener noreferrer` | [index:490](index.html#L490), [galerie:276](galerie.html#L276), [discografie:326](discografie.html#L326), [servicii:305](servicii.html#L305), [oferte:345](oferte.html#L345), [contact:271](contact.html#L271), [blog:266](blog.html#L266), [articol:205](articol.html#L205) |

### 5.3 Resurse third-party (CDN / fonturi) — identice pe toate cele 8 pagini

- `https://cdn.tailwindcss.com?plugins=forms,container-queries` (`<script src>`)
- `https://fonts.googleapis.com` + `https://fonts.gstatic.com` (`rel="preconnect"`)
- `https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap`
- `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap`

---

## 6. JSON-LD

Fiecare pagină are exact un bloc `application/ld+json`.

| fișier | `@type` | `url` / `@id` | `sameAs` | `email` | `telephone` |
|---|---|---|---|---|---|
| [index.html:27-45](index.html#L27-L45) | `MusicGroup` | `@id`: `https://ioana-balan.ro/#artist` ([:31](index.html#L31))<br>`url`: `https://ioana-balan.ro/` ([:33](index.html#L33)) | **da**, 4 ([:38-43](index.html#L38-L43)) | — | — |
| [galerie.html](galerie.html#L31) | `ImageGallery` | `url`: `https://ioana-balan.ro/galerie.html` ([:31](galerie.html#L31)) | — | — | — |
| [discografie.html](discografie.html#L27) | `ItemList` de 3 × `MusicAlbum` | — | — | — | — |
| [servicii.html](servicii.html#L31) | `Service` | `url`: `https://ioana-balan.ro/servicii.html` ([:31](servicii.html#L31)) | — | — | — |
| [oferte.html](oferte.html#L27) | `Product` + `Offer` | — | — | — | — |
| [contact.html:30-48](contact.html#L30-L48) | `EntertainmentBusiness` | `@id`: `https://ioana-balan.ro/#artist` ([:34](contact.html#L34))<br>`url`: `https://ioana-balan.ro` ([:44](contact.html#L44), **fără slash final**) | — | `contact@ioana-balan.ro` ([:43](contact.html#L43)) | `+40722911485` ([:42](contact.html#L42)) |
| [blog.html](blog.html#L32) | `Blog` + `BreadcrumbList` | `@id` / `url`: `https://ioana-balan.ro/blog.html` ([:32](blog.html#L32), [:34](blog.html#L34))<br>`item`: `https://ioana-balan.ro/` ([:41](blog.html#L41)), `https://ioana-balan.ro/blog.html` ([:42](blog.html#L42)) | — | — | — |
| [articol.html](articol.html#L39) | `BlogPosting` | `mainEntityOfPage.@id`: `https://ioana-balan.ro/articol.html` ([:39](articol.html#L39)) | — | — | — |

**Constatări:**

- `sameAs` există **doar** în [index.html:38-43](index.html#L38-L43). Cele 4
  URL-uri de acolo sunt identice cu cele din footer (aceleași handle-uri,
  aceeași ordine).
- `email` și `telephone` există **doar** în JSON-LD-ul din
  [contact.html](contact.html#L42-L43).
- Cele două entități care partajează `@id` = `https://ioana-balan.ro/#artist`
  au `@type` diferit: `MusicGroup` ([index.html:30](index.html#L30)) vs.
  `EntertainmentBusiness` ([contact.html:33](contact.html#L33)).
- `discografie.html` și `oferte.html` nu declară niciun `url` în JSON-LD.

---

## 7. Meta tags

`twitter:site` și `twitter:creator` **nu există în niciun fișier.**
`twitter:card` = `summary_large_image` pe toate cele 8 pagini.
`og:site_name` = `Ioana Balan` pe toate cele 8 pagini.
`canonical` și `og:url` coincid pe fiecare pagină.

| fișier | canonical | og:url | og:site_name | twitter:card |
|---|---|---|---|---|
| index.html | [:7](index.html#L7) `https://ioana-balan.ro/` | [:11](index.html#L11) `https://ioana-balan.ro/` | [:9](index.html#L9) | [:19](index.html#L19) |
| galerie.html | [:7](galerie.html#L7) `…/galerie.html` | [:11](galerie.html#L11) | [:9](galerie.html#L9) | [:19](galerie.html#L19) |
| discografie.html | [:6](discografie.html#L6) `…/discografie.html` | [:10](discografie.html#L10) | [:8](discografie.html#L8) | [:18](discografie.html#L18) |
| servicii.html | [:7](servicii.html#L7) `…/servicii.html` | [:11](servicii.html#L11) | [:9](servicii.html#L9) | [:19](servicii.html#L19) |
| oferte.html | [:6](oferte.html#L6) `…/oferte.html` | [:10](oferte.html#L10) | [:8](oferte.html#L8) | [:18](oferte.html#L18) |
| contact.html | [:6](contact.html#L6) `…/contact.html` | [:10](contact.html#L10) | [:8](contact.html#L8) | [:18](contact.html#L18) |
| blog.html | [:7](blog.html#L7) `…/blog.html` | [:11](blog.html#L11) | [:9](blog.html#L9) | [:19](blog.html#L19) |
| articol.html | [:9](articol.html#L9) `…/articol.html` | [:13](articol.html#L13) | [:11](articol.html#L11) | [:21](articol.html#L21) |

Diferență de formă (nu de valoare): în `articol.html` atributele sunt scrise
în ordine inversă (`content` înaintea `property`/`name`) față de celelalte 7
pagini — ex. [articol.html:11](articol.html#L11)
`<meta content="Ioana Balan" property="og:site_name">` vs.
[index.html:9](index.html#L9) `<meta property="og:site_name" content="Ioana Balan">`.
Idem pentru `<link rel="canonical">` ([articol.html:9](articol.html#L9) are
`href` înaintea `rel`).

---

# A. INCONSISTENȚE ÎNTRE PAGINI

### A.1 Linkuri sociale — set identic pe toate cele 8 pagini

Toate cele 8 pagini au **exact același bloc social în footer**: 4 linkuri,
aceeași ordine (Facebook, Instagram, YouTube, TikTok), aceleași URL-uri,
același text ancoră, aceeași clasă, `target="_blank"` fără `rel`, fără iconuri.

- **Nicio pagină nu are linkuri sociale lipsă.**
- **Nicio diferență de ordine, de icon sau de text ancoră între pagini.**
- **Nicio pagină nu are un link social în afara footerului**, cu excepția
  linkurilor YouTube de conținut din [galerie.html:180](galerie.html#L180) și
  [discografie.html](discografie.html#L132) (12 linkuri) — vezi §4.2.

Asimetria reală: **YouTube apare de 14 ori în conținut** (galerie + discografie),
în timp ce Facebook, Instagram și TikTok apar **exclusiv în footer**, câte o
dată per pagină.

### A.2 `sameAs` există doar pe o pagină

[index.html:38-43](index.html#L38-L43) este singurul JSON-LD cu `sameAs`.
Celelalte 7 pagini nu declară niciun profil social în date structurate,
deși toate le afișează în footer.

### A.3 Poziția widgetului flotant WhatsApp diferă în DOM

Elementul `.whatsapp-float` este identic ca markup pe toate cele 8 pagini,
dar plasat în locuri structural diferite:

| pagină | linia | poziție în DOM |
|---|---|---|
| [index.html:53](index.html#L53) | 53 | imediat după skip-link, **înainte de `<header>`** |
| [galerie.html:44](galerie.html#L44) | 44 | idem |
| [discografie.html:60](discografie.html#L60) | 60 | idem |
| [servicii.html:45](servicii.html#L45) | 45 | idem |
| [oferte.html:64](oferte.html#L64) | 64 | idem |
| [contact.html:103](contact.html#L103) | 103 | **după închiderea meniului mobil**, în interiorul `<header>` |
| [blog.html:213](blog.html#L213) | 213 | **după `</main>`** |
| [articol.html:231](articol.html#L231) | 231 | **după `</footer>`** |

Consecință directă: ordinea de tabulare a widgetului diferă între pagini —
primul element focusabil pe 5 pagini, ultimul pe `articol.html`.

### A.4 Numărul de puncte de conversie WhatsApp per pagină

| pagină | wa.me | din care în corpul paginii (fără header / meniu mobil / widget) |
|---|---|---|
| index.html | 5 | 2 (hero [:126](index.html#L126), Recomandări [:330](index.html#L330)) |
| oferte.html | 5 | 2 (carduri pachete [:179](oferte.html#L179), [:196](oferte.html#L196)) |
| galerie.html | 4 | 1 ([:202](galerie.html#L202)) |
| discografie.html | 4 | 1 ([:272](discografie.html#L272)) |
| servicii.html | 4 | 1 ([:241](servicii.html#L241)) |
| articol.html | 4 | 1 ([:153](articol.html#L153)) |
| **contact.html** | **3** | **0** |
| **blog.html** | **3** | **0** |

`contact.html` și `blog.html` sunt singurele pagini fără niciun CTA WhatsApp
în conținut — pe `contact.html`, blocul `<address>`
([:130](contact.html#L130), [:139](contact.html#L139)) oferă doar email și
telefon, nu WhatsApp.

### A.5 Vocabular de CTA divergent

31 din 32 de linkuri WhatsApp de acțiune poartă textul „Rezervă pe WhatsApp"
(sau „Salut! Scrie-mi pe WhatsApp" pentru widget). Excepție:
[index.html:330](index.html#L330) — **„Rezervă data ta"**, cu un mesaj
prefill diferit („Aș dori o ofertă…" în loc de „Aș dori să rezerv o dată…").

### A.6 Text ancoră divergent pe linkul de recenzii Google

15 din 16 linkuri Google folosesc „5,0 · 61 de recenzii Google · Grand Music
Events". Excepție: [index.html:230](index.html#L230) — „5,0 · 61 de recenzii
Google", fără segmentul „Grand Music Events".

### A.7 Ordinea atributelor în `<head>` diferă pe `articol.html`

Vezi §7. Nu afectează randarea; e o diferență de generare a fișierului.

---

# B. VARIANTE DE DOMENIU ȘI EMAIL

## B.1 Domeniu

| Variantă | Ocurențe | Fișiere |
|---|---|---|
| `https://ioana-balan.ro` (+ path) | **45** | toate cele 8 pagini — `canonical`, `og:url`, `og:image`, `twitter:image`, JSON-LD |
| `ioanabalan.ro` (**fără cratimă**) | **18** | doar ca parte a adresei de email `contact@ioanabalan.ro` — vezi B.2 |

**Constatări:**

- Nu există nicio apariție cu `www.` pentru domeniul propriu.
- Nu există nicio apariție cu `http://` (toate sunt `https://`).
- Domeniul canonic este consecvent `ioana-balan.ro` peste tot unde apare ca URL.
- **Singura inconsecvență de formă:** trailing slash. JSON-LD-ul din
  [contact.html:44](contact.html#L44) declară `"url": "https://ioana-balan.ro"`
  (fără `/` final), în timp ce [index.html:33](index.html#L33) declară
  `"url": "https://ioana-balan.ro/"` și [blog.html:41](blog.html#L41)
  `"item": "https://ioana-balan.ro/"`. Ambele entități partajează același
  `@id` (`https://ioana-balan.ro/#artist`).

## B.2 Email

| Variantă | Ocurențe | Fișiere / linii |
|---|---|---|
| `contact@ioanabalan.ro` (**fără cratimă**) | **18** (9 `mailto:` + 9 ca text ancoră/vizibil) | [index:494](index.html#L494), [galerie:280](galerie.html#L280), [discografie:330](discografie.html#L330), [servicii:309](servicii.html#L309), [oferte:349](oferte.html#L349), [contact:130](contact.html#L130) + [:136](contact.html#L136), [contact:275](contact.html#L275), [blog:270](blog.html#L270), [articol:209](articol.html#L209) |
| `contact@ioana-balan.ro` (**cu cratimă**) | **1** | [contact.html:43](contact.html#L43) — JSON-LD `"email"` |
| `email@exemplu.ro` | 1 | [contact.html:196](contact.html#L196) — `placeholder` de formular |

**Constatare:** pe `contact.html`, datele structurate declară
`contact@ioana-balan.ro`, iar linkul vizibil de pe aceeași pagină
([:130](contact.html#L130) / [:136](contact.html#L136)) trimite la
`contact@ioanabalan.ro`. Cele două adrese sunt pe domenii diferite.
`ioanabalan.ro` (fără cratimă) nu apare nicăieri ca URL de site.

## B.3 Domenii externe (handle-uri sociale)

| Domeniu | Formă folosită | Ocurențe |
|---|---|---|
| `facebook.com` | `https://facebook.com/ioanabalan` (fără `www.`) | 9 (8 footer + 1 `sameAs`) |
| `instagram.com` | `https://instagram.com/iamioanabalan` (fără `www.`) | 9 |
| `tiktok.com` | `https://tiktok.com/@ioanabalanmusic` (fără `www.`) | 9 |
| `youtube.com` | `https://youtube.com/@BalanIoana` (**fără** `www.`) | 22 |
| `youtube.com` | `https://youtube.com/@BalanIoana/videos` | 1 ([discografie:132](discografie.html#L132)) |
| `youtu.be` | `https://youtu.be/hPACrfwibFw` | 1 ([discografie:147](discografie.html#L147)) |
| `www.youtube.com` | `https://www.youtube.com/embed/...` | 1 ([index.html:578](index.html#L578), în JS) |
| `www.google.com` | `https://www.google.com/maps/place/?q=place_id:…` (**cu** `www.`) | 16 |
| `anpc.ro` | `https://anpc.ro`, `https://anpc.ro/ce-este-sal/` (fără `www.`) | 16 |

Singura inconsecvență `www.` în linkurile YouTube este între markup (fără
`www.`) și JS-ul care construiește embed-ul ([index.html:578](index.html#L578),
cu `www.`) — dar sunt URL-uri cu scop diferit (canal vs. embed).

---

# C. IGIENĂ TEHNICĂ A LINKURILOR EXTERNE

## C.1 Sumar

| Grup de linkuri | Nr. | `target="_blank"` | `rel` | Nume accesibil |
|---|---|---|---|---|
| Social footer (Facebook/Instagram/YouTube/TikTok) | 32 | ✅ toate | ❌ **niciunul** | ✅ text vizibil |
| WhatsApp (widget flotant) | 8 | ✅ | ✅ `noopener` | ✅ `aria-label` + text ascuns sub `sm` |
| WhatsApp (restul) | 24 | ✅ | ✅ `noopener` | ✅ text vizibil |
| YouTube în conținut | 12 | ✅ | ✅ `noopener` | ✅ text vizibil |
| Google Maps / recenzii | 16 | ✅ | ✅ `noopener noreferrer` | ✅ text vizibil |
| ANPC | 8 | ✅ | ✅ `noopener noreferrer` | ✅ text vizibil |
| SAL | 8 | ✅ | ✅ `noopener noreferrer` | ✅ text + `aria-label` |
| `tel:` | 18 | — (corect) | — (corect) | ✅ (vezi C.3) |
| `mailto:` | 9 | — (corect) | — (corect) | ✅ text vizibil |

## C.2 Lipsuri identificate

**C.2.1 — 32 de linkuri sociale cu `target="_blank"` și fără `rel`.**
Singurul grup de linkuri externe din proiect care nu declară `rel`. Restul
linkurilor externe (WhatsApp, YouTube, Google, ANPC) au `noopener`.

| fișier | linii |
|---|---|
| [index.html](index.html#L473-L476) | 473, 474, 475, 476 |
| [galerie.html](galerie.html#L259-L262) | 259, 260, 261, 262 |
| [discografie.html](discografie.html#L309-L312) | 309, 310, 311, 312 |
| [servicii.html](servicii.html#L288-L291) | 288, 289, 290, 291 |
| [oferte.html](oferte.html#L328-L331) | 328, 329, 330, 331 |
| [contact.html](contact.html#L254-L257) | 254, 255, 256, 257 |
| [blog.html](blog.html#L249-L252) | 249, 250, 251, 252 |
| [articol.html](articol.html#L188-L191) | 188, 189, 190, 191 |

**C.2.2 — Inconsecvență `noopener` vs. `noopener noreferrer`.**
WhatsApp și YouTube folosesc doar `noopener`; Google Maps, ANPC și SAL
folosesc `noopener noreferrer`. Ambele forme sunt valide; diferența e
neuniformă între grupuri.

**C.2.3 — 12 linkuri cu text ancoră care nu descrie destinația.**
În tracklistul din [discografie.html](discografie.html#L147-L210), fiecare
piesă este un link către YouTube, dar textul ancoră este titlul piesei +
durata („02 · Bărbățelul meu · 04:22"), fără indicație că linkul deschide
o filă nouă către un site extern. Linia [:147](discografie.html#L147) duce
la un clip concret; liniile
[:156](discografie.html#L156), [:165](discografie.html#L165),
[:174](discografie.html#L174), [:183](discografie.html#L183),
[:192](discografie.html#L192), [:201](discografie.html#L201),
[:210](discografie.html#L210) duc toate la pagina canalului — vezi §D.2.

**C.2.4 — Două linkuri cu text ancoră identic și destinație identică pe
aceeași pagină:** „Vezi Colecția" la
[discografie.html:241](discografie.html#L241) și
[discografie.html:256](discografie.html#L256), ambele către
`https://youtube.com/@BalanIoana`, dar în carduri de albume diferite.

**C.2.5 — Niciun link extern nu semnalează deschiderea într-o filă nouă**
(nici prin text, nici prin `aria-label`, nici prin icon cu `alt`). Toate
SVG-urile din interiorul linkurilor au `aria-hidden="true"`.

## C.3 Linkuri icon-only

Există **8** linkuri fără text vizibil (doar SVG). **Toate au `aria-label`,
deci niciunul nu rămâne fără nume accesibil.**

| fișier | linia | href | `aria-label` |
|---|---|---|---|
| [index.html:78](index.html#L78) | 78 | `tel:+40722911485` | „Sună acum" |
| [galerie.html:69](galerie.html#L69) | 69 | `tel:+40722911485` | „Sună acum" |
| [discografie.html:85](discografie.html#L85) | 85 | `tel:+40722911485` | „Sună acum" |
| [servicii.html:70](servicii.html#L70) | 70 | `tel:+40722911485` | „Sună acum" |
| [oferte.html:89](oferte.html#L89) | 89 | `tel:+40722911485` | „Sună acum" |
| [contact.html:72](contact.html#L72) | 72 | `tel:+40722911485` | „Sună acum" |
| [blog.html:74](blog.html#L74) | 74 | `tel:+40722911485` | „Sună acum" |
| [articol.html:68](articol.html#L68) | 68 | `tel:+40722911485` | „Sună acum" |

Widgetul flotant WhatsApp (8 ocurențe) are text vizibil doar de la breakpoint
`sm` în sus (`hidden sm:inline`), dar are `aria-label="Contact Ioana Balan pe
WhatsApp"`, deci are nume accesibil și sub `sm`.

---

# D. LINKURI MOARTE SAU PLACEHOLDER

## D.1 Placeholder-uri clasice — niciunul

Căutare pentru `href="#"`, `href=""`, `href="javascript:void(0)"`,
`example.com`, `lorem`: **0 rezultate reale** în cele 8 pagini.

Singurele apariții textuale ale șirului `href="#"` sunt **în interiorul unor
comentarii HTML**, nu în markup activ — de ex.
[index.html:482](index.html#L482). Paginile legale sunt marcate ca `<span>`,
nu ca `<a>`:

| fișier | linii | element | text |
|---|---|---|---|
| [index.html:484-485](index.html#L484-L485) | 484, 485 | `<span>` (fără `href`) | „Termeni și Condiții", „Politică de Confidențialitate" |
| [galerie.html:270-271](galerie.html#L270-L271) | 270, 271 | idem | idem |
| [discografie.html:320-321](discografie.html#L320-L321) | 320, 321 | idem | idem |
| [servicii.html:299-300](servicii.html#L299-L300) | 299, 300 | idem | idem |
| [oferte.html:339-340](oferte.html#L339-L340) | 339, 340 | idem | idem |
| [contact.html:265-266](contact.html#L265-L266) | 265, 266 | idem | idem |
| [blog.html:260-261](blog.html#L260-L261) | 260, 261 | idem | idem |
| [articol.html:199-200](articol.html#L199-L200) | 199, 200 | idem | idem |

Singurele `href="#..."` sunt ancore interne funcționale:
`href="#continut"` (skip-link) — [index:51](index.html#L51),
[galerie:42](galerie.html#L42), [discografie:58](discografie.html#L58),
[servicii:43](servicii.html#L43), [oferte:62](oferte.html#L62),
[contact:52](contact.html#L52), [blog:54](blog.html#L54),
[articol:48](articol.html#L48).

## D.2 Linkuri sociale către pagină generică în loc de profil concret

Toate cele 4 handle-uri sociale sunt **profile concrete**, nu pagini generice
de platformă:

- `facebook.com/ioanabalan` — profil
- `instagram.com/iamioanabalan` — profil
- `youtube.com/@BalanIoana` — canal
- `tiktok.com/@ioanabalanmusic` — profil

**Însă 9 din cele 12 linkuri YouTube de conținut duc la canalul generic în
locul resursei specifice pe care textul ancoră o promite:**

| fișier | linia | text ancoră promite | href duce la |
|---|---|---|---|
| [discografie.html:156](discografie.html#L156) | 156 | piesa „Bărbățelul meu" | canalul `@BalanIoana` |
| [discografie.html:165](discografie.html#L165) | 165 | piesa „Fratele rămâne frate" | canalul |
| [discografie.html:174](discografie.html#L174) | 174 | piesa „Ține minte omule" | canalul |
| [discografie.html:183](discografie.html#L183) | 183 | piesa „Varsă țara lacrimi grele" | canalul |
| [discografie.html:192](discografie.html#L192) | 192 | piesa „Dragoste mare" | canalul |
| [discografie.html:201](discografie.html#L201) | 201 | piesa „Hai murgule-n vale" | canalul |
| [discografie.html:210](discografie.html#L210) | 210 | piesa „Să merg la părinți acasă" | canalul |
| [discografie.html:241](discografie.html#L241) | 241 | „Vezi Colecția" (album) | canalul |
| [discografie.html:256](discografie.html#L256) | 256 | „Vezi Colecția" (alt album) | canalul |

Singurul link YouTube către o resursă specifică este
[discografie.html:147](discografie.html#L147) → `https://youtu.be/hPACrfwibFw`
(piesa 01).

## D.3 Fallback declarat explicit în JS

[index.html:573-575](index.html#L573-L575): dacă `data-yt` lipsește sau are
valoarea literală `'TODO'`, butonul video deschide canalul generic YouTube în
loc să încarce un iframe. Valoarea `'TODO'` nu apare însă în niciun atribut
`data-yt` din proiect — singurul `data-yt` existent este
[index.html:251](index.html#L251) = `hPACrfwibFw`.

## D.4 Formulare fără destinație

Nu sunt linkuri, dar sunt puncte de contact non-funcționale:

| fișier | linia | element | observație |
|---|---|---|---|
| [contact.html:196](contact.html#L196) | 196 | `<input type="email" placeholder="email@exemplu.ro">` | formularul de contact nu are `action` |
| [blog.html:194](blog.html#L194) | 194 | `<input type="email" placeholder="Email-ul tău" required>` | formularul de newsletter nu are `action` |

---

# Anexa 1 — `_stitch-export/` (în afara scope-ului, relevant pentru B.2)

Fragmentele WordPress primite de la client conțin **alte** handle-uri sociale
și **altă** adresă de email decât prototipul. Ortografia numelui diferă:
`ioanablan` / `ioanablanmusic` / `iamioanablan` (fără al doilea „a") față de
`ioanabalan` / `ioanabalanmusic` / `iamioanabalan` în prototip.

| fișier | linia | valoare în `_stitch-export/` | echivalent în prototip |
|---|---|---|---|
| [wordpress-header-footer.html:101](_stitch-export/wordpress-header-footer.html#L101) | 101 | `ioanablanoficial@gmail.com` (text, fără `mailto:`) | `contact@ioanabalan.ro` |
| [wordpress-header-footer.html:110](_stitch-export/wordpress-header-footer.html#L110) | 110 | `https://facebook.com/ioanablan` | `https://facebook.com/ioanabalan` |
| [wordpress-header-footer.html:111](_stitch-export/wordpress-header-footer.html#L111) | 111 | `https://tiktok.com/@ioanablanmusic` | `https://tiktok.com/@ioanabalanmusic` |
| [wordpress-header-footer.html:112](_stitch-export/wordpress-header-footer.html#L112) | 112 | `https://instagram.com/iamioanablan` | `https://instagram.com/iamioanabalan` |
| [wordpress-header-footer.html:113](_stitch-export/wordpress-header-footer.html#L113) | 113 | `https://www.youtube.com/@BalanIoana` (**cu** `www.`) | `https://youtube.com/@BalanIoana` |

Ordinea socialelor în export este **Facebook → TikTok → Instagram → YouTube**,
față de **Facebook → Instagram → YouTube → TikTok** în prototip.

Exportul nu conține niciun `wa.me`, `tel:` sau `mailto:`.

**Nu se poate stabili static care set de handle-uri este cel corect** —
niciuna dintre variante nu a fost verificată prin cerere HTTP.

---

# Anexa 2 — limitele auditului

- Analiză **exclusiv statică**. Niciun URL nu a fost apelat; nu se știe dacă
  vreunul returnează 404 sau redirecționează.
- `place_id:ChIJGxv0gfr-sUARlkjS2WERmRs` nu a fost validat.
- Handle-urile sociale nu au fost verificate că există.
- ID-ul video `hPACrfwibFw` nu a fost verificat.
- Nu s-au inspectat imaginile (`assets/img/`) pentru text incrustat care ar
  putea conține date de contact.
