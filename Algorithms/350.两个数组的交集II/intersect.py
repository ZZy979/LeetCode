from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        res = []
        for x in c1:
            for n in range(min(c1[x], c2[x])):
                res.append(x)
        return res
