class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num / 3
        ans = []
        if mid % 1 == 0:
            ans.append(int(mid-1))
            ans.append(int(mid))
            ans.append(int(mid+1))
            return ans
        return []