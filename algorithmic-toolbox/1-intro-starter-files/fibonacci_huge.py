# Uses python3
import sys


def picasa_number_length(m):
    res = []

    while True:
        if not res:
            res = [0, 1]
        res.append((res[len(res) - 1] + res[len(res) - 2]) % m)
        if res[len(res) - 1] == 1 and res[len(res) - 2] == 0:
            break

    return len(res) - 2


def calc_fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def get_fibonaccihuge(n, m):
    return (calc_fib(n % picasa_number_length(m)) % m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
