class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1:
            return True
        root = postorder[-1]
        split = 0
        while postorder[split] < root:
            split += 1
        return all(v > root for v in postorder[split:-1]) and self.verifyPostorder(postorder[:split]) and self.verifyPostorder(postorder[split:-1])
