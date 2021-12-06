from utils import read_lines
import numpy as np


def run(data, iterations):
    """
    [
        0 days left
        1 day left
        2 days left
        3 days left
        4 days left
        5 days left
        6 days left
        7 days left
        8 days left
    ]
    """
    timers = np.zeros(9, dtype=int)
    data = [int(n) for n in data[0].split(',')]

    # make the initial list
    for n in data:
        timers[n] += 1

    for i in range(iterations):
        # remember the amount of fish with timer of 0
        zero_timers = timers[0]
        # rotate left
        timers = np.roll(timers, -1)
        # make new ones
        timers[8] = zero_timers
        # add the ones that was a 0s before as 6s
        timers[6] += zero_timers

    return timers.sum()


def run1(data):
    return run(data, 80)


def run2(data):
    return run(data, 256)


if __name__ == '__main__':
    data = read_lines('inputs/day06.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
