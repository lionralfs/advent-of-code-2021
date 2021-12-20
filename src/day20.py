from utils import read_segments
import numpy as np


def neighbors(point):
    x = point[0]
    y = point[1]
    result = []

    # top left
    result.append((x-1, y-1))
    # top
    result.append((x-1, y))
    # top right
    result.append((x-1, y+1))
    # left
    result.append((x, y-1))
    # middle
    result.append((x, y))
    # right
    result.append((x, y+1))
    # bottom left
    result.append((x+1, y-1))
    # bottom
    result.append((x+1, y))
    # bottom right
    result.append((x+1, y+1))

    return result


def run(segments, iterations):
    alg = segments[0]
    image = np.array([list(line) for line in segments[1].split('\n')])
    output = None

    neutral_element = '.'
    for _ in range(iterations):
        pad_size = 3
        image = np.pad(image, (pad_size, pad_size),
                       constant_values=(neutral_element))
        output = image.copy()

        row_count = image.shape[0]
        col_count = image.shape[1]

        for y in range(1, row_count - 1):
            for x in range(1, col_count - 1):
                point = (x, y)
                ns = neighbors(point)
                binary = ''.join([image[neighbor] for neighbor in ns])
                binary = binary.replace('.', '0')
                binary = binary.replace('#', '1')
                binary = int(binary, 2)
                output[point] = alg[binary]

        neutral_element = output[(1, 1)]
        output = np.delete(output, [0, 1, -2, -1], axis=0)
        output = np.delete(output, [0, 1, -2, -1], axis=1)
        image = output

    return len(output[output == '#'])


def run1(segments):
    return run(segments, 2)


def run2(segments):
    return run(segments, 50)


if __name__ == '__main__':
    input = read_segments('inputs/day20.txt')
    print('[Part1]:', run1(input))
    print('[Part2]:', run2(input))
