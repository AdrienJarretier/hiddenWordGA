import matplotlib.pyplot as plt
import json
import sys
import os

if len(sys.argv) < 3:
  print('You need to specify <group_num> <seed_used>')
  exit()

group_num = sys.argv[1]
seed = sys.argv[2]

tracesDir = './traces'

filename = ''
for file in os.listdir(tracesDir):
  if group_num+'_' in file and '_'+seed+'.json' in file:
    filename = tracesDir + '/' + file
    break

data = json.load(open(filename,'r'))

obsels = data['obsels']
group_num = data['group_num']
seed = data['seed']
password = obsels[-1]['bestPhenotype']

maxs = [obsel['maxFitness'] for obsel in obsels]
means = [obsel['meanFitness'] for obsel in obsels]
mins = [obsel['minFitness'] for obsel in obsels]

plt.title('Groupe ' + str(group_num) + ' "' + password + '"')

plt.plot(maxs, label='Fitness maximum')
plt.plot(means, label='Fitness moyenne')

plt.xlabel('Générations')
plt.ylabel('Fitness')

plt.legend()

plt.show()