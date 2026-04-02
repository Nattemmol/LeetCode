class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        temp = []
        dig_let = {
        '2': ['a','b','c'],'3': ['d','e','f'],'4': ['g','h','i'],
        '5': ['j','k','l'],'6': ['m','n','o'],'7': ['p','q','r','s'],
        '8': ['t','u','v'],'9': ['w','x','y','z'],
        }
        n = len(digits)

        def comb(i):
            if i == n:
                ans.append("".join(temp))
                return
            
            curr = digits[i]
            for j in dig_let[curr]:
                    temp.append(j)
                    comb(i+1)
                    temp.pop()
        
        comb(0)
        return ans
    


                
