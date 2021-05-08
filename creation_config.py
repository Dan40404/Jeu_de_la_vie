from parametres import *


def infect_List():

    from random import randint
    # cette fonction auxilliaire sert à renvoyer une liste avec toutes les cellules à mettre en état infectée(s)

    #la liste renvoyer contiendra les position des cellule qui seront contaminer
    List_position = []
    densite = get_densite_c_init()
    largeur = get_largeur()
    hauteur = get_hauteur()

    for i in range(densite):
        continuer = True
        #on introduit un booleen qui va faire tournée une boucle dans le cas ou on obtiendrais 2 fois la meme position de cellule au hasard
        while continuer == True:
            continuer = False
            #on creer un dictionnaire avec la position en longueur et en hauteur de la cellule et on l'ajoute à notre liste
            n = {"x" : randint(0,largeur-1), "y" : randint(0,hauteur-1)}
            if n in List_position:
                continuer = True
        List_position.append(n)

    return List_position

def creation_list():
    largeur = get_largeur()
    hauteur = get_hauteur()
    #On retourne une liste qui à hauteur élement, à l'interieur on creer largeur fois un dictionnaire decrivant son état et une valeur pour les parametres comme le
    #taux de mortalité, confinement etc...
    L = [[{'etat' : 'saine', 'valeur' : 0} for a in range(largeur)] for i in range(hauteur)]
    return L

def infect(L):
    #on récupere une liste sans modification et une list avec des cellules a infecter, on les infecte ensuite via une boucle qui va rechercher la clés état de nos cellules à contaminer
    #notre liste modifié avec les bonnes cellules inféctés est ensuite retourné
    List_pos_infect = infect_List()
    for i in range(len(List_pos_infect)):
        L[List_pos_infect[i]["y"]][List_pos_infect[i]["x"]]["etat"] = "contaminee"
        L[List_pos_infect[i]["y"]][List_pos_infect[i]["x"]]["valeur"] = get_J_avant_G()
    return L

def creation_simulation():
    # on creer une fonction qui nous renvoie la liste de départ de la simulation
    L = creation_list()
    L = infect(L)
    return L
