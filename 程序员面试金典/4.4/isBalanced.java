/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Result {
    int height;
    boolean isBalanced;

    Result(int height, boolean isBalanced) {
        this.height = height;
        this.isBalanced = isBalanced;
    }

}

class Solution {
    public boolean isBalanced(TreeNode root) {
        return isBalancedRec(root).isBalanced;
    }

    private Result isBalancedRec(TreeNode root) {
        if (root == null)
            return new Result(0, true);
        Result leftResult = isBalancedRec(root.left);
        Result rightResult = isBalancedRec(root.right);
        return new Result(
            1 + Math.max(leftResult.height, rightResult.height),
            leftResult.isBalanced && rightResult.isBalanced && Math.abs(leftResult.height - rightResult.height) <= 1
        );
    }
}
