# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pointer = dummy
        for i in range(n):
            pointer = pointer.next
        # print(pointer.val)
        start = dummy
        while pointer.next:
            pointer = pointer.next
            start = start.next
        # Now remove the next node of the start 
        start.next = start.next.next
        return dummy.next
            
        