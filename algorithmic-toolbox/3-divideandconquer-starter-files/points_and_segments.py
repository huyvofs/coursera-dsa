# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    cnt = {}
    segments_num = 0

    listpoints = [(x, 'l') for x in starts]
    listpoints += [(x, 'p') for x in points]
    listpoints += [(x, 'r') for x in ends]

    listpoints.sort()

    for p in listpoints:
        if p[1] == 'l':
            segments_num += 1
        elif p[1] == 'r':
            segments_num -= 1
        else:
            cnt[p[0]] = segments_num

    return [cnt[x] for x in points]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
