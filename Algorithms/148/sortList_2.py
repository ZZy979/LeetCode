# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 方法2：自底向上归并排序
# 时间复杂度：O(nlog n)，空间复杂度：O(1)
# 496 ms
class Solution:
    def sortList(self, head: ListNode) -> ListNode:  
        if not head:
            return head
        
        length = length_of_list(head)
        new_head = ListNode(0, head)
        sub_length = 1
        while sub_length < length:
            prev, cur = new_head, new_head.next
            while cur:
                head1 = cur
                head2 = cut(head1, sub_length)
                succ = cut(head2, sub_length) if head2 else None
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                cur = succ
            sub_length *= 2
        return new_head.next


def length_of_list(head):
    length = 0
    p = head
    while p:
        length += 1
        p = p.next
    return length


def cut(head, sub_length):
    for i in range(sub_length - 1):
        if head.next:
            head = head.next
        else:
            break
    head_next = head.next
    head.next = None
    return head_next


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
