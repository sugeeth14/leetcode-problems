# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        if l == r:
            return l
        while l < r:
            mid = (l + r)//2
            if isBadVersion(mid):
                if mid-1 >=1:
                    if not isBadVersion(mid - 1):
                        # print("returning from here")
                        return mid
                r = mid
            else:
                l = mid
                if mid + 1 <=n:
                    if isBadVersion(mid + 1):
                        # print("eee")
                        return mid + 1
        return mid
            