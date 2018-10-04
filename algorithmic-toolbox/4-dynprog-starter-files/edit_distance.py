# Uses python3
def edit_distance(s, t):
    n = len(s) + 1
    m = len(t) + 1

    D = [[0 for x in range(m)] for x in range(n)]

    for i, j in zip(range(n), range(m)):
        D[i][0] = i
        D[0][j] = j

    for j in range(1, m):
        for i in range(1, n):
            insertion = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1
            mismatch = D[i - 1][j - 1] + 1
            match = D[i - 1][j - 1]
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)

    return D[n - 1][m - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
