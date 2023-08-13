from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    result = None
    if list1 and list2:
        if list1.val <= list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next
    elif list1:
        result = list1
        list1 = list1.next
    elif list2:
        result = list2
        list2 = list2.next
    else:
        # Both are None
        return None
    cur = result
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            cur = list1
            list1 = list1.next
        else:
            cur.next = list2
            cur = list2
            list2 = list2.next
    # At this point one of list1 and list2 are None:
    if list1:
        while list1:
            cur.next = list1
            cur = list1
            list1 = list1.next
    elif list2:
        while list2:
            cur.next = list2
            cur = list2
            list2 = list2.next
    return result

def test1():
    print("Running TEST 1:")
    list1 = None
    list2 = None
    expected = None
    result = mergeTwoLists(list1, list2)
    assert expected == result
    print("- TEST successful.")


if __name__ == "__main__":
    test1()
