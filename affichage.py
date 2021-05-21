
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
        
        
        
        

def parametrage_menu(parametres_initiaux):
    """
    Fonction affichant un menu pour que l'utilisateur puisse choisir le CSV à ouvrir et dans quel fichier il voudrais 
    sauvegarder ses parametres ou sa partie
    - parametres_initiaux : liste des parametres contenus dans le fichier csv
    """
    #affichage des parametres modifiables
    n = 0
    for cle in parametres_initiaux:
        print(n, "...", cle,':', parametres_initiaux[cle])
        
    #on cree un liste des clés des parametres
    choix = False
    liste_cles = []
    for cle in parametres_initiaux:
        liste_cles.append(cle)
    
    while choix == False :
        while True :
            changement = input("Quel paramètre voulez-vous changer ? : ")
#            if changement > 0 and changement < n :
#                for i in range(len(liste_cles)):
#                    if i == n :
#                        nvlle_valeur = input("Quelle valeur souhaitez vous lui assigner ? : ")
#                        
#                        if changement == 2 or changement == 3 :
#                            while changement == 2 and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
#                                nvlle_valeur = float(input("Une probabilité ne peut être comprise qu'entre 0 et 1 : "))
#                           
#                            while changement == 3 and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
#                                nvlle_valeur = float(input("Une densité ne peut être comprise qu'entre 0 et 1 : "))
#                            nvlle_valeur = float(nvlle_valeur)
#                        else:
#                            nvlle_valeur = int(nvlle_valeur)
                            
                        
            
            
            
            
            
            
            if changement in liste_cles :
                for cle in parametres_initiaux:
                    if cle == changement :
                        nvlle_valeur = input("Quelle valeur souhaitez vous lui assigner ? : ")
                        if changement in ['proba_infect','densite_c_init']:
                            while changement == 'proba_infect' and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
                                nvlle_valeur = float(input("Une probabilité ne peut être comprise qu'entre 0 et 1 : "))
                           
                            while changement == 'densite_c_init' and ( float(nvlle_valeur) > 1 or float(nvlle_valeur) < 0 ) :
                                nvlle_valeur = float(input("Une densité ne peut être comprise qu'entre 0 et 1 : "))
                            nvlle_valeur = float(nvlle_valeur)
                        else:
                            nvlle_valeur = int(nvlle_valeur)
                            
                        parametres_initiaux[cle] = nvlle_valeur
                        for cle in parametres_initiaux:
                            print(cle,':', parametres_initiaux[cle])
                break
                
            else:
                print("Entrée invalide. Veuillez saisir autre chose : ")
        question_ok = 0
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
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    

