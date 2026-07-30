class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        rob[0],rob[1], rob[2] = nums[0], nums[1], nums[0]+nums[2]

        for i in range(3, len(nums)):
            rob[i] = nums[i] + max(rob[i-2],rob[i-3])
        print(rob)
        return max(rob[-1],rob[-2])