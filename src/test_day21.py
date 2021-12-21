from utils import read_lines
from day21 import run1, run2
import pytest


def test_part1_example():
    data = read_lines('inputs/day21-test01.txt')
    result = run1(data)
    assert result == 739785


def test_part1_full():
    data = read_lines('inputs/day21.txt')
    result = run1(data)
    assert result == 556206


def test_part2_example():
    data = read_lines('inputs/day21-test01.txt')
    result = run2(data)
    assert result == 444356092776315


def test_part2_full():
    data = read_lines('inputs/day21.txt')
    result = run2(data)
    assert result == 630797200227453


if __name__ == '__main__':
    pytest.main(args=['-s'])
