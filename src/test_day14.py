from utils import read_segments
from day14 import run1, run2
import pytest


def test_part1_example():
    data = read_segments('inputs/day14-test01.txt')
    result = run1(data)
    assert result == 1588


def test_part1_full():
    data = read_segments('inputs/day14.txt')
    result = run1(data)
    assert result == 2435


def test_part2_example():
    data = read_segments('inputs/day14-test01.txt')
    result = run2(data)
    assert result == 2188189693529


def test_part2_full():
    data = read_segments('inputs/day14.txt')
    result = run2(data)
    assert result == 2587447599164


if __name__ == '__main__':
    pytest.main(args=['-s'])
