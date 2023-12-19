import re
from collections import deque
import numpy as np

import copy

FILE = "part2-solution.txt"
# FILE = "part1-test.txt"

with open(FILE) as f:
    matrix = []
    for line in f.readlines():
        matrix.append(list(line.strip()))

start_pos = None

for i, row in enumerate(matrix):
    if "S" in row:
        start_pos = np.array((i, row.index("S")))
        break

visited_matrix = np.zeros((len(matrix), len(matrix)))
in_out_matrix = copy.deepcopy(matrix)

# Of type [(y_1, x_1), (y_2, x_2), ...]
pipes = {
    "|": [(np.array((-1, 0)), "U"), (np.array((1, 0)), "D")],
    "-": [(np.array((0, -1)), "L"), (np.array((0, 1)), "R")],
    "L": [(np.array((-1, 0)), "U"), (np.array((0, 1)), "R")],
    "J": [(np.array((-1, 0)), "U"), (np.array((0, -1)), "L")],
    "7": [(np.array((1, 0)), "D"), (np.array((0, -1)), "L")],
    "F": [(np.array((1, 0)), "D"), (np.array((0, 1)), "R")],
}

direction_vectors = {
    "U": np.array((-1, 0)),
    "D": np.array((1, 0)),
    "R": np.array((0, 1)),
    "L": np.array((0, -1)),
}


def left_side_right_side(in_out_matrix, matrix, current, direction):
    # Inner = Left side
    # Outer = Right side
    if direction == "U":
        inner = direction_vectors["L"]
        outer = direction_vectors["R"]
    elif direction == "D":
        inner = direction_vectors["R"]
        outer = direction_vectors["L"]
    elif direction == "R":
        inner = direction_vectors["U"]
        outer = direction_vectors["D"]
    elif direction == "L":
        inner = direction_vectors["D"]
        outer = direction_vectors["U"]
    pos = current + inner
    if (
        not np.any(pos < 0)
        and pos[0] < len(matrix)
        and pos[1] < len(matrix[0])
        and not in_out_matrix[pos[0]][pos[1]] == "X"
    ):
        in_out_matrix[pos[0]][pos[1]] = "I"
    pos = current + outer
    if (
        not np.any(pos < 0)
        and pos[0] < len(matrix)
        and pos[1] < len(matrix[0])
        and not in_out_matrix[pos[0]][pos[1]] == "X"
    ):
        in_out_matrix[pos[0]][pos[1]] = "O"


def breadth_search(start, matrix, in_out_matrix):
    #    starting_steps = [np.array((1, 0)), np.array((0, 1)), np.array((-1, 0)), np.array((0, -1))]
    queue = deque()
    # starting_steps = [np.array((-1, 0)), np.array((0, 1))]
    starting_steps = [np.array((-1, 0))]
    starting_positions = [
        np.array(start) + starting_step for starting_step in starting_steps
    ]
    for start_pos in starting_positions:
        queue.append((start_pos, 1, "U"))
    steps = []
    while queue:
        current, step, direction = queue.popleft()
        if visited_matrix[current[0]][current[1]]:
            steps.append(step)
            continue
        visited_matrix[current[0]][current[1]] = True

        in_out_matrix[current[0]][current[1]] = "X"

        # I = Left side
        # O = Right side
        left_side_right_side(in_out_matrix, matrix, current, direction)

        for step_direction, direction in pipes[matrix[current[0]][current[1]]]:
            next_step = current + step_direction
            if matrix[next_step[0]][next_step[1]] in ["S", ".", "X"]:
                continue
            if (
                not np.any(next_step < 0)
                and not visited_matrix[next_step[0]][next_step[1]]
            ):
                queue.append((next_step, step + 1, direction))

    return in_out_matrix


new_matrix = breadth_search(start_pos, matrix, in_out_matrix)

with open("loop-designated.txt", "w") as f:
    for line in new_matrix:
        f.write("".join(line) + "\n")
