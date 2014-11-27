import fileinput
from math import sqrt

def count_primes( num ):
    flags = [ True ] * (num+1)
    flags[0] = False
    flags[1] = False
    count = 0
    for x in xrange(2, int(sqrt(num)) + 1):
        if flags[x]:
            y = x * x
            while y <= num:
                flags[y] = False
                y = y + x
    for x in xrange(2,len(flags)):
        if flags[x]:
            count += 1
    return count

if __name__ == "__main__":
    stdin = fileinput.input()
    num = int(stdin.next())
    count = count_primes( num )
    print count

# Performance numbers:
#
#    Total primes up to 1000000 :: 78498
#
#    real    0m2.753s
#    user    0m0.359s
#    sys     0m0.007s
# 
#    100000000
#    Total primes up to 100000000 :: 5761455
#    
#    real    0m49.965s
#    user    0m46.383s
#    sys     0m0.126s
