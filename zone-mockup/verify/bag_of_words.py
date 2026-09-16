"""4.1 — Regula bag-of-words pe cinci câmpuri.

După plierea diacriticelor și eliminarea prepozițiilor, cei trei tokeni —
formație, nuntă, toponim — nu au voie să apară SIMULTAN în același câmp,
indiferent de distanța dintre ei. Câmpuri: <h1>, <title>, <meta description>,
`description` din JSON-LD (toate nivelurile), slug = numele fișierului.
Canonicalul e comentat pe toate paginile, deci slug-ul se ia din fișier.
"""
import os
import re
import sys

from _common import ALL_PAGES, OLD_PAGES, ROOT, find_toponyms, jsonld, read, soup, tokens

PREPOSITIONS = {"in", "din", "la", "pentru", "de", "si", "cu", "pe", "a", "al", "ale"}


def descriptions(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "description" and isinstance(v, str):
                yield v
            else:
                yield from descriptions(v)
    elif isinstance(node, list):
        for v in node:
            yield from descriptions(v)


def fields(page):
    doc = soup(page)
    h1 = doc.find("h1")
    meta = doc.find("meta", attrs={"name": "description"})
    return {
        "h1": h1.get_text(" ") if h1 else "",
        "title": doc.title.get_text() if doc.title else "",
        "meta": meta["content"] if meta else "",
        "jsonld": " | ".join(d for block in jsonld(page) for d in descriptions(block)),
        "slug": os.path.basename(page).rsplit(".", 1)[0].replace("-", " "),
    }


def check(text):
    toks = [t for t in tokens(text) if t not in PREPOSITIONS]
    formatie = [t for t in toks if t.startswith("formati")]
    nunta = [t for t in toks if t.startswith("nunt")]
    topo = find_toponyms(toks)
    return formatie, nunta, topo


def main():
    violations = 0
    print(f"{'pagină':22} {'câmp':7} formație nunt* toponim  verdict")
    for page in ALL_PAGES:
        for name, text in fields(page).items():
            f, n, t = check(text)
            bad = bool(f and n and t)
            violations += bad
            print(f"{page:22} {name:7} {len(f):>8} {len(n):>5} {len(t):>7}  {'ÎNCĂLCARE' if bad else 'ok'}"
                  + (f"   [{', '.join(sorted(set(t)))}]" if t and (f or n) else ""))
    print(f"\nÎncălcări pe cele 20 de pagini noi: {violations}")

    # Informativ: cele 11 pagini existente, citite din rădăcina repo-ului. Nu se
    # modifică din zone-mockup, deci nu influențează codul de ieșire.
    old = 0
    print(f"\nInformativ — cele {len(OLD_PAGES)} pagini existente:")
    for page in OLD_PAGES:
        for name, text in fields(os.path.join(ROOT, page)).items():
            f, n, t = check(text)
            if f and n and t:
                old += 1
                print(f"  {page:26} {name:7} ÎNCĂLCARE   [{', '.join(sorted(set(t)))}]")
    print(f"Încălcări pe toate 31: {violations + old} ({violations} noi + {old} existente)")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
