from utils import read_lines
from day02 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day02-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 150


def test_part1_full():
    data = read_lines('inputs/day02.txt', cast_as=str)
    result = run1(data)
    assert result == 1924923


def test_part2_example():
    data = read_lines('inputs/day02-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 900


def test_part2_full():
    data = read_lines('inputs/day02.txt', cast_as=str)
    result = run2(data)
    assert result == 1982495697


if __name__ == '__main__':
    pytest.main(args=['-s'])
