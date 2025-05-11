class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        n1, n2 = nums1.count(0), nums2.count(0)
        if n1 == 0 and s2 + n2 > s1 or n2 == 0 and s1 + n1 > s2:
            return -1
        return max(s1 + n1, s2 + n2)
