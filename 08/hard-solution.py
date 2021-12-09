import os
import re
import collections

puzzle = list(map(lambda x : x.strip().split(" | "), open(os.path.join(os.path.dirname(__file__),"input")).readlines()))
count = 0
for line in puzzle:
    count += len([word for word in line[1].split() if len(word) in [2,3,4,7]])

c = collections.Counter({len(word) : 1 for line in puzzle for part in line for word in part.split()})

test_counter = collections.Counter(["one", "two", "two"])
print(test_counter)

print(count)