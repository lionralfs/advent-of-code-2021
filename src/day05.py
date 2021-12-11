from utils import read_lines
import numpy as np


def to_line(fn_string):
    return [tuple([int(n) for n in x.split(',')])
            for x in fn_string.split(' -> ')]


def is_straight(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def points_in_line(line):
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]

    x_step = 1
    y_step = 1

    if x1 > x2:
        x_step = -1
    if y1 > y2:
        y_step = -1

    xs = np.arange(start=x1, stop=x2+x_step, step=x_step)
    ys = np.arange(start=y1, stop=y2+y_step, step=y_step)

    is_horizontal = y1 == y2
    if is_horizontal:
        return [(x, y1) for x in xs]

    is_vertical = x1 == x2
    if is_vertical:
        return [(x1, y) for y in ys]

    return list(zip(xs, ys))


def plot(field, line):
    for point in points_in_line(line):
        field[point[0], point[1]] += 1
    return field


def make_field(lines):
    max_x = np.array([[x[0][0], x[1][0]] for x in lines]).flatten().max()
    max_y = np.array([[x[0][1], x[1][1]] for x in lines]).flatten().max()
    return np.zeros((max_x+1, max_y+1), dtype=int)


def run1(data):
    lines = [to_line(x) for x in data]
    field = make_field(lines)

    for line in lines:
        if is_straight(line):
            field = plot(field, line)

    return np.count_nonzero(field >= 2)


def run2(data):
    lines = [to_line(x) for x in data]
    field = make_field(lines)

    for line in lines:
        field = plot(field, line)

    return np.count_nonzero(field >= 2)


if __name__ == '__main__':
    data = read_lines('inputs/day05.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
