from .models import Scan
from datetime import timedelta
from django.utils import timezone

# Provides settings from the configuration file in templates
def template_stats(request):
    # disabled in prod: these 4 per-request COUNTs (unindexed, full-table) were the page slowdown
    dscans = 0
    localscans = 0
    total = 0
    day = 0
    return {
        'stats': {
            "day": day,
            "total": total,
            "d": dscans,
            "l": localscans
        }
    }
