class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        n = len(nums)
        used = []

        def comb(i):
            if len(temp) >= 2:
                if temp not in ans:
                    ans.append(temp[:])
                
            
            for j in range(i, n):
                if temp and temp[-1] > nums[j]:
                    continue
                temp.append(nums[j])
                comb(j+1)
                temp.pop()

        comb(0)
        return ans

