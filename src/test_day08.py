from utils import read_lines
from day08 import run1, run2
import pytest

if __name__ == '__main__':
    pytest.main(args=['-s'])


def test_part1_example1():
    data = read_lines('inputs/day08-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 0


def test_part1_example2():
    data = read_lines('inputs/day08-test02.txt', cast_as=str)
    result = run1(data)
    assert result == 26


def test_part1_full():
    data = read_lines('inputs/day08.txt', cast_as=str)
    result = run1(data)
    assert result == 440


def test_part2_example1():
    data = read_lines('inputs/day08-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 5353


def test_part2_example2():
    data = read_lines('inputs/day08-test02.txt', cast_as=str)
    result = run2(data)
    assert result == 61229


def test_part2_full():
    data = read_lines('inputs/day08.txt', cast_as=str)
    result = run2(data)
    assert result == 1046281
