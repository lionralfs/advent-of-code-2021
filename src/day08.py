from utils import read_lines


def unique_entries(line):
    result = set()

    for entry in line[0]:
        result.add(frozenset(entry))
    for entry in line[1]:
        result.add(frozenset(entry))

    return result


def find(fn, items):
    return list(filter(fn, items))[0]


def get_numbers(data):
    """
    this is where the magic happens
    """
    entries = unique_entries(data)
    # the 1 is the only number with two segments
    one = find(lambda entry: len(entry) == 2, entries)
    # the 2 is the only number with four segments
    four = find(lambda entry: len(entry) == 4, entries)
    # the 7 is the only number with three segments
    seven = find(lambda entry: len(entry) == 3, entries)
    # the 8 is the only number with seven segments
    eight = find(lambda entry: len(entry) == 7, entries)
    entries.remove(one)
    entries.remove(four)
    entries.remove(seven)
    entries.remove(eight)

    # using the fact that 8 - 6 is a subset of number 1 with length 1
    six = find(
        lambda entry: eight.difference(entry).issubset(
            one) and len(eight.difference(entry)) == 1,
        entries
    )
    entries.remove(six)

    # 9 has six segments and the 4 fits completely inside it
    nine = find(lambda entry: len(entry) == 6 and len(
        four.union(entry)) == 6, entries)
    entries.remove(nine)

    # the left, bottom segment is 8 - 9
    left_bottom = eight.difference(nine)

    # the 5 is the 6 without the bottom left segment
    five = find(
        lambda entry: len(six.difference(
            left_bottom).symmetric_difference(entry)) == 0,
        entries)
    entries.remove(five)

    # the 0 is the last number that's left with 6 segments
    zero = find(lambda entry: len(entry) == 6, entries)
    entries.remove(zero)

    # the two is the only one that's left using the bottom left segment
    two = find(lambda entry: left_bottom.issubset(entry), entries)
    entries.remove(two)

    # three must be the last one left
    three = entries.pop()

    return {
        zero: 0,
        one: 1,
        two: 2,
        three: 3,
        four: 4,
        five: 5,
        six: 6,
        seven: 7,
        eight: 8,
        nine: 9
    }


def run1(data):
    data = [[x.split(' ') for x in line.split(' | ')] for line in data]

    result = [[x for x in line[1] if len(x) in [2, 3, 4, 7]] for line in data]
    return len([item for sublist in result for item in sublist])


def run2(data):
    data = [[x.split(' ') for x in line.split(' | ')] for line in data]

    outputs = [''.join([str(get_numbers(line)[frozenset(x)])
                       for x in line[1]]) for line in data]

    return sum([int(output) for output in outputs])


if __name__ == '__main__':
    data = read_lines('inputs/day08.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
