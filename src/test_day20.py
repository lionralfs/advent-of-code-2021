from utils import read_segments
from day20 import run1, run2
import pytest


def test_part1_example():
    data = read_segments('inputs/day20-test01.txt')
    result = run1(data)
    assert result == 35


def test_part1_full():
    data = read_segments('inputs/day20.txt')
    result = run1(data)
    assert result == 5229


def test_part2_example():
    data = read_segments('inputs/day20-test01.txt')
    result = run2(data)
    assert result == 3351


def test_part2_full():
    data = read_segments('inputs/day20.txt')
    result = run2(data)
    assert result == 17009


if __name__ == '__main__':
    pytest.main(args=['-s'])
