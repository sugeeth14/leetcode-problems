# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        nums = set(nums)
        
        ptr = head
        ptr2 = dummy
        
        while ptr:
            if ptr.val in nums:
                # do nothing
                ptr = ptr.next
            else:
                node = ptr
                nxt = node.next
                ptr = nxt
                node.next = None
                ptr2.next = node
                ptr2 = node
        return dummy.next
                
        