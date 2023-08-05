# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Algorithm
        # Maintain a queue along with the level, if level is less than depth - 1 keep adding its children to the queue
        # if level is equal to the depth
        # break out of the queue
        # Iterate the queue and for each element in the queue create a left child and a right child nodes with val
        # do pointer manipulations to append the new nodes 
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        queue = collections.deque()
        queue.append((root, 1))
        
        while queue:
            top_node, top_level = queue[0]
            if top_level == depth - 1:
                break
            else:
                top_node, top_level = queue.popleft()
                if top_node.left:
                    queue.append((top_node.left, top_level + 1))
                if top_node.right:
                    queue.append((top_node.right, top_level + 1))
        # now iterate over the items of the queue
        while queue:
            top, _ = queue.popleft()
            left = TreeNode(val)
            right = TreeNode(val)
            
            left.left = top.left
            right.right = top.right
            
            top.left = left
            top.right = right
        return root
        