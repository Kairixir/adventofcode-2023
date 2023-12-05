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
print(lst[line_num])
print(lst[line_num + 1])

matches = []
symbols = []
for y, line in enumerate(lst):
    for match in re.finditer(r"\*", line):
        symbols[(match.start(),y)] = 

for i, line in enumerate(lst):
    for match in re.finditer(r"\d+", line)
        for symb_lines in symbols[i-1:i+1]

for line in lst:
    matches.append(re.finditer(r"\d+", line))
#for match in re.finditer(r"\*", line):
#    # re.finditer(r"(?<=\.)(\d+)(?:(?=\.)|(?=$))", line)
#    for i in range(-1, 2):
#        pass
#        re.findall(r"\d+", line[line_num + i]

