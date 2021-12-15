import math
from utils import read_lines
from queue import PriorityQueue
from collections import namedtuple
import numpy as np

Point = namedtuple('Point', ['x', 'y'])


def neighbors(field, point):
    max_x = field.shape[1] - 1
    max_y = field.shape[0] - 1

    neighbors = []
    # up
    if point.y > 0:
        neighbors.append(Point(point.x, point.y-1))
    # down
    if point.y < max_y:
        neighbors.append(Point(point.x, point.y+1))
    # left
    if point.x > 0:
        neighbors.append(Point(point.x-1, point.y))
    # right
    if point.x < max_x:
        neighbors.append(Point(point.x+1, point.y))

    return neighbors


def manhattan_distance(a, b):
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)

    return dx+dy


def AStar(field, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, [start]))

    scanned = set(start)

    while not frontier.empty():
        value, path = frontier.get()
        last = path[-1]

        if last == goal:
            return path

        for neighbor in neighbors(field, last):
            if neighbor not in scanned:
                scanned.add(neighbor)
                newpath = path.copy()
                newpath.append(neighbor)
                pathweight = sum([field[point.y][point.x]
                                  for point in newpath[1:]])
                d = manhattan_distance(neighbor, goal)
                frontier.put((d+pathweight, newpath))


def run1(data):
    field = np.array([[int(n) for n in line] for line in data])

    start = Point(0, 0)
    end = Point(field.shape[1] - 1, field.shape[0] - 1)

    path = AStar(field, start, end)
    return sum([field[point.y][point.x] for point in path[1:]])


def run2(data):
    field = np.array([[int(n) for n in line] for line in data])
    firstrow = np.array(field, copy=True)

    # first col
    for i in range(4):
        newfield = np.array(field, copy=True)
        newfield = newfield + i + 1
        overflow = newfield > 9
        newfield[overflow] = (newfield[overflow] % 10) + 1
        firstrow = np.concatenate((firstrow, newfield), axis=1)

    biggerfield = np.array(firstrow, copy=True)
    # rows
    for i in range(4):
        newfield = np.array(firstrow, copy=True)
        newfield = newfield + i + 1
        overflow = newfield > 9
        newfield[overflow] = (newfield[overflow] % 10) + 1
        biggerfield = np.concatenate((biggerfield, newfield), axis=0)

    start = Point(0, 0)
    end = Point(biggerfield.shape[1] - 1, biggerfield.shape[0] - 1)
    path = AStar(biggerfield, start, end)
    return sum([biggerfield[point.y][point.x] for point in path[1:]])


if __name__ == '__main__':
    data = read_lines('inputs/day15.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
