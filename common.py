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

# usedSeed = 46255


def printSeed():

    print()
    print('-----------------------------------------------------------')
    print('| seed :', USED_SEED, '|')
    print('-----------------------------------------------------------')
    print()


printSeed()

random.seed(USED_SEED)


def getFullChoices():

    AVAILABLE_CHARS = string.ascii_uppercase + string.digits + '___'
    return AVAILABLE_CHARS


SIZE_CHOICES = len(getFullChoices())


WORD_LEN = 12
GENOTYPE_LENGTH = WORD_LEN

FITNESS_PROGAM = 'ibi_' + ('2017-2018' if WORD_LEN == 10 else
                           '2018-2019') + '_fitness_windows.exe'

POP_SIZE = 80

SELECT_ELITES_SIZE = int(POP_SIZE*0.5)

CROSS_OVER_PROB = 0.5
MUTATE_PROB_PER_GENE = 0.2


# ELECTED_COUNT = 1

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

# MAX_FITNESS = 1

# MUTATION_RATE = 20 / 100

# PARENTS_SELECTED_SIZE = int(POPULATION_SIZE / 2)


# def randomChromosome():

#     chrom = ''

#     for _ in range(WORD_LEN):
#         chrom += random.choice(AVAILABLE_CHARS)

#     return chrom
