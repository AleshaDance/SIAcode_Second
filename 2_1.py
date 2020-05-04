import math
import timeit

# Bine formula : 0.0000029000000000001247 / 0.0000029000000000001247 / 0.0000029000000000001247
# AVG Bine formula - 0.0000029000000000001247

# Iterative formula : 0.000006200000000001343 / 0.000006099999999998468 / 0.000006199999999997874
# AVG Iterative formula - 0.000006166666666665895

# Ascending dp : 0.0000004000000000010939 / 0.00000029999999999821836 / 0.00000029999999999821836
# AVG Ascending dp - 0.0000003333333333325102

# Downstream dp : 0.000035800000000002496e / 0.000025999999999998247 / 0.00002539999999999834
# AVG Downstream dp - 0.000029066666666666362

# Divide & rule : 0.000006200000000001343 / 0.000003900000000001125 / 0.000003900000000001125
# AVG Divide & rule - 0.000004666666666667864


def formula_bine():
    start = timeit.default_timer()
    result = (pow((1 + math.sqrt(5)) / 2, 35) - pow((1 - math.sqrt(5)) / 2, 35)) / math.sqrt(5)
    return [int(result), timeit.default_timer() - start]


def iterative_formula():
    start = timeit.default_timer()
    a, b = 1, 1
    for i in range(3, 36):
        if i % 2 == 0:
            a += b
        else:
            b += a
    result = max(a, b)
    return [result, timeit.default_timer() - start]


def divide_rule():
    start = timeit.default_timer()
    n = 35
    result = lambda n: result(n - 1) + result(n - 2) if n > 2 else 1
    return [result, timeit.default_timer() - start]


def top_down():
    start = timeit.default_timer()
    dictionary = {0: 0,
                  1: 1}

    def cycle(elem):
        if elem in dictionary:
            return dictionary[elem]
        dictionary[elem] = cycle(elem - 1) + cycle(elem - 2)
        return dictionary[elem]
    result = cycle(35)

    return [result, timeit.default_timer() - start]


def top_up():
    start = timeit.default_timer()

    def cycle(n):
        a, b = 0, 1
        for __ in range(n):
            a, b = b, a + b
        return a
    result = cycle(35)

    return [result, timeit.default_timer() - start]


print("=={}==\nResult: {} | Time: {}\n".format('Bine formula', formula_bine()[0], formula_bine()[1]))
print("=={}==\nResult: {} | Time: {}\n".format('Iterative formula', iterative_formula()[0], iterative_formula()[1]))
print("=={}==\nResult: {} | Time: {}\n".format('Divide & rule', divide_rule()[0], divide_rule()[1]))
print("=={}==\nResult: {} | Time: {}\n".format('Downstream dp', top_down()[0], top_down()[1]))
print("=={}==\nResult: {} | Time: {}\n".format('Ascending dp', top_up()[0], top_up()[1]))