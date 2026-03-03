class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        dicts = {0:1}
        currentSum = 0
        for i in nums:
            currentSum +=i
            diff = currentSum -k
            result += dicts.get(diff,0)
            dicts[currentSum] = dicts.get(currentSum,0) + 1
        return result