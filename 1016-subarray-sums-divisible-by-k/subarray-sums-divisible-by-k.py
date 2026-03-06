class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dicts = defaultdict(int)
        dicts[0] = 1
        currentSum = 0
        total = 0
        for num in nums:
            currentSum +=num
            mod = currentSum % k
            total += dicts.get(mod,0)
            dicts[mod] = dicts.get(mod,0)+1
        return total
