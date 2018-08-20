import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class SmtpEmail:
    def __init__(self, server, user='', password=''):
        self.server = server
        self.user = user
        self.password = password

    def send(self, from_email, to, subject, body, image_list):
        try:
            msg_root = MIMEMultipart('related')
            msg_root['Subject'] = subject
            msg_root['From'] = from_email
            msg_root['To'] = to
            msg_root.preamble = 'This is a multi-part message in MIME format.'

            msg_alternative = MIMEMultipart('alternative')
            msg_root.attach(msg_alternative)

            msgText = MIMEText('This is the alternative plain text message.')
            msg_alternative.attach(msgText)

            msgText = MIMEText(body, 'html')
            msg_alternative.attach(msgText)

            for image in image_list:
                fp = open(image, 'rb')
                msg_image = MIMEImage(fp.read(), name=os.path.basename(image))
                fp.close()

                msg_root.attach(msg_image)

            mailserver = self.__get_mailserver()
            # mailserver.sendmail(from_email, to.split(", "), msg_root.as_string())
            mailserver.send_message(msg_root)

            mailserver.quit()
            return True
        except:
            return False

    def __get_mailserver(self):
        mailserver = smtplib.SMTP(self.server, 25)
        # mailserver.set_debuglevel(1)
        mailserver.ehlo()

        assert self.user == None and self.password == None or self.user != None and self.password != None
        if self.user != '':
            mailserver.starttls()
            mailserver.login(self.user, self.password)

        return mailserver
