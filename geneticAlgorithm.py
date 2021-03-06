from common import *

from subprocess import check_output

from functools import reduce

import numpy
import pprint
import json
import time

if SHOW_PLOT:
    import matplotlib.pyplot as plt

import pyfiglet


def filterSpecials(text):

    specialsMap = {
        'àâä': 'a',
        'éèêë': 'e',
        'îï': 'i',
        'ûüù': 'u',
        'ôö': 'o',
        'ç': 'c',
        '°': 'o'
    }

    bannerWord = ''

    for c in text:
        replaced = False
        for key, replacement in specialsMap.items():
            for keyC in key:
                if c == keyC:
                    bannerWord += replacement
                    replaced = True
                    break
            if replaced:
                break
        if not replaced:
            bannerWord += c

    return bannerWord


# ------------------------------------------------------

# A class representing one individual in the populatio
#
# An individuals has
# a chromosome : a list of ints representing the index of the letters in the list returned by common.getFullChoices()
#
#
#


class Individual:

    nextId = 0

    def __init__(self, chromosome):

        self.id = Individual.nextId
        Individual.nextId += 1

        self.chromosome = chromosome[:]

        self.fitness = 0

        # self.fitness = getFitness_external(self)

    def __repr__(self):

        return self.toPhenotype() + ' ( ' + str(
            self.fitness) + ' ) id : ' + str(self.id)

    def toPhenotype(self):

        choices = getFullChoices()
        phenotype = ''.join(list(map(lambda x: choices[x], self.chromosome)))

        return phenotype


# ------------------------------------------------------


def fullFitness(population):

    for indiv in population:

        indiv.fitness = EXTERNAL_FITNESS_FUNCTION(indiv)


# ------------------------------------------------------

# # ------------------------------------------------------

# def fullFitness(genPopulation):

#     genIndexSorted = []
#     for i in range(len(genPopulation)):
#         if genPopulation[i].fitness == 0:
#             genIndexSorted.append(i)

#     if len(genIndexSorted) == 0:
#         return numpy.argmax(list(map(lambda x: x.fitness, genPopulation))), 0

#     com = [FITNESS_PROGAM, str(GROUP_NUM)]
#     for genIndex in genIndexSorted:
#         phen = genPopulation[genIndex].toPhenotype()
#         com.append(phen)

#     fullOut = check_output(com)
#     fullOut = fullOut.decode()
#     allOut = fullOut.split('\r\n')

#     scores = []
#     for i in range(len(allOut) - 1):
#         out = allOut[i]
#         score = float(out.split('\t')[1])
#         scores.append(score)
#         genPopulation[genIndexSorted[i]].fitness = score

# # ------------------------------------------------------


def generateRandom():
    genotype = []
    for _ in range(random.randint(1, 77)):
        genotype.append(random.randint(0, SIZE_CHOICES - 1))
    return genotype


# ------------------------------------------------------

# chromosome : the chromosome to mutate : list of ints
# mutationRate : The chance for each gene to be randomly replaced by another value : float
#
# returns the mutated chromosome
# def mutate(chromosome, mutationRate):

#     chance = mutationRate / 100

#     newChrom = []
#     for i in range(len(chromosome)):
#         char = chromosome[i]
#         if random.random() < chance:
#             char = random.randint(0, SIZE_CHOICES - 1)
#         newChrom.append(char)
#     return newChrom


def mutate(chromosome, mutationRate):

    MUTATION_DELETION = 0
    MUTATION_ADDITION = 1
    MUTATION_SUBSTITUTION = 2
    mutationType = 0

    chance = mutationRate / 100

    newChrom = chromosome[:]

    for i in range(len(chromosome)):

        if random.random() < chance:

            if len(newChrom) == 1:
                mutationType = random.randint(1, 2)
            else:
                mutationType = random.randint(0, 2)

            if mutationType == MUTATION_DELETION:

                deletePosition = random.randint(0, len(newChrom) - 1)
                del newChrom[deletePosition]

            elif mutationType == MUTATION_ADDITION:

                insertPosition = random.randint(0, len(newChrom))
                newChrom.insert(insertPosition,
                                random.randint(0, SIZE_CHOICES - 1))

            elif mutationType == MUTATION_SUBSTITUTION:

                substPosition = random.randint(0, len(newChrom) - 1)
                newChrom[substPosition] = random.randint(0, SIZE_CHOICES - 1)

    # for i in range(len(chromosome)):
    #     char = chromosome[i]
    #     if random.random() < chance:
    #         char = random.randint(0, SIZE_CHOICES - 1)
    #     newChrom.append(char)

    return newChrom


# ------------------------------------------------------


# chrom1, chrom2 : the chromosomes to mate : list of ints
#
#
#
# returns two new childs resulting of the crossover between the 2 given chromosomes
def cross_over(chrom1, chrom2):
    # print('g1 :',g1)
    # print('g2 :',g2)
    # print()

    child1 = []
    child2 = []
    cutter = random.randint(0, min(len(chrom1), len(chrom2)) - 1)

    def appendToChilds(gene1, gene2):

        child1.append(gene1)
        child2.append(gene2)

    for i in range(0, cutter):
        appendToChilds(chrom1[i], chrom2[i])

    for i in range(cutter, min(len(chrom1), len(chrom2))):
        appendToChilds(chrom2[i], chrom1[i])

    return child1, child2


# ------------------------------------------------------


# pop : list of Indivduals
# count : the quantity of individuals to select by roulette wheel
#
# returns list of selected individuals
def wheel_select(pop, count):
    weights = list(map(lambda x: x.fitness, pop))
    indexs = random.choices([i for i in range(len(pop))],
                            weights=weights,
                            k=count)
    return list(map(lambda x: pop[x], indexs))


# ------------------------------------------------------


# popSize : the number of individuals in the population : int
#
# return list of Individuals of len popSize
def generateRandomPopulation(popSize):
    pop = []
    for i in range(popSize):
        pop.append(Individual(generateRandom()))

    return pop


# ------------------------------------------------------


def sort_population(pop):
    return sorted(pop, key=lambda x: x.fitness, reverse=True)


# ------------------------------------------------------


# Generate a new generation of individuals by selecting parents, applying crossover and mutating the childs
#
# population : the current population : list of Individuals
# popSize : populaiton size : int
# mutationRate : mutation chance per : float
# crossoverProb : max run time in seconds : float
# ratioSelectedParents : max run time in seconds : float
#
# returns the new generation, a list of Individuals
def nextGeneration(population, popSize, mutationRate, crossoverProb,
                   ratioSelectedParents):

    parentsSelectedCount = int(popSize * ratioSelectedParents / 100)

    if len(population) == 0:
        pop = generateRandomPopulation(popSize)
        fullFitness(pop)
        return pop

    selected = wheel_select(population, parentsSelectedCount)

    newPop = []

    while len(newPop) < popSize:
        mumChrom = selected[random.randint(
            0, parentsSelectedCount - 1)].chromosome[:]
        dadChrom = selected[random.randint(
            0, parentsSelectedCount - 1)].chromosome[:]

        if random.random() < crossoverProb / 100:
            c1, c2 = cross_over(mumChrom, dadChrom)

            mumChrom = c1
            dadChrom = c2

        mum = Individual(mutate(mumChrom, mutationRate))
        dad = Individual(mutate(dadChrom, mutationRate))

        newPop += [mum, dad]

    # time.sleep(1)

    fullFitness(newPop)

    bigPop = sort_population(population + newPop)
    newGeneration = bigPop[:popSize]
    random.shuffle(newGeneration)

    return newGeneration


def getBestIndex(pop):
    return numpy.argmax(list(map(lambda x: x.fitness, pop)))


# ------------------------------------------------------

# Run the genetic algorithm with given parameters and set a max run time
#
# popSize : populaiton size : int
# maxTime : max run time in seconds : float
# mutationRate : mutation chance per : float
# crossoverProb : max run time in seconds : float
# ratioSelectedParents : max run time in seconds : float
#
# return runtime or -1 if the function times out


def runGA(popSize, maxTime, mutationRate, crossoverProb, ratioSelectedParents):

    start_time = time.time()

    population = []

    bestInd = Individual([])

    genCount = 0
    lastGenPrint = genCount

    obsels = []
    fitnesses = []

    if SHOW_PLOT:
        plt.ion()

        fig = plt.figure()
        ax = fig.add_subplot(111)
        line1, = ax.plot(
            [], fitnesses,
            'r-')  # Returns a tuple of line objects, thus the comma
        plt.title('Nombre de différences entre le meilleur' + '\n' +
                  'individu et le mot à trouver')

    if SHOW_PLOT:
        generationsNum = []

    while bestInd.fitness < 1 and time.time() - start_time < maxTime:

        population = nextGeneration(population, popSize, mutationRate,
                                    crossoverProb, ratioSelectedParents)

        genCount += 1

        bestIndex = getBestIndex(population)
        thisBestInd = population[bestIndex]

        if thisBestInd.fitness > bestInd.fitness:
            bestInd = thisBestInd
            # print('new best:', bestInd, ',', genCount, ')')

            distStr = str(int(1 / bestInd.fitness - 1))
            padding = 3 - len(distStr)

            textLine = 'Meilleur mot (distance : ' + ' ' * padding + distStr + ') : ' + bestInd.toPhenotype(
            )

            print(' ' + textLine, '\n')

            if SHOW_PLOT:

                fitnesses.append((1 / thisBestInd.fitness) - 1)
                generationsNum.append(genCount)
                line1.set_xdata(generationsNum)
                line1.set_ydata(fitnesses)

                #plt.title('Fitness of the best individual in time')
                ax.relim()
                ax.autoscale_view()
                bottom, top = ax.get_ylim()
                ax.set_ylim(0, top)

                fig.canvas.draw()
                fig.canvas.flush_events()

            # if bestInd.fitness >= 0.5 :
            # mutationRate = 0
            # crossoverProb = 0

            lastGenPrint = genCount

        fitnessList = [ind.fitness for ind in population]
        obsels.append({
            'bestPhenotype':
            bestInd.toPhenotype(),
            'bestFitness':
            bestInd.fitness,
            'nbEvaluation':
            POP_SIZE,
            'maxFitness':
            max(fitnessList),
            'minFitness':
            min(fitnessList),
            'meanFitness':
            reduce(lambda x, y: x + y, fitnessList) / len(fitnessList)
        })

        print(" Génération #", genCount, end='\r')

        # if genCount - lastGenPrint == 1000:
        #     print(
        #         'the best:',
        #         thisBestInd,
        #         end='')
        #     print(', generation #', end='')
        #     print(genCount, ')')
        #     lastGenPrint = genCount

    returnToken = -1

    if bestInd.fitness == 1:
        # fitnesses.append(1)

        print('\nLe mot a été trouvé!')
        foundWord = bestInd.toPhenotype()
        ascii_banner = pyfiglet.figlet_format(filterSpecials(foundWord))
        print(ascii_banner)
        print()

        runTime = time.time() - start_time

        print('\nen',
              int(runTime * 10) / 10, 'secondes et', genCount, 'générations\n')
        # printSeed()
        # line1.set_xdata(range(len(fitnesses)))
        # line1.set_ydata(fitnesses)
        # ax.relim()
        # ax.autoscale_view()
        # fig.canvas.draw()
        # fig.canvas.flush_events()
        returnToken = runTime

    else:

        foundWord = bestInd.toPhenotype()

        print("\n\n L'algorithme n'a pas trouvé la solution exacte")
        print(" en moins de", maxTime, "secondes.\n")

        label = "Plus proche trouvé : "

        print(' ' * (3 + len(label)), '-' * (len(foundWord) + 4))
        print('', label, ': |', foundWord, '|')
        print(' ' * (3 + len(label)), '-' * (len(foundWord) + 4))

        runTime = time.time() - start_time

        print('\nen',
              int(runTime * 10) / 10, 'secondes et', genCount, 'générations\n')
        # printSeed()

        returnToken = runTime

    if SAVE_TRACE and returnToken != -1:

        data = {'obsels': obsels, 'group_num': GROUP_NUM, 'seed': USED_SEED}
        TRACES_DIR = 'traces'
        filename = str(GROUP_NUM)+'_(' + \
            bestInd.toPhenotype()+')_'+str(genCount) + \
            '_'+str(USED_SEED)+'.json'

        SAVE_PATH = os.path.join(TRACES_DIR, filename)

        json.dump(data, open(SAVE_PATH, 'w'))
        print('save at', SAVE_PATH)

    return returnToken


########################################################
# ------------------------------------------------------

# This is used to optimize the hyper parameters

parameters = [
    'POP_SIZE', 'MUTATION_RATE', 'CROSS_OVER_PROB', 'RATIO_SELECTED_PARENTS'
]

parametersValues = [
    POP_SIZE, MUTATION_RATE, CROSS_OVER_PROB, RATIO_SELECTED_PARENTS
]

# ------------------------------------------------------
########################################################


def reset():
    Individual.nextId = 0


def main(maxRunTime):

    reset()

    mainTimeStart = time.time()

    pp = pprint.PrettyPrinter(indent=2)

    print()
    print(' --- Recherche du mot caché avec un algorithme génétique --- ')
    print()

    # ranges = [
    #     [200, 2, -1],  # POP
    #     [100, 0, -1],  # MUT
    #     [100, 0, -1],  # CROSS
    #     [100, 2, -1]  # RATIO_SELECTED_PARENTS
    # ]

    ranges = [
        [POP_SIZE, POP_SIZE - 1, 1],  # POP
        [MUTATION_RATE, MUTATION_RATE - 1, 1],  # MUT
        [CROSS_OVER_PROB, CROSS_OVER_PROB - 1, 1],  # CROSS
        [RATIO_SELECTED_PARENTS, RATIO_SELECTED_PARENTS - 1,
         1]  # RATIO_SELECTED_PARENTS
    ]

    # store the results of the optimization loops
    results = []

    for parameterUsedId in range(1):  # len(parameters)):

        bestValues = []
        bestTimes = []

        minValue = ranges[parameterUsedId][0]
        maxValue = ranges[parameterUsedId][1]

        while len(bestValues) < 1:  # 5:

            loopTimeStart = time.time()

            print()
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
            # print('POP_SIZE :', POP_SIZE)
            # print('MUTATION_RATE :', MUTATION_RATE)
            # print('CROSS_OVER_PROB :', CROSS_OVER_PROB)
            # print('RATIO_SELECTED_PARENTS :', RATIO_SELECTED_PARENTS)
            print()
            # print('changin parameter : ' + parameters[parameterUsedId])

            # USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

            # resetRNG(USED_SEED)

            maxTime = runGA(POP_SIZE, maxRunTime, MUTATION_RATE,
                            CROSS_OVER_PROB, RATIO_SELECTED_PARENTS)

            # print(parameters[parameterUsedId] + ' range :', minValue, '-',
            #       maxValue)

            bestValue = parametersValues[parameterUsedId]

            # +1):
            for v in range(minValue, maxValue + ranges[parameterUsedId][2],
                           ranges[parameterUsedId][2]):

                vs = [
                    POP_SIZE, MUTATION_RATE, CROSS_OVER_PROB,
                    RATIO_SELECTED_PARENTS
                ]

                vs[parameterUsedId] = v

                resetRNG(USED_SEED)

                print()
                print(parameters[parameterUsedId] + ' :', v)

                runTime = runGA(vs[0], maxTime, vs[1], vs[2], vs[3])

                if runTime != -1:
                    if runTime < maxTime:
                        maxTime = runTime
                        bestValue = v
                else:
                    print('timeout')

            if maxTime > -1:
                bestValues.append('   ' + str(bestValue) + ', # ' +
                                  str(USED_SEED) + '   ')
                bestTimes.append(maxTime)

        result = {
            'parameter': parameters[parameterUsedId],
            'bestValues': bestValues
            # ,'bestTimes': bestTimes
        }
        results.append(result)

        # print()
        # print('best ' + parameters[parameterUsedId] + ' s :')
        # pp.pprint(bestValues)
        # print()
        # print('bestTimes :')
        # pp.pprint(bestTimes)

    # print()
    # pp.pprint(results)
