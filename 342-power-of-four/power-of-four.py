class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ans = n/4
        if n == 1:
            return True
        if n == 0:
            return False
        if ans == 4 or ans == 1:
            return True
        elif ans < 4:
            return False
        else:
            return self.isPowerOfFour(ans)

