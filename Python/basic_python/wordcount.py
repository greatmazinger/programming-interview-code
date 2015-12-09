import sys
# Need sys for command line argument processing
import os
# Lots of important functionality in os. Most importantly
# for us is the processing of files

def split_into_words( line ):
    words = []
    return words

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
    with open(filename, "rb") as filehandle:
        # "rb" means
        #  r - read mode
        #  b - binary mode. Don't worry too much about this, but
        #      you almost always want binary mode.
        for line in filehandle:
            print line
            words = split_into_words( line )
            print words

if __name__ == "__main__":
    main()
