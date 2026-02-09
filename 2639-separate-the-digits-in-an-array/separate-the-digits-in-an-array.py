class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            digits = list(map(int, str(num)))
            for i in digits:
                ans.append(i)
        return ans