#!/usr/bin/env python3
"""Prototip (zone-mockup/*.html) -> JSON Elementor pentru ioana-balan.ro.

Aceeasi gramatica ca paginile construite pe 9 sept. (3782, 3819, 3815, 3821):
- containere flex native, text in widget-uri native legate de __globals__;
- componente compuse in widget HTML. Diferenta fata de paginile vechi: markup-ul
  lor pastreaza clasele Tailwind din prototip, compilate o singura data, scopate
  sub .ib-tw, in assets/zone.css (vezi build_css.sh). Nu se scrie CSS per componenta.

Iesire: migrare/out/<fisier>.json = {meta:{...}, elements:[...]}
Imaginile raman ca token {{IMG:<baza>}} si se rezolva pe server (lib.php).
"""
import json, re, sys, os, html as H
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'zone-mockup')
OUT = os.path.join(ROOT, 'migrare', 'out')
SLUGS = json.load(open(os.path.join(ROOT, 'migrare', 'slug-map.json')))

# ---- tokeni --------------------------------------------------------------
G_COL = {  # culoare prototip -> global Elementor
    'text-on-surface': 'primary', 'text-white': 'primary',
    'text-on-surface-variant': 'secondary', 'text-secondary': 'secondary',
    'text-primary': 'secondary',
}
HEX = {'primary': '#E5E2E1', 'secondary': '#C6C6C6'}

def rem(v):
    return round(float(v) * 4)  # tailwind: 1 unitate = 0.25rem = 4px

def spacing(classes, prop):
    """mb-4 md:mb-12 -> (mobile, desktop) px; prop in m/p + t/b/l/r/x/y."""
    base = md = None
    for c in classes:
        bp = ''
        if ':' in c:
            bp, c = c.split(':', 1)
        named = {'margin-desktop': 64, 'margin-mobile': 16, 'gutter': 24, 'unit': 8}
        mn = re.fullmatch(prop + r'-([a-z-]+)', c)
        if mn and mn.group(1) in named:
            v = named[mn.group(1)]
            if bp == '':
                base = v
            elif bp == 'md':
                md = v
            continue
        m = re.fullmatch(prop + r'-(\d+(?:\.\d+)?)', c)
        if not m:
            m2 = re.fullmatch(prop + r'-\[(\d+)px\]', c)
            if not m2:
                continue
            v = int(m2.group(1))
        else:
            v = rem(m.group(1))
        if bp == '':
            base = v
        elif bp == 'md':
            md = v
    if md is None:
        md = base
    return base, md

def dim(t=0, r=0, b=0, l=0, unit='px'):
    return {'unit': unit, 'top': str(t), 'right': str(r), 'bottom': str(b), 'left': str(l), 'isLinked': False}

def size(v, unit='px'):
    return {'unit': unit, 'size': v, 'sizes': []}

MAXW = {'max-w-md': 448, 'max-w-xl': 576, 'max-w-2xl': 672, 'max-w-3xl': 768, 'max-w-4xl': 896,
        'max-w-5xl': 1024, 'max-w-max-width': 1200}

# ---- linkuri ---------------------------------------------------------------
def rewrite_href(h):
    if not h or h.startswith(('http', 'mailto:', 'tel:', '#')):
        return h
    path, _, frag = h.partition('#')
    b = os.path.basename(path)
    if b in SLUGS['new']:
        u = SLUGS['new'][b]['path']
    elif b in SLUGS['live']:
        u = SLUGS['live'][b]
    else:
        raise SystemExit(f'link nemapat: {h}')
    return u + ('#' + frag if frag else '')

IMG_RE = re.compile(r'(?:\.\./)?assets/img/([a-z0-9-]+?)(?:-(?:480|640|694|800|1024|1304|1440))?\.(?:jpg|webp|png)')

def fix_markup(tag):
    for a in tag.find_all('a', href=True):
        a['href'] = rewrite_href(a['href'])
    # <picture> -> <img> cu token; srcset-ul il pune serverul
    for pic in tag.find_all('picture'):
        img = pic.find('img')
        base = IMG_RE.search(img['src']).group(1)
        new = BeautifulSoup('', 'html.parser').new_tag('img')
        for k, v in img.attrs.items():
            if k in ('src', 'srcset', 'sizes'):
                continue
            new[k] = v
        new['src'] = '{{IMG:%s}}' % base
        new['data-ib-img'] = base
        pic.replace_with(new)
    for img in tag.find_all('img'):
        if '{{IMG' not in img.get('src', ''):
            base = IMG_RE.search(img['src']).group(1)
            img['src'] = '{{IMG:%s}}' % base
            img['data-ib-img'] = base
            for k in ('srcset', 'sizes'):
                img.attrs.pop(k, None)
    for c in tag.find_all(string=lambda s: isinstance(s, type(tag.string)) and False):
        pass
    return tag

def strip_comments(tag):
    from bs4 import Comment
    for c in tag.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()

# ---- constructie -----------------------------------------------------------
class Page:
    def __init__(self, code):
        self.code = code
        self.n = 0

    def id(self):
        self.n += 1
        return f'{self.code}{self.n:03x}'

def cls(t):
    return t.get('class', []) if isinstance(t, Tag) else []

def is_eyebrow(t):
    c = cls(t)
    return t.name == 'span' and 'uppercase' in c and any('tracking-[0.2em]' in x for x in c)

def is_text_p(t):
    """Paragraf de text simplu: fara link-buton (uppercase)."""
    if t.name != 'p':
        return False
    for a in t.find_all('a'):
        if 'uppercase' in cls(a):
            return False
    if t.find(['svg', 'img', 'div']):
        return False
    # badge-uri si alte span-uri stilizate raman in HTML; .ph e CSS global (zone.css)
    for d in t.find_all(True):
        if d.name != 'a' and cls(d) and cls(d) != ['ph']:
            return False
    return True

TEXTISH = ('h1', 'h2', 'h3', 'h4')

def is_text_wrapper(t):
    if t.name != 'div':
        return False
    kids = [k for k in t.children if isinstance(k, Tag)]
    if not kids:
        return False
    for k in kids:
        if not (is_eyebrow(k) or k.name in TEXTISH or is_text_p(k)):
            return False
    return True

def margins(t):
    c = cls(t)
    mt_b, mt_d = spacing(c, 'mt')
    mb_b, mb_d = spacing(c, 'mb')
    s = {}
    if any(v for v in (mt_b, mt_d, mb_b, mb_d)):
        s['_margin'] = dim(mt_d or 0, 0, mb_d or 0, 0)
        s['_margin_tablet'] = dim(mt_d or 0, 0, mb_d or 0, 0)
        s['_margin_mobile'] = dim(mt_b or 0, 0, mb_b or 0, 0)
    else:
        s['_margin'] = dim(0, 0, 0, 0)
    return s

def own_width_css(t):
    c = cls(t)
    mw = next((MAXW[x] for x in c if x in MAXW), None)
    css = ''
    if mw:
        css += 'selector{max-width:%dpx !important}' % mw
        if 'mx-auto' in c:
            css += 'selector{margin-left:auto;margin-right:auto}'
    return css

def color_of(t, default='secondary'):
    for c in cls(t):
        if c in G_COL:
            return G_COL[c]
    return default

def inner_html(t):
    return ''.join(str(x) for x in t.contents).strip()

def clean_inline(t):
    """Text native: scot clasele Tailwind de pe <a> (stilul de link vine din components.css)."""
    for a in t.find_all('a'):
        a.attrs.pop('class', None)
    return t

def w_heading(P, t, align):
    lvl = t.name if t.name in TEXTISH else 'div'
    c = cls(t)
    if lvl == 'h1' or 'font-display-lg' in c:
        typo = 'primary'
    elif 'font-headline-lg' in c:
        typo = 'secondary'
    elif 'font-headline-md' in c:
        typo = 'lead'
    else:
        typo = 'lead'
    col = color_of(t, 'primary')
    s = {'title': inner_html(clean_inline(fix_markup(t))), 'header_size': lvl, 'title_color': HEX[col],
         '__globals__': {'title_color': f'globals/colors?id={col}', 'typography_typography': f'globals/typography?id={typo}'}}
    if align:
        s['align'] = align
    s.update(margins(t))
    if own_width_css(t):
        s['custom_css'] = own_width_css(t)
    if t.get('id'):
        s['_element_id'] = t['id']
    return {'id': P.id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': s, 'elements': []}

def w_eyebrow(P, t, align):
    col = color_of(t, 'secondary')
    s = {'title': t.get_text(strip=True), 'header_size': 'div', 'title_color': HEX[col],
         'typography_typography': 'custom', 'typography_font_family': 'Inter',
         'typography_font_size': size(14), 'typography_font_weight': '600',
         'typography_text_transform': 'uppercase', 'typography_letter_spacing': size(0.2, 'em'),
         'typography_line_height': size(20),
         '__globals__': {'title_color': f'globals/colors?id={col}'}}
    if align:
        s['align'] = align
    s.update(margins(t))
    return {'id': P.id(), 'elType': 'widget', 'widgetType': 'heading', 'settings': s, 'elements': []}

def w_text(P, t, align):
    c = cls(t)
    if 'font-display-lg' in c:
        typo, dcol = 'stat', 'primary'
    elif 'font-headline-md' in c:
        typo, dcol = 'lead', 'primary'
    else:
        typo = 'quote' if any('body-lg' in x for x in c) else 'text'
        dcol = 'secondary'
    col = color_of(t, dcol)
    fix_markup(t)
    clean_inline(t)
    body = inner_html(t)
    s = {'editor': f'<p>{body}</p>', 'text_color': HEX[col], 'custom_css': 'selector p{margin:0}' + own_width_css(t),
         '__globals__': {'text_color': f'globals/colors?id={col}', 'typography_typography': f'globals/typography?id={typo}'}}
    if align:
        s['align'] = align
    s.update(margins(t))
    return {'id': P.id(), 'elType': 'widget', 'widgetType': 'text-editor', 'settings': s, 'elements': []}

def w_html(P, t, css=''):
    fix_markup(t)
    s = {'html': f'<div class="ib-tw">{t}</div>'}
    if css:
        s['custom_css'] = css
    return {'id': P.id(), 'elType': 'widget', 'widgetType': 'html', 'settings': s, 'elements': []}

FAQ_CSS = ('selector{margin-bottom:16px}selector h3{margin:0;padding-right:16px;font-family:"EB Garamond",Georgia,serif;'
           'font-size:16px;font-weight:500;line-height:1.375;color:var(--e-global-color-primary)}'
           '@media(min-width:768px){selector h3{font-size:24px}}'
           'selector .faq-item__answer{font-family:Inter,sans-serif;font-size:16px;line-height:1.6}'
           'selector .faq-item__answer p{margin:0}selector .faq-item__answer p+p{margin-top:12px}')
CHEVRON = ('<svg aria-hidden="true" width="24" height="24" viewBox="0 -960 960 960" fill="currentColor">'
           '<path d="M480-357.85 253.85-584l32.61-32.61L480-423.08l193.54-193.53L706.15-584 480-357.85Z"/></svg>')

def w_faq(P, item):
    """Markup-ul exact de pe paginile live (3819), nu cel din prototip."""
    d = item.find('details')
    q = d.find('summary').find('h3')
    ans = d.find('summary').find_next_sibling('div')
    fix_markup(ans)
    for a in ans.find_all('a'):
        a.attrs.pop('class', None)
    op = d.has_attr('open')
    body = inner_html(ans)
    h = (f'<div class="faq-item"><details{" open" if op else ""}><summary aria-expanded="{"true" if op else "false"}">'
         f'<h3>{inner_html(q)}</h3>{CHEVRON}</summary><div class="faq-item__answer">{body}</div></details></div>')
    return {'id': P.id(), 'elType': 'widget', 'widgetType': 'html', 'settings': {'html': h, 'custom_css': FAQ_CSS}, 'elements': []}

def cmargins(t):
    """Containerele Elementor citesc 'margin', nu '_margin' (verificat pe CSS-ul generat, 30.09)."""
    return {k.lstrip('_'): v for k, v in margins(t).items()}

def container(P, elements, **s):
    base = {'container_type': 'flex', 'content_width': 'full', 'flex_direction': 'column',
            'padding': dim(0, 0, 0, 0), 'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0', 'isLinked': True}}
    base.update(s)
    return {'id': P.id(), 'elType': 'container', 'settings': base, 'elements': elements, 'isInner': True}

def wrapper_container(P, t, kids, align):
    c = cls(t)
    s = {}
    mw = next((MAXW[x] for x in c if x in MAXW), None)
    if mw:
        s['width'] = size(mw)
        s['width_mobile'] = size(100, '%')
    css = ''
    if mw:
        css += 'selector{max-width:100%}'
    if 'mx-auto' in c:
        s['_flex_align_self'] = 'center'
        css += 'selector{margin-left:auto;margin-right:auto}'
    gb, gd = spacing(c, 'gap')
    if gd:
        s['flex_gap'] = {'unit': 'px', 'size': gd, 'column': str(gd), 'row': str(gd), 'isLinked': True}
    s.update(cmargins(t))
    if css:
        s['custom_css'] = css
    return container(P, kids, **s)

def convert_children(P, parent, align):
    out = []
    for k in parent.children:
        if not isinstance(k, Tag):
            continue
        c = cls(k)
        if is_eyebrow(k):
            out.append(w_eyebrow(P, k, align))
        elif k.name in TEXTISH:
            out.append(w_heading(P, k, align))
        elif is_text_p(k):
            out.append(w_text(P, k, align))
        elif k.name == 'div' and any(x.startswith('space-y') for x in c) and k.find(class_='faq-item'):
            items = [w_faq(P, it) for it in k.find_all('div', class_='faq-item', recursive=False)]
            s = {'width': size(768), 'width_mobile': size(100, '%'), 'custom_css': 'selector{max-width:100%}'}
            s.update(cmargins(k))
            out.append(container(P, items, **s))
        elif is_text_wrapper(k):
            sub_align = 'center' if 'text-center' in c else align
            out.append(wrapper_container(P, k, convert_children(P, k, sub_align), sub_align))
        else:
            out.append(w_html(P, k))
    return out

def pad_settings(c, px_fallback=(24, 64)):
    pyb, pyd = spacing(c, 'py')
    ptb, ptd = spacing(c, 'pt')
    pbb, pbd = spacing(c, 'pb')
    tb, td = (ptb if ptb is not None else pyb) or 0, (ptd if ptd is not None else pyd) or 0
    bb, bd = (pbb if pbb is not None else pyb) or 0, (pbd if pbd is not None else pyd) or 0
    xm, xd = px_fallback
    return {'padding': dim(td, xd, bd, xd), 'padding_tablet': dim(td, xd, bd, xd), 'padding_mobile': dim(tb, xm, bb, xm)}

def section_css(c):
    css = []
    if any(x.startswith('border-b') for x in c):
        css.append('selector{border-bottom:1px solid rgba(68,71,72,.1)}')
    if any(x.startswith('border-t') for x in c):
        css.append('selector{border-top:1px solid rgba(68,71,72,.1)}')
    return ''.join(css)

def bg_settings(c):
    if 'bg-surface-container-low' in c:
        return {'background_background': 'classic', 'background_color': '#1C1B1B',
                '__globals__': {'background_color': 'globals/colors?id=surfacealt'}}, 'selector{background-color:#1C1B1B}'
    if 'bg-surface-container-lowest' in c:
        return {'background_background': 'classic', 'background_color': '#0E0E0E',
                '__globals__': {'background_color': 'globals/colors?id=hairline'}}, 'selector{background-color:#0E0E0E}'
    return {'background_background': 'classic', 'background_color': '#131313',
            '__globals__': {'background_color': 'globals/colors?id=surface'}}, 'selector{background-color:#131313}'

def top_container(P, elements, boxed, c, extra_css='', align=None, **more):
    bg, bgcss = bg_settings(c)
    s = {'container_type': 'flex', 'content_width': 'boxed', 'boxed_width': size(boxed),
         'flex_direction': 'column', 'flex_gap': {'unit': 'px', 'size': 0, 'column': '0', 'row': '0', 'isLinked': True}}
    if align == 'center':
        # fara flex_align_items:center - widget-urile HTML s-ar strange pe continut (butoanele w-full)
        extra_css += 'selector{text-align:center}'
    s.update(bg)
    s['custom_css'] = bgcss + section_css(c) + extra_css
    s.update(more)
    return {'id': P.id(), 'elType': 'container', 'settings': s, 'elements': elements, 'isInner': False}

def convert_hero(P, sec):
    inner = sec.find('div', class_='z-10')
    c_in = cls(inner)
    col = inner.find('div', recursive=False)  # max-w-3xl
    kids = convert_children(P, col, None)
    content = wrapper_container(P, col, kids, None)
    img = sec.find('img')
    base = IMG_RE.search(img['src']).group(1)
    pos = 'center 6%' if 'object-[center_6%]' in cls(img) else 'center center'
    s = pad_settings(c_in)
    s.update({'background_image': {'url': '{{IMG:%s}}' % base, 'id': '{{IMGID:%s}}' % base, 'size': '', 'alt': '', 'source': 'library'},
              'background_size': 'cover', 'background_position': 'center center',
              'background_overlay_background': 'gradient', 'background_overlay_color': '#131313',
              'background_overlay_opacity': size(1), 'background_overlay_color_stop': size(0, '%'),
              'background_overlay_color_b': 'rgba(19,19,19,0.72)', 'background_overlay_color_b_stop': size(100, '%'),
              'background_overlay_gradient_type': 'linear', 'background_overlay_gradient_angle': size(0, 'deg')})
    sc = cls(sec)
    el = top_container(P, [content], 1072, [], extra_css=f'selector{{background-position:{pos}}}', **s)
    el['settings']['background_background'] = 'classic'
    el['settings'].pop('background_color', None)
    el['settings']['__globals__'] = {}
    el['settings']['custom_css'] = section_css(sc) + f'selector{{background-position:{pos}}}'
    if sec.get('aria-labelledby'):
        el['settings']['_element_id'] = 'hero'
    return el

def convert_section(P, sec):
    c = cls(sec)
    if sec.find('div', class_='absolute', recursive=False) and sec.find('img'):
        return convert_hero(P, sec)
    align = 'center' if 'text-center' in c else None
    if 'max-w-max-width' in c:
        # sectiune standard: max 1200 + px-6/md:px-64 pe acelasi element
        s = pad_settings(c)
        kids = convert_children(P, sec, align)
        return top_container(P, kids, 1072, c, align=align, **s)
    # sectiune full-bleed (CTA final): fundalul pe section, latimea pe div-ul interior
    inner = [k for k in sec.children if isinstance(k, Tag)]
    assert len(inner) == 1, sec.get('class')
    inner = inner[0]
    ic = cls(inner)
    mw = next((MAXW[x] for x in ic if x in MAXW), 1200)
    s = pad_settings(c)
    xb, xd = spacing(ic, 'px')
    xb, xd = xb or 24, xd or 64
    for k in ('padding', 'padding_tablet'):
        s[k]['left'] = s[k]['right'] = str(xd)
    s['padding_mobile']['left'] = s['padding_mobile']['right'] = str(xb)
    kids = convert_children(P, inner, align)
    return top_container(P, kids, mw - 2 * xd, c, align=align, **s)

def convert_divider(P, div):
    h = {'id': P.id(), 'elType': 'widget', 'widgetType': 'html', 'settings': {'html': '<div class="zona-divider"></div>'}, 'elements': []}
    return top_container(P, [h], 1072, [], padding=dim(0, 64, 0, 64), padding_tablet=dim(0, 64, 0, 64), padding_mobile=dim(0, 24, 0, 24))

def meta_of(soup, fname):
    title = soup.title.get_text(strip=True)
    desc = soup.find('meta', attrs={'name': 'description'})
    ld = [json.loads(s.string) for s in soup.find_all('script', type='application/ld+json')]
    sm = SLUGS['new'][fname]
    h1 = soup.find('h1').get_text(' ', strip=True)
    return {'src': fname, 'slug': sm['slug'], 'parent': sm['parent'], 'noindex': sm['noindex'],
            'seo_title': title, 'metadesc': desc['content'] if desc else '', 'jsonld': ld, 'h1': h1}

def convert(fname, code):
    soup = BeautifulSoup(open(os.path.join(SRC, fname)), 'html.parser')
    meta = meta_of(soup, fname)
    main = soup.find('main')
    strip_comments(main)
    P = Page(code)
    els = []
    for k in main.children:
        if not isinstance(k, Tag):
            continue
        c = cls(k)
        if k.name == 'section':
            els.append(convert_section(P, k))
        elif k.find(class_='zona-divider'):
            els.append(convert_divider(P, k))
        elif 'bg-surface-container-lowest' in c and k.find('p') and 'date reale' in k.get_text():
            continue  # legenda de placeholder: doar pentru review-ul prototipului
        else:
            raise SystemExit(f'{fname}: bloc necunoscut {c}')
    return {'meta': meta, 'elements': els}

TITLES = {'zone.html': 'Zone deservite', 'nunta.html': 'Nuntă', 'botez.html': 'Botez',
          'eveniment-privat.html': 'Eveniment privat', 'corporate.html': 'Evenimente corporate',
          'repertoriu.html': 'Repertoriu', 'formatia.html': 'Formația', 'folclor-si-manele.html': 'Folclor și petrecere'}

def post_title(fname, soup_meta):
    if fname in TITLES:
        return TITLES[fname]
    return None  # zonele: numele judetului, din badge

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    files = sys.argv[1:] or sorted(SLUGS['new'])
    for f in files:
        code = re.sub(r'[^a-z]', '', f.replace('zona-', 'z').replace('.html', ''))[:4]
        data = convert(f, code)
        soup = BeautifulSoup(open(os.path.join(SRC, f)), 'html.parser')
        t = post_title(f, data['meta'])
        if not t:
            badge = soup.find(class_='zona-badge').get_text(strip=True)
            t = badge.split('Județul')[-1].strip()
        data['meta']['title'] = t
        json.dump(data, open(os.path.join(OUT, f.replace('.html', '.json')), 'w'), ensure_ascii=False)
        print(f, len(data['elements']), 'sectiuni', t)
