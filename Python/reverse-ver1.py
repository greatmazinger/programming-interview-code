def get_next_word( words ):
   # Either gets the next alpha-word, or set of spaces
    if len(words) == 0:
        return []
    elif words[0] == " ":
        # spaces
        result = []
        while len(words) > 0 and words[0] == " ":
            result.append( words.pop(0) )
    else:
        # Not space
        result = []
        while len(words) > 0 and words[0] != " ":
            result.append( words.pop(0) )
    return result           

# Recursive reverse
def reverse( words ):
    if len(words) == 0:
        return []
    myword = get_next_word( words )
    result = []
    result.extend( reverse( words ) )
    result.extend( myword )
    return result

def reverse_iterative( words ):
    if len(words) == 0:
        return []
    total = len(words)
    result = []
    seen = 0
    while seen < total:
        myword = get_next_word( words )
        seen = seen + len(myword)
        myword.extend( result )
        result = myword
    return result

words = []
words.extend( x for x in "I do not like them in a house I do not like them with a mouse    " )
print "Original:"
print words
print "============================================================"
print "Reverse using recursive version:"
revwords = reverse(words)
print "   as list:"
print revwords
print "   as string:"
print "".join( x for x in revwords )
print "============================================================"
print "Original:"
words.extend( x for x in "I do not like them in a house I do not like them with a mouse    " )
print words
print "Reverse using iterative version:"
revwords2 = reverse_iterative(words)
print "   as list:"
print revwords2
print "   as string:"
print "".join( x for x in revwords2 )
