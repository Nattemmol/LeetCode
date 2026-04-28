# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         pre = defaultdict(list)
#         pre_count = [0 for _ in range(numCourses)]

#         ans = []

#         for x,y in prerequisites:
#             pre[y].append(x)
#             pre_count[x] += 1

#         for i in range(numCourses):
#             if i not in pre:
#                 pre[i] = []
        
#         print(pre,pre_count)
        
#         stack = []


from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)
            

        state = [0] * numCourses
        ans = []

        def dfs(course):
            
            if state[course] == 1:
                return False
                
            if state[course] == 2:
                return True
            
            state[course] = 1
            
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            
            state[course] = 2
            ans.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans
