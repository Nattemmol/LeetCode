class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        curr,prev = 2,1

        for i in range(3,n+1):
            prev,curr = curr, curr+prev
        return curr