class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = []
        for key in cnt:
            if cnt[key] == 2:
                ans.append(key)
        return ans