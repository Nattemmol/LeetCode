class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        self.temps = []
        word_set = set(wordDict)

        def word(i, s):
            if i == len(s):
                ans.append(" ".join(self.temps))
            
            for j in range(i, len(s)+1):
                temp = s[i:j]
                if temp in word_set:
                    self.temps.append(temp)
                    word(j,s)
                    self.temps.pop()
        
        word(0,s)
        return ans