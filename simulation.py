from creation_config import *
from affichage import affichage_simulation
from mise_a_jour import *

L = creation_simulation()
for i in range(15):
    affichage_simulation(L)
    L = transition(L)
    print('\033[0m')

