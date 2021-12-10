from utils import read_lines
from day10 import first_illegal_character, run1, run2, stack_remainder, stack_score
import pytest

if __name__ == '__main__':
    pytest.main(args=['-s'])


def test_part1_example():
    data = read_lines('inputs/day10-test01.txt', cast_as=str)
    result = run1(data)
    assert result == 26397


def test_part1_full():
    data = read_lines('inputs/day10.txt', cast_as=str)
    result = run1(data)
    assert result == 299793


def test_part2_example():
    data = read_lines('inputs/day10-test01.txt', cast_as=str)
    result = run2(data)
    assert result == 288957


def test_part2_full():
    data = read_lines('inputs/day10.txt', cast_as=str)
    result = run2(data)
    assert result == 3654963618


def test_stack_score():
    stack = list('])}>')
    result = stack_score(stack)
    assert result == 294


def test_stack_remainer():
    input = list('{(')
    result = stack_remainder(input)
    assert len(result) == 2
