# fichier pour l'import / export du fichier .csv
import csv
import globals

def choisir_fichier():
    """
    liste les fichiers du répertoire parametres et demande à l'utilisateur d'en choisir un
    retourne le nom du fichier choisi
    """
    import os
    liste_fichiers = os.listdir('parametres')
    i=1
    for fichier in liste_fichiers: # on affiche les fichiers
        print('[' + str(i) + '] ' + fichier)
        i+= 1

    while True:
        try:
            numero = int(input('quel numéro de fichier choisissez-vous ?')) -1
        except:
            # si le numéro n'est pas un entier, on aura une exception sur le return
            # il n'est donc pas necessaire de "gérer" ici
            pass      
        # on ne veut pas de numéro négatif
        if(numero < 0):
            print("ce numero n'existe pas!")
        else:
            try: # on regarde si le numéro entré correspond bien à un fichier
                return liste_fichiers[numero]
            except:
                print("ce numéro n'existe pas!")


def get_parametres():
    """
    Fonction permettant d'extraire les informations contenues dans le fichier .csv 
    sous la forme d'un dictionnaire
    """
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
    globals.parametre = Parametres_grille


def write_parametre_fichier(parametres,fichier):
    """
    Fonction permettant d'écrire dans un fichier .csv
    - parametres : dictionnaire des parametres
    - fichier : nom du fichier où l'utilisateur veut sauvegarder ses parametres
    """
    with open('parametres/' + fichier, 'w', newline='') as fichier_csv :
        parametre_write = csv.writer(fichier_csv, delimiter=';')
        for cle in parametres:
            parametre = parametres[cle]
            parametre_write.writerow([cle] + [parametre])

            
def sauvegarde_parametres(parametres):
    """demande à l'utilisateur s'il souhaite sauvegarder les parametres.
    lui demande quel fichier, et écrase le fichier si besoin"""
    
    choix = input('Souhaitez-vous sauvegarder ces paramètres ? o/n :')
    if choix == 'n':
        print('Paramètres non sauvegardés')
        return

    choix = input('Souhaitez-vous créer un nouveau fichier? o/n :')
    if choix == 'n':
        fichier = choisir_fichier()
    else:
        fichier = input('Nom du nouveau fichier: ')
        # si l'utilisateur ne rentre pas de nom, on le fait sortir
        if fichier == '':
            print('Aucun fichier choisi')
            return
        # on protège pour ne pas que l'utilisateur "sorte" du répertoire
        fichier = fichier.replace('/','-')
        # si le fichier n'est pas en .CSV sur les 4 derniers carateres, on le rajoute
        if(fichier.find('.csv') - len(fichier) != -4):
            fichier = fichier + '.csv'
    write_parametre_fichier(parametres, fichier)
    return