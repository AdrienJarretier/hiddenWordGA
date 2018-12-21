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

  La graîne est à mettre dans `common.py` ligne 11 en décommentant `USED_SEED` et en remplacant la valeur par la graîne voulue

 - 28733635357208232931699525957662699157320 (exemple du rapport, 2403)

 - 79615503822743527775510821281651351260513
 - 27393421549473337516760820128169300218841
 - 17092217883483800913574113123584402071032
 - 66834573038808458200921589709185145789024
 - 84493593307495204710215505294078040402967
 - 48655529486363514674739527422330791906218
 - 62327906386620647073753872199822071777043
 - 14982735947378171813515770665228767702683