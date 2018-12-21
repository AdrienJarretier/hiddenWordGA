from common import *

from subprocess import check_output

from functools import reduce

import numpy
import pprint
import json
import time


class Individual:
    def __init__(self, chromosome):

        self.chromosome = chromosome[:]

        self.fitness = 0

        # self.fitness = getFitness_external(self)

    def __repr__(self):

        return self.toPhenotype() + ' ( ' + str(self.fitness) + ' )'

    def toPhenotype(self):

        choices = getFullChoices()
        phenotype = ''.join(list(map(lambda x: choices[x], self.chromosome)))

        return phenotype


def fullFitness(genPopulation):

    genIndexSorted = []
    for i in range(len(genPopulation)):
        if genPopulation[i].fitness == 0:
            genIndexSorted.append(i)

    if len(genIndexSorted) == 0:
        return numpy.argmax(list(map(lambda x: x.fitness, genPopulation))), 0

    com = [FITNESS_PROGAM, str(GROUP_NUM)]
    for genIndex in genIndexSorted:
        phen = genPopulation[genIndex].toPhenotype()
        com.append(phen)

    fullOut = check_output(com)
    fullOut = fullOut.decode()
    allOut = fullOut.split('\r\n')
    scores = []
    for i in range(len(allOut) - 1):
        out = allOut[i]
        score = float(out.split('\t')[1])
        scores.append(score)
        genPopulation[genIndexSorted[i]].fitness = score


# ------------------------------------------------------


def generateRandom():
    genotype = []
    for _ in range(GENOTYPE_LENGTH):
        genotype.append(random.randint(0, SIZE_CHOICES - 1))
    return genotype


# ------------------------------------------------------


def mutate(genotype, mutationRate):

    chance = mutationRate / 100

    newGen = []
    for i in range(len(genotype)):
        char = genotype[i]
        if random.random() < chance:
            char = random.randint(0, SIZE_CHOICES - 1)
        newGen.append(char)
    return newGen


# ------------------------------------------------------


def cross_over(g1, g2):
    child1 = []
    child2 = []
    cutter = random.randint(0, len(g1) - 1)
    for i in range(0, len(g1)):
        c1 = g1[i]
        c2 = g2[i]
        if i > cutter:
            c1 = g2[i]
            c2 = g1[i]
        child1.append(c1)
        child2.append(c2)
    return child1, child2


# ------------------------------------------------------


def wheel_select(pop, count):
    weights = list(map(lambda x: x.fitness, pop))
    indexs = random.choices([i for i in range(len(pop))],
                            weights=weights,
                            k=count)
    return list(map(lambda x: pop[x], indexs))


# ------------------------------------------------------


def generateRandomPopulation(popSize):
    pop = []
    for i in range(popSize):
        pop.append(Individual(generateRandom()))

    return pop


def sort_population(pop):
    return sorted(pop, key=lambda x: x.fitness, reverse=True)


# ------------------------------------------------------
# ------------------------------------------------------


def nextGeneration(population, popSize, mutationRate, crossoverProb, ratioSelectedParents):

    parentsSelectedCount = int(popSize * ratioSelectedParents/100)

    if len(population) == 0:
        pop = generateRandomPopulation(popSize)
        fullFitness(pop)
        return pop

    selected = wheel_select(population, parentsSelectedCount)

    newPop = []

    while len(newPop) < popSize:
        mum = selected[random.randint(0, parentsSelectedCount - 1)]
        dad = selected[random.randint(0, parentsSelectedCount - 1)]

        if random.random() < crossoverProb/100:
            c1, c2 = cross_over(mum.chromosome, dad.chromosome)
            mum.chromosome = c1
            dad.chromosome = c2

        mum = Individual(mutate(mum.chromosome, mutationRate))
        dad = Individual(mutate(dad.chromosome, mutationRate))

        newPop += [mum, dad]

    fullFitness(newPop)

    bigPop = sort_population(population + newPop)
    newGeneration = bigPop[:popSize]
    random.shuffle(newGeneration)

    return newGeneration


def getBestIndex(pop):
    return numpy.argmax(list(map(lambda x: x.fitness, pop)))

# ------------------------------------------------------

# run the genetic algorithm with a given populaiton size and set a max run time
#
# popSize : populaiton size : int
# maxTime : max run time in seconds : float
#
# return runtime or -1 if the function times out


def runGA(popSize, maxTime, mutationRate, crossoverProb, ratioSelectedParents):

    start_time = time.time()

    population = []

    bestInd = Individual([])

    genCount = 0
    lastGenPrint = genCount

    obsels = []

    while bestInd.fitness < 1 and time.time() - start_time < maxTime:

        population = nextGeneration(
            population, popSize, mutationRate, crossoverProb, ratioSelectedParents)

        genCount += 1

        bestIndex = getBestIndex(population)
        thisBestInd = population[bestIndex]

        if thisBestInd.fitness > bestInd.fitness:
            bestInd = thisBestInd
            print('new best:', bestInd, ',', genCount, ')')
            lastGenPrint = genCount

        fitnessList = [ind.fitness for ind in population]
        obsels.append({
            'bestPhenotype': bestInd.toPhenotype(),
            'bestFitness': bestInd.fitness,
            'nbEvaluation': POP_SIZE,
            'maxFitness': max(fitnessList),
            'minFitness': min(fitnessList),
            'meanFitness': reduce(lambda x, y: x+y, fitnessList)/len(fitnessList)
        })

        if genCount - lastGenPrint == 1000:
            print(
                'the best:',
                thisBestInd.toPhenotype(),
                '(',
                thisBestInd.fitness,
                end='')
            print(', generation #', end='')
            print(genCount, ')')
            lastGenPrint = genCount

    returnToken = -1
    if bestInd.fitness == 1:

        print()
        print('found', bestInd)

        runTime = time.time() - start_time

        print('in time', runTime, 'seconds')
        # printSeed()

        returnToken = runTime

    if SAVE_TRACE:

        data = {'obsels': obsels, 'group_num': GROUP_NUM, 'seed': USED_SEED}
        TRACES_DIR = 'traces'
        filename = str(GROUP_NUM)+'_(' + \
            bestInd.toPhenotype()+')_'+str(genCount) + \
            '_'+str(USED_SEED)+'.json'

        SAVE_PATH = os.path.join(TRACES_DIR, filename)

        json.dump(data, open(SAVE_PATH, 'w'))
        print('save at', SAVE_PATH)

    return returnToken


parameters = ['POP_SIZE', 'MUTATION_RATE',
              'CROSS_OVER_PROB', 'RATIO_SELECTED_PARENTS']

parametersValues = [POP_SIZE, MUTATION_RATE,
                    CROSS_OVER_PROB, RATIO_SELECTED_PARENTS]

if __name__ == '__main__':

    mainTimeStart = time.time()

    pp = pprint.PrettyPrinter(indent=2)

    print()
    print(' --- Finding hidden word with a genetic algorithm --- ')
    print()

    mainRunTime = 9*3600

    minLoopTime = 0

    ranges = [
        [200, 2, -1],  # POP
        [100, 0, -1],  # MUT
        [100, 0, -1],  # CROSS
        [100, 2, -1]  # SELECT
    ]

    results = []

    for parameterUsedId in range(len(parameters)):  # len(parameters)):

        bestValues = []
        bestTimes = []

        minValue = ranges[parameterUsedId][0]
        maxValue = ranges[parameterUsedId][1]

        while len(bestValues) < 1:  # 5:

            loopTimeStart = time.time()

            print()
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
            print('POP_SIZE :', POP_SIZE)
            print('MUTATION_RATE :', MUTATION_RATE)
            print('CROSS_OVER_PROB :', CROSS_OVER_PROB)
            print('RATIO_SELECTED_PARENTS :', RATIO_SELECTED_PARENTS)
            print()
            print('changin parameter : ' + parameters[parameterUsedId])

            USED_SEED = int.from_bytes(os.urandom(SEED_SIZE), sys.byteorder)

            resetRNG(USED_SEED)

            maxTime = runGA(POP_SIZE, 9, MUTATION_RATE,
                            CROSS_OVER_PROB, RATIO_SELECTED_PARENTS)

            print(parameters[parameterUsedId] +
                  ' range :', minValue, '-', maxValue)

            bestValue = parametersValues[parameterUsedId]

            # +1):
            for v in range(minValue, maxValue+ranges[parameterUsedId][2], ranges[parameterUsedId][2]):

                vs = [POP_SIZE, MUTATION_RATE,
                      CROSS_OVER_PROB, RATIO_SELECTED_PARENTS]

                vs[parameterUsedId] = v

                resetRNG(USED_SEED)

                print()
                print(parameters[parameterUsedId] + ' :', v)

                runTime = runGA(vs[0], maxTime, vs[1],
                                vs[2], vs[3])

                if runTime != -1:
                    if runTime < maxTime:
                        maxTime = runTime
                        bestValue = v
                else:
                    print('timeout')

            if maxTime > -1:
                bestValues.append(
                    '   ' + str(bestValue) + ', # ' + str(USED_SEED) + '   ')
                bestTimes.append(maxTime)

            loopTime = time.time() - loopTimeStart

            if minLoopTime == 0 or loopTime < minLoopTime:

                minLoopTime = loopTime

        result = {

            'parameter': parameters[parameterUsedId],
            'bestValues': bestValues
            # ,'bestTimes': bestTimes

        }
        results.append(result)

        print()
        print('best ' + parameters[parameterUsedId] + ' s :')
        pp.pprint(bestValues)
        print()
        print('bestTimes :')
        pp.pprint(bestTimes)

    print()
    pp.pprint(results)
