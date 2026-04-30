class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = defaultdict(list)
        adj_cnt = [0]*numCourses
 
        for f,t in prerequisites:
            adj[t].append(f)
            adj_cnt[t] += 1
        
        ans = []

        for i in range(numCourses):
            if adj_cnt[i] == 0:
                ans.append([])
                continue
            queue = deque([i])
            visited = set()

            temp = []
            while queue:
                node = queue.popleft()
                if node != i and node not in temp:
                    temp.append(node)

                for negh in adj[node]:
                    if negh not in visited:
                        queue.append(negh)
                        visited.add(negh)
            ans.append(temp)
        res = []

        for u,v in queries:
            if u in ans[v]:
                res.append(True)
            else:
                res.append(False)
        return res
        