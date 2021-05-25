#fichier principal

import globals
from creation_config import *
from affichage import *
from mise_a_jour import *
from import_export import *


# on créé notre variable globale - parametre, accessible en globals.parametre
globals.initialize()
get_parametres()
parametres_nouveaux = parametrage_menu(globals.parametre)


sauvegarde_parametres(parametres_nouveaux)
globals.parametre = parametres_nouveaux
Stats = creation_stats()
L = creation_simulation()


for i in range(30):
    affichage_simulation(L)
    Stats["jour"] += 1
    print('\033[0m')
    suivi_statistique(Stats)
    L = transition(L, Stats)

input()

# TODO : apres modif dans mise_a_jour sur les differents temps, on ne peut contaminer et immuniser que l*L cellules donc pas normal

# TODO : maintenant, on contamine que L*l et toutes les valeurs décroissent jusqu'à 0 et ne remontent jamais

