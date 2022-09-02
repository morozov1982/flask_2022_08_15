from config_vars import KEY, USERNAME, PASSWORD, YA_USERNAME, YA_PASSWORD


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = KEY

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
    MAIL_USERNAME = YA_USERNAME
    MAIL_PASSWORD = YA_PASSWORD
