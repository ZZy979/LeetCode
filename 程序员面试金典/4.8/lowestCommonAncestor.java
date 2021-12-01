/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// 1253 ms
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q)
            return root;
        boolean pIsOnLeft = covers(root.left, p);
        boolean qIsOnLeft = covers(root.left, q);
        if (pIsOnLeft != qIsOnLeft)
            return root;
        return lowestCommonAncestor(pIsOnLeft ? root.left : root.right, p, q);
    }

    private boolean covers(TreeNode root, TreeNode p) {
        if (root == null)
            return false;
        if (root == p)
            return true;
        return covers(root.left, p) || covers(root.right, p);
    }

}
