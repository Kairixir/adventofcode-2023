import re

FILE = "part1-solution.txt"
# FILE = "test-part1.txt"


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


key = "AAA"
found_end = False

num_step = 0
while key != "ZZZ":
    print(f"{key}: {num_step}")
    key = paths[key][int(instructions[num_step % len(instructions)])]
    num_step += 1

print(f"{key}: {num_step}")
