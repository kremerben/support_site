from __future__ import unicode_literals
from django.conf import settings


def api_v1_root(request):
    """
    Adds api v1 root context variables to content.
    """
    return {'APIV1ROOT': settings.APIV1ROOT}

