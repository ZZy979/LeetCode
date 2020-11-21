# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法1：自顶向下归并排序
# 时间复杂度：O(nlog n)，空间复杂度：O(log n)
# 428 ms
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return merge_sort(head, None)


def merge_sort(head, tail):
    if not head:
        return head
    elif head.next is tail:
        head.next = None  # 注意这里！
        return head
    mid = find_mid(head, tail)
    return merge(merge_sort(head, mid), merge_sort(mid, tail))


def find_mid(head, tail):
    fast = slow = head
    while fast is not tail and fast.next is not tail:
        fast = fast.next.next
        slow = slow.next
    return slow


# 21.合并两个有序链表
def merge(l1, l2):
    p = result = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    p.next = l1 or l2
    return result.next
