from typing import List, Optional

class ListNode(object):
    def __init__(self, val, nextptr = None):
        self.val = val
        self.next = nextptr

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode], carry: Optional[int] = 0) -> Optional[ListNode]:
    if l1 is None and l2 is None:
        return None if carry == 0 else ListNode(carry)
    val1 = l1.val if l1 is not None else 0
    val2 = l2.val if l2 is not None else 0
    value = val1 + val2 + carry
    if value > 9:
        value %= 10
        new_carry = 1
    else:
        new_carry = 0
    rest = addTwoNumbers(
        l1.next if l1 else None,
        l2.next if l2 else None,
        new_carry
    )
    return ListNode(value, rest)

def create_linked_list(l: List) -> Optional[ListNode]:
    if len(l) == 0:
        return None
    dummy = ListNode(0)
    cur = dummy
    for x in l:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def verify(expected, result):
    while expected != None:
        assert result != None
        assert expected.val == result.val
        expected = expected.next
        result = result.next
    assert expected == None
    assert result == None

def list_to_str(l):
    if l == None:
        print("<NONE>")
    result = []
    while l != None:
        result.append(str(l.val))
        l = l.next
    return "".join(result)

def test1():
    print("Running TEST 1:")
    l1 = create_linked_list([1, 2, 3])
    l2 = create_linked_list([4, 5, 6])
    expected = create_linked_list([5, 7, 9])
    result = addTwoNumbers(l1, l2)
    verify(expected, result)
    print("- TEST 1 successful.")

def test2():
    print("Running TEST 2:")
    l1 = create_linked_list([9])
    l2 = create_linked_list([9])
    expected = create_linked_list([8, 1])
    result = addTwoNumbers(l1, l2)
    verify(expected, result)
    print("- TEST 2 successful.")

if __name__ == "__main__":
    test1()
    test2()
