from flask import Flask
from flask_admin import Admin
import sys

app = Flask(__name__)


if __name__ == "__main__":
    app.run()


app.config.from_pyfile('/Users/antoinepradier/PycharmProjects/ARCANE/config.py')
