class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False] * len(rooms)
        self.nvisited = 0
        self.dfs(rooms, 0)
        return self.nvisited == len(rooms)
        
    def dfs(self, rooms, cur):
        self.visited[cur] = True
        self.nvisited += 1
        for key in rooms[cur]:
            if not self.visited[key]:
                self.dfs(rooms, key)
