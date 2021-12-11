from utils import read_lines
from day06 import run1, run2
import pytest

if __name__ == '__main__':
    pytest.main(args=['-s'])


def test_part1_example():
    data = read_lines('inputs/day06-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 5934


def test_part1_full():
    data = read_lines('inputs/day06.txt', cast_as=str)
    result = run1(data)
    assert result == 391671


def test_part2_example():
    data = read_lines('inputs/day06-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 26984457539


def test_part2_full():
    data = read_lines('inputs/day06.txt', cast_as=str)
    result = run2(data)
    assert result == 1754000560399
