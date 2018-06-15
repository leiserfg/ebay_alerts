from django.db import transaction
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet

from .models import Alert, Customer
from .serializers import AlertSerializer, CreateAlertSerializer
from .utils import register_viewset

router = SimpleRouter()


@register_viewset(router, 'alerts')
class AlertView(ModelViewSet):
    queryset = Alert.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAlertSerializer
        return AlertSerializer
