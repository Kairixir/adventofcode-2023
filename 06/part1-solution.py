with open("input.txt", "r") as f:
    times = f.readline().strip().split(" ")
    times = times[1:]
    times = map(int, times)
    distances = f.readline().strip().split(" ")
    distances = distances[1:]
    distances = map(int, distances)


total = 1
for i, time in enumerate(times):
    best_distance = next(distances)
    counter = 0

    for hold_time in range(time // 2 + 1):
        distance = hold_time * (time - hold_time)
        if distance > best_distance:
            counter += 2

    if time % 2 == 0:
        counter = counter - 1

    total *= counter

print(total)
