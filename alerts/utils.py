from urllib.parse import urljoin

from django.conf import settings
from rest_framework.reverse import reverse
from rest_framework.routers import BaseRouter
from rest_framework.viewsets import ViewSet

DEFAULT_DOMAIN = settings.DEFAULT_DOMAIN


def register_viewset(router: BaseRouter, name: str, base_name: str = ''):
    def _regist(viewset: ViewSet):
        router.register(name, viewset, base_name=base_name or None)
        return viewset

    return _regist


def absolute_reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    url = reverse(viewname, args=args, kwargs=kwargs,
                  request=request, format=format, **extra)
    if request:
        return url

    return urljoin(DEFAULT_DOMAIN, url)
