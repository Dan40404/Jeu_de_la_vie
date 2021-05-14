
from import_export import *

def get_densite_c_init(parametre):
    """
    Fonction retournant la densité initiale contenue dans le .csv 
    """
    return parametre['densité_c_init']

def get_largeur(parametre):
    """
    Fonction retournant la largeur contenue dans le .csv 
    """
    return parametre['largeur']

def get_hauteur(parametre):
    """
    Fonction retournant la hauteur contenue dans le .csv 
    """
    return parametre['hauteur']

#Pour chaque get, on vient chercher une valeur du dictionnaire parametres, cela permet de simplifier le code en lisant facilement la valeur utilisé
def get_infect_luck(parametre):
    """
    Fonction retournant la probabilité de contamination d'une cellule contenue dans le .csv 
    """
    return parametre['proba_infect']

def get_J_avant_G(parametre):
    """
    Fonction retournant le temps avant qu'une cellule soit guerie contenu dans le .csv 
    """
    return parametre['J_avant_G']

def get_taux_mortal(parametre):
    return parametre['taux_mortal']

def get_imunne_time(parametre):
    """
    Fonction retournant le temps d'immunisation d'une cellule contenu dans le .csv 
    """
    return parametre['imunne_time']
