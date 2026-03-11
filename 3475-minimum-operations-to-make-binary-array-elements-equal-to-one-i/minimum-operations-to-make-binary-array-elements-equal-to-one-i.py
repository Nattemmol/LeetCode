class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)-2):
            if nums[i]==0:
                count+=1
                nums[i]=1
                nums[i+1] = 0 if nums[i+1] else 1
                nums[i+2] = 0 if nums[i+2] else 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return count