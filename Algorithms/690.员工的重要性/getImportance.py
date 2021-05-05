"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {e.id: e for e in employees}
        return dfs(employees, id)
    
def dfs(employees, id):
    return employees[id].importance + sum(dfs(employees, s) for s in employees[id].subordinates)
