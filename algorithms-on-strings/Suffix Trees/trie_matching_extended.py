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


def prefix_trie_matching(text, trie, external_idx):
    idx = 0
    symbol = text[idx]
    current = trie[0]
    res = -1

    while True:
        if not current:
            return res
        if '$' in current:
            return res
        if symbol in current:
            current = trie[current[symbol]]
            res = external_idx
            idx += 1
            if idx < len(text):
                symbol = text[idx]
            elif '$' in current:
                return res
            else:
                symbol = '@'
                res = -1
        else:
            return res if '$' in current else -1


def solve(text, n, patterns):
    result = set()
    trie = build_trie(patterns)
    n = len(text)
    for i in range(n):
        value = prefix_trie_matching(text[i:], trie, i)
        if value != -1:
            result.add(value)

    return sorted(list(result))


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
