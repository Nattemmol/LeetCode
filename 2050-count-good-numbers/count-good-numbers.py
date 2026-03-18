class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n + 1) // 2
        prime = n//2
        return (pow(5,even, (10**9 +7))  * pow(4,prime, (10**9 +7))) % (10**9 +7)