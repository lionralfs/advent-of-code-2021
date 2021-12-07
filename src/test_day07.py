from utils import read_lines
from day07 import run1, run2
import pytest

if __name__ == '__main__':
    pytest.main(args=['-s'])

def test_part1_example():
    data = read_lines('inputs/day07-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 37


def test_part1_full():
    data = read_lines('inputs/day07.txt', cast_as=str)
    result = run1(data)
    assert result == 333755


def test_part2_example():
    data = read_lines('inputs/day07-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 168


def test_part2_full():
    data = read_lines('inputs/day07.txt', cast_as=str)
    result = run2(data)
    assert result == 94017638

