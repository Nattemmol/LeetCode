class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums = 0
        need = 0
        for i in range(len(nums)):
            sums += nums[i]
            need = min(need, sums)
        mini = abs(need) + 1
        
        return mini