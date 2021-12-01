/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 递归版本
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        return addList(l1, l2, 0);
    }

    private ListNode addList(ListNode l1, ListNode l2, int carry) {
        if (l1 == null && l2 == null && carry == 0)
            return null;
        int x = l1 != null ? l1.val : 0;
        int y = l2 != null ? l2.val : 0;
        int s = x + y + carry;
        ListNode result = new ListNode(s % 10);
        result.next = addList(l1 != null ? l1.next : null, l2 != null ? l2.next : null, s / 10);
        return result;
    }

}
