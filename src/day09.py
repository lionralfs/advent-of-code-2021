from utils import read_lines
import numpy as np


def all_local_minima(arr):
    max_x = arr.shape[0] - 1
    max_y = arr.shape[1] - 1
    iterator = np.nditer(arr, flags=['multi_index'])

    result = []
    for value in iterator:
        up = 10
        down = 10
        left = 10
        right = 10

        x = iterator.multi_index[0]
        y = iterator.multi_index[1]

        if x > 0:
            up = arr[x-1][y]
        if x < max_x:
            down = arr[x+1][y]
        if y > 0:
            left = arr[x][y-1]
        if y < max_y:
            right = arr[x][y+1]

        if all(value < other for other in [up, down, left, right]):
            result.append((x, y))

    return result


def run1(data):
    lines = [[int(n) for n in list(line)] for line in data]
    arr = np.array(lines)
    minimas = all_local_minima(arr)

    return sum(1+arr[point[0]][point[1]] for point in minimas)


def run2(data):
    return 0


if __name__ == '__main__':
    data = read_lines('inputs/day09-test01.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
