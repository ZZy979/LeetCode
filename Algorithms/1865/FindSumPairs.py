from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.cnt2[self.nums2[index]] -= 1
        self.cnt2[self.nums2[index] + val] += 1
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        return sum(n * self.cnt2[tot - x] for x, n in self.cnt1.items())


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
