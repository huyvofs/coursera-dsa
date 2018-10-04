# Uses python3

import sys


def reach(adj, x, y):
    visited = [False for x in range(len(adj))]

    def DFS(x):
        visited[x] = True
        for w in adj[x]:
            if w == y:
                visited[w]
            if visited[w] is False:
                DFS(w)
        return 1 if visited[y] is True else 0
    return DFS(x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
