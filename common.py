import math
import string
import random
import os
import sys

SEED_SIZE = 17

USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

# USED_SEED = 809335550007552268796735201475338772531677040207
USED_SEED = 27554115246066715920827339483807944935587


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
    44,  # 39018190143983315733414797461575953091785   ',
    100,  # 70144977305557996971719098305482476374623   ',
    72,  # 84677765061521387604761329341501152527832   ',
    108,  # 52487340720311867218875631390092212317865   ',
    177,  # 39668485433188872936775227031301603981526   ']
    34,  # 30511593567475620871610028281301742551648   ',
    46,  # 57288682899733007671071435965553172329260   ',
    74,  # 49630043593527674322465267217759000837251   ',
    46,  # 12012119498191750760927755905421357433806   ',
    100  # 59679665510247967544955524070889507976585
]

# Times': [ 2.1000030040740967,
#                    3.5400052070617676,
#                    3.846005439758301,
#                    2.005002975463867,
#                    4.455006122589111
#                    4.585006475448608,
#                    3.3450047969818115,
#                    2.0900027751922607,
#                    4.485006093978882,
#                    2.4250035285949707]


POP_SIZE = int(sum(popSizes)/len(popSizes))


ratiosParents = [
    42,  # 77304821201341145841731808396183936380084   ',
    87,  # 65227268462521045178149780102827337961506   ',
    42,  # 10054131929369876299983219503340483559606   ',
    47,  # 64154343470163404736905975221543013897263   ',
    63,  # 84146523079354578729618805480699788035355   ',
    30,  # 72000301428343629148164362406608235351153   ',
    4,  # 22647201571802444581484964932930249855596   ',
    78,  # 40849129751827873593384772673782713370019   ',
    57,  # 73730044297316696979916593455687247182943   ',
    70  # 41017568448533075147682297489383387060805   '
]

#   { 'bestTimes': [ 2.6800038814544678,
#                    3.6650049686431885,
#                    5.955008506774902,
#                    2.80000376701355,
#                    3.9850056171417236],
#                    4.710006475448608,
#                    2.5460033416748047,
#                    4.435006141662598,
#                    1.7400023937225342,
#                    6.105008363723755],


RATIO_SELECTED_PARENTS = sum(ratiosParents)/len(ratiosParents)


crossoverProbabilities = [
    9,  # 72711734309566977139110687521435887085027   ',
    26,  # 75493281485610471114275086223253062609139   ',
    58,  # 617771866242227395136854080313867164063   ',
    26,  # 50413206290878119665569176217559987552163   ',
    36,  # 32341474903823884575288197919674667391878   '
    11,  # 57092835875979569756576569353407579022899   ',
    8,  # 55407810372922069941855740880204737477425   ',
    19,  # 76663320510137196649273257129025785056811   ',
    55,  # 16872333953337503934653693718269183845230   ',
    18  # 28394198696543123820836475860517386122831   '],
]

#   {'bestTimes': [3.115004539489746,
#                    5.765007972717285,
#                    4.0550055503845215,
#                    2.1150028705596924,
#                    1.6700024604797363],
#   { 'bestTimes': [ 1.495002269744873,
#                    0.9350011348724365,
#                    0.9300010204315186,
#                    3.6000049114227295,
#                    1.4300017356872559],


CROSS_OVER_PROB = sum(crossoverProbabilities)/len(crossoverProbabilities)


mutationRates = [

    8,  # 80104423781092459455947216290085428336113   ',
    15,  # 66671579430643755365597158423550201375766   ',
    17,  # 57024946581638439101399775303136034877476   ',
    15,  # 51382975329969454414422270548622136801392   ',
    18,  # 60292068922061633228389742143659048996943   '
    13,  # 45066877629516674534119525225061540820567   ',
    19,  # 31147612887120858218110083009387263278326   ',
    19,  # 77333184628598948904043570869266284207031   ',
    17,  # 42288469531415021708620823139802536827873   ',
    6  # 37625324834873432485426706442381904979278   '
]


#   { 'bestTimes': [ 3.0000040531158447,
#                    1.1150012016296387,
#                    17.110023975372314,
#                    6.111008644104004,
#                    9.96601390838623],

#   { 'bestTimes': [ 3.305004835128784,
#                    1.5100018978118896,
#                    1.4100019931793213,
#                    3.6600050926208496,
#                    1.0750014781951904],


MUTATION_RATE = sum(mutationRates)/len(mutationRates)

GROUP_NUM = int(sys.argv[1])
print('GROUP_NUM :', GROUP_NUM)

SAVE_TRACE = True
