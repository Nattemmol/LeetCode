class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # def bucket_sort(arr):
        #     if not arr: return arr
        #     bucket_count = len(arr)
        #     max_val, min_val = max(arr), min(arr)
        #     buckets = [[] for _ in range(bucket_count)]

        #     for num in arr:
        #         index = int((num - min_val) / (max_val - min_val + 1) * bucket_count)
        #         buckets[index].append(num)

        #     return [val for b in buckets for val in sorted(b)]



        adj = defaultdict(list)
        adj_cnt = [0 for _ in range(n)]


        for f,t in edges:
            adj[t].append(f)
            adj_cnt[t] += 1

        ans = []
        for i in range(n):
            if adj_cnt[i] == 0:
                ans.append([])
                continue
            queue = deque([i])
            pos = []
            visited = set()
            while queue:
                node = queue.popleft()
                if node != i and node not in pos:
                    pos.append(node)
                for negh in adj[node]:
                    if negh not in visited:
                        queue.append(negh)
                        visited.add(negh)
                        

            pos.sort()
            ans.append(pos)
        
        return ans
        


