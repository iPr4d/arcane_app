# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
import timestring
import json

from api import app

## Link Flask/SQL

db = SQLAlchemy(app)
ma = Marshmallow(app)

## Define good class

class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    nb_rooms = db.Column(db.Integer, nullable=False)
    rooms_charac = db.Column(db.Text)  
    owner_id = db.Column(db.Integer, nullable=False)

## modify selected good infos method

    def modify_good(self,new_name,new_description,new_type,new_city,new_nb_rooms,new_rooms_charac):
        id_not_modified_good=self.id
        owner_id=self.owner_id
        db.session.delete(self)
        new_good = Good(id=id_not_modified_good,name=new_name, description=new_description, type=new_type, city=new_city,
                        nb_rooms=new_nb_rooms, rooms_charac=new_rooms_charac, owner_id=owner_id)
        db.session.add(new_good)
        db.session.commit()

## ## independant function to create new Good object

def create_new_good(name,description,type,city,nb_rooms,rooms_charac,owner_id):
    new_good=Good(name=name, description=description, type=type, city=city,
                        nb_rooms=nb_rooms, rooms_charac=rooms_charac, owner_id=owner_id)
    db.session.add(new_good)
    db.session.commit()
    return new_good

## Define User class

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    username=db.Column(db.String(80), unique=True)
    password=db.Column(db.String(80), unique=False)

##  modify selected user infos method

    def modify_infos(self,new_user_name,new_user_fname,new_user_bd,new_user_username,new_user_password):
        id_not_modified=self.id
        db.session.delete(self)
        new_user=User(id=id_not_modified,name=new_user_name,first_name=new_user_fname,birth_date=new_user_bd,username=new_user_username,password=new_user_password)
        db.session.add(new_user)
        db.session.commit()

## independant function to create new User object

def create_new_user(new_user_name,new_user_fname,new_user_bd,new_user_username,new_user_password):
    new_user=User(name=new_user_name,first_name=new_user_fname,birth_date=new_user_bd, username=new_user_username,password=new_user_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

## JSON needs

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name','first_name','birth_date','username', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class GoodSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name','description','type','city','nb_rooms','rooms_charac','owner_id')


good_schema = GoodSchema()
goods_schema = GoodSchema(many=True)


db.create_all()

## Good database initialization


import logging as lg

def init_db():
    db.session.add(Good(name='Appartement T2 à louer coeur de Paris',
                       description='Très bel appartemment situé quartier Saint_paul....', type='Appartement',
                       city='Paris', nb_rooms=2, rooms_charac='Chambre de 16m2, cuisine équipée...', owner_id=1))
    db.session.commit()
    lg.warning('Database initialized!')


