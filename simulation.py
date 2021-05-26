# -*- coding: utf-8 -*-
#fichier principal

import globals
import random
from creation_config import *
from affichage import *
from mise_a_jour import *
from import_export import *


# on créé notre variable globale - parametre, accessible en globals.parametre
globals.initialize()

while True:
    get_parametres()
    parametres_nouveaux = parametrage_menu(globals.parametre)
    print()
    print("NOS RECOMMANDATIONS POUR LA DUREE DES SIMULATIONS PRE-ENREGISTREES :")
    print("- simulation_grande.csv : 60 ou plus", end='\n')
    print("- onde.csv : 50 ou un peu moins ( correspond à la largeur/hauteur", end='\n')
    print("- tranche_pasteque.csv : 40 ou un peu moins", end='\n')
    print("- rapide.csv : 15", end='\n')
    nombre_jours = input("Combien de jours souhaitez-vous que la simulation dure ? : ")
    try:
        nombre_jours = int(nombre_jours)
    except:
        print("Votre valeur est erronée. Nous allons en mettre une au hasard")
        nombre_jours = random.randint(5, 100)
    
    print()
    sauvegarde_parametres(parametres_nouveaux)
    globals.parametre = parametres_nouveaux
    Stats = creation_stats()
    L = creation_simulation()
    
    
    for i in range(nombre_jours):
        affichage_simulation(L)
        Stats["jour"] += 1
        print('\033[0m')
        suivi_statistique(Stats)
        L = transition(L, Stats)
    
    input()
    sauvegarde_parametres(parametres_nouveaux)
    recommencer = input('Voulez-vous recommencer? o/n: ')
    if recommencer == 'n':
        break


