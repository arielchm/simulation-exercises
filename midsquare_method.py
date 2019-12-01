# Midsquare method
seed = int(input('Enter a 4 digit number:\n'))
x = seed
pseudo_randoms = []
n = 0

while x not in pseudo_randoms:
    n += 1
    pseudo_randoms.append(x)
    aux = str(int(x * x)).zfill(8)[2:6]
    x = int(aux)
    u = '0.' + aux
    print('u(' + str(n) + ') = ' + str(u) + '\n')
