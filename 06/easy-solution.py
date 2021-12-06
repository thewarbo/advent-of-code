import os

sim_length = 256

fish = list(map(int, open(os.path.join(os.path.dirname(__file__),"input")).read().split(",")))

for i in range(sim_length):
    old_fish = len(fish)
    for j in range(old_fish):
        if fish[j] == 0:
            fish.append(8)
            fish[j] = 6
        else:
            fish[j] -= 1
    print(i, end=",")
print(len(fish))