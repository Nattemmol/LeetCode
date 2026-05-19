class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        amount = [0]*n
        amount[0] = nums[0]
        amount[1] = nums[1]
        amount[2] = nums[0] + nums[2]
        ans = 0
        i = 3
        while i < len(nums):
            amount[i] = max(nums[i]+amount[i-2],nums[i]+amount[i-3])
            i += 1
        print(amount)
        return max(amount[n-1],amount[n-2])
