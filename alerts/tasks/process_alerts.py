from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task, task

from ..models import Alert


@task()
def process_alert(alert):
    print(alert.owner.email)


@db_periodic_task(crontab(minute='*'))
def search_for_notifications():
    for alert in Alert.need_for_notification().prefetch_related('owner'):
        process_alert(alert)
