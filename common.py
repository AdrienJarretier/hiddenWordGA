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

USED_SEED = 698325033554064352154953158910771806122921069494

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

# POP_SIZE = 139 # 388279633733923904574047398755986705022040457603
# POP_SIZE = 195  # 583581761348884047384480420104860010890843096924
POP_SIZE = 80

PARENTS_SELECTED_SIZE = int(POP_SIZE / 2)

CROSS_OVER_PROB = 0.5
MUTATION_RATE = 0.2

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = True

# def randomChromosome():

#     chrom = ''

#     for _ in range(WORD_LEN):
#         chrom += random.choice(AVAILABLE_CHARS)

#     return chrom
