import re
import os

my_pattern = r"(\d+),(\d+) -> (\d+),(\d+)"

lines = open(os.path.join(os.path.dirname(__file__),"input")).readlines()

segments = [list(map(int, re.search(my_pattern, line).groups())) for line in lines]

def makes_intersection(seg, x, y):
    if seg[0] == seg[2]:
        return seg[0] == x and ((seg[1] <= y and y <= seg[3]) or (seg[3] <= y and y <= seg[1]))
    elif seg[2] == x:
        return seg[3] == y
    else:
        return (min(seg[0], seg[2]) <= x and x <= max(seg[0],seg[2]) and \
            min(seg[1],seg[3]) <= y and y <= max(seg[1], seg[3])) and \
            abs((seg[3] - seg[1])/(seg[2] - seg[0]) - (seg[3] - y)/(seg[2] - x)) < 0.001
    

point_count = 0
multis = []
for x in range(1000):
    print(x, end=",")
    for y in range(1000):
        point_count += (sum([makes_intersection(seg, x, y) for seg in segments]) > 1)

            

print()
print(multis)
print(point_count)
        