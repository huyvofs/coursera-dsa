# Uses python3
import sys


def optimal_sequence(n):
    sequence = []

    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = arr[i - 1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i // 2] + 1, arr[i])
        if i % 3 == 0:
            arr[i] = min(arr[i // 3] + 1, arr[i])

    while n >= 1:
        sequence.append(n)
        if arr[n] == arr[n - 1] + 1:
            n = n - 1
        elif n % 2 == 0 and arr[n // 2] == arr[n] - 1:
            n = n // 2
        elif n % 3 == 0 and arr[n // 3] == arr[n] - 1:
            n = n // 3

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
