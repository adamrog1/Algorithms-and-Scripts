import random


def RandomNumbers(leftend, rightend, n):
    return [random.uniform(leftend, rightend) for number in range(n)]


def Krzyzowanie(first, second, leftEnd, rightEnd):
    child = []
    for i in range(len(first)):
        chromosome = first[i] + random.random() * (second[i] - first[i])
        chromosome = max(min(chromosome, rightEnd), leftEnd)
        child.append(chromosome)
    return child


def Sum_Squares(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (i + 1) * numberList[i] ** 2
    return sum


def Weierstrass(numberList):
    sum = 0
    for i in range(len(numberList)): sum += (abs(numberList[i] + 0.5)) ** 2
    return sum


def GeneticAlgorithm(Function, leftEnd, rightEnd, dimension, searchingMinimum=True):
    generationCount = 120  # liczba generacji
    populationCount = 400  # wielkość populacji
    population = [RandomNumbers(leftEnd, rightEnd, dimension) for i in range(populationCount)]

    t = 0
    population.sort(key=lambda x: Function(x))
    if searchingMinimum == False: population.reverse()

    while t <= generationCount:
        # Mutacja:
        lambdaVector = RandomNumbers(0, 1, populationCount)
        mutationProbability = random.random()
        for personNumber in range(populationCount):
            if lambdaVector[personNumber] < mutationProbability:
                ksi = random.random()
                for chromosome in population[personNumber]:
                    chromosome = max(min(chromosome + ksi, rightEnd), leftEnd)

        # Krzyżowanie:
        for i in range(populationCount - 1):
            population.append(Krzyzowanie(population[i], population[i + 1], leftEnd, rightEnd))

        # Sukcesja elitarna:
        population.sort(key=lambda x: Function(x))
        if searchingMinimum == False: population.reverse()
        population = population[:populationCount]
        t += 1

    bestVector = population[0]
    for x in range(len(bestVector)): bestVector[x] = round(bestVector[x], 5)
    extremum = "max" if searchingMinimum == False else "min"
    print( str(Function.__name__) + "'s", extremum, "\n   x  =", bestVector, \
          "\n f(x) =", round(Function(bestVector), 5), "\n")


GeneticAlgorithm(Sum_Squares, -10, 10, 5, False)
GeneticAlgorithm(Weierstrass, -10, 10, 5, False)
GeneticAlgorithm(Sum_Squares, -10, 10, 5, True)
GeneticAlgorithm(Weierstrass, -10, 10, 5, True)