import math
import string
import random
import os
import sys

import hideWord

PLOT_FITNESS = True

# FIXED_SEED = 78346491646665448331375559176698498067758

SEED_SIZE = 17

USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

groupsSeeds = {
    0: [None],
    1: [75795746538702431825231596378678609854601],
    2: [57898373048797701248030760706223929892843],
    3: [34307131148606961706035830131773201455151],
    4: [51125071761193270253084876803159650081895],
    5: [59035401142058509487392061374447297474953],
    6: [41959581600763531497919970445067915796584],
    7: [2965988349138115145838932619275020242716, 61682586887150453981018539792203053627320],
    8: [6937648821172558053977157461091145751131],
    9: [4053186976828155375633292078250015868095],
    10: [13124769730084739354891336969933520504011],
    11: [76458922023380351070754258573816411539356],
    12:   [40792353933216437615877413934357640352145],
    13:   [50341707845917812908321140186635189272127],
    14:   [35318624593995925449085837891820577706692],
    15:  [20640707991682958819861659323359425990410],
    16:   [25628965506633661545596903427686502553771],
    17:  [52467615546477726510281981859110131014503],
    18:  [75457651982315009158990077421179717733670],
    19:   [28482203774730128182163940064591258939595],
    20:   [65319839803758032662087632851647641195230],
    21:   [54058832227497148660504239293936902199785],
    22:    [57354880297455905967085071791215723824482],
    23:    [5240974929559795187140653709984178453196],
    24:   [49864554335335321192408198597214825176435],
    25:   [79961701940385312990642022376200348006790]
}

# USED_SEED = groupsSeeds[7][0]


try:
    FIXED_SEED
except NameError:
    FIXED_SEED = USED_SEED

USED_SEED = FIXED_SEED

def printSeed(usedSeed):

    print()
    print('-----------------------------------------------------------')
    print('| seed :', usedSeed, '|')
    print('-----------------------------------------------------------')
    print()


def resetRNG(usedSeed):

    # printSeed(usedSeed)
    random.seed(usedSeed)


resetRNG(USED_SEED)


def getFullChoices():

    ACCENTS = 'àâéèîêûôçïëüäöù'
    SPECIALS = '-_°'
    AVAILABLE_CHARS = string.ascii_uppercase + string.digits \
        + string.ascii_lowercase + ACCENTS + ' ' \
        + string.punctuation + SPECIALS
    return AVAILABLE_CHARS


SIZE_CHOICES = len(getFullChoices())

# WORD_LEN = 12
# GENOTYPE_LENGTH = WORD_LEN

# FITNESS_PROGAM = 'ibi_' + ('2017-2018' if WORD_LEN == 10 else
#                            '2018-2019') + '_fitness_windows.exe'

EXTERNAL_FITNESS_FUNCTION = hideWord.fitness

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

# GROUP_NUM = int(sys.argv[1])
# print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = False



