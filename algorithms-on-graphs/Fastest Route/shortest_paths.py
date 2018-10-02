# Uses python3
import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    vertices = len(adj)
    distance[s] = 0
    reachable[s] = 1
    queue = []
    visited = [False]*vertices

    for _ in range(vertices-1):
        for u in range(vertices):
            i = 0  # magic variable
            for v in adj[u]:
                if distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    reachable[v] = 1
                i += 1

    for u in range(vertices):
        i = 0  # magic variable
        for v in adj[u]:
            if distance[v] > distance[u] + cost[u][i]:
                if v not in queue:
                    queue.append(v)
            i += 1

    while queue:
        u = queue.pop(0)
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v] and v not in queue:
                queue.append(v)


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
