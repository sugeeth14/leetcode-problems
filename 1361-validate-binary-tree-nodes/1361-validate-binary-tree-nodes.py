class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # first find the root(s)
        left_set = set(leftChild)
        right_set = set(rightChild)
        roots = []
        for i in range(n):
            if i not in left_set and i not in right_set:
                roots.append(i)
        if len(roots) != 1:
            return False
        root = roots[0]
        # Do traversal on root and find if you get any already visited
        visited = set()
        def backtrack(node):
            if node == -1:
                return True
            else:
                if node in visited:
                    return False
                visited.add(node)
                return backtrack(leftChild[node]) and backtrack(rightChild[node])
        has_no_cycle = backtrack(root)
        if has_no_cycle:
            return len(visited) == n
        else:
            return False
        