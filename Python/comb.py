def comb(xs):
    if len(xs) == 0:
        return [""]
    else:
        return comb2(xs) + [""]

def comb2(xs):
    if len(xs) == 1:
        return [ xs ]
    else:
        subwo = comb2( xs[1:] )
        head = xs[0]
        subwith = [ head + zs for zs in subwo ]
        return subwo + subwith + [ head ]

result = comb( "abcde" )
result.sort()
print result
print len( result )
