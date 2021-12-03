from utils import read_lines
from day03 import run1, run2
import pytest

def test_part1_example():
    data = read_lines('inputs/day03-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 198


def test_part1_full():
    data = read_lines('inputs/day03.txt', cast_as=str)
    result = run1(data)
    assert result == 4174964

def test_part2_example():
    data = read_lines('inputs/day03-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 230

def test_part2_full():
    data = read_lines('inputs/day03.txt', cast_as=str)
    result = run2(data)
    assert result == 4474944

if __name__ == '__main__':
    pytest.main(args=['-s'])
