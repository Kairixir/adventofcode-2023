import re

lst = []

with open("just_stars.txt", "r") as f:
    for line in f.readlines():
        lst.append(line.strip())

# for line in lst:
#     pass


# print(next(re.finditer(r'(?<=\.)(\d+)(?:(?=\.)|(?=$))', line)))

line_num = 2
line = lst[line_num]
print(lst[line_num - 1])
print(line)
print(lst[line_num + 1])

for match in re.finditer(r"\*", line):
    print(match)
    print(match.start())
    print(match.end())
    print(match.span())
    re.finditer(r"(?<=\.)(\d+)(?:(?=\.)|(?=$))", line)
    for i in range(-1, 2):
        inverse = ""
        for j in range(match.start() - 1, match.start() + 2):
            if lst[line_num + i][j] not in ["*", "."]:
                pattern = re.compile(r"(\d+)\.")
                first_part = pattern.search(lst[line_num + i], j).group(0)
                print("First part: ", first_part)
                pattern.sub(r"\." * len(first_part), lst[line)
