originallines = [int(line, base = 2) for line in open("input").readlines()]
originallines.sort()
lines = originallines.copy()

for i in reversed(range(12)):
    if lines[0] == lines[len(lines)-1]:
        break
    common = 2**i & lines[len(lines) // 2]
    lines = [line for line in lines if 2**i & line == common]
first = lines[0]

lines = originallines.copy()
for i in reversed(range(12)):
    if lines[0] == lines[len(lines)-1]:
        break
    common = 2**i & lines[len(lines) // 2]
    lines = [line for line in lines if 2**i & line != common]
    second = lines[0]
print(first, second, first * second)