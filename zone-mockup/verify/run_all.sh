#!/usr/bin/env bash
# Rulează toate verificările din /zone-mockup/verify/, în ordinea din brief.
#
# Cod de ieșire:
#   0 — toate scripturile au ieșit cu 0
#   1 — cel puțin un script a raportat eșec SAU a crăpat (inclusiv la import)
#   2 — dependențele lipsesc; nu s-a rulat nimic
#
# Codul fiecărui script se capturează în `rc` IMEDIAT după `python3`, înainte de
# orice `echo`. Un `echo` intercalat ar suprascrie `$?` și un script crăpat ar
# trece neobservat.
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1

SCRIPTS=(bag_of_words.py non_duplicare.py marcaje.py integritate.py linkuri_noi.py)

# --- Preflight: dependențele, înainte de orice verificare ---------------------
# Fără el, un `ModuleNotFoundError` arată la fel ca un eșec de conținut, iar
# raportul per script devine un zid de stacktrace-uri identice.
if ! python3 - <<'PY'
import sys
lipsa = []
for modul, pachet in (("bs4", "beautifulsoup4"), ("soupsieve", "soupsieve")):
    try:
        __import__(modul)
    except ImportError:
        lipsa.append((modul, pachet))
if lipsa:
    print("DEPENDENȚE LIPSĂ — nu s-a rulat nicio verificare:", file=sys.stderr)
    for modul, pachet in lipsa:
        print("  · %-12s (pachetul %s)" % (modul, pachet), file=sys.stderr)
    print("\nInstalează-le cu:", file=sys.stderr)
    print("  pip install -r zone-mockup/verify/requirements.txt", file=sys.stderr)
    sys.exit(1)
PY
then
  exit 2
fi

status=0
declare -a REZULTATE=()

for s in "${SCRIPTS[@]}"; do
  echo "=================================================================="
  echo "  $s"
  echo "=================================================================="
  python3 "$s"
  rc=$?                    # IMEDIAT după python3, înainte de orice echo
  if [ "$rc" -ne 0 ]; then
    status=1
    REZULTATE+=("$s|EȘEC (cod $rc)")
  else
    REZULTATE+=("$s|ok")
  fi
  echo
done

echo "=================================================================="
echo "  REZULTAT PER SCRIPT"
echo "=================================================================="
for r in "${REZULTATE[@]}"; do
  printf '  %-22s %s\n' "${r%%|*}" "${r#*|}"
done
echo
if [ "$status" -eq 0 ]; then
  echo "  Toate cele ${#SCRIPTS[@]} verificări au trecut."
else
  echo "  Cel puțin o verificare a eșuat — vezi mai sus."
fi

exit $status
