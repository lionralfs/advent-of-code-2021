from os import read
from utils import read_lines
from collections import Counter
import numpy as np


def most_common_bit(lst, fallback=0):
    data = Counter(lst)
    zero = data.get(0, 0)
    one = data.get(1, 0)
    if zero > one:
        return 0
    if zero == one:
        return fallback
    return 1


def flip(bit):
    return bit ^ 1


def to_decimal(list_of_bits):
    return int(''.join([str(x) for x in list_of_bits]), 2)


def oxygen_rating(data):
    column_count = data.shape[1]
    for column_i in range(column_count):
        b = most_common_bit(data[:, column_i], fallback=1)
        data = data[data[:, column_i] == b]
        if data.shape[0] == 1:
            return to_decimal(data[0])


def co2_rating(data):
    column_count = data.shape[1]
    for column_i in range(column_count):
        b = flip(most_common_bit(data[:, column_i], fallback=1))
        data = data[data[:, column_i] == b]
        if data.shape[0] == 1:
            return to_decimal(data[0])


def run1(data):
    data = [[int(n) for n in list(x)] for x in data]
    list_of_columns = list(zip(*data))
    gamma_rate = [most_common_bit(x) for x in list_of_columns]
    epsilon_rate = [flip(bit) for bit in gamma_rate]
    return to_decimal(gamma_rate) * to_decimal(epsilon_rate)


def run2(data):
    data = np.array([[int(n) for n in list(x)] for x in data])
    return co2_rating(data) * oxygen_rating(data)


if __name__ == '__main__':
    data = read_lines('inputs/day03.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
