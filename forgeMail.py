from SMTP import SMTP


def main():

    host = input("SMTP Host: ")
    port = input("SMTP Port: ")

    print("Creating the connection")
    connection = SMTP(host, str(port))

    username = input('Username: ')
    password = input('Password: ')
    connection.login(username, password)

    sender = input('Sender: ')
    sender_name = input('Sender name: ')
    receiver = input('Receiver: ')

    subject = input('Subject: ')
    html = ''

    message = connection.create_message(sender, sender_name, receiver, subject, html)

    connection.send_mail(message)


if __name__ == "__main__":
    main()
