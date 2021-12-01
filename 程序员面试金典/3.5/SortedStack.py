class SortedStack:

    def __init__(self):
        self.main_stack = []
        self.sub_stack = []

    def push(self, val: int) -> None:
        while self.main_stack and self.main_stack[-1] < val:
            self.sub_stack.append(self.main_stack.pop())
        self.main_stack.append(val)
        while self.sub_stack:
            self.main_stack.append(self.sub_stack.pop())

    def pop(self) -> None:
        if self.main_stack:
            self.main_stack.pop()

    def peek(self) -> int:
        return self.main_stack[-1] if self.main_stack else -1

    def isEmpty(self) -> bool:
        return len(self.main_stack) == 0


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
