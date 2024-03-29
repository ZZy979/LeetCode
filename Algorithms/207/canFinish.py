from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        edges = defaultdict(list)
        for j, i in prerequisites:
            indegree[j] += 1
            edges[i].append(j)
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        finish = 0
        while queue:
            i = queue.popleft()
            finish += 1
            for j in edges[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        return finish == numCourses
