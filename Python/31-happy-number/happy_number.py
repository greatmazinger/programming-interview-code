def get_next_number(x):
    digits = []
    while x >= 10: 
        y = x // 10
        rem = x % 10
        digits.append(rem)
        x = y
    if x > 0:
        digits.append(x)
    return sum(d*d for d in digits)

def isHappy(n: int) -> bool:
    seen = {}
    nextnum = n
    while (nextnum != 1) and (nextnum not in seen):
        temp = get_next_number(nextnum)
        seen[nextnum] = temp
        nextnum = temp
    return nextnum == 1

def test1():
    print("Running TEST 1:")
    n = 19
    assert isHappy(n)
    print("TEST 1 success.")


if __name__ == "__main__":
    test1()
