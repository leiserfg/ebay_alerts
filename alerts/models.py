import uuid
from datetime import datetime

from django.db import models

LOW = 2
NORMAL = 10
HIGH = 30

FREQUENCY_CHOICES = (
    (LOW, 'Every 2 minutes'),
    (NORMAL, 'Every 10 minutes'),
    (HIGH, 'Every 30 minutes'),
)


class ModelWithUUID(models.Model):
    # Using uuid1 to ensure temporal order
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid1,
        editable=False)

    class Meta:
        abstract = True


class Customer(ModelWithUUID):
    email = models.EmailField()

    def __str__(self):
        return self.email


def _datetime_to_mins(when=None):
    if when is None:
        when = datetime.utcnow()
    return int((when - datetime(1970, 1, 1)).total_seconds() / 60)


class Alert(ModelWithUUID):
    owner = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='alerts')
    search_terms = models.CharField(max_length=50, blank=False, null=False)
    frequency = models.IntegerField(choices=FREQUENCY_CHOICES, default=NORMAL)
    enabled = models.BooleanField(default=False)
    updated_minute = models.IntegerField()

    @staticmethod
    def create_with_email(email: str, **kwargs):
        owner, _ = Customer.objects.get_or_create(email=email)
        return Alert.objects.create(owner=owner, **kwargs)

    def save(self, *args, **kwargs):
        self.updated_minute = _datetime_to_mins()
        self.full_clean()
        super().save(*args, **kwargs)

    @staticmethod
    def need_for_notification(when=None):
        # Using the last minute, thats way the customer
        # donesn't needs to wait a complete period
        last_min = _datetime_to_mins(when) - 1
        F = models.F
        to_notify = (last_min - F('updated_minute')) % F('frequency')
        return Alert.objects.filter(enabled=True).annotate(
            to_notify=to_notify).filter(to_notify=0)
