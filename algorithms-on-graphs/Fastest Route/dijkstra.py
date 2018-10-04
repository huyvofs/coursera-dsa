# Uses python3

import sys
import queue


def extract_min(visited, dist):
    min_vertex = len(dist)
    min_distance = 9223372036854775807

    for v in range(len(dist)):
        if not visited[v] and dist[v] < min_distance:
            min_vertex = v
            min_distance = dist[v]

    return min_vertex


def distance(adj, cost, s, t):
    vertices = len(adj)
    dist = [9223372036854775807] * vertices
    visited = [False] * vertices
    dist[s] = 0

    for _ in range(vertices - 1):
        v = extract_min(visited, dist)
        if v == vertices:
            break
        visited[v] = True
        i = 0  # magic variable
        for u in adj[v]:
            if not visited[u] and dist[u] > dist[v] + cost[v][i]:
                dist[u] = dist[v] + cost[v][i]
            i += 1

    return dist[t] if dist[t] != 9223372036854775807 else -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
