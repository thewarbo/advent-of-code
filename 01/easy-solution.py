f = open("input")
count = 0
lines = [int(line) for line in f.readlines()]
solution = [(lines[i+1] - lines[i] > 0) for i in range(len(lines)-1)]
print(sum(solution))
