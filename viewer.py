import matplotlib.pyplot as plt
import json

filename = 'traces/9_(_70_R_T4_NK_)_3216_27554115246066715920827339483807944935587.json'

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