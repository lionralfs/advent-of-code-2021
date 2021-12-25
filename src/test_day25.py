from utils import read_lines
from day25 import run1
import pytest


def test_part1_example():
    data = read_lines('inputs/day25-test01.txt')
    result = run1(data)
    assert result == 58


def test_part1_full():
    data = read_lines('inputs/day25.txt')
    result = run1(data)
    assert result == 568


if __name__ == '__main__':
    pytest.main(args=['-s'])
