import os
import copy
from collections import Counter

def format(line):
    return [int(x) for x in line.strip()]

puzzle = list(map(format, open(os.path.join(os.path.dirname(__file__),"input")).readlines()))
height = len(puzzle)
width = len(puzzle[0])
points = [[x,y] for y in range(height) for x in range(width)]

def find_neighbors(x, y):
    neighbors = []
    if x > 0: neighbors.append([x-1, y])
    if x < width-1: neighbors.append([x+1, y])
    if y > 0: neighbors.append([x, y-1])
    if y < height-1: neighbors.append([x, y+1])
    return neighbors

def is_low_point(x,y):
    return all([puzzle[y0][x0] > puzzle[y][x] for (x0,y0) in find_neighbors(x,y)])

basins = [[None]* width for i in range(height)]
remaining = [[True]* width for i in range(height)]

for [x,y] in points:
    if is_low_point(x,y):
        basins[y][x] = str(x) + "," + str(y)
        remaining[y][x] = False
    if puzzle[y][x] == 9:
        remaining[y][x] = False
        
while any([remaining[y][x] for [x,y] in points]):
    for [x,y] in points:
       if remaining[y][x]:
           basins[y][x] = next((basins[y0][x0] for [x0,y0] in find_neighbors(x,y) if basins[y0][x0] is not None), None)
           if basins[y][x] != None:
               remaining[y][x] = False
    print(basins)

print(Counter([basin for list1 in basins for basin in list1]).most_common(4))