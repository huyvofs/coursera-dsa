# Uses python3

import sys


def toposort(adj):
    visited = [False] * len(adj)
    order = []

    def explore(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                explore(u)
        order.append(v)

    for v in range(len(adj)):
        if not visited[v]:
            explore(v)

    order.reverse()
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
