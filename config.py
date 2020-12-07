
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False
    
class TestConfiguration(BaseConfiguration):
    TESTING = True

    CSRF_ENABLED = False

    DATABASE = 'tests.db'
    DATABASE_PATH = os.path.join(_basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # + DATABASE_PATH

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig
}
