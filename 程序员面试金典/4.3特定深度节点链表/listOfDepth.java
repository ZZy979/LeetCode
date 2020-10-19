/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

// 前序遍历
class Solution {
    private List<ListNode> firsts = new ArrayList<>();
    private List<ListNode> lasts = new ArrayList<>();

    public ListNode[] listOfDepth(TreeNode tree) {
        createLevelList(tree, 0);
        return firsts.toArray(new ListNode[0]);
    }

    private void createLevelList(TreeNode root, int level) {
        if (root == null)
            return;
        if (lasts.size() == level) {
            ListNode node = new ListNode(root.val);
            firsts.add(node);
            lasts.add(node);
        }
        else {
            ListNode node = lasts.get(level);
            node.next = new ListNode(root.val);
            lasts.set(level, node.next);
        }
        createLevelList(root.left, level + 1);
        createLevelList(root.right, level + 1);
    }

}
