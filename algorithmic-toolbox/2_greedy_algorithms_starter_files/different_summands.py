# Uses python3
import sys


def optimal_summands(n):
    summands = []
    m = 1

    while n > 2 * m:
        summands.append(m)
        n -= m
        m += 1
    else:
        summands.append(n)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))

    for x in summands:
        print(x, end='')
