class Solution(object):
    def singleNumber(self, nums):
        single_one = 0
        cnt = Counter(nums)
        for k in cnt:
            if cnt[k] == 1:
                single_one = k
        return single_one