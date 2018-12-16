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

# USED_SEED = 516965727647980285240122060590487863092577996099

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

PARENTS_SELECTED_SIZE = int(POP_SIZE / 2)

CROSS_OVER_PROB = 0.5

mutationRates = [

    20,
    22  # 583576999695658761133502616487917580694931131784

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
