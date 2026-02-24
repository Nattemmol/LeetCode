class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cc=sqrt(c)
        a = 0
        b = cc
        b = int(b)
        while a <= b:
            if a**2 + b**2 == c:
                return True
            if a**2 + b**2 > c:
                b-=1
            if a**2 + b**2 < c:
                a+=1
        return False