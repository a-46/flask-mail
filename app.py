import os 
from flask import Flask
from flask-mail import Mail

app = Flask(__name__)

app.config.update(
    MAIL_SERVER=os.getrnv('MAIL_SERVER')
    MAIL_PORT=465
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER=('dezhao', os.getenv(MAIL_USERNAME))

)

mail = Mail(app)
