from utils import read_segments
from collections import Counter, namedtuple
from itertools import combinations

Point = namedtuple('Point', ['x', 'y', 'z'])


def manhattan(a: Point, b: Point) -> int:
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    dz = abs(a.z - b.z)

    return dx+dy+dz


class Scanner():
    def __init__(self, name: str, points: list[Point]):
        self.name = name
        self.points = points
        self.distances = {}
        self.distances_counter = Counter()
        for i, point in enumerate(self.points):
            for j in range(i+1, len(self.points)):
                other_point = self.points[j]
                distance = manhattan(point, other_point)
                self.distances_counter[distance] += 1
                self.distances[(i, j)] = distance
                self.distances[(j, i)] = distance

    def all_indices(self):
        return range(len(self.points))

    def has_distance(self, distance):
        return distance in self.distances.values()

    def distances_within_points(self, point_indices):
        result = []
        for i in range(len(point_indices)):
            point_index = point_indices[i]
            for j in range(i+1, len(point_indices)):
                other_point_index = point_indices[j]
                result.append(self.distances[(point_index, other_point_index)])
        return result


def to_point(point_raw: str) -> Point:
    parts = [int(n) for n in point_raw.split(',')]
    assert len(parts) > 1
    return Point(parts[0], parts[1], parts[2] if len(parts) > 2 else 0)


def parse_scanner(scanner_raw) -> Scanner:
    lines = scanner_raw.split('\n')
    name = lines[0].replace('---', '').strip()
    points = [to_point(point_raw) for point_raw in lines[1:]]
    return Scanner(name, points)


def same_distances(a_distances, b_distances):
    if len(a_distances) != len(b_distances):
        return False
    return sorted(a_distances) == sorted(b_distances)


def overlapping_points(A: Scanner, B: Scanner) -> bool:

    return False


def run1(scanners_raw):
    scanners = [parse_scanner(segment) for segment in scanners_raw]

    A = scanners[0]
    B = scanners[1]

    overlap_threshold = 12
    edges_count = int((overlap_threshold * (overlap_threshold - 1)) / 2)

    A_points = A.all_indices()
    B_points = B.all_indices()

    first, second = A_points[0], A_points[1]
    mask = set([first, second])
    possible_pairs_B = [pair for pair in combinations(
        B_points, 2) if B.distances[pair] == A.distances[(first, second)]]

    possible_points_B = set()
    for pair in possible_pairs_B:
        possible_points_B.add(pair[0])
        possible_points_B.add(pair[1])

    print(possible_points_B)
    for other in A_points:
        if other in mask:
            continue
        potential_new_mask = list(mask) + [other]
        distances = [A.distances[pair]
                     for pair in combinations(potential_new_mask, 2)]
        for bpoint in B_points:
            if bpoint in possible_points_B:
                continue
            print(set(list(possible_points_B) + [bpoint]))


if __name__ == '__main__':
    input = read_segments('inputs/day19-test02.txt')
    print('[Part1]:', run1(input))
    # print('[Part2]:', run2(input))
