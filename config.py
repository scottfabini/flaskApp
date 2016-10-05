import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Common to all configs
class Config:
    SECRET_KEY = '2ED35C78BC8F58B54F83A291A1EE4'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKAPP_MAIL_SUBJECT_PREFIX = '[FlaskApp]'
    FLASKAPP_MAIL_SENDER = 'FlaskApp Admin <flasky@example.com>'
    FLASKAPP_ADMIN = os.environ.get('FLASKAPP_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# A helper dictionary for selecting config options
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
