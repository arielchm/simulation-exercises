sequence = ['Dry', 'Rainy']
observations = ('Dry', 'Rainy')
states = ('Low', 'High')
initial = {'Low': 0.4, 'High': 0.6}
transition = {
    'Low': {'Low': 0.3, 'High': 0.7},
    'High': {'Low': 0.2, 'High': 0.8}
}
emition = {
    'Low': {'Dry': 0.4, 'Rainy': 0.6},
    'High': {'Dry': 0.6, 'Rainy': 0.4}
}


def forward():
    result = {}
    for i in range(len(sequence)):
        currentObservation = sequence[i]
        if i == 0:
            for state in states:
                result[state] = initial[state] * \
                    emition[state][currentObservation]
        else:
            previousResult = result.copy()
            for state in states:
                value = 0
                for previousState in states:
                    value = value + \
                        transition[previousState][state] * \
                        previousResult[previousState]

                result[state] = value * emition[state][currentObservation]
    return sum(result.values())


print(forward())
