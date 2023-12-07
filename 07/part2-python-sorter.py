data = []

with open("part2-solution.txt", 'r') as f:
    for line in f:
        hand, bid = line.strip().split(' ')
        data.append([None, hand, bid])

for entry in data:
    entry[0] = ''.join(sorted(entry[1])[::-1])

with open("part2-solution-pythonsorted.txt", 'w') as f:
    for entry in data:
        f.write(f"{entry[0]} {entry[1]} {entry[2]}\n")
