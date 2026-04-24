class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        group = [0 for _ in range(n)]


        for i in range(n):
            if group[i] == 0:  
                queue = deque([i])
                group[i] = 1
            
            while queue:
                node = queue.popleft()

                for negh in graph[node]:
                    if group[negh] == 0:
                        group[negh] = 3 - group[node]
                        queue.append(negh)
                    elif group[negh] == group[node]:
                        return False
        return True


