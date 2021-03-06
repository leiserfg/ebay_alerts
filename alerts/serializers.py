from rest_framework import serializers

from .models import Alert, Customer


class AlertSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    frequency_name = serializers.CharField(
        source='get_frequency_display', read_only=True)

    class Meta:
        model = Alert
        exclude = ('updated_minute',)


class CreateAlertSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    frequency_name = serializers.CharField(
        source='get_frequency_display', read_only=True)

    class Meta:
        model = Alert
        # id field is hidden to avoid someone spamming a customer
        fields = ('email', 'search_terms', 'frequency', 'frequency_name')

    def create(self, validated_data):
        data = validated_data.copy()
        email = data.pop('email')
        return Alert.create_with_email(email, **data)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
