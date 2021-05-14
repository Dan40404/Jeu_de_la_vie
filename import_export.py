# fichier pour l'import / export du fichier .csv

def choisir_fichier():
    """
    liste les fichiers du répertoire parametres et demande à l'utilisateur lequel charger
    retourne le nom du fichier choisi
    """
    import os
    liste_fichiers = os.listdir('parametres')
    i=1
    for fichier in liste_fichiers:
        print('[' + str(i) + '] ' + fichier)
        i+= 1
    numero = int(input('quel numéro de fichier choississez-vous ?')) -1
    # TODO: mettre les protections si liste_fichiers[numero] n'existe pas 
    return liste_fichiers[numero]


def get_parametres():
    """
    Fonction permettant d'extraire les informations contenues dans le fichier .csv 
    sous la forme d'un dictionnaire
    """
    import csv
    #on import le module qui nous permet d'ouvrir un fichier csv
    file = open("parametres/" + choisir_fichier())
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

