"""4.4 — Integritate: blocuri protejate, ținte relative, JSON-LD, interdicții.

Referința pentru blocurile protejate e zona-brasov.html (șablonul A).
Separat: footer-ul celor 11 pagini din rădăcină, comparat între ele, cu excepția
temporară FOOTER_DEMO.
"""
import json
import os
import re
import sys
from urllib.parse import unquote, urldefrag

from _common import ALL_PAGES, MOCKUP, OLD_PAGES, ROOT, read, soup

REFERENCE = "zona-brasov.html"

PROTECTED = {
    "robots": r'<meta name="robots" content="noindex, follow">',
    "head-assets": r'<link rel="preload".*?<link rel="stylesheet" href="\.\./assets/styles\.css">',
    "style": r"<style>.*?</style>",
    "header": r"<!-- TopNavBar -->.*?</header>",
    "drawer": r"<!-- Mobile Side Drawer \(canonic\) -->.*?</nav>\n</div>\n</div>",
    "legendă": r"<!-- Legenda de placeholder.*?</div>\n</div>",
    "footer": r"<!-- Footer -->.*?</footer>",
    "scripturi+whatsapp": r"</footer>.*",
    "canonical-comentat": r'<link rel="canonical" href="https://ioana-balan\.ro/______\.html"> -->',
}

FORBIDDEN = {
    "aggregateRating": r"aggregateRating",
    "Material Symbols": r"(?i)material[ -]symbols",
    "localStorage": r"localStorage",
    "offers/price în JSON-LD": None,  # verificat separat, doar în JSON-LD
}

# --- Footer-ul paginilor din rădăcină -----------------------------------------
# Paginile din rădăcină au propria familie de footer: aceleași clase ca în
# zone-mockup/, dar căi fără `../` și fără „Zone deservite” (href="#" pe paginile
# noi). De aceea nu se compară cu zona-brasov.html, ci între ele.
#
# EXCEPȚIE TEMPORARĂ — SE ȘTERGE LA MIGRARE.
# index.html are footer-ul de DEMONSTRAȚIE pentru client (2026-09-17, cerere client,
# demonstrație de structură pentru NAV-FOOTER-MIGRARE.md §2): coloanele „Servicii”
# și „Repertoriu”, „Zone deservite” către hub și „Blog”. Celelalte 10 pagini din
# rădăcină și cele 20 din zone-mockup/ rămân pe footer-ul canonic până la migrare.
# La migrare footer-ul devine un template unic în Elementor, iar FOOTER_DEMO se
# golește. Dacă footer-ul de pe o pagină din FOOTER_DEMO revine la cel canonic,
# verificarea pică: excepția a expirat și trebuie scoasă de aici.
FOOTER_DEMO = {"index.html"}
FOOTER_RE = re.compile(r"<footer\b.*?</footer>", re.S)

COLOR_RE = re.compile(r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)")


def block(src, pattern):
    m = re.search(pattern, src, re.S)
    return m.group(0) if m else None


def ids_of(path):
    return set(re.findall(r'\bid="([^"]+)"', open(path, encoding="utf-8").read()))


def check_links(page):
    errors = []
    doc = soup(page)
    base = MOCKUP
    own_ids = ids_of(os.path.join(MOCKUP, page))
    targets = []
    for tag in doc.find_all(True):
        for attr in ("href", "src"):
            if tag.has_attr(attr):
                targets.append(tag[attr])
        if tag.has_attr("srcset"):
            targets += [part.strip().split()[0] for part in tag["srcset"].split(",")]
    for t in targets:
        if re.match(r"^(https?:|mailto:|tel:|data:|//)", t):
            continue
        url, frag = urldefrag(t)
        if not url:
            if frag and frag not in own_ids:
                errors.append(f"ancoră inexistentă: {t}")
            continue
        path = os.path.normpath(os.path.join(base, unquote(url)))
        if not os.path.exists(path):
            errors.append(f"țintă lipsă: {t}")
        elif frag and path.endswith(".html") and frag not in ids_of(path):
            errors.append(f"ancoră inexistentă în țintă: {t}")
    return errors, len(targets)


def jsonld_keys(node):
    if isinstance(node, dict):
        for k, v in node.items():
            yield k
            yield from jsonld_keys(v)
    elif isinstance(node, list):
        for v in node:
            yield from jsonld_keys(v)


def check_root_footers():
    """Footer-ul celor 11 pagini din rădăcină: identic între ele, cu FOOTER_DEMO ca excepție."""
    footers = {}
    for page in OLD_PAGES:
        m = FOOTER_RE.search(open(os.path.join(ROOT, page), encoding="utf-8").read())
        footers[page] = m.group(0) if m else None
    canonical_pages = [p for p in OLD_PAGES if p not in FOOTER_DEMO]
    canonical = footers[canonical_pages[0]]
    failures = 0
    print(f"\nFooter — paginile din rădăcină (referință: {canonical_pages[0]}; "
          f"excepție temporară: {', '.join(sorted(FOOTER_DEMO)) or 'niciuna'}):")
    for page in OLD_PAGES:
        f = footers[page]
        if f is None:
            verdict, bad = "footer lipsă", True
        elif page in FOOTER_DEMO:
            if f == canonical:
                verdict, bad = "EXCEPȚIE EXPIRATĂ: footer identic cu cel canonic, scoate pagina din FOOTER_DEMO", True
            else:
                verdict, bad = "diferit — footer de demonstrație, excepție temporară (FOOTER_DEMO)", False
        else:
            verdict, bad = ("identic" if f == canonical else "DIFERIT față de footer-ul canonic"), f != canonical
        failures += bad
        print(f"  {page:26} {verdict}")
    print(f"Pagini din rădăcină cu problemă de footer: {failures}")
    return failures


def main():
    ref = read(REFERENCE)
    ref_colors = set(c.lower() for c in COLOR_RE.findall(ref))
    failures = 0
    for page in ALL_PAGES:
        src = read(page)
        problems = []
        for name, pattern in PROTECTED.items():
            a, b = block(ref, pattern), block(src, pattern)
            if b is None:
                problems.append(f"bloc lipsă: {name}")
            elif a != b:
                problems.append(f"bloc diferit: {name}")
        link_errors, n_targets = check_links(page)
        problems += link_errors
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', src, re.S)
        if not blocks:
            problems.append("JSON-LD lipsă")
        for raw in blocks:
            try:
                data = json.loads(raw)
                keys = set(jsonld_keys(data))
                for k in ("aggregateRating", "offers", "price", "priceRange"):
                    if k in keys:
                        problems.append(f"JSON-LD conține {k}")
            except json.JSONDecodeError as exc:
                problems.append(f"JSON-LD neparsabil: {exc}")
        # Interdicțiile se caută în cod, nu în comentariile care le documentează
        # („Fără `aggregateRating`: scos deliberat…").
        code = re.sub(r"/\*.*?\*/", "", re.sub(r"<!--.*?-->", "", src, flags=re.S), flags=re.S)
        for name, pattern in FORBIDDEN.items():
            if pattern and re.search(pattern, code):
                problems.append(f"interzis: {name}")
        new_colors = sorted(set(c.lower() for c in COLOR_RE.findall(src)) - ref_colors)
        if new_colors:
            problems.append(f"culori noi: {new_colors}")
        if re.search(r"-\[#|-\[rgb", src):
            problems.append("culoare arbitrară Tailwind")
        if 'content="noindex, follow"' not in src:
            problems.append("noindex lipsă")
        failures += bool(problems)
        print(f"{page:22} ținte={n_targets:>3}  JSON-LD={len(blocks)}  " + ("ok" if not problems else "PROBLEME"))
        for p in problems:
            print(f"    · {p}")
    print(f"\nPagini cu probleme: {failures}")
    root_failures = check_root_footers()
    return 1 if failures or root_failures else 0


if __name__ == "__main__":
    sys.exit(main())
