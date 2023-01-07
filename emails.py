from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path
import requests

my_mail = EmailMessage()

html_template = Template(Path('templates/index.html').read_text())
html_content = html_template.substitute({'name': 'Bob', 'date': 'tomorrow'})

my_mail['from'] = "kos"
my_mail['to'] = 'test@gmail.com'
my_mail['subject'] = 'Hello from python'
my_mail.set_content(html_content, 'html')

with open('images/forest.jpg', 'rb') as attaches:
    att_data = attaches.read()
    my_mail.add_attachment(att_data, 'image', 'jpg')

with smtplib.SMTP(host='127.0.0.1', port=2525) as server:
    server.ehlo()
    # server.starttls()
    # server.login(user='', password='')
    server.send_message(my_mail)
    print('send')
