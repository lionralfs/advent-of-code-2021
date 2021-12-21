from utils import read_segments
from collections import namedtuple
from itertools import combinations, product
from dataclasses import dataclass

Point = namedtuple('Point', ['x', 'y', 'z'])


@dataclass
class Scanner():
    name: str
    points: set[Point]
    position = Point(0, 0, 0)


def to_point(point_raw: str) -> Point:
    parts = [int(n) for n in point_raw.split(',')]
    assert len(parts) > 1
    return Point(parts[0], parts[1], parts[2] if len(parts) > 2 else 0)


def parse_scanner(scanner_raw) -> Scanner:
    lines = scanner_raw.split('\n')
    name = lines[0].replace('---', '').strip()
    points = [to_point(point_raw) for point_raw in lines[1:]]
    return Scanner(name, set(points))


def make_orientations():
    a = 0
    b = 1
    c = 2
    facing = [
        (-1, -1, -1),
        (-1, -1, 1),
        (-1, 1, -1),
        (-1, 1, 1),
        (1, -1, -1),
        (1, -1, 1),
        (1, 1, -1),
        (1, 1, 1),
    ]
    dims = [(a, b, c), (a, c, b), (b, c, a), (b, a, c), (c, a, b), (c, b, a)]
    return product(facing, dims)


ORIENTATIONS = list(make_orientations())


def apply_orientation(point: Point, orientation):
    coords = point.x, point.y, point.z
    facing = orientation[0]
    order = orientation[1]
    return Point(
        coords[order[0]] * facing[0],
        coords[order[1]] * facing[1],
        coords[order[2]] * facing[2]
    )


def compare_scanners(A: Scanner, B: Scanner):
    for A_point in A.points:
        others_A = [point for point in A.points if point != A_point]
        # try all orientations for scanner B
        for o in ORIENTATIONS:
            B_points_oriented = set([apply_orientation(
                point, o) for point in B.points])

            for B_point in B_points_oriented:

                dx = A_point.x - B_point.x
                dy = A_point.y - B_point.y
                dz = A_point.z - B_point.z

                matches = 1

                for other_A in others_A:
                    new = Point(other_A.x-dx, other_A.y-dy, other_A.z-dz)
                    if new in B_points_oriented:
                        matches += 1
                if matches >= 12:
                    return o, (dx, dy, dz)
    return None


def add(point: Point, offset: tuple[int, int, int]) -> Point:
    return Point(point.x+offset[0], point.y+offset[1], point.z+offset[2])


def manhattan(A: Point, B: Point) -> int:
    dx = abs(A.x - B.x)
    dy = abs(A.y - B.y)
    dz = abs(A.z - B.z)
    return dx+dy+dz


def run1(scanners_raw):
    scanners = [parse_scanner(segment) for segment in scanners_raw]
    all = solve(scanners)
    return len(all.points)


def run2(scanners_raw):
    scanners = [parse_scanner(segment) for segment in scanners_raw]

    solve(scanners)

    return max([manhattan(A.position, B.position)
                for A, B in combinations(scanners, 2)])


def solve(scanners: list[Scanner]):
    combined_scanner = scanners[0]
    yet_to_reach = list(range(1, len(scanners)))
    recently_discovered = [scanners[0]]
    while len(yet_to_reach) > 0:
        last = recently_discovered[-1]
        match = matching_scanner(last, scanners, yet_to_reach)
        if match is None:
            recently_discovered.pop()
        else:
            other_scanner_updated, index = match
            yet_to_reach.remove(index)
            recently_discovered.append(other_scanner_updated)
            for point in other_scanner_updated.points:
                combined_scanner.points.add(point)

    return combined_scanner


def matching_scanner(
        scanner: Scanner,
        scanners: list[Scanner],
        todo: list[int]):

    for i in todo:
        other_scanner = scanners[i]
        overlap = compare_scanners(scanner, other_scanner)
        if overlap is None:
            continue

        orientation, translation = overlap

        aligned_points = set([
            add(apply_orientation(point, orientation), translation)
            for point in other_scanner.points
        ])

        other_scanner.points = aligned_points
        other_scanner.position = Point(
            translation[0],
            translation[1],
            translation[2],
        )

        return other_scanner, i
    return None


if __name__ == '__main__':
    input = read_segments('inputs/day19.txt')
    print('[Part1]:', run1(input))
    print('[Part2]:', run2(input))
