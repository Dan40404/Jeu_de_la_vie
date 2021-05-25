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
# TODO : apres modif dans mise_a_jour sur les differents temps, on ne peut contaminer et immuniser que l*L cellules donc pas normal

# TODO : maintenant, on contamine que L*l et toutes les valeurs décroissent jusqu'à 0 et ne remontent jamais

