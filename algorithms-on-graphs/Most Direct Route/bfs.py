# Uses python3

import sys
import queue


def distance(adj, s, t):
    n = len(adj)
    dist = [n] * n
    dist[s] = 0
    queue = []
    queue.append(s)

    while queue:
        v = queue.pop(0)
        for u in adj[v]:
            if dist[u] == n:
                queue.append(u)
                dist[u] = dist[v] + 1

    return -1 if dist[t] == n else dist[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
