# python3
import sys


def preprocess_bwt(bwt):
    sorted_bwt = ''.join(sorted(bwt))
    char_set = set(sorted_bwt)
    starts = {x: sorted_bwt.find(x) for x in char_set}

    occ_count_before = {}

    for x in char_set:
        lst = [0]
        counter = 0
        for i in range(len(bwt)):
            if bwt[i] == x:
                counter += 1
            lst.append(counter)
        occ_count_before[x] = lst

    return starts, occ_count_before


def count_occurrences(pattern, bwt, starts, occ_counts_before):
    top, bottom = 0, len(bwt) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom + 1]:
                first_occurence = starts[symbol]
                top = first_occurence + occ_counts_before[symbol][top]
                bottom = first_occurence + \
                    occ_counts_before[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()

    starts, occ_counts_before = preprocess_bwt(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(
            count_occurrences(
                pattern,
                bwt,
                starts,
                occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
