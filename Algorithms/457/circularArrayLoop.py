# 官方题解：快慢指针
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i):
            return (i + nums[i]) % n
        
        for i, d in enumerate(nums):
            if d == 0:
                break
            slow, fast = i, nxt(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[nxt(fast)] > 0:
                if slow == fast:
                    if slow == nxt(slow):
                        break
                    return True
                slow = nxt(slow)
                fast = nxt(nxt(fast))
            j = i
            while nums[j] * nums[nxt(j)] > 0:
                tmp, j = j, nxt(j)
                nums[tmp] = 0
        return False
