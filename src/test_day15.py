from utils import read_lines
from day15 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day15-test01.txt')
    result = run1(data)
    assert result == 40


def test_part1_full():
    data = read_lines('inputs/day15.txt')
    result = run1(data)
    assert result == 769


def test_part2_example():
    data = read_lines('inputs/day15-test01.txt')
    result = run2(data)
    assert result == 315


def test_part2_full():
    data = read_lines('inputs/day15.txt')
    result = run2(data)
    assert result == 2963


if __name__ == '__main__':
    pytest.main(args=['-s'])
