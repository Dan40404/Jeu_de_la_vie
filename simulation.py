from creation_config import *
from affichage import *
from mise_a_jour import *
from import_export import *


parametre = get_parametres()
Stats = creation_stats(parametre)
L = creation_simulation(parametre)
parametrage_menu(parametre)

#input()
#for i in range(15):
#    affichage_simulation(L)
#    Stats["jour"] += 1
#    print('\033[0m')
#    print(Stats)
#    L = transition(L, Stats)

