import math
import string
import random
import os
import sys

SEED_SIZE = 17

USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

# USED_SEED = 809335550007552268796735201475338772531677040207


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

    80

]


POP_SIZE = int(sum(popSizes)/len(popSizes))

ratiosParents = [

    50

]

RATIO_SELECTED_PARENTS = sum(ratiosParents)/len(ratiosParents)


crossoverProbabilities = [

    50

]


CROSS_OVER_PROB = sum(crossoverProbabilities)/len(crossoverProbabilities)


mutationRates = [

    20

]

MUTATION_RATE = sum(mutationRates)/len(mutationRates)

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = False
