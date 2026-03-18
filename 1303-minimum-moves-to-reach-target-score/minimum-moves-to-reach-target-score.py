class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        down = target

        steps = 0
        while down > 1 and maxDoubles > 0:
            if down % 2 == 1:
                down -= 1
                steps += 1
            else:
                down //= 2
                maxDoubles -= 1
                steps += 1
        
        return steps + (down-1)