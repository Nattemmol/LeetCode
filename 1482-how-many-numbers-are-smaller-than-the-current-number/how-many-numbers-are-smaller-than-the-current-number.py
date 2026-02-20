class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sumed = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j] and i!=j:
                    sumed[i]+=1
        return sumed