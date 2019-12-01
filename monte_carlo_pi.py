# Generates approximated values of Pi for different number of simulations

import random
import math

radius = 1.0

simulations = [10, 100, 1000, 1000000, 10000000]


def montecarlo(simulations):
    r = []
    for n in simulations:
        inside_points = 0
        for i in range(n):
            x = random.random()*radius
            y = random.random()*radius
            d = math.sqrt(((x)**2)+((y)**2))
            if d <= radius:
                inside_points += 1
        pi = 4*(inside_points/n)
        r.append(pi)
    return r


print('For the following number of simulations:')
print(simulations)
print('The convergences are:')
print(montecarlo(simulations))
