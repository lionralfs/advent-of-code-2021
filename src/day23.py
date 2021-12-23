from utils import read_lines
from collections import defaultdict
from queue import PriorityQueue


MASK = [list('#############'),
        list('#...........#'),
        list('###.#.#.#.###'),
        list('  #.#.#.#.#'),
        list('  #########')]


def print_state(state):
    assert len(state) == 8
    result = [line.copy() for line in MASK]
    a1 = state[0]
    result[a1[0]][a1[1]] = 'A'
    a2 = state[1]
    result[a2[0]][a2[1]] = 'A'
    b1 = state[2]
    result[b1[0]][b1[1]] = 'B'
    b2 = state[3]
    result[b2[0]][b2[1]] = 'B'
    c1 = state[4]
    result[c1[0]][c1[1]] = 'C'
    c2 = state[5]
    result[c2[0]][c2[1]] = 'C'
    d1 = state[6]
    result[d1[0]][d1[1]] = 'D'
    d2 = state[7]
    result[d2[0]][d2[1]] = 'D'
    print('\n'.join([''.join(line) for line in result]))


room_index = {
    0: 3,
    1: 3,
    2: 5,
    3: 5,
    4: 7,
    5: 7,
    6: 9,
    7: 9,
}

cost_multiplier = {
    0: 1,
    1: 1,
    2: 10,
    3: 10,
    4: 100,
    5: 100,
    6: 1000,
    7: 1000,
}


def can_go_to_room(state, index):
    current_pos = state[index]
    assert current_pos[0] == 1  # in hallway
    designated_room = room_index[index]

    # if needing to go right, check all potential blocks
    if designated_room > current_pos[1]:
        potential_block = (1, designated_room-1)
        while potential_block[1] > current_pos[1]:
            if potential_block in state:
                return False
            potential_block = (1, potential_block[1]-2)

    # also check right
    if designated_room < current_pos[1]:
        potential_block = (1, designated_room+1)
        while potential_block[1] < current_pos[1]:
            if potential_block in state:
                return False
            potential_block = (1, potential_block[1]+2)

    return True


def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])


def is_done(state):
    return all(room_done(state, i) for i in [3, 5, 7, 9])


def room_done(state, room):
    positions = [state[i] for i, iroom in room_index.items() if room == iroom]
    a = [position[1] == room for position in positions]
    return len(a) == 2 and all(a)


def room_partially_done(state, room):
    for i in range(len(state)):
        if state[i][1] == room and room_index[i] != room:
            return False
    return True


def next_states_for_index(
    state: list[tuple[int, int]],
    index: int
) -> tuple[int, list]:
    result = []
    current_pos = state[index]
    designated_room = room_index[index]
    in_hallway = current_pos[0] == 1

    # first, don't handle rooms that are already done
    if not in_hallway and room_done(state, current_pos[1]):
        return []

    # second, if in hallway, check if way to designated room is free
    if in_hallway and can_go_to_room(state, index):
        # check if room is partially done
        if room_partially_done(state, designated_room):
            if (3, designated_room) in state:
                newpos = state[:index]+((2, designated_room),)+state[index+1:]
                steps = abs(designated_room-current_pos[1]) + 1
                cost = steps * cost_multiplier[index]
                return [(cost, newpos)]
            else:
                steps = abs(designated_room-current_pos[1]) + 2
                cost = steps * cost_multiplier[index]
                newpos = state[:index]+((3, designated_room),)+state[index+1:]
                return [(cost, newpos)]

    # if not in hallway,
    # start checking from the bottom
    # of the room if it's possible to move up
    if not in_hallway:
        # bottom of room, check up
        if current_pos[0] == 3 and (2, current_pos[1]) in state:
            return []

        # check hallway, left
        up_left = (1, current_pos[1]-1)
        while up_left[1] > 0:
            if up_left in state:
                break
            steps = manhattan(current_pos, up_left)
            result.append((
                steps * cost_multiplier[index],
                state[:index]+(up_left,)+state[index+1:]
            ))
            if up_left == (1, 2):
                result.append((
                    (steps+1) * cost_multiplier[index],
                    state[:index]+((1, 1),)+state[index+1:]
                ))
            up_left = (1, up_left[1]-2)

        # check hallway, right
        up_right = (1, current_pos[1]+1)
        while up_right[1] < 12:
            if up_right in state:
                break
            steps = manhattan(current_pos, up_right)
            result.append((
                steps * cost_multiplier[index],
                state[:index]+(up_right,)+state[index+1:]
            ))
            if up_right == (1, 10):
                result.append((
                    (steps+1) * cost_multiplier[index],
                    state[:index]+((1, 11),)+state[index+1:]
                ))
            up_right = (1, up_right[1]+2)

    return result


def next_states(state):
    result = []
    for i in range(len(state)):
        for next in next_states_for_index(state, i):
            result.append(next)

    return result


def run1(lines):
    input_positions = [
        (2, 3), (3, 3), (2, 5), (3, 5), (2, 7), (3, 7), (2, 9), (3, 9)
    ]

    positions_by_value = defaultdict(list)

    for y, x in input_positions:
        val = lines[y][x]
        positions_by_value[val].append((y, x))

    state = tuple(
        positions_by_value['A'] +
        positions_by_value['B'] +
        positions_by_value['C'] +
        positions_by_value['D']
    )

    return solve(state)


def solve(start_state):
    queue = PriorityQueue()
    queue.put((0, start_state))
    distances = {
        start_state: 0
    }

    while not queue.empty():
        _, state = queue.get()

        if is_done(state):
            return distances[state]

        for costchange, next in next_states(state):
            nextcost = distances[state]+costchange
            if next not in distances or distances[next] > nextcost:
                queue.put((nextcost, next))
                distances[next] = nextcost
    return None


if __name__ == '__main__':
    input = read_lines('inputs/day23.txt')
    print('[Part1]:', run1(input))
    # print('[Part2]:', run2(input))
