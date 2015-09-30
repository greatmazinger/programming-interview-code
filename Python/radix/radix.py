import fileinput

def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""
    # Taken from: http://code.activestate.com/recipes/577586-converts-from-decimal-to-any-base-between-2-and-26/

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod >= 10)) + converted_string
    return converted_string

result = []
lines = []
for line in fileinput.input():
    line = line.rstrip()
    lines.append( line.split(",") )

for line in lines:
    try:
        mem = -1
        radix = int(line[1], 10)
        assert( radix <= 36 )
        assert( radix >= 2 )
        newradix = int(line[2], 10)
        assert( newradix <= 36 )
        assert( newradix >= 2 )
        mem = int(line[0], radix)
        newmem = base10toN( mem, newradix )
        print newmem.lower()
    except:
        print "Invalid Input"

print
