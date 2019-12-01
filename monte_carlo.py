import random

# Monte Carlo
# Estimates the probabilites of rolling a sequence, using a Monte Carlo simulation


def roll():
    sides = [1, 2, 3, 4, 5, 6]
    result = random.choice(sides)
    return result


def simulate(goal, throws):
    total = 0
    for i in range(throws):
        result = ''
        for j in range(len(goal)):
            result += str(roll())
        if result == goal:
            total += 1
    calculated_probability = round(1/float(6**(len(goal))), 8)
    estimated_probability = round(total/float(throws), 8)

    print('Estimated probability of ' + goal +
          ' = '+str(calculated_probability))
    print('Approx. probability of' +
          goal + ' = '+str(estimated_probability))


simulate('6546', 100000)
