class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        pre_count = [0 for _ in range(numCourses)]

        ans = []

        for x,y in prerequisites:
            pre[y].append(x)
            pre_count[x] += 1
        
        queue = deque()
        for i in range(len(pre_count)):
            if pre_count[i] == 0:
                queue.append(i)
                ans.append(i)
        
        while queue:
            node = queue.pop()

            for negh in pre[node]:
                pre_count[negh] -= 1
                if pre_count[negh] == 0:
                    queue.append(negh)
                    ans.append(negh)
        
        if len(ans) < numCourses:
            return []
        else:
            return ans
