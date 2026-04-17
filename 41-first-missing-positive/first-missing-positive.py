class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        ans = 0
        n = len(nums)
        i = 0

        while i < n:
            corr = nums[i]-1
            if 1<= nums[i] <= n and nums[i] != nums[corr]:
                nums[i], nums[corr] = nums[corr], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                ans = i + 1
                return ans
        return n+1