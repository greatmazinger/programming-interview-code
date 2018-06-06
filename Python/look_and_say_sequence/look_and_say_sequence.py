import fileinput

"""
Look and say sequence: 
    To generate a member of the sequence from the previous member, read off the digits of the previous member.
    Analyzed by John Conway.
    The sequence starts out as:
        1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ....

    from: https://en.wikipedia.org/wiki/Look-and-say_sequence
"""

def get_next_run(seq = []):
    if len(seq) == 0:
        return None
    want = seq[0]
    cur = 1
    while cur < len(seq) and seq[cur] == want:
        cur += 1
    return (want, cur)

def get_next_sequence(seq = [], num = 0):
    if len(seq) == 0:
        return
    i = 0
    new_seq = []
    while i < len(seq):
        elem, count = get_next_run(seq[i:])
        # print "%d: %d - %d" % (i, elem, count)
        i += count
        new_seq.extend([ count, elem ])
    return new_seq

def print_look_and_say_sequence_up_to(num = 1):
    if num < 1:
        return
    # First sequence is the base case:
    i = 1
    seq = [1]
    print str(seq[0])
    i += 1
    while i <= num:
        new_seq = get_next_sequence(seq, i)
        print "".join([ str(x) for x in new_seq ])
        seq = new_seq
        i += 1

if __name__ == "__main__":
    stdin = fileinput.input()
    num = int(stdin.next())
    print "--------------------------------------------------------------------------------"
    print_look_and_say_sequence_up_to(num)
