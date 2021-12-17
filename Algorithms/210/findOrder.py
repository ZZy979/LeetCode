from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        edges = defaultdict(list)
        for j, i in prerequisites:
            indegree[j] += 1
            edges[i].append(j)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        ans = []
        while queue:
            i = queue.popleft()
            ans.append(i)
            for j in edges[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        return ans if len(ans) == numCourses else []
