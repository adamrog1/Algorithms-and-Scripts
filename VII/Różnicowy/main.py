import random


def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]


def GenerateMutatedVector(mutationControlParam, population, i, leftEnd, rightEnd):
    tmp = population[:i]
    mutationPool = random.sample(tmp, 3)
    mutatedVector = []
    tmp.extend(population[(i + 1):])

    for j in range(len(mutationPool[0])):
        number = mutationPool[0][j] + mutationControlParam * (mutationPool[1][j] - mutationPool[2][j])
        number = max(min(number, rightEnd), leftEnd)
        mutatedVector.append(number)
    return mutatedVector


def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i + 1) * numberList[i] ** 2
    return sum


def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def DifferentialEvolution(Function, leftEnd, rightEnd, dimension, searchingMinimum=True):
    generationCount = 400  # liczba generacji
    populationCount = 200  # liczba osób w populacji
    mutationControlParam = 0.3  # parametr kontroli mutacji
    crossoverProbability = 0.5  # prawdopodobieństwo krzyżowania

    population = [RandomNumbers(leftEnd, rightEnd, dimension) for i in range(populationCount)]
    t = 0
    while t <= generationCount:
        # Mutacja:
        mutatedVectors = []
        for i in range(populationCount):
            mutatedVectors.append(GenerateMutatedVector(mutationControlParam, population, i, leftEnd, rightEnd))

        # Krzyżowanie:
        crossoveredVectors = []
        for i in range(populationCount):
            crossVec = []
            for j in range(dimension):
                r = random.random()
                di = random.randint(0, dimension - 1)
                if r > crossoverProbability and j != di:
                    crossVec.append(population[i][j])
                else:
                    crossVec.append(mutatedVectors[i][j])
            crossoveredVectors.append(crossVec)

        # Optymalizacja:
        for i in range(populationCount):
            if searchingMinimum == True:
                if Function(crossoveredVectors[i]) < Function(population[i]):
                    population[i] = crossoveredVectors[i]
            else:
                if Function(crossoveredVectors[i]) > Function(population[i]):
                    population[i] = crossoveredVectors[i]
        t += 1

    population.sort(key=lambda x: Function(x))
    if searchingMinimum == False: population.reverse()
    bestVector = population[0]
    for x in range(len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "maximum" if searchingMinimum == False else "minimum"
    print( str(Function.__name__) + "'s", extremum, "\n   x  =", bestVector, \
          "\n f(x) =", round(Function(bestVector), 5), "\n")


DifferentialEvolution(Sum_Squares, -10, 10, 5, False)
DifferentialEvolution(Weierstrass, -10, 10, 5, False)

DifferentialEvolution(Sum_Squares, -10, 10, 5, True)
DifferentialEvolution(Weierstrass, -10, 10, 5, True)