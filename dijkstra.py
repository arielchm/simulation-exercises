from math import inf
adjacency_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                    [4, 0, 8, 0, 0, 0, 0, 11, 0],
                    [0, 8, 0, 7, 0, 4, 0, 0, 2],
                    [0, 0, 7, 0, 9, 14, 0, 0, 0],
                    [0, 0, 0, 9, 0, 10, 0, 0, 0],
                    [0, 0, 4, 14, 10, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 2, 0, 1, 6],
                    [8, 11, 0, 0, 0, 0, 1, 0, 7],
                    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

size = len(adjacency_matrix)


def dijkstra(adjacency_matrix, s):
    visited = []
    length = len(adjacency_matrix)
    min_distances = [inf]*length
    min_distances[s] = 0
    while len(visited) < length:
        l = []  # lista de distancias a todos los nodos no visitados
        for i in range(length):
            if i not in visited:
                l.append(min_distances[i])
                # print(str(l))
        smallest = min(l)
        index = min_distances.index(smallest)
        visited.append(index)
        index = 0
        for j in adjacency_matrix[index]:
            if j != 0:
                alt = min_distances[index] + \
                    adjacency_matrix[index][index]
                if alt < min_distances[index]:
                    min_distances[index] = alt
            index += 1
    return min_distances


print('Min. distance from node 0 to all nodes')
print(dijkstra(adjacency_matrix, 0))
