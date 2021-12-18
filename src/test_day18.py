import pytest
from day18 import *
from utils import read_lines


def test_parse1():
    root = parse('[[1,2],3]')
    assert root.data == 0
    assert root.depth == 0
    assert root.right.data == 3
    assert root.left.depth == 1
    assert root.right.depth == 1
    assert root.left.left.data == 1
    assert root.left.right.data == 2


def test_explode1():
    root = parse('[[[[[9,8],1],2],3],4]')
    deep_nodes = find_deep_nodes(root)
    assert len(deep_nodes) == 1
    explode(deep_nodes[0])
    assert root.right.data == 4
    assert root.left.right.data == 3
    assert root.left.left.right.data == 2
    assert root.left.left.left.right.data == 9
    assert root.left.left.left.left.data == 0


def test_explode2():
    root = parse('[[6,[5,[4,[3,2]]]],1]')
    deep_nodes = find_deep_nodes(root)
    assert len(deep_nodes) == 1
    assert len(deep_nodes) == 1
    explode(deep_nodes[0])
    assert root.right.data == 3
    assert root.left.left.data == 6
    assert root.left.right.left.data == 5
    assert root.left.right.right.left.data == 7
    assert root.left.right.right.right.data == 0
    assert root.left.right.right.right.left is None
    assert root.left.right.right.right.right is None


def test_sum1():
    lines = [
        '[1,1]',
        '[2,2]',
        '[3,3]',
        '[4,4]',
    ]
    result = lines_sum(lines)
    assert to_string(result) == '[[[[1,1],[2,2]],[3,3]],[4,4]]'


def test_sum2():
    lines = [
        '[1,1]',
        '[2,2]',
        '[3,3]',
        '[4,4]',
        '[5,5]',
    ]
    result = lines_sum(lines)
    assert to_string(result) == '[[[[3,0],[5,3]],[4,4]],[5,5]]'


def test_sum3():
    lines = [
        '[1,1]',
        '[2,2]',
        '[3,3]',
        '[4,4]',
        '[5,5]',
        '[6,6]',
    ]
    result = lines_sum(lines)
    assert to_string(result) == '[[[[5,0],[7,4]],[5,5]],[6,6]]'


def test_sum4():
    lines = [
        '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
        '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
    ]
    result = lines_sum(lines)
    assert to_string(
        result) == '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'


def test_sum5():
    lines = [
        '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]',
        '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
    ]
    result = lines_sum(lines)
    assert to_string(result) == '[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]'  # noqa


def test_part1_example():
    input = read_lines('inputs/day18-test01.txt')
    result = run1(input)
    assert result == 4140


def test_part1_full():
    input = read_lines('inputs/day18.txt')
    result = run1(input)
    assert result == 3494


def test_part2_example():
    input = read_lines('inputs/day18-test01.txt')
    result = run2(input)
    assert result == 3993


# takes too long

# def test_part2_full():
#     input = read_lines('inputs/day18.txt')
#     result = run2(input)
#     assert result == 4712


if __name__ == '__main__':
    pytest.main(args=['-s'])
