import os

SECRET_KEY='Dj}wexP1|nkf@!T?!0WKs*@k'

ARCANE_APP_ID= 1200420960103822

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
