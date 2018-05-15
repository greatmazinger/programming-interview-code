import fileinput

"""
Look and say sequence: 
    To generate a member of the sequence from the previous member, read off the digits of the previous member.
    Analyzed by John Conway.
    from: https://en.wikipedia.org/wiki/Look-and-say_sequence
"""
if __name__ == "__main__":
    stdin = fileinput.input()
    num = int(stdin.next())
    print "--------------------------------------------------------------------------------"
    # TODO
