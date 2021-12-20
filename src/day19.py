from utils import read_segments
from collections import namedtuple
from dataclasses import dataclass

Point = namedtuple('Point', ['x', 'y', 'z'])


@dataclass
class Scanner():
    name: str
    points: list[Point]


def to_point(point_raw: str) -> Point:
    parts = [int(n) for n in point_raw.split(',')]
    assert len(parts) > 1
    return Point(parts[0], parts[1], parts[2] if len(parts) > 2 else 0)


def parse_scanner(scanner_raw) -> Scanner:
    lines = scanner_raw.split('\n')
    name = lines[0].replace('---', '').strip()
    points = [to_point(point_raw) for point_raw in lines[1:]]
    return Scanner(name, points)


def run1(scanners_raw):
    scanners = [parse_scanner(segment) for segment in scanners_raw]
    print(scanners[0])


if __name__ == '__main__':
    input = read_segments('inputs/day19-test02.txt')
    print('[Part1]:', run1(input))
    # print('[Part2]:', run2(input))
