from rest_framework.routers import BaseRouter
from rest_framework.viewsets import ViewSet


def register_viewset(router: BaseRouter, name: str, base_name: str = ''):
    def _regist(viewset: ViewSet):
        router.register(name, viewset, base_name=base_name or None)
        return viewset

    return _regist
