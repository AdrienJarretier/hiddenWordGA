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

USED_SEED = 516965727647980285240122060590487863092577996099

# print()
# print('seed : ', end='')
# USED_SEED = int(input())


def printSeed():

    print()
    print('-----------------------------------------------------------')
    print('| seed :', USED_SEED, '|')
    print('-----------------------------------------------------------')
    print()


def resetRNG():

    printSeed()
    random.seed(USED_SEED)


resetRNG()


def getFullChoices():

    AVAILABLE_CHARS = string.ascii_uppercase + string.digits + '___'
    return AVAILABLE_CHARS


SIZE_CHOICES = len(getFullChoices())

WORD_LEN = 12
GENOTYPE_LENGTH = WORD_LEN

FITNESS_PROGAM = 'ibi_' + ('2017-2018' if WORD_LEN == 10 else
                           '2018-2019') + '_fitness_windows.exe'

popSizes = [

    76, # 1246693330185985807830912950342831830252608934725
    126,  # 825223724335007065240278192078841274655492415313
    128, # 1374172824681245420414519898052264799487685467700
    139,  # 388279633733923904574047398755986705022040457603
    195,  # 583581761348884047384480420104860010890843096924
    201  # 80653406655206812433266136065413654415375883151

]

POP_SIZE = int(sum(popSizes)/len(popSizes))

PARENTS_SELECTED_SIZE = int(POP_SIZE / 2)

CROSS_OVER_PROB = 0.5
MUTATION_RATE = 0.2

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = False

# def randomChromosome():

#     chrom = ''

#     for _ in range(WORD_LEN):
#         chrom += random.choice(AVAILABLE_CHARS)

#     return chrom
