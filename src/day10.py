from utils import read_lines
import numpy as np

brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points_part1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points_part2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def first_illegal_character(line):
    result = first_illegal_character_rec(line, [])
    if isinstance(result, list):
        return None
    return result


def stack_remainder(line):
    result = first_illegal_character_rec(line, [])
    if isinstance(result, list):
        return result
    return []


def first_illegal_character_rec(line, stack):
    if len(line) == 0 and len(stack) == 0:
        return None

    if len(line) == 0:
        return stack

    first = line[0]

    # opening bracket
    if first in brackets:
        stack.append(brackets[first])
        return first_illegal_character_rec(line[1:], stack)

    # closing bracket
    first_on_stack = stack.pop()
    if first == first_on_stack:
        return first_illegal_character_rec(line[1:], stack)

    return first


def run1(data):
    lines = [list(line) for line in data]
    illegal_characters = [first_illegal_character(line) for line in lines]
    return sum([points_part1[char] for char in illegal_characters
                if char is not None])


def run2(data):
    lines = [list(line) for line in data]

    scores = list(filter(lambda x: x != 0,
                         [stack_score(reversed(stack_remainder(line)))
                          for line in lines]))

    return int(np.median(scores))


def stack_score(stack):
    score = 0
    for item in stack:
        score *= 5
        score += points_part2[item]
    return score


if __name__ == '__main__':
    data = read_lines('inputs/day10.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
