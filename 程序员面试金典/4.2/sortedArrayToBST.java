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
    public TreeNode sortedArrayToBST(int[] nums) {
        return createTree(nums, 0, nums.length);
    }

    private TreeNode createTree(int[] nums, int left, int right) {
        if (left >= right)
            return null;
        int m = (left + right) / 2;
        TreeNode root = new TreeNode(nums[m]);
        root.left = createTree(nums, left, m);
        root.right = createTree(nums, m + 1, right);
        return root;
    }

}
