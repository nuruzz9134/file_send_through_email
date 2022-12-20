from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import threading



class SendEmail(threading.Thread):

    def __init__(self , email , subject , message):
        self.email=email
        self.subject=subject
        self.message = message
        threading.Thread.__init__(self)


    def run(self):

        

        email_from = settings.EMAIL_HOST
        email_message = EmailMessage(self.subject,self.message,email_from,[self.email])
        email_message.attach_file("/email_attach_file/pdf_file/Resume")
        email_message.send()
