lines = [int(line, base = 2) for line in open("input").readlines()]
zerocounts = {2**i : 0 for i in range(12)}
onecounts = {2**i : 0 for i in range(12)}

for line in lines:
    for i in range(12):
        if (2**i) & line:
            onecounts[2**i] += 1
        else:
            zerocounts[2**i] += 1
print(zerocounts)
print(onecounts)
epsilon = sum([2**i for i in range(12) if onecounts[2**i] > zerocounts[2**i]])
delta = sum([2**i for i in range(12) if onecounts[2**i] < zerocounts[2**i]])
print(epsilon, delta, epsilon*delta)