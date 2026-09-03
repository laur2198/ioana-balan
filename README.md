# ioana-balan.ro — machete redesign

Prototip static de validare pentru site-ul **ioana-balan.ro** (artist / formație
nuntă & evenimente). Cele 8 pagini sunt machete generate cu **Stitch** și servesc
la validarea vizuală a redesign-ului cu clientul. După aprobare, vor fi
**reimplementate în WordPress/Elementor** — codul de aici este de unică folosință,
**nu este cod de producție**.

## Stack actual

- **HTML static** — fiecare pagină este un fișier standalone.
- **Tailwind CSS via CDN** (`https://cdn.tailwindcss.com`), cu config inline în fiecare pagină.
- Fonturi Google (EB Garamond) + Material Symbols, încărcate de la CDN.
- Fără build tools, fără backend, fără dependențe npm.

## Scop

Prototip de **validare cu clientul** — se deschide direct în browser (nu necesită
server). Nu este optimizat pentru producție și nu este destinat indexării/live.

## Pagini

| Fișier             | Pagină                    |
|--------------------|---------------------------|
| `index.html`       | Acasă                     |
| `galerie.html`     | Galerie                   |
| `discografie.html` | Discografie               |
| `servicii.html`    | Servicii                  |
| `oferte.html`      | Oferte / Pachete          |
| `contact.html`     | Contact                   |
| `blog.html`        | Blog (listă articole)     |
| `articol.html`     | Articol (pagină single)   |

> Fragmentele de export WordPress livrate de client (fostul `_stitch-export/`:
> header/footer HTML, `styles.css`, export pagină Discografie) au fost eliminate
> din repo — nu făceau parte din cele 8 pagini și conțineau date de contact
> greșite. Se pot recupera din istoricul git, în commit-ul baseline `8026eb9`.

## Cum se rulează

Se deschide orice `.html` direct în browser. Opțional, un server static local:

```bash
python3 -m http.server 8000
# apoi http://localhost:8000
```

## Probleme cunoscute

Machetele au fost livrate brute (commit-ul baseline). Următoarele inconsistențe
au fost identificate; unele sunt/vor fi rezolvate în commit-uri ulterioare, altele
sunt lăsate intenționat pentru decizia clientului:

- **Navigație inconsistentă** între pagini (rezolvat ulterior):
  - `discografie.html` are doar 4 itemi (lipsesc Servicii, Oferte).
  - `blog.html` are 7 itemi (item „Blog" în plus).
  - `servicii.html` / `contact.html` folosesc etichete diferite („Servicii
    Evenimente", „Pachete", „Oferte și Pachete").
  - `articol.html` are meniul în **engleză** (Home, Gallery, Services…).
  - Majoritatea linkurilor sunt `href="#"`; doar `galerie.html` are linkuri reale.
- **Date de contact inconsistente** (se normalizează după confirmarea clientului):
  - Email: `ioanablanoficial@gmail.com` (typo, lipsă „a", 8 apariții),
    `ioanabalanoficial@gmail.com` (corect, 1 apariție), `contact@ioanabalan.ro`
    (2 apariții), plus placeholder `EMAIL@DOMAIN.COM` în `contact.html`.
  - Telefon în formate diferite: `+40722911485`, `40722911485`, `0722 911 485`,
    `+40 722 911 485`, `tel:+40722911485`, `tel:0722911485`.
  - Instagram: URL malformat în `galerie.html` (`instagram.com/@iamioanabalan`).
  - Facebook: `www.facebook.com` vs `facebook.com`.
- **An copyright inconsistent**: `© 2024` (articol, blog), `© 2010-2026`
  (5 pagini), `© 2010-2027` (oferte).
- **Tailwind via CDN** — nepotrivit pentru producție (fără purge/build);
  acceptabil doar pentru prototip.
- **Linkuri externe reziduale** în unele pagini (`grand-music.ro`,
  `oferta-nunta.ro`, `muzica-nunta.ro`) — de revizuit la reimplementare.
- **Formulare fără backend** — formularul de contact/booking nu trimite date
  (se rezolvă în WordPress).

## Ce NU se face în această fază

Culorile, fonturile și imaginile rămân **neschimbate**. Nu se adaugă build tools
(Vite/Astro etc.) — proiectul rămâne HTML static. Backend-ul pentru formulare se
implementează în WordPress.
