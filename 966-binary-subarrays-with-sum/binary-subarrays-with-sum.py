class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        

        count = Counter({0: 1})
        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num
            if current_sum - goal in count:
                ans += count[current_sum-goal]
            count[current_sum] += 1
        
        return ans
        