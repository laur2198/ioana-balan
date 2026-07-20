# Plan de remediere — ioana-balan.ro (prototip)

> **Pentru Claude Code.** Acest plan se execută în repo-ul `laur2198/ioana-balan` (HTML static + Tailwind CDN).
> Citește mai întâi `CLAUDE.md` din repo — toate constrângerile de acolo rămân valabile:
> - **NU** adăuga build tools, npm, bundlere. Codul rămâne HTML static + Tailwind CDN.
> - Orice layout nou trebuie exprimabil în **containere flexbox** (destinația finală e Elementor). Fără grid complex, overlap-uri sau poziționare absolută elaborată.
> - Quality floor: responsive până la 360px, focus vizibil, `prefers-reduced-motion` respectat, contrast ≥4.5:1.
> - **NU** înlocui imaginile placeholder cu alte imagini inventate — doar cu materiale reale marcate `<!-- TODO client -->`.
> - Sistemul de design (culori, tipografie, ierarhie CTA) e definit în `CLAUDE.md` §5 — nu-l modifica, aplică-l.
>
> **Mod de lucru:** o fază = un commit (sau mai multe commit-uri mici per fază). După fiecare fază, rulează checklist-ul de verificare al fazei. Fazele 0–3 nu depind de client; Faza 4 e blocată de materiale reale.

---

## FAZA 0 — Bug-uri (fără dependențe, ~o zi)

### 0.1 `discografie.html` — parallax-ul mișcă logo-ul din header
`document.querySelector('img')` selectează prima imagine din DOM = logo-ul din nav, care se translatează și scalează la scroll.
**Fix:** șterge complet blocul de parallax la scroll (e efect decorativ, CLAUDE.md descurajează parallax). Alternativ minim: țintește explicit imaginea de copertă (`img[alt^="Copertă Album"]`). Preferă ștergerea.

### 0.2 `contact.html` — starea de succes a formularului folosește culoarea interzisă
La submit, butonul primește `backgroundColor: rgba(200,198,197,0.2)` și `color: #c8c6c5` — argintiul ca fond de buton e **eliminat explicit** în CLAUDE.md §5.
**Fix:** starea „VĂ MULȚUMIM" păstrează fondul bordo (`--accent #800020`) cu text alb, sau folosește contur argintiu + fond transparent (stilul CTA secundar). Nu introduce culori noi.

### 0.3 `servicii.html` — copy expirat + JS dublat
- „Calendarul pentru sezonul **2025** se completează rapid" → „sezonul **2026–2027**".
- Smooth-scroll există și în CSS (`scroll-behavior: smooth` în `styles.css`) și în JS (`scrollIntoView`). Șterge implementarea JS; cea CSS respectă deja `prefers-reduced-motion`.

### 0.4 Widget WhatsApp — 3 implementări divergente
`index/galerie/discografie` au un SVG + label expandabil; `oferte.html` are alt SVG fără label; `servicii.html` are al treilea SVG + tooltip.
**Fix:** alege varianta de pe `index.html` ca **snippet canonic** (marcheaz-o `<!-- WhatsApp Widget (canonic) -->`) și copiaz-o identic în toate cele 8 pagini.

### 0.5 Diacritice inconsecvente
„Hai sa nu ne mai mintim" (discografie: title, h1, tracklist) vs „Hai să nu ne mai mințim" (index, galerie).
**Fix:** cu diacritice peste tot în text vizibil și meta description. Verifică și „Barbatelul meu", „Fratele ramane frate", „Tine minte omule", „Varsa tara lacrimi grele", „Sa merg la parinti acasa" → toate cu diacritice.

### 0.6 An copyright
Verifică toate footer-ele + `blog.html` și `articol.html` (README semnalează `© 2024` și `© 2010-2027`). Canonic: `© 2010-2026 Ioana Balan`.

**Verificare Faza 0:** deschide fiecare pagină, scroll pe discografie (logo static), submit formular contact (buton rămâne în sistemul de culoare), widget WhatsApp identic pe toate paginile, grep pentru `2025`/`mintim`/`2027` fără rezultate false.

---

## FAZA 1 — Vocabular CTA + conținut

### 1.1 Unificarea vocabularului CTA (regulă fără excepții)
Astăzi „Rezervă Acum" duce la `contact.html` în header (5 pagini), la WhatsApp în header pe `contact.html` și la WhatsApp în hero-ul homepage. Regula CLAUDE.md: aceeași acțiune = același nume, mereu.

**Convenție de aplicat peste tot:**
| Etichetă | Acțiune | Stil |
|---|---|---|
| `Rezervă pe WhatsApp` | link `wa.me/40722911485` (+ text precompletat) | CTA primar (bordo) |
| `Cere ofertă` | `contact.html` (formularul) | CTA secundar (contur) sau primar unde e singurul CTA |

De actualizat: header + drawer mobil (toate paginile), hero index, butoanele pachetelor din `oferte.html` („Rezervă Standard/Premium" → „Rezervă pe WhatsApp"; „Solicită Detalii" → „Cere ofertă" cu link spre contact + parametru sau text precompletat), CTA final galerie („Contact" → „Cere ofertă"), link „Solicită Ofertă Personalizată" (mailto) din Booking CTA index → `contact.html`.
**Maxim un CTA primar per secțiune vizibilă** — unde apar două bordo unul lângă altul, al doilea devine secundar.

### 1.2 Eliminarea cifrelor inventate
- `index.html` Stats: șterge cardul „99% Clienți Satisfăcuți". Înlocuiește cu cifra reală: `5,0★ · 61 recenzii Google`.
- „Peste 1000 de evenimente live" și „Discografie premiată național" → marchează `<!-- TODO client: cifră de confirmat -->` și înlocuiește temporar cu fapte verificabile: „Peste 15 ani de scenă", „3 albume proprii (2018, 2021, 2025)".
- „300+ Piese în Repertoriu" → păstrează doar dacă clientul confirmă; altfel TODO.

### 1.3 De-clișeizare copy (CLAUDE.md §7: fără „excelență", „de neuitat", „magie")
Înlocuiri punctuale (păstrează tonul cald și direct):
- index h2 „Peste 15 Ani de Magie pe Scenă: Povestea Ioanei Balan" → „Peste 15 ani pe scenă"
- index eyebrow „Excelență în Evenimente" → „Nuntă · Botez · Corporate"
- servicii „Transformăm momentele speciale în amintiri eterne prin excelență artistică." → o frază concretă: „Program live complet — de la folclor autentic la cover-uri internaționale — cu formația Grand Music Events."
- oferte „Excelență artistică și performanță live impecabilă…" → „Pachete complete: formație live, interpreți, DJ/MC și producție tehnică."
- contact „Doriți o atmosferă de neuitat…" → „Spuneți-ne data și locația — revenim în aceeași zi cu disponibilitate și ofertă."
- galerie etichete generice („Esența Autenticității", „Gala Nunților", „Spectacol Autentic") → `<!-- TODO client: nume eveniment real, ex „Nuntă · București · sept 2025" -->`

### 1.4 Disciplina uppercase
Uppercase + tracking extins rămâne **doar** pe eyebrow-uri și butoane. Se trece la sentence case: label-urile formularului din contact, opțiunile `<select>`, „Consultanță Muzicală Gratuită", titlul „Cere Oferta Personalizată" (devine headline Garamond normal, „Cere ofertă personalizată").

**Verificare Faza 1:** grep `Rezervă Acum` → 0 rezultate; grep `99%|1000 de evenimente|premiată` → 0; toate CTA-urile primare bordo, max 1 per secțiune.

---

## FAZA 2 — Structură / wireframe

### 2.1 Hero-uri interioare comprimate
`servicii.html` și `oferte.html` au hero de 60–70vh pentru titlu + un paragraf; pe mobil prima informație utilă e la 2 ecrane distanță.
**Fix:** `min-h-[60vh] md:min-h-[70vh]` → `min-h-[32vh] md:min-h-[40vh]`, padding vertical redus, imaginea de fundal păstrată. Rating-ul 5,0★ rămâne în hero.

### 2.2 `index.html` — unifică secțiunile duplicate
„Galerie Foto & Video" și „Vezi cum arată un eveniment" sunt structural identice, consecutive. Păstrează **una singură**: titlu „Vezi cum arată un eveniment", grid cu 1 clip video (facade existentă) + 2 foto, link „Vezi toată galeria". Șterge cealaltă secțiune integral.

### 2.3 `index.html` — teaser-ul de oferte devine secțiune reală, mutată mai sus
Ordinea nouă a homepage-ului: Hero → Servicii → **Oferte (cu preț)** → Despre (+ rând de cifre) → Eveniment/Galerie → Recenzii → Booking CTA → FAQ.
Secțiunea Oferte: titlu, un rând cu „Pachete de la **4.800€**" (cifră mare, Garamond) + justificarea în același ecran (5,0★ · 61 recenzii, „formație 6 instrumente + 3 interpreți") + CTA „Vezi ofertele".
`<!-- TODO client: afișarea prețului pe homepage e decizie deschisă (CLAUDE.md §9) — secțiunea se construiește, dar cifra se activează doar după confirmare; până atunci textul e „Pachete pentru 2026–2027" -->`

### 2.4 `index.html` — Stats devine rând de cifre sub Despre
Șterge secțiunea Stats separată; sub textul „Despre" adaugă un rând flexbox cu 3 cifre verificate (15+ ani / 3 albume / 5,0★·61). Imaginea din Stats se poate refolosi în secțiunea Eveniment.

### 2.5 `servicii.html` — ierarhie în bento
Serviciile core (Muzică Populară, Cover Band, DJ & MC) primesc carduri mari cu imagine; „Consultant Evenimente" și „Muzică Live 100%" devin carduri mici, pe un rând secundar. Structură din flexbox cu `flex-wrap`, nu grid cu col-span (Elementor).

### 2.6 CTA de final pe paginile-fundătură
`discografie.html` și `galerie.html` se termină fără pas următor. Adaugă înaintea footer-ului o secțiune scurtă (reutilizează „Booking CTA" din index ca snippet canonic): „Îți place ce auzi? Rezervă data ta." + `Rezervă pe WhatsApp` / `Cere ofertă`.

### 2.7 FAQ extins la 5–6 întrebări
Adaugă la cele 2 existente (răspunsuri scurte, concrete): Cât durează programul? · Ce se întâmplă în pauzele formației? · Cântați și în afara Bucureștiului? (5 orașe SEO) · Cum rezerv data — avans și contract? `<!-- TODO client: validare răspunsuri -->`

**Verificare Faza 2:** pe mobil 360px, prima cifră de preț pe `oferte.html` vizibilă în max 1 ecran de scroll; homepage fără secțiuni duplicate; fiecare pagină se termină cu un CTA.

---

## FAZA 3 — Identitate vizuală (broderia + culoarea)

### 3.1 Motivele de broderie — ancora vizuală (cea mai importantă lucrare din fază)
Creează `assets/motifs.svg` cu 2–3 motive geometrice românești vectorizate simplu (romb, cruciuliță, linie frântă), **desenate după pozele reale în ie** (nu inventate ornamental). Un singur path per motiv, `currentColor`.
Aplicare (subtil, structural — nu ornament):
- **Separator de secțiune:** un rând de motive repetate orizontal (SVG inline sau `background-image` repetat), 15–20% opacitate, în locul liniilor `.luxury-line`/`hairline-separator` de pe paginile principale.
- **Marcatori:** bullet-urile listelor din pachetele de oferte (înlocuiesc `check_circle` Material) și ancora de eyebrow.
- **Textura din contact:** înlocuiește grila de puncte `.motif-overlay` cu motivul repetat la opacitate foarte mică (~4%).
Definește clasele o singură dată în `assets/styles.css`.

### 3.2 Politica de culoare pe imagini
- Hero-urile principale (index, oferte, servicii) și grid-ul principal din galerie: **color** (costumul trebuie să se vadă) — la placeholder-e se scoate doar clasa `grayscale`; imaginile reale vin de la client.
- Alb-negru rămâne **deliberat** pe: portretul din Despre, imaginile de atmosferă secundare.
- Șterge toate tranzițiile `grayscale hover:grayscale-0 duration-700/1000` de pe imagini mari (scumpe, inexistente pe mobil, greu de replicat în Elementor). Hover-ul pe carduri rămâne doar border/opacity.

### 3.3 Logo SVG
`<!-- TODO client: semnătura vectorizată -->` — când sosește: `assets/logo.svg` (alb pe transparent), înlocuiește URL-ul googleusercontent din header/drawer/footer pe toate paginile. Până atunci nu schimba nimic.

**Verificare Faza 3:** separatoarele cu motiv apar pe index + oferte + servicii; contrast păstrat ≥4.5:1; nicio tranziție grayscale pe imagini mari; `motifs.svg` sub 5KB.

---

## FAZA 4 — Capitolul „evenimente" (BLOCAT de materiale client)

> Nu începe faza fără materialele de mai jos. Structurile se pot pregăti cu placeholder marcat, dar nu se prezintă clientului final fără conținut real.

### Materiale necesare de la client (de cerut ACUM, în paralel cu fazele 0–3)
1. ID-uri YouTube pentru clipuri **live de la evenimente** (sloturile `data-yt="TODO"`)
2. 20–30 fotografii reale de la evenimente, color, cu ia vizibilă + sala/formația/ringul
3. 3–5 clipuri verticale 9:16 (TikTok/Instagram) cu momente live
4. Export recenzii Google Business Profile → selectăm 6–8
5. Semnătura pentru vectorizare (logo)
6. Confirmări: 300+ piese, componența exactă a formației, prețul pe homepage (da/nu), emailul oficial

### 4.1 Video live în hero (`index.html`)
Extinde pattern-ul `video-facade` existent: thumbnail-ul hero devine clip real live; buton „Vezi live" peste. Opțional (doar desktop): `<video muted loop playsinline>` de 10–15s ca fundal, cu fallback imagine — un singur video pe pagină, respectă `prefers-reduced-motion` (nu porni autoplay când e setat).

### 4.2 Secțiunea „Seara unui eveniment" (index, după Oferte sau în locul secțiunii Eveniment)
4 pași orizontali (flexbox, pe mobil stivă verticală): Primirea invitaților → Program folclor în ie → Petrecerea → Momentul DJ. Fiecare: foto/clip real + 1 frază concretă + ora aproximativă (ex. „20:30"). Titlu: „Cum arată seara cu noi".

### 4.3 Formația, cu chipuri (`servicii.html` + referință din oferte)
Secțiune nouă: foto de grup + rând de carduri mici (instrument + prenume). Leagă vizual cifra „6 instrumente + 3 interpreți" din pachetul Premium de oameni reali.

### 4.4 Galeria pe evenimente reale (`galerie.html`)
Restructurare: albume grupate pe eveniment („Nuntă · București · sept 2025"), fiecare cu 4–6 poze + 1 clip. Etichetele generice dispar.

### 4.5 Rând de clipuri verticale (galerie + teaser pe index)
Scroll orizontal (`overflow-x-auto` + `.no-scrollbar` existent), carduri 9:16, facade pe fiecare clip (pattern-ul existent). 4–5 momente live scurte cu sunet real.

### 4.6 Recenzii reale
Cele 3 carduri placeholder din index → 6–8 recenzii reale (prenume, tip eveniment, oraș) + link „Vezi toate cele 61 pe Google" (URL-ul profilului GBP).

### 4.7 Foto de producție în accordion (`oferte.html`)
În „Echipament Tehnic Profesional": 2–3 foto reale de setup (scenă montată, ecran LED, lumini) — justificarea vizuală a prețului de vârf.

**Verificare Faza 4:** niciun `data-yt="TODO"` rămas; toate imaginile din secțiunile noi sunt reale (fără aida-public); Lighthouse mobile fără regresie majoră (facade-urile țin iframe-urile lazy).

---

## Ordinea de execuție recomandată
1. **Faza 0** (azi) → commit „fix: bug-uri prototip"
2. **Trimite clientului lista de materiale** (Faza 4, secțiunea Materiale) — e pe drumul critic
3. **Faza 1** → commit „content: vocabular CTA + cifre verificate"
4. **Faza 2** → commit „structure: homepage reordonat + hero-uri comprimate"
5. **Faza 3** → commit „visual: motive broderie + politica de culoare"
6. **Faza 4** — pe măsură ce sosesc materialele, un commit per sub-task
