import random
demand = [1, 2, 2, 1, 3, 0, 3, 1, 3]
frequency = {i: demand.count(i) for i in demand}
probabilities = {i: frequency[i]/len(demand) for i in frequency}
accumulated = {}

for i in range(len(probabilities)):
    if (i == 0):
        accumulated[i] = probabilities[i]
    else:
        accumulated[i] = probabilities[i]+accumulated[i-1]

days = int(input("Number of days to simulate: "))
simulated_demand = []
print("Day\tR(i)\t\tDemand")
for n in range(days):
    a = random.random()
    value = -1
    for i in range(len(accumulated)):
        if (i == 0):
            if (a >= 0 and a < accumulated[i]):
                value = i
        elif(i < days):
            if (a >= accumulated[i-1] and a < accumulated[i]):
                value = i
        else:
            if (a >= accumulated[i-1] and a < 1):
                value = i
    simulated_demand.append(value)
    print(str(n+1)+"\t"+str(round(a, 5))+"\t\t"+str(value))

print(simulated_demand)
