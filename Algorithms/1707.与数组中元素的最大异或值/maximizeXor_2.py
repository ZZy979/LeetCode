# 评论区解法，1924 ms
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        n, q = len(nums), len(queries)
        ans = [0] * q
        for i in range(q):
            x, m = queries[i]
            # edge cases
            if m < nums[0]: 
                ans[i] = -1
                continue
            elif m == 0:
                ans[i] = x
                continue
            # align the digits of binary strings
            dm = len(bin(m)) - 2
            xb = bin(x)[2:]
            mb = bin(m)[2:]
            if dm > len(xb):
                xb = '0' * (dm - len(xb)) + xb
            else:
                xb = xb[-dm:]
            # binary search
            base = 0
            lb, rb = nums[0], nums[bisect_right(nums, m) - 1] 
            inv = 1 << len(mb)  # length of interval
            d = -1
            while lb != rb:
                inv >>= 1
                d += 1
                if xb[d] == '1':  # need 0
                    if lb >= base + inv:  # miss
                        base += inv
                        continue
                    idx = bisect_left(nums, min(base + inv, rb + 1)) - 1  # maximum number smaller than min(base + inv, rb + 1)
                    rb = nums[idx]  # update rb
                else:  # need 1
                    if rb < base + inv:
                        continue
                    idx = bisect_left(nums, max(base + inv, lb))  # maximum number greater than min(base + inv, lb)
                    lb = nums[idx]
                    base += inv    
            ans[i] = x ^ lb
        return ans
