import os 
from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)


app.config.update(
    MAIL_SERVER=os.getenv('MAIL_SERVER'),
    MAIL_PORT=465,
    MAIL_USE_SSL = True,
    MAIL_USE_TLS = True,
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_DEFAULT_SENDER=('dezhao', os.getenv('MAIL_USERNAME')),

)

mail = Mail(app)
'''
def send_mail(subject,to,body):
    message = Message(subject, recipients=[to], body=body)
    mail.send(message)

send_mail('hello','janall <janall@163.com>','1234567899')
2112694290
message= Message(subject='abc', recipients=['janall <2112694290@qq.com>'], body='1234666') 
from flask_mail import Message
from app import mail
'''