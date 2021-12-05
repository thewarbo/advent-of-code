import re
import os

my_pattern = r"(\d+),(\d+) -> (\d+),(\d+)"

lines = open(os.path.join(os.path.dirname(__file__),"input")).readlines()

segments = [list(map(int, re.search(my_pattern, line).groups())) for line in lines]
segments = [seg for seg in segments if ((seg[0] == seg[2]) or (seg[1] == seg[3]))]

def sorter(arg):
    if arg[0] > arg[2]:
        (arg[2], arg[0]) = (arg[0], arg[2])
    if arg[1] > arg[3]:
        (arg[3], arg[1]) = (arg[1], arg[3])
    return arg

        
segments = list(map( sorter, segments ))

point_count = 0
for x in range(1000):
    print(x, end = ",")
    for y in range(1000):
        point_count += (sum([(seg[0] <= x and x <= seg[2] and seg[1] <= y and y <= seg[3]) for seg in segments]) > 1)

print()
print(point_count)
        