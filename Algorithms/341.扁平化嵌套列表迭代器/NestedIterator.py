# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# 蠢。。
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = nestedList
        self.i = 0
        self._nested_iter = self._get_nested_iter()
        self._next_elem = self._get_next_elem()
    
    def _get_nested_iter(self):
        if self.i >= len(self.data) or self.data[self.i].isInteger():
            return None
        else:
            return NestedIterator(self.data[self.i].getList())
    
    def _get_next_elem(self):
        while self.i < len(self.data) and self._nested_iter and not self._nested_iter.hasNext():
            self.i += 1
            self._nested_iter = self._get_nested_iter()
        if self.i >= len(self.data):
            return None
        elif not self._nested_iter:
            ret = self.data[self.i].getInteger()
            self.i += 1
            self._nested_iter = self._get_nested_iter()
            return ret
        else:
            return self._nested_iter.next()
    
    def next(self) -> int:
        ret = self._next_elem
        self._next_elem = self._get_next_elem()
        return ret
    
    def hasNext(self) -> bool:
        return self._next_elem is not None

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
