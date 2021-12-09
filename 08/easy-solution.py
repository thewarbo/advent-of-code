import os
import re

puzzle = list(map(lambda x : x.strip().split(" | "), open(os.path.join(os.path.dirname(__file__),"input")).readlines()))
count = 0
for line in puzzle:
    count += len([word for word in line[1].split() if len(word) in [2,3,4,7]])

print(count)