import logging, os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment

flaskApp = Flask(__name__)
flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)
login = LoginManager(flaskApp)
login.login_view = 'login'
mail = Mail(flaskApp)
bootstrap = Bootstrap(flaskApp)
moment = Moment(flaskApp)

from app import routes, models, errors

if not flaskApp.debug:
    if flaskApp.config['MAIL_SERVER']:
        auth = None
        if flaskApp.config['MAIL_USERNAME'] or flaskApp.config['MAIL_PASSWORD']:
            auth = (flaskApp.config['MAIL_USERNAME'], flaskApp.config['MAIL_PASSWORD'])
        secure = None
        if flaskApp.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(flaskApp.config['MAIL_SERVER'], flaskApp.config['MAIL_PORT']),
            fromaddr='no-reply@' + flaskApp.config['MAIL_SERVER'],
            toaddrs=flaskApp.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        flaskApp.logger.addHandler(mail_handler)
    
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    flaskApp.logger.addHandler(file_handler)

    flaskApp.logger.setLevel(logging.INFO)
    flaskApp.logger.info('Microblog startup')