f = open("input")
count = 0
lines = [int(line) for line in f.readlines()]
sums = [lines[i] + lines[i+1] + lines[i+2] for i in range(len(lines)-2)]
solution = [(sums[i+1] - sums[i] > 0) for i in range(len(sums)-1)]
print(sum(solution))
