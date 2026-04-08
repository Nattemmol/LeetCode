class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        temp = []
        n = len(pattern)
        self.flag = True

        def pos():
            if ans:
                return
            if len(temp) == n+1:
                for i in range(n):
                    if pattern[i] == "I" and temp[i] < temp[i+1]:
                        continue
                    elif pattern[i] == "D" and temp[i] > temp[i+1]:
                        continue
                    else:
                        self.flag = False
                        break
                if self.flag:
                    ans.append(temp[:])
                    return
                self.flag = True
            
            for j in range(1,10):
                if j not in temp:
                    temp.append(j)
                    pos()
                    temp.pop()
            
        pos()
        
        if ans:
            return "".join([str(x) for x in ans[0]])
        return ""
                    