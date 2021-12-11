from utils import read_lines
import numpy as np


def neighbors(point, max_x, max_y):
    x = point[0]
    y = point[1]
    result = []

    # top left
    if x > 0 and y > 0:
        result.append((x-1, y-1))
    # top
    if x > 0:
        result.append((x-1, y))
    # top right
    if x > 0 and y < max_y:
        result.append((x-1, y+1))
    # right
    if y < max_y:
        result.append((x, y+1))
    # bottom right
    if x < max_x and y < max_y:
        result.append((x+1, y+1))
    # bottom
    if x < max_x:
        result.append((x+1, y))
    # bottom left
    if x < max_x and y > 0:
        result.append((x+1, y-1))
    # left
    if y > 0:
        result.append((x, y-1))

    return result


def simulate_step(field):
    max_x = field.shape[0] - 1
    max_y = field.shape[1] - 1

    # step 1: add 1 to each energy level
    field = (field+1) % 10

    flashed = np.where(field == 0)
    # list of points that flashed
    flashed = list(zip(flashed[0], flashed[1]))

    todo = set(flashed)

    flash_count = len(todo)

    while len(todo) > 0:
        point = todo.pop()
        # go through every point that flashed, and increase their neighbors
        for neighbor in neighbors(point, max_x, max_y):
            value = field[neighbor[0]][neighbor[1]]
            if value == 0:
                continue

            if value == 9:
                flash_count += 1
                todo.add(neighbor)

            field[neighbor[0]][neighbor[1]] = (value+1) % 10

    return field, flash_count


def run1(data):
    field = np.array([[int(n) for n in list(line)] for line in data])

    flash_count_sum = 0
    for _ in range(100):
        field, flash_count = simulate_step(field)
        flash_count_sum += flash_count

    return flash_count_sum


def run2(data):
    field = np.array([[int(n) for n in list(line)] for line in data])

    size = field.shape[0] * field.shape[1]

    i = 0
    while True:
        i += 1
        field, flash_count = simulate_step(field)
        if flash_count == size:
            return i


if __name__ == '__main__':
    data = read_lines('inputs/day11.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
