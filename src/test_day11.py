from utils import read_lines
from day11 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day11-test02.txt', cast_as=str)
    result = run1(data)
    assert result == 1656


def test_part1_full():
    data = read_lines('inputs/day11.txt', cast_as=str)
    result = run1(data)
    assert result == 1632


def test_part2_example():
    data = read_lines('inputs/day11-test02.txt', cast_as=str)
    result = run2(data)
    assert result == 195


def test_part2_full():
    data = read_lines('inputs/day11.txt', cast_as=str)
    result = run2(data)
    assert result == 303


if __name__ == '__main__':
    pytest.main(args=['-s'])
