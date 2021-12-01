/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private Integer last = null;

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null)
            return null;
        TreeNode suc = inorderSuccessor(root.left, p);
        if (suc != null)
            return suc;
        if (last != null && last == p.val)
            return root;
        last = root.val;
        return inorderSuccessor(root.right, p);
    }
}
