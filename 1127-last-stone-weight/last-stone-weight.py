class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            left = heapq.heappop(stones)
            right = heapq.heappop(stones)
            if right-left > 0:
                heapq.heappush(stones, left-right)
            
        
        if stones != []:
            return abs(stones[0])
        return 0