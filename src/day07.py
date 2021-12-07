from utils import read_lines
import numpy as np
import math


def geo_sum(n):
    return int((n*(n+1))/2)


def run1(data):
    arr = [int(n) for n in data[0].split(',')]
    median = int(np.median(arr))
    return np.array([abs(n - median) for n in arr]).sum()


def run2(data):
    arr = [int(n) for n in data[0].split(',')]
    mean = np.mean(arr)
    mean_down = math.floor(mean)
    mean_up = math.ceil(mean)

    return min(
        np.array([geo_sum(abs(n - mean_down)) for n in arr]).sum(),
        np.array([geo_sum(abs(n - mean_up)) for n in arr]).sum(),
    )


if __name__ == '__main__':
    data = read_lines('inputs/day07.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
