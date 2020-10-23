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
    public boolean checkSubTree(TreeNode t1, TreeNode t2) {
        if (t2 == null)
            return true;
        else if (t1 == null)
            return false;
        else if (t1.val == t2.val)
            return checkSubTree(t1.left, t2.left) && checkSubTree(t1.right, t2.right);
        else
            return checkSubTree(t1.left, t2) || checkSubTree(t1.right, t2);
    }
}
