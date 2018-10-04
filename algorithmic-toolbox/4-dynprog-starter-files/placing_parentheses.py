# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(M, m, i, j, operators):
    min_value = 10000000
    max_value = -10000000
    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], operators[k])
        b = evalt(M[i][k], m[k + 1][j], operators[k])
        c = evalt(m[i][k], M[k + 1][j], operators[k])
        d = evalt(m[i][k], m[k + 1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(digits, operators):
    n = len(digits)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            if i != j:
                m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n - 1]


if __name__ == "__main__":
    dataset = input()
    operators = []
    digits = []

    for char in dataset:
        if char in ['+', '-', '*']:
            operators.append(char)
        else:
            digits.append(int(char))

    print(get_maximum_value(digits, operators))
