# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    opt_value = 0
    items = list(zip(values, weights))
    items.sort(key=lambda item: item[0] / item[1], reverse=True)
    values = [item[0] for item in items]
    weights = [item[1] for item in items]

    for value, weight in zip(values, weights):
        if capacity == 0:
            return opt_value
        min_weight = min(weight, capacity)
        opt_value += min_weight * (value / weight)
        weight -= min_weight
        capacity -= min_weight

    return opt_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
