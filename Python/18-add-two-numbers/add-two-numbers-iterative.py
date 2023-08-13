from typing import Optional

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def get_next_digit(ln):
    """
    Gets the next digit in the ListNode. If at end of list,
    the next digit is a 0.

    :type ln: ListNode
    """
    return 0 if (ln == None) else ln.val

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    cur1 = l1
    cur2 = l2
    result = ListNode(0) # dummy node
    curresult = result
    carry = 0
    while (cur1 != None) or (cur2 != None) or (carry > 0):
        d1 = get_next_digit(cur1)
        d2 = get_next_digit(cur2)
        total = d1 + d2 + carry
        carry = total // 10
        newd = total % 10
        curresult.next = ListNode(newd)
        curresult = curresult.next
        if cur1 != None:
            cur1 = cur1.next
        if cur2 != None:
            cur2 = cur2.next
    return result.next

# TODO: Do test cases as unit tests

