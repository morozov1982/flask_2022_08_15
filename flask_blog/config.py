from os import environ
from dotenv import load_dotenv


load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'postgres://ryzwaxrcsvglft:d89851a207aa5415eafcf37572d088d55589eb40cbd84362ce7a22b53f4ec6c2@ec2-34-253-119-24.eu-west-1.compute.amazonaws.com:5432/da1ggg35aq97vr'
    SECRET_KEY = environ.get('KEY')

    # gmail config
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = USERNAME
    # MAIL_PASSWORD = PASSWORD

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = environ.get('YA_USERNAME')
    MAIL_PASSWORD = environ.get('YA_PASSWORD')
