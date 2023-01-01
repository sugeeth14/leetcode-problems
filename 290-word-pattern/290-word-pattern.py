class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_length = len(pattern)
        strings = s.split(" ")
        strings_length = len(strings)
        strings_dict = {}
        if pattern_length != strings_length:
            return False
        else:
            dic = {}
            for i in range(pattern_length):
                if pattern[i] in dic:
                    if strings[i] != dic[pattern[i]]:
                        return False
                else:
                    if strings[i] in strings_dict:
                        return False
                    strings_dict[strings[i]] = True
                    dic[pattern[i]] = strings[i]
            return True