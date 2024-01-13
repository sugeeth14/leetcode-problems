class RandomizedSet:

    def __init__(self):
        self.numsMap = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.numsMap
        
        if res:
            # we must insert the element
            self.numsMap[val] = len(self.nums)
            self.nums.append(val)
        
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numsMap
        if res:
            # we must remove the element
            index = self.numsMap[val]
            lastVal = self.nums[len(self.nums) - 1]
            
            
            self.nums[index] = lastVal
            self.nums.pop()
            
            
            self.numsMap[lastVal] = index
            
            del self.numsMap[val]
            
        
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()