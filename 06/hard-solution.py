import os

sim_length = 256

fish = list(map(int, open(os.path.join(os.path.dirname(__file__),"input")).read().split(",")))
fish_counts = {age : fish.count(age) for age in fish}
for i in range(10):
    if not i in fish_counts.keys():
        fish_counts[i] = 0
print(fish_counts)

for i in range(sim_length):
    for j in range(10):
        if j == 0:
            fish_counts[9] = fish_counts[0]
            fish_counts[7] += fish_counts[0]
            fish_counts[j] = fish_counts[j+1]
        elif j == 9:
            fish_counts[j] = 0
        else:
            fish_counts[j] = fish_counts[j+1]
    for j in range(10):
        if fish_counts[j] != 0:
            print(j, fish_counts[j], sep=":", end=", ")
    print()
print(fish_counts)
print(sum(fish_counts.values()))