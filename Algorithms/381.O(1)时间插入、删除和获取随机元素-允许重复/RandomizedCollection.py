import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.element = []
        self.val2indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.element.append(val)
        self.val2indices[val].add(len(self.element) - 1)
        return len(self.val2indices[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.val2indices:
            return False
        last_element = self.element[-1]
        self.val2indices[last_element].remove(len(self.element) - 1)
        if val != last_element:
            index = next(iter(self.val2indices[val]))
            self.element[index] = last_element
            self.val2indices[val].remove(index)
            self.val2indices[last_element].add(index)
        if not self.val2indices[val]:
            del self.val2indices[val]
        self.element.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.element)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
