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

def reverse( words ):
    if len(words) == 0:
        return []
    myword = get_next_word( words )
    result = []
    result.extend( reverse( words ) )
    result.extend( myword )
    return result

words = []
words.extend( x for x in "I do not like them in a house I do not like them with a mouse    " )
print "Original:"
print words
print "Reversed:"
revwords = reverse(words)
print "   as list:"
print revwords
print "   as string:"
print "".join( x for x in revwords )
