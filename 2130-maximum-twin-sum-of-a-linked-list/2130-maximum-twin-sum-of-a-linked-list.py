# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes = []
        ptr = head
        while ptr:
            nodes.append(ptr.val)
            ptr = ptr.next
        
        max_sum = 0
        for i in range(len(nodes)//2):
            current_sum = nodes[i] + nodes[len(nodes) - 1 - i]
            max_sum = max(current_sum, max_sum)
        return max_sum
            
        