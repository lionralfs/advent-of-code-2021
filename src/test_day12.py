from utils import read_lines
from day12 import run1, run2
import pytest


def test_part1_example1():
    data = read_lines('inputs/day12-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 10


def test_part1_example2():
    data = read_lines('inputs/day12-test02.txt', cast_as=str)
    result = run1(data)
    assert result == 19


def test_part1_example3():
    data = read_lines('inputs/day12-test03.txt', cast_as=str)
    result = run1(data)
    assert result == 226


def test_part1_full():
    data = read_lines('inputs/day12.txt', cast_as=str)
    result = run1(data)
    assert result == 4773


def test_part2_example1():
    data = read_lines('inputs/day12-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 36


def test_part2_example2():
    data = read_lines('inputs/day12-test02.txt', cast_as=str)
    result = run2(data)
    assert result == 103


def test_part2_example3():
    data = read_lines('inputs/day12-test03.txt', cast_as=str)
    result = run2(data)
    assert result == 3509


def test_part2_full():
    data = read_lines('inputs/day12.txt', cast_as=str)
    result = run2(data)
    assert result == 116985


if __name__ == '__main__':
    pytest.main(args=['-s'])
