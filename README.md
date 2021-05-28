# Jeu_de_la_vie

Projet De NSI à  rendre pour le 28/05/2021 - Briac.H et Dan.F

Arboresence :
    - hirou_farouze_epidemie.zip
        ├── affichage.py
        ├── creation_config.py
        ├── globals.py
        ├── import_export.py
        ├── les_modes.py
        ├── mise_a_jour.py
        ├── parametres
        │   ├── fichier-de-parametrage-1.csv
        │   └── fichier-de-parametrage-2.csv
        │   └── fichier-de-parametrage-3.csv
        │   └── .......
        ├── parametres.py
        ├── README.md
        └── simulation.py

Version : 1.0

--------------I - Execution du Jeu--------------

Afin d'éxecuter le jeu, il vous faudra installer les modules suivant :
- csv
utilité : manipulation de fichier csv pour lancer le jeu dans différentes configuration
NOTE: lancer le jeu dans un terminal de commandes Linux pour avoir les couleurs ( ni la console Spyder, ni l'invite de commandes Windows ni un terminal bash installé sur Windows ne permet d'obtenir un affichage en couleur ).

Après cela fait, lancer le fichier simulation.py 
------------------------------------------------


--------------II - Paramétrages du Jeu--------------

Lors du lancement, vous devrez choisir entre plusieurs mode :
[1] meutrier : beaucoup d'inféctées | la maladie possède un fort taux de mortalité
[2] onde: la propagation de l'épidémie forme une belle onde
[3] rapide : La maladie se propage très vite
[4] simulation_grande : réalisation d'une simulation sur une population importante de cellules
[5] test : Mode basique, parfait pour initialiser les joueurs débutants à nos simulations
[6] tranche_pasteque : la propagation de l'épidémie forme une tranche ressemblant à une tranche de pastèque (ou à une demi-lune)

Les paramètres peuvent par la suite êtres modifiés si ils ne conviennent pas :
0 ... largeur : nombre de cellule par ligne
1 ... hauteur : nombre de ligne
2 ... densite_c_init : nombre de cellule contaminées au départ de l'épidémie
3 ... proba_infect : probabilitée d'infection d'une cellule voisine
4 ... J_avant_G : Nombre de jour avant qu'une cellule inféctée devienne immunisée/meurt
5 ... taux_mortal : taux de mortalité de la maladie
6 ... densité_conf : densité de confinement
7 ... imunne_time : temps d'immunité d'une cellule

Le joueur définit ensuite le nombre de jour de l'épidémie, puis il lance la simulation
Si il le souhaite, il peut modifier certains paramètres de la simulation pour créer un nouveau fichier csv qu'il pourra utiliser par la suite en tant que paramètre déja définit
----------------------------------------------------


LISTE DES MODES IDEES :
- incubation
- confinement
- variants
- un certain nb de tour, on peut choisir une cellule Ã  vacciner ( elle peut devenir variant / un zombie ).
- plus l'epidemie avance, plus le vaccin devient efficace ou non.
- faire 2 grilles avec un variant chacune pr voir qui va contaminer/tuer le plus de cellules.
- dire qu'une cellule est l'utilisateur et qu'il peut, chaque tour, se deplacer ( sauf sur les morts ).
- prendre en compte poid et taille (IMC) et ajouter pathologies. 
- faire des simulation faux-negatif et faux-positif our confiner les mauvaises cellules ( qui peuvent mourrir en confinement ).
