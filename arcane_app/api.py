## import required flask packages to build app and api

from flask import Flask, request, jsonify, g, abort
from flask_sqlalchemy import SQLAlchemy

## import packages to manage authentication

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

## function to verify user password

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

## Other importations

import os
import sys
import datetime
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)
from models import *


## defining app

app = Flask(__name__)


## define app configuration

pardir = os.path.abspath(os.path.pardir)

app.config.from_pyfile(os.path.join(pardir, 'arcane/config.py'))

## defining database

db = SQLAlchemy(app)


## endpoint 1 : Create new user

@app.route("/user", methods=["POST"])
def add_user():
    name = request.json['name']
    first_name=request.json['first_name']
    birth_date=request.json['birth_date']
    username = request.json['username']
    password = request.json['password']
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user

    birth_date2=datetime.date(int(birth_date[0:4]),int(birth_date[5:7]),int(birth_date[8:10]))


    new_user=create_new_user(name,first_name,birth_date2,username,password)

    return user_schema.jsonify(new_user)

## endpoint 2 : Create new good -> authentication needed to know who's the owner

@app.route("/good", methods=["POST"])
@auth.login_required
def add_good():
    name = request.json['name']
    description=request.json['description']
    type = request.json['type']
    city = request.json['city']
    nb_rooms= request.json['nb_rooms']
    rooms_charac = request.json['rooms_charac']
    owner_id=g.user.get_id() ## the owner is the authenticated user

    new_good=create_new_good(name,description,type,city,int(nb_rooms),rooms_charac, owner_id)

    return good_schema.jsonify(new_good)

## endpoint 3 : Modify existing good -> authentication needed

@app.route("/good/<id>", methods=["PUT"])
@auth.login_required
def modif_good(id):

## testing if the authenticated user is the selected good owner

    selected_good=Good.query.get(id)
    if g.user.get_id()!=selected_good.owner_id:
        abort(400, " This authenticated user cannot modify this good : he's not the owner ") ## not the owner

## if yes, we allow the user to modify his own good infos

    name = request.json['name']
    description=request.json['description']
    type = request.json['type']
    city = request.json['city']
    nb_rooms= request.json['nb_rooms']
    rooms_charac = request.json['rooms_charac']

    selected_good.modify_good(name,description,type,city,int(nb_rooms),rooms_charac)

    modified_good=Good.query.get(id)

    return good_schema.jsonify(modified_good)

## endpoint 4 : Modify existing user : need authentication

@app.route("/user/<id>", methods=["PUT"])
@auth.login_required
def user_update(id):
    if int(g.user.get_id())!=int(id):
        abort(400, "This authenticated user cannot modify these informations : not his personal account") 
    user = User.query.get(id)
    name = request.json['name']
    first_name=request.json['first_name']
    birth_date=request.json['birth_date']
    birth_date2=datetime.date(int(birth_date[0:4]),int(birth_date[5:7]),int(birth_date[8:10]))
    password = request.json['password']

    user.modify_infos(name,first_name,birth_date2,password)

    modified_user=User.query.get(id)

    return user_schema.jsonify(modified_user)

## endpoint 5 : Get all goods from a city

@app.route("/goods/<city>", methods=["GET"])
def good_detail(city):
    selected_goods = Good.query.filter(Good.city == city).all()
    result = goods_schema.dump(selected_goods)
    return goods_schema.jsonify(result.data)

