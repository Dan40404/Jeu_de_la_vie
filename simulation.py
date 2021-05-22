import globals
from creation_config import *
from affichage import *
from mise_a_jour import *
from import_export import *


# on créé notre variable globale - parametre, accessible en globals.parametre
globals.initialize()
get_parametres()
parametres_nouveaux = parametrage_menu(globals.parametre)

# TODO: mettre en option ligne en dessous 
# TODO: proteger saisie utilisateur ( ../ )

sauvegarde_parametres(parametres_nouveaux)
globals.parametre = parametres_nouveaux
Stats = creation_stats()
L = creation_simulation()


for i in range(15):
    affichage_simulation(L)
    Stats["jour"] += 1
    print('\033[0m')
    suivi_statistique(Stats)
    L = transition(L, Stats)

input()