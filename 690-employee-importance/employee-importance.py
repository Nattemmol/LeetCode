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
        total = 0
        ids = 0

        emp_map = {emp.id: emp for emp in employees}

        queue = deque([emp_map[id]])

        while queue:
            node = queue.popleft()

            total += node.importance

            for ids in node.subordinates:
                queue.append(emp_map[ids])
        
        return total


