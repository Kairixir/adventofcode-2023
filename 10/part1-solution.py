import re
from collections import deque
import numpy as np

FILE = "part1-solution.txt"
# FILE = "part1-test.txt"

with open(FILE) as f:
    matrix = []
    for line in f.readlines():
        matrix.append(line)

start_pos = None

for i, row in enumerate(matrix):
    search = re.search("S", row)
    if search is not None:
        start_pos = np.array((i, search.start()))
        del search
        break

visited_matrix = np.zeros((len(matrix), len(matrix)))


# Of type [(y_1, x_1), (y_2, x_2), ...]
pipes = {
    "|": [np.array((-1, 0)), np.array((1, 0))],
    "-": [np.array((0, -1)), np.array((0, 1))],
    "L": [np.array((-1, 0)), np.array((0, 1))],
    "J": [np.array((-1, 0)), np.array((0, -1))],
    "7": [np.array((1, 0)), np.array((0, -1))],
    "F": [np.array((1, 0)), np.array((0, 1))],
}


def breadth_search(start) -> int:
    queue = deque()
#    starting_steps = [np.array((1, 0)), np.array((0, 1)), np.array((-1, 0)), np.array((0, -1))]
    starting_steps = [np.array((-1, 0)), np.array((0, 1))]
    starting_positions = [np.array(start) + starting_step for starting_step in starting_steps]
    for start_pos in starting_positions:
        queue.append((start_pos, 1))
    steps = []
#    import pdb; pdb.set_trace()
    while queue:
        current, step = queue.popleft()
        if visited_matrix[current[0]][current[1]]:
            steps.append(step)
            continue
        visited_matrix[current[0]][current[1]] = True
        for step_direction in pipes[matrix[current[0]][current[1]]]:
            next_step = current + step_direction
            if matrix[next_step[0]][next_step[1]] in ["S", "."]:
                continue
            if not np.any(next_step < 0) and not visited_matrix[next_step[0]][next_step[1]]:
                queue.append((next_step, step + 1))


    print(steps)
    return max(steps)


print(breadth_search(start_pos))
