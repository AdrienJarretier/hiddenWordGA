from common import *

from subprocess import check_output

import numpy
import json
import time


def fullFitness(genPopulation):
    genIndexSorted = []
    for i in range(len(genPopulation)):
        if genPopulation[i][1] == 0:
            genIndexSorted.append(i)

    if len(genIndexSorted) == 0:
        return numpy.argmax(list(map(lambda x: x[1], genPopulation)))

    com = [FITNESS_PROGAM, str(GROUP_NUM)]
    for genIndex in genIndexSorted:
        phen = genToPhen(genPopulation[genIndex][0])
        com.append(phen)

    fullOut = check_output(com)
    fullOut = fullOut.decode()
    allOut = fullOut.split('\r\n')
    scores = []
    for i in range(len(allOut)-1):
        out = allOut[i]
        score = float(out.split('\t')[1])
        scores.append(score)
        genPopulation[genIndexSorted[i]][1] = score
    return numpy.argmax(scores)

# ------------------------------------------------------


def genToPhen(genotype):
    choices = getFullChoices()
    phen = ''.join(list(map(lambda x: choices[x], genotype)))
    return phen


def generateRandom():
    genotype = []
    for i in range(GENOTYPE_LENGTH):
        genotype.append(random.randint(0, SIZE_CHOICES-1))
    return genotype

# ------------------------------------------------------


def mutate(genotype, chance):
    newGen = []
    for i in range(len(genotype)):
        char = genotype[i]
        if random.random() < chance:
            char = random.randint(0, SIZE_CHOICES-1)
        newGen.append(char)
    return newGen

# ------------------------------------------------------


def cross_over(g1, g2):
    child1 = []
    child2 = []
    cutter = random.randint(0, len(g1)-1)
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
    weights = list(map(lambda x: x[1], pop))
    indexs = random.choices(
        [i for i in range(len(pop))], weights=weights, k=count)
    return list(map(lambda x: pop[x], indexs))

# ------------------------------------------------------


def generateRandomPopulation(popSize):
    pop = []
    for i in range(popSize):
        pop.append([generateRandom(), 0])
    return pop


def sort_population(pop):
    return sorted(pop, key=lambda x: x[1], reverse=True)


# ------------------------------------------------------
# ------------------------------------------------------


# ------------------------------------------------------


if __name__ == '__main__':

    print()
    print(' --- Finding hidden word with a genetic algorithm --- ')
    print()

    start_time = time.time()

    population = generateRandomPopulation(POP_SIZE)

    bestInd = [None, 0]

    genCount = 0

    obsels = []

    while bestInd[1] < 1:

        genCount += 1

        bestIndex = fullFitness(population)

        thisBestInd = population[bestIndex]
        if thisBestInd[1] > bestInd[1]:
            bestInd = thisBestInd
            phenotype = genToPhen(bestInd[0])
            fitness = bestInd[1]
            obsels.append(
                {'individu': phenotype, 'generation': genCount, 'fitness': fitness})
            print('new best:', phenotype, '(', bestInd[1], ',', genCount, ')')

        if genCount % 1000 == 0:
            bg = thisBestInd[0]
            bf = thisBestInd[1]
            print('the best:', genToPhen(bg), '(', bf, ',', genCount, ')')

        selected = wheel_select(population, SELECT_ELITES_SIZE)

        newPop = []

        while len(newPop) < POP_SIZE:
            mum = selected[random.randint(0, SELECT_ELITES_SIZE-1)]
            dad = selected[random.randint(0, SELECT_ELITES_SIZE-1)]

            if random.random() < CROSS_OVER_PROB:
                c1, c2 = cross_over(mum[0], dad[0])
                mum[0] = c1
                dad[0] = c2

            mum = [mutate(mum[0], MUTATE_PROB_PER_GENE), 0]
            dad = [mutate(dad[0], MUTATE_PROB_PER_GENE), 0]

            newPop += [mum, dad]
        fullFitness(newPop)

        bigPop = sort_population(population + newPop)
        population = bigPop[:POP_SIZE]
        random.shuffle(population)

    print()
    print('found', genToPhen(bestInd[0]))
    print('in time', time.time()-start_time, 'seconds')
    printSeed()

    data = {'obsels': obsels, 'group_num': GROUP_NUM, 'seed': USED_SEED}
    TRACES_DIR = 'traces'
    filename = str(GROUP_NUM)+'_(' + \
        genToPhen(bestInd[0])+')_'+str(genCount)+'_'+str(USED_SEED)+'.json'

    SAVE_PATH = os.path.join(TRACES_DIR, filename)

    json.dump(data, open(SAVE_PATH, 'w'))
    print('save at', SAVE_PATH)
