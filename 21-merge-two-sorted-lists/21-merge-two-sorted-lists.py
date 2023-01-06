# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        list2 = []
        
        if l1 != None:
        
            while(l1.next != None):
                # print(l1.val)
                list1.append(l1.val)
                l1 = l1.next
                # list1.append(l1.val)
            list1.append(l1.val)
        if l2 != None:
            while(l2.next != None):
                list2.append(l2.val)
                l2 = l2.next

            list2.append(l2.val)
        
        final_list = sorted(list1 + list2)
        
        for i, element in enumerate(final_list):
            final_list[i] = ListNode(element, None)      
        
        for i in range(len(final_list) -1, 0, -1):
            final_list[i-1].next = final_list[i]
        if l1 == None and l2 == None:
            return None
        return final_list[0]
        
            
        