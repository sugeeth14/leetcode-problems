# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from collections import deque
        
        stack = deque()
        
        while head:
            stack.append(head)
            head = head.next
        if len(stack) % 2 == 0:
            return stack[len(stack)//2]
        else:
            return stack[len(stack)//2]
        
        