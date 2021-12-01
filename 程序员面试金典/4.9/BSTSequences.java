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
    public List<List<Integer>> BSTSequences(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            result.add(new LinkedList<>());
            return result;
        }
        List<List<Integer>> leftSeq = BSTSequences(root.left);
        List<List<Integer>> rightSeq = BSTSequences(root.right);
        LinkedList<Integer> prefix = new LinkedList<>();
        prefix.add(root.val);
        for (List<Integer> left : leftSeq)
            for (List<Integer> right : rightSeq)
                result.addAll(weave((LinkedList<Integer>) left, (LinkedList<Integer>) right, prefix));
        return result;
    }

    private List<List<Integer>> weave(LinkedList<Integer> l1, LinkedList<Integer> l2, LinkedList<Integer> prefix) {
        List<List<Integer>> weaved = new ArrayList<>();
        if (l1.isEmpty() || l2.isEmpty()) {
            LinkedList<Integer> result = new LinkedList<>();
            result.addAll(prefix);
            result.addAll(l1);
            result.addAll(l2);
            weaved.add(result);
            return weaved;
        }

        int l1Head = l1.removeFirst();
        prefix.addLast(l1Head);
        weaved.addAll(weave(l1, l2, prefix));
        prefix.removeLast();
        l1.addFirst(l1Head);

        int l2Head = l2.removeFirst();
        prefix.addLast(l2Head);
        weaved.addAll(weave(l1, l2, prefix));
        prefix.removeLast();
        l2.addFirst(l2Head);

        return weaved;
    }
}
