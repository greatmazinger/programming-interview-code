import fileinput
from itertools import permutations

result = []
lines = []
for line in fileinput.input():
    lines.append( line.rstrip() )

result = []
for line in lines:
    if len(line) == 1:
        result.append((0,1))
    else:
        sortline = sorted(line)
        cur = 0
        word = []
        while cur < len(sortline)-1:
            if sortline[cur] == sortline[cur+1]:
                word.append( sortline.pop(cur) )
                word.append( sortline.pop(cur) )
            else:
                cur += 1
        removed = len(sortline) - 1 if len(sortline) > 0 else 0
        halfword =  [ word[i] for i in xrange(0, len(word), 2) ]
        perms = permutations(halfword)
        tmplist = []
        for p in perms:
            tmplist.append( "".join(list(p)) )
        tmpset = set(tmplist)
        ptotal = len(tmpset)
        result.append((removed, ptotal))
for x in result:
    print "%d,%d" % (x[0], x[1])
print
