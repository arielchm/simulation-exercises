import operator
sequence = ['6', '1', '3', '6', '6', '6', '3', '5', '1', '6']
observations = ('1', '2', '3', '4', '5', '6')
states = ('Regular', 'Loaded')
initial = {'Regular': 0.5, 'Loaded': 0.5}
transition = {
    'Regular': {'Regular': 0.95, 'Loaded': 0.05},
    'Loaded': {'Regular': 0.05, 'Loaded': 0.95}
}
emition = {
    'Regular': {'1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6},
    'Loaded': {'1': 1/10, '2': 1/10, '3': 1/10, '4': 1/10, '5': 1/10, '6': 1/2}
}

estimated = []
statesProbabilities = {}


def initialize(currentObservation):
    for state in states:
        statesProbabilities[state] = [
            initial[state]*emition[state][currentObservation]]


def iterate(currentObservation):
    probabilities = {}
    for state in states:
        probabilities[state] = statesProbabilities[state][-1]
    for state in states:
        values = []
        for previousState in states:
            values.append(probabilities[previousState]*transition[previousState]
                          [state]*emition[state][currentObservation])
        statesProbabilities[state].append(max(values))


for i in range(len(sequence)):
    if i == 0:
        initialize(sequence[i])
    else:
        iterate(sequence[i])

for i in range(len(sequence)):
    values = {}
    for state in states:
        values[state] = statesProbabilities[state][i]
    estimated.append(max(values.items(), key=operator.itemgetter(1))[0])

print(statesProbabilities)
print(estimated)
