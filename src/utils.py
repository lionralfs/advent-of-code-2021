def read_lines(file, cast_as=str):
    with open(file, mode='rt') as f:
        return [cast_as(x.rstrip()) for x in f.readlines()]
