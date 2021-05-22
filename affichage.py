
from import_export import *
from parametres import *

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
        
        
        
def affichage_menu_parametres(parametres):
    """affichage des parametres avec un numero"""
    n = 0
    #on cree un liste des clés des parametres
    for cle in parametres:
        print(n, "...", cle,':', parametres[cle])
        n = n+1
    

def parametrage_menu(parametres_initiaux):
    """
    Fonction affichant un menu pour que l'utilisateur puisse choisir le CSV à ouvrir et dans quel fichier il voudrais 
    sauvegarder ses parametres ou sa partie
    - parametres_initiaux : liste des parametres contenus dans le fichier csv
    """

    #on cree un liste des clés des parametres
    liste_cles = []
    for cle in parametres_initiaux:
        liste_cles.append(cle)
        
    choix = False    
    while choix == False :
        while True :
            affichage_menu_parametres(parametres_initiaux)

            changement = input("Quel numéro de paramètre voulez-vous changer ? (appuyez sur 'ENTREE' si aucun) : ")
            if changement == '':
                choix = True
                break                          
            cle = liste_cles[int(changement)]

            try:
                cle = liste_cles[int(changement)]
            except:
                print("Entrée invalide. Veuillez saisir autre chose")
                break
            print("Vous avez choisi de modifier", cle, ":", parametres_initiaux[cle])
            nvlle_valeur = input("Quelle valeur souhaitez vous lui assigner ? : ")
            if cle in ['proba_infect','densite_c_init','taux_mortal']:
                while cle == 'proba_infect' and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
                    nvlle_valeur = float(input("Une probabilité ne peut être comprise qu'entre 0 et 1 : "))
                       
                while cle == 'densite_c_init' and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
                    nvlle_valeur = float(input("Une densité ne peut être comprise qu'entre 0 et 1 : "))

                while cle == 'taux_mortal' and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
                    nvlle_valeur = float(input("Un taux ne peut être compris qu'entre 0 et 1 : "))

                nvlle_valeur = float(nvlle_valeur)
            else:
                # si on a rentré du texte, on recommence ! 
                try:
                    nvlle_valeur = int(nvlle_valeur)
                except:
                    print("Entrée invalide. Veuillez saisir autre chose")
                    break                    
                parametres_initiaux[cle] = nvlle_valeur
            break
                

        question_ok = 0
        if changement == '':
            question_ok = 1
        while question_ok == 0 :
            question = input("Voulez-vous changer la valeur d'autres parametres ? (o/n) : ")
            if question == 'n' :
                choix = True
                question_ok = 1
            elif question == 'o' :
                question_ok = 1
        
    for cle in parametres_initiaux:
        print(cle,':', parametres_initiaux[cle])
        
    return parametres_initiaux
