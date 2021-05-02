import timeit

import numpy

"""
Sum the numbers from 0 to n-1 in different ways.
"""

# 13.05s


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:  # done in python
        s += i
        i += 1
    return s

# 6.75s
# python pass interation in C, which is why for is faster


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i  # done in python
    return s


# 13.50
def for_loop_with_increment(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
        i += 1  # does not do anything but will increase the time
    return s

# 12.19s


def for_loop_with_test(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n:
            pass  # useless check add time
        s += i
    return s


# 18.04s
def for_loop_with_increment_and_test(n=100_000_000):
    s = 0
    for i in range(n):
        if i < n:
            pass
        i += 1
        s += i
    return s

# 3.85s, use buildin instead of loops will speed up, not memory constraint.


def sum_range(n=100_000_000):
    return sum(range(n))


# 9.80s, not as fast as loops
def sum_generator(n=100_000_000):
    return sum(i for i in range(n))

# 12.72s


def sum_list_comp(n=100_000_000):
    return sum([i for i in range(n)])

# 0.50s, numpy is fast! This is one C call. Might not have n memory.  memory intensive.


def sum_numpy(n=100_000_000):
    return numpy.sum(numpy.arange(n, dtype=numpy.int64))


def sum_numpy_python_range(n=100_000_000):
    return numpy.sum(range(n))

# pure math is fastest.


def sum_math(n=100_000_000):
    return (n * (n - 1)) // 2


# fastest way to loop in Python is not to loop, but compute ahead.
# if have to use, use numpy and then build ins.
def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for pure\t\t', timeit.timeit(for_loop, number=1))
    print('for inc\t\t\t', timeit.timeit(for_loop_with_increment, number=1))
    print('for test\t\t', timeit.timeit(for_loop_with_test, number=1))
    print('for inc+test\t', timeit.timeit(for_loop_with_increment_and_test, number=1))
    print('sum range\t\t', timeit.timeit(sum_range, number=1))
    print('sum generator\t\t', timeit.timeit(sum_generator, number=1))
    print('sum list comp\t\t', timeit.timeit(sum_list_comp, number=1))
    print('numpy sum\t\t', timeit.timeit(sum_numpy, number=1))
    print('numpy sum python range\t\t', timeit.timeit(
        sum_numpy_python_range, number=1))
    print('math sum\t\t', timeit.timeit(sum_math, number=1))


if __name__ == '__main__':
    main()
