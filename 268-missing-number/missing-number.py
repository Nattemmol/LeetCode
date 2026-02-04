class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = len(nums)+1
        mini = 0
        for i in range(mini, maxi):
            if i not in nums:
                return i
        
