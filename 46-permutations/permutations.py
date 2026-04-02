class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        n = len(nums)
        used = [False] * n

        def per(i):
            if i == n:
                ans.append(temp[:])
                return

            for j in range(n):
                if used[j]:
                    continue

                temp.append(nums[j])
                used[j] = True
                per(i+1)
                temp.pop()
                used[j] = False
        
        per(0)
        return ans