class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        start = 0
        end = 0
        while end < len(chars):
            if chars[start] == chars[end]:
                end += 1
            else:
                # in this case we have to append
                if start +1 == end:
                    # just append the character
                    chars[insert] = chars[start]
                    insert += 1
                else:
                    # insert the number as well
                    diff = end - start
                    diff = str(diff)
                    chars[insert] = chars[start]
                    insert += 1
                    for i in range(len(diff)):
                        chars[insert] = diff[i]
                        insert += 1
                # since we have appended update start
                # end += 1
                start = end
        #add the last character
        # print(start, end, insert)
        if start + 1== end:
            # just append the character
            chars[insert] = chars[start]
            insert += 1
        else:
            diff = end - start
            diff = str(diff)
            chars[insert] = chars[start]
            insert += 1
            for i in range(len(diff)):
                chars[insert] = diff[i]
                insert += 1
        # print(chars)
        return insert
        
        