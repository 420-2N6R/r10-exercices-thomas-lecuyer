import requests as rq

BASE_URL = 'https://fakestoreapi.com'

# Prend un dictionnaire correspondant au produit à mettre à jour.
# Le paramètre id est optionnel SI le produit passé en paramètre contient une clef id.
# On peut donc passé le produit au complet mis à jour ou seulement les valeurs à mettre à jour.

def mettre_produit_a_jour(produit:dict,id:int=None):
    if id == None:
        id = produit.get("id")
    response = rq.patch(f"{BASE_URL}/products/{id}",json=produit)
    return response.json()

def get_prix_nom():
    res=rq.get(f"{BASE_URL}/products")
    res_json=res.json()
    liste_produit=[]
    for produit in res_json:
        new_dict={"title":produit["title"],"price":produit["price"],"id":produit["id"]}
        liste_produit.append(new_dict)
    return liste_produit
print(get_prix_nom())
