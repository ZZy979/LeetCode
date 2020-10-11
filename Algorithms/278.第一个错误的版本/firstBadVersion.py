# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binsearch(1, n + 1)
    
    def binsearch(self, left, right):
        if right == left:
            return left
        mid = (left + right) // 2
        if isBadVersion(mid):
            return self.binsearch(left, mid)
        else:
            return self.binsearch(mid + 1, right)
