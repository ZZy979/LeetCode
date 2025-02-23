import random

class Skiplist:
    MAX_LEVEL = 32

    def __init__(self):
        self.level = 0
        self.head = SkiplistNode(None, self.MAX_LEVEL)

    def random_level(self):
        level = 1
        while random.random() < 0.5:
            level += 1
        return min(level, self.MAX_LEVEL)

    def search(self, target: int) -> bool:
        p = self.head
        for i in range(self.level, -1, -1):
            while p.forward[i] and p.forward[i].value < target:
                p = p.forward[i]
        p = p.forward[0]
        return p is not None and p.value == target

    def find_node(self, target):
        update = [None] * (self.MAX_LEVEL + 1)
        p = self.head
        for i in range(self.level, -1, -1):
            while p.forward[i] and p.forward[i].value < target:
                p = p.forward[i]
            update[i] = p
        return p, update

    def add(self, num: int) -> None:
        _, update = self.find_node(num)
        insert_level = self.random_level()
        if insert_level > self.level:
            self.level = insert_level = self.level + 1
            update[self.level] = self.head

        new_node = SkiplistNode(num, insert_level)
        for i in range(insert_level, -1, -1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        p, update = self.find_node(num)
        p = p.forward[0]
        if not p or p.value != num:
            return False

        for i in range(self.level + 1):
            if update[i].forward[i] is not p:
                break
            update[i].forward[i] = p.forward[i]

        while self.level > 0 and self.head.forward[self.level] is None:
            self.level -= 1
        return True


class SkiplistNode:
    def __init__(self, value, level, next=None):
        self.value = value
        self.level = level
        self.forward = [next] * (level + 1)


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
