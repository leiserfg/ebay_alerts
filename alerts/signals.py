from django.db.models.signals import post_save
from django.dispatch import receiver

from .emails import subscription
from .models import Alert


@receiver(post_save, sender=Alert, dispatch_uid="create_subscription")
def create_subscription(sender, instance, created, **kwargs):
    if created:
        subscription(instance)
