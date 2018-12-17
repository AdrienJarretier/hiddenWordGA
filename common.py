import math
import string
import random
import os
import sys

# seed sympas:
# - 236957502862991091183765 - 23794
# - 46255 - 3225 - 7
# - 42474 - 17728 - 9
# - 30542 - 17837 - 1
# - 30542 - 17837 - 1
# - 31744 - 2252 - 7

USED_SEED = int.from_bytes(os.urandom(20), sys.byteorder)

# USED_SEED = 809335550007552268796735201475338772531677040207

# print()
# print('seed : ', end='')
# USED_SEED = int(input())


def printSeed(usedSeed):

    print()
    print('-----------------------------------------------------------')
    print('| seed :', usedSeed, '|')
    print('-----------------------------------------------------------')
    print()


def resetRNG(usedSeed):

    printSeed(usedSeed)
    random.seed(usedSeed)


resetRNG(USED_SEED)


def getFullChoices():

    AVAILABLE_CHARS = string.ascii_uppercase + string.digits + '___'
    return AVAILABLE_CHARS


SIZE_CHOICES = len(getFullChoices())

WORD_LEN = 12
GENOTYPE_LENGTH = WORD_LEN

FITNESS_PROGAM = 'ibi_' + ('2017-2018' if WORD_LEN == 10 else
                           '2018-2019') + '_fitness_windows.exe'


popSizes = [

    5,  # 462887619648695420303324250720117330140454296985
    73,  # 1166483567965177056269091236949548191193937835969
    76,  # 1246693330185985807830912950342831830252608934725
    126,  # 825223724335007065240278192078841274655492415313
    127,  # 615984430483285982547492797844669283579840246669
    128,  # 1374172824681245420414519898052264799487685467700
    139,  # 388279633733923904574047398755986705022040457603
    157,  # 406926350306076806918747298547763029347450359160
    195,  # 583581761348884047384480420104860010890843096924
    201,  # 80653406655206812433266136065413654415375883151
    241,  # 1248877566227091681756808799471169325980844555492
    279,  # 662248835634772145104285420170654192873626060790
    308,  # 860775926485888677062073984721455843044794273764
    315,  # 111416190166104625913601912792286810708956813806
    346  # 419266162619322786091769142916652687735838744899

]


POP_SIZE = int(sum(popSizes)/len(popSizes))

ratiosParents = [

    74,  # 281594342038715290326795111845371746857021528575
    21,  # 173449566813955240477191565866711199634619085436
    38,  # 1198288024949901115357025942449931939775790032841
    46,  # 858784158225045999061061558689719277516767623048
    50.0,  # 717149552759120187285623257490924274347761502281
    74,  # 929512525325389666452645723881837800761292736093
    36,  # 1086069444628207706255856611148263795581315496730
    62,  # 333018993173420278093571869625545733757962107114
    47,  # 1185682424764930557968385856218455919846770500588
    70  # 655049849088218974803616875051760558720076678446

]

RATIO_SELECTED_PARENTS = sum(ratiosParents)/len(ratiosParents)

# PARENTS_SELECTED_SIZE = int(POP_SIZE / 2)

crossoverProbabilities = [

    12,  # 162732043196758253513196614573439553469239637820
    19,  # 1351908070700933876550696295163325360354723903342
    20,  # 171797837861791118470786620435349024640732881194
    20,  # 556871533926445346021388306415370881436729710452
    13,  # 511200318672292769714217209110153800919169937812
    19,  # 1033486403366198037734760980696373982737087549658
    8,  # 1091079434731895894179527870734228856864241769556

]


CROSS_OVER_PROB = sum(crossoverProbabilities)/len(crossoverProbabilities)


mutationRates = [

    17,  # 1202331411471408584270122333533501159103089405517
    15,  # 70372267452102502922354368611410150901141006212
    17,  # 835919406231861536584842265468945369407931659518
    19,  # 1318623033030752460926627959152098251695315000874
    17,  # 1173867281730081574374878870865691659190588139348
    26  # 1024917471585070607964863157052207738719970653009

]

MUTATION_RATE = sum(mutationRates)/len(mutationRates)

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = False

# def randomChromosome():

#     chrom = ''

#     for _ in range(WORD_LEN):
#         chrom += random.choice(AVAILABLE_CHARS)

#     return chrom
