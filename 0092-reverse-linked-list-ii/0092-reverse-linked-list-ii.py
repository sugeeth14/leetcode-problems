# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
    
        if not head:
            return None
        
        if left == right:
            return head
        dummy = ListNode()
        tail = dummy
        ptr = head
        count = 0
        left_ptr = None
        while ptr:
            count += 1
            if count + 1 == left:
                left_ptr = ptr
            if count >= left and count <= right:
                tail.next = ptr
                tail = tail.next
            ptr = ptr.next
        last_ptr = tail.next
        tail.next = None
        # print(left_ptr)
        if left_ptr:
            left_ptr.next = self.reverse_list(dummy.next,last_ptr)
            # print(dummy)
            return (head)
        else:
            return self.reverse_list(dummy.next,last_ptr)
        # print(last_ptr)
            
    def reverse_list(self, list_node, last_ptr):
        prev = last_ptr
        curr = list_node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        list_node = prev
        return (list_node)