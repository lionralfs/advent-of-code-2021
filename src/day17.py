from utils import read_lines
from collections import namedtuple

Target = namedtuple('Target', ['xmin', 'xmax', 'ymin', 'ymax'])
Point = namedtuple('Point', ['x', 'y'])


def parse_target(input_raw: str) -> Target:
    data = input_raw.replace('target area: ', '')
    parts = data.split(', ')
    coords = [[int(n) for n in part.split('=')[1].split('..')]
              for part in parts]

    return Target(coords[0][0], coords[0][1], coords[1][0], coords[1][1])


def triangle_numbers(n):
    return int((n*(n+1))/2)


def in_target(point: Point, target: Target):
    return point.x >= target.xmin and \
        point.x <= target.xmax and \
        point.y >= target.ymin and \
        point.y <= target.ymax


def en_route(point: Point, target: Target):
    return point.x <= target.xmax and point.y >= target.ymin


def hits_target(velocity: Point, target: Target) -> tuple[bool, list[Point]]:
    velocity_x = velocity.x
    velocity_y = velocity.y
    point = Point(0, 0)

    passed_points = []

    while en_route(point, target):
        point = Point(point.x + velocity_x, point.y + velocity_y)
        passed_points.append(point)
        if in_target(point, target):
            return True, passed_points
        if velocity_x < 0:
            velocity_x += 1
        if velocity_x > 0:
            velocity_x -= 1
        velocity_y -= 1

    return False, []


def all_hits(target: Target) -> dict[Point, list[Point]]:
    min_x_velocity = min(filter(lambda x: triangle_numbers(x) >=
                                target.xmin,  range(target.xmin)))

    hit_paths = {}
    for x_velocity in range(min_x_velocity, target.xmax+1):
        for y_velocity in range(target.ymin, x_velocity + abs(target.ymin)):
            velocity = Point(x_velocity, y_velocity)
            hits, points = hits_target(velocity, target)
            if hits:
                hit_paths[velocity] = points

    return hit_paths


def run1(input_raw):
    target = parse_target(input_raw)

    hits = all_hits(target)
    return max([max([point.y for point in points])
                for points in hits.values()])


def run2(input_raw):
    target = parse_target(input_raw)

    hits = all_hits(target)
    return len(hits)


if __name__ == '__main__':
    input = read_lines('inputs/day17.txt')
    print('[Part1]:', run1(input[0]))
    print('[Part2]:', run2(input[0]))
