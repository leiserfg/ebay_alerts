from rest_framework import serializers

from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    frequency_name = serializers.CharField(
        source='get_frequency_display', read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Alert
        fields = '__all__'
