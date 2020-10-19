// BFS
class Solution {
    public boolean findWhetherExistsPath(int n, int[][] graph, int start, int target) {
        Map<Integer, Set<Integer>> edges = new HashMap<>();
        for (int[] edge : graph)
            if (edge[0] != edge[1]) {
                if (!edges.containsKey(edge[0]))
                    edges.put(edge[0], new HashSet<>());
                edges.get(edge[0]).add(edge[1]);
            }
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        Set<Integer> visited = new HashSet<>();
        while (!queue.isEmpty()) {
            int v = queue.remove();
            if (v == target)
                return true;
            else if (edges.containsKey(v))
                for (int u : edges.get(v))
                    if (!visited.contains(u)) {
                        visited.add(u);
                        queue.add(u);
                    }
        }
        return false;
    }
}
