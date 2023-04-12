class Solution:
    def simplifyPath(self, path: str) -> str:

        path = path.split("/")
        from collections import deque


        result = deque()
        for i in range(1, len(path)):
            if path[i] == "":
                continue
            if path[i] == "..":
                if result:
                    result.pop()
            elif path[i] == ".":
                continue
            else:
                result.append(path[i])
        answer = "/" + "/".join(result)
        return (answer)


