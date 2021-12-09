import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = input('from :')
email['to'] = input('enter sender email id: ')
email['subject'] = input('subject : ')

email.set_content(html.substitute({'name':input('type name : ')}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(input('your email_id : '),input('password : '))  # If you using gmail as a hostname a google will mail you a securit email like to solve this just "yes it was me" after that go to manage your google account than security than scroll down find less secure app access than turn it on
    smtp.send_message(email)
    print('all good')
