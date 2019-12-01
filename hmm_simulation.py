# Given the following probabilites simulate a HMM for a regular and loaded dice

import random
pi = [0.7, 0.3]
A = [[0.6, 0.4], [0.6, 0.4]]
B = [[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], [1/4, 1/4, 1/4, 1/4, 0, 0]]

observations = []
state_sequence = []
n = 10


def chooseFromVector(vector):
    a = random.random()
    i = 0
    s = vector[0]
    while (a > s):
        i += 1
        s += vector[i]
    return i


def determine_state(state_sequence):
    dice = []
    for i in range(len(state_sequence)):
        if state_sequence[i] == 0:
            dice.append('Regular')
        if state_sequence[i] == 1:
            dice.append('Loaded')
    return dice


def simulate(k):
    for j in range(k):
        state_sequence = []
        observations = []
        selected_die = chooseFromVector(pi)
        state_sequence.append(selected_die)
        observations.append(chooseFromVector(B[selected_die])+1)

        for i in range(n-1):
            selected_die = chooseFromVector(A[selected_die])
            state_sequence.append(selected_die)
            observations.append(chooseFromVector(B[selected_die])+1)

        # print(state_sequence)
        print(determine_state(state_sequence))
        print(observations)
        print('------------------------------')


simulate(150)
