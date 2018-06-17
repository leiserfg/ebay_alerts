from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task, task

from ..models import Alert
from ..utils import search_on_ebay


@task()
def process_alert(alert: Alert):
    from ..emails import send_alert  # here for avoid cyclic import
    items = search_on_ebay(alert.search_terms)
    send_alert(alert, items)


@db_periodic_task(crontab(minute='*'))
def search_for_notifications():
    for alert in Alert.need_for_notification().prefetch_related('owner'):
        process_alert(alert)
