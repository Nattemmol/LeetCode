class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans =  float("inf")
        child = [0 for _ in range(k)]
        
        def dis(i):
            if i == len(cookies):
                self.ans = min(self.ans, max(child))
            
            if max(child) >= self.ans:
                return
                
            for j in range(k):
                child[j] += cookies[i]
                dis(i+1)
                child[j] -= cookies[i]
                if child[j] == 0:
                    break
            
        dis(0)
        return self.ans