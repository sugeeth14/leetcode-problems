# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        nodes = []
        ptr = head
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        # print(nodes)
        nodes[k-1], nodes[len(nodes) - k] = nodes[len(nodes) - k], nodes[k-1]
        
        # for node in nodes:
        #     print(node.val)
        dummy_head = ListNode()
        ptr = dummy_head
        for node in nodes:
            ptr.next = node
            ptr = node
        ptr.next = None
        return dummy_head.next
        