import uuid

from django.db import models

LOW = 2
NORMAL = 10
HIGH = 30

FREQUENCY_CHOICES = (
    (LOW, 'For every 2 minutes'),
    (NORMAL, 'For every 10 minutes'),
    (HIGH, 'For every 30 minutes'),
)


class ModelWithUUID(models.Model):
    # ids as uuid  'cause they will be exposed
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)

    class Meta:
        abstract = True


class Costumer(ModelWithUUID):
    email = models.EmailField()


class Alert(ModelWithUUID):
    owner = models.ForeignKey(
        Costumer, on_delete=models.CASCADE, related_name='alerts')
    search_terms = models.CharField(max_length=50, blank=False, null=False)
    frequency = models.IntegerField(choices=FREQUENCY_CHOICES, default=NORMAL)
    enabled = models.BooleanField(default=False)


class Response(models.Model):
    alert = models.ForeignKey(
        Alert, on_delete=models.CASCADE, related_name='responses')
    sended = models.BooleanField(default=False)


class Item(models.Model):
    response = models.ForeignKey(
        Response, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=50)
    url = models.URLField()
