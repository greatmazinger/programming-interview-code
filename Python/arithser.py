# TODO: Did this for a coding challenge.
# I should have documented what it does. I will
# commit the code and figure out what it does later.
# From the title, it has something to do with arithmetic series.
# 2015-1128
import fileinput

stdin = fileinput.input()
num = stdin.next()
num = int(num.rstrip())
numlist = stdin.next()
numlist = [ int(x) for x in numlist.rstrip().split() ]

diffs = {}
for x in xrange(num-2):
    d = numlist[x+1] - numlist[x]
    if d not in diffs:
        diffs[d] = 1
    else:
        diffs[d] += 1
        step = None
for d, dcount in diffs.iteritems():
    if dcount > 1:
        step = d
if step != None:
    for x in xrange(num-2):
        if (numlist[x+1] - numlist[x]) != step:
            print numlist[x] + step
            exit(0)
exit(-1)           
