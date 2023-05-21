class Solution:
    def defangIPaddr(self, address: str) -> str:
        points = address.split(".")
        return "[.]".join(points)
        