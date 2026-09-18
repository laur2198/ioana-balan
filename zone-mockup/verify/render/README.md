# Harness de randare

Măsoară layout-ul paginilor prototipului într-un browser real: derulare
orizontală și ținte de tap, pe lățimi configurabile.

**Nu face parte din site și nu intră în `run_all.sh`.** Suita de bază rămâne
fără rețea și fără Node — se rulează oriunde, cu `pip install -r
../requirements.txt`. Harness-ul ăsta cere Node și Chromium, deci stă separat.

---

## De ce există

Paginile încarcă Tailwind de pe `cdn.tailwindcss.com`, la runtime:

```html
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script src="../assets/tailwind.config.js"></script>
```

În sandbox-ul de dezvoltare, domeniul e **blocat de proxy-ul de egress**. Un
browser care deschide pagina de pe disc primește `ERR_BLOCKED` pe script și
randează documentul cu **zero clase Tailwind aplicate**. Pagina arată ca HTML
nestilizat, dar nu crapă și nu spune nimic — se măsoară fericit, și dă cifre
false.

Asta s-a și întâmplat: o rundă de audit a raportat „160 px de derulare
orizontală pe toate paginile de zonă, cauzată de drawerul mobil”. Nu exista.
Cei 160 px erau imaginea de hero randată la lățimea ei intrinsecă de 512 px,
pentru că `w-full h-full object-cover` nu se aplicase. Cu Tailwind încărcat,
`scrollWidth == clientWidth` pe toate paginile, iar drawerul închis stă la
`x = 360..720`, complet în afara viewportului.

Morala, și motivul pentru care harness-ul e în repo: **o măsurătoare de layout
fără CSS nu e o măsurătoare mai slabă, e o măsurătoare a altui document.**

---

## Cum funcționează

1. `build-tailwind.js` execută `assets/tailwind.config.js` cu un obiect
   `tailwind` fals — exact cum face scriptul CDN — și scoate un CSS din aceiași
   tokeni pe care îi folosește site-ul. Configurarea **nu se copiază**: dacă
   tokenii se schimbă în `assets/`, build-ul îi ia automat la următoarea rulare.
2. `measure.py` interceptează cererea către `cdn.tailwindcss.com` și o servește
   cu un shim care injectează CSS-ul construit și expune `window.tailwind`, ca
   `assets/tailwind.config.js` să nu crape când se încarcă imediat după.

**Paginile nu se modifică niciodată.** Injecția trăiește în contextul
browserului, pe durata măsurătorii. Harness-ul nu scrie în `*.html`.

Rezultatul e o aproximare bună, nu identitatea cu producția: Tailwind Play CDN
generează clasele la runtime din DOM, iar CLI-ul le generează la build din
sursă. Pentru clasele scrise literal în markup — tot ce folosesc paginile
astea — cele două coincid. O clasă compusă dinamic în JS ar lipsi din build;
prototipul nu are așa ceva.

---

## Instalare

```bash
cd zone-mockup/verify/render
npm install                                # versiuni fixate în package.json
pip install -r requirements.txt            # playwright
```

Chromium e preinstalat în sandbox, la `/opt/pw-browsers/`. `measure.py` îl
găsește singur; dacă nu e acolo, cade pe browserul implicit al lui Playwright.

`node_modules/` și `build/` sunt în `.gitignore`.

---

## Rulare

```bash
node build-tailwind.js        # o dată, și după orice schimbare de tokeni
python3 measure.py            # toate paginile din zone-mockup/, 5 lățimi
```

Opțiuni:

| Opțiune | Implicit | Ce face |
|---|---|---|
| `--dir` | `zone-mockup/` | directorul cu paginile |
| `--pagini` | toate `.html` din `--dir` | listă separată prin virgulă |
| `--latimi` | `360,390,768,1024,1440` | lățimile de viewport |
| `--tap` | oprit | raportează și țintele de tap |
| `--prag-tap` | `44` | pragul, în px |

```bash
# doar două pagini, două lățimi
python3 measure.py --pagini zona-ilfov.html,zona-prahova.html --latimi 360,1440

# paginile din rădăcină, cu ținte de tap
python3 measure.py --dir ../../.. --tap
```

Cod de ieșire: `0` dacă nimic nu depășește, `1` altfel.

---

## Ce raportează

**overflow** — `scrollWidth − clientWidth` pe `<html>`. Ținta e `0`: nicio bară
de derulare orizontală, până la 360 px (CLAUDE.md §8).

**tap** — ținte interactive sub prag. Două excepții, ambele intenționate:

- **linkurile inline din proză** se numără separat, nu ca eșec. WCAG 2.5.8
  „Target Size (Minimum)” scoate explicit ținta a cărei mărime e dată de
  line-height-ul textului din jur. A umfla la 44 px un link dintr-o frază ar
  rupe fluxul rândului;
- **conținutul drawerului închis** se ignoră cât timp drawerul e `inert` —
  nu e atingibil, deci nu e țintă.

---

## Cifre de referință

Măsurate pe `ae8f8b0`. Runda următoare compară față de ele.

| Pagini | Lățimi | overflow |
|---|---|---|
| cele 20 din `zone-mockup/` | 360 / 390 / 768 / 1024 / 1440 | **0 px, peste tot** |
| cele 11 din rădăcină | aceleași | **0 px, peste tot** |

Drawerul mobil, la 360 px: închis `x=360..720` cu `inert=true`, deschis
`x=0..360` cu `inert=false`, iar Escape îl închide și întoarce focusul pe
`#menu-toggle`.

### Ținte de tap — starea cunoscută

`--tap` raportează azi **două constatări, pe fiecare pagină**, ambele
preexistente și identice pe pagini neatinse. Harness-ul iese cu `1` din cauza
lor; asta e corect, sunt sub prag.

| Constatare | Lățimi | Ce e |
|---|---|---|
| `SAL 30×44` | 360, 390, 768 | linkul către platforma SOL/ODR din footer. 44 px înălțime, **30 px lățime** |
| `Despre / Galerie / Discografie / Oferte …` la `×20` | 1024, 1440 | nav-ul desktop: linkuri de 20 px înălțime, în `<nav>`, deci neacoperite de excepția „Inline” |

Niciuna nu ține de modulul de locații, care **nu conține elemente
interactive**. Se tratează separat; până atunci, un `--tap` care raportează
exact aceste două categorii înseamnă „nicio regresie”.

Pentru non-duplicare, cifrele de referință sunt în `../BAZA-NON-DUPLICARE.md`.
