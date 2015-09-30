import fileinput

swaps = 0
for line in fileinput.input():
    data = line.split()
    break
data = [ int(x) for x in data ]

result = []
for steps in xrange(len(data), 2, -1):
    for index in xrange(steps-1):
        if data[index] > data[index+1]:
            data[index], data[index+1] = data[index+1], data[index]
            swaps += 1

print swaps
for x in data:
    print x,
