/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null)
            return true;
        int length = lengthOfList(head);
        Stack<Integer> stack = new Stack<>();
        ListNode p = head;
        for (int i = 0; i < length / 2; ++i) {
            stack.push(p.val);
            p = p.next;
        }
        if (length % 2 == 1)
            p = p.next;
        for (int i = 0; i < length / 2; ++i) {
            if (p.val != stack.pop())
                return false;
            p = p.next;
        }
        return true;
    }

    private int lengthOfList(ListNode head) {
        int length = 0;
        while (head != null) {
            ++length;
            head = head.next;
        }
        return length;
    }

}
