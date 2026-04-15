class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self.ans = []
        self.max_len = 0

        def generate(i, temp, opening):
            
            if len(temp) + (len(s) - i) < self.max_len:
                return
            
            if opening == 0:
                if len(temp) > self.max_len:
                    self.max_len = len(temp)
                    self.ans = ["".join(temp)]
                elif len(temp) == self.max_len:
                    self.ans.append("".join(temp))

            for j in range(i, len(s)):
                
                if j > i and s[j] == s[j-1]:
                    continue
                
                new_opening = opening
                
                if new_opening == 0 and s[j] == ")":
                    continue
                
                if s[j] == "(":
                    new_opening += 1
                elif s[j] == ")":
                    new_opening -= 1
                
                temp.append(s[j])
                generate(j+1, temp, new_opening)
                temp.pop()
        
        generate(0, [], 0)

        if not self.ans:
            return [""]
        
        return list(set(self.ans))