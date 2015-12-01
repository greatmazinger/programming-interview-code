import random

def generate_random_list( length, maximum ):
    result = []
    for i in xrange(length):
        result.append( random.randint( 1, maximum ) )
    return sorted( result )

first = generate_random_list( 10, 1000 )
copy1 = list(first)
second = generate_random_list( 20, 2000 )
copy2 = list(second)
result = []

while len(first) > 0 and len(second) > 0:
    if first[0] < second[0]:
        result.append( first.pop(0) )
    else:
        result.append( second.pop(0) )

remain = first if len(first) > 0 else second
result.extend( remain )

print "FIRST:"
print str(copy1)
print "================================================================================"
print "SECOND:"
print str(copy2)
print "================================================================================"
print "RESULT"
print result

print "Verifying...",
verify = sorted(copy1 + copy2)

for i in xrange(len(verify)):
    assert( verify[i] == result[i] )
print "DONE."
