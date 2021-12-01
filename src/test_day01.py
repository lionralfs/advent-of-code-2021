import hypothesis
import pytest
from hypothesis import given, strategies as st
from utils import read_lines
from day01 import run1, run2


def test_part1_example():
    data = read_lines('inputs/day01-test01.txt', cast_as=int)
    result = run1(data)
    assert result == 7


def test_part1_full():
    data = read_lines('inputs/day01.txt', cast_as=int)
    result = run1(data)
    assert result == 1154


def test_part2_example():
    data = read_lines('inputs/day01-test01.txt', cast_as=int)
    result = run2(data)
    assert result == 5


def test_part2_full():
    data = read_lines('inputs/day01.txt', cast_as=int)
    result = run2(data)
    assert result == 1127


@given(st.lists(st.integers(min_value=0), min_size=1, unique=True).map(lambda list: sorted(list, reverse=False)))
def test_part1_sorted_asc(a_list):
    result = run1(a_list)
    assert result == len(a_list) - 1


@given(st.lists(st.integers(min_value=0), min_size=1, unique=True).map(lambda list: sorted(list, reverse=True)))
def test_part1_sorted_desc(a_list):
    result = run1(a_list)
    assert result == 0


@given(st.lists(st.integers(min_value=0), min_size=1, unique=True).map(lambda list: sorted(list, reverse=True)))
def test_part2_sorted_desc(a_list):
    result = run2(a_list)
    assert result == 0


if __name__ == '__main__':
    pytest.main(args=['-s'])
