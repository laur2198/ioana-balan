#!/usr/bin/env bash
# Rulează toate verificările din /zone-mockup/verify/, în ordinea din brief.
cd "$(dirname "$0")" || exit 1
export PYTHONDONTWRITEBYTECODE=1
status=0
for s in bag_of_words.py non_duplicare.py marcaje.py integritate.py linkuri_noi.py; do
  echo "=================================================================="
  echo "  $s"
  echo "=================================================================="
  python3 "$s" || status=1
  echo
done
exit $status
