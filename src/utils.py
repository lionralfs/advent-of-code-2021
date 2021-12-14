def read_lines(file, cast_as=str):
    with open(file, mode='rt') as f:
        return [cast_as(x.rstrip()) for x in f.readlines()]


def read_segments(file):
    with open(file, mode='rt') as f:
        return f.read().split('\n\n')
