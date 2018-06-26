from models import Good, User

selected_feature=input("Quelle fonctionnalité voulez-vous utiliser ? \n 1 : Modifier les informations d'un bien \n 2 : Créer ou modifier son espace utilisateur \n 3 : Consulter les biens d'une ville \n" )

if selected_feature=='1':

    ##### A MODIFIER ######

    id_user = input("Quel est votre ID d'utilisateur ? ")

    #######################

    id_good=input("Quel est l'ID du bien à modifier ? ")

    selected_good=Good.query.get(id_good)

    if str(id_user) != str(selected_good.owner_id):
        print("Vous ne pouvez pas effectuer cette action : vous n'êtes pas le propriétaire de ce bien immobilier")
    else:
        selected_modif=input("Que voulez-vous modifier ? \n 1 : le nom \n 2 : la description \n 3 : le type \n 4 : la ville \n 5 : le nombre de pièces \n 6 : la description des pièces \n 7 : le propriétaire \n")
    if selected_modif=='1':
        selected_good.modify_name()
    if selected_modif=='2':
        selected_good.modify_des()
    if selected_modif=='3':
        selected_good.modify_type()
    if selected_modif=='4':
        selected_good.modify_city()
    if selected_modif=='5':
        selected_good.modify_nb_rooms()
    if selected_modif=='6':
        selected_good.modify_rooms_charac()
    if selected_modif=='7':
        selected_good.modify_owner()

if selected_feature=='2':
    selected_action= input("Voulez-vous créer ou modifier votre espace utilisateur ? \n 1 : Créer \n 2 : Modifier \n ")
    if selected_action=='1':
        User.create_new_user()
    if selected_action=='2':
        id_user=input("Quel est votre ID d'utilisateur ?")
        selected_user=User.query.get(id_user)
        selected_user.modify_infos()

if selected_feature=='3':
    selected_city=input('De quelle ville voulez-vous voir les biens disponibles ? ')
    goods_list=Good.query.filter(city=selected_city)