from utils_fakestore import converter as conv
from utils_fakestore import fakestore_rq as fk_rq
# Vous avez deux modules faits pour travailler avec votre API fakestore.
#   Le module converter permet de convertir des valeurs monétaires d'un prix canadien à un prix américain.
#   Le module fakestore_rq contient une fonction "mettre_produit_a_jour" qui permet de changer les valeurs d'un produit dans la base de données de fakestore.


print(f"Q1{60*'_'}")
# Q1 :
# On veut pouvoir afficher la liste des prix des différents produits en euro.

#   Q1 - A
#   Ajouter une fonction au module fakestore_rq qui retourne une liste de dictionnaires.
#   chaque dictionnaire contient le nom d'un produit ainsi que son prix


#   Q1 - B
#   Appeler cette nouvelle fonction développée en Q1 - A. En utilisant le module converter, 
#   afficher dans l'invite de commande : le nom de chaque produit et son prix en euro.

liste_produits=fk_rq.get_prix_nom()
liste_euro=[]
for line in liste_produits:
    prix_eur=conv.convert_cad_to_eur(line["price"])
    line["price"]=round(prix_eur,2)
    liste_euro.append(line)
print(liste_euro)


print(f"Q2{60*'_'}")
# Q2 :
# On étend le site web pour qu'il fasse affaire au japon
# On veut mettre le site web à jour pour que tous les prix soit en yen japonais pas défaut (jpy)

#   Q2 - A :
#   Ajouter une nouvelle fonction au module converter pour convertir le prix du dollar canadien au yen japonais.

#   Q2 - B :
#   En utilisant la fonction "mettre_produit_a_jour" du module fakestore_rq, mettez à jour tous les prix des produits pour qu'ils soient en jpy.
liste_jpy=[]
for line in liste_produits:
    prix_jpy=conv.convert_cad_to_jpy(line["price"])
    line["price"]=round(prix_jpy,2)
    liste_jpy.append(line)
print(liste_jpy)

for ligne in liste_jpy:
    retour=fk_rq.mettre_produit_a_jour(ligne)
    print(retour)