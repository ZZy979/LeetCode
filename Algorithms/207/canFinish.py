from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjvex = {i: [] for i in range(numCourses)}
        for j, i in prerequisites:
            indegree[j] += 1
            adjvex[i].append(j)
        queue = deque()
        for j in range(numCourses):
            if indegree[j] == 0:
                queue.append(j)
        finish = 0
        while queue:
            i = queue.popleft()
            finish += 1
            for j in adjvex[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        return finish == numCourses
