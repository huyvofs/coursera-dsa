# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = [max(lines)]
act = {}


def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    lineRoot = 0

    if realDestination == realSource:
        return False

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lineRoot = lines[realDestination]
        lines[realSource] = 0

    elif rank[realDestination] == rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lineRoot = lines[realDestination]
        lines[realSource] = 0
        rank[realDestination] += 1

    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lineRoot = lines[realSource]
        lines[realDestination] = 0

    if lineRoot > ans[0]:
        ans[0] = lineRoot

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans[0])
