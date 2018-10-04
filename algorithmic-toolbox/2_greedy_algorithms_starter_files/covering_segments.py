# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    segments = list(map(list, segments))
    segments.sort(key=lambda s: s[1], reverse=False)

    for i in range(len(segments)):
        if (i == 0) or (segments[i][0] != 0 and segments[i][1] != 0):
            points.append(segments[i][1])
            for x in segments[i+1:]:
                if x[0] <= segments[i][1] <= x[1]:
                    x[0] = 0
                    x[1] = 0
            segments[i][0] = 0
            segments[i][1] = 0

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]),
                        zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
