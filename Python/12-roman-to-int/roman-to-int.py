romdict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

subdict = {
     "IV": 4,
     "IX": 9,
     "XL": 40,
     "XC": 90,
     "CD": 400,
     "CM": 900
}

def romanToInt(s: str) -> int:
    # First, find all instances of:
    total = 0
    i = 0
    while i < len(s) - 1:
        pat2 = "".join(s[i:i+2])
        if pat2 in subdict:
            total += subdict[pat2]
            i += 2
        else:
            x = s[i]
            total += romdict[x]
            i += 1
    if i < len(s):
        total += romdict[s[i]]
    return total

def test1():
    s = "MCMXCIV"
    exp = 1994

    result = romanToInt(s)
    print(f"TEST 1: exp={exp}, result={result}")
    assert exp == result

if __name__ == "__main__":
    test1()
