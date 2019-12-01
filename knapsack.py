#values = ['valor', 10, 4, 6, 9, 8, 3, 10, 2]
#weights = ['peso', 10, 5, 1, 3, 3, 4, 3, 1]

#values = ['valor', 15, 10, 9, 5]
#weights = ['peso', 1, 5, 3, 4]

values = ['valor', 10, 40, 30, 50]
weights = ['peso', 5, 4, 6, 3]


def knapsack(values, weights, n, m):
    f = {}
    for g in range(m + 1):
        f[0, g] = 0

    for i in range(1, n + 1):
        for g in range(m + 1):
            if weights[i] <= g:
                f[i, g] = max(
                    values[i] + f[i - 1, g - weights[i]], f[i - 1, g])
            else:
                f[i, g] = f[i - 1, g]
    return f[n, m]


print(knapsack(values, weights, 4, 10))
