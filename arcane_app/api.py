## import required packages

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

from models import *


app = Flask(__name__)


## define app configuration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'databases.sqlite')

db = SQLAlchemy(app)



## Create new user

@app.route("/user", methods=["POST"])
def add_user():
    name = request.json['name']
    first_name=request.json['first_name']
    birth_date=request.json['birth_date']
    username = request.json['username']
    password = request.json['password']
    birth_date2=datetime.date(int(birth_date[0:4]),int(birth_date[5:7]),int(birth_date[8:10]))

    new_user=create_new_user(name,first_name,birth_date2,username,password)

    return user_schema.jsonify(new_user)

## Create new good 

@app.route("/good", methods=["POST"])
def add_good():
    name = request.json['name']
    description=request.json['description']
    type = request.json['type']
    city = request.json['city']
    nb_rooms= request.json['nb_rooms']
    rooms_charac = request.json['rooms_charac']
    owner_id=1 ## à modifier

    new_good=create_new_good(name,description,type,city,int(nb_rooms),rooms_charac, owner_id)

    return good_schema.jsonify(new_good)

## Modify existing good

@app.route("/good/<id>", methods=["PUT"])
def modif_good(id):
    selected_good=Good.query.get(id)
    name = request.json['name']
    description=request.json['description']
    type = request.json['type']
    city = request.json['city']
    nb_rooms= request.json['nb_rooms']
    rooms_charac = request.json['rooms_charac']

    selected_good.modify_good(name,description,type,city,int(nb_rooms),rooms_charac)
    modified_good=Good.query.get(id)

    return good_schema.jsonify(modified_good)

## Modify existing user

@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    name = request.json['name']
    first_name=request.json['first_name']
    birth_date=request.json['birth_date']
    birth_date2=datetime.date(int(birth_date[0:4]),int(birth_date[5:7]),int(birth_date[8:10]))
    username = request.json['username']
    password = request.json['password']

    user.modify_infos(name,first_name,birth_date2,username,password)
    modified_user=User.query.get(id)

    return user_schema.jsonify(modified_user)

## Get all goods from a city

@app.route("/goods/<city>", methods=["GET"])
def good_detail(city):
    selected_goods = Good.query.filter(Good.city == city).all()
    result = goods_schema.dump(selected_goods)
    return goods_schema.jsonify(result.data)





