# 方法二：滑动窗口
# 时间复杂度O(nC)，空间复杂度O(C)，其中C=6
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = [0] * 30  # bits[i]表示第i个二进制位为1的元素个数
        ans = 0xFFFFFFFF
        left = 0
        for right in range(len(nums)):
            add(bits, nums[right])
            while left <= right and calc(bits) >= k:
                ans = min(ans, right - left + 1)
                sub(bits, nums[left])
                left += 1
        return ans if ans != 0xFFFFFFFF else -1

def calc(bits):
    return sum(1 << i for i in range(len(bits)) if bits[i])

def add(bits, num):
    for i in range(len(bits)):
        bits[i] += (num >> i) & 1

def sub(bits, num):
    for i in range(len(bits)):
        bits[i] -= (num >> i) & 1
