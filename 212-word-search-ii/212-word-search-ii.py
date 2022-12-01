class Solution:
    def findWords(self, board, words):
        
        
        words_set = set()
        
        longest_length = 0
        for word in words:
            longest_length = max(longest_length, len(word))
        rows = len(board)
        columns = len(board[0])
        
        def backtrack(current_word, x, y, path):
            if x < 0 or x == rows or y <0 or y == columns:
                return
            if (x, y) in path:
                return
            else:
                path.add((x,y))
                current_word += board[x][y]
                words_set.add(current_word)
                if len(current_word) == longest_length:
                    path.remove((x,y))
                    return
                else:
                    backtrack(current_word, x + 1, y, path)
                    backtrack(current_word, x - 1, y, path)
                    backtrack(current_word, x, y + 1, path)
                    backtrack(current_word, x, y-1, path)
                    path.remove((x,y))
                
                # current_word = current_word[:-1]
                # path = path[:-1]
        for i in range(rows):
            for j in range(columns):
                backtrack("", i, j, set())
        res = []
        for word in words:
            if word in words_set:
                res.append(word)
        return res
        