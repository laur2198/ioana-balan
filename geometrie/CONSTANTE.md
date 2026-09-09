# Constante si exceptii — geometrie masurata

Extras din masuratorile din `geometrie/*.md`: 11 pagini, 4 viewport-uri, **103 sectiuni** in total (fara header, footer si hero-ul din `index.html`, masurate separat).

Toate cifrele sunt masurate in Chromium, nu citite din clase.

---

## 1. Padding-ul vertical de sectiune

**1440px** — valori (sus/jos), in ordinea frecventei:

| padding sus / jos | aparitii | sectiuni |
|---|---|---|
| 0 / 0 | 80 | oferte·S2, oferte·S3, oferte·S4, despre·S2, despre·S4, despre·S5 … |
| 96 / 96 | 11 | index·S1, index·S2, index·S3, index·S4, index·S5, index·S6 … |
| 128 / 128 | 2 | index·S7, galerie·S3 |
| 40 / 40 | 2 | oferte·S1, despre·S1 |
| 20 / 20 | 2 | politica-cookie·S1, termeni-si-conditii·S1 |
| 24 / 24 | 2 | politica-cookie·S4, termeni-si-conditii·S4 |
| 72 / 72 | 1 | despre·S3 |
| 64 / 0 | 1 | faq·S8 |
| 32 / 32 | 1 | blog·S3 |
| 48 / 48 | 1 | articol·S4 |

**Dominant la 1440: 0 sus / 0 jos**, in 80 din 103 sectiuni masurate.

Valoarea `0 / 0` vine aproape integral din paginile legale, care nu distanteaza sectiunile cu `padding`, ci cu `margin-bottom` pe sectiune. **Ignorand sectiunile fara padding vertical, dominanta la 1440 e 96 sus / 96 jos**, in 11 din 23 sectiuni cu padding.

La sectiunile cu padding `0 / 0`, distantarea reala vine din `margin-bottom`: **64px** ×53, **80px** ×7, **96px** ×3, **40px** ×3, **48px** ×3.

**1024px** — valori (sus/jos), in ordinea frecventei:

| padding sus / jos | aparitii | sectiuni |
|---|---|---|
| 0 / 0 | 80 | oferte·S2, oferte·S3, oferte·S4, despre·S2, despre·S4, despre·S5 … |
| 96 / 96 | 11 | index·S1, index·S2, index·S3, index·S4, index·S5, index·S6 … |
| 128 / 128 | 2 | index·S7, galerie·S3 |
| 40 / 40 | 2 | oferte·S1, despre·S1 |
| 20 / 20 | 2 | politica-cookie·S1, termeni-si-conditii·S1 |
| 24 / 24 | 2 | politica-cookie·S4, termeni-si-conditii·S4 |
| 72 / 72 | 1 | despre·S3 |
| 64 / 0 | 1 | faq·S8 |
| 32 / 32 | 1 | blog·S3 |
| 48 / 48 | 1 | articol·S4 |

**Dominant la 1024: 0 sus / 0 jos**, in 80 din 103 sectiuni masurate.

Valoarea `0 / 0` vine aproape integral din paginile legale, care nu distanteaza sectiunile cu `padding`, ci cu `margin-bottom` pe sectiune. **Ignorand sectiunile fara padding vertical, dominanta la 1024 e 96 sus / 96 jos**, in 11 din 23 sectiuni cu padding.

La sectiunile cu padding `0 / 0`, distantarea reala vine din `margin-bottom`: **64px** ×53, **80px** ×7, **96px** ×3, **40px** ×3, **48px** ×3.

**768px** — valori (sus/jos), in ordinea frecventei:

| padding sus / jos | aparitii | sectiuni |
|---|---|---|
| 0 / 0 | 79 | oferte·S2, oferte·S3, oferte·S4, despre·S2, despre·S4, despre·S5 … |
| 96 / 96 | 11 | index·S1, index·S2, index·S3, index·S4, index·S5, index·S6 … |
| 128 / 128 | 2 | index·S7, galerie·S3 |
| 40 / 40 | 2 | oferte·S1, despre·S1 |
| 20 / 20 | 2 | politica-cookie·S1, termeni-si-conditii·S1 |
| 24 / 24 | 2 | politica-cookie·S4, termeni-si-conditii·S4 |
| 72 / 72 | 1 | despre·S3 |
| 64 / 0 | 1 | faq·S8 |
| 32 / 32 | 1 | blog·S3 |
| 48 / 48 | 1 | articol·S4 |

**Dominant la 768: 0 sus / 0 jos**, in 79 din 102 sectiuni masurate.

Valoarea `0 / 0` vine aproape integral din paginile legale, care nu distanteaza sectiunile cu `padding`, ci cu `margin-bottom` pe sectiune. **Ignorand sectiunile fara padding vertical, dominanta la 768 e 96 sus / 96 jos**, in 11 din 23 sectiuni cu padding.

La sectiunile cu padding `0 / 0`, distantarea reala vine din `margin-bottom`: **64px** ×53, **80px** ×7, **96px** ×3, **40px** ×3, **48px** ×3.

**390px** — valori (sus/jos), in ordinea frecventei:

| padding sus / jos | aparitii | sectiuni |
|---|---|---|
| 0 / 0 | 79 | oferte·S2, oferte·S3, oferte·S4, despre·S2, despre·S4, despre·S5 … |
| 64 / 64 | 13 | index·S1, index·S2, index·S3, index·S4, index·S5, index·S6 … |
| 20 / 20 | 4 | politica-cookie·S1, politica-cookie·S4, termeni-si-conditii·S1, termeni-si-conditii·S4 |
| 40 / 40 | 2 | oferte·S1, despre·S1 |
| 80 / 80 | 1 | galerie·S3 |
| 48 / 0 | 1 | faq·S8 |
| 32 / 32 | 1 | blog·S3 |
| 24 / 24 | 1 | articol·S4 |

**Dominant la 390: 0 sus / 0 jos**, in 79 din 102 sectiuni masurate.

Valoarea `0 / 0` vine aproape integral din paginile legale, care nu distanteaza sectiunile cu `padding`, ci cu `margin-bottom` pe sectiune. **Ignorand sectiunile fara padding vertical, dominanta la 390 e 64 sus / 64 jos**, in 13 din 23 sectiuni cu padding.

La sectiunile cu padding `0 / 0`, distantarea reala vine din `margin-bottom`: **48px** ×50, **64px** ×7, **56px** ×5, **32px** ×3, **40px** ×3.

---

## 2. Latimea de container (continut, fara padding)

| Viewport | latime continut | aparitii | padding orizontal al containerului | sectiuni |
|---|---|---|---|---|
| 1440 | 576 | 56 | 0/0 | faq·S8, articol·S4, politica-cookie·S2, politica-cookie·S3, politica-cookie·S5 … |
| 1440 | 1072 | 21 | 64/64 | index·S1, index·S2, index·S3, index·S4, index·S5 … |
| 1440 | 704 | 6 | 0/0 | faq·S2, faq·S3, faq·S4, faq·S5, faq·S6 … |
| 1440 | 528 | 4 | 24/24 | politica-cookie·S1, politica-cookie·S4, termeni-si-conditii·S1, termeni-si-conditii·S4 |
| 1440 | 1440 | 3 | 0/0 | oferte·S1, despre·S1, contact·S1 |
| 1440 | 640 | 2 | 16/16 | oferte·S6, despre·S6 |
| 1440 | 220 | 1 | 0/0 | faq·S1 |
| 1440 | 720 | 1 | 0/0 | contact·S2 |
| 1440 | 432.66 | 1 | 0/0 | contact·S3 |
| 1440 | 615.34 | 1 | 0/0 | contact·S4 |
| 1440 | 672 | 1 | 0/0 | blog·S1 |
| 1440 | 382 | 1 | 0/0 | blog·S2 |
| 1440 | 168 | 1 | 32/32 | blog·S3 |
| 1440 | 232 | 1 | 0/0 | blog·S4 |
| 1440 | 896 | 1 | 0/0 | articol·S1 |
| 1440 | 706.66 | 1 | 0/0 | articol·S2 |
| 1440 | 768 | 1 | 0/0 | articol·S3 |
| 1024 | 576 | 56 | 0/0 | faq·S8, articol·S4, politica-cookie·S2, politica-cookie·S3, politica-cookie·S5 … |
| 1024 | 896 | 22 | 64/64, 0/0 | index·S1, index·S2, index·S3, index·S4, index·S5 … |
| 1024 | 704 | 6 | 0/0 | faq·S2, faq·S3, faq·S4, faq·S5, faq·S6 … |
| 1024 | 528 | 4 | 24/24 | politica-cookie·S1, politica-cookie·S4, termeni-si-conditii·S1, termeni-si-conditii·S4 |
| 1024 | 1024 | 3 | 0/0 | oferte·S1, despre·S1, contact·S1 |
| 1024 | 640 | 2 | 16/16 | oferte·S6, despre·S6 |
| 1024 | 589.33 | 2 | 0/0 | blog·S1, articol·S2 |
| 1024 | 220 | 1 | 0/0 | faq·S1 |
| 1024 | 512 | 1 | 0/0 | contact·S2 |
| 1024 | 359.33 | 1 | 0/0 | contact·S3 |
| 1024 | 512.67 | 1 | 0/0 | contact·S4 |
| 1024 | 316 | 1 | 0/0 | blog·S2 |
| 1024 | 124 | 1 | 32/32 | blog·S3 |
| 1024 | 188 | 1 | 0/0 | blog·S4 |
| 1024 | 768 | 1 | 0/0 | articol·S3 |
| 768 | 576 | 56 | 0/0, 32/32 | faq·S8, blog·S3, politica-cookie·S2, politica-cookie·S3, politica-cookie·S5 … |
| 768 | 640 | 25 | 64/64, 0/0 | index·S1, index·S2, index·S3, index·S4, index·S5 … |
| 768 | 704 | 6 | 0/0 | faq·S2, faq·S3, faq·S4, faq·S5, faq·S6 … |
| 768 | 528 | 4 | 24/24 | politica-cookie·S1, politica-cookie·S4, termeni-si-conditii·S1, termeni-si-conditii·S4 |
| 768 | 768 | 3 | 0/0 | oferte·S1, despre·S1, contact·S1 |
| 768 | 720 | 2 | 24/24 | discografie·S1, discografie·S2 |
| 768 | 418.66 | 2 | 0/0 | blog·S1, articol·S2 |
| 768 | 220 | 1 | 0/0 | faq·S1 |
| 768 | 448 | 1 | 0/0 | contact·S3 |
| 768 | 306 | 1 | 0/0 | blog·S2 |
| 768 | 542 | 1 | 0/0 | articol·S4 |
| 390 | 342 | 68 | 0/0, 24/24 | oferte·S2, oferte·S3, oferte·S4, despre·S2, despre·S3 … |
| 390 | 358 | 23 | 16/16, 0/0 | index·S1, index·S2, index·S3, index·S4, index·S5 … |
| 390 | 390 | 3 | 0/0 | oferte·S1, despre·S1, contact·S1 |
| 390 | 294 | 3 | 24/24, 32/32 | blog·S3, politica-cookie·S1, termeni-si-conditii·S1 |
| 390 | 302 | 2 | 20/20 | politica-cookie·S4, termeni-si-conditii·S4 |
| 390 | 220 | 1 | 0/0 | faq·S1 |
| 390 | 356 | 1 | 0/0 | blog·S2 |
| 390 | 308 | 1 | 0/0 | articol·S4 |

- **1440: dominant 576px**, in 56 din 103 sectiuni.
- **1024: dominant 576px**, in 56 din 103 sectiuni.
- **768: dominant 576px**, in 56 din 102 sectiuni.
- **390: dominant 342px**, in 68 din 102 sectiuni.

---

## 3. Gap-ul de grila

| Viewport | gap x / gap y | display | aparitii | sectiuni |
|---|---|---|---|---|
| 1440 | 16px / 16px | flex | 10 | index·S6, oferte·S5, oferte·S6, despre·S6, galerie·S2 … |
| 1440 | 24px / 24px | grid | 7 | index·S1, index·S3, index·S4, index·S5, oferte·S3 … |
| 1440 | 64px / 64px | grid | 3 | despre·S2, despre·S3, despre·S5 |
| 1440 | 8px / 8px | flex | 2 | faq·S2, blog·S4 |
| 1440 | 64px / 64px | flex | 1 | index·S2 |
| 1440 | 32px / 32px | flex | 1 | index·S7 |
| 1440 | 10px / 4px | inline-flex | 1 | oferte·S2 |
| 1440 | 32px / 32px | grid | 1 | discografie·S2 |
| 1440 | 48px / 48px | flex | 1 | discografie·S3 |
| 1440 | 40px / 40px | grid | 1 | contact·S4 |
| 1024 | 16px / 16px | flex | 10 | index·S6, oferte·S5, oferte·S6, despre·S6, galerie·S2 … |
| 1024 | 24px / 24px | grid | 7 | index·S1, index·S3, index·S4, index·S5, oferte·S3 … |
| 1024 | 64px / 64px | grid | 3 | despre·S2, despre·S3, despre·S5 |
| 1024 | 8px / 8px | flex | 2 | faq·S2, blog·S4 |
| 1024 | 64px / 64px | flex | 1 | index·S2 |
| 1024 | 32px / 32px | flex | 1 | index·S7 |
| 1024 | 10px / 4px | inline-flex | 1 | oferte·S2 |
| 1024 | 32px / 32px | grid | 1 | discografie·S2 |
| 1024 | 48px / 48px | flex | 1 | discografie·S3 |
| 1024 | 40px / 40px | grid | 1 | contact·S4 |
| 768 | 16px / 16px | flex | 10 | index·S6, oferte·S5, oferte·S6, despre·S6, galerie·S2 … |
| 768 | 24px / 24px | grid | 7 | index·S1, index·S3, index·S4, index·S5, oferte·S3 … |
| 768 | 64px / 64px | grid | 3 | despre·S2, despre·S3, despre·S5 |
| 768 | 8px / 8px | flex | 2 | faq·S2, blog·S4 |
| 768 | 64px / 64px | flex | 1 | index·S2 |
| 768 | 32px / 32px | flex | 1 | index·S7 |
| 768 | 10px / 4px | inline-flex | 1 | oferte·S2 |
| 768 | 32px / 32px | grid | 1 | discografie·S2 |
| 768 | 48px / 48px | flex | 1 | discografie·S3 |
| 768 | 40px / 40px | grid | 1 | contact·S4 |
| 390 | 16px / 16px | flex | 10 | index·S6, oferte·S5, oferte·S6, despre·S6, galerie·S2 … |
| 390 | 40px / 40px | grid | 4 | index·S3, despre·S2, despre·S3, despre·S5 |
| 390 | 24px / 24px | grid | 3 | index·S1, oferte·S3, discografie·S1 |
| 390 | 16px / 16px | grid | 2 | index·S4, index·S5 |
| 390 | 32px / 32px | grid | 2 | discografie·S2, contact·S4 |
| 390 | 8px / 8px | flex | 2 | faq·S2, blog·S4 |
| 390 | 40px / 40px | flex | 1 | index·S2 |
| 390 | 24px / 24px | flex | 1 | index·S7 |
| 390 | 10px / 4px | inline-flex | 1 | oferte·S2 |
| 390 | 48px / 48px | grid | 1 | galerie·S3 |
| 390 | 32px / 32px | flex | 1 | discografie·S3 |

- **1440: gap dominant 16px x / 16px y**, in 10 din 28 grile.
- **1024: gap dominant 16px x / 16px y**, in 10 din 28 grile.
- **768: gap dominant 16px x / 16px y**, in 10 din 28 grile.
- **390: gap dominant 16px x / 16px y**, in 12 din 28 grile.

---

## 4. Ritmul antetului de sectiune (eyebrow → titlu → motif → continut)

Sectiuni cu titlu detectat: **64**; cu eyebrow: **15**; cu separator `motif-*`: **23**.

Distantele sunt `rect.top` − `rect.bottom`, masurate.

| Pagina · sectiune | eyebrow | motif | eyebrow→titlu (1440/1024/768/390) | titlu→motif | motif(sau titlu)→continut |
|---|---|---|---|---|---|
| index · S1 | da | da | 12/12/12/12 | 20/20/20/20 | 64/64/64/48 |
| index · S2 | da | nu | 12/12/12/12 | —/—/—/— | -101.50/-115.50/136/128 |
| index · S3 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| index · S4 | da | nu | 8/8/8/8 | —/—/—/— | 56/56/56/40 |
| index · S5 | da | da | 16/16/16/16 | 24/24/24/24 | 64/64/64/40 |
| index · S6 | da | da | 16/16/16/16 | 20/20/20/20 | 56/56/56/40 |
| index · S7 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| oferte · S1 | da | da | 12/12/12/12 | 132/132/132/168 | —/—/—/— |
| oferte · S2 | nu | da | —/—/—/— | 20/20/20/20 | —/—/—/— |
| oferte · S3 | nu | da | —/—/—/— | 20/20/20/20 | 48/48/48/32 |
| oferte · S4 | da | nu | 12/12/12/12 | —/—/—/— | —/—/—/— |
| oferte · S5 | da | da | 16/16/16/16 | 20/20/20/20 | 64/64/64/40 |
| oferte · S6 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| despre · S1 | da | da | 12/12/12/12 | 28/28/28/28 | —/—/—/— |
| despre · S3 | nu | da | —/—/—/— | 24/24/24/24 | 24/24/24/24 |
| despre · S5 | nu | da | —/—/—/— | 24/24/24/24 | 24/24/24/24 |
| despre · S6 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| galerie · S1 | da | nu | 16/16/16/16 | —/—/—/— | 188/188/188/184 |
| galerie · S2 | da | nu | 12/12/12/12 | —/—/—/— | -20/-20/-20/16 |
| galerie · S3 | nu | nu | —/—/—/— | —/—/—/— | -119/-137/-113/316 |
| discografie · S1 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| discografie · S2 | nu | da | —/—/—/— | 8/8/8/8 | 48/48/48/48 |
| discografie · S3 | nu | nu | —/—/—/— | —/—/—/— | -13/-33/116/92 |
| faq · S1 | da | da | 12/12/12/12 | 104/104/104/152 | 40/40/40/32 |
| faq · S3 | nu | da | —/—/—/— | 16/16/16/16 | 32/32/32/28 |
| faq · S4 | nu | da | —/—/—/— | 16/16/16/16 | 32/32/32/28 |
| faq · S5 | nu | da | —/—/—/— | 16/16/16/16 | 32/32/32/28 |
| faq · S6 | nu | da | —/—/—/— | 16/16/16/16 | 32/32/32/28 |
| faq · S7 | nu | da | —/—/—/— | 16/16/16/16 | 32/32/32/28 |
| faq · S8 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| contact · S3 | nu | nu | —/—/—/— | —/—/—/— | 244/268/244/260 |
| contact · S4 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| blog · S1 | da | nu | 16/16/16/16 | —/—/—/— | —/—/—/— |
| blog · S2 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| articol · S1 | nu | nu | —/—/—/— | —/—/—/— | 116/116/116/116 |
| articol · S3 | nu | nu | —/—/—/— | —/—/—/— | 840/840/892/1302 |
| articol · S4 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| politica-cookie · S2 | da | nu | 12/12/12/12 | —/—/—/— | 80/80/80/72 |
| politica-cookie · S5 | nu | nu | —/—/—/— | —/—/—/— | 434.38/434.38/434.38/577.50 |
| politica-cookie · S7 | nu | da | —/—/—/— | 69.43/69.43/69.43/97.19 | 18/18/18/18 |
| politica-cookie · S9 | nu | nu | —/—/—/— | —/—/—/— | 1099.42/1099.42/1099.42/1448.80 |
| politica-cookie · S11 | nu | nu | —/—/—/— | —/—/—/— | 721.88/721.88/721.88/909.43 |
| politica-cookie · S13 | nu | nu | —/—/—/— | —/—/—/— | 227.75/227.75/227.75/233.97 |
| politica-cookie · S15 | nu | da | —/—/—/— | 132.31/132.31/132.31/185.97 | 18/18/18/18 |
| politica-cookie · S17 | nu | nu | —/—/—/— | —/—/—/— | 402.94/402.94/402.94/488.72 |
| politica-cookie · S19 | nu | nu | —/—/—/— | —/—/—/— | 178.31/178.31/178.31/215.97 |
| politica-cookie · S21 | nu | nu | —/—/—/— | —/—/—/— | —/—/—/— |
| termeni-si-conditii · S2 | da | nu | 12/12/12/12 | —/—/—/— | 80/80/80/72 |
| termeni-si-conditii · S5 | nu | da | —/—/—/— | 69.44/69.44/69.44/97.19 | 18/18/18/18 |
| termeni-si-conditii · S7 | nu | nu | —/—/—/— | —/—/—/— | 322.06/322.06/322.06/411.53 |
| termeni-si-conditii · S9 | nu | nu | —/—/—/— | —/—/—/— | 322.06/322.06/322.06/411.53 |
| termeni-si-conditii · S11 | nu | da | —/—/—/— | 150.31/150.31/150.31/203.97 | 18/18/18/18 |
| termeni-si-conditii · S13 | nu | nu | —/—/—/— | —/—/—/— | 464.38/464.38/464.38/518.72 |
| termeni-si-conditii · S15 | nu | nu | —/—/—/— | —/—/—/— | 340.06/340.06/340.06/370.35 |
| termeni-si-conditii · S17 | nu | nu | —/—/—/— | —/—/—/— | 259.19/259.19/259.19/293.15 |
| termeni-si-conditii · S19 | nu | nu | —/—/—/— | —/—/—/— | 452.37/452.37/452.37/595.50 |
| termeni-si-conditii · S21 | nu | nu | —/—/—/— | —/—/—/— | 371.50/371.50/371.50/429.53 |
| termeni-si-conditii · S23 | nu | nu | —/—/—/— | —/—/—/— | 371.50/371.50/371.50/429.53 |
| termeni-si-conditii · S25 | nu | nu | —/—/—/— | —/—/—/— | 259.19/259.19/259.19/293.16 |
| termeni-si-conditii · S27 | nu | da | —/—/—/— | 1099.11/1099.11/1172.69/1292.41 | 18/18/18/18 |
| termeni-si-conditii · S29 | nu | nu | —/—/—/— | —/—/—/— | 146.87/146.87/146.87/156.78 |
| termeni-si-conditii · S31 | nu | da | —/—/—/— | 118.88/118.88/118.88/144.78 | 18/18/18/18 |
| termeni-si-conditii · S33 | nu | nu | —/—/—/— | —/—/—/— | 259.19/259.19/259.19/322.75 |
| termeni-si-conditii · S35 | nu | nu | —/—/—/— | —/—/—/— | 146.87/146.87/146.87/156.78 |

- **eyebrow→titlu la 1440: dominant 12px** (9 din 15 cazuri). Restul: 16px ×5, 8px ×1.
- **titlu→motif la 1440: dominant 20px** (5 din 23 cazuri). Restul: 16px ×5, 24px ×3, 132px ×1, 28px ×1, 8px ×1.
- **motif/titlu→continut la 1440: dominant 18px** (6 din 49 cazuri). Restul: 32px ×5, 64px ×3, 259.19px ×3, 56px ×2, 48px ×2.

---

## 5. Scala tipografica efectiv folosita

### 1440px — 38 combinatii distincte, 688 elemente de text

| font-size | line-height | raport lh/fs | font-weight | familie | letter-spacing | aparitii | exemple |
|---|---|---|---|---|---|---|---|
| 16 | 24 | 1.50 | 400 | Inter | normal | 136 | index:Formație live și sonoriz, index:Muzică live și DJ pentru |
| 17 | 31.45 | 1.85 | 400 | Inter | normal | 111 | politica-cookie:Cookie-urile nu pot rula, politica-cookie:Pe lângă cookie-uri, sit |
| 17 | 31.45 | 1.85 | 600 | Inter | normal | 70 | politica-cookie:Regulamentul (UE) 2016/6, politica-cookie:art. 4 alin. (5) din Leg |
| 24 | 32 | 1.33 | 500 | EB Garamond | normal | 51 | index:Corporate, index:Muzică Botez |
| 32 | 40 | 1.25 | 500 | EB Garamond | normal | 48 | index:Muzică pentru nuntă, bot, index:Peste 15 ani pe scenă |
| 14 | 20 | 1.43 | 600 | Inter | 1.40 | 46 | index:Evenimente, index:Vezi ofertele |
| 14 | 20 | 1.43 | 600 | Inter | 0.70 | 29 | index:Ani pe scenă, index:Nuntă · Botez · Corporat |
| 18 | 28 | 1.56 | 400 | Inter | normal | 27 | index:Disponibilă pentru nunți, index:Formație live, interpreț |
| 11 | 13.20 | 1.20 | 600 | Inter | 1.54 | 23 | faq:Răspuns de confirmat, oferte:De confirmat |
| 16 | 25.60 | 1.60 | 400 | Inter | normal | 22 | politica-cookie:HTTP, politica-cookie:ioana-balan.ro |
| 48 | 56 | 1.17 | 500 | EB Garamond | -0.96 | 15 | index:Pachete pentru 2026–2027, index:Rezervă Formație Nuntă |
| 14 | 20 | 1.43 | 600 | Inter | 2.80 | 14 | oferte:Condiții comerciale, oferte:Nuntă |
| 14 | 22.40 | 1.60 | 600 | Inter | 0.84 | 9 | politica-cookie:Furnizor, politica-cookie:Nume |
| 16 | 26 | 1.62 | 400 | Inter | normal | 8 | articol:Luminile de scenă nu sun, index:Muzica nu este doar o pr |
| 12 | 18 | 1.50 | 400 | Inter | 1.20 | 8 | oferte:Duminică, oferte:Sâmbătă |
| 10 | 12 | 1.20 | 600 | Inter | 1.80 | 7 | galerie:Muzică de petrecere, index:Formație live |
| 22 | 27.50 | 1.25 | 500 | EB Garamond | normal | 7 | galerie:Atmosferă de petrecere l, index:Colaj de Moldova, live l |
| 16 | 24 | 1.50 | 600 | Inter | normal | 6 | politica-cookie:Ultima actualizare:, politica-cookie:[DATA-PUBLICARE] |
| 16 | 25.60 | 1.60 | 600 | Inter | normal | 6 | politica-cookie:[NUME-COOKIE], politica-cookie:[SCOP] |
| 11 | 24 | 2.18 | 400 | Inter | normal | 5 | blog:formatie nunta Bucuresti, blog:muzica populara nunta |
| 11 | 16.50 | 1.50 | 400 | Inter | 1.10 | 4 | oferte:Buget redus, oferte:Cel mai căutat |
| 36 | 40 | 1.11 | 400 | EB Garamond | normal | 4 | oferte:3.200 €, oferte:5.500 € |
| 24 | 32 | 1.33 | 400 | EB Garamond | normal | 4 | oferte:2.800 €, oferte:4.800 € |
| 10 | 24 | 2.40 | 400 | Inter | 1 | 4 | blog:Botezuri, blog:Nunți |
| 16 | 24 | 1.50 | 400 | Inter | 1.60 | 3 | index:Detalii |
| 15.64 | 28.93 | 1.85 | 400 | ui-monospace | normal | 3 | politica-cookie:localStorage, politica-cookie:sessionStorage |
| 36 | 36 | 1.00 | 400 | EB Garamond | normal | 2 | index:15+, index:3 |
| 14 | 20 | 1.43 | 600 | Inter | 4.20 | 2 | index:Întrebări Frecvente, oferte:Întrebări Frecvente |
| 15 | 24.38 | 1.63 | 400 | Inter | normal | 2 | contact:Politica de confidențial, contact:Sunt de acord ca datele  |
| 14 | 20 | 1.43 | 600 | Inter | 2.52 | 2 | politica-cookie:Document în lucru — nu e, termeni-si-conditii:Document în lucru — nu e |
| 16 | 26 | 1.62 | 600 | Inter | normal | 2 | politica-cookie:[EXEMPLU], termeni-si-conditii:[EXEMPLU] |
| 14 | 20 | 1.43 | 600 | Inter | 2.10 | 2 | politica-cookie:Cuprins, termeni-si-conditii:Cuprins |
| 18 | 28 | 1.56 | 400 | EB Garamond | normal | 1 | oferte:__ RON/km |
| 13 | 19.50 | 1.50 | 400 | Inter | normal | 1 | oferte:Elementele marcate „opți |
| 36 | 45 | 1.25 | 400 | EB Garamond | normal | 1 | despre:ca o frumoasă și de preț |
| 14 | 20 | 1.43 | 400 | Inter | normal | 1 | galerie:Autenticitate în fiecare |
| 56 | 61.60 | 1.10 | 400 | EB Garamond | normal | 1 | blog:Sfaturi și Inspirație pe |
| 48 | 60 | 1.25 | 500 | EB Garamond | -0.96 | 1 | articol:Importanța luminilor de  |

Marimi, pe frecventa: **16px** ×183, **17px** ×181, **14px** ×105, **24px** ×55, **32px** ×48, **11px** ×32, **18px** ×28, **48px** ×16, **10px** ×11, **12px** ×8, **22px** ×7, **36px** ×7, **15.64px** ×3, **15px** ×2, **13px** ×1, **56px** ×1.

### 1024px — 38 combinatii distincte, 688 elemente de text

| font-size | line-height | raport lh/fs | font-weight | familie | letter-spacing | aparitii | exemple |
|---|---|---|---|---|---|---|---|
| 16 | 24 | 1.50 | 400 | Inter | normal | 136 | index:Formație live și sonoriz, index:Muzică live și DJ pentru |
| 17 | 31.45 | 1.85 | 400 | Inter | normal | 111 | politica-cookie:Cookie-urile nu pot rula, politica-cookie:Pe lângă cookie-uri, sit |
| 17 | 31.45 | 1.85 | 600 | Inter | normal | 70 | politica-cookie:Regulamentul (UE) 2016/6, politica-cookie:art. 4 alin. (5) din Leg |
| 24 | 32 | 1.33 | 500 | EB Garamond | normal | 51 | index:Corporate, index:Muzică Botez |
| 32 | 40 | 1.25 | 500 | EB Garamond | normal | 48 | index:Muzică pentru nuntă, bot, index:Peste 15 ani pe scenă |
| 14 | 20 | 1.43 | 600 | Inter | 1.40 | 46 | index:Evenimente, index:Vezi ofertele |
| 14 | 20 | 1.43 | 600 | Inter | 0.70 | 29 | index:Ani pe scenă, index:Nuntă · Botez · Corporat |
| 18 | 28 | 1.56 | 400 | Inter | normal | 27 | index:Disponibilă pentru nunți, index:Formație live, interpreț |
| 11 | 13.20 | 1.20 | 600 | Inter | 1.54 | 23 | faq:Răspuns de confirmat, oferte:De confirmat |
| 16 | 25.60 | 1.60 | 400 | Inter | normal | 22 | politica-cookie:HTTP, politica-cookie:ioana-balan.ro |
| 48 | 56 | 1.17 | 500 | EB Garamond | -0.96 | 15 | index:Pachete pentru 2026–2027, index:Rezervă Formație Nuntă |
| 14 | 20 | 1.43 | 600 | Inter | 2.80 | 14 | oferte:Condiții comerciale, oferte:Nuntă |
| 14 | 22.40 | 1.60 | 600 | Inter | 0.84 | 9 | politica-cookie:Furnizor, politica-cookie:Nume |
| 16 | 26 | 1.62 | 400 | Inter | normal | 8 | articol:Luminile de scenă nu sun, index:Muzica nu este doar o pr |
| 12 | 18 | 1.50 | 400 | Inter | 1.20 | 8 | oferte:Duminică, oferte:Sâmbătă |
| 10 | 12 | 1.20 | 600 | Inter | 1.80 | 7 | galerie:Muzică de petrecere, index:Formație live |
| 22 | 27.50 | 1.25 | 500 | EB Garamond | normal | 7 | galerie:Atmosferă de petrecere l, index:Colaj de Moldova, live l |
| 16 | 24 | 1.50 | 600 | Inter | normal | 6 | politica-cookie:Ultima actualizare:, politica-cookie:[DATA-PUBLICARE] |
| 16 | 25.60 | 1.60 | 600 | Inter | normal | 6 | politica-cookie:[NUME-COOKIE], politica-cookie:[SCOP] |
| 11 | 24 | 2.18 | 400 | Inter | normal | 5 | blog:formatie nunta Bucuresti, blog:muzica populara nunta |
| 11 | 16.50 | 1.50 | 400 | Inter | 1.10 | 4 | oferte:Buget redus, oferte:Cel mai căutat |
| 36 | 40 | 1.11 | 400 | EB Garamond | normal | 4 | oferte:3.200 €, oferte:5.500 € |
| 24 | 32 | 1.33 | 400 | EB Garamond | normal | 4 | oferte:2.800 €, oferte:4.800 € |
| 10 | 24 | 2.40 | 400 | Inter | 1 | 4 | blog:Botezuri, blog:Nunți |
| 16 | 24 | 1.50 | 400 | Inter | 1.60 | 3 | index:Detalii |
| 15.64 | 28.93 | 1.85 | 400 | ui-monospace | normal | 3 | politica-cookie:localStorage, politica-cookie:sessionStorage |
| 36 | 36 | 1.00 | 400 | EB Garamond | normal | 2 | index:15+, index:3 |
| 14 | 20 | 1.43 | 600 | Inter | 4.20 | 2 | index:Întrebări Frecvente, oferte:Întrebări Frecvente |
| 15 | 24.38 | 1.63 | 400 | Inter | normal | 2 | contact:Politica de confidențial, contact:Sunt de acord ca datele  |
| 14 | 20 | 1.43 | 600 | Inter | 2.52 | 2 | politica-cookie:Document în lucru — nu e, termeni-si-conditii:Document în lucru — nu e |
| 16 | 26 | 1.62 | 600 | Inter | normal | 2 | politica-cookie:[EXEMPLU], termeni-si-conditii:[EXEMPLU] |
| 14 | 20 | 1.43 | 600 | Inter | 2.10 | 2 | politica-cookie:Cuprins, termeni-si-conditii:Cuprins |
| 18 | 28 | 1.56 | 400 | EB Garamond | normal | 1 | oferte:__ RON/km |
| 13 | 19.50 | 1.50 | 400 | Inter | normal | 1 | oferte:Elementele marcate „opți |
| 36 | 45 | 1.25 | 400 | EB Garamond | normal | 1 | despre:ca o frumoasă și de preț |
| 14 | 20 | 1.43 | 400 | Inter | normal | 1 | galerie:Autenticitate în fiecare |
| 56 | 61.60 | 1.10 | 400 | EB Garamond | normal | 1 | blog:Sfaturi și Inspirație pe |
| 48 | 60 | 1.25 | 500 | EB Garamond | -0.96 | 1 | articol:Importanța luminilor de  |

Marimi, pe frecventa: **16px** ×183, **17px** ×181, **14px** ×105, **24px** ×55, **32px** ×48, **11px** ×32, **18px** ×28, **48px** ×16, **10px** ×11, **12px** ×8, **22px** ×7, **36px** ×7, **15.64px** ×3, **15px** ×2, **13px** ×1, **56px** ×1.

### 768px — 38 combinatii distincte, 688 elemente de text

| font-size | line-height | raport lh/fs | font-weight | familie | letter-spacing | aparitii | exemple |
|---|---|---|---|---|---|---|---|
| 16 | 24 | 1.50 | 400 | Inter | normal | 136 | index:Formație live și sonoriz, index:Muzică live și DJ pentru |
| 17 | 31.45 | 1.85 | 400 | Inter | normal | 111 | politica-cookie:Cookie-urile nu pot rula, politica-cookie:Pe lângă cookie-uri, sit |
| 17 | 31.45 | 1.85 | 600 | Inter | normal | 70 | politica-cookie:Regulamentul (UE) 2016/6, politica-cookie:art. 4 alin. (5) din Leg |
| 24 | 32 | 1.33 | 500 | EB Garamond | normal | 51 | index:Corporate, index:Muzică Botez |
| 32 | 40 | 1.25 | 500 | EB Garamond | normal | 48 | index:Muzică pentru nuntă, bot, index:Peste 15 ani pe scenă |
| 14 | 20 | 1.43 | 600 | Inter | 1.40 | 46 | index:Evenimente, index:Vezi ofertele |
| 14 | 20 | 1.43 | 600 | Inter | 0.70 | 29 | index:Ani pe scenă, index:Nuntă · Botez · Corporat |
| 18 | 28 | 1.56 | 400 | Inter | normal | 27 | index:Disponibilă pentru nunți, index:Formație live, interpreț |
| 11 | 13.20 | 1.20 | 600 | Inter | 1.54 | 23 | faq:Răspuns de confirmat, oferte:De confirmat |
| 16 | 25.60 | 1.60 | 400 | Inter | normal | 22 | politica-cookie:HTTP, politica-cookie:ioana-balan.ro |
| 48 | 56 | 1.17 | 500 | EB Garamond | -0.96 | 15 | index:Pachete pentru 2026–2027, index:Rezervă Formație Nuntă |
| 14 | 20 | 1.43 | 600 | Inter | 2.80 | 14 | oferte:Condiții comerciale, oferte:Nuntă |
| 14 | 22.40 | 1.60 | 600 | Inter | 0.84 | 9 | politica-cookie:Furnizor, politica-cookie:Nume |
| 16 | 26 | 1.62 | 400 | Inter | normal | 8 | articol:Luminile de scenă nu sun, index:Muzica nu este doar o pr |
| 12 | 18 | 1.50 | 400 | Inter | 1.20 | 8 | oferte:Duminică, oferte:Sâmbătă |
| 10 | 12 | 1.20 | 600 | Inter | 1.80 | 7 | galerie:Muzică de petrecere, index:Formație live |
| 22 | 27.50 | 1.25 | 500 | EB Garamond | normal | 7 | galerie:Atmosferă de petrecere l, index:Colaj de Moldova, live l |
| 16 | 24 | 1.50 | 600 | Inter | normal | 6 | politica-cookie:Ultima actualizare:, politica-cookie:[DATA-PUBLICARE] |
| 16 | 25.60 | 1.60 | 600 | Inter | normal | 6 | politica-cookie:[NUME-COOKIE], politica-cookie:[SCOP] |
| 11 | 24 | 2.18 | 400 | Inter | normal | 5 | blog:formatie nunta Bucuresti, blog:muzica populara nunta |
| 11 | 16.50 | 1.50 | 400 | Inter | 1.10 | 4 | oferte:Buget redus, oferte:Cel mai căutat |
| 36 | 40 | 1.11 | 400 | EB Garamond | normal | 4 | oferte:3.200 €, oferte:5.500 € |
| 24 | 32 | 1.33 | 400 | EB Garamond | normal | 4 | oferte:2.800 €, oferte:4.800 € |
| 10 | 24 | 2.40 | 400 | Inter | 1 | 4 | blog:Botezuri, blog:Nunți |
| 16 | 24 | 1.50 | 400 | Inter | 1.60 | 3 | index:Detalii |
| 15.64 | 28.93 | 1.85 | 400 | ui-monospace | normal | 3 | politica-cookie:localStorage, politica-cookie:sessionStorage |
| 36 | 36 | 1.00 | 400 | EB Garamond | normal | 2 | index:15+, index:3 |
| 14 | 20 | 1.43 | 600 | Inter | 4.20 | 2 | index:Întrebări Frecvente, oferte:Întrebări Frecvente |
| 15 | 24.38 | 1.63 | 400 | Inter | normal | 2 | contact:Politica de confidențial, contact:Sunt de acord ca datele  |
| 14 | 20 | 1.43 | 600 | Inter | 2.52 | 2 | politica-cookie:Document în lucru — nu e, termeni-si-conditii:Document în lucru — nu e |
| 16 | 26 | 1.62 | 600 | Inter | normal | 2 | politica-cookie:[EXEMPLU], termeni-si-conditii:[EXEMPLU] |
| 14 | 20 | 1.43 | 600 | Inter | 2.10 | 2 | politica-cookie:Cuprins, termeni-si-conditii:Cuprins |
| 18 | 28 | 1.56 | 400 | EB Garamond | normal | 1 | oferte:__ RON/km |
| 13 | 19.50 | 1.50 | 400 | Inter | normal | 1 | oferte:Elementele marcate „opți |
| 36 | 45 | 1.25 | 400 | EB Garamond | normal | 1 | despre:ca o frumoasă și de preț |
| 14 | 20 | 1.43 | 400 | Inter | normal | 1 | galerie:Autenticitate în fiecare |
| 48 | 52.80 | 1.10 | 400 | EB Garamond | normal | 1 | blog:Sfaturi și Inspirație pe |
| 48 | 60 | 1.25 | 500 | EB Garamond | -0.96 | 1 | articol:Importanța luminilor de  |

Marimi, pe frecventa: **16px** ×183, **17px** ×181, **14px** ×105, **24px** ×55, **32px** ×48, **11px** ×32, **18px** ×28, **48px** ×17, **10px** ×11, **12px** ×8, **22px** ×7, **36px** ×7, **15.64px** ×3, **15px** ×2, **13px** ×1.

### 390px — 56 combinatii distincte, 690 elemente de text

| font-size | line-height | raport lh/fs | font-weight | familie | letter-spacing | aparitii | exemple |
|---|---|---|---|---|---|---|---|
| 16 | 24 | 1.50 | 400 | Inter | normal | 154 | index:Formație live și sonoriz, index:Muzică live și DJ pentru |
| 16 | 29.60 | 1.85 | 400 | Inter | normal | 113 | politica-cookie:Cookie-urile nu pot rula, politica-cookie:Pe lângă cookie-uri, sit |
| 16 | 29.60 | 1.85 | 600 | Inter | normal | 70 | politica-cookie:Regulamentul (UE) 2016/6, politica-cookie:art. 4 alin. (5) din Leg |
| 14 | 20 | 1.43 | 600 | Inter | 1.40 | 46 | index:Evenimente, index:Vezi ofertele |
| 24 | 30 | 1.25 | 400 | EB Garamond | normal | 30 | faq:Prestația, faq:Preț |
| 16 | 22 | 1.38 | 400 | EB Garamond | normal | 25 | index:Cum rezerv data — avans , index:Cântați și în afara Bucu |
| 14 | 20 | 1.43 | 600 | Inter | 0.70 | 24 | index:Alexandru Dimov, index:Cristina Lixandru |
| 11 | 13.20 | 1.20 | 600 | Inter | 1.54 | 23 | faq:Răspuns de confirmat, oferte:De confirmat |
| 16 | 25.60 | 1.60 | 400 | Inter | normal | 22 | politica-cookie:HTTP, politica-cookie:ioana-balan.ro |
| 16 | 26 | 1.62 | 400 | Inter | normal | 14 | index:Muzica nu este doar o pr, index:Pentru mine, cea mai mar |
| 14 | 20 | 1.43 | 600 | Inter | 2.80 | 14 | oferte:Condiții comerciale, oferte:Nuntă |
| 24 | 32 | 1.33 | 500 | EB Garamond | normal | 12 | index:Corporate, index:Muzică Botez |
| 20 | 30 | 1.50 | 400 | EB Garamond | normal | 10 | politica-cookie:3.1 Cookie-uri strict ne, politica-cookie:3.2 Cookie-uri de analiz |
| 14 | 22.40 | 1.60 | 600 | Inter | 0.84 | 9 | politica-cookie:Furnizor, politica-cookie:Nume |
| 20 | 28 | 1.40 | 400 | EB Garamond | normal | 8 | oferte:4.800 €, oferte:Pachet Premium |
| 12 | 18 | 1.50 | 400 | Inter | 1.20 | 8 | oferte:Duminică, oferte:Sâmbătă |
| 28 | 24 | 0.86 | 400 | EB Garamond | normal | 7 | index:Muzică pentru nuntă, bot, index:Peste 15 ani pe scenă |
| 10 | 12 | 1.20 | 600 | Inter | 1.80 | 7 | galerie:Muzică de petrecere, index:Formație live |
| 18 | 22.50 | 1.25 | 500 | EB Garamond | normal | 7 | galerie:Atmosferă de petrecere l, index:Colaj de Moldova, live l |
| 30 | 37.50 | 1.25 | 400 | EB Garamond | normal | 6 | despre:Despre mine, galerie:Esența Tradiției în Imag |
| 16 | 24 | 1.50 | 600 | Inter | normal | 6 | politica-cookie:Ultima actualizare:, politica-cookie:[DATA-PUBLICARE] |
| 16 | 25.60 | 1.60 | 600 | Inter | normal | 6 | politica-cookie:[NUME-COOKIE], politica-cookie:[SCOP] |
| 30 | 36 | 1.20 | 400 | EB Garamond | normal | 5 | oferte:3.200 €, oferte:5.500 € |
| 11 | 24 | 2.18 | 400 | Inter | normal | 5 | blog:formatie nunta Bucuresti, blog:muzica populara nunta |
| 24 | 32 | 1.33 | 400 | EB Garamond | normal | 4 | despre:Rădăcini, oferte:Acoperire |
| 11 | 16.50 | 1.50 | 400 | Inter | 1.10 | 4 | oferte:Buget redus, oferte:Cel mai căutat |
| 10 | 24 | 2.40 | 400 | Inter | 1 | 4 | blog:Botezuri, blog:Nunți |
| 16 | 24 | 1.50 | 400 | Inter | 1.60 | 3 | index:Detalii |
| 18 | 28 | 1.56 | 400 | Inter | normal | 3 | articol:La o formație de nuntă, , blog:Descoperă secretele unei |
| 24 | 24 | 1.00 | 400 | EB Garamond | normal | 3 | discografie:Glasul Inimii, discografie:Melodii noi Ioana Balan |
| 14.72 | 27.23 | 1.85 | 400 | ui-monospace | normal | 3 | politica-cookie:localStorage, politica-cookie:sessionStorage |
| 12 | 24 | 2.00 | 400 | Inter | 3.60 | 2 | index:Nuntă · Botez · Corporat, index:Oferte |
| 28 | 28 | 1.00 | 400 | EB Garamond | normal | 2 | index:15+, index:3 |
| 12 | 24 | 2.00 | 400 | Inter | normal | 2 | index:Albume proprii, index:Ani pe scenă |
| 14 | 20 | 1.43 | 600 | Inter | 4.20 | 2 | index:Întrebări Frecvente, oferte:Întrebări Frecvente |
| 28 | 35 | 1.25 | 400 | EB Garamond | normal | 2 | despre:Hai să ne cunoaștem, oferte:Verificați dacă data est |
| 15 | 24.38 | 1.63 | 400 | Inter | normal | 2 | contact:Politica de confidențial, contact:Sunt de acord ca datele  |
| 32 | 40 | 1.25 | 500 | EB Garamond | normal | 2 | articol:Atmosfera și Dinamica Vi, articol:Profesionalismul din Spa |
| 14 | 20 | 1.43 | 600 | Inter | 2.52 | 2 | politica-cookie:Document în lucru — nu e, termeni-si-conditii:Document în lucru — nu e |
| 16 | 26 | 1.62 | 600 | Inter | normal | 2 | politica-cookie:[EXEMPLU], termeni-si-conditii:[EXEMPLU] |
| 14 | 20 | 1.43 | 600 | Inter | 2.10 | 2 | politica-cookie:Cuprins, termeni-si-conditii:Cuprins |
| 32 | 40 | 1.25 | 400 | EB Garamond | normal | 1 | index:Pachete pentru 2026–2027 |
| 20 | 24 | 1.20 | 400 | EB Garamond | normal | 1 | index:+40 722 911 485 |
| 12 | 24 | 2.00 | 400 | Inter | 1.20 | 1 | index:Cere ofertă |
| 18 | 28 | 1.56 | 400 | EB Garamond | normal | 1 | oferte:__ RON/km |
| 13 | 19.50 | 1.50 | 400 | Inter | normal | 1 | oferte:Elementele marcate „opți |
| 28 | 42 | 1.50 | 400 | EB Garamond | normal | 1 | oferte:Preț, rezervare și contr |
| 26 | 33.80 | 1.30 | 400 | EB Garamond | normal | 1 | despre:ca o frumoasă și de preț |
| 14 | 20 | 1.43 | 400 | Inter | normal | 1 | galerie:Autenticitate în fiecare |
| 36 | 45 | 1.25 | 400 | EB Garamond | normal | 1 | discografie:Hai să nu ne mai mințim |
| 26 | 24 | 0.92 | 400 | EB Garamond | normal | 1 | discografie:Îți place ce auzi? Rezer |
| 26 | 32.50 | 1.25 | 400 | EB Garamond | normal | 1 | faq:Nu ați găsit răspunsul? |
| 28 | 35 | 1.25 | 500 | EB Garamond | normal | 1 | contact:Rezervări și Contact Ioa |
| 32 | 35.20 | 1.10 | 400 | EB Garamond | normal | 1 | blog:Sfaturi și Inspirație pe |
| 48 | 60 | 1.25 | 500 | EB Garamond | -0.96 | 1 | articol:Importanța luminilor de  |
| 48 | 56 | 1.17 | 500 | EB Garamond | -0.96 | 1 | articol:Plănuiți un eveniment? |

Marimi, pe frecventa: **16px** ×415, **14px** ×100, **24px** ×49, **11px** ×32, **20px** ×19, **12px** ×13, **28px** ×13, **10px** ×11, **18px** ×11, **30px** ×11, **32px** ×4, **14.72px** ×3, **26px** ×3, **15px** ×2, **48px** ×2, **13px** ×1, **36px** ×1.

---

# Exceptiile

Fiecare sectiune care deviaza de la constanta dominanta, cu valoarea ei si diferenta fata de norma. Nu sunt clasificate ca intentionate sau scapari — doar masurate.

## E1. Padding vertical de sectiune diferit de dominanta

| Pagina · sectiune | Viewport | masurat sus/jos | norma | delta sus | delta jos |
|---|---|---|---|---|---|
| index · S1 — Muzică pentru nuntă, botez și corp | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S2 — Pachete pentru 2026–2027 | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S3 — Peste 15 ani pe scenă | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S4 — Vezi cum arată un eveniment | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S5 — Ce Spun Mirii și Gazdele | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S6 — Ce ne întrebați cel mai des | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S7 — Rezervă Formație Nuntă | 1440 | 128 / 128 | 0 / 0 | 128 | 128 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 1440 | 40 / 40 | 0 / 0 | 40 | 40 |
| oferte · S5 — Preț, rezervare și contract | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| oferte · S6 — Verificați dacă data este liberă | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| despre · S1 — Despre mine | 1440 | 40 / 40 | 0 / 0 | 40 | 40 |
| despre · S3 — Rădăcini | 1440 | 72 / 72 | 0 / 0 | 72 | 72 |
| despre · S6 — Hai să ne cunoaștem | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S3 — Esența Tradiției în Imagini. | 1440 | 128 / 128 | 0 / 0 | 128 | 128 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1440 | 96 / 96 | 0 / 0 | 96 | 96 |
| faq · S8 — Nu ați găsit răspunsul? | 1440 | 64 / 0 | 0 / 0 | 64 | 0 |
| blog · S3 — Primește Noutăți | 1440 | 32 / 32 | 0 / 0 | 32 | 32 |
| articol · S4 — Plănuiți un eveniment? | 1440 | 48 / 48 | 0 / 0 | 48 | 48 |
| politica-cookie · S1 — [EXEMPLU] | 1440 | 20 / 20 | 0 / 0 | 20 | 20 |
| politica-cookie · S4 — cuprins | 1440 | 24 / 24 | 0 / 0 | 24 | 24 |
| termeni-si-conditii · S1 — [EXEMPLU] | 1440 | 20 / 20 | 0 / 0 | 20 | 20 |
| termeni-si-conditii · S4 — cuprins | 1440 | 24 / 24 | 0 / 0 | 24 | 24 |
| index · S1 — Muzică pentru nuntă, botez și corp | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S2 — Pachete pentru 2026–2027 | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S3 — Peste 15 ani pe scenă | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S4 — Vezi cum arată un eveniment | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S5 — Ce Spun Mirii și Gazdele | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S6 — Ce ne întrebați cel mai des | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S7 — Rezervă Formație Nuntă | 1024 | 128 / 128 | 0 / 0 | 128 | 128 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 1024 | 40 / 40 | 0 / 0 | 40 | 40 |
| oferte · S5 — Preț, rezervare și contract | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| oferte · S6 — Verificați dacă data este liberă | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| despre · S1 — Despre mine | 1024 | 40 / 40 | 0 / 0 | 40 | 40 |
| despre · S3 — Rădăcini | 1024 | 72 / 72 | 0 / 0 | 72 | 72 |
| despre · S6 — Hai să ne cunoaștem | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S3 — Esența Tradiției în Imagini. | 1024 | 128 / 128 | 0 / 0 | 128 | 128 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1024 | 96 / 96 | 0 / 0 | 96 | 96 |
| faq · S8 — Nu ați găsit răspunsul? | 1024 | 64 / 0 | 0 / 0 | 64 | 0 |
| blog · S3 — Primește Noutăți | 1024 | 32 / 32 | 0 / 0 | 32 | 32 |
| articol · S4 — Plănuiți un eveniment? | 1024 | 48 / 48 | 0 / 0 | 48 | 48 |
| politica-cookie · S1 — [EXEMPLU] | 1024 | 20 / 20 | 0 / 0 | 20 | 20 |
| politica-cookie · S4 — cuprins | 1024 | 24 / 24 | 0 / 0 | 24 | 24 |
| termeni-si-conditii · S1 — [EXEMPLU] | 1024 | 20 / 20 | 0 / 0 | 20 | 20 |
| termeni-si-conditii · S4 — cuprins | 1024 | 24 / 24 | 0 / 0 | 24 | 24 |
| index · S1 — Muzică pentru nuntă, botez și corp | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S2 — Pachete pentru 2026–2027 | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S3 — Peste 15 ani pe scenă | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S4 — Vezi cum arată un eveniment | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S5 — Ce Spun Mirii și Gazdele | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S6 — Ce ne întrebați cel mai des | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| index · S7 — Rezervă Formație Nuntă | 768 | 128 / 128 | 0 / 0 | 128 | 128 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 768 | 40 / 40 | 0 / 0 | 40 | 40 |
| oferte · S5 — Preț, rezervare și contract | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| oferte · S6 — Verificați dacă data este liberă | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| despre · S1 — Despre mine | 768 | 40 / 40 | 0 / 0 | 40 | 40 |
| despre · S3 — Rădăcini | 768 | 72 / 72 | 0 / 0 | 72 | 72 |
| despre · S6 — Hai să ne cunoaștem | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| galerie · S3 — Esența Tradiției în Imagini. | 768 | 128 / 128 | 0 / 0 | 128 | 128 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 768 | 96 / 96 | 0 / 0 | 96 | 96 |
| faq · S8 — Nu ați găsit răspunsul? | 768 | 64 / 0 | 0 / 0 | 64 | 0 |
| blog · S3 — Primește Noutăți | 768 | 32 / 32 | 0 / 0 | 32 | 32 |
| articol · S4 — Plănuiți un eveniment? | 768 | 48 / 48 | 0 / 0 | 48 | 48 |
| politica-cookie · S1 — [EXEMPLU] | 768 | 20 / 20 | 0 / 0 | 20 | 20 |
| politica-cookie · S4 — cuprins | 768 | 24 / 24 | 0 / 0 | 24 | 24 |
| termeni-si-conditii · S1 — [EXEMPLU] | 768 | 20 / 20 | 0 / 0 | 20 | 20 |
| termeni-si-conditii · S4 — cuprins | 768 | 24 / 24 | 0 / 0 | 24 | 24 |
| index · S1 — Muzică pentru nuntă, botez și corp | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S2 — Pachete pentru 2026–2027 | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S3 — Peste 15 ani pe scenă | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S4 — Vezi cum arată un eveniment | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S5 — Ce Spun Mirii și Gazdele | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S6 — Ce ne întrebați cel mai des | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| index · S7 — Rezervă Formație Nuntă | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 390 | 40 / 40 | 0 / 0 | 40 | 40 |
| oferte · S5 — Preț, rezervare și contract | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| oferte · S6 — Verificați dacă data este liberă | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| despre · S1 — Despre mine | 390 | 40 / 40 | 0 / 0 | 40 | 40 |
| despre · S3 — Rădăcini | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| despre · S6 — Hai să ne cunoaștem | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| galerie · S3 — Esența Tradiției în Imagini. | 390 | 80 / 80 | 0 / 0 | 80 | 80 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 390 | 64 / 64 | 0 / 0 | 64 | 64 |
| faq · S8 — Nu ați găsit răspunsul? | 390 | 48 / 0 | 0 / 0 | 48 | 0 |
| blog · S3 — Primește Noutăți | 390 | 32 / 32 | 0 / 0 | 32 | 32 |
| articol · S4 — Plănuiți un eveniment? | 390 | 24 / 24 | 0 / 0 | 24 | 24 |
| politica-cookie · S1 — [EXEMPLU] | 390 | 20 / 20 | 0 / 0 | 20 | 20 |
| politica-cookie · S4 — cuprins | 390 | 20 / 20 | 0 / 0 | 20 | 20 |
| termeni-si-conditii · S1 — [EXEMPLU] | 390 | 20 / 20 | 0 / 0 | 20 | 20 |
| termeni-si-conditii · S4 — cuprins | 390 | 20 / 20 | 0 / 0 | 20 | 20 |

Total devieri de padding: **92**.

## E2. Latime de container diferita de dominanta

| Pagina · sectiune | Viewport | latime continut | norma | delta |
|---|---|---|---|---|
| index · S1 — Muzică pentru nuntă, botez și corp | 1440 | 1072 | 576 | 496 |
| index · S2 — Pachete pentru 2026–2027 | 1440 | 1072 | 576 | 496 |
| index · S3 — Peste 15 ani pe scenă | 1440 | 1072 | 576 | 496 |
| index · S4 — Vezi cum arată un eveniment | 1440 | 1072 | 576 | 496 |
| index · S5 — Ce Spun Mirii și Gazdele | 1440 | 1072 | 576 | 496 |
| index · S6 — Ce ne întrebați cel mai des | 1440 | 1072 | 576 | 496 |
| index · S7 — Rezervă Formație Nuntă | 1440 | 1072 | 576 | 496 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 1440 | 1440 | 576 | 864 |
| oferte · S2 — Condiții comerciale | 1440 | 1072 | 576 | 496 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 1440 | 1072 | 576 | 496 |
| oferte · S4 — Acoperire | 1440 | 1072 | 576 | 496 |
| oferte · S5 — Preț, rezervare și contract | 1440 | 1072 | 576 | 496 |
| oferte · S6 — Verificați dacă data este liberă | 1440 | 640 | 576 | 64 |
| despre · S1 — Despre mine | 1440 | 1440 | 576 | 864 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 1440 | 1072 | 576 | 496 |
| despre · S3 — Rădăcini | 1440 | 1072 | 576 | 496 |
| despre · S4 — ca o frumoasă și de preț zestre, p | 1440 | 1072 | 576 | 496 |
| despre · S5 — Primii pași | 1440 | 1072 | 576 | 496 |
| despre · S6 — Hai să ne cunoaștem | 1440 | 640 | 576 | 64 |
| galerie · S1 — Galerie de Spectacole | 1440 | 1072 | 576 | 496 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 1440 | 1072 | 576 | 496 |
| galerie · S3 — Esența Tradiției în Imagini. | 1440 | 1072 | 576 | 496 |
| discografie · S1 — Hai să nu ne mai mințim | 1440 | 1072 | 576 | 496 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 1440 | 1072 | 576 | 496 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1440 | 1072 | 576 | 496 |
| faq · S1 — Ce ne întrebați cel mai des | 1440 | 220 | 576 | -356 |
| faq · S2 — Preț | 1440 | 704 | 576 | 128 |
| faq · S3 — Preț (#pret) | 1440 | 704 | 576 | 128 |
| faq · S4 — Rezervare și contract (#rezervare- | 1440 | 704 | 576 | 128 |
| faq · S5 — Prestația (#prestatia) | 1440 | 704 | 576 | 128 |
| faq · S6 — Tehnic și locație (#tehnic-si-loca | 1440 | 704 | 576 | 128 |
| faq · S7 — Deplasare (#deplasare) | 1440 | 704 | 576 | 128 |
| contact · S1 — div.absolute | 1440 | 1440 | 576 | 864 |
| contact · S2 — div.absolute | 1440 | 720 | 576 | 144 |
| contact · S3 — Rezervări și Contact Ioana Balan | 1440 | 432.66 | 576 | -143.34 |
| contact · S4 — Cere ofertă personalizată | 1440 | 615.34 | 576 | 39.34 |
| blog · S1 — Sfaturi și Inspirație pentru Eveni | 1440 | 672 | 576 | 96 |
| blog · S2 — Cum să alegi formația de nuntă per | 1440 | 382 | 576 | -194 |
| blog · S3 — Primește Noutăți | 1440 | 168 | 576 | -408 |
| blog · S4 — Tag-uri SEO | 1440 | 232 | 576 | -344 |
| articol · S1 — Importanța luminilor de scenă pent | 1440 | 896 | 576 | 320 |
| articol · S2 — "Lumina nu doar luminează, ea tran | 1440 | 706.66 | 576 | 130.66 |
| articol · S3 — Atmosfera și Dinamica Vizuală | 1440 | 768 | 576 | 192 |
| politica-cookie · S1 — [EXEMPLU] | 1440 | 528 | 576 | -48 |
| politica-cookie · S4 — cuprins | 1440 | 528 | 576 | -48 |
| termeni-si-conditii · S1 — [EXEMPLU] | 1440 | 528 | 576 | -48 |
| termeni-si-conditii · S4 — cuprins | 1440 | 528 | 576 | -48 |
| index · S1 — Muzică pentru nuntă, botez și corp | 1024 | 896 | 576 | 320 |
| index · S2 — Pachete pentru 2026–2027 | 1024 | 896 | 576 | 320 |
| index · S3 — Peste 15 ani pe scenă | 1024 | 896 | 576 | 320 |
| index · S4 — Vezi cum arată un eveniment | 1024 | 896 | 576 | 320 |
| index · S5 — Ce Spun Mirii și Gazdele | 1024 | 896 | 576 | 320 |
| index · S6 — Ce ne întrebați cel mai des | 1024 | 896 | 576 | 320 |
| index · S7 — Rezervă Formație Nuntă | 1024 | 896 | 576 | 320 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 1024 | 1024 | 576 | 448 |
| oferte · S2 — Condiții comerciale | 1024 | 896 | 576 | 320 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 1024 | 896 | 576 | 320 |
| oferte · S4 — Acoperire | 1024 | 896 | 576 | 320 |
| oferte · S5 — Preț, rezervare și contract | 1024 | 896 | 576 | 320 |
| oferte · S6 — Verificați dacă data este liberă | 1024 | 640 | 576 | 64 |
| despre · S1 — Despre mine | 1024 | 1024 | 576 | 448 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 1024 | 896 | 576 | 320 |
| despre · S3 — Rădăcini | 1024 | 896 | 576 | 320 |
| despre · S4 — ca o frumoasă și de preț zestre, p | 1024 | 896 | 576 | 320 |
| despre · S5 — Primii pași | 1024 | 896 | 576 | 320 |
| despre · S6 — Hai să ne cunoaștem | 1024 | 640 | 576 | 64 |
| galerie · S1 — Galerie de Spectacole | 1024 | 896 | 576 | 320 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 1024 | 896 | 576 | 320 |
| galerie · S3 — Esența Tradiției în Imagini. | 1024 | 896 | 576 | 320 |
| discografie · S1 — Hai să nu ne mai mințim | 1024 | 896 | 576 | 320 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 1024 | 896 | 576 | 320 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1024 | 896 | 576 | 320 |
| faq · S1 — Ce ne întrebați cel mai des | 1024 | 220 | 576 | -356 |
| faq · S2 — Preț | 1024 | 704 | 576 | 128 |
| faq · S3 — Preț (#pret) | 1024 | 704 | 576 | 128 |
| faq · S4 — Rezervare și contract (#rezervare- | 1024 | 704 | 576 | 128 |
| faq · S5 — Prestația (#prestatia) | 1024 | 704 | 576 | 128 |
| faq · S6 — Tehnic și locație (#tehnic-si-loca | 1024 | 704 | 576 | 128 |
| faq · S7 — Deplasare (#deplasare) | 1024 | 704 | 576 | 128 |
| contact · S1 — div.absolute | 1024 | 1024 | 576 | 448 |
| contact · S2 — div.absolute | 1024 | 512 | 576 | -64 |
| contact · S3 — Rezervări și Contact Ioana Balan | 1024 | 359.33 | 576 | -216.67 |
| contact · S4 — Cere ofertă personalizată | 1024 | 512.67 | 576 | -63.33 |
| blog · S1 — Sfaturi și Inspirație pentru Eveni | 1024 | 589.33 | 576 | 13.33 |
| blog · S2 — Cum să alegi formația de nuntă per | 1024 | 316 | 576 | -260 |
| blog · S3 — Primește Noutăți | 1024 | 124 | 576 | -452 |
| blog · S4 — Tag-uri SEO | 1024 | 188 | 576 | -388 |
| articol · S1 — Importanța luminilor de scenă pent | 1024 | 896 | 576 | 320 |
| articol · S2 — "Lumina nu doar luminează, ea tran | 1024 | 589.33 | 576 | 13.33 |
| articol · S3 — Atmosfera și Dinamica Vizuală | 1024 | 768 | 576 | 192 |
| politica-cookie · S1 — [EXEMPLU] | 1024 | 528 | 576 | -48 |
| politica-cookie · S4 — cuprins | 1024 | 528 | 576 | -48 |
| termeni-si-conditii · S1 — [EXEMPLU] | 1024 | 528 | 576 | -48 |
| termeni-si-conditii · S4 — cuprins | 1024 | 528 | 576 | -48 |
| index · S1 — Muzică pentru nuntă, botez și corp | 768 | 640 | 576 | 64 |
| index · S2 — Pachete pentru 2026–2027 | 768 | 640 | 576 | 64 |
| index · S3 — Peste 15 ani pe scenă | 768 | 640 | 576 | 64 |
| index · S4 — Vezi cum arată un eveniment | 768 | 640 | 576 | 64 |
| index · S5 — Ce Spun Mirii și Gazdele | 768 | 640 | 576 | 64 |
| index · S6 — Ce ne întrebați cel mai des | 768 | 640 | 576 | 64 |
| index · S7 — Rezervă Formație Nuntă | 768 | 640 | 576 | 64 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 768 | 768 | 576 | 192 |
| oferte · S2 — Condiții comerciale | 768 | 640 | 576 | 64 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 768 | 640 | 576 | 64 |
| oferte · S4 — Acoperire | 768 | 640 | 576 | 64 |
| oferte · S5 — Preț, rezervare și contract | 768 | 640 | 576 | 64 |
| oferte · S6 — Verificați dacă data este liberă | 768 | 640 | 576 | 64 |
| despre · S1 — Despre mine | 768 | 768 | 576 | 192 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 768 | 640 | 576 | 64 |
| despre · S3 — Rădăcini | 768 | 640 | 576 | 64 |
| despre · S4 — ca o frumoasă și de preț zestre, p | 768 | 640 | 576 | 64 |
| despre · S5 — Primii pași | 768 | 640 | 576 | 64 |
| despre · S6 — Hai să ne cunoaștem | 768 | 640 | 576 | 64 |
| galerie · S1 — Galerie de Spectacole | 768 | 640 | 576 | 64 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 768 | 640 | 576 | 64 |
| galerie · S3 — Esența Tradiției în Imagini. | 768 | 640 | 576 | 64 |
| discografie · S1 — Hai să nu ne mai mințim | 768 | 720 | 576 | 144 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 768 | 720 | 576 | 144 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 768 | 640 | 576 | 64 |
| faq · S1 — Ce ne întrebați cel mai des | 768 | 220 | 576 | -356 |
| faq · S2 — Preț | 768 | 704 | 576 | 128 |
| faq · S3 — Preț (#pret) | 768 | 704 | 576 | 128 |
| faq · S4 — Rezervare și contract (#rezervare- | 768 | 704 | 576 | 128 |
| faq · S5 — Prestația (#prestatia) | 768 | 704 | 576 | 128 |
| faq · S6 — Tehnic și locație (#tehnic-si-loca | 768 | 704 | 576 | 128 |
| faq · S7 — Deplasare (#deplasare) | 768 | 704 | 576 | 128 |
| contact · S1 — div.absolute | 768 | 768 | 576 | 192 |
| contact · S3 — Rezervări și Contact Ioana Balan | 768 | 448 | 576 | -128 |
| contact · S4 — Cere ofertă personalizată | 768 | 640 | 576 | 64 |
| blog · S1 — Sfaturi și Inspirație pentru Eveni | 768 | 418.66 | 576 | -157.34 |
| blog · S2 — Cum să alegi formația de nuntă per | 768 | 306 | 576 | -270 |
| blog · S4 — Tag-uri SEO | 768 | 640 | 576 | 64 |
| articol · S1 — Importanța luminilor de scenă pent | 768 | 640 | 576 | 64 |
| articol · S2 — "Lumina nu doar luminează, ea tran | 768 | 418.66 | 576 | -157.34 |
| articol · S3 — Atmosfera și Dinamica Vizuală | 768 | 640 | 576 | 64 |
| articol · S4 — Plănuiți un eveniment? | 768 | 542 | 576 | -34 |
| politica-cookie · S1 — [EXEMPLU] | 768 | 528 | 576 | -48 |
| politica-cookie · S4 — cuprins | 768 | 528 | 576 | -48 |
| termeni-si-conditii · S1 — [EXEMPLU] | 768 | 528 | 576 | -48 |
| termeni-si-conditii · S4 — cuprins | 768 | 528 | 576 | -48 |
| index · S1 — Muzică pentru nuntă, botez și corp | 390 | 358 | 342 | 16 |
| index · S2 — Pachete pentru 2026–2027 | 390 | 358 | 342 | 16 |
| index · S3 — Peste 15 ani pe scenă | 390 | 358 | 342 | 16 |
| index · S4 — Vezi cum arată un eveniment | 390 | 358 | 342 | 16 |
| index · S5 — Ce Spun Mirii și Gazdele | 390 | 358 | 342 | 16 |
| index · S6 — Ce ne întrebați cel mai des | 390 | 358 | 342 | 16 |
| index · S7 — Rezervă Formație Nuntă | 390 | 358 | 342 | 16 |
| oferte · S1 — Pachete și prețuri pentru nuntă și | 390 | 390 | 342 | 48 |
| oferte · S5 — Preț, rezervare și contract | 390 | 358 | 342 | 16 |
| oferte · S6 — Verificați dacă data este liberă | 390 | 358 | 342 | 16 |
| despre · S1 — Despre mine | 390 | 390 | 342 | 48 |
| despre · S6 — Hai să ne cunoaștem | 390 | 358 | 342 | 16 |
| galerie · S1 — Galerie de Spectacole | 390 | 358 | 342 | 16 |
| galerie · S2 — Cum arată un eveniment (#clipuri) | 390 | 358 | 342 | 16 |
| galerie · S3 — Esența Tradiției în Imagini. | 390 | 358 | 342 | 16 |
| discografie · S1 — Hai să nu ne mai mințim | 390 | 358 | 342 | 16 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 390 | 358 | 342 | 16 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 390 | 358 | 342 | 16 |
| faq · S1 — Ce ne întrebați cel mai des | 390 | 220 | 342 | -122 |
| contact · S1 — div.absolute | 390 | 390 | 342 | 48 |
| contact · S3 — Rezervări și Contact Ioana Balan | 390 | 358 | 342 | 16 |
| contact · S4 — Cere ofertă personalizată | 390 | 358 | 342 | 16 |
| blog · S1 — Sfaturi și Inspirație pentru Eveni | 390 | 358 | 342 | 16 |
| blog · S2 — Cum să alegi formația de nuntă per | 390 | 356 | 342 | 14 |
| blog · S3 — Primește Noutăți | 390 | 294 | 342 | -48 |
| blog · S4 — Tag-uri SEO | 390 | 358 | 342 | 16 |
| articol · S1 — Importanța luminilor de scenă pent | 390 | 358 | 342 | 16 |
| articol · S2 — "Lumina nu doar luminează, ea tran | 390 | 358 | 342 | 16 |
| articol · S3 — Atmosfera și Dinamica Vizuală | 390 | 358 | 342 | 16 |
| articol · S4 — Plănuiți un eveniment? | 390 | 308 | 342 | -34 |
| politica-cookie · S1 — [EXEMPLU] | 390 | 294 | 342 | -48 |
| politica-cookie · S4 — cuprins | 390 | 302 | 342 | -40 |
| termeni-si-conditii · S1 — [EXEMPLU] | 390 | 294 | 342 | -48 |
| termeni-si-conditii · S4 — cuprins | 390 | 302 | 342 | -40 |

Total devieri de latime: **174**.

## E3. Gap de grila diferit de dominanta

| Pagina · sectiune | Viewport | gap x / y | norma | delta x | delta y |
|---|---|---|---|---|---|
| index · S1 — Muzică pentru nuntă, botez și corp | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S2 — Pachete pentru 2026–2027 | 1440 | 64px / 64px | 16px / 16px | 48 | 48 |
| index · S3 — Peste 15 ani pe scenă | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S4 — Vezi cum arată un eveniment | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S5 — Ce Spun Mirii și Gazdele | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S7 — Rezervă Formație Nuntă | 1440 | 32px / 32px | 16px / 16px | 16 | 16 |
| oferte · S2 — Condiții comerciale | 1440 | 10px / 4px | 16px / 16px | -6 | -12 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 1440 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S3 — Rădăcini | 1440 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S5 — Primii pași | 1440 | 64px / 64px | 16px / 16px | 48 | 48 |
| galerie · S3 — Esența Tradiției în Imagini. | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S1 — Hai să nu ne mai mințim | 1440 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 1440 | 32px / 32px | 16px / 16px | 16 | 16 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1440 | 48px / 48px | 16px / 16px | 32 | 32 |
| faq · S2 — Preț | 1440 | 8px / 8px | 16px / 16px | -8 | -8 |
| contact · S4 — Cere ofertă personalizată | 1440 | 40px / 40px | 16px / 16px | 24 | 24 |
| blog · S4 — Tag-uri SEO | 1440 | 8px / 8px | 16px / 16px | -8 | -8 |
| index · S1 — Muzică pentru nuntă, botez și corp | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S2 — Pachete pentru 2026–2027 | 1024 | 64px / 64px | 16px / 16px | 48 | 48 |
| index · S3 — Peste 15 ani pe scenă | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S4 — Vezi cum arată un eveniment | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S5 — Ce Spun Mirii și Gazdele | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S7 — Rezervă Formație Nuntă | 1024 | 32px / 32px | 16px / 16px | 16 | 16 |
| oferte · S2 — Condiții comerciale | 1024 | 10px / 4px | 16px / 16px | -6 | -12 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 1024 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S3 — Rădăcini | 1024 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S5 — Primii pași | 1024 | 64px / 64px | 16px / 16px | 48 | 48 |
| galerie · S3 — Esența Tradiției în Imagini. | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S1 — Hai să nu ne mai mințim | 1024 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 1024 | 32px / 32px | 16px / 16px | 16 | 16 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 1024 | 48px / 48px | 16px / 16px | 32 | 32 |
| faq · S2 — Preț | 1024 | 8px / 8px | 16px / 16px | -8 | -8 |
| contact · S4 — Cere ofertă personalizată | 1024 | 40px / 40px | 16px / 16px | 24 | 24 |
| blog · S4 — Tag-uri SEO | 1024 | 8px / 8px | 16px / 16px | -8 | -8 |
| index · S1 — Muzică pentru nuntă, botez și corp | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S2 — Pachete pentru 2026–2027 | 768 | 64px / 64px | 16px / 16px | 48 | 48 |
| index · S3 — Peste 15 ani pe scenă | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S4 — Vezi cum arată un eveniment | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S5 — Ce Spun Mirii și Gazdele | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S7 — Rezervă Formație Nuntă | 768 | 32px / 32px | 16px / 16px | 16 | 16 |
| oferte · S2 — Condiții comerciale | 768 | 10px / 4px | 16px / 16px | -6 | -12 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 768 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S3 — Rădăcini | 768 | 64px / 64px | 16px / 16px | 48 | 48 |
| despre · S5 — Primii pași | 768 | 64px / 64px | 16px / 16px | 48 | 48 |
| galerie · S3 — Esența Tradiției în Imagini. | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S1 — Hai să nu ne mai mințim | 768 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 768 | 32px / 32px | 16px / 16px | 16 | 16 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 768 | 48px / 48px | 16px / 16px | 32 | 32 |
| faq · S2 — Preț | 768 | 8px / 8px | 16px / 16px | -8 | -8 |
| contact · S4 — Cere ofertă personalizată | 768 | 40px / 40px | 16px / 16px | 24 | 24 |
| blog · S4 — Tag-uri SEO | 768 | 8px / 8px | 16px / 16px | -8 | -8 |
| index · S1 — Muzică pentru nuntă, botez și corp | 390 | 24px / 24px | 16px / 16px | 8 | 8 |
| index · S2 — Pachete pentru 2026–2027 | 390 | 40px / 40px | 16px / 16px | 24 | 24 |
| index · S3 — Peste 15 ani pe scenă | 390 | 40px / 40px | 16px / 16px | 24 | 24 |
| index · S7 — Rezervă Formație Nuntă | 390 | 24px / 24px | 16px / 16px | 8 | 8 |
| oferte · S2 — Condiții comerciale | 390 | 10px / 4px | 16px / 16px | -6 | -12 |
| oferte · S3 — Patru pachete, pentru nuntă și pen | 390 | 24px / 24px | 16px / 16px | 8 | 8 |
| despre · S2 — Numele meu este Ioana Balan. Sunt  | 390 | 40px / 40px | 16px / 16px | 24 | 24 |
| despre · S3 — Rădăcini | 390 | 40px / 40px | 16px / 16px | 24 | 24 |
| despre · S5 — Primii pași | 390 | 40px / 40px | 16px / 16px | 24 | 24 |
| galerie · S3 — Esența Tradiției în Imagini. | 390 | 48px / 48px | 16px / 16px | 32 | 32 |
| discografie · S1 — Hai să nu ne mai mințim | 390 | 24px / 24px | 16px / 16px | 8 | 8 |
| discografie · S2 — Arhiva Sonoră Ioana Balan | 390 | 32px / 32px | 16px / 16px | 16 | 16 |
| discografie · S3 — Îți place ce auzi? Rezervă data ta | 390 | 32px / 32px | 16px / 16px | 16 | 16 |
| faq · S2 — Preț | 390 | 8px / 8px | 16px / 16px | -8 | -8 |
| contact · S4 — Cere ofertă personalizată | 390 | 32px / 32px | 16px / 16px | 16 | 16 |
| blog · S4 — Tag-uri SEO | 390 | 8px / 8px | 16px / 16px | -8 | -8 |

Total devieri de gap: **70**.

## E4. Sectiuni fara antet complet

Antetul canonic e eyebrow → titlu → separator `motif-*`. Sectiuni carora le lipseste o parte:

| Pagina · sectiune | are eyebrow | are motif |
|---|---|---|
| index · S2 | da | **nu** |
| index · S3 | **nu** | **nu** |
| index · S4 | da | **nu** |
| index · S7 | **nu** | **nu** |
| oferte · S2 | **nu** | da |
| oferte · S3 | **nu** | da |
| oferte · S4 | da | **nu** |
| oferte · S6 | **nu** | **nu** |
| despre · S3 | **nu** | da |
| despre · S5 | **nu** | da |
| despre · S6 | **nu** | **nu** |
| galerie · S1 | da | **nu** |
| galerie · S2 | da | **nu** |
| galerie · S3 | **nu** | **nu** |
| discografie · S1 | **nu** | **nu** |
| discografie · S2 | **nu** | da |
| discografie · S3 | **nu** | **nu** |
| faq · S3 | **nu** | da |
| faq · S4 | **nu** | da |
| faq · S5 | **nu** | da |
| faq · S6 | **nu** | da |
| faq · S7 | **nu** | da |
| faq · S8 | **nu** | **nu** |
| contact · S3 | **nu** | **nu** |
| contact · S4 | **nu** | **nu** |
| blog · S1 | da | **nu** |
| blog · S2 | **nu** | **nu** |
| articol · S1 | **nu** | **nu** |
| articol · S3 | **nu** | **nu** |
| articol · S4 | **nu** | **nu** |
| politica-cookie · S2 | da | **nu** |
| politica-cookie · S5 | **nu** | **nu** |
| politica-cookie · S7 | **nu** | da |
| politica-cookie · S9 | **nu** | **nu** |
| politica-cookie · S11 | **nu** | **nu** |
| politica-cookie · S13 | **nu** | **nu** |
| politica-cookie · S15 | **nu** | da |
| politica-cookie · S17 | **nu** | **nu** |
| politica-cookie · S19 | **nu** | **nu** |
| politica-cookie · S21 | **nu** | **nu** |
| termeni-si-conditii · S2 | da | **nu** |
| termeni-si-conditii · S5 | **nu** | da |
| termeni-si-conditii · S7 | **nu** | **nu** |
| termeni-si-conditii · S9 | **nu** | **nu** |
| termeni-si-conditii · S11 | **nu** | da |
| termeni-si-conditii · S13 | **nu** | **nu** |
| termeni-si-conditii · S15 | **nu** | **nu** |
| termeni-si-conditii · S17 | **nu** | **nu** |
| termeni-si-conditii · S19 | **nu** | **nu** |
| termeni-si-conditii · S21 | **nu** | **nu** |
| termeni-si-conditii · S23 | **nu** | **nu** |
| termeni-si-conditii · S25 | **nu** | **nu** |
| termeni-si-conditii · S27 | **nu** | da |
| termeni-si-conditii · S29 | **nu** | **nu** |
| termeni-si-conditii · S31 | **nu** | da |
| termeni-si-conditii · S33 | **nu** | **nu** |
| termeni-si-conditii · S35 | **nu** | **nu** |

Total sectiuni cu antet incomplet: **57** din 64.

## E5. Tokeni de font care nu se aplica la mobil

Tokenii proprii (`font-display-*`, `font-headline-*`, `font-label-*`) poarta si `font-weight` si `line-height`, dar se aplica doar impreuna cu clasa de marime a tokenului. Unde markup-ul foloseste o marime arbitrara (`text-[28px]`) pe breakpoint-ul mic si tokenul (`md:text-headline-lg`) pe cel mare, la mobil raman `font-weight` si `line-height` mostenite de la `<body>`.

| Pagina | Element | clasa de marime | fw 1440 → 390 | lh 1440 → 390 | fs 390 | raport lh/fs la 390 |
|---|---|---|---|---|---|---|
| index | «Nuntă · Botez · Corporate» | `text-[12px]` | 600 → **400** | 20 → **24** | 12 | 2.00 |
| index | «Muzică pentru nuntă, botez și corp» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| index | «Oferte» | `text-[12px]` | 600 → **400** | 20 → **24** | 12 | 2.00 |
| index | «Pachete pentru 2026–2027» | `text-[32px]` | 500 → **400** | 56 → **40** | 32 | 1.25 |
| index | «Formație live, interpreți, DJ/MC ș» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| index | «Peste 15 ani pe scenă» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| index | «15+» | `text-[28px]` | 400 → **400** | 36 → **28** | 28 | 1.00 |
| index | «Ani pe scenă» | `text-[12px]` | 600 → **400** | 20 → **24** | 12 | 2.00 |
| index | «3» | `text-[28px]` | 400 → **400** | 36 → **28** | 28 | 1.00 |
| index | «Albume proprii» | `text-[12px]` | 600 → **400** | 20 → **24** | 12 | 2.00 |
| index | «Vezi cum arată un eveniment» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| index | «Ce Spun Mirii și Gazdele» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| index | «Ce ne întrebați cel mai des» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| index | «Prețul unei formații pentru 2026-2» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| index | «Cântați și în afara Bucureștiului?» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| index | «Cum rezerv data — avans și contrac» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| index | «Rezervă Formație Nuntă» | `text-[28px]` | 500 → **400** | 56 → **24** | 28 | 0.86 |
| index | «Disponibilă pentru nunți, botezuri» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| index | «+40 722 911 485» | `text-[20px]` | 500 → **400** | 32 → **24** | 20 | 1.20 |
| index | «Cere ofertă» | `text-[12px]` | 600 → **400** | 20 → **24** | 12 | 2.00 |
| oferte | «Preț, rezervare și contract» | `text-[28px]` | 500 → **400** | 40 → **42** | 28 | 1.50 |
| oferte | «Prețul unei formații pentru 2026-2» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| oferte | «Cum rezerv data — avans și contrac» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| oferte | «Cât este avansul și când se achită» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| oferte | «Cu cât timp înainte ar trebui să v» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| oferte | «Ce se întâmplă dacă trebuie să amâ» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| oferte | «Verificați dacă data este liberă» | `text-[28px]` | 500 → **400** | 56 → **35** | 28 | 1.25 |
| despre | «ca o frumoasă și de preț zestre, p» | `text-[26px]` | 400 → **400** | 45 → **33.80** | 26 | 1.30 |
| despre | «Hai să ne cunoaștem» | `text-[28px]` | 500 → **400** | 56 → **35** | 28 | 1.25 |
| discografie | «Hai să nu ne mai mințim» | `text-[36px]` | 500 → **400** | 56 → **45** | 36 | 1.25 |
| discografie | «Melodii noi Ioana Balan» | `text-[24px]` | 500 → **400** | 40 → **24** | 24 | 1.00 |
| discografie | «Hai să nu ne mai mințim» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Bărbățelul meu» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Fratele rămâne frate» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Ține minte omule» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Varsă țara lacrimi grele» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Dragoste mare» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Hai murgule-n vale» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Să merg la părinți acasă» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| discografie | «Arhiva Sonoră Ioana Balan» | `text-[28px]` | 500 → **400** | 40 → **24** | 28 | 0.86 |
| discografie | «Glasul Inimii» | `text-[24px]` | 500 → **400** | 40 → **24** | 24 | 1.00 |
| discografie | «Rădăcini» | `text-[24px]` | 500 → **400** | 40 → **24** | 24 | 1.00 |
| discografie | «Îți place ce auzi? Rezervă data ta» | `text-[26px]` | 500 → **400** | 40 → **24** | 26 | 0.92 |
| discografie | «Spuneți-ne data și locația — reven» | `text-[16px]` | 400 → **400** | 28 → **24** | 16 | 1.50 |
| faq | «Ce ne întrebați cel mai des» | `text-[30px]` | 500 → **400** | 56 → **37.50** | 30 | 1.25 |
| faq | «Preț» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| faq | «Prețul unei formații pentru 2026-2» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Rezervare și contract» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| faq | «Cum rezerv data — avans și contrac» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cât este avansul și când se achită» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Ce se întâmplă dacă trebuie să amâ» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cu cât timp înainte ar trebui să v» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Prestația» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| faq | «Ce tipuri de evenimente acoperă Io» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cât durează programul?» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Pot cere o piesă anume pentru un m» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cântați și muzică ușoară, sau doar» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Ce se întâmplă în pauzele formație» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Tehnic și locație» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| faq | «Ce echipament aduceți și ce trebui» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «De cât spațiu aveți nevoie pentru » | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cântați și la evenimente în aer li» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Aveți nevoie de masă pentru formaț» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Deplasare» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| faq | «Cântați și în afara Bucureștiului?» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Cum se calculează costul deplasări» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Ce se întâmplă la distanțe mari, u» | `text-[16px]` | 500 → **400** | 32 → **22** | 16 | 1.38 |
| faq | «Nu ați găsit răspunsul?» | `text-[26px]` | 500 → **400** | 56 → **32.50** | 26 | 1.25 |
| blog | «Sfaturi și Inspirație pentru Eveni» | `text-[32px]` | 400 → **400** | 61.60 → **35.20** | 32 | 1.10 |
| politica-cookie | «Politica de cookie-uri» | `text-[30px]` | 500 → **400** | 56 → **37.50** | 30 | 1.25 |
| politica-cookie | «1. Ce sunt cookie-urile» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «2. Temeiul legal» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «3. Ce cookie-uri folosim» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «3.1 Cookie-uri strict necesare» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| politica-cookie | «3.2 Cookie-uri de analiză» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| politica-cookie | «3.3 Cookie-uri de publicitate» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| politica-cookie | «4. Conținut încorporat de la terți» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «5. Cum vă puteți retrage consimțăm» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «6. Cum puteți controla cookie-uril» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «7. Drepturile dumneavoastră» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «8. Modificarea acestei politici» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| politica-cookie | «9. Contact» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «Termeni și condiții» | `text-[30px]` | 500 → **400** | 56 → **37.50** | 30 | 1.25 |
| termeni-si-conditii | «1. Identificarea operatorului» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «2. Obiectul site-ului» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «3. Acceptarea termenilor» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «4. Informațiile publicate. Prețuri» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «5. Rezervarea și încheierea contra» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «6. Deplasarea» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «7. Modificarea și anularea rezervă» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «8. Drepturi de proprietate intelec» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «9. Materiale audio-video de la eve» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «10. Limitarea răspunderii» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «11. Linkuri către site-uri terțe» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «12. Prelucrarea datelor cu caracte» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «12.1 Operatorul» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.2 Ce date prelucrăm, în ce scop» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.3 Cui transmitem datele» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.4 Transferuri în afara Spațiulu» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.5 Drepturile dumneavoastră» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.6 Dreptul de a depune plângere» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «12.7 Caracterul obligatoriu al fur» | `text-[20px]` | 500 → **400** | 32 → **30** | 20 | 1.50 |
| termeni-si-conditii | «13. Cookie-uri» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «14. Soluționarea litigiilor» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «15. Modificarea termenilor» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |
| termeni-si-conditii | «16. Contact» | `text-[24px]` | 500 → **400** | 40 → **30** | 24 | 1.25 |

Total elemente afectate: **106**.

Dintre ele, **8** ajung la 390px cu `line-height` **mai mic decat `font-size`** (raport sub 1,00), adica randurile se ating daca textul trece pe doua randuri:

- discografie — «Arhiva Sonoră Ioana Balan», raport 0.86
- index — «Ce Spun Mirii și Gazdele», raport 0.86
- index — «Ce ne întrebați cel mai des», raport 0.86
- index — «Muzică pentru nuntă, botez și corporate», raport 0.86
- index — «Peste 15 ani pe scenă», raport 0.86
- index — «Rezervă Formație Nuntă», raport 0.86
- index — «Vezi cum arată un eveniment», raport 0.86
- discografie — «Îți place ce auzi? Rezervă data ta.», raport 0.92

