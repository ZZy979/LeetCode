class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        self.vals = preorder.split(',')
        self.i = 0
        return self.validate() and self.i == len(self.vals)
    
    def validate(self):
        if self.i >= len(self.vals):
            return False
        elif self.vals[self.i] == '#':
            self.i += 1
            return True
        else:
            self.i += 1
            return self.validate() and self.validate()
