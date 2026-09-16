"""4.3 / 6.3 — Numărul de marcaje .ph per pagină (ținta pe cluster și serviciu: ≤ 9).

Numără elementele cu class="ph" (marcaj inline) și, separat, sloturile
.ph-zone folosite în markup — nu aparițiile din comentariile blocului <style>.
"""
import sys

from _common import ALL_PAGES, CLUSTER, SERVICE, soup

LIMIT = 9


def main():
    over = 0
    limited = CLUSTER + SERVICE
    for page in ALL_PAGES:
        doc = soup(page)
        ph = doc.select(".ph")
        zones = doc.select(".ph-zone")
        flag = ""
        if page in limited and len(ph) > LIMIT:
            flag = "  PESTE LIMITĂ"
            over += 1
        print(f"{page:22} .ph={len(ph):>3}  .ph-zone={len(zones):>2}{flag}")
        if page in limited:
            for el in ph:
                print(f"    · {el.get_text(' ', strip=True)}")
    return 1 if over else 0


if __name__ == "__main__":
    sys.exit(main())
