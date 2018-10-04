# Uses python3

import sys


def negative_cycle(adj, cost):
    vertices = len(adj)
    dist = [9223372036854775807] * vertices
    dist[0] = 0

    for _ in range(vertices - 1):
        for u in range(vertices):
            i = 0  # magic variable
            for v in adj[u]:
                weight = dist[u] + cost[u][i]
                if dist[v] > weight:
                    dist[v] = weight
                else:
                    i += 1

    for u in range(vertices):
        i = 0
        for v in adj[u]:
            weight = dist[u] + cost[u][i]
            if dist[v] > weight:
                return 1
            else:
                i += 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
