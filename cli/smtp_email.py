import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtpEmail:
    def __init__(self, server, user='', password=''):
        self.server = server
        self.user = user
        self.password = password

    def send(self, from_email, to, subject, body):
        try:
            mailserver = smtplib.SMTP(self.server, 25)
            # mailserver.set_debuglevel(1)
            mailserver.ehlo()

            assert self.user == None and self.password == None or self.user != None and self.password != None
            if self.user != '':
                mailserver.starttls()
                mailserver.login(self.user, self.password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to

            part = MIMEText(body, 'html')
            msg.attach(part)

            mailserver.send_message(msg)
            mailserver.quit()
            return True
        except:
            return False
