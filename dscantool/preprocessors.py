from datetime import datetime, timezone

from django.conf import settings
from django.utils import timezone as dj_timezone


# Promo banner shown on every page within this window (UTC)
PROMO_START = datetime(2026, 10, 22, 11, 0, tzinfo=timezone.utc)
PROMO_END = datetime(2026, 10, 29, 11, 0, tzinfo=timezone.utc)


# Provides settings from the configuration file in templates
def template_settings(request):
    return {
        'debug': settings.DEBUG,
        'show_promo': PROMO_START <= dj_timezone.now() < PROMO_END,
    }
