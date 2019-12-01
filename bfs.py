# Breadth First Search

graph = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F', 'G'],
         'C': ['H', 'I', 'J'],
         'D': ['K'],
         'E': ['L', 'M', 'N'],
         'F': ['O'],
         'G': ['P'],
         'H': [],
         'I': [],
         'J': [],
         'K': [],
         'L': [],
         'M': [],
         'N': [],
         'O': [],
         'P': []}


def bfs(graph, s):
    mark = [s]
    remaining = [s]
    while remaining:
        u = remaining[0]
        children = graph[u]
        unmarked = [v for v in children if v not in mark]
        if unmarked:
            v = unmarked[0]
            mark.append(v)
            remaining.append(v)
        else:
            remaining.remove(u)
    return mark


print(bfs(graph, 'A'))
