class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)-1
        
        while i < n:
            pos = nums[i]-1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos],nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return nums[i]