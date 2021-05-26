# -*- coding: utf-8 -*-
import globals

def get_densite_c_init():
    """
    Fonction retournant la densité initiale contenue dans le .csv 
    """
    return globals.parametre['densite_c_init']

def get_largeur():
    """
    Fonction retournant la largeur contenue dans le .csv 
    """
    return globals.parametre['largeur']

def get_hauteur():
    """
    Fonction retournant la hauteur contenue dans le .csv 
    """
    return globals.parametre['hauteur']

#Pour chaque get, on vient chercher une valeur du dictionnaire globals.globals.globals.globals.globals.parametres, cela permet de simplifier le code en lisant facilement la valeur utilisé
def get_infect_luck():
    """
    Fonction retournant la probabilité de contamination d'une cellule contenue dans le .csv 
    """
    return globals.parametre['proba_infect']

def get_J_avant_G():
    """
    Fonction retournant le temps avant qu'une cellule soit guerie contenu dans le .csv 
    """
    return globals.parametre['J_avant_G']

def get_taux_mortal():
    return globals.parametre['taux_mortal']

def get_imunne_time():
    """
    Fonction retournant le temps d'immunisation d'une cellule contenu dans le .csv 
    """
    return globals.parametre['imunne_time']


