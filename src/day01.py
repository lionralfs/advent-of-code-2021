from utils import read_lines

data = read_lines('inputs/day01-test01.txt', cast_as=int)


def run1(data):
    last = None
    increasesCounter = 0
    for n in data:
        if last is None:
            last = n
            continue
        if n > last:
            increasesCounter += 1
        last = n
    return increasesCounter


def run2(data):
    lastSum = None
    increasesCounter = 0
    for i in range(len(data)):
        window = data[i:i+3]
        window_sum = sum(window)
        if lastSum is None:
            lastSum = window_sum
            continue

        if window_sum > lastSum:
            increasesCounter += 1
        lastSum = window_sum
    return increasesCounter


if __name__ == '__main__':
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
