class TrieNode:
    def __init__(self):
        self.children = {}
        self.islast = False
    
    def insert(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.islast = True
    
    def delete(self, word):
        # Here we must recursively delete the word
        
        def backtrack(cur, index):
            if index == len(word):
                # If this is the last character delete the node
                cur.islast = False
                return
            else:
                backtrack(cur.children[word[index]], index + 1)
                if len(cur.children[word[index]].children) == 0:
                    del cur.children[word[index]]
        backtrack(self, 0)
                
            
                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.root = TrieNode()
        for word in words:
            self.root.insert(word)
        
        
        rows = len(board)
        cols = len(board[0])
        
        res = set()
        visit = set()
        
        def dfs(i, j, node, word):
            if i < 0 or i == rows or j < 0 or j == cols:
                return
            if (i, j) in visit:
                return
            if board[i][j] not in node.children:
                return
            
            visit.add((i, j))
            word += board[i][j]
            node = node.children[word[-1]]
            if node.islast:
                res.add(word)
                self.root.delete(word)
            dfs(i-1, j, node, word)
            dfs(i + 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            
            
            visit.remove((i, j))
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, self.root, "")
        return list(res)
        