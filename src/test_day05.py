from utils import read_lines
from day05 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day05-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 5


def test_part1_full():
    data = read_lines('inputs/day05.txt', cast_as=str)
    result = run1(data)
    assert result == 7085


def test_part2_example():
    data = read_lines('inputs/day05-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 12


def test_part2_full():
    data = read_lines('inputs/day05.txt', cast_as=str)
    result = run2(data)
    assert result == 20271


if __name__ == '__main__':
    pytest.main(args=['-s'])
