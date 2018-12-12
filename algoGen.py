from subprocess import check_output
import random
import numpy
import json
import time
import sys
import os

# seed sympas:
# - 236957502862991091183765 - 23794
# - 46255 - 3225 - 7
# - 42474 - 17728 - 9
# - 30542 - 17837 - 1
# - 30542 - 17837 - 1
# - 31744 - 2252 - 7

R_SEED = int.from_bytes(os.urandom(2), sys.byteorder)
#R_SEED = 30542
print(R_SEED)
random.seed(R_SEED)

def fullFitness(genPopulation):
  genIndexSorted = []
  for i in range(len(genPopulation)):
    if genPopulation[i][1]==0:
      genIndexSorted.append(i)

  if len(genIndexSorted) == 0:
    return numpy.argmax(list(map(lambda x:x[1],genPopulation)))

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

def getFullChoices():
  return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789___'

SIZE_CHOICES = len(getFullChoices())

def genToPhen(genotype):
  choices = getFullChoices()
  phen = ''.join(list(map(lambda x: choices[x],genotype)))
  return phen

def generateRandom():
  genotype = []
  for i in range(GENOTYPE_LENGTH):
    genotype.append(random.randint(0,SIZE_CHOICES-1))
  return genotype

# ------------------------------------------------------

def mutate(genotype, chance):
  newGen = []
  for i in range(len(genotype)):
    char = genotype[i]
    if random.random() < chance:
      char = random.randint(0,SIZE_CHOICES-1)
    newGen.append(char)
  return newGen

# ------------------------------------------------------

def cross_over(g1,g2):
  child1 = []
  child2 = []
  cutter = random.randint(0,len(g1)-1)
  for i in range(0,len(g1)):
    c1 = g1[i]
    c2 = g2[i]
    if i > cutter :
      c1 = g2[i]
      c2 = g1[i]
    child1.append(c1)
    child2.append(c2)
  return child1,child2

# ------------------------------------------------------

def wheel_select(pop,count):
  weights = list(map(lambda x: x[1],pop))
  indexs = random.choices([i for i in range(len(pop))], weights=weights, k=count)
  return list(map(lambda x: pop[x],indexs))

# ------------------------------------------------------

def generateRandomPopulation(popSize):
  pop = []
  for i in range(popSize):
    pop.append([generateRandom(),0])
  return pop

def sort_population(pop):
  return sorted(pop,key=lambda x: x[1],reverse=True)


# ------------------------------------------------------
# ------------------------------------------------------

FITNESS_PROGAM = 'ibi_2018-2019_fitness_windows.exe'
GENOTYPE_LENGTH = 12

import sys

GROUP_NUM = int(sys.argv[1])

print('Searching for group number',GROUP_NUM,'...')

POP_SIZE = 80
SELECT_ELITES_SIZE = int(POP_SIZE*0.5)

CROSS_OVER_PROB = 0.5
MUTATE_PROB_PER_GENE = 0.2

# ------------------------------------------------------

start_time = time.time()

population = generateRandomPopulation(POP_SIZE)

bestInd = [None,0]

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
    obsels.append({'individu':phenotype,'generation':genCount,'fitness':fitness})
    print('new best:',phenotype,'(',bestInd[1],',',genCount,')')

  if genCount%100 == 0:
    bg = thisBestInd[0]
    bf = thisBestInd[1]
    print('the best:',genToPhen(bg),'(',bf,',',genCount,')')

  selected = wheel_select(population,SELECT_ELITES_SIZE)

  newPop = []

  while len(newPop) < POP_SIZE:
    mum = selected[random.randint(0,SELECT_ELITES_SIZE-1)]
    dad = selected[random.randint(0,SELECT_ELITES_SIZE-1)]

    if random.random() < CROSS_OVER_PROB:
      c1,c2 = cross_over(mum[0],dad[0])
      mum[0] = c1
      dad[0] = c2

    mum = [mutate(mum[0],MUTATE_PROB_PER_GENE),0]
    dad = [mutate(dad[0],MUTATE_PROB_PER_GENE),0]

    newPop += [mum,dad]
  fullFitness(newPop)

  bigPop = sort_population(population + newPop)
  population = bigPop[:POP_SIZE]
  random.shuffle(population)

print('found',genToPhen(bestInd[0]))
print('in time',time.time()-start_time,'seconds')
print(R_SEED)

data = {'obsels':obsels,'group_num':GROUP_NUM,'seed':R_SEED}
filename = str(GROUP_NUM)+'_('+genToPhen(bestInd[0])+')_'+str(genCount)+'_'+str(R_SEED)+'.json'
json.dump(data,open(filename,'w'))
print('save at',filename)