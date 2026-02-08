class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = Counter(nums)
        ans = []
        for k in cnt:
            if cnt[k] > n/3:
                ans.append(k)
        return ans