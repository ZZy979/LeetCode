/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// 中序遍历法
class Solution {
    private Integer last = null;

    public boolean isValidBST(TreeNode root) {
        if (root == null)
            return true;
        if (!isValidBST(root.left))
            return false;
        if (last != null && root.val <= last)
            return false;
        last = root.val;
        if (!isValidBST(root.right))
            return false;
        return true;
    }
}
