class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for k in count.keys():
            if count[k] > 1:
                return True
        return False