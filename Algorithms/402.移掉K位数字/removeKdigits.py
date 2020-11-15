# 官方题解：贪心+单调栈
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_stack = ['0']
        # 构建单调递增的数字串
        for digit in num:
            while k and num_stack[-1] > digit:
                num_stack.pop()
                k -= 1
            num_stack.append(digit)
        # 如果k > 0，删除末尾的k个字符
        num_stack = num_stack[:-k] if k else num_stack
        return ''.join(num_stack).lstrip('0') or '0'
