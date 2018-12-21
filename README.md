# AlgoGenetique 
### Hugo Castaneda - Adrien Jarretier-Yuste

Projet pédagogique - UE Intelligence Bio Inspirée - Module Algorithme Génétique

## Langage
  * Python 3.7

## Exécution

  * Exécution de l'algoGen pour un numéro de groupe (7 par exemple) `> python algoGen.py 7`

  * Exécution du pokedex 
      Pokedex pour trouver les mots de passes du groupe 1 à 25 `> pokedex.bat 1`
      Pokedex pour trouver les mots de passes du groupe 25 à 1 `> pokedex.bat -1`

  * Le lancement de l'algoGen vas générer une trace d'exécution enregistrée dans le répertoire ./traces et portant le nom `<num_groupe>_<password>_<nb_generations>_<seed>.json`
    Pour lancer la visualisation d'une trace: python `> viewer.py <num_groupe> <seed>`
    (Attention nécessite matplotlib)

## Seed "intéressantes"
 - 28733635357208232931699525957662699157320 (exemple du rapport, 2403)