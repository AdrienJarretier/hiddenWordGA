from common import *

from subprocess import check_output

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
        return numpy.argmax(list(map(lambda x: x.fitness, genPopulation)))

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
    return numpy.argmax(scores)


# ------------------------------------------------------


def generateRandom():
    genotype = []
    for _ in range(GENOTYPE_LENGTH):
        genotype.append(random.randint(0, SIZE_CHOICES - 1))
    return genotype


# ------------------------------------------------------


def mutate(genotype, chance):
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


def nextGeneration(population):

    if len(population) == 0:
        return generateRandomPopulation(POP_SIZE)

    selected = wheel_select(population, PARENTS_SELECTED_SIZE)

    newPop = []

    while len(newPop) < POP_SIZE:
        mum = selected[random.randint(0, PARENTS_SELECTED_SIZE - 1)]
        dad = selected[random.randint(0, PARENTS_SELECTED_SIZE - 1)]

        if random.random() < CROSS_OVER_PROB:
            c1, c2 = cross_over(mum.chromosome, dad.chromosome)
            mum.chromosome = c1
            dad.chromosome = c2

        mum = Individual(mutate(mum.chromosome, MUTATION_RATE))
        dad = Individual(mutate(dad.chromosome, MUTATION_RATE))

        newPop += [mum, dad]
    fullFitness(newPop)

    bigPop = sort_population(population + newPop)
    newGeneration = bigPop[:POP_SIZE]
    random.shuffle(newGeneration)

    return newGeneration


# ------------------------------------------------------

# run the genetic algorithm with a given populaiton size and set a max run time
#
# popSize : populaiton size : int
# maxTime : max run time in seconds : float
#
# return runtime or -1 if the function times out
def runGA(popSize, maxTime):

    start_time = time.time()

    population = []

    bestInd = Individual([])

    genCount = 0
    lastGenPrint = genCount

    obsels = []

    while bestInd.fitness < 1 and time.time() - start_time < maxTime:

        population = nextGeneration(population)

        genCount += 1

        bestIndex = fullFitness(population)

        thisBestInd = population[bestIndex]

        if thisBestInd.fitness > bestInd.fitness:

            bestInd = thisBestInd

            phenotype = bestInd.toPhenotype()
            obsels.append({
                'individu': phenotype,
                'generation': genCount,
                'fitness': bestInd.fitness
            })
            print('new best:', bestInd, ',', genCount, ')')
            lastGenPrint = genCount

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

    if bestInd.fitness == 1:

        print()
        print('found', bestInd)

        runTime = time.time() - start_time

        print('in time', runTime, 'seconds')
        # printSeed()

        return runTime

    else:

        return -1

    if SAVE_TRACE:

        data = {'obsels': obsels, 'group_num': GROUP_NUM, 'seed': USED_SEED}
        TRACES_DIR = 'traces'
        filename = str(GROUP_NUM)+'_(' + \
            bestInd.toPhenotype()+')_'+str(genCount) + \
            '_'+str(USED_SEED)+'.json'

        SAVE_PATH = os.path.join(TRACES_DIR, filename)

        json.dump(data, open(SAVE_PATH, 'w'))
        print('save at', SAVE_PATH)


if __name__ == '__main__':

    mainTimeStart = time.time()

    pp = pprint.PrettyPrinter(indent=2)

    print()
    print(' --- Finding hidden word with a genetic algorithm --- ')
    print()

    bestPop = POP_SIZE

    bestPops = []
    bestTimes = []

    mainRunTime = 32400

    minLoopTime = 0

    while time.time() - mainTimeStart < mainRunTime - minLoopTime:

        loopTimeStart = time.time()

        print()
        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
        print('POP_SIZE :', POP_SIZE)

        USED_SEED = int.from_bytes(os.urandom(20), sys.byteorder)

        resetRNG(USED_SEED)

        maxTime = runGA(POP_SIZE, math.inf)

        minPop = max(1, min(popSizes) - (max(popSizes) - min(popSizes)))
        maxPop = max(popSizes) + (max(popSizes) - min(popSizes))

        print('pop size range :', minPop, '-', maxPop)

        for popSize in range(minPop, maxPop+1):

            print()
            print('popSize :', popSize)

            runTime = runGA(popSize, maxTime)

            if runTime != -1:
                if runTime < maxTime:
                    maxTime = runTime
                    bestPop = popSize
            else:
                print('timeout')

        bestPops.append('  ' + str(bestPop) + ', # ' + str(USED_SEED) + '  ')
        bestTimes.append(maxTime)

        loopTime = time.time() - loopTimeStart

        if minLoopTime == 0 or loopTime < minLoopTime:

            minLoopTime = loopTime

    print()
    print('bestPops :')
    pp.pprint(bestPops)
    print()
    print('bestTimes :')
    pp.pprint(bestTimes)
