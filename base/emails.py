from django.conf import settings
from django.core.mail import send_mail    # this is a funstion in  django which help to send mail 

def send_account_activation_email(email, email_token):
    subject = "your accounts needs to be verified"
    email_from = settings.EMAIL_HOST_USER
    message = f'Hi , click on the link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'

    send_mail(subject, message , email_from , [email])

