#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Măsurători de randare pentru paginile prototipului.

Două verificări, pe lățimi configurabile:

  overflow   scrollWidth vs clientWidth pe <html> — ținta e 0, adică nicio bară
             de derulare orizontală (CLAUDE.md §8, quality floor)
  tap        ținte interactive sub pragul de dimensiune (implicit 44 px)

Tailwind se INJECTEAZĂ la măsurătoare, interceptând cererea către
cdn.tailwindcss.com. Fișierele HTML nu se ating: harness-ul nu scrie niciodată
în paginile prototipului. Vezi README.md.

Rulare:
    node build-tailwind.js && python3 measure.py
    python3 measure.py --dir ../../ --latimi 360,768
    python3 measure.py --pagini zona-ilfov.html,zona-prahova.html --tap
"""
import argparse
import glob
import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Lipsește playwright. Instalează:\n"
             "  pip install -r zone-mockup/verify/render/requirements.txt")

AICI = os.path.dirname(os.path.abspath(__file__))
CSS = os.path.join(AICI, "build", "tailwind.css")
IMPLICIT_DIR = os.path.normpath(os.path.join(AICI, "..", "..")) + os.sep
LATIMI = [360, 390, 768, 1024, 1440]
PRAG_TAP = 44

JS_OVERFLOW = """() => {
  const de = document.documentElement;
  return {cw: de.clientWidth, sw: de.scrollWidth};
}"""

# Linkurile inline din proză sunt exceptate: WCAG 2.5.8 „Target Size (Minimum)"
# scoate explicit ținta a cărei mărime e dată de line-height-ul textului din jur.
# A le umfla la 44 px ar rupe fluxul rândului.
JS_TAP = """(prag) => {
  const rezultat = {mici: [], inline: 0, total: 0};
  const sel = 'a, button, input, select, textarea, [role=button]';
  const drawer = document.getElementById('mobile-menu');
  for (const el of document.querySelectorAll(sel)) {
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    // drawerul închis e inert: conținutul lui nu e atingibil
    if (drawer && drawer.inert && drawer.contains(el)) continue;
    rezultat.total++;
    if (r.height >= prag && r.width >= prag) continue;
    const p = el.parentElement;
    const inline = p && /^(P|LI|SPAN|TD)$/.test(p.tagName) &&
      p.textContent.trim().length > el.textContent.trim().length + 10;
    if (inline) { rezultat.inline++; continue; }
    rezultat.mici.push((el.textContent || el.tagName).trim().slice(0, 40) +
      ' ' + Math.round(r.width) + '×' + Math.round(r.height));
  }
  return rezultat;
}"""


def sir_js(text):
    return '"' + (text.replace('\\', '\\\\').replace('"', '\\"')
                      .replace('\n', '\\n').replace('\r', '')) + '"'


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=IMPLICIT_DIR,
                    help="directorul cu paginile (implicit: zone-mockup/)")
    ap.add_argument("--pagini", default="",
                    help="listă separată prin virgulă; implicit toate .html din --dir")
    ap.add_argument("--latimi", default=",".join(map(str, LATIMI)),
                    help="lățimi de viewport, separate prin virgulă")
    ap.add_argument("--tap", action="store_true",
                    help="raportează și țintele de tap sub prag")
    ap.add_argument("--prag-tap", type=int, default=PRAG_TAP)
    args = ap.parse_args()

    if not os.path.exists(CSS):
        sys.exit("Lipsește " + CSS + "\nRulează întâi:  node build-tailwind.js")
    css = open(CSS, encoding="utf-8").read()

    director = os.path.abspath(args.dir) + os.sep
    if args.pagini:
        pagini = [p.strip() for p in args.pagini.split(",") if p.strip()]
    else:
        pagini = sorted(os.path.basename(p) for p in glob.glob(director + "*.html"))
    if not pagini:
        sys.exit("Nicio pagină în " + director)
    latimi = [int(w) for w in args.latimi.split(",")]

    executabil = None
    for cale in sorted(glob.glob("/opt/pw-browsers/chromium*/chrome-linux/chrome")):
        executabil = cale
        break

    # Shim-ul face ce face scriptul CDN: injectează CSS-ul și expune `tailwind`,
    # pentru ca ../assets/tailwind.config.js, încărcat imediat după, să nu crape.
    shim = ("(function(){var s=document.createElement('style');s.textContent="
            + sir_js(css) + ";document.head.appendChild(s);"
            "window.tailwind={config:{}};})();")

    def ruteaza(route):
        if "cdn.tailwindcss.com" in route.request.url:
            route.fulfill(status=200, content_type="application/javascript", body=shim)
        else:
            route.continue_()

    esecuri = 0
    randuri = []
    with sync_playwright() as p:
        browser = (p.chromium.launch(executable_path=executabil) if executabil
                   else p.chromium.launch())
        ctx = browser.new_context()
        ctx.route("**/*", ruteaza)
        for pagina in pagini:
            cale = director + pagina
            if not os.path.exists(cale):
                print("  lipsă: " + pagina, file=sys.stderr)
                esecuri += 1
                continue
            rand = [pagina, []]
            for w in latimi:
                pg = ctx.new_page()
                pg.set_viewport_size({"width": w, "height": 900})
                pg.goto("file://" + cale, wait_until="load")
                pg.wait_for_timeout(120)
                o = pg.evaluate(JS_OVERFLOW)
                celula = {"over": o["sw"] - o["cw"]}
                if args.tap:
                    celula["tap"] = pg.evaluate(JS_TAP, args.prag_tap)
                rand[1].append(celula)
                pg.close()
            randuri.append(rand)
        browser.close()

    print("\noverflow = scrollWidth − clientWidth, în px. Ținta: 0.\n")
    print("%-26s %s" % ("pagină", "  ".join("%7s" % ("%dpx" % w) for w in latimi)))
    for pagina, celule in randuri:
        rea = any(c["over"] > 0 for c in celule)
        esecuri += rea
        print("%-26s %s%s" % (pagina,
                              "  ".join("%7d" % c["over"] for c in celule),
                              "  ← OVERFLOW" if rea else ""))
    print("\nPagini cu overflow: %d / %d" % (
        sum(1 for _, c in randuri if any(x["over"] > 0 for x in c)), len(randuri)))

    if args.tap:
        print("\nȚinte de tap sub %d px (linkurile inline din proză sunt exceptate,\n"
              "WCAG 2.5.8 „Inline\"):\n" % args.prag_tap)
        for pagina, celule in randuri:
            for w, c in zip(latimi, celule):
                t = c["tap"]
                if t["mici"]:
                    esecuri += 1
                    print("  %-24s %4dpx  DE REPARAT: %s" % (pagina, w, t["mici"][:4]))
        print("  (nimic de reparat dacă lista de mai sus e goală)")
        for pagina, celule in randuri:
            t = celule[0]["tap"]
            print("  %-24s %4dpx  %d interactive, %d inline exceptate"
                  % (pagina, latimi[0], t["total"], t["inline"]))

    return 1 if esecuri else 0


if __name__ == "__main__":
    sys.exit(main())
