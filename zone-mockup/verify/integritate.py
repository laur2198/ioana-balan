"""4.4 — Integritate: blocuri protejate, ținte relative, JSON-LD, interdicții.

Referința pentru blocurile protejate e zona-brasov.html (șablonul A).
"""
import json
import os
import re
import sys
from urllib.parse import unquote, urldefrag

from _common import ALL_PAGES, MOCKUP, read, soup

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
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
