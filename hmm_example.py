# Estimate weather given a persons mood

sequence = ['Happy', 'Happy', 'Sad', 'Sad', 'Sad', 'Happy', 'Happy']

sunny_day_prob = 0.67
rainy_day_prob = 0.33
happy_if_sunny = 0.8
sad_if_sunny = 0.2
happy_if_rainy = 0.4
sad_if_rainy = 0.6
sunny_if_sunny = 0.8
rainy_if_sunny = 0.2
sunny_if_Rainy = 0.4
rainy_if_rainy = 0.6
sunny_prob = []
rainy_prob = []
estimated = []

for i in range(len(sequence)):
    if i == 0:
        if sequence[i] == 'Happy':
            sunny_prob.append(sunny_day_prob * happy_if_sunny)
            rainy_prob.append(rainy_day_prob * happy_if_rainy)
        if sequence[i] == 'Sad':
            sunny_prob.append(sunny_day_prob * sad_if_sunny)
            rainy_prob.append(rainy_day_prob * sad_if_rainy)
    else:
        a = sunny_prob[-1]
        b = rainy_prob[-1]
        if sequence[i] == 'Happy':
            values = []
            values.append(a*sunny_if_sunny*happy_if_sunny)
            values.append(b*sunny_if_Rainy*happy_if_sunny)
            sunny_prob.append(max(values))
            values = []
            values.append(a*rainy_if_sunny*happy_if_rainy)
            values.append(b*rainy_if_rainy*happy_if_rainy)
            rainy_prob.append(max(values))
        if sequence[i] == 'Sad':
            values = []
            values.append(a*sunny_if_sunny*sad_if_sunny)
            values.append(b*sunny_if_Rainy*sad_if_sunny)
            sunny_prob.append(max(values))
            values = []
            values.append(a*rainy_if_sunny*sad_if_rainy)
            values.append(b*rainy_if_rainy*sad_if_rainy)
            rainy_prob.append(max(values))

for i in range(len(sunny_prob)):
    if sunny_prob[i] > rainy_prob[i]:
        estimated.append('Sunny')
    else:
        estimated.append('Rainy')

print(sunny_prob)
print(rainy_prob)
print(estimated)
