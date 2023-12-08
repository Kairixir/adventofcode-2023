import re
import numpy as np

FILE = "part2-solution.txt"
# FILE = "part2-test.txt"


with open(FILE) as f:
    instructions = f.readline().strip()
    f.readline()
    paths = {}
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    for line in f.readlines():
        matches = pattern.match(line)
        if matches is None:
            exit(1)
        paths[matches.group(1)] = matches.group(2, 3)


keys = np.array([key for key in paths.keys() if key[2] == "A"], dtype=str)

end_in_z = np.zeros((1, len(keys)), dtype=bool)


def next_step(key, num_step, instruction_length):
    return paths[key][int(instructions[num_step % instruction_length])]


def is_char_last(key, char):
    return key[-1] == char


counters = np.ones(len(keys), dtype=int)

print(keys)

next_step_vect = np.vectorize(next_step)
is_char_last_vect = np.vectorize(is_char_last)

num_step = 0
while not end_in_z.all():
    keys = next_step_vect(keys, num_step, len(instructions))
    end_in_z = is_char_last_vect(keys, "Z")
    num_step += 1

    if end_in_z.any():
        for i in np.where(end_in_z)[0]:
            print(f"Periodic step for index {i}: {num_step - counters[i]}")
            counters[i] = num_step
        print(f"{counters} at index {np.where(end_in_z)[0]}")
        print(f"Keys: {keys} at num_step {num_step}")

print(f"{keys}: {num_step}")
