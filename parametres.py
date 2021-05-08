def get_parametres():
    import csv
    #on import le module qui nous permet d'ouvrir un fichier csv
    file = open("parametres/test.csv")
    fichier_demander = csv.reader(file,delimiter=";")
    #le delimiter permet de creer une liste avec un element pour chaque case

    #Création du dictionnaire retourné contenant les parametres
    Parametres_grille = {}

    #on parcoure chaque ligne
    for ligne in fichier_demander:
        try:
            #l'element 0 correspond au parametre et l'element 1 à sa valeur
            #on utilise un try excepte car certaines valeur sont compris entre 0 et 1, ce ne sont pas des int, donc si il y'a une erreur on les ajoutes en tant que float
            Parametres_grille[(ligne[0])] = int(ligne[1])
        except:
            Parametres_grille[(ligne[0])] = float(ligne[1])

    return Parametres_grille

def get_densite_c_init():
    parametre = get_parametres()
    return parametre['densité_c_init']

def get_largeur():
    parametre = get_parametres()
    return parametre['largeur']

def get_hauteur():
    parametre = get_parametres()
    return parametre['hauteur']

def get_infect_luck():
    parametre = get_parametres()
    return parametre['proba_infect']
