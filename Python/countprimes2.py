import itertools
import fileinput

def sieve(xs):
    x = next(xs)
    yield x
    for y in sieve(i for i in xs if (i % x) > 0):
        yield y

if __name__ == "__main__":
    count = 0
    stdin = fileinput.input()
    num = int(stdin.next())
    for p in sieve(itertools.count(2)):
        if p > num:
            break
        count += 1
    print count
