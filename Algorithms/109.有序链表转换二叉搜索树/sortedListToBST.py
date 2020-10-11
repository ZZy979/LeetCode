# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        return self.create_tree(head, length)
    
    def create_tree(self, head, length):
        if length <= 0:
            return None
        m = head
        for i in range(length // 2):
            m = m.next
        root = TreeNode(m.val)
        root.left = self.create_tree(head, length // 2)
        root.right = self.create_tree(m.next, length - length // 2 - 1)
        return root
