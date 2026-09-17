# Inventarul imaginilor primite pe WhatsApp (2026-09-14)

Fișierele brute din `assets/img/`, primite de la clientă pe WhatsApp. Numele sunt cele
generate de WhatsApp. Inventariate pe 2026-09-17, fiecare deschisă și descrisă.

**Stare:** netrackuite în git. Intră în repo doar cele folosite, redenumite descriptiv și
convertite (WebP + JPEG), ca `ioana-balan-portret-dantela-rosie`. Aici nu se mapează
nimic pe pagini. Sloturile propuse sunt punct de plecare, nu decizie.

Prefixul comun `WhatsApp Image 2026-09-14 at` e omis din tabel.

---

## Trei constatări de păstrat

**1. `15.56.17 1111` — persoană de confirmat. NU SE FOLOSEȘTE.** Captură de story (cu
benzi de interfață sus și jos), ie albă cu broderie neagră, fustă de tul neagră. Trăsăturile
par altele decât în portretele de referință (CLAUDE.md §10). Nu intră pe nicio pagină până
când clienta confirmă că e ea.

**2. Duplicate: `17.40.15 4` și `17.40.15`.** md5 identic
(`175d5b4ec9909d3c590ff2ad21574d39`). Rămâne `17.40.15`, iar `17.40.15 4` iese din
inventar. Fișierul nu s-a șters de pe disc.

**3. Corecție la identificarea din brief.** `15.56.17 8` nu e portret de studio, ci
fotografie live, noaptea, sub ghirlande de becuri. Portretul de studio (fundal alb, rochie
neagră, microfon în mână) e `15.56.17 11111`.

---

## Deja folosită

| Fișier original | Redenumit | px | Unde |
|---|---|---|---|
| `15.56.17 1111111` | `ioana-balan-portret-dantela-rosie` | 1200×1600 | `index.html`, hero |

Selfie: bluză roșie din dantelă cu volane și guler de satin, mâna ridicată spre obiectiv în
semnul V, cercei geometrici din romburi, interior neclar pe fundal. Portretul anterior din
hero, `ioana-balan-ie-cosita-impletita`, a trecut în `galerie.html`, în locul
`formatie-ring-dans`.

---

## Inventar

„Acord” = persoane identificabile în cadru, altele decât artista (miri, invitați,
muzicieni). CLAUDE.md §10 explică de ce contează: o fotografie de la un eveniment, într-o
galerie care poartă numele artistei. „Localitate” contează doar pentru sloturile de zonă.

| Fișier | px | Orientare | Ce se vede | Slot propus | Ce lipsește |
|---|---|---|---|---|---|
| `16.20.59 7` | 960×720 | peisaj | Horă mare văzută de sus, sală cu candelabre, fum de scenă albastru. Artista nu e identificabilă. | `folclor-si-manele` sau hub-ul `zone` | acordul invitaților (fețe vizibile în prim-plan); rezoluție: 960px, sub minimul de 1440px din A8 |
| `15.56.17 11` | 1200×800 | peisaj | Primul dans al mirilor în fum greu, sală clasică cu candelabru, formația pe scenă. Solista e departe, în centru, în rochie albă cu roșu. | `nunta.html` | acordul mirilor; confirmarea că solista din cadru e Ioana (prea mică pentru verificare); rezoluție: 1200px, sub 1440 |
| `15.56.17 9` | 1600×1446 | peisaj (aproape pătrat, 1,11) | Artista în negru cu broderie argintie, pe ringul de dans. În spate formația: saxofon, vioară, acordeon, DJ. Lumini violet. | `formatia.html` | confirmarea că instrumentiștii sunt formația ei (cerută explicit de A87); acordul muzicienilor; raportul 1,11 cere decupaj într-o bandă peisaj |
| `15.56.17 111111` | 750×500 | peisaj | Cântă pe scenă: bluză albă cu dantelă, fustă roșie, brâu. Formația în spate (clape, DJ). | `repertoriu.html`, **la limita de rezoluție**: 750px față de 1440 cerut de A86 | rezoluție; acordul muzicienilor identificabili |
| `7` (`7.jpeg`) | 1600×1200 | peisaj | Cântă printre invitați, noaptea, în exterior (pavilion alb, piscină, ghirlande de becuri). Costum negru cu broderie argintie. | de mapat după localitate | localitate; acordul invitaților din prim-plan (bărbat în cămașă albă, femeie în rochie roșie cu flori) |
| `15.56.17 8` | 1200×1600 | portret | Același eveniment ca `7`: cântă la microfon, cu un braț ridicat, sub ghirlande. Invitați estompați în fundal. **Nu e portret de studio** (constatarea 3). | de mapat după localitate | localitate |
| `15.56.17 11111` | 1075×1600 | portret | Portret de studio: fundal alb neutru, rochie neagră cu volane, colier metalic mare, microfon în mână. | de mapat | nimic de persoană sau de acord; localitatea nu e relevantă |
| `15.56.17 1111` | 750×1334 | portret | Captură de story: ie albă cu broderie neagră, fustă de tul neagră, sprijinită de un fotoliu, în exterior. | **NU SE FOLOSEȘTE** | **confirmarea persoanei** (constatarea 1); captura are benzi de interfață, deci cere decupaj |
| `17.40.14 5` | 1066×1599 | portret | Cântă în prim-plan stânga, lângă mirii care dansează. Sală albă, lumină violet. | de mapat după localitate | localitate; acordul mirilor și al invitaților |
| `17.40.14 6` | 1374×1168 | peisaj | Aceeași nuntă, cadru larg: mirii din spate, alt cuplu dansând, invitați care filmează. Artista cântă în dreapta. | de mapat după localitate | localitate; acordul invitaților; rezoluție: 1374px, sub 1440 |
| `17.40.15 2` | 1278×1600 | portret | Cântă în prim-plan, între doi invitați care dansează. În spate: saxofon, acordeon, lumini de scenă. | de mapat după localitate | localitate; acordul celor doi invitați (clar identificabili) |
| `17.40.15 3` | 1066×1600 | portret | Mirii în prim-plan. Solista cântă în dreapta, cu acordeonist în spate. | de mapat după localitate | localitate; acordul mirilor; confirmarea persoanei: aceeași ținută ca în `17.40.15 2`, dar părul citește mai deschis sub lumina de scenă |
| `17.40.15` | 1066×1600 | portret | Mirii dansează. Solista cântă în stânga, violonistul în dreapta, rampă de lumini deasupra. | de mapat după localitate | localitate; acordul mirilor și al violonistului |

Seria `17.40.*` e aceeași nuntă (aceeași sală, aceiași miri, aceeași ținută neagră). Seria
`7` + `15.56.17 8` e același eveniment în exterior.

---

## Ce nu se face cu ele

- **Sloturile `.ph-zone` de pe `zona-brasov` și `zona-constanta` rămân goale.** Cer
  fotografie din județ (A57–A72), iar pentru nicio imagine de aici nu se știe unde s-a
  făcut.
- Nicio imagine nu se leagă de un județ sau de un eveniment într-o legendă ori într-un
  `alt` fără localitatea confirmată.
- Maparea pe secțiuni se face după răspunsurile clientei: localități, acorduri, `15.56.17 1111`.
