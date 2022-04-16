# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# 自顶向下语法分析
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        self.s, self.i = s, 0
        # E -> integer | L
        # L -> [ A ]
        # A -> E | E , A
        return self.nested_integer()
    
    @property
    def c(self):
        return self.s[self.i]
    
    def nested_integer(self):
        return self.integer() if self.c.isdigit() or self.c == '-' else self.nested_list()
    
    def integer(self):
        j = self.i
        if self.c == '-':
            j += 1
        while j < len(self.s) and self.s[j].isdigit():
            j += 1
        integer = NestedInteger(int(self.s[self.i:j]))
        self.i = j
        return integer
    
    def nested_list(self):
        self.i += 1  # '['
        nested_list = NestedInteger()
        while self.c != ']':
            nested_list.add(self.nested_integer())
            if self.s[self.i] == ',':
                self.i += 1  # ','
        self.i += 1  # ']'
        return nested_list
