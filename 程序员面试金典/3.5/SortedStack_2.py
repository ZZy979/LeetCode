# 没必要每次push完后都把所有元素压回主栈，这样连续push时耗时会大大减少
class SortedStack:

    def __init__(self):
        self.main_stack = []
        self.sub_stack = []

    def push(self, val: int) -> None:
        while self.main_stack and self.main_stack[-1] < val:
            self.sub_stack.append(self.main_stack.pop())
        while self.sub_stack and self.sub_stack[-1] > val:
            self.main_stack.append(self.sub_stack.pop())
        self.main_stack.append(val)

    def pop(self) -> None:
        self.sub_to_main()
        if self.main_stack:
            self.main_stack.pop()

    def peek(self) -> int:
        self.sub_to_main()
        return self.main_stack[-1] if self.main_stack else -1

    def isEmpty(self) -> bool:
        self.sub_to_main()
        return len(self.main_stack) == 0

    def sub_to_main(self):
        while self.sub_stack:
            self.main_stack.append(self.sub_stack.pop())


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
