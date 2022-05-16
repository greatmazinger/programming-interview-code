from random import randrange

randset = set([])

while len(randset) < 21:
    num = randrange(1,101)
    if num not in randset:
        randset.update([ num ])

result = list(randset)
result.sort()

print(result)
