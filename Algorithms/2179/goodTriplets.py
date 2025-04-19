from sortedcontainers import SortedList

# 评论区解法：有序集合，时间复杂度O(nlog n)，空间复杂度O(n)
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        idx_of_nums1 = {v: i for i, v in enumerate(nums1)}
        ranks = [idx_of_nums1[v] for v in nums2]  # ranks[i]为nums2[i]在nums1中的位置
        n = len(nums1)
        result = 0
        buf = SortedList()  # 排序后的ranks[:j]
        # 遍历好三元组的中间元素在nums2中的下标
        for j in range(n):
            idx = buf.bisect_left(ranks[j])
            left_cnt = idx
            right_cnt = n - 1 - ranks[j] - (len(buf) - idx)  # nums1中位于nums2[j]右侧的元素个数减去这些元素在nums2中位于nums2[j]左侧的元素个数
            result += left_cnt * right_cnt
            buf.add(ranks[j])
        return result
