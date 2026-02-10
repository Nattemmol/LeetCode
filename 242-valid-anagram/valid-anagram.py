class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)

        for k,v in s_count.items():
            if s_count[k] == t_count[k]:
                continue
            else:
                return False
        return True