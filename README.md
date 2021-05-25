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
