class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)

        if len(num) <=2:
            return False

        def fib(i,res):
            if i == n:
                return len(res) >= 3
            
            curr = 0
            for j in range(i,n):
                if j > i and num[i] == "0":
                    break
                
                curr = curr*10 + ord(num[j]) - ord("0")
                if len(res) < 2 or curr == res[-1] + res[-2]:
                    res.append(curr)
                    if fib(j+1, res):
                        return True
                    res.pop()
                if len(res) >= 2 and curr > res[-1] + res[-2]:
                    break
                
            return False

        return fib(0,[])

            
