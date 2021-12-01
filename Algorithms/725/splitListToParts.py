# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        vhead = ListNode(0, head)
        n = calc_length(vhead)
        q, r = divmod(n, k)
        ans = []
        for _ in range(r):
            ans.append(split(vhead, q + 1))
        for _ in range(k - r):
            ans.append(split(vhead, q))
        return ans


def calc_length(vhead):
    length = 0
    while vhead.next is not None:
        length += 1
        vhead = vhead.next
    return length


def split(vhead, m):
    if m == 0:
        return None
    sub_head, p = vhead.next, vhead
    for _ in range(m):
        p = p.next
    vhead.next, p.next = p.next, None
    return sub_head
