# A pangram is a sentence that uses every letter of the  alphabet at least once.
# Assuming the English alphabet (26 letters), this checks to see if the
# word supplied is a pangram.
import fileinput
import re

stdin = fileinput.input()
sentence = stdin.next()

letters = re.sub("[^a-zA-Z]", "", sentence)
print letters
letters = set(letters.lower())
if len(letters) == 26:
    print "pangram"
else:
    print "not pangram"
