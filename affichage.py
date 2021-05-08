def couleur_cellule(etat):
    #on definit une fonction pour retourner la couleur en fonction de l'etat dans laquelle on pourra par consequens ajouter des couleur
    couleur = ''
    if etat == 'saine':
        couleur = '\033[92m'
    elif etat == 'contaminee':
        couleur = '\033[91m'
    return couleur

def affichage_simulation(List_simulation):
    for i in range(len(List_simulation)):
        #la valeur i correspond à la hauteur à laquelle on se situe lorsqu'on parcoure notre cellule de position j
        for j in range(len(List_simulation[i])):
            couleur = couleur_cellule(List_simulation[i][j]["etat"])
            print(couleur + "o", end=" ")

        print()