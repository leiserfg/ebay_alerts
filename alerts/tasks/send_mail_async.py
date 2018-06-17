from django.core.mail import send_mail
from huey.contrib.djhuey import task


@task()
def send_mail_async(subject, message, from_email, recipient_list,
                    html_message=None):
    send_mail(subject, message, from_email, recipient_list,
              html_message=html_message)
