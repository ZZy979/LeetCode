# 官方题解2：单调栈
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda p: (p[0], -p[1]))
        num_weak = 0
        stack = []
        for _, defense in properties:
            while stack and stack[-1] < defense:
                stack.pop()
                num_weak += 1
            stack.append(defense)
        return num_weak
