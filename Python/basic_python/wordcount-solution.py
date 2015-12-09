# CS League of Learning:  Programming for non-programmers - Python 2
# 12/9/2015
# author: Raoul Veroy

import sys
# Need sys for command line argument processing
import os
# Lots of important functionality in os. We use it to check if the 
# file exists.
from collections import defaultdict
# Used to make counting easier

def split_into_words( line ):
    """
    Takes a line, and returns a list of words diving on space.
    """
    words = []  # same as list()
    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        if word == '':
            continue
        words.append( word )
    return words
    # Next level: do this with list comprehensions

def clean_words( words ):
    """
    Takes a list of words (possibly with punctuation and upper case)
    and returns a list of words without punctuation, everything lower case.
    Note that numbers are considered valid words.
    """
    result = []
    for w in words:
        # Remove punctuation marks
        w = w.replace( ".", "" )
        w = w.replace( ",", "" )
        w = w.replace( "_", "" )
        w = w.replace( "?", "" )
        w = w.replace( ":", "" )
        w = w.replace( "[", "" )
        w = w.replace( "]", "" )
        # Next level: refactor out into a function that uses loops
        # Check to see if the word was all punctation marks 
        if len(w) == 0:
            continue
            # Because we don't want to add an empty string
        # Lower case
        w = w.lower()
        result.append(w)
    # To lower case
    return result

def main():
    print "Running", sys.argv[0]
    if len(sys.argv) < 2:
        filename = "part7.txt"
        print "Using hardcoded test file: %s" % filename
    else:
        filename = sys.argv[1]
        print "Using supplied file: %s" % filename
    # Note: sys.argv[0] is always the program filename
    if not os.path.isfile(filename):
        print "File %s not found." % filename
        exit(2)
    # Version 1
    # counter = {}
    counter = defaultdict( int )
    with open(filename, "rb") as filehandle:
        # "rb" means
        #  r - read mode
        #  b - binary mode. Don't worry too much about this, but
        #      you almost always want binary mode.
        for line in filehandle:
            words = split_into_words( line )
            if len(words) == 0:
                continue
            words = clean_words( words )
            # count them
            # Version 1
            # for w in words:
            #     if w in counter:
            #         counter[w] = counter[w] + 1
            #         # same as
            #         # counter[w] += 1
            #     else:
            #         counter[w] = 1
            # Version 2 with defaultdict
            for w in words:
                counter[w] += 1
            # Version 3 using collections.Counter
            # Added if there's time
    print "WORD COUNT:"
    for word, value in counter.iteritems():
        print "%s -> %d" % (word, value)
    # Possible options:
    # 1. Get top 10 list
    # 2. How do you sort based on count
    # 3. Simplify code using list comprehensions

if __name__ == "__main__":
    main()
