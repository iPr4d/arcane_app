import os
import sys

SECRET_KEY='Dj}wexP1|nkf@!T?!0WKs*@k'

ARCANE_APP_ID= 1200420960103822

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'arcane_app/databases.sqlite')

SQLALCHEMY_TRACK_MODIFICATIONS=True

TESTING = False
