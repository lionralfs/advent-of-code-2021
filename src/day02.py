from os import read
from utils import read_lines


def prep_data(data):
    return [[x.split(' ')[0], int(x.split(' ')[1])] for x in data]


def run1(data):
    data = prep_data(data)
    coords = (0, 0)
    switcher = {
        'down': lambda x: (coords[0], coords[1]+x),
        'up': lambda x: (coords[0], coords[1]-x),
        'forward': lambda x: (coords[0]+x, coords[1])
    }

    for move in data:
        coords = switcher[move[0]](move[1])

    return coords[0] * coords[1]


def run2(data):
    data = prep_data(data)
    coords = (0, 0, 0)
    switcher = {
        'down': lambda x: (coords[0], coords[1], coords[2]+x),
        'up': lambda x: (coords[0], coords[1], coords[2]-x),
        'forward': lambda x: (coords[0]+x, coords[1]+(coords[2]*x), coords[2]),
    }

    for move in data:
        coords = switcher[move[0]](move[1])

    return coords[0] * coords[1]


if __name__ == '__main__':
    data = read_lines('inputs/day02.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
