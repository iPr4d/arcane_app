# arcane_app

Pour faire tourner l'API en local, veuillez suivre les instructions suivantes :

### Installations et versions nécessaires

- utiliser les versions de Python et de Flask telles que fixées dans le fichier `requirements.txt`

- installer les packages nécessaires à l'application décrits dans `requirements.txt`

### Exécution du script

- exécuter le script `run.py` dans une fenêtre de Terminal

- ouvrir une nouvelle fenêtre de Terminal

### Utilisation des fonctionnalités : commandes bash à utiliser dans la 2ème fenêtre du terminal


- **Créer un nouvel utilisateur** : requête POST

`curl -i -H "Content-type: application/json" -X POST -d 'user_json' http://127.0.0.1:5000/user `

L'objet *user_json* au format JSON contiendra alors toutes les caractéristiques de l'utilisateur que l'on souhaite créer.

Par exemple, pour l'utilisateur Jean Dupont, né le 12/05/1994 ayant pour nom d'utilisateur `jdupont` et pour mot de passe `motdepasse1` :

` user_json = {"name":"Dupont", "first_name":"Jean", "birth_date":"1964/05/12", "username":"jdupont", "password":"motdepasse1"} `

Il est à noter que, pour des raisons de sécurité, la réponse à cette requête est `user_json` mais que cette fois-ci, le mot de passe est crypté.
Il en est de même dans la base SQLite.

- **Modifier ses informations personelles d'utilisateur** : requête PUT avec nécéssité d'authentification

`curl -u  username:password -i -H "Content-type: application/json" -X PUT -d 'user_json_no_username' http://127.0.0.1:5000/user/<id> `

Par exemple si l'on veut modifier les informations personelles d'utilisateur `jdupont` créé précédemment, on utilisera `username=jdupont`, `password=motdepasse1`.

Et on définira `user_json_no_username= {"name":"nouveauDupont", "first_name":"nouveauJean","birth_date":"1956/05/11","password":"nouveaumdp1" }`

- **Consulter les biens immobiliers d'une ville particulière** : requête GET

`curl -u GET http://127.0.0.1:5000/goods/<city>`

Donc, par exemple, pour obtenir les biens parisiens présents sur la plateforme, on utilisera la commande :

`curl -u GET http://127.0.0.1:5000/goods/Paris`

*NB* : sur mon Macbook Pro (version 10.11.3 El Capitan), on me demande de rentrer mon mdp d'utilisateur pour valider cette requête, je ne sais pas pourquoi, mais en rentrant le bon mdp la commande fonctionne.

- **Créer un nouveau bien sur la plateforme** : nécessité d'authentification pour identifier le détenteur du bien, requête POST

`curl -u  username:password -i -H "Content-type: application/json" -X POST -d 'good_json' http://127.0.0.1:5000/good`

avec par exemple (en plus d'un username et d'un password valides) :

`good_json = {"name":"appart test","description":"description test","type":"Studio","city":"Paris","nb_rooms":1,"rooms_charac":"test charac"}`

- **Modifier un bien sur la plateforme avec vérification du propriétaire** : comme vous avez dû le comprendre, pour mettre en place la fonctionnalité bonus j'ai opté pour un champ supplémentaire dans le modèle Good, qui représente celui de l'identifiant du propriétaire, et qui est automatiquement fixé lorsque qu'un bien est ajouté sur la plateforme par un propriétaire.

La vérification de la détention du bien est alors simple à effectuer : il suffit de tester si l'ID de l'utilisateur authentifié est bien celui du détenteur du bien que cet utilisateur souhaite modifier.

`curl -u  username:password -i -H "Content-type: application/json" -X PUT -d 'new_good_json' http://127.0.0.1:5000/good/<id>`

avec par exemple :

` new_good_json = {"name":"nouveau appart test","description":"new des","type":"T2","city":"Paris","nb_rooms":2,"rooms_charac":"new charac"} `

### Initialisation de la base de données : 

Si vous le souhaitez, la fonction `init_db()` dans le fichier `models.py` permet d'initialiser la base de données afin de pouvoir tester les différentes fonctionnalités.

Pour l'appeler, il suffit d'exécuter la commande `FLASK_APP=run.py flask shell` dans la première fenêtre de Terminal, et d'exécuter le code suivant :

```python
from arcane_app.models import *
init_db()
```
