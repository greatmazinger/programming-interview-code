import sys
# Need sys for command line argument processing
import os
# Lots of important functionality in os. Most importantly
# for us is the processing of files
from collections import defaultdict

def split_into_words( line ):
    line = line.rstrip("\n")
    words = line.split(" ")
    return words

def clean_words( words ):
    result = []
    for w in words:
        # Convert everything to lower case
        w = w.lower()
        # Remove all(?) punctuation marks
        w = w.replace( ".", "" )
        w = w.replace( ",", "" )
        w = w.replace( "_", "" )
        w = w.replace( ";", "" )
        w = w.replace( ":", "" )
        result.append( w )
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
    counter = defaultdict( int )
    with open(filename, "rb") as filehandle:
        # "rb" means
        #  r - read mode
        #  b - binary mode. Don't worry too much about this, but
        #      you almost always want binary mode.
        for line in filehandle:
            words = split_into_words( line )
            words = clean_words( words )
            for x in words:
                counter[x] = counter[x] + 1
        for k, v in counter.iteritems():
            print k, "->", v

if __name__ == "__main__":
    main()
