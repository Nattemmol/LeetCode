class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = set()

        i,n = 0, len(nums)

        while i < n:
            pos = nums[i]-1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i:
                ans.add(nums[i])

        return list(ans)