"""Audit de cuvinte cheie: cele 11 pagini existente față de cele 20 noi.

Raport, nu verificare: nu intră în run_all.sh și nu întoarce cod de eroare.

  --campuri   title, h1, meta description, description din JSON-LD, h2, h3,
              verdictul bag-of-words și termenii clientului, per pagină (JSON)
  --matrice   non-duplicare 20 noi × 11 vechi, brut și mascat; toate maximele
              pe pereche și fiecare potrivire > 85%

Paginile vechi se citesc din rădăcina repo-ului. Pentru ele, bag-of-words
folosește aceeași funcție ca bag_of_words.py; toponimele sunt aceleași.
"""
import json
import os
import re
import sys

from _common import ALL_PAGES, MOCKUP, OLD_PAGES, ROOT, find_toponyms, jsonld, read, soup, tokens
from bag_of_words import PREPOSITIONS, descriptions

# Termenii clientului, pliați. Fiecare se caută ca secvență de tokeni, cu
# plural/articol tolerat pe ultimele litere (formatie/formatii/formatia,
# nunta/nunti/nuntii).
CLIENT_TERMS = {
    "formatie nunta": [("formati",), ("nunt",)],
    "oferta formatie nunta": [("ofert",), ("formati",), ("nunt",)],
    "recomandari formatii nunta": [("recomand",), ("formati",), ("nunt",)],
    "top formatii nunta": [("top",), ("formati",), ("nunt",)],
    "formatie folclor si manele": [("formati",), ("folclor",), ("si",), ("manel",)],
    "formatie muzica de petrecere": [("formati",), ("muzic",), ("de",), ("petrecer",)],
}


def path_of(page):
    return os.path.join(ROOT, page) if page in OLD_PAGES else os.path.join(MOCKUP, page)


def term_positions(toks, pattern, gap=2):
    """Secvența în ordine, cu cel mult `gap` tokeni intercalați între elemente
    (prinde „formație de nuntă", „formația pentru nunta ta")."""
    hits = []
    for i, t in enumerate(toks):
        if not t.startswith(pattern[0][0]):
            continue
        j, ok = i, True
        for (stem,) in pattern[1:]:
            nxt = next((k for k in range(j + 1, min(len(toks), j + 2 + gap)) if toks[k].startswith(stem)), None)
            if nxt is None:
                ok = False
                break
            j = nxt
        if ok:
            hits.append(" ".join(toks[i:j + 1]))
    return hits


def page_fields(page):
    p = path_of(page)
    doc = soup(p)
    meta = doc.find("meta", attrs={"name": "description"})
    h1 = doc.find("h1")
    clean = lambda el: re.sub(r"\s+", " ", el.get_text(" ")).strip()
    return {
        "title": doc.title.get_text().strip() if doc.title else "",
        "h1": clean(h1) if h1 else "",
        "meta": meta["content"].strip() if meta else "",
        "jsonld": [d for block in jsonld(p) for d in descriptions(block)],
        "h2": [clean(h) for h in doc.find_all("h2")],
        "h3": [clean(h) for h in doc.find_all("h3")],
        "slug": page.rsplit(".", 1)[0],
    }


def bow(text):
    toks = [t for t in tokens(text) if t not in PREPOSITIONS]
    return {
        "formatie": [t for t in toks if t.startswith("formati")],
        "nunta": [t for t in toks if t.startswith("nunt")],
        "topo": find_toponyms(toks),
    }


def terms_in(text):
    toks = tokens(text)
    return {name: term_positions(toks, pat) for name, pat in CLIENT_TERMS.items() if term_positions(toks, pat)}


def campuri():
    out = {}
    for page in OLD_PAGES + ALL_PAGES:
        f = page_fields(page)
        verdict, terms = {}, {}
        for name in ("title", "h1", "meta", "jsonld", "slug", "h2", "h3"):
            val = f[name]
            items = val if isinstance(val, list) else [val]
            b = [bow(x) for x in items]
            if name in ("title", "h1", "meta", "jsonld", "slug"):
                joined = bow(" | ".join(items))
                verdict[name] = {
                    "formatie": len(joined["formatie"]), "nunta": len(joined["nunta"]),
                    "topo": sorted(set(joined["topo"])),
                    "incalcare": bool(joined["formatie"] and joined["nunta"] and joined["topo"]),
                }
            for x in items:
                for t, h in terms_in(x).items():
                    terms.setdefault(t, []).append({"camp": name, "text": x, "potrivire": h})
            # Toponime în headinguri: pentru analiza C.
            if name in ("h2", "h3"):
                verdict[name + "_topo"] = [(x, sorted(set(bb["topo"]))) for x, bb in zip(items, b) if bb["topo"]]
        out[page] = {"fields": f, "bow": verdict, "terms": terms, "old": page in OLD_PAGES}
    json.dump(out, sys.stdout, ensure_ascii=False, indent=1)


def matrice():
    import non_duplicare as nd
    rows, hits = [], []
    for a in ALL_PAGES:
        for b in OLD_PAGES:
            for masked in (False, True):
                res = nd.compare(a, os.path.join(ROOT, b), masked)
                mx = {k: max((r[0] for r in v), default=0.0) for k, v in res.items()}
                label = "mascat" if masked else "brut"
                rows.append((a, b, label, mx))
                for k, rr in res.items():
                    for score, ta, tb in rr:
                        if score > nd.REPORT:
                            hits.append((a, b, label, k, score, ta, tb))
    for a, b, label, mx in rows:
        print(f"{a:24} {b:26} {label:6} " + " ".join(f"{mx[k] * 100:6.1f}%" for k in ("paragraf", "propoziție", "shingle-6")))
    print(f"\nPotriviri > 85%: {len(hits)}")
    for a, b, label, k, score, ta, tb in hits:
        print(f"\n  {a} ↔ {b} [{label}, {k}] {score:.1%}\n    A: {ta}\n    B: {tb or '(shingles)'}")
    top = sorted(rows, key=lambda r: -max(r[3].values()))[:15]
    print("\nCele mai mari 15 maxime pe pereche:")
    for a, b, label, mx in top:
        print(f"  {a:24} {b:26} {label:6} " + " ".join(f"{k}={mx[k] * 100:.1f}%" for k in mx))


if __name__ == "__main__":
    if "--matrice" in sys.argv:
        matrice()
    else:
        campuri()
