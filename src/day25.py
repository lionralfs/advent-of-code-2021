from utils import read_lines


def print_field(east, south, size_x, size_y):
    field = [['.' for _ in range(size_x)] for _ in range(size_y)]
    for (x, y) in east:
        field[y][x] = '>'
    for (x, y) in south:
        field[y][x] = 'v'
    print('\n'.join([''.join(line) for line in field]))


def parse(lines):
    south = set()
    east = set()
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            val = line[x]
            if val == '>':
                east.add((x, y))
            elif val == 'v':
                south.add((x, y))
    return east, south, len(lines[0]), len(lines)


def run1(input):
    east, south, size_x, size_y = parse(input)

    steps = 0
    while True:
        steps += 1
        # run all east
        moved = 0
        neweast = set()
        for old in east:
            x, y = old
            new = ((x+1) % size_x, y)
            if new not in east and new not in south:
                neweast.add(new)
                moved += 1
            else:
                neweast.add(old)
        east = neweast

        # run all south
        newsouth = set()
        for old in south:
            x, y = old
            new = (x, (y+1) % size_y)
            if new not in east and new not in south:
                newsouth.add(new)
                moved += 1
            else:
                newsouth.add(old)
        south = newsouth

        if moved == 0:
            break

    return steps


if __name__ == '__main__':
    input = read_lines('inputs/day25.txt')
    print('[Part1]:', run1(input))
