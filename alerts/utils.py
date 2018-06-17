from urllib.parse import urljoin, urlparse
from urllib.request import getproxies

from django.conf import settings
from ebaysdk.finding import Connection as finding
from rest_framework.reverse import reverse
from rest_framework.routers import BaseRouter
from rest_framework.viewsets import ViewSet

DEFAULT_DOMAIN = settings.DEFAULT_DOMAIN
EBAY_ID = settings.EBAY_ID
EBAY_DOMAIN = settings.EBAY_DOMAIN
DEBUG = settings.DEBUG


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


def _resolve_proxy():
    # I need it
    proxies = getproxies()
    http_proxy = proxies.get('http', None) or proxies.get(
        'https', 'http://:80')
    parts = urlparse(http_proxy)
    return parts.hostname or None, parts.port or 80


def search_on_ebay(search_term, count=20, order_by='PricePlusShippingLowest'):
    proxy_host, proxy_port = _resolve_proxy()

    api = finding(debug=DEBUG, appid=EBAY_ID, domain=EBAY_DOMAIN,
                  config_file=None, proxy_host=proxy_host, proxy_port=proxy_port)
    result = api.execute('findItemsAdvanced',
                         dict(keywords=search_term, sortOrder=order_by,
                              paginationInput={'entriesPerPage': count}),
                         )
    return result.reply.searchResult.item
