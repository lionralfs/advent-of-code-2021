from utils import read_lines
from itertools import product
from collections import Counter, defaultdict


class Die:
    last = 0
    rolls = 0

    def roll(self):
        self.rolls += 1
        self.last += 1
        if self.last == 101:
            self.last = 1
        return self.last


def run1(input_raw):
    pos = [int(line.split(': ')[1])-1 for line in input_raw]
    scores = [0, 0]

    die = Die()
    i = 0
    while scores[0] < 1000 and scores[1] < 1000:
        player = i % 2
        a = die.roll()
        b = die.roll()
        c = die.roll()
        d = sum([a, b, c])
        pos[player] = (pos[player] + d) % 10
        scores[player] = scores[player] + pos[player] + 1
        i += 1
    loser_points = scores[0] if scores[0] < 1000 else scores[1]

    return loser_points * die.rolls


"""
precalculate the number possibilities (universes) that are
created for each possible amount of steps

exactly 1 possibility where you go 3 steps (rolled 1-1-1)
???
exactly 1 possibility where you go 9 steps (rolled 3-3-3)
"""
sums = [sum(comb) for comb in set(product(range(1, 4), repeat=3))]
possibilities_of_steps = Counter(sums)


def new_player_states(pos, score):
    result = defaultdict(int)
    for step, count in possibilities_of_steps.items():
        newpos = (pos + step) % 10
        newscore = score + newpos + 1
        result[(newpos, newscore)] += count
    return result


def run2(input_raw):
    pos = [int(line.split(': ')[1])-1 for line in input_raw]

    """
    the state is a dictionary of

    (gamestate) -> number of universes with this game state

    where gamestate is a 4-tuple of:
    - player 1 position (0-indexed)
    - player 2 position (0-indexed)
    - player 1 score
    - player 2 score
    """
    state = {(pos[0], pos[1], 0, 0): 1}

    p1_winning_count = 0
    p2_winning_count = 0

    while len(state) > 0:
        newstate = defaultdict(int)

        for item, universes in state.items():
            p1_pos = item[0]
            p2_pos = item[1]
            p1_score = item[2]
            p2_score = item[3]

            new_p1 = new_player_states(p1_pos, p1_score)
            new_p2 = new_player_states(p2_pos, p2_score)

            for p1_state, p1count in new_p1.items():
                if p1_state[1] >= 21:
                    p1_winning_count += p1count * universes
                    continue
                for p2_state, p2count in new_p2.items():
                    if p2_state[1] >= 21:
                        p2_winning_count += p1count * p2count * universes
                        continue
                    newstate[(p1_state[0], p2_state[0], p1_state[1],
                              p2_state[1])] += p1count * p2count * universes

        state = newstate

    return max(p1_winning_count, p2_winning_count)


if __name__ == '__main__':
    input = read_lines('inputs/day21.txt')
    print('[Part1]:', run1(input))
    print('[Part2]:', run2(input))
