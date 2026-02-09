class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sums = 0
        for i in nums:
            if i % 2 == 0:
                sums += i
        for i in queries:
            if nums[i[1]] % 2 == 0 and i[0]% 2 == 1:
                sums -= nums[i[1]]
            elif nums[i[1]] % 2 == 0 and i[0]% 2 == 0:
                sums += i[0]
            elif nums[i[1]] % 2 == 1 and i[0]% 2 == 1:
                sums += nums[i[1]] + i[0]
            print(sums)
            nums[i[1]] += i[0]
            ans.append(sums)
        return ans