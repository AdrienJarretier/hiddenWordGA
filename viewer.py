import matplotlib.pyplot as plt
import json

filename = 'traces/25_(__P1K4CHU___)_1512_40514377531397772412586756095806046791652.json'

data = json.load(open(filename,'r'))

obsels = data['obsels']
group_num = data['group_num']
seed = data['seed']
password = obsels[-1]['bestPhenotype']

maxs = [obsel['maxFitness'] for obsel in obsels]
means = [obsel['meanFitness'] for obsel in obsels]
mins = [obsel['minFitness'] for obsel in obsels]

plt.title('Groupe ' + str(group_num) + ' -- "' + password + '"')

plt.plot(maxs)
plt.plot(means)

plt.show()