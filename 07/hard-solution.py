import os
import statistics

crabs = list(map(int, open(os.path.join(os.path.dirname(__file__),"input")).read().split(",")))

def triangle(n):
    return n * (n+1) / 2

results = {}
for i in range(max(crabs)):
    used = sum([triangle(abs(crab-i)) for crab in crabs])
    results[i] = used

for key in results.keys():
    if results.get(key) == min(results.values()):
        print(key)
        print(results[key])