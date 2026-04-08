class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        sets = ['a','b','c']
        temp = []

        def generate(i):
            if len(temp) == n:
                if temp not in ans:
                    ans.append(temp[:])
                    return

            
            for j in range(i,3):
                if not temp or sets[j] != temp[-1]:
                    temp.append(sets[j])
                    generate(i)
                    temp.pop()
        generate(0)
        
        ans.sort()
        if len(ans) <= k-1:
            return ""
        else:
            return "".join(ans[k-1])