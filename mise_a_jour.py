from parametres import *

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
            if x_c + i < 0 or y_c + j < 0 or x_c + i > get_hauteur()-1 or y_c + j > get_largeur()-1:
                bord = True
            if bord == False:
                if (i != 0 or j != 0) and L[x_c+i][y_c+j]["etat"] == "contaminee":
                    voisin +=1
    return voisin

def etat_suivant(etat_cellule,voisin, valeur, Stats):
    import random
    #on creer un dictionnaire identique à celui de la cellule, que nous allons modifier puis retourner
    dictionnaire_return = {"etat": etat_cellule, "valeur" : valeur}
    if valeur > 0:
        #si la valeur est > 0 on enleve 1, qui correspond à un jour (d'immunité, de contamination etc...)
        dictionnaire_return['valeur'] -= 1


    if etat_cellule == "saine":
        for i in range(voisin):
            #on relance la proba autant de fois qu'il y a de voisin
            #on genere un nombre au hasard, si on se trouve sur l'intervalle de [0;get_infect_luck()[ alors on infecte la cellule ayant un ou plusieurs voisin(s) infectée(s)
            if random.random() < get_infect_luck():
                Stats["contaminee"] += 1
                dictionnaire_return['etat'] = 'contaminee'
                dictionnaire_return['valeur'] = get_J_avant_G()


    if etat_cellule == "contaminee" and valeur == 0:
        #si la cellule est contaminé on declare que la cellule peut mourrir avec une probabilité get_taux_mortal(), sinon elle devient immunisé
        if random.random() < get_taux_mortal():
            Stats["decedee"] += 1
            dictionnaire_return['etat'] = 'decedee'
        else:
            Stats["immunisee"] += 1
            dictionnaire_return['etat'] = 'immunisee'
            dictionnaire_return['valeur'] = get_imunne_time()

    if etat_cellule == "immunisee" and valeur == 0:
        #A la fin de sa période d'imunité, la cellule redevient saine
        dictionnaire_return['etat'] = 'saine'




    return dictionnaire_return


def transition(L, Stats):
    H = [[] for i in range(get_largeur())]
    #on creer une liste a deux dimension identique à celle de base

    for i in range(len(L)):
        for j in range(len(L[i])):
            #on parcours toutes la liste, pour chaque cellule on calcule le nombre de voisin puis on ajoute la cellule à la nouvelle liste créer
            voisin = animation_du_quartier(L,i,j)
            H[i].append(etat_suivant(L[i][j]["etat"], voisin, L[i][j]["valeur"], Stats))
            #Une fois que la nouvelle List est complete, on la return
    return H

