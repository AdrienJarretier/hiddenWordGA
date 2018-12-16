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

ratiosParents = [

    50

]

RATIO_SELECTED_PARENTS = sum(ratiosParents)/len(ratiosParents)

# PARENTS_SELECTED_SIZE = int(POP_SIZE / 2)

crossoverProbabilities = [

    2,  # 241951018739417220024846594761015198551027065860
    18,  # 556423771146402972412631043365392253297415970925
    18,  # 933279315061331901524001312263226291877158205031
    18,  # 1349067475760935017824336028901293145410030846361
    14,  # 280609004429807415475776980168847065279905492710
    14,  # 772629318679104773110134858151885197536104209830
    7,  # 1013732279000849181028748737926293807617784253058
    9,  # 815400720860164649145117541743112924424699709407
    17,  # 1163856676087015739072654447450378947655588852570
    8,  # 1308263811321100654169755369479712046139082040409
    5,  # 1087830290191702428806944320452561660191498446189
    15,  # 1356551455243820075063143151497233452541663575378
    3,  # 592062838236553925556155141908608083251138716148
    12,  # 284126676451303069952318043829142386429551454387
    10,  # 954502864191026317763120343474006263956038762956
    9,  # 996390299745288130051717150978855121779322580698
    3,  # 486926790651903304267580880706913382060438655837
    2  # 120429731259652096613125355697013669634614529545

]


CROSS_OVER_PROB = sum(crossoverProbabilities)/len(crossoverProbabilities)

mutationRates = [


    8,  # 93349979692297197883044107479601493851630400252
    9,  # 903860603288980701899501897057010203604415066201
    9,  # 646450174771161989453367923979814090663060166898

    10,  # 1370925320328070598749364956501344678626367313205

    10,  # 702279771265097274557639199615102335133591606916


    13,  # 979804055809967880784548137992037677913615747698
    16,  # 841224141087050625177963392526735868487810557404
    16,  # 1219637794890435896769837033335741390286120631435
    16,  # 1033075842203101595200874622781666705322206065209
    16,  # 1315073836764458347934692688513521765145071895125
    16,  # 338259452194744845939871876890712413316405605714
    16,  # 123323499599536742075984259324536534290807843730
    16,  # 1451051545941385832111281305152424511054072407522

    17,  # 1333168000160203230422044130619651317910441513925
    17,  # 235956400164186781187731139320620761961511295318
    17,  # 323911439605760349811115267686715377296843748195
    17,  # 720640866390440626191403482652944658789961178910
    17,  # 96882087916229283937148057803077796239716317046
    17,  # 237482759855575717667851305043571254967020280428
    17,  # 1269753704121786122149386166235052196935952057171
    17,  # 1388788849100313770336810435083964059145211104078

    18,  # 191698041560476803798862462198668571004933748946
    18,  # 1432738369933174409073832747400223892417740807380
    18,  # 984737122764993368123732199139078090951467293609
    18,  # 298985626997110734640277641124782845143120245736
    18,  # 1207929020736836417717528816270074606950916015252
    18,  # 519393923818527392894453849678067175860741522636

    18,  # 628845188619397862455803289174839019389440582840
    19,  # 992515042513338722783686708423604139913056271054
    19,  # 1313316412584196213772797988519087774000815749393
    19,  # 1165277474372717282703445954459970643824309044197
    19,  # 710679388256783002946121835002905725473959474292
    19,  # 1347151251877656092939536320350889930748653743804


    19,  # 566449887334110609399600746997340457299446100942

    19,  # 1047606475892292442804405147279484894371677058219


    20,  # 587391284601439425540326412057741473252431394299


    20,  # 1399867898855807130332640778088497326929296999722
    20,  # 1068751865872989674130197784566338872628241030424
    20,  # 1083153398491164914457678219493486683513883502358
    20,  # 678407068572448040595754045748749282001234766716


    20.3333333333,  # 243554523133885587236843211720600907341510790539
    20.3333333333,  # 895479107042187272816074542544580445829442095033
    20.3333333333,  # 968002592649491870959299078098517287128682351695
    20.3333333333,  # 500495989371689330699585492462433014081020094205


    21,  # 114922108006485490613265300533470588012529439825
    21,  # 1018310343553537097431493021462883307259424443661
    21,  # 823843951506468804507631244107570715483464438614

    22,  # 583576999695658761133502616487917580694931131784

    22,  # 297510189402973250404579512222768142770574545117
    22,  # 1363971966842979370454695133806382525603201639742

    22,  # 1212453881120642682262422730430609381354653304754

    23,  # 1077738541321100298074549526810803327797646563955
    23,  # 634419114328996779452300066017426900804902886251

    24,  # 1370081228373737443921312860138364010093299223025
    24,  # 371445580791980853003222029235035132496697766153

    25  # 1429494216597026025915126886762924277680306217054

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
