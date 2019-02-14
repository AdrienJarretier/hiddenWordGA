from pptree import *



def printFamilyTree(individual, distance=0, childNode=None):

    solutionNode = Node(individual.toPhenotype(), childNode)


    # print('node {$' + individual.toPhenotype() + '$}', end='')

    if distance < 3:

        if individual.mum is not None:

            printFamilyTree(individual.mum, distance+1, solutionNode)

            
            # print(' '*distance, 'child {', end='')
            # printFamilyTree(individual.mum, distance+1)
            # print('}', end='')

        if individual.dad is not None:

            printFamilyTree(individual.dad, distance+1, solutionNode)


            # print(' '*distance, 'child {', end='')
            # printFamilyTree(individual.dad, distance+1)
            # print('}', end='')

    if distance == 0:

        print_tree(solutionNode)



