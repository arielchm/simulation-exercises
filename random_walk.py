import random
import math

walks = 10000
deviation = 'North'
radius_of_action = 4


def randomWalk(steps, deviation):
    x, y = 0, 0
    weights = []
    if deviation == 'None':
        weights = [1, 1, 1, 1]
    elif deviation == 'North':
        weights = [2, 1, 1, 1]
    elif deviation == 'South':
        weights = [1, 2, 1, 1]
    elif deviation == 'East':
        weights = [1, 1, 2, 1]
    elif deviation == 'West':
        weights = [1, 1, 1, 2]
    for i in range(steps):
        (dx, dy) = random.choices(population=[
            (0, 1), (0, -1), (1, 0), (-1, 0)], weights=weights, k=1)[0]
        x += dx
        y += dy

    # Returns final position
    return (x, y)


def simulate(walks, walk_steps, deviation):
    stranded = 0
    distances = []
    x_values = []
    y_values = []
    for i in range(walks):
        (x, y) = randomWalk(walk_steps, deviation)
        distance = float(math.sqrt(x**2 + y**2))
        distances.append(distance)
        x_values.append(x)
        y_values.append(y)
        if distance > radius_of_action:
            stranded += 1

        return_probability = 1-float(stranded/walks)
    print('Return probability: ' + str(return_probability))
    print('Max. distance: ' + str(max(distances)))
    print('Min. distance: ' + str(min(distances)))
    print('Avg. distance: ' + str(sum(distances)/len(distances)))
    print('Avg. coordinates: (' + str(sum(x_values) /
                                      len(x_values))+', '+str(sum(y_values)/len(y_values))+') ')


for walk_steps in range(1, 31):
    print('========================================================')
    print('When ' + str(walk_steps)+' are taken')
    print('========================================================')
    print('Random')
    simulate(walks, walk_steps, 'None')
    print('--------------------------------------------------------')
    print(deviation+' deviation')
    simulate(walks, walk_steps, deviation)
    print('--------------------------------------------------------')
