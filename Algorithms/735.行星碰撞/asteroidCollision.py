class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack and 0 < stack[-1] < -x:
                    stack.pop()
                if stack and stack[-1] > 0:
                    if stack[-1] == -x:
                        stack.pop()
                else:
                    stack.append(x)
        return stack
