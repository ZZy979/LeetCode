class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack_size = stackSize
        self.data = [None] * (3 * stackSize)
        self.size = [0] * 3

    def push(self, stackNum: int, value: int) -> None:
        if self.size[stackNum] < self.stack_size:
            self.data[stackNum * self.stack_size + self.size[stackNum]] = value
            self.size[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.size[stackNum] == 0:
            return -1
        else:
            self.size[stackNum] -= 1
            return self.data[stackNum * self.stack_size + self.size[stackNum]]

    def peek(self, stackNum: int) -> int:
        return -1 if self.size[stackNum] == 0 else self.data[stackNum * self.stack_size + self.size[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.size[stackNum] == 0


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
