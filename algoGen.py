from common import *

from subprocess import check_output

import numpy
import json
import time


class Individual:
    def __init__(self, chromosome):

        self.chromosome = chromosome[:]

        self.fitness = 0

        # self.fitness = getFitness_external(self)

    def copy(self):

        indivCopy = Individual(self.chromosome)

        indivCopy.fitness = self.fitness

        return indivCopy

    def __repr__(self):

        return self.toPhenotype() + ' ( ' + str(bestInd.fitness) + ' )'

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

    selected = wheel_select(population, PARENTS_SELECTED_SIZE)

    newPop = []

    while len(newPop) < POP_SIZE:
        mum = selected[random.randint(0, PARENTS_SELECTED_SIZE - 1)].copy()
        dad = selected[random.randint(0, PARENTS_SELECTED_SIZE - 1)].copy()

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

if __name__ == '__main__':

    print()
    print(' --- Finding hidden word with a genetic algorithm --- ')
    print()

    start_time = time.time()

    population = generateRandomPopulation(POP_SIZE)

    bestInd = Individual([])

    genCount = 0

    obsels = []

    while bestInd.fitness < 1:

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

        if genCount % 1000 == 0:
            print(
                'the best:',
                thisBestInd.toPhenotype(),
                '(',
                thisBestInd.fitness,
                end='')
            print(', generation #', end='')
            print(genCount, ')')

        population = nextGeneration(population)

    print()
    print('found', bestInd.toPhenotype())

    runTime = time.time() - start_time

    maxTime = runTime
    bestPop = POP_SIZE

    print('in time', runTime, 'seconds')
    printSeed()

    if SAVE_TRACE:

        data = {'obsels': obsels, 'group_num': GROUP_NUM, 'seed': USED_SEED}
        TRACES_DIR = 'traces'
        filename = str(GROUP_NUM)+'_(' + \
            bestInd.toPhenotype()+')_'+str(genCount) + \
            '_'+str(USED_SEED)+'.json'

        SAVE_PATH = os.path.join(TRACES_DIR, filename)

        json.dump(data, open(SAVE_PATH, 'w'))
        print('save at', SAVE_PATH)

    # print('bestPop :', bestPop)
    # print('maxTime :', maxTime)
