from utils import read_lines
from day09 import run1, run2
import pytest

if __name__ == '__main__':
    pytest.main(args=['-s'])


def test_part1_example():
    data = read_lines('inputs/day09-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 15


def test_part1_full():
    data = read_lines('inputs/day09.txt', cast_as=str)
    result = run1(data)
    assert result == 548


def test_part2_example():
    data = read_lines('inputs/day09-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 1134


def test_part2_full():
    data = read_lines('inputs/day09.txt', cast_as=str)
    result = run2(data)
    assert result == 786048
