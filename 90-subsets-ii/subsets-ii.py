class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def subset(i,temp):
            ans.append(temp[:])
            for j in range(i, n):
                if j > i and nums[j] == nums[j-1]:
                    continue
                temp.append(nums[j])
                subset(j+1,temp)
                temp.pop()
        subset(0,[])
        return ans