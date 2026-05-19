class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {0:0, 1:1,2:2}

        def fib(num):
            if num not in self.memo:
                self.memo[num] = fib(num-1) + fib(num-2)
            return self.memo[num]
        fib(n)
        return self.memo[n]