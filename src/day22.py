from utils import read_lines
from dataclasses import dataclass


@dataclass
class Cuboid:
    on: bool
    xstart: int
    xend: int
    ystart: int
    yend: int
    zstart: int
    zend: int

    def has_volume(self):
        return self.xstart <= self.xend and \
            self.ystart <= self.yend and \
            self.zstart <= self.zend

    def volume(self):
        dx = self.xend - self.xstart
        dy = self.yend - self.ystart
        dz = self.zend - self.zstart

        return (dx+1) * (dy+1) * (dz+1)


def parse(line):
    parts = line.split(' ')
    coords = parts[1].split(',')
    x = [int(n) for n in coords[0][2:].split('..')]
    y = [int(n) for n in coords[1][2:].split('..')]
    z = [int(n) for n in coords[2][2:].split('..')]

    on = True if parts[0] == 'on' else False

    return Cuboid(on, x[0], x[1], y[0], y[1], z[0], z[1])


def split(A: Cuboid, B: Cuboid):
    assert B.on is True
    result = []
    # above
    above = Cuboid(True,
                   B.xstart, B.xend,
                   A.yend+1, B.yend,
                   B.zstart, B.zend)
    if above.has_volume():
        result.append(above)

    # below
    below = Cuboid(True,
                   B.xstart, B.xend,
                   B.ystart, A.ystart-1,
                   B.zstart, B.zend)
    if below.has_volume():
        result.append(below)

    Y_START = max(B.ystart, A.ystart)
    Y_END = min(B.yend, A.yend)

    # back-left
    back_left = Cuboid(True,
                       B.xstart, A.xstart-1,
                       Y_START, Y_END,
                       A.zend+1, B.zend)
    if back_left.has_volume():
        result.append(back_left)

    # back-right
    back_right = Cuboid(True,
                        A.xend+1, B.xend,
                        Y_START, Y_END,
                        A.zend+1, B.zend)
    if back_right.has_volume():
        result.append(back_right)

    # front-right
    front_right = Cuboid(True,
                         A.xend+1, B.xend,
                         Y_START, Y_END,
                         B.zstart, A.zstart-1)
    if front_right.has_volume():
        result.append(front_right)

    # front-left
    front_left = Cuboid(True,
                        B.xstart, A.xstart-1,
                        Y_START, Y_END,
                        B.zstart, A.zstart-1)
    if front_left.has_volume():
        result.append(front_left)

    # left
    left = Cuboid(True,
                  B.xstart, A.xstart-1,
                  Y_START, Y_END,
                  max(A.zstart, B.zstart), min(A.zend, B.zend))
    if left.has_volume():
        result.append(left)

    # right
    right = Cuboid(True,
                   A.xend+1, B.xend,
                   Y_START, Y_END,
                   max(A.zstart, B.zstart), min(A.zend, B.zend))
    if right.has_volume():
        result.append(right)

    # front-center
    front_center = Cuboid(True,
                          max(A.xstart, B.xstart), min(A.xend, B.xend),
                          Y_START, Y_END,
                          B.zstart, A.zstart-1)
    if front_center.has_volume():
        result.append(front_center)

    # back-center
    back_center = Cuboid(True,
                         max(A.xstart, B.xstart), min(A.xend, B.xend),
                         Y_START, Y_END,
                         A.zend+1, B.zend)
    if back_center.has_volume():
        result.append(back_center)

    return result


def in_init_zone(cuboid: Cuboid):
    return min(cuboid.xstart, cuboid.ystart, cuboid.zstart) >= -50 and \
        max(cuboid.xend, cuboid.yend, cuboid.zend) <= 50


def run(input_cuboids):

    on: list[Cuboid] = []

    for input_cuboid in input_cuboids:
        new_on = []
        for other in on:
            if overlap(input_cuboid, other):
                for new in split(input_cuboid, other):
                    new_on.append(new)
            else:
                new_on.append(other)

        if input_cuboid.on:
            new_on.append(input_cuboid)

        on = new_on

    return sum([cuboid.volume() for cuboid in on])


def overlap(a: Cuboid, b: Cuboid):
    if a.xstart > b.xend:
        return False
    if a.xend < b.xstart:
        return False
    if a.ystart > b.yend:
        return False
    if a.yend < b.ystart:
        return False
    if a.zstart > b.zend:
        return False
    if a.zend < b.zstart:
        return False
    return True


def run1(input):
    cuboids = [parse(line) for line in input]
    return run([c for c in cuboids if in_init_zone(c)])


def run2(input):
    cuboids = [parse(line) for line in input]
    return run(cuboids)


if __name__ == '__main__':
    input = read_lines('inputs/day22.txt')
    print('[Part1]:', run1(input))
    print('[Part2]:', run2(input))
