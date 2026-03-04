class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        idx = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < 0:
                idx = i
                break
        sums = 0
        need = 0
        for i in range(idx+1):
            sums += nums[i]
            need = min(need, sums)
        mini = abs(need) + 1
        
        return mini