import math
import string
import random
import os
import sys

SEED_SIZE = 17

USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

groupsSeeds = [
    [None],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

# USED_SEED = 21052245958756179004718051174220846454455


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


# Below are the hyper parameters of the algorithms,
# each one is the average of the values found by the optimization process


popSizes = [
    62,  # 79615503822743527775510821281651351260513
    106,  # 27393421549473337516760820128169300218841
    93,  # 5783239214666646746182155304646764962074
    47,  # 51984081950513707900363557252943247079731
]

# The number of individuals in a generation
POP_SIZE = int(sum(popSizes)/len(popSizes))


ratiosParents = [
    51,  # 17092217883483800913574113123584402071032
    81,  # 66834573038808458200921589709185145789024
    23,  # 20432701732304932232798449194648946334815
    94,  # 6387323999521112018454449408743858894669
]


# the ratio of parents selected
RATIO_SELECTED_PARENTS = sum(ratiosParents)/len(ratiosParents)


crossoverProbabilities = [
    4,  # 84493593307495204710215505294078040402967
    4,  # 48655529486363514674739527422330791906218
    1,  # 74194572575874471455227123660413651782052
    10,  # 9075244738064861171526480097837063391090
]


CROSS_OVER_PROB = sum(crossoverProbabilities)/len(crossoverProbabilities)

mutationRates = [
    20,  # 62327906386620647073753872199822071777043
    20,  # 14982735947378171813515770665228767702683
    6,  # 81517773795792090147766981679395821987282
    17,  # 25537276601247711865034804159372457066860
]


MUTATION_RATE = sum(mutationRates)/len(mutationRates)

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = True
