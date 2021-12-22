from utils import read_lines
from day22 import run1, run2
import pytest


def test_part1_example1():
    data = read_lines('inputs/day22-test01.txt')
    result = run1(data)
    assert result == 39


def test_part1_example2():
    data = read_lines('inputs/day22-test02.txt')
    result = run1(data)
    assert result == 590784


def test_part1_example3():
    data = read_lines('inputs/day22-test03.txt')
    result = run1(data)
    assert result == 474140


def test_part1_full():
    data = read_lines('inputs/day22.txt')
    result = run1(data)
    assert result == 580098


def test_part2_example1():
    data = read_lines('inputs/day22-test03.txt')
    result = run2(data)
    assert result == 2758514936282235


def test_part2_full():
    data = read_lines('inputs/day22.txt')
    result = run2(data)
    assert result == 1134725012490723


if __name__ == '__main__':
    pytest.main(args=['-s'])
