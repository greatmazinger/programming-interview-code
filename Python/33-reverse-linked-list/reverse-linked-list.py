# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeHead(self, head: ListNode):
        new_head = head.next
        head.next = None
        return new_head, head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        revhead = None
        head, revhead = self.removeHead(head)
        while head != None:
            head, node = self.removeHead(head)
            node.next = revhead
            revhead = node
        return revhead
