from django.db import transaction
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet

from .models import Alert, Customer
from .serializers import AlertSerializer, CreateAlertSerializer
from .utils import register_viewset

router = SimpleRouter()

owner_param = openapi.Parameter('owner', in_=openapi.IN_QUERY, description='Owner of the alert',
                                type=openapi.TYPE_STRING)


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[owner_param]))
@register_viewset(router, 'alerts', 'alert')
class AlertView(ModelViewSet):
    def get_queryset(self):
        queryset = Alert.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            return queryset.filter(owner__email=owner)
        return queryset.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAlertSerializer
        return AlertSerializer
