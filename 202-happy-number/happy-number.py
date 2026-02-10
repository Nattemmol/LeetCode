class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum_of_squares = 0
            for digit in str(n):
                sum_of_squares += int(digit) **2
            n = sum_of_squares
        return n == 1
