/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 使用散列表，时间复杂度O(n)，空间复杂度O(n)
class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        Set<Integer> seen = new HashSet<>();
        ListNode prev = null, p = head;
        while (p != null) {
            if (seen.contains(p.val))
                prev.next = p.next;
            else {
                seen.add(p.val);
                prev = p;
            }
            p = p.next;
        }
        return head;
    }
}
