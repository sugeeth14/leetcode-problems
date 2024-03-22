/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverse(node *ListNode) *ListNode {
    if node == nil || node.Next == nil {
        return node
    }
    prev := node
    nxt := node.Next
    prev.Next = nil
    
    for nxt != nil {
        temp := nxt.Next
        nxt.Next = prev
        prev = nxt
        nxt = temp
    }
    return prev
    
}
func isPalindrome(head *ListNode) bool {
    /*
    Algorithm for O(n) time and O(1) space:
    1. Find the middle of the linked list
    2. Take the list from middle as the head and make it the second list.
    3. Reverse the second list
    4. Iterate and compare the two lists node by node.
    5. Return if they are equal or not.
    */
    
    // Count the number of nodes
    ptr := head
    nodes := 0
    for ptr != nil {
        nodes++
        ptr = ptr.Next
    }
    if nodes == 1{
        return true
    }
    ptr1 := head
    ptr2 := head
    if nodes % 2 == 0 {
        // The number of nodes are even and middle would be nodes / 2
        for range nodes/2 {
            ptr2 = ptr2.Next
        }
        
    } else {
        // The number of nodes are odd
        for range (nodes/2) + 1 {
            ptr2 = ptr2.Next
        }
    }
    ptr2 = reverse(ptr2)
    
    for ptr1 != nil && ptr2 != nil {
        if ptr1.Val != ptr2.Val {
            return false
        }
        ptr1 = ptr1.Next
        ptr2 = ptr2.Next
    }
    return true
    
    
}