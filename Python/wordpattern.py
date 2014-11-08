# Complete the function below.
import re

def rec_wordpattern( pattern, input, words ):
    """Solves the wordpattern problem with a given dictionary of
    already assigned words (in the words dictionary)."""
    # Base cases for recursion
    if len(pattern) == 0 and len(input) == 0:
        # Trivial true case
        return 1
    if len(pattern) == 0 and len(input) > 0:
        # Used up the pattern, still some letters left in input
        return 0
    if len(pattern) > 0 and len(input) == 0:
        # Used up the words, still some letters left in pattern
        return 0
    nextpat = pattern[0]
    if nextpat in words:
        # already  have  an  assignment  for  this  pattern
        if re.match(words[nextpat], input):
            # Found  the  word.   Remove  it  and  recursively  call
            return rec_wordpattern( pattern[1:], input[len(words[nextpat]):], words )
            # The  backtracking  happens  in  the  previous  call
        else:
            return 0
    else:
        # create new word
        for index in xrange(1,len(input)):
            words[nextpat] = input[:index]
            if rec_wordpattern(pattern[1:], input[index:], words):
                # Success
                return 1
            else:
                # remove the assignment from nextpat and try again
                words.pop(nextpat, None)
    # If we got here, that means we failed
    return 0
    
# Assumption: Only the letter of the pattern matters, not the case.
# In other words:
#   "AAAA" is the same as "Aaaa" and "aaaa"
#
# The given test cases seem to be all lower case, but since the specification
# of the problem did not mention anything, I'm just coding for this.
def wordpattern( pattern, input):
    pattern = pattern.lower()
    return rec_wordpattern(pattern, input, {})
