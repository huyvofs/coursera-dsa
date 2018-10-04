# Uses python3

import sys

sys.setrecursionlimit(200000)


def reverse_graph(adj):
    reverse_adj = [[] for _ in range(len(adj))]
    for vertex in range(len(adj)):
        for adj_vertex in adj[vertex]:
            reverse_adj[adj_vertex].append(vertex)
    return reverse_adj


def number_of_strongly_connected_components(adj):
    result = 0
    visited = [False] * len(adj)
    finish_order = []

    def explore(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                explore(u)
        finish_order.append(v)

    def explore_reverse(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                explore(u)

    for v in range(len(adj)):
        if not visited[v]:
            explore(v)

    adj = reverse_graph(adj)
    visited = [False] * len(adj)

    while finish_order:
        v = finish_order.pop()
        if not visited[v]:
            explore_reverse(v)
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
