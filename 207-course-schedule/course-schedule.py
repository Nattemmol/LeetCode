class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True
        
        ans = []
        pre = defaultdict(list)
        pre_count = [0 for _ in range(numCourses)]

        for u,v in prerequisites:
            pre[u].append(v)
            pre_count[v] += 1

        queue = deque()

        for i in range(len(pre_count)):
            if pre_count[i] == 0:
                queue.append(i)
        
        while queue:

            node = queue.pop()
            ans.append(node)
            
            for negh in pre[node]:
                pre_count[negh] -= 1
                if pre_count[negh] == 0:
                    queue.append(negh)
        
        return len(ans) == numCourses