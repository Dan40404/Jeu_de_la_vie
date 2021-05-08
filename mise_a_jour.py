from parametres import get_largeur
from parametres import get_hauteur
from parametres import get_infect_luck

def animation_du_quartier(L,x_c,y_c):
    voisin = 0
    #on parcoure les cellules voisines aux positions suivantes : pour une cellule de Position C(i,j) ses voisins sont A(i-1, j-1), A’(i-1, j), B(i-1, j + 1), B’(i, j-1), C’(i,j+1), D(i+1, j-1), D’(i+1, j), E(i+1, j + 1)
    #on va parcoure toutes les cellules voisines et faire les verifications suivante :
    # - verifier que nous ne sommes pas au bord en verifiant que la hauteur/largeur du voisin n'est pas négatife ou au dessue de la grille
    # - veifier que nous ne sommes pas dans notre cellule pour ne pas ajouter un voisin qui n'existe pas
    # - verifier que le voisin est contaminé pour ajouter un voisin
    for i in range(-1,2):
        for j in range(-1,2):
            bord = False
            if x_c + i < 0 or y_c + j < 0 or x_c + i > get_hauteur() or y_c + j > get_largeur():
                bord = True
            if (i != 0 or j != 0) and (bord == False) and L[x_c+i][y_c+j]["etat"] == "contaminee":
                voisin +=1
    return voisin

def etat(etat_cellule,voisin, valeur):
    import random
    dictionnaire_return = {"etat": etat_cellule, "valeur" : valeur}
    if etat_cellule == "sain":
        for i in range(voisin):
            if random.random() <= get_infect_luck():
                dictionnaire_return['etat'] = 'contaminee'

    return dictionnaire_return





def transition(L):
    H = [[] for i in range(get_largeur())]

    for i in range(len(L)):
        for j in range(len(L[i])):
            voisin = animation_du_quartier(L,i,j)

