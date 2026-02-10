class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        count = 0
        print(s_count)
        print(t_count)
        for k,v in s_count.items():
            if s_count[k] > t_count[k]:
                count += s_count[k] - t_count[k]
        return count