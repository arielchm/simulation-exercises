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

n = len(sequence)


def alpha():
    result = {}
    for i in range(n):
        current_observation = sequence[i]
        if i == 0:
            for state in states:
                result[state] = initial[state] * \
                    emition[state][current_observation]
        elif i < n:
            previousResult = result.copy()
            for state in states:
                value = 0
                for previous_state in states:
                    value = value + \
                        transition[previous_state][state] * \
                        previousResult[previous_state]

                result[state] = value * emition[state][current_observation]
    return result


def backward():
    inverse_sequence = sequence[::-1]
    state_probabilities = {key: 1 for key in states}
    for i in range(n-1):
        current_observation = inverse_sequence[i]
        previous_prob = state_probabilities.copy()
        for state in states:
            value = 0
            for previous_state in states:
                value += transition[state][previous_state] * \
                    emition[previous_state][current_observation] * \
                    previous_prob[previous_state]
            state_probabilities[state] = value
    return state_probabilities


print('alfa * beta: '+str(sum(alpha().values())*sum(backward().values())))
