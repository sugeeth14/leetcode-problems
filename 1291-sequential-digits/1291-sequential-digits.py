class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        '''
        1. Get two digits of low and high
        2. Initialize starting string with 1..9
        3. Iterate over each of digit from low to high
        4. Construct a starting int. 
        5. Iterate 10 - number of digits times and keep adding 111 before adding, check if the current number is present in between low and high
        6. If so add to the result
        '''
        
        base_string = "123456789"
        
        def find_digits(num):
            return len(str(num))
        
        low_digits = find_digits(low)
        high_digits = find_digits(high)
        
        ans = []
        
        for digit in range(low_digits, high_digits + 1):
            current = int(base_string[:digit])
            add_number = int("1" * digit)
            for i in range(10 - digit):
                if low <= current <= high:
                    ans.append(current)
                current = current + add_number
        return ans
            
            
        