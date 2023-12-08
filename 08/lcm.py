from math import lcm
from functools import reduce

# Wrong
nums = [13939, 17621, 11309, 20777, 19199, 15517]
print(reduce(lcm, nums))

# Right - Why?
# I had 17620 instad of 17621, lol
print(lcm(13939, 17621, 11309, 20777, 19199, 15517))
