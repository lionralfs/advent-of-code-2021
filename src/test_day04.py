from utils import read_lines
from day04 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day04-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 4512


def test_part1_full():
    data = read_lines('inputs/day04.txt', cast_as=str)
    result = run1(data)
    assert result == 25023


def test_part2_example():
    data = read_lines('inputs/day04-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 1924


def test_part2_full():
    data = read_lines('inputs/day04.txt', cast_as=str)
    result = run2(data)
    assert result == 2634


if __name__ == '__main__':
    pytest.main(args=['-s'])
