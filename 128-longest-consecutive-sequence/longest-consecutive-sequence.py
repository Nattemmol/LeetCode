class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        nums = list(set_num)
        nums.sort()
        i = 0
        maxi = 0
        longest = 1
        if len(nums) == 1:
            return 1
        while i < len(nums)-1:
            if nums[i+1] - nums[i] == 1:
                longest += 1
            else:
                longest = 1
            maxi = max(maxi, longest)
            i += 1
        return maxi