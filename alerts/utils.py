from json import load
from pathlib import Path
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
fake_response = Path(__file__).parent / 'fake_ebay.json'


def register_viewset(router: BaseRouter, name: str, base_name: str = ''):
    """
    Adds a biewset to a router 
    """
    def _regist(viewset: ViewSet):
        router.register(name, viewset, base_name=base_name or None)
        return viewset

    return _regist


def absolute_reverse(viewname, args=None, kwargs=None, request=None, format=None, **extra):
    """
    Used in emails when you have not a request
    """
    url = reverse(viewname, args=args, kwargs=kwargs,
                  request=request, format=format, **extra)
    if request:
        return url

    return urljoin(DEFAULT_DOMAIN, url)


def absolute_url(url, request=None):
    if request:
        return request.build_absolute_uri(url)
    return urljoin(DEFAULT_DOMAIN, url)


def search_on_ebay(search_term, count=20, order_by='PricePlusShippingLowest'):
    #  For avoiding ebay slow responses and proxis on development
    if EBAY_DOMAIN == 'fake':
        return load(fake_response.open())

    api = finding(appid=EBAY_ID, domain=EBAY_DOMAIN,
                  config_file=None)
    result = api.execute('findItemsAdvanced',
                         dict(keywords=search_term, sortOrder=order_by,
                              paginationInput={'entriesPerPage': count}),
                         )
    return result.reply.searchResult.item
