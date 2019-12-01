# Linear Congruential Generator


def lcg(n):
    x = 123456789.0
    a = 101427
    b = 321
    m = (2 ** 16)
    i = 0
    f = open('pseudoRandomNumbers.txt', 'w')
    while i < n:
        x = (a * x + b) % m
        u = x/m
        f.write('u(' + str(i) + ') = ' + str(u) + '\n')
        i += 1
    f.close()


lcg(100000)
