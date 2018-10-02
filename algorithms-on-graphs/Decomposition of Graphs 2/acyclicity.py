# Uses python3

import sys


def move_vertex(vertex, src, dst):
    src.remove(vertex)
    dst.append(vertex)


def acyclic(adj):
    finish = []
    current = []
    set = [x for x in range(len(adj))]

    def explore(v):
        move_vertex(v, set, current)
        for u in adj[v]:
            if u in finish:
                continue
            if u in current:
                return True
            if explore(u):
                return True
        move_vertex(v, current, finish)
        return False

    while len(set) > 0:
        if explore(set[0]):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
