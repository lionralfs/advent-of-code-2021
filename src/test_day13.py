from utils import read_lines
from day13 import run1, run2
import pytest


def test_part1_example1():
    data = read_lines('inputs/day13-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 17


def test_part1_full():
    data = read_lines('inputs/day13.txt', cast_as=str)
    result = run1(data)
    assert result == 684


def test_part2_example1():
    data = read_lines('inputs/day13-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 16


def test_part2_full():
    data = read_lines('inputs/day13.txt', cast_as=str)
    result = run2(data)
    assert result == 98


if __name__ == '__main__':
    pytest.main(args=['-s'])
