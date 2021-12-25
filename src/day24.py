from os import name
from utils import read_lines


def parse_line(line):
    parts = line.split(' ')
    operation = parts[0]
    arg1 = parts[1]

    if len(parts) == 2:
        return (operation, arg1)
    arg2 = parts[2]
    if arg2 not in ['w', 'x', 'y', 'z']:
        arg2 = int(arg2)
    return (operation, arg1, arg2)


def run(inputs: list[str], operations):
    registers = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    for operation in operations:
        print(registers)
        opname = operation[0]
        a_val = registers[operation[1]] if \
            operation[1] in registers.keys() else operation[1]
        b_val = None
        if len(operation) > 2:
            b_val = registers[operation[2]] if \
                operation[2] in registers.keys(
            ) else operation[2]

        if opname == 'inp':
            assert len(inputs) > 0
            val = inputs[0]
            inputs = inputs[1:]
            registers[operation[1]] = val
            continue
        if opname == 'add':
            registers[operation[1]] = a_val + b_val
            continue
        if opname == 'mul':
            registers[operation[1]] = a_val * b_val
            continue
        if opname == 'div':
            assert b_val != 0
            registers[operation[1]] = int(a_val / b_val)
            continue
        if opname == 'mod':
            assert a_val >= 0
            assert b_val > 0
            registers[operation[1]] = a_val % b_val
            continue
        if opname == 'eql':
            registers[operation[1]] = 1 if a_val == b_val else 0
            continue

    return registers['z']


def run1(input):
    operations = [parse_line(line) for line in input]

    # solved it on paper..
    # solution for part1: 49917929934999
    # solution for part2: 11911316711816
    output = run([1, 1, 9, 1, 1, 3, 1, 6, 7, 1, 1, 8, 1, 6], operations)


if __name__ == '__main__':
    input = read_lines('inputs/day24.txt')
    run1(input)
