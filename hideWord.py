def fitness(individual):

    global hiddenWord

    indivPhenotype = individual.toPhenotype()

    distance = abs(len(hiddenWord) - len(indivPhenotype))

    for i in range(min(len(hiddenWord), len(indivPhenotype))):

        if hiddenWord[i] != indivPhenotype[i]:

            distance += 1

    return 1/(distance+1)


def hide(word) :

    global hiddenWord

    hiddenWord = word

