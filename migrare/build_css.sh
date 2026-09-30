#!/usr/bin/env bash
# Construieste migrare/out/zone.css pentru child theme (assets/zone.css).
# 1. mini-preflight scopat pe .ib-tw (Tailwind fara preflight nu are border-style)
# 2. blocul <style> comun celor 28 de pagini din zone-mockup (identic pe toate)
# 3. utilitarele Tailwind folosite efectiv, compilate cu config-ul prototipului, sub .ib-tw
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TW="${TW_DIR:-/tmp/claude-0/tw}"
OUT="$ROOT/migrare/out/zone.css"
mkdir -p "$ROOT/migrare/out"

node -e '
global.tailwind={};require(process.argv[1]);
const c=tailwind.config;c.content=[process.argv[2]+"/zone-mockup/*.html"];
c.important=".ib-tw";c.corePlugins={preflight:false};
require("fs").writeFileSync(process.argv[3]+"/tailwind.config.cjs","module.exports="+JSON.stringify(c));
' "$ROOT/assets/tailwind.config.js" "$ROOT" "$TW"
echo '@tailwind utilities;' > "$TW/in.css"
(cd "$TW" && npx tailwindcss -c tailwind.config.cjs -i in.css -o util.css --minify 2>/dev/null)

python3 - "$ROOT" "$TW/util.css" "$OUT" <<'EOF'
import re,sys
root,util,out=sys.argv[1:]
h=open(root+'/zone-mockup/zona-prahova.html').read()
st=re.search(r'<style>(.*?)</style>',h,re.S).group(1)
st=re.sub(r'/\*.*?\*/','',st,flags=re.S)
st=re.sub(r'\s+',' ',st).strip()
pre=('/* zone.css - generat de migrare/build_css.sh din zone-mockup. Nu se editeaza manual. */\n'
 ':root{--accent-edge:#C41236;--outline:#8e9192}\n'
 '/* preflight cu :where() = specificitate 0: componentele din site.css (.motif-rule__gem etc.) castiga */\n'
 ':where(.ib-tw),:where(.ib-tw) *,:where(.ib-tw) *::before,:where(.ib-tw) *::after{box-sizing:border-box;border-width:0;border-style:solid;border-color:#444748}\n'
 ':where(.ib-tw) :where(h1,h2,h3,h4,p,blockquote,figure,ol,ul,dl,dd){margin:0}\n'
 ':where(.ib-tw) :where(ol,ul){list-style:none;padding:0}\n'
 ':where(.ib-tw) :where(h1,h2,h3,h4){font-size:inherit;font-weight:inherit;line-height:inherit;color:inherit}\n'
 ':where(.ib-tw) :where(a){color:inherit;text-decoration:inherit}\n'
 ':where(.ib-tw) :where(img,svg){display:block;max-width:100%}:where(.ib-tw) :where(img){height:auto}\n'
 ':where(.ib-tw) :where(summary){list-style:none}.ib-tw summary::-webkit-details-marker{display:none}\n'
 '.ib-tw{font-family:Inter,sans-serif;font-size:16px;color:#e5e2e1;line-height:1.5}\n')
open(out,'w').write(pre+st+'\n'+open(util).read()+'\n')
print(out, len(open(out).read()))
EOF
