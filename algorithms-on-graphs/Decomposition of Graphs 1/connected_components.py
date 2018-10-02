# Uses python3

import sys


def number_of_components(adj):
    visited = [False for x in range(len(adj))]
    components = 0

    def DFS(x):
        visited[x] = True
        for w in adj[x]:
            if visited[w] is False:
                DFS(w)

    for vertex in range(len(adj)):
        if visited[vertex] is False:
            components += 1
            DFS(vertex)

    return components


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
