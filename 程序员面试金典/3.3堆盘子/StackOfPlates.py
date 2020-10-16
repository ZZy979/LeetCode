class StackOfPlates:

    def __init__(self, cap: int):
        self.stacks = []
        self.cap = cap

    def push(self, val: int) -> None:
        if self.cap == 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.popAt(-1)

    def popAt(self, index: int) -> int:
        try:
            val = self.stacks[index].pop()
            if not self.stacks[index]:
                self.stacks.pop(index)
            return val
        except IndexError:
            return -1


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
