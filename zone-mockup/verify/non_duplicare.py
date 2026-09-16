"""4.2 — Non-duplicare, în două treceri: text brut și text cu toponime mascate.

Pentru fiecare pereche ordonată (A, B) se calculează, pe fiecare bloc /
propoziție din A, cea mai bună potrivire din B:

  paragraf   — SequenceMatcher pe tokeni, bloc cu bloc (blocuri ≥ 6 tokeni)
  propoziție — SequenceMatcher pe tokeni, propoziție cu propoziție (≥ 8 tokeni)
  shingle-6  — ce fracție din secvențele de 6 cuvinte ale blocului din A apare
               oriunde în B (prinde un paragraf lipit dintr-un altul mai lung)

Setul de perechi e matricea completă: fiecare dintre cele 20 de pagini noi față
de celelalte 19 (20 × 20) și față de cele 11 pagini existente (20 × 11). Până
la runda a șaptea, scriptul rula o listă de perechi alese de mână, în care
paginile de zonă nu erau comparate între ele.

Eșec (cod 1):
  - orice potrivire > 85%, pe orice pereche;
  - orice potrivire > 75% între două pagini de zonă (același rol structural).
Potrivirile între 75% și 85% pe celelalte perechi se listează, fără eșec.

Semnalări separate, fără eșec: maxime sistematic > 75% ale repertoriu.html față
de zone; nunta.html > 75% față de ../index.html sau ../oferte.html (ar fi a
treia pagină despre nuntă).

Scoase înainte de comparație (vezi _common.content_blocks): comentarii,
scripturi, marcajele .ph și .ph-zone, legenda de placeholder, plus:
  - recenziile (`figure blockquote`, `figure figcaption`) — citate verbatim,
    identice intenționat cu cele de pe ../index.html;
  - `.nota-productie` — instrucțiuni de producție, nu text de pagină;
  - linkurile de interfață (butoane în afara unui p/li/heading). Linkurile din
    fraze rămân comparate.
"""
import os
import re
import sys
from difflib import SequenceMatcher
from functools import lru_cache

from _common import ALL_PAGES, MOCKUP, OLD_PAGES, ROOT, ZONE_PAGES, content_blocks, mask, tokens

REPORT = 0.85
SYSTEMIC = 0.75
PREFILTER = 0.50
# Recenzii Google citate verbatim (text reprodus identic) și note de producție.
EXCLUDED = ("figure blockquote", "figure figcaption", ".nota-productie")


def sentences(block):
    return [s for s in re.split(r"(?<=[.!?;])\s+|\s+—\s+", block) if s.strip()]


@lru_cache(maxsize=None)
def prep(page, masked):
    blocks = content_blocks(page, drop=EXCLUDED, ui_links=False)
    tf = (lambda t: mask(tokens(t))) if masked else tokens
    blk = [(b, tf(b)) for b in blocks]
    snt = [(s, tf(s)) for b in blocks for s in sentences(b)]
    return [x for x in blk if len(x[1]) >= 6], [x for x in snt if len(x[1]) >= 8], blk


def best(items_a, items_b):
    """Pentru fiecare element din A, cea mai bună potrivire în B."""
    out = []
    for text_a, ta in items_a:
        top = (0.0, None)
        for text_b, tb in items_b:
            sm = SequenceMatcher(None, ta, tb, autojunk=False)
            if sm.real_quick_ratio() < max(PREFILTER, top[0]) or sm.quick_ratio() < max(PREFILTER, top[0]):
                continue
            r = sm.ratio()
            if r > top[0]:
                top = (r, text_b)
        out.append((top[0], text_a, top[1]))
    return out


def shingles(toks, n=6):
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def containment(blocks_a, all_b):
    pool = set()
    for _, tb in all_b:
        pool |= shingles(tb)
    out = []
    for text_a, ta in blocks_a:
        sh = shingles(ta)
        if len(sh) >= 3:
            out.append((len(sh & pool) / len(sh), text_a, None))
    return out


def compare(a, b, masked):
    ba, sa, _ = prep(a, masked)
    bb, sb, allb = prep(b, masked)
    res = {
        "paragraf": best(ba, bb),
        "propoziție": best(sa, sb),
        "shingle-6": containment(ba, allb),
    }
    return res


def rel(path):
    return os.path.relpath(path, MOCKUP) if os.path.isabs(path) else path


METRICS = ("paragraf", "propoziție", "shingle-6")


def short(page):
    return os.path.basename(page).replace(".html", "").replace("zona-", "z-")


def main():
    assert len(ALL_PAGES) == 20, ALL_PAGES
    old = [os.path.join(ROOT, p) for p in OLD_PAGES]
    pairs = [(a, b) for a in ALL_PAGES for b in ALL_PAGES if b != a] + [(a, b) for a in ALL_PAGES for b in old]

    pair_max = {}   # (a, b) -> {trecere: {metrică: maxim}}
    hits, band = [], []
    for a, b in pairs:
        for masked in (False, True):
            label = "mascat" if masked else "brut"
            res = compare(a, b, masked)
            pair_max.setdefault((a, rel(b)), {})[label] = {k: max((r[0] for r in v), default=0.0) for k, v in res.items()}
            for k, rows in res.items():
                for score, ta, tb in rows:
                    if score > REPORT:
                        hits.append((a, rel(b), label, k, score, ta, tb))
                    elif score > SYSTEMIC:
                        band.append((a, rel(b), label, k, score, ta, tb))

    top = {ab: max(max(m.values()) for m in v.values()) for ab, v in pair_max.items()}

    cols = ALL_PAGES + [rel(p) for p in old]
    print("Maxime per pereche (rând = A, coloană = B), cea mai mare valoare din trei metrici × două treceri.")
    print("'-' = sub 50% (prefiltru); '·' = aceeași pagină.\n")
    for i, c in enumerate(cols):
        print(f"  [{i:2}] {short(c)}")
    print("\n" + " " * 20 + "".join(f"{i:>4}" for i in range(len(cols))))
    for a in ALL_PAGES:
        cells = []
        for c in cols:
            if c == a:
                cells.append("   ·")
            else:
                v = top[(a, c)]
                cells.append(f"{v * 100:4.0f}" if v >= PREFILTER else "   -")
        print(f"{short(a):20}" + "".join(cells))

    def show(rows):
        for a, b, label, k, score, ta, tb in sorted(rows, key=lambda r: -r[4]):
            print(f"\n  {a} ↔ {b} [{label}, {k}] {score:.1%}\n    A: {ta}\n    B: {tb or '(shingles)'}")

    print(f"\nPotriviri > {REPORT:.0%}: {len(hits)}")
    show(hits)
    print(f"\nPotriviri între {SYSTEMIC:.0%} și {REPORT:.0%}: {len(band)}")
    show(band)

    zone_zone = sorted((ab, v) for ab, v in top.items() if ab[0] in ZONE_PAGES and ab[1] in ZONE_PAGES and v > SYSTEMIC)
    print(f"\nPerechi zonă ↔ zonă peste {SYSTEMIC:.0%}: {len(zone_zone)}")
    for (a, b), v in zone_zone:
        print(f"  {a} ↔ {b}: {v:.1%}")

    above = sorted(z for z in ZONE_PAGES if top[("repertoriu.html", z)] > SYSTEMIC)
    print(f"\nPagini de zonă cu maxim > {SYSTEMIC:.0%} față de repertoriu.html: {len(above)}/{len(ZONE_PAGES)}"
          + (f" — {', '.join(above)}" if above else ""))
    if len(above) >= len(ZONE_PAGES) // 2:
        print("ATENȚIE: maxime sistematic peste 75% — repertoriul repetă în loc să extindă.")

    print(f"\nnunta.html — maxime față de paginile existente despre nuntă (prag {SYSTEMIC:.0%}):")
    third = False
    for b in ("../index.html", "../oferte.html"):
        for label, mx in pair_max[("nunta.html", b)].items():
            t = max(mx.values())
            third |= t > SYSTEMIC
            fmt = lambda k: f"{mx[k]:.1%}" if mx[k] >= PREFILTER or k == "shingle-6" else "<50%"
            print(f"  {b:22} {label:7} " + " · ".join(f"{k} {fmt(k)}" for k in METRICS)
                  + f"  → {'PESTE 75%' if t > SYSTEMIC else 'sub prag'}")
    if third:
        print("ATENȚIE: nunta.html stă peste 75% — ar fi a treia pagină despre nuntă.")

    return 1 if hits or zone_zone else 0


if __name__ == "__main__":
    sys.exit(main())
