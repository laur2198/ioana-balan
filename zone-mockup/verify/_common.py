"""Utilitare comune pentru scripturile de verificare din /zone-mockup/verify/.

Doar stdlib + BeautifulSoup. Se rulează din orice director: căile se rezolvă
relativ la acest fișier.
"""
import glob
import json
import os
import re
import unicodedata

from bs4 import BeautifulSoup, Comment

MOCKUP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(MOCKUP)

ZONE_PAGES = sorted(os.path.basename(p) for p in glob.glob(os.path.join(MOCKUP, "zona-*.html")))
HUB = "zone.html"
CLUSTER = ["repertoriu.html", "formatia.html", "folclor-si-manele.html"]
# Pagini de serviciu: una per tip de eveniment, fără localități și fără logistică.
SERVICE = ["nunta.html", "botez.html", "eveniment-privat.html", "corporate.html"]
ALL_PAGES = ZONE_PAGES + [HUB] + [p for p in CLUSTER + SERVICE if os.path.exists(os.path.join(MOCKUP, p))]
# Cele 11 pagini existente, din rădăcina repo-ului. Doar referință de comparație:
# nu se modifică din zone-mockup.
OLD_PAGES = [
    "index.html", "oferte.html", "despre.html", "galerie.html", "discografie.html",
    "contact.html", "blog.html", "articol.html", "faq.html",
    "termeni-si-conditii.html", "politica-cookie.html",
]


def read(name):
    path = name if os.path.isabs(name) else os.path.join(MOCKUP, name)
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def fold(text):
    """Litere mici, fără diacritice (ș/ş, ț/ţ, ă, â, î)."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return text.lower()


def tokens(text):
    return re.findall(r"[a-z0-9]+", fold(text))


# --- Toponime -----------------------------------------------------------------
# Regiuni, județe, orașe și toate localitățile listate pe paginile de zonă.
# Lista de localități se citește din pagini, ca să nu rămână în urmă.
REGIONS = [
    "Muntenia", "Ardeal", "Transilvania", "Oltenia", "Dobrogea", "Moldova",
    "Banat", "Maramureș", "Bucovina", "Crișana", "Muscel", "Bărăgan",
    "Țara Bârsei", "Vrancea", "Dunăre", "Dunărea", "Olt", "Milcov", "Vâlcea",
    "Valea Prahovei", "Doftana", "Chiciu", "Ostrov", "România", "București",
    "Capitala", "Ilfov", "Giurgiu", "Prahova", "Dâmbovița", "Teleorman",
    "Călărași", "Ialomița", "Buzău", "Argeș", "Brașov", "Constanța", "Dolj",
    "Craiova", "Pitești", "Ploiești", "litoral", "Vlașca",
]
# Adjective derivate din toponime. NU intră în regula bag-of-words (nu sunt
# toponime), dar SE MASCHEAZĂ la trecerea a doua de non-duplicare: altfel
# „hora oltenească" vs „hora moldovenească" ar ascunde un șablon comun.
DERIVED_STEMS = [
    "muntenesc", "muntenest", "ardelenesc", "ardelenest", "oltenesc", "oltenest",
    "dobrogean", "moldovenesc", "moldovenest", "muscelean", "bucurestean",
    "aromanesc", "aromanest", "machedonesc", "grecesc", "balcanic",
]


def localities():
    out = set()
    for page in ZONE_PAGES:
        for ul in re.findall(r'<ul class="motif-list.*?</ul>', read(page), re.S):
            out |= set(re.findall(r"<li[^>]*>(.*?)</li>", ul))
    return out


def toponym_token_seqs():
    seqs = {tuple(tokens(t)) for t in set(REGIONS) | localities()}
    seqs.discard(())
    return sorted(seqs, key=len, reverse=True)


def token_is_toponym_form(tok, base):
    """Forma de bază sau flexionată (-ul, -ului, -ei, -ii, -i)."""
    if tok == base:
        return True
    if len(base) < 4:
        return False
    # Brașov → brasovul, brasovului; București → bucurestiului
    if tok.startswith(base) and tok[len(base):] in ("ul", "ului", "lui", "ei", "ii", "i"):
        return True
    # Muntenia → munteniei; Dobrogea → dobrogei; Constanța → constantei
    if base.endswith("a") and tok.startswith(base[:-1]) and tok[len(base) - 1:] in ("ei", "ii"):
        return True
    if base.endswith("ea") and tok == base[:-2] + "ei":
        return True
    return False


def find_toponyms(toks):
    hits = []
    seqs = toponym_token_seqs()
    for i in range(len(toks)):
        for seq in seqs:
            n = len(seq)
            if i + n > len(toks):
                continue
            window = toks[i:i + n]
            if all(w == s for w, s in zip(window[:-1], seq[:-1])) and token_is_toponym_form(window[-1], seq[-1]):
                hits.append(" ".join(window))
                break
    return hits


def mask(toks):
    """Înlocuiește toponimele și adjectivele derivate cu un token neutru."""
    seqs = toponym_token_seqs()
    out, i = [], 0
    while i < len(toks):
        matched = 0
        for seq in seqs:
            n = len(seq)
            if i + n <= len(toks) and all(w == s for w, s in zip(toks[i:i + n - 1], seq[:-1])) \
                    and token_is_toponym_form(toks[i + n - 1], seq[-1]):
                matched = n
                break
        if matched:
            out.append("TOPO")
            i += matched
        elif any(toks[i].startswith(s) for s in DERIVED_STEMS):
            out.append("TOPO")
            i += 1
        else:
            out.append(toks[i])
            i += 1
    return out


# --- Conținut -----------------------------------------------------------------
def soup(name):
    return BeautifulSoup(read(name), "html.parser")


# Elemente de tip bloc. Fiecare nod de text aparține celui mai apropiat strămoș
# din această listă, și numai lui: un <div> care conține un <p> raportează doar
# textul pus direct în el, iar textul <p>-ului rămâne blocul <p>-ului.
# Inline-urile (a, span, strong, button…) nu sunt blocuri: textul lor intră în
# blocul care le conține.
BLOCK_TAGS = {
    "p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "blockquote", "figcaption", "dd", "dt",
    "div", "section", "article", "aside", "header", "footer", "nav", "figure", "details",
    "summary", "label", "form", "fieldset", "legend", "table", "thead", "tbody", "tr",
    "td", "th", "caption", "ul", "ol", "dl", "address", "main", "body",
}


PROSE_TAGS = ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6"]


def content_blocks(name, drop=(), ui_links=True):
    """Blocurile de text din <main>, fără comentarii, scripturi, SVG, marcaje .ph
    și .ph-zone și fără legenda de placeholder (bloc protejat, identic pe toate
    paginile). `drop` = selectori CSS scoși suplimentar înainte de extracție.

    ui_links=False scoate linkurile de interfață: <a> care nu stă într-un p, li
    sau heading și nu conține la rândul lui elemente de tip bloc (butoane, CTA
    „Vezi toate…”). Linkurile din fraze rămân; la fel cardurile-link care
    conțin text structurat (lista de piese din discografie.html).

    Până la runda a șaptea, funcția citea doar p/li/h*/blockquote/figcaption/dd/dt
    și pierdea textul pus direct în <div> (faq.html ~70%, index.html ~30%)."""
    doc = soup(name)
    main = doc.find("main") or doc.body
    for c in main.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    for tag in main.find_all(["script", "svg", "style"]):
        tag.decompose()
    for sel in (".ph", ".ph-zone") + tuple(drop):
        for tag in main.select(sel):
            tag.decompose()
    if not ui_links:
        for a in main.find_all("a"):
            if not a.find_parent(PROSE_TAGS) and not a.find(sorted(BLOCK_TAGS)):
                a.decompose()
    legend = main.find("p", string=re.compile("Zonele marcate se completează"))
    if legend:
        legend.decompose()
    groups = {}
    for s in main.find_all(string=True):
        if not s.strip():
            continue
        owner = next((a for a in s.parents if a.name in BLOCK_TAGS), main)
        groups.setdefault(id(owner), []).append(str(s))
    blocks = []
    for parts in groups.values():  # dict păstrează ordinea din document
        txt = re.sub(r"\s+", " ", " ".join(parts)).strip()
        if txt:
            blocks.append(txt)
    return blocks


def jsonld(name):
    out = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', read(name), re.S):
        out.append(json.loads(raw))
    return out
