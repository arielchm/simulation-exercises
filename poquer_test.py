from collections import Counter
import math

random_numbers = [0.85881, 0.99700, 0.75289, 0.82813, 0.02818, 0.36065, 0.45649, 0.06451, 0.07582, 0.73994,
                  0.52480, 0.03333, 0.50410, 0.76568, 0.11767, 0.37587, 0.55763, 0.33089, 0.53339, 0.41700,
                  0.24577, 0.74797, 0.92023, 0.93143, 0.05520, 0.94996, 0.35838, 0.85376, 0.41727, 0.08969]

# todos diferentes, un par, dos pares, three_of_a_kind, full_house, poker, five_of_a_kind

probabilities = [0.3024, 0.5040, 0.1080, 0.072, 0.0090, 0.0045, 0.0001]

all_different = 0
one_pair = 0
two_pairs = 0
three_of_a_kind = 0
full_house = 0
poker = 0
five_of_a_kind = 0

for i in range(len(random_numbers)):
    n = random_numbers[i]*100000
    a = int(n/10000)
    b = int((n % 10000)/1000)
    c = int((n % 1000)/100)
    d = int((n % 100)/10)
    e = int((n % 10))
    digits = [a, b, c, d, e]
    frequencies = dict((x, digits.count(x)) for x in set(digits))
    if len(frequencies) == 5:
        all_different += 1
    if len(frequencies) == 1:
        five_of_a_kind += 1
    if len(frequencies) == 4:
        one_pair += 1
    if len(frequencies) == 2:
        for i in frequencies:
            if frequencies[i] == 4:
                poker += 1
                break
            if frequencies[i] == 2:
                full_house += 1
                break
    if len(frequencies) == 3:
        for i in frequencies:
            if frequencies[i] == 3:
                three_of_a_kind += 1
                break
            if frequencies[i] == 2:
                two_pairs += 1
                break

observed_frequencies = [all_different, one_pair, two_pairs,
                        three_of_a_kind, full_house, poker, five_of_a_kind]
total = all_different+five_of_a_kind+one_pair + \
    two_pairs+three_of_a_kind+poker+full_house
expected_frequencies = [float(total)*float(probabilities[i])
                        for i in range(len(observed_frequencies))]
print("INITIAL FREQUENCIES")
print(f"Observed: {observed_frequencies}")
print(f"Expected: {expected_frequencies}")
expected_frequencies.reverse()
observed_frequencies.reverse()

while expected_frequencies[0] < 5:
    expected_frequencies[1] = expected_frequencies[1]+expected_frequencies[0]
    observed_frequencies[1] = observed_frequencies[1]+observed_frequencies[0]
    expected_frequencies.pop(0)
    observed_frequencies.pop(0)

expected_frequencies.reverse()
observed_frequencies.reverse()
print("ADJUSTED FREQUENCIES")
print(f"Observed: {observed_frequencies}")
print(f"Expected: {expected_frequencies}")

table = [(expected_frequencies[i]-observed_frequencies[i])**2/expected_frequencies[i]
         for i in range(len(observed_frequencies))]
print(f"(fo-fe)^2/fe: {table}")
alfa = len(expected_frequencies)-1
s = sum(table)
print(s)

chi = {0.05: [3.84, 5.99, 7.81, 9.49, 11.07, 12.59, 14.07, 15.51]}
if s < chi[0.05][alfa-1]:
    print("These numbers are random")
else:
    print("These numbers are NOT random")
