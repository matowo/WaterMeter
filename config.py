import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hell0Wor79'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI ='postgres://nzedwwaiipwfjr:a55de8f65a6887a38d8f9ac5c418b5afa5e3c9fb8ea78c2ee9098d7a3c00c27e@ec2-23-21-106-241.compute-1.amazonaws.com:5432/d6qcn6gdhgmknc'

    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/pivot'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['email']
    LANGUAGES = ['en', 'sw', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL ')

    AUTHY_KEY = ''
    TWILIO_AUTH_TOKEN = ''
    TWILIO_ACCOUNT_SID = ''
    TWILIO_NUMBER = ''


    MQTT_CLIENT_ID = "pivot_iot_hub"
    MQTT_BROKER_URL = os.environ.get('MQTT_BROKER_URL') or 'm24.cloudmqtt.com'
    MQTT_BROKER_PORT = 19576
    MQTT_USERNAME = 'cosxuovc'
    MQTT_PASSWORD = 'EiZIWjLTCvYk'
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://redis-17797.c11.us-east-1-2.ec2.cloud.redislabs.com:17797/0'
    POST_PER_PAGE = 25
    REDIS_HOST = 'redis-17797.c11.us-east-1-2.ec2.cloud.redislabs.com'
    REDIS_PORT = 17797
    REDIS_DB = '0'
    REDIS_PASSWORD = 'vPs9ZLVGNCEgDkumIEJzrgfQKvMsfxyc'

    CELERY_BROKER_URL = 'redis://:vPs9ZLVGNCEgDkumIEJzrgfQKvMsfxyc@redis-17797.c11.us-east-1-2.ec2.cloud.redislabs.com:17797/0'
    BROKER_URL = CELERY_BROKER_URL
    CELERY_RESULT_BACKEND = CELERY_BROKER_URL

    # MONGODB SET_UP
    __mongo_doc__ = ""
    MONGODB_HOST_NAME = "ds257858.mlab.com"
    MONGODB_PORT = 57858
    MONGODB_DBNAME = ""
    MONGODB_USERNAME = "intelecs_sensors"
    MONGODB_PASSWORD = "intelecs3232"

    # CKEDITOR
    DIR = os.path.join(os.path.dirname(__file__), 'app/static')
    CKEDITOR_FILE_UPLOADER = 'upload'
    UPLOADED_PATH = os.path.join(DIR, 'upload')

    SUPPORTED_LANGUAGES = {'sw': 'Swahili', 'en': 'English'}
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

    # TWILIO
    AUTHY_KEY = 'TBBWGGPaYk3GfTId0VUv1za4i0o2Uil2'
    TWILIO_ACCOUNT_SID = 'AC8bc0dd53a382f8fb556dcde01447e921'
    TWILIO_AUTH_TOKEN = 'a8ee4cf9270c0fdacbed1c264946c4c6'
    TWILIO_NUMBER = '+12012920895'


    # A WHERE API
    A_WHERE_CONSUMER_KEY = 'k1CZ5kPJQ8DY3292JaLd2ARU5pafZkCE'
    A_WHERE_CONSUMER_SECRET = 'oCWGioF1ubGxMKPR'

    PESA_PAL_CONSUMER = 'IU5LNHtKJZSJjj3fLsV1iQKRIxnkzOFY'
    PESA_PAL_SECRECT = 'jM2GRNgzUjgJcKthv2l6yoChP+A='


