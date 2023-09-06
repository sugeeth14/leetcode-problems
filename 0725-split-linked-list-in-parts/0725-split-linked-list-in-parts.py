# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ptr = head
        count = 0
        while ptr:
            count += 1
            ptr = ptr.next
        # print(count)
        extra = count % k
        actual = count // k
        ptr = head
        res = []
        # print(actual, extra)
        while ptr:
            new_head = ListNode()
            current = new_head
            for i in range(actual):
                current.next = ptr
                current = current.next
                ptr = ptr.next
            
            if extra:
                current.next = ptr
                current = current.next
                ptr = ptr.next
                extra -= 1
            current.next = None
            res.append(new_head.next)
            # print(res)
        diff = k - len(res)
        for i in range(diff):
            res.append(None)
        return res
            
                
            
        