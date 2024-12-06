class Config():
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI="sqlite:///BlogLiteDb.sqlite3"
    DEBUG=True

    SECRET_KEY='THIS-IS-THE-MOST-SECURE-KEY'
    SECURITY_PASSWORD_HASH="bcrypt"
    SECURITY_PASSWORD_SALT="THIS#IS$THE%MOST&SECURE*SALT"
    WTF_CSRF_ENABLED=False
    SECURITY_TOKEN_AUTHENTICATION_HEADER="Authentication-Token"