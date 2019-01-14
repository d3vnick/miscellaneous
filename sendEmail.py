import shutil
import smtplib
import sys

from os.path import basename
from datetime import date
from email.message import EmailMessage

today = date.today()

email_username = 'email@example.com'
from_addr = email_username
to_addr = email_username
subject = 'A subject'

smtp_addr = 'smpt.an.email.provider.com:587'


def sendEmail(example_filename_to_attach):

    # Ask Password
    password = input('email password: ')
    if password is None or password == '':
        print('Wrong password, try again')
        sys.exit(1)

    # Metadata
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['To'] = to_addr
    msg['From'] = from_addr
    ctype = 'application/zip'
    maintype, subtype = ctype.split('/', 1)

    # Attachments
    print('Attaching {}'.format(example_filename_to_attach))
    with open(example_filename_to_attach, 'rb') as file:
        msg.add_attachment(file.read(),
                           maintype=maintype,
                           subtype=subtype,
                           filename='zipefile.zip'.format(today))

    # Sending
    print("Sending email...")
    s = smtplib.SMTP(smtp_addr)
    print('EHLO...')
    s.ehlo()
    print('Start TLS')
    s.starttls()
    print('Login')
    s.login(email_username, password)
    print('Sending...')
    s.sendmail(from_addr, [to_addr], msg.as_string())
    print('Sent.')
    s.quit()
