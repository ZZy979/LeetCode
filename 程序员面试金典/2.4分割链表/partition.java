/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 创建一个新链表，将小于x的节点加入头部，大于等于x的节点加入尾部
class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null)
            return head;
        ListNode newHead = head, tail = head, p = head;
        while (p != null) {
            ListNode next = p.next;
            if (p.val < x) {
                p.next = newHead;
                newHead = p;
            }
            else {
                tail.next = p;
                tail = p;
            }
            p = next;
        }
        tail.next = null;
        return newHead;
    }
}
