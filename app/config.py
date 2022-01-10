from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    UPLOADED_PATH = path.join(basedir, 'uploads')
    BASE_URL = 'https://functions.yandexcloud.net/d4e4kbm7oeqfaj0ebhps/'
    DROPZONE_UPLOAD_MULTIPLE = True
    DROPZONE_ALLOWED_FILE_CUSTOM = True
    DROPZONE_ALLOWED_FILE_TYPE = '.dxf'
    DROPZONE_MAX_FILES = 10
    DROPZONE_REDIRECT_VIEW = 'index'
    API_REQUEST_TIMEOUT = 60


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    APP_BASE_URL = 'https://any-cut-nester-ui.herokuapp.com'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    APP_BASE_URL = 'http://localhost:5000'
