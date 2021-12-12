from utils import read_lines


def valid_neighbor1(path, neighbor):
    return neighbor.isupper() or neighbor not in path


def valid_neighbor2(path, neighbor):
    if neighbor.isupper():
        return True

    if neighbor in ['start', 'end']:
        return neighbor not in path

    lower = [n for n in path if n.islower()]
    # allow the neighbor if no other lowercase letter is used twice
    if len(lower) == len(set(lower)):
        return True
    return neighbor not in path


def search(adjacency_list, start, end, neighbor_check):
    todo = [[start]]
    result_paths = []

    while len(todo) > 0:
        path = todo.pop()
        last_in_path = path[-1]
        if last_in_path == end:
            result_paths.append(path)
            continue

        neighbors = [n for n in adjacency_list[last_in_path]
                     if neighbor_check(path, n)]
        for neighbor in neighbors:
            new_path = path.copy()
            new_path.append(neighbor)
            todo.append(new_path)

    return result_paths


def run1(data):
    lines = [line.split('-') for line in data]
    adjacency_list = {}
    for a, b in lines:
        if a not in adjacency_list:
            adjacency_list[a] = set()
        if b not in adjacency_list:
            adjacency_list[b] = set()

        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    results = search(adjacency_list, 'start', 'end',
                     neighbor_check=valid_neighbor1)
    return len(results)


def run2(data):
    lines = [line.split('-') for line in data]
    adjacency_list = {}
    for a, b in lines:
        if a not in adjacency_list:
            adjacency_list[a] = set()
        if b not in adjacency_list:
            adjacency_list[b] = set()

        adjacency_list[a].add(b)
        adjacency_list[b].add(a)

    results = search(adjacency_list, 'start', 'end',
                     neighbor_check=valid_neighbor2)
    return len(results)


if __name__ == '__main__':
    data = read_lines('inputs/day12.txt', cast_as=str)
    print('[Part1]:', run1(data))
    print('[Part2]:', run2(data))
