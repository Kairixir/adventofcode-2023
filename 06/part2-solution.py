with open("input.txt", "r") as f:
    time = f.readline().replace(" ", "").split(":")
    time = int(time[1])
    best_distance = f.readline().replace(" ", "").split(":")
    best_distance = int(best_distance[1])

counter = 0

for hold_time in range(time // 2 + 1):
    distance = hold_time * (time - hold_time)
    if distance > best_distance:
        counter += 2

if time % 2 == 0:
    counter = counter - 1

print(counter)
