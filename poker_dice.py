# Calculates the probability of rolling a poker dice combination using the Monte Carlo Method

import random


def roll():
    side = [1, 2, 3, 4, 5, 6]
    result = []
    for i in range(5):
        result.append(random.choice(side))
    result.sort(reverse=True)
    return result


def simulate(combination, simulations):
    matches = 0

    combination_array = []
    for i in list(combination):
        combination_array.append(int(i))

    while(len(combination_array) < 5):
        combination_array.append(0)
    combination_array.sort(reverse=True)

    for i in range(simulations):
        result = roll()
        frequency = []
        while len(result) != 0:
            value = result[0]
            frequency.append(result.count(value))
            while value in result:
                result.remove(value)
        frequency.sort(reverse=True)

        while(len(frequency) < 5):
            frequency.append(0)

        if combination_array == frequency:
            matches += 1
    approximated_p = round(matches/float(simulations), 10)

    print('Approximated probability of rolling ' +
          combination + ' = '+str(approximated_p))


simulate('32', 100000)
