class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        mini = min(candies)
        if sum(candies) < k:
            return 0
        elif sum(candies) == k:
            return 1
        # elif len(candies) >= k:
        #     return min(candies)
        # # else:

        # #     for i in range(len(candies)):
        # #         mini = min(mini, candies[i]-mini)
            
        # #     return mini
        left, right = 1, sum(candies)//k

        ans = 0

        while left <= right:
            mid = left + (right-left)//2
            pos = 0
            print(right)
            for i in range(len(candies)):
                pos += candies[i]//mid
                # print(pos)
            if pos >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans