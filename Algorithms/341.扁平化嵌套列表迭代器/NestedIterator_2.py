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

# 评论区解法：生成器
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.iter = self._build_generator(nestedList)
    
    def _build_generator(self, nestedList):
        for x in nestedList:
            if x.isInteger():
                yield x.getInteger()
            else:
                yield from self._build_generator(x.getList())
    
    def next(self) -> int:
        return self.v
    
    def hasNext(self) -> bool:
        try:
            self.v = next(self.iter)
            return True
        except StopIteration:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
