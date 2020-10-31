import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.element = []
        self.val2index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2index:
            return False
        self.element.append(val)
        self.val2index[val] = len(self.element) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2index:
            return False
        last_element = self.element[-1]
        index = self.val2index[val]
        self.element[index] = last_element
        self.element.pop()
        self.val2index[last_element] = index
        del self.val2index[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.element)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
