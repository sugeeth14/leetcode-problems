class RandomizedSet:

    def __init__(self):
        self.int_to_val = {}
        self.val_to_int = {}
        self.current_size = 0
        
        

    def insert(self, val: int) -> bool:
        # check if val is present
        if val in self.val_to_int:
            return False
        # Insert the element
        self.int_to_val[self.current_size] = val
        self.val_to_int[val] = self.current_size
        self.current_size += 1
        # print("insert")
        # print(self.val_to_int)
        # print(self.int_to_val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.val_to_int:
            return False
        # Remove the element.
        if len(self.int_to_val) == 1:
            self.int_to_val = {}
            self.val_to_int = {}
            self.current_size = 0
        elif self.val_to_int[val] == self.current_size - 1:
            del self.val_to_int[val]
            del self.int_to_val[self.current_size - 1]
            self.current_size -= 1
        else:
            current_index = self.val_to_int[val]
            del(self.val_to_int[val])
            # Mark the last element to current_index
            self.int_to_val[current_index] = self.int_to_val[self.current_size - 1]

            last_val = self.int_to_val[self.current_size - 1]
            del(self.int_to_val[self.current_size - 1])
            # set the last val index to current index
            self.val_to_int[last_val] = current_index
            self.current_size -= 1
            # print(self.int_to_val)
            # print(self.val_to_int)
        return True
        
    def getRandom(self) -> int:
        val = random.randint(0, self.current_size-1)
        # print(self.val_to_int)
        # print(self.int_to_val)
        return self.int_to_val[val]
    
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()