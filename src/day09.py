from utils import read_lines
import numpy as np


def all_local_minima(arr):
    iterator = np.nditer(arr, flags=['multi_index'])

    result = []
    for value in iterator:
        x = iterator.multi_index[0]
        y = iterator.multi_index[1]

        if all(value < arr[otherpoint[0]][otherpoint[1]] for otherpoint in neighbors_points(arr, (x, y))):
            result.append((x, y))

    return result


def neighbors_points(arr, point, compare_values=lambda a, b: True):
    max_x = arr.shape[0] - 1
    max_y = arr.shape[1] - 1
    x = point[0]
    y = point[1]

    value = arr[x][y]
    neighbors = []
    # up
    if x > 0 and compare_values(value, arr[x-1][y]):
        neighbors.append((x-1, y))
    # down
    if x < max_x and compare_values(value, arr[x+1][y]):
        neighbors.append((x+1, y))
    # left
    if y > 0 and compare_values(value, arr[x][y-1]):
        neighbors.append((x, y-1))
    # right
    if y < max_y and compare_values(value, arr[x][y+1]):
        neighbors.append((x, y+1))

    return neighbors


def basin_from_point(arr, point):
    scanned = set()
    todo = set([point])

    while len(todo) > 0:
        point_to_scan = todo.pop()
        new_points = [point for point in neighbors_points(
            arr, point_to_scan, compare_values=lambda a, b: a < b and b != 9) if point not in scanned]

        scanned.add(point_to_scan)

        for point in new_points:
            todo.add(point)
    return scanned


def run1(data):
    lines = [[int(n) for n in list(line)] for line in data]
    arr = np.array(lines)
    minimas = all_local_minima(arr)

    return sum(1+arr[point[0]][point[1]] for point in minimas)


def run2(data):
    lines = [[int(n) for n in list(line)] for line in data]
    arr = np.array(lines)
    minimas = all_local_minima(arr)
    basin_sizes = [len(basin_from_point(arr, point)) for point in minimas]
    return np.product(sorted(basin_sizes, reverse=True)[:3])


if __name__ == '__main__':
    data = read_lines('inputs/day09.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
