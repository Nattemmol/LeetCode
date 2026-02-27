class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zeros = 0
        l = 0
        longest = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            longest = max(longest, i-l)
        return longest