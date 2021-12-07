import os
import statistics

crabs = list(map(int, open(os.path.join(os.path.dirname(__file__),"input")).read().split(",")))
print(sum([abs( crab - statistics.median(crabs) )for crab in crabs]))

