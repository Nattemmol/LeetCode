class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= (n - mid):
                right = mid
            else:
                left = mid + 1
        return n - right