import os
import re

def format(line):
    return [int(x) for x in line.strip()]

puzzle = list(map(format, open(os.path.join(os.path.dirname(__file__),"input")).readlines()))
print(puzzle)
height = len(puzzle)
width = len(puzzle[0])

def risk_level(x, y):
    neighbors = []
    if x > 0: neighbors.append([x-1, y])
    if x < width-1: neighbors.append([x+1, y])
    if y > 0: neighbors.append([x, y-1])
    if y < height-1: neighbors.append([x, y+1])
    return all([puzzle[y0][x0] > puzzle[y][x] for (x0,y0) in neighbors]) * (puzzle[y][x] +1)


result = sum([risk_level(x,y) for x in range(width) for y in range(height)])
print(result)
     