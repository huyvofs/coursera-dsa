# Uses python3
import sys


def optimal_weight(W, w):
    res = [[0 for x in range(W + 1)] for x in range(len(w) + 1)]

    for i in range(0, len(w) + 1):
        for j in range(0, W + 1):
            if i == 0 or j == 0:
                res[i][j] = 0
            elif w[i - 1] > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(w[i - 1] + res[i - 1]
                                [j - w[i - 1]], res[i - 1][j])

    return res[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
