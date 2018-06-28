#! /usr/bin/env python
from arcane_app import app
import os

cdir = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    app.run(debug=True)