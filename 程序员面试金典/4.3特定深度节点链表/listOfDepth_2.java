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

// 层序遍历
class Solution {
    public ListNode[] listOfDepth(TreeNode tree) {
        if (tree == null)
            return new ListNode[0];
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(tree);
        List<ListNode> res = new ArrayList<>();
        ListNode dummyNode = new ListNode(0);
        while (!queue.isEmpty()) {
            ListNode cur = dummyNode;
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                TreeNode node = queue.poll();
                cur = cur.next = new ListNode(node.val);
                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }
            res.add(dummyNode.next);
        }
        return res.toArray(new ListNode[0]);
    }
}
