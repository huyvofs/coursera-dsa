# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def PolyHash(s, prime, multiplier):
    hash = 0
    for c in reversed(s):
        hash = (hash * multiplier + ord(c)) % prime
    return hash


def PrecomputeHashes(text, len_pattern, prime, multiplier):
    H = [None] * (len(text) - len_pattern + 1)
    S = text[len(text) - len_pattern:]
    H[len(text) - len_pattern] = PolyHash(S, prime, multiplier)
    y = 1
    for i in range(len_pattern):
        y = (y * multiplier) % prime
    for i in range(len(text) - len_pattern - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) -
                y * ord(text[i + len_pattern])) % prime
    return H


def get_occurrences(pattern, text):
    result = []
    prime = 1610612741
    multiplier = 263
    p_hash = PolyHash(pattern, prime, multiplier)
    H = PrecomputeHashes(text, len(pattern), prime, multiplier)

    for i in range(len(text) - len(pattern) + 1):
        if (p_hash == H[i]) and (text[i:i + len(pattern)] == pattern):
            result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
