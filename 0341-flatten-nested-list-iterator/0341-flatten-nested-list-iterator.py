# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # print(nestedList[1]._integer)
        self.res = []
        # print(nestedList)
        
        def backtrack(current):
            # print(current)
            if type(current) == int:
                self.res.append(current)
                return
            elif type(current) == list:
                for item in current:
                    backtrack(item)
            elif not current:
                return
            else:
                backtrack(current._integer)
                backtrack(current._list)
        backtrack(nestedList)
        # print(self.res)
        self.pointer = -1
        
    
    def next(self) -> int:
        self.pointer += 1
        return self.res[self.pointer]
        
    
    def hasNext(self) -> bool:
        if self.pointer == len(self.res) - 1:
            return False
        return True
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())