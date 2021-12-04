from utils import read_lines
import numpy as np


def split_given_size(a, size):
    return np.split(a, np.arange(size, len(a), size))


def is_winner(field, numbers_drawn):
    for row in field:
        if len(set(row.tolist()).difference(set(numbers_drawn))) == 0:
            return True

    for row in field.T:
        if len(set(row.tolist()).difference(set(numbers_drawn))) == 0:
            return True

    return False


def run1(data):
    ns = ([int(x) for x in data[0].split(',')])

    data = [x.split() for x in data[2:] if x != '']
    data = np.array(split_given_size(data, 5), dtype=int)

    for i in range(len(ns)):
        numbers_drawn = ns[:i+1]
        last_drawn_number = ns[i]
        for field in data:
            if is_winner(field, numbers_drawn):
                return last_drawn_number * sum([x for x in field.flatten() if x not in numbers_drawn])


def run2(data):
    ns = ([int(x) for x in data[0].split(',')])

    data = [x.split() for x in data[2:] if x != '']
    data = np.array(split_given_size(data, 5), dtype=int)

    for i in range(len(ns)):
        numbers_drawn = ns[:i+1]
        last_drawn_number = ns[i]

        if len(data) == 1 and is_winner(data[0], numbers_drawn):
            return last_drawn_number * sum([x for x in data[0].flatten() if x not in numbers_drawn])

        data = np.array(
            [field for field in data if is_winner(field, numbers_drawn) is False])


if __name__ == '__main__':
    data = read_lines('inputs/day04.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
