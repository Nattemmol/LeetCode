class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        se = [0] * (n+1)

        for l,r,add in shifts:
            if add == 1:
                se[l] +=1
                se[r+1]-=1
            if add == 0:
                se[l] -=1
                se[r+1]+=1
        for i in range(1,len(se)):
               se[i] += se[i-1]
        
        ans = []
        for i in range(len(s)):
            shift = se[i]%26
            new_char = chr((ord(s[i]) - ord('a')+shift) %26 + ord('a'))
            ans.append(new_char)
        return "".join(ans)