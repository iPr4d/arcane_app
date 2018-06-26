# coding=utf-8
from flask_sqlalchemy import SQLAlchemy
import datetime
import timestring

from views import app

## Lien Flask/SQL

db = SQLAlchemy(app)

## Création de la classe des biens avec leurs attributs

class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    nb_rooms = db.Column(db.Integer, nullable=False)
    rooms_charac = db.Column(db.Text)  ## pas d'obligation d'insertion
    owner_id = db.Column(db.Integer, nullable=False)


## Ces fonctions à l'intérieur de la classe Good sont celles qui permettent de réaliser la première fonctionnalité du microservice
## Pour chaque instance de cette classe, on crée une fonction de modification en demandant la nouvelle entrée à l'utilisateur

    def modify_name(self):
        new_name = input(' Nouveau nom du bien : ')
        id_not_modified_good=self.id
        new_good = Good(id=id_not_modified_good,name=new_name, description=self.description, type=self.type, city=self.city,
                        nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification du nom du bien réussie')

    def modify_des(self):
        new_description = input(' Nouvelle description du bien : ')
        id_not_modified_good=self.id
        new_good = Good(id=id_not_modified_good,name=self.name, description=new_description, type=self.type, city=self.city,
                        nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification de la description du bien réussie')

    def modify_type(self):
        new_type = input(' Nouveau type du bien : ')
        id_not_modified_good = self.id
        new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=new_type,
                        city=self.city,
                        nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification du type de bien réussie')

    def modify_city(self):
        new_city = input(' Nouvelle ville du bien : ')
        id_not_modified_good = self.id
        new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=self.type,
                        city=new_city,
                        nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification de la ville du bien réussie')

    def modify_nb_rooms(self):
        new_nb_rooms = input(' Nouveau nombre de pièces du bien : ')
        id_not_modified_good = self.id
        new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=self.type,
                        city=self.city,
                        nb_rooms=new_nb_rooms, rooms_charac=self.rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification du nombre de pièces réussie')

    def modify_rooms_charac(self):
        new_rooms_charac = input(' Nouvelle description des pièces du bien : ')
        id_not_modified_good = self.id
        new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=self.type,
                        city=self.city,
                        nb_rooms=self.nb_rooms, rooms_charac=new_rooms_charac, owner_id=self.owner_id)
        db.session.delete(self)
        db.session.add(new_good)
        db.session.commit()
        print(' Modification de la description des pièces réussie')

    def modify_owner(self):
        new_owner_name = input(' Nom du nouveau propriétaire : ')
        new_owner_fname =input(' Prénom du nouveau propriétaire : ')
        new_date_birth=input(' Date de naissance du nouveau propriétaire (format YYYY/MM/JJ) : ')

        ## Dans cette sous-partie de la fonction, on va tester si le nouveau propriétaire est déjà ou non dans
        ## notre base d'utilisateurs

        same_name_list=User.query.filter_by(name=new_owner_name).all()
        for i in len(test1):
            test2=[]
            same_first_name=test1[i].query.filter_by(first_name=new_owner_fname).all()
        test3=test2.query.filter_by(birth_date=new_date_birth).all()

        if test3 is None:
            new_user=User(name=new_owner_name,first_name=new_owner_fname,birth_date=new_date_birth)
            db.session.add(new_user)
            db.session.commit()
            print('Nouvel utilisateur créé, modification du propriétaire du bien à venir...')
            id_not_modified_good = self.id
            new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=self.type,
                            city=self.city,
                            nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=new_user.id)
            db.session.delete(self)
            db.session.add(new_good)
            db.session.commit()
            print(' Modification de propriétaire réussie')

        else:
            id_not_modified_good = self.id
            new_good = Good(id=id_not_modified_good, name=self.name, description=self.description, type=self.type,
                            city=self.city,
                            nb_rooms=self.nb_rooms, rooms_charac=self.rooms_charac, owner_id=test3.id)
            db.session.delete(self)
            db.session.add(new_good)
            db.session.commit()
            print(' Modification de propriétaire réussie')





## Création de la classe des utilisateurs avec leurs attributs

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)

    def __str__(self, name, first_name):
        return (self.name + ' ' + self.first_name)

    def create_new_user():
        new_user_name=input('Quel est votre nom ? ')
        new_user_fname=input('Quel est votre prénom ? ')
        new_user_bd=input('Quelle est votre date de naissance ? (AAAA/MM/JJ) ')
        new_user_bd2=datetime.date(int(new_user_bd[0:3]),int(new_user_bd[5:7]),int(new_user_bd[8:10]))
        new_user=User(name=new_user_name,first_name=new_user_fname,birth_date=new_user_bd2)
        db.session.add(new_user)
        db.session.commit()
        print('Création de votre espace utilisateur réussi, votre ID est : ' + str(new_user.id))

    def modify_infos(self):
        id_not_modified=self.id
        db.session.delete(self)
        new_user_name=input('Quel est votre nouveau nom ? ')
        new_user_fname=input('Quel est votre nouveau prénom ? ')
        new_user_bd=input('Quelle est votre nouvelle date de naissance ? (AAAA/MM/JJ) ')
        new_user_bd2=datetime.date(int(new_user_bd[0:3]),int(new_user_bd[5:7]),int(new_user_bd[8:10]))
        new_user=User(id=id_not_modified,name=new_user_name,first_name=new_user_fname,birth_date=new_user_bd2)
        db.session.add(new_user)
        db.session.commit()
        print('Modification de vos informations personnelles réussie, votre ID est toujours : ' + str(new_user.id))

db.create_all()

## Cette partie là du code est simplement pour éviter la création d'une nouvelle base SQL à chaque redémarrage côté serveur

import logging as lg

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(User(name='Dupont', first_name='Jean', birth_date=datetime.date(1971, 2, 23)))
    db.session.add(User(name='Martin', first_name='Francois', birth_date=datetime.date(1965, 5, 17)))
    db.session.add(Good(name='Appartement T2 à louer coeur de Paris',
                       description='Très bel appartemment situé quartier Saint_paul....', type='Appartement',
                       city='Paris', nb_rooms=2, rooms_charac='Chambre de 16m2, cuisine équipée...', owner_id=1))
    db.session.commit()
    lg.warning('Database initialized!')
