class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        queue = deque([[0]])
        ans = []
        
        while queue:
            path = queue.popleft()
            curr_node = path[-1]
            
            if curr_node == target:
                ans.append(path)
            else:
                for neighbor in graph[curr_node]:
                    queue.append(path + [neighbor])
                    print(path + [neighbor])
        return ans
