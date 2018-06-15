from rest_framework import serializers

from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Alert
        fields = '__all__'
