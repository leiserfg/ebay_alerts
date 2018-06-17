from django.db import transaction
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Alert, Customer
from .serializers import (AlertSerializer, CreateAlertSerializer,
                          CustomerSerializer)
from .utils import register_viewset

router = SimpleRouter()

owner_param = openapi.Parameter('owner', in_=openapi.IN_QUERY, description='Owner of the alert',
                                type=openapi.TYPE_STRING)


@method_decorator(name='list', decorator=swagger_auto_schema(manual_parameters=[owner_param]))
@register_viewset(router, 'alerts', 'alert')
class AlertView(ModelViewSet):
    def get_queryset(self):
        queryset = Alert.objects.all()
        if self.action != 'list':
            return queryset

        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            return queryset.filter(owner=owner)
        return queryset.none()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateAlertSerializer
        return AlertSerializer

    @swagger_auto_schema(responses={204: 'Unsuscribed', 404: 'Does not exist'})
    @action(methods=['get'], detail=True)
    def unsuscribe(self, request, pk=None):
        alert = self.get_object()
        alert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True)
    def suscribe(self, request, pk=None):
        alert: Alert = self.get_object()
        alert.enabled = True
        alert.save()
        serializer = AlertSerializer(alert)
        return Response(serializer.data)


@register_viewset(router, 'customers')
class CustomerView(RetrieveModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
