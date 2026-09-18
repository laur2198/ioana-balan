"""Linkuri interne contextuale între cele 20 de pagini noi (runda a opta).

Rândurile se citesc din pagini, după poziție, nu dintr-o listă ținută de mână:
  vecine   — <p> din secțiunea de localități care conține linkuri către zona-*.html
  servicii — <p> din secțiunea de pachete (zone) sau de județe (hub) care
             conține un link către nunta.html

Verificări (eșec = cod 1):
  1. rândurile de vecine comparate între ele, brut și cu toponime mascate
     (SequenceMatcher pe tokeni): zero perechi la 75% sau peste;
  2. tiparul de construcție: semnătura „linkuri per frază” (ex. 0111 = frază-cadru
     fără link, apoi câte un link pe frază). Cel mult 4 rânduri pe aceeași
     semnătură. Separat, informativ: scheletul de cuvinte funcționale (conținutul
     înlocuit cu „_”, toponimele cu TOPO), perechi ≥ 75%;
  3. aceleași două teste pe rândurile către servicii (12 zone + hub);
  4. fragment identic: orice secvență de 10+ cuvinte consecutive comună între
     două rânduri noi (brut și mascat). Informativ: aceeași căutare între fiecare
     rând nou și restul textului de pe cele 31 de pagini;
  9. linkuri interne per pagină (tot documentul și doar <main>); cu
     `--baza DIR`, și starea dinainte, citită din copia din DIR.
Plus: fiecare pagină de zonă are exact un rând de vecine (2–3 linkuri, fără
propria pagină) și un rând de servicii cu toate cele patru ținte; hubul are
rândul de servicii plus repertoriu.html și formatia.html.
"""
import itertools
import os
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher

from bs4 import BeautifulSoup

from _common import ALL_PAGES, HUB, OLD_PAGES, ROOT, SERVICE, ZONE_PAGES, content_blocks, mask, soup, tokens

THRESHOLD = 0.75
MAX_SAME_SHAPE = 4
FRAGMENT = 10

NEIGHBOURS = {
    "zona-ilfov.html": {"giurgiu", "dambovita", "prahova"},
    "zona-giurgiu.html": {"ilfov", "teleorman", "calarasi"},
    "zona-prahova.html": {"ilfov", "dambovita", "buzau"},
    "zona-dambovita.html": {"ilfov", "prahova", "arges"},
    "zona-teleorman.html": {"giurgiu", "arges", "dolj"},
    "zona-calarasi.html": {"giurgiu", "ialomita", "constanta"},
    "zona-ialomita.html": {"calarasi", "buzau", "constanta"},
    "zona-buzau.html": {"prahova", "ialomita", "brasov"},
    "zona-arges.html": {"dambovita", "teleorman", "dolj"},
    "zona-brasov.html": {"prahova", "buzau", "dambovita"},
    "zona-constanta.html": {"calarasi", "ialomita"},
    "zona-dolj.html": {"teleorman", "arges"},
    # Runda a doua de zone, 19.09.2026. Fiecare legătură pornește de la o
    # relație reală între județe — drum, râu sau trecere cu bacul — nu de la
    # vecinătatea de pe hartă: Tulcea și Galați nu au hotar terestru comun,
    # dar au bacul de la Brăila–Smârdan și malul celălalt al Dunării.
    "zona-tulcea.html": {"constanta", "galati"},
    "zona-valcea.html": {"arges", "dolj", "olt"},
    "zona-galati.html": {"bacau", "braila", "tulcea"},
    "zona-mehedinti.html": {"dolj", "valcea"},
    "zona-olt.html": {"dolj", "teleorman", "valcea"},
    "zona-braila.html": {"buzau", "galati", "ialomita", "tulcea"},
    "zona-bacau.html": {"buzau", "galati"},
    # Vrancea, 18.09.2026. Bacău și Galați sunt vecinii de Moldova, cu același
    # bloc de repertoriu; Buzău e trecerea peste Milcov spre Muntenia, singura
    # legătură a paginii cu setul vechi.
    "zona-vrancea.html": {"bacau", "buzau", "galati"},
}

# Cuvinte funcționale păstrate în schelet (pliate, fără diacritice).
FUNCTION_WORDS = set("""
a al ale ai cel cea cei cele celui celei un o unui unei niste
si sau ori iar dar ci nici fie ca daca decat desi pentru deoarece caci
in din la pe de cu spre prin intre dupa inainte catre pana fara sub peste langa dinspre
se si-a isi il o le ii ne va nu mai tot toate toti fiecare fiecarui
e este sunt au are a fost era care ce cine unde cand cat cum
acolo aici deja doar numai chiar tot totusi apoi
""".split())


def text_of(p):
    return re.sub(r"\s+", " ", p.get_text(" ")).strip()


def neighbour_rows():
    out = {}
    for page in ZONE_PAGES:
        sec = soup(page).find("section", attrs={"aria-labelledby": "localitati-titlu"})
        rows = [p for p in sec.find_all("p") if p.find("a", href=re.compile(r"^zona-.*\.html$"))]
        out[page] = rows
    return out


def service_rows():
    out = {}
    for page in ZONE_PAGES + [HUB]:
        sid = "zone-titlu" if page == HUB else "pachete-titlu"
        sec = soup(page).find("section", attrs={"aria-labelledby": sid})
        out[page] = [p for p in sec.find_all("p") if p.find("a", href="nunta.html")]
    return out


def signature(p):
    """Linkuri per frază. Frazele se despart la . ! ? urmate de spațiu; textul
    linkului se înlocuiește cu un marcaj ca punctele din ancore să nu conteze."""
    clone = BeautifulSoup(str(p), "html.parser")
    for a in clone.find_all("a"):
        a.replace_with(" \x00 ")
    txt = re.sub(r"\s+", " ", clone.get_text(" "))
    parts = [s for s in re.split(r"(?<=[.!?])\s+", txt) if s.strip()]
    return "".join(str(s.count("\x00")) for s in parts)


def skeleton(text):
    return ["_" if (t not in FUNCTION_WORDS and t != "TOPO") else t for t in mask(tokens(text))]


def ratio(a, b):
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def ngrams(toks, n):
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def longest_common_run(a, b):
    m = SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
    return m.size, a[m.a:m.a + m.size]


def short(page):
    return page.replace("zona-", "").replace(".html", "")


def compare_group(title, rows):
    """rows: {pagină: text}. Întoarce numărul de eșecuri."""
    fails = 0
    pages = list(rows)
    raw = {p: tokens(t) for p, t in rows.items()}
    msk = {p: mask(raw[p]) for p in pages}
    best = {p: (0.0, None, None) for p in pages}
    pairs = []
    for a, b in itertools.combinations(pages, 2):
        r, m = ratio(raw[a], raw[b]), ratio(msk[a], msk[b])
        s = max(r, m)
        pairs.append((s, r, m, a, b))
        for x, y in ((a, b), (b, a)):
            if s > best[x][0]:
                best[x] = (s, y, "mascat" if m >= r else "brut")
    over = [x for x in pairs if x[0] >= THRESHOLD]
    fails += len(over)
    print(f"\n--- {title}: {len(pages)} rânduri, {len(pairs)} perechi ---")
    print(f"Perechi ≥ {THRESHOLD:.0%} (maximul dintre brut și mascat): {len(over)}")
    for s, r, m, a, b in sorted(pairs, reverse=True)[:5]:
        print(f"  {s:6.1%}  (brut {r:5.1%}, mascat {m:5.1%})  {short(a)} ↔ {short(b)}")
    vals = sorted(v[0] for v in best.values())
    buckets = [("<25%", 0, .25), ("25–50%", .25, .50), ("50–75%", .50, .75), ("≥75%", .75, 1.01)]
    print("Maximul fiecărui rând față de celelalte:")
    for p in sorted(pages, key=lambda p: -best[p][0]):
        s, other, how = best[p]
        print(f"  {short(p):12} {s:6.1%}  ← {short(other)} ({how})")
    print("Distribuția maximelor: " + " · ".join(
        f"{name} {sum(lo <= v < hi for v in vals)}" for name, lo, hi in buckets)
        + f" · mediană {vals[len(vals) // 2]:.1%}")
    return fails


def shapes(title, rows_html):
    fails = 0
    groups = defaultdict(list)
    for page, p in rows_html.items():
        groups[signature(p)].append(short(page))
    print(f"\nTipar de construcție — {title} (linkuri per frază):")
    for sig, pages in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        flag = "  PESTE LIMITĂ" if len(pages) > MAX_SAME_SHAPE else ""
        print(f"  {sig:6} × {len(pages)}: {', '.join(pages)}{flag}")
        fails += len(pages) > MAX_SAME_SHAPE
    print(f"  Cel mai mare grup: {max(len(v) for v in groups.values())} (limita {MAX_SAME_SHAPE})")
    sk = {p: skeleton(text_of(h)) for p, h in rows_html.items()}
    close = sorted(((ratio(sk[a], sk[b]), a, b) for a, b in itertools.combinations(sk, 2)), reverse=True)
    print(f"  Schelet de cuvinte funcționale, informativ: perechi ≥ {THRESHOLD:.0%}: "
          f"{sum(s >= THRESHOLD for s, _, _ in close)}; cea mai apropiată: "
          f"{close[0][0]:.1%} {short(close[0][1])} ↔ {short(close[0][2])}")
    return fails


def fragments(all_rows):
    fails = 0
    print(f"\nFragment identic ≥ {FRAGMENT} cuvinte între două rânduri noi (brut și mascat):")
    items = list(all_rows.items())
    hits = 0
    for (ka, ta), (kb, tb) in itertools.combinations(items, 2):
        for label, f in (("brut", tokens), ("mascat", lambda t: mask(tokens(t)))):
            common = ngrams(f(ta), FRAGMENT) & ngrams(f(tb), FRAGMENT)
            if common:
                hits += 1
                print(f"  {ka} ↔ {kb} [{label}]: {' '.join(sorted(common)[0])}")
    print(f"  Perechi cu fragment comun: {hits}")
    fails += hits
    longest = max(
        (longest_common_run(mask(tokens(ta)), mask(tokens(tb)))[0], ka, kb)
        for (ka, ta), (kb, tb) in itertools.combinations(items, 2))
    print(f"  Cea mai lungă secvență comună (mascat): {longest[0]} cuvinte, {longest[1]} ↔ {longest[2]}")

    # Informativ: rândurile noi față de restul textului de pe cele 31 de pagini.
    new_texts = {t for _, t in items}
    corpus = []
    for page in ALL_PAGES + [os.path.join(ROOT, p) for p in OLD_PAGES]:
        for b in content_blocks(page):
            if b not in new_texts:
                corpus.append((os.path.basename(page), b))
    print(f"\n  Informativ — rând nou față de restul textului (31 de pagini, {len(corpus)} blocuri), "
          f"fragmente ≥ {FRAGMENT} cuvinte, mascat:")
    found = 0
    corpus_ng = [(pg, ngrams(mask(tokens(b)), FRAGMENT)) for pg, b in corpus]
    for key, t in items:
        mine = ngrams(mask(tokens(t)), FRAGMENT)
        for pg, ng in corpus_ng:
            common = mine & ng
            if common:
                found += 1
                print(f"    {key} ↔ {pg}: {' '.join(sorted(common)[0])}")
    print(f"    Potriviri: {found}")
    return fails


def link_counts(base_dir=None):
    def count(path):
        with open(path, encoding="utf-8") as fh:
            doc = BeautifulSoup(fh.read(), "html.parser")
        internal = lambda a: not re.match(r"^(https?:|mailto:|tel:|#|//)", a.get("href", "")) and a.get("href")
        main = doc.find("main")
        return (sum(1 for a in doc.find_all("a") if internal(a)),
                sum(1 for a in main.find_all("a") if internal(a)))
    from _common import MOCKUP
    print("\nLinkuri interne per pagină (document întreg / doar <main>):")
    header = f"  {'pagină':22} {'acum':>11}"
    if base_dir:
        header += f" {'înainte':>11} {'Δ main':>7}"
    print(header)
    for page in ALL_PAGES:
        now = count(os.path.join(MOCKUP, page))
        line = f"  {page:22} {now[0]:>5} / {now[1]:<3}"
        if base_dir:
            before = count(os.path.join(base_dir, page))
            line += f" {before[0]:>5} / {before[1]:<3} {now[1] - before[1]:>+5}"
        print(line)


def main():
    base_dir = None
    if "--baza" in sys.argv:
        base_dir = sys.argv[sys.argv.index("--baza") + 1]
    fails = 0

    nb = neighbour_rows()
    sv = service_rows()
    print("Structură:")
    for page in ZONE_PAGES:
        rows = nb[page]
        problems = []
        if len(rows) != 1:
            problems.append(f"{len(rows)} rânduri de vecine")
        else:
            targets = {a["href"][5:-5] for a in rows[0].find_all("a", href=re.compile(r"^zona-"))}
            if targets != NEIGHBOURS[page]:
                problems.append(f"vecine {sorted(targets)} ≠ {sorted(NEIGHBOURS[page])}")
        if len(sv[page]) != 1:
            problems.append(f"{len(sv[page])} rânduri de servicii")
        else:
            targets = {a["href"] for a in sv[page][0].find_all("a")}
            if not set(SERVICE) <= targets:
                problems.append(f"servicii lipsă: {sorted(set(SERVICE) - targets)}")
        fails += bool(problems)
        print(f"  {page:22} " + ("ok" if not problems else "; ".join(problems)))
    hub_targets = {a["href"] for a in sv[HUB][0].find_all("a")} if len(sv[HUB]) == 1 else set()
    need = set(SERVICE) | {"repertoriu.html", "formatia.html"}
    ok = need <= hub_targets
    fails += not ok
    print(f"  {HUB:22} " + ("ok" if ok else f"lipsă: {sorted(need - hub_targets)}"))

    nb_html = {p: rows[0] for p, rows in nb.items() if rows}
    sv_html = {p: rows[0] for p, rows in sv.items() if rows}
    fails += compare_group("1. Zone vecine", {p: text_of(h) for p, h in nb_html.items()})
    fails += shapes("zone vecine", nb_html)
    fails += compare_group("3. Servicii (12 zone + hub)", {p: text_of(h) for p, h in sv_html.items()})
    fails += shapes("servicii", sv_html)
    all_rows = {f"vecine:{short(p)}": text_of(h) for p, h in nb_html.items()}
    all_rows.update({f"servicii:{short(p)}": text_of(h) for p, h in sv_html.items()})
    fails += fragments(all_rows)
    link_counts(base_dir)

    print(f"\nEșecuri: {fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
