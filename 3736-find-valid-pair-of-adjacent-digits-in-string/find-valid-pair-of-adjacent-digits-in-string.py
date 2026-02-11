class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        ans = ""
        print(count)
        for i in range(len(s)-1):
            if int(s[i]) != int(s[i+1]) and count[s[i]] == int(s[i]) and count[s[i+1]] == int(s[i+1]):
                return s[i:i+2]
        return ""