from django.conf import settings
from django.template import loader

from .models import Alert, Customer
from .tasks.send_mail_async import send_mail_async
from .utils import absolute_reverse

mail_sender = settings.MAIL_SENDER    # TODO


def _subscribe_action(alert: Alert):
    return absolute_reverse('alert-suscribe', args=[alert.id])


def _unsuscribe_action(alert: Alert):
    return absolute_reverse('alert-unsuscribe', args=[alert.id])


def _manager_action(customer: Customer):
    return absolute_reverse('customer-detail', args=[customer.id])


def subscription(alert: Alert):
    email = alert.owner.email
    frequency = alert.get_frequency_display()
    search_terms = alert.search_terms

    ctx = dict(
        email=email,
        frequency=frequency,
        search_terms=search_terms,
        actions=[{'text': 'Confirm Subscription',
                  'link': _subscribe_action(alert)},
                 {'text': 'Manage your notifications',
                  'link': _manager_action(alert.owner)}]
    )
    template_txt = loader.get_template('alerts/subscription.txt')
    template_html = loader.get_template('alerts/subscription.html')

    message = template_txt.render(ctx)
    message_html = template_html.render(ctx)
    send_mail_async(
        'Alert Subscription',
        message,
        mail_sender,
        [email],
        html_message=message_html
    )


def send_alert(alert: Alert, items):
    email = alert.owner.email
    frequency = alert.get_frequency_display()
    search_terms = alert.search_terms

    ctx = dict(
        email=email,
        frequency=frequency,
        search_terms=search_terms,
        items=items,
        actions=[{'text': 'Unsuscribe',
                  'link': _unsuscribe_action(alert)},
                 {'text': 'Manage your notifications',
                  'link': _manager_action(alert.owner)}]
    )
    template_txt = loader.get_template('alerts/alert.txt')
    template_html = loader.get_template('alerts/alert.html')

    message = template_txt.render(ctx)
    message_html = template_html.render(ctx)
    send_mail_async(
        'Alert',
        message,
        mail_sender,
        [email],
        html_message=message_html
    )
