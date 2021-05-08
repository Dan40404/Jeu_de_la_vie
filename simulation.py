from creation_config import *
from affichage import affichage_simulation
from mise_a_jour import *


L = creation_simulation()
affichage_simulation(L)
print('\033[0m',end="")

