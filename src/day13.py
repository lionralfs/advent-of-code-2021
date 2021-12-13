from utils import read_lines
import numpy as np


def run1(data):
    points = set()
    instructions = []
    for line in data:
        if line == '':
            continue
        if line.startswith('fold'):
            instructions.append(line.replace('fold along ', '').split('='))
        else:
            points.add(tuple(int(n) for n in line.split(',')))

    for fold_instruction in instructions[:1]:
        newpoints = set()
        foldpoint = int(fold_instruction[1])

        for point in points:
            if fold_instruction[0] == 'y':
                if point[1] < foldpoint:
                    newpoints.add(point)
                if point[1] > foldpoint:
                    distance_from_foldpoint = abs(point[1] - foldpoint)
                    new_y = point[1] - 2*distance_from_foldpoint
                    newpoints.add((point[0], new_y))
            else:
                if point[0] < foldpoint:
                    newpoints.add(point)
                if point[0] > foldpoint:
                    distance_from_foldpoint = abs(point[0] - foldpoint)
                    new_x = point[0] - 2*distance_from_foldpoint
                    newpoints.add((new_x, point[1]))

        points = newpoints

    return len(points)


def run2(data):
    points = set()
    instructions = []
    for line in data:
        if line == '':
            continue
        if line.startswith('fold'):
            instructions.append(line.replace('fold along ', '').split('='))
        else:
            points.add(tuple(int(n) for n in line.split(',')))

    for fold_instruction in instructions:
        newpoints = set()
        foldpoint = int(fold_instruction[1])

        for point in points:
            if fold_instruction[0] == 'y':
                if point[1] < foldpoint:
                    newpoints.add(point)
                if point[1] > foldpoint:
                    distance_from_foldpoint = abs(point[1] - foldpoint)
                    new_y = point[1] - 2*distance_from_foldpoint
                    newpoints.add((point[0], new_y))
            else:
                if point[0] < foldpoint:
                    newpoints.add(point)
                if point[0] > foldpoint:
                    distance_from_foldpoint = abs(point[0] - foldpoint)
                    new_x = point[0] - 2*distance_from_foldpoint
                    newpoints.add((new_x, point[1]))

        points = newpoints

    max_x = max([point[0] for point in points])
    max_y = max([point[1] for point in points])

    print('')
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print('')
    print('')

    return len(points)


if __name__ == '__main__':
    data = read_lines('inputs/day13.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
