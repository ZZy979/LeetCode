/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 两重循环，时间复杂度O(n^2)，空间复杂度O(1)
class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        ListNode p = head;
        while (p != null) {
            ListNode q = p;
            while (q.next != null)
                if (q.next.val == p.val)
                    q.next = q.next.next;
                else
                    q = q.next;
            p = p.next;
        }
        return head;
    }
}
