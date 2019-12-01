import time
sequence = ['Seco', 'Lluvioso', 'Seco', 'Seco', 'Lluvioso', 'Seco']
observations = ('Seco', 'Lluvioso')
states = ('Baja', 'Alta')
initial = {'Baja': 0.4, 'Alta': 0.6}
transition = {
    'Baja': {'Baja': 0.3, 'Alta': 0.7},
    'Alta': {'Baja': 0.2, 'Alta': 0.8}
}
emition = {
    'Baja': {'Seco': 0.4, 'Lluvioso': 0.6},
    'Alta': {'Seco': 0.6, 'Lluvioso': 0.4}
}

n = len(sequence)
combination_vector = []


def generate_combinations(combination_vector):
    if len(combination_vector) == 0:
        for state in states:
            combination_vector.append([state])
    else:
        for i in range(len(combination_vector)):
            element = combination_vector[0]
            combination_vector.pop(0)
            for state in states:
                sub = element.copy()
                sub.append(state)
                combination_vector.append(sub)
    return combination_vector


def calculate(observed_sequence, combination_sequence):
    value = initial[combination_sequence[0]] * \
        emition[combination_sequence[0]][observed_sequence[0]]
    for i in range(len(combination_sequence)-1):
        value *= transition[combination_sequence[i]][combination_sequence[i+1]
                                                     ]*emition[combination_sequence[i+1]][observed_sequence[i+1]]
    return value


def inefficient_method():
    for i in range(n):
        generate_combinations(combination_vector)
    start_time = time.time()
    probability = 0
    for i in range(len(combination_vector)):
        probability += calculate(sequence, combination_vector[i])
    end_time = time.time()
    # print(str(start_time))
    # print(str(end_time))
    # print(str(end_time-start_time))
    return [probability, str(end_time-start_time)]


def forward():
    start_time = time.time()
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
                result[state] = value * \
                    emition[state][currentObservation]
    end_time = time.time()
    # print(str(start_time))
    # print(str(end_time))
    # print(str(end_time-start_time))
    return [sum(result.values()), str(end_time-start_time)]


print("-----------------------------------------------")
print("NAIVE")
inefficient_results = inefficient_method()
print("Probability: ",
      inefficient_results[0], "\nExec. time: ", inefficient_results[1])
print("-----------------------------------------------")
print("FORWARD")
results = forward()
print("Probability: ", results[0], "\nExec. time: ", results[1])
