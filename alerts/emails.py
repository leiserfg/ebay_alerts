from django.template import loader

from .models import Alert, Customer
from .tasks.send_mail_async import send_mail_async
from .utils import absolute_reverse

mail_sender = 'sender@mail.com'    # TODO


def _subscribe_action(customer: Customer):
    return absolute_reverse('alert-suscribe', args=[customer.id])


def _unsuscribe_action(customer: Customer):
    return absolute_reverse('alert-unsuscribe', args=[customer.id])


def subscription(alert: Alert):
    email = alert.owner.email
    frequency = alert.get_frequency_display()
    search_terms = alert.search_terms

    ctx = dict(
        email=email,
        frequency=frequency,
        search_terms=search_terms,
        actions=[{'text': 'Confirm Subscription',
                  'link': _subscribe_action(alert.owner)}]
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


def send_alert(alert: Alert, response):
    email = alert.owner.email
    frequency = alert.get_frequency_display()
    search_terms = alert.search_terms

    ctx = dict(
        email=email,
        frequency=frequency,
        search_terms=search_terms,
        response=response,
        actions=[{'text': 'Unsuscribe',
                  'link': _unsuscribe_action(alert.owner)}]
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
