from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#     def hasCycleUseSpace(head: Optional[ListNode]) -> bool:
#         cur = head
#         i = 0
#         seen = {}
#         while cur != None and cur not in seen:
#             seen[cur] = i
#             cur = cur.next
#             i += 1
#         return cur in seen
#
#     def hasCycleOverwriteValue(head: Optional[ListNode]) -> bool:
#         cur = head
#         i = 0
#         while cur != None and cur.val != None:
#             cur.val = None
#             cur = cur.next
#         if cur == None:
#             return False
#         return cur.val == None

def hasCycle(head: Optional[ListNode]) -> bool:
    cur = head
    i = 0
    if cur == None:
        return False
    cur.seen = False
    while True:
        if cur == None:
            return False
        if hasattr(cur, "seen") and cur.seen:
            return True
        cur.seen = True
        cur = cur.next

def create_linked_list(llist: List[ListNode]):
    # TODO: Pass in array.
    #       Use array, but return only head node
    llist = [1, 2, 3, -4]
    pos = -1
    node = None
    head = None
    for val in llist:
        newnode = ListNode(val)
        if head == None:
            head = newnode
        if node is not None:
            node.next = newnode
        node = newnode
    if node is not None:
        node.next = pos
    cur = head
    while cur != None:
        print(f"DBG: val={cur.val}, next={str(cur.next)}")
        cur = cur.next

def test01():
    assert True

if __name__ == "__main__":
    test01()
