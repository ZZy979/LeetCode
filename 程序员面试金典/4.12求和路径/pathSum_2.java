/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// 使用散列表优化，速度提高5倍
class Solution {
    private Map<Integer, Integer> pathCount = new HashMap<>();

    public int pathSum(TreeNode root, int sum) {
        return countPathsWithSum(root, sum, 0);
    }

    private int countPathsWithSum(TreeNode root, int targetSum, int runningSum) {
        if (root == null)
            return 0;
        runningSum += root.val;
        int sum = runningSum - targetSum;
        int totalPaths = pathCount.getOrDefault(sum, 0);
        if (runningSum == targetSum)
            ++totalPaths;
        
        pathCount.put(runningSum, pathCount.getOrDefault(runningSum, 0) + 1);
        totalPaths += countPathsWithSum(root.left, targetSum, runningSum);
        totalPaths += countPathsWithSum(root.right, targetSum, runningSum);
        pathCount.put(runningSum, pathCount.getOrDefault(runningSum, 0) - 1);
        return totalPaths;
    }
}
