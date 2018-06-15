from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import ModelViewSet

from .models import Alert, Customer
from .serializers import AlertSerializer
from .utils import register_viewset

router = SimpleRouter()


@register_viewset(router, 'alerts')
class AlertView(ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
