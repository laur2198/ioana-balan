#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit pentru cele 7 pagini de zonă noi: Mehedinți, Olt, Brăila, Bacău,
Vâlcea, Galați, Tulcea.

Raport, nu verificare: nu intră în run_all.sh și nu întoarce cod de eroare.
Reutilizează logica din audit_keywords.py și bag_of_words.py fără să le modifice.

Ce face:

  --propuneri   Verifică fiecare title și H1 propus:
                · regula bag-of-words (formație + nuntă + toponim în același câmp)
                · termenii clientului detectați (CLIENT_TERMS din audit_keywords)
                · interdicția „formatie nunta", rezervat pentru grand-music.ro
                · coliziuni de toponim cu titlurile/H1-urile celor 12 pagini
                  existente

  --tipar       Tiparul real al celor 12 pagini existente: title, H1 și ce
                termeni ating, ca propunerile să se poată compara cu el.

Propunerile trăiesc în PROPUNERI de mai jos și în zone-mockup/ZONE-NOI-PLAN.md.
Sursele live (grand-music.ro, ioana-balan.ro) NU se pot interoga din sandbox:
ambele domenii sunt blocate de proxy-ul de egress. Partea de audit care depinde
de ele e marcată ca parțială în ZONE-NOI-PLAN.md §2, cu sursele citate acolo.
"""
import argparse
import sys

from _common import ZONE_PAGES, find_toponyms, read, tokens
from audit_keywords import bow, page_fields, terms_in

# Rezervat pentru grand-music.ro. Paginile ioana-balan.ro nu îl folosesc:
# ar pune cele două domenii în competiție pe aceeași interogare.
TERMEN_REZERVAT = "formatie nunta"

# (județ, title propus, H1 propus)
PROPUNERI = [
    ("Mehedinți",
     "Folclor Oltenesc și Muzică de Petrecere în Drobeta-Turnu Severin și Mehedinți | Nunți, Botezuri | Ioana Balan",
     "Folclor de Dunăre și cântec oltenesc, la nunți și botezuri în Mehedinți"),
    ("Olt",
     "Cântec Oltenesc și Muzică de Petrecere în Slatina și Olt | Nunți, Botezuri | Ioana Balan",
     "Cântec oltenesc de câmpie, pentru nunți și botezuri în Slatina și Olt"),
    ("Brăila",
     "Horă de Baltă și Muzică de Petrecere în Brăila | Nunți, Botezuri | Ioana Balan",
     "Hore de baltă și sârbe de Bărăgan, la nunți și botezuri în Brăila"),
    ("Bacău",
     "Folclor Moldovenesc și Muzică de Petrecere în Bacău | Nunți, Botezuri | Ioana Balan",
     "Folclor moldovenesc de Siret și Trotuș, la nunți și botezuri în Bacău"),
    ("Vâlcea",
     # NU „Formație": cu „Nunți" și toponim în același câmp ar încălca regula
     # bag-of-words, iar Vâlcea e singurul din cele 7 unde grand-music.ro are
     # deja pagină (/formatie-nunta-valcea/). Aici ne ținem cel mai departe.
     "Cântec de Sub Carpați și Muzică de Petrecere în Râmnicu Vâlcea și Vâlcea | Nunți, Botezuri | Ioana Balan",
     "Cântec de sub Carpați și joc oltenesc, la nunți și botezuri în Vâlcea"),
    ("Galați",
     "Folclor Moldovenesc și Muzică de Petrecere în Galați | Nunți, Botezuri | Ioana Balan",
     "Folclor de Dunăre moldovenească, la nunți și botezuri în Galați"),
    ("Tulcea",
     "Folclor Dobrogean și Muzică de Petrecere în Tulcea și Delta Dunării | Nunți, Botezuri | Ioana Balan",
     "Folclor dobrogean și ritmuri de Deltă, la nunți și botezuri în Tulcea"),
]


def incalca_bow(text):
    """Regula bag-of-words: formație + nuntă + toponim nu au voie simultan."""
    b = bow(text)
    return bool(b["formatie"]) and bool(b["nunta"]) and bool(b["topo"])


def contine_rezervat(text):
    toks = [t for t in tokens(text)]
    for i, t in enumerate(toks):
        if t.startswith("formati"):
            for u in toks[i + 1:i + 4]:
                if u.startswith("nunt"):
                    return True
    return False


def tipar_existent():
    out = {}
    for page in ZONE_PAGES:
        f = page_fields(page)
        out[page] = (f["title"], f["h1"])
    return out


def cmd_tipar():
    print("Tiparul celor %d pagini de zonă existente\n" % len(ZONE_PAGES))
    for page, (title, h1) in sorted(tipar_existent().items()):
        b_t, b_h = bow(title), bow(h1 or "")
        print("%s" % page)
        print("  title  %s" % title)
        print("         bow: formație=%d nuntă=%d toponim=%s%s"
              % (len(b_t["formatie"]), len(b_t["nunta"]), b_t["topo"] or "—",
                 "   ÎNCALCĂ" if incalca_bow(title) else ""))
        print("  h1     %s" % (h1 or "—"))
        print("         bow: formație=%d nuntă=%d toponim=%s%s"
              % (len(b_h["formatie"]), len(b_h["nunta"]), b_h["topo"] or "—",
                 "   ÎNCALCĂ" if incalca_bow(h1 or "") else ""))
        t = terms_in(title)
        if t:
            print("         termeni: %s" % ", ".join(sorted(t)))
        print()


def cmd_propuneri():
    existent = tipar_existent()
    topo_existente = {}
    for page, (title, h1) in existent.items():
        for grup in (bow(title)["topo"], bow(h1 or "")["topo"]):
            for t in grup:
                topo_existente.setdefault(t, set()).add(page)

    print("Propuneri pentru cele %d pagini noi\n" % len(PROPUNERI))
    probleme = 0
    for judet, title, h1 in PROPUNERI:
        print("=== %s ===" % judet)
        for eticheta, text in (("title", title), ("h1", h1)):
            b = bow(text)
            steaguri = []
            if incalca_bow(text):
                steaguri.append("ÎNCALCĂ bag-of-words")
            if contine_rezervat(text):
                steaguri.append("conține „%s" % TERMEN_REZERVAT + "”, REZERVAT grand-music.ro")
            coliziuni = sorted({p for t in b["topo"] for p in topo_existente.get(t, ())})
            if coliziuni:
                steaguri.append("toponim comun cu: %s" % ", ".join(coliziuni))
            probleme += sum(1 for s in steaguri if s.startswith(("ÎNCALCĂ", "conține")))
            print("  %-6s %s" % (eticheta, text))
            print("         formație=%d nuntă=%d toponim=%s"
                  % (len(b["formatie"]), len(b["nunta"]), b["topo"] or "—"))
            t = terms_in(text)
            if t:
                print("         termeni: %s" % ", ".join(sorted(t)))
            print("         %s" % ("ok" if not steaguri else " · ".join(steaguri)))
        print()
    print("Propuneri cu problemă de regulă: %d" % probleme)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--propuneri", action="store_true")
    ap.add_argument("--tipar", action="store_true")
    a = ap.parse_args()
    if not (a.propuneri or a.tipar):
        ap.print_help()
        return 0
    if a.tipar:
        cmd_tipar()
    if a.propuneri:
        cmd_propuneri()
    return 0


if __name__ == "__main__":
    sys.exit(main())
