from itertools import product


def reg_sum_hits(n, s):
    all_variants = list(product(range(1, s + 1), repeat=n))
    counter = {}
    for variant in all_variants:
        sum_value = sum(variant)
        if sum_value in counter.keys():
            counter[sum_value] += 1
        else:
            counter[sum_value] = 1
    return [[i, j] for i, j in counter.items()]


print(reg_sum_hits(2, 6))
