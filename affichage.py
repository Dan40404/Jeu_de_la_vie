
from import_export import *

def couleur_cellule(etat):
    #on definit une fonction pour retourner la couleur en fonction de l'etat dans laquelle on pourra par consequens ajouter des couleur
    couleur = '\033[92m'
    if etat == 'saine':
        couleur = '\033[92m'
    elif etat == 'contaminee':
        couleur = '\033[91m'
    elif etat == 'immunisee':
        couleur = '\033[94m'
    elif etat == 'decedee':
        couleur = '\033[30m'
    return couleur

def affichage_simulation(List_simulation):
    for i in range(len(List_simulation)):
        #la valeur i correspond à la hauteur à laquelle on se situe lorsqu'on parcoure notre cellule de position j
        for j in range(len(List_simulation[i])):
            couleur = couleur_cellule(List_simulation[i][j]["etat"])
            print(couleur + "o", end=" ")

        print()
        
def parametrage_menu(parametres_initiaux):
    for cle in parametres_initiaux:
        print(cle,':', parametres_initiaux[cle])
