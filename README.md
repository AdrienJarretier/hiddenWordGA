# Un algorithme génétique pour trouver un mot caché 

Projet pédagogique - UE Intelligence Bio Inspirée - Module Algorithme Génétique

Des modifications ont été apportées pour ajouter de l'intéractivité (en proposant à un utilisateur de rentrer le mot à trouver) dans le cadre d'une médiation sur le thème de l'IA à la médiathèque de Bron

## Langage
  * Python 3.8.5

## Install

`pip3 install -r requirements.txt`

### If using Anaconda

`conda install pywin32`

## Exécution

`python .`

L'interface demande d'entrer un mot à cacher, l'algorithme génétique ne le connait pas et essaye de le trouver.

La fonctione d'aptitude est simplement la [distance de Levenshtein](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein) entre l'individu et la chaîne cachée

une mutation d'un individu peut supprimer, ajouter ou remplacer un caractère par un caractère aléatoire

## Exécution ancienne version

  * Copier `ibi_2018-2019_fitness_windows.exe` dans la racine du répertoire (cad à côté de algoGen.py)

  * Exécution de l'algoGen pour un numéro de groupe (7 par exemple) `> python algoGen.py 7`

  * Exécution du pokedex 
      Pokedex pour trouver les mots de passes du groupe 1 à 25 `> pokedex.bat 1`
      Pokedex pour trouver les mots de passes du groupe 25 à 1 `> pokedex.bat -1`

  * Le lancement de l'algoGen vas générer une trace d'exécution enregistrée dans le répertoire ./traces et portant le nom `<num_groupe>_<password>_<nb_generations>_<seed>.json`
    Pour lancer la visualisation d'une trace: python `> viewer.py <num_groupe> <seed>`
    (Attention nécessite matplotlib)
    Pour toutes les graînes présentées ci-dessous il existe déjà une trace visualisable avec le viewer.

## Seed "intéressantes"

  La graîne est à mettre dans `common.py` ligne 40 en décommentant `USED_SEED` et en remplacant la valeur par la graîne voulue

 - 2965988349138115145838932619275020242716 (exemple du rapport, 1398 générations)

  Les graines du pokédex :

 - groupe_(mot caché)_gens  graines

 - 1_(_8ULB1Z4RR3_)_4025_   75795746538702431825231596378678609854601
 - 2_(H3R8_1Z4RRE_)_909_    57898373048797701248030760706223929892843
 - 3_(F_L0R1Z4RR_3)_1296_   34307131148606961706035830131773201455151
 - 4_(54L_AM3_CHE_)_481_    51125071761193270253084876803159650081895
 - 5_(_R3P7_1NCEL_)_1154_   59035401142058509487392061374447297474953
 - 6_(DR4C___AUF3U)_2039_   41959581600763531497919970445067915796584
 - 7_(__C4RA__PUC3)_2778_   61682586887150453981018539792203053627320
 - 8_(C4_RA_84FF3_)_4280_   6937648821172558053977157461091145751131
 - 9_(_70_R_T4_NK_)_1908_   4053186976828155375633292078250015868095
 - 10_(_CH3NI_P4N__)_2175_  13124769730084739354891336969933520504011
 - 11_(CHRY54C13R__)_1347_  76458922023380351070754258573816411539356
 - 12_(_P4P1LU5I0N_)_2377_  40792353933216437615877413934357640352145
 - 13_(4_S_P_1C_0_7)_353_   50341707845917812908321140186635189272127
 - 14_(_C0CON_F0R7_)_4549_  35318624593995925449085837891820577706692
 - 15_(_D4RDAR6N4N_)_1533_  20640707991682958819861659323359425990410
 - 16_(R_0_U_C_O0_L)_3748_  25628965506633661545596903427686502553771
 - 17_(_R0U__COUP5_)_2454_  52467615546477726510281981859110131014503
 - 18_(R0U_C4RNA63_)_652_   75457651982315009158990077421179717733670
 - 19_(__R47TA74___)_2799_  28482203774730128182163940064591258939595
 - 20_(R47____TA74C)_2551_  65319839803758032662087632851647641195230
 - 21_(_P14F_A_83C_)_3740_  54058832227497148660504239293936902199785
 - 22_(R4PA5_D3_P1C)_371_   57354880297455905967085071791215723824482
 - 23_(4_8_0__A_B_O)_2605_  5240974929559795187140653709984178453196
 - 24_(4R80K__ARBOK)_2162_  49864554335335321192408198597214825176435
 - 25_(__P1K4CHU___)_1592_  79961701940385312990642022376200348006790
 
 # Authors
 
- ### Oceane Cassan
- ### Hugo Castaneda
- ### Adrien Jarretier-Yuste
