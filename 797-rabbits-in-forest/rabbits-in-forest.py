class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = Counter(answers)
        
        res = 0
        mult = 1
        rem = 1
        for k,v in count.items():
            if k == 0:
                res += v
            else:
                mult = v//(k+1)
                rem = v % (k+1)
                if mult > 0:
                    res += mult*(k+1)
                if rem > 0:
                    res += k+1
        
        return res