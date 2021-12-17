from utils import read_lines
from day17 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day17-test01.txt')
    result = run1(data[0])
    assert result == 45


def test_part1_full():
    data = read_lines('inputs/day17.txt')
    result = run1(data[0])
    assert result == 4278


def test_part2_example():
    data = read_lines('inputs/day17-test01.txt')
    result = run2(data[0])
    assert result == 112


def test_part2_full():
    data = read_lines('inputs/day17.txt')
    result = run2(data[0])
    assert result == 1994


if __name__ == '__main__':
    pytest.main(args=['-s'])
