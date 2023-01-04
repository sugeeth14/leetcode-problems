class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        count_array = []
        for i in range(len(tasks)):
            if i == 0:
                curr = 1
            else:
                if tasks[i-1] == tasks[i]:
                    curr += 1
                else:
                    count_array.append(curr)
                    curr = 1
        
        count_array.append(curr)
        result = 0
        # print(count_array)
        for num in count_array:
            if num == 1:
                result = -1
                break
            else:
                mod_value = num % 3
                if mod_value == 0:
                    result += (num//3)
                elif mod_value == 1:
                    result = result + (num//3) - 1
                    result += 2
                else:
                    result = result + (num//3)
                    result += 1
        return(result)
            
        