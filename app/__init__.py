import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask, request, current_app, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from elasticsearch import Elasticsearch
from redis import Redis

import rq
from celery import Celery
from config import Config
from flask_sslify import SSLify
from pymongo import MongoClient
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_ckeditor import CKEditor
from flask_wtf import CSRFProtect
from flask_marshmallow import Marshmallow
import flask_excel as excel


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please Log in to access this page')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
# sslify = SSLify()
babel = Babel()
mqtt = Mqtt()
socketio = SocketIO()
ckeditor = CKEditor()
marshmallow = Marshmallow()
csrf = CSRFProtect()

mongo_client = MongoClient(Config.MONGODB_HOST_NAME, Config.MONGODB_PORT)
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
mongodb = mongo_client.smart_sensors
try:
    mongodb.authenticate(Config.MONGODB_USERNAME, Config.MONGODB_PASSWORD)
except Exception as e:
    print(" * [INFO] Error " + str(e) + " Occured")

try:
    redis = Redis(
        host='redis-17797.c11.us-east-1-2.ec2.cloud.redislabs.com',
        port=17797,
        db=0,
        password='vPs9ZLVGNCEgDkumIEJzrgfQKvMsfxyc'
    )
except Exception as e:
    print("[INFO]Error " + str(e) + " Occured")


def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_class)
    #sslify.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    socketio.init_app(app)
    mqtt.init_app(app)
    ckeditor.init_app(app)
    csrf.init_app(app)
    marshmallow.init_app(app)
    excel.init_excel(app)

    # Celery
    celery.conf.update(app.config)

    app.jinja_env.auto_reload = True

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('pivot_hub', connection=app.redis)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    from app.adminstrator import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='pivot_hub',
                credentials=auth, secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/pivot_logs.log',
                                               maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Intelecs startup")

    return app


@babel.localeselector
def get_locale():
    #return 'sw'
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])


from app import models
