from django.template import loader

from .models import Alert
from .tasks import send_mail_async


def subscription(alert: Alert):
    email = alert.owner.email
    frequency = alert.get_frequency_display()
    search_terms = alert.search_terms

    ctx = dict(
        email=email,
        frequency=frequency,
        search_terms=search_terms,
        actions=[]
    )
    template_txt = loader.get_template('alerts/subscription.txt')
    template_html = loader.get_template('alerts/subscription.html')

    message = template_txt.render(ctx)
    message_html = template_html.render(ctx)
    send_mail_async(
        'Alert Subscription',
        message,
        'yo@mail.com',
        [email],
        html_message=message_html
    )
