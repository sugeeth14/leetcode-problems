# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        def reverse(node):
            if not node or not node.next:
                return node
            prev = node
            nxt = node.next
            prev.next = None
            
            while nxt:
                temp = nxt.next
                nxt.next = prev
                prev = nxt
                nxt = temp
                # print(nxt, prev)
            return prev
        
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        
        ptr1 = head
        ptr2 = head
        for i in range((count+1)//2):
            ptr2 = ptr2.next
        ptr2 = reverse(ptr2)
        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True