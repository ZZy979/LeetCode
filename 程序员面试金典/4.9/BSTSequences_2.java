/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// 评论区解法，速度快2倍
class Solution {
    public List<List<Integer>> BSTSequences(TreeNode root) {
        List<TreeNode> items = new ArrayList<>();
        if (root != null)
            items.add(root);
        List<Integer> tmpRes = new ArrayList<>();
        List<List<Integer>> reses = new ArrayList<>();
        dfs(items, tmpRes, reses);
        return reses;
    }

    public void dfs(List<TreeNode> items, List<Integer> tmpRes, List<List<Integer>> reses) {
        if(items.isEmpty()) {
            reses.add(new ArrayList<Integer>(tmpRes));
            return;
        }
        int len = items.size();
        for(int i = 0; i < len ; i++) {
            TreeNode tmp = items.get(i);
            items.remove(i);
            if(tmp.left != null)
                items.add(tmp.left);
            if(tmp.right != null)
                items.add(tmp.right);
            tmpRes.add(tmp.val);
            dfs(items, tmpRes, reses);
            tmpRes.remove(tmpRes.size() - 1);
            items.add(i, tmp);
            items.remove(tmp.left);
            items.remove(tmp.right);
        }
    }
}
