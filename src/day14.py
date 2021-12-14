from utils import read_segments


def run(data, iterations):
    template = data[0]
    instructions = dict([x.split(' -> ') for x in data[1].split('\n')])

    rules_extended = produced_rules(instructions)
    tracked_rules_count, letter_count = initial(template)

    for _ in range(iterations):
        new_rules = {}
        for rule, count in list(tracked_rules_count.items()):
            # first, each rule produced a letter
            letter = instructions[rule]
            if letter not in letter_count:
                letter_count[letter] = 0
            letter_count[letter] += count

            # then, make the new rules
            for new_rule in rules_extended[rule]:
                if new_rule not in new_rules:
                    new_rules[new_rule] = count
                else:
                    new_rules[new_rule] += count
        tracked_rules_count = new_rules

    letters_sorted = sorted(letter_count.items(), key=lambda x: x[1])
    return letters_sorted[-1][1] - letters_sorted[0][1]


def initial(template):
    rules = {}
    for i in range(len(template)-1):
        pair = template[i:i+2]
        if pair not in rules:
            rules[pair] = 1
        else:
            rules[pair] += 1

    counts = {}
    for letter in template:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1

    return rules, counts


def produced_rules(instructions):
    result = {}
    for key, value in instructions.items():
        result[key] = [key[0]+value, value+key[1]]
    return result


def run1(data):
    return run(data, iterations=10)


def run2(data):
    return run(data, iterations=40)


if __name__ == '__main__':
    data = read_segments('inputs/day14.txt')
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
