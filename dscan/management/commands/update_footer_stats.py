import json
import os
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from dscan.models import Scan

STATS_PATH = os.environ.get("FOOTER_STATS_PATH", "/app/stats/footer_stats.json")


class Command(BaseCommand):
    help = "Recompute footer scan stats out-of-band and write them to FOOTER_STATS_PATH."

    def handle(self, *args, **options):
        now = timezone.now()
        stats = {
            "total": Scan.objects.count(),
            "day": Scan.objects.filter(created__gte=now - timedelta(hours=24)).count(),
            "d": Scan.objects.filter(type=Scan.DSCAN).count(),
            "l": Scan.objects.filter(type=Scan.LOCALSCAN).count(),
            "updated": now.isoformat(),
        }
        os.makedirs(os.path.dirname(STATS_PATH), exist_ok=True)
        tmp = STATS_PATH + ".tmp"
        with open(tmp, "w") as f:
            json.dump(stats, f)
        os.replace(tmp, STATS_PATH)
        self.stdout.write("footer stats: %s" % stats)
