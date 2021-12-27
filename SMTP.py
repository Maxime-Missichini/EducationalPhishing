import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SMTP:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = host + ':' + port
        self.server = None
        self.sender = None
        self.receiver = None

        self.connect()
        self.start_tls()

    # Exchange with the server
    def ehlo(self):
        try:
            print('Sending ehlo to the server')
            self.server.ehlo()
        except smtplib.SMTPHeloError:
            print('The server did not respond to the EHLO')
            exit(1)

    def connect(self):
        try:
            print('Connection to the SMTP socket')
            self.server = smtplib.SMTP(self.host, self.port)
            print('Connection established')
        except OSError:
            print('Error while trying to connect to the socket')
            exit(1)

    def start_tls(self):
        self.ehlo()
        try:
            print('Starting SSL')
            self.server.starttls()
            print('SSL established')
        except RuntimeError:
            print('SSL/TLS failed')
            exit(1)

    def login(self, username, password):
        try:
            print('Trying to login')
            self.server.login(username, password)
            print('Successfully logged')
        except smtplib.SMTPAuthenticationError:
            print('Bad combinaison of username/password')
        except smtplib.SMTPNotSupportedError:
            print('Authentication not supported')
        except smtplib.SMTPException:
            print('Error during authentication')

    def create_message(self, sender, name, receiver, subject, html):

        print('Creating the message')
        self.sender = sender
        self.receiver = receiver

        message = MIMEMultipart('alternative')
        message.set_charset('utf-8')
        message['From'] = name + '<' + sender + '>'
        message['Subject'] = subject
        message['To'] = receiver

        body = MIMEText(html, 'html')
        message.attach(body)

        print('Message created: ' + message.as_string())

        return message

    def send_mail(self, message):
        try:
            print('Sending spoofed mail')
            self.server.sendmail(self.sender, self.receiver, message.as_string())
            print('Message successfully sent !')
        except smtplib.SMTPException:
            print('Error while sending the mail')
            exit(1)
