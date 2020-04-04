# Found this on stackoverflow. But now I can't find the question I got
# this code from. If you find it, please let me know and I will link to
# it here.
import difflib

def lcs(str1, str2):
    sm = difflib.SequenceMatcher()
    sm.set_seqs(str1, str2)
    matching_blocks = [ str1[m.a : m.a + m.size] for m in sm.get_matching_blocks() ]
    return "".join(matching_blocks)

print lcs('abacbdab', 'bdacba')
