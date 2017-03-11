import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = r'\xf7E\x16\xab\xc2\xfe\x17{\xeb\xc4Q\x8e9\xd5\x18\x1b\x82\x14[|p<\x14'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/bankdb'
    print SQLALCHEMY_DATABASE_URI

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
