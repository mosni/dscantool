import json
import os

STATS_PATH = os.environ.get("FOOTER_STATS_PATH", "/app/stats/footer_stats.json")
_ZEROS = {"day": 0, "total": 0, "d": 0, "l": 0}


# Footer scan stats. Computed OUT-OF-BAND by `manage.py update_footer_stats` (a 30-min systemd timer) and
# written to STATS_PATH, because the 4 COUNTs take several seconds on this box (small row count but huge
# TEXT rows + a 256 MB InnoDB buffer pool). This processor only READS the precomputed file — it never
# touches the DB — so no request ever pays that cost. Falls back to zeros if the file is missing.
def template_stats(request):
    try:
        with open(STATS_PATH) as f:
            data = json.load(f)
        stats = {k: data.get(k, 0) for k in _ZEROS}
    except Exception:
        stats = dict(_ZEROS)
    return {"stats": stats}
