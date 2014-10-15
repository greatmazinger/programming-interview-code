import itertools

def sieve(xs):
    x = next(xs)
    yield x
    for y in sieve(i for i in xs if (i % x) > 0):
        yield y

try:
    for p in sieve(itertools.count(2)):
        print p,
        if p > 1000:
            break
    print ''
except RuntimeError as e:
    print e

