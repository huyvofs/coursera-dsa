# python3
import sys


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1

    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            if letter in current:
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1
        current['$'] = {}
    return tree


def solve(p, q):
    patterns = [p, q]
    for i in range(1, len(p)):
        patterns.append(p[i:])
        patterns.append(q[i:])

    trie = build_trie(patterns)
    print(trie)

    current = trie[0]
    substring = ""

    while '$' not in current or current == trie[0]:
        for child in current:
            substring += child
            if child not in q:
                return substring
            else:
                current = trie[current[child]]
                substring = substring[:-1]
    return p


p = sys.stdin.readline().strip()
q = sys.stdin.readline().strip()

ans = solve(p, q)

sys.stdout.write(ans + '\n')
