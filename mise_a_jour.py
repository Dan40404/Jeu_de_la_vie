# -*- coding: utf-8 -*-
from parametres import *

def animation_du_quartier(L,x_c,y_c):
    """
    Fonction qui permet de determiner le nombre de cellules contaminées touchant une cellule.
    On retourne le nombre de voisins infectés.
    - L : (list) liste des etats des cellules
    - x_c : (int) numéro de colonne de la cellule dont on cherche les voisins infectés
    - y_c : (int) numéro de ligne de la cellule dont on cherche les voisins infectés
    """
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

def etat_suivant(etat_cellule, voisin, valeur, Stats, temps):
    """
    Fonction permettant d'affecter un nouvel état à chaque cellule apres un tour. 
    - etat_cellule : (string) etat de la cellule
    - voisin : (int) nombre de voisins infectés de la cellule
    - valeur : (int) nombre de jours depuis sa contamination
    - Stats : (dict) dictionnaire comportant le nombre de cellules saines, infectées, mortes et le nombre du jour
    """
    import random
    #on creer un dictionnaire identique à celui de la cellule, que nous allons modifier puis retourner
    dictionnaire_return = {"etat": etat_cellule, "valeur" : valeur, "temps" : temps}
    if valeur > 0:
        #si la valeur est > 0 on enlève 1, qui correspond à un jour (d'immunité, de contamination etc...)
        dictionnaire_return['valeur'] -= 1
    # on dit d'office que la cellule est dans son etat un jour de plus et si cela s'avère faux, on réinitialisera à 0 dans la condition correspondante
    dictionnaire_return['temps'] += 1


    if etat_cellule == "saine":        
        for i in range(voisin):
            #on relance la proba autant de fois qu'il y a de voisin
            #on genere un nombre au hasard, si on se trouve sur l'intervalle de [0;get_infect_luck()[ alors on infecte la cellule ayant un ou plusieurs voisin(s) infectée(s)
            if random.random() < get_infect_luck():
                Stats["contaminees"] += 1
                Stats["saines"] -= 1
                dictionnaire_return['etat'] = 'contaminee'
                dictionnaire_return['valeur'] = get_J_avant_G()
                dictionnaire_return['temps'] = 0 # la cellule devient contaminee donc son compteur est remit à 0
                break # on sort de la boucle Pour afin d'éviter de compter plusieurs fois la cellule comme contaminée


    if etat_cellule == "contaminee" and valeur == 0:
        #si la cellule est contaminé on declare que la cellule peut mourrir avec une probabilité get_taux_mortal(), sinon elle devient immunisé
        
        if random.random() < get_taux_mortal():
            Stats["decedees"] += 1
            Stats["contaminees"] -= 1
            dictionnaire_return['etat'] = 'decedee'
            dictionnaire_return['temps'] = 0 
        else:
            Stats["immunisees"] += 1
            Stats["contaminees"] -= 1
            dictionnaire_return['etat'] = 'immunisee'
            dictionnaire_return['valeur'] = get_imunne_time()
            dictionnaire_return['temps'] = 0
        

    if etat_cellule == "immunisee" and valeur == 0:
        #A la fin de sa période d'imunité, la cellule redevient saine
        dictionnaire_return['etat'] = 'saine'
        Stats["saines"] += 1
        Stats["immunisees"] -= 1
        dictionnaire_return['temps'] = 0

    return dictionnaire_return


def transition(L, Stats):
    """
    Fonction qui permet de faire une nouvelle grille avec les nouvelles informations obtenues grace à etat_suivant.
    - L : (list) liste de dictionnaires des etats de toutes les cellules
    - Stats : (dict) dictionnaire comportant le nombre de cellules saines, infectées, mortes et le nombre du jour
    """
    H = [[] for i in range(get_hauteur())]
    #on creer une liste a deux dimension identique à celle de base

    for i in range(len(L)):
        for j in range(len(L[i])):
            #on parcours toutes la liste, pour chaque cellule on calcule le nombre de voisin puis on ajoute la cellule à la nouvelle liste créer
            voisin = animation_du_quartier(L,i,j)
            H[i].append(etat_suivant(L[i][j]["etat"], voisin, L[i][j]["valeur"], Stats, L[i][j]["temps"]))
            #Une fois que la nouvelle List est complete, on la return
    return H


def suivi_statistique(Stats):
    """
    Fonction permettant d'afficher les statistiques à la fin de chaque étape
    - Stats : (dict) dictionnaire comportant le nombre de cellules saines, infectées, mortes et le nombre du jour
    """
    print(Stats)





















