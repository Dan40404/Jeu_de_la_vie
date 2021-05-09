from creation_config import *
from affichage import affichage_simulation
from mise_a_jour import *

Stats = creation_stats()
L = creation_simulation()
for i in range(15):
    affichage_simulation(L)
    Stats["jour"] += 1
    print('\033[0m')
    print(Stats)
    L = transition(L, Stats)

