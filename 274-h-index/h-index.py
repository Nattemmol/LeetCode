class Solution:
    def hIndex(self, citations: List[int]) -> int:
        vals = Counter(citations)
        maxi = max(citations)
        cnt = 0
        citations.sort()
        prev = citations[-1]
        ans = 0

        for i in range(maxi,-1,-1):
            cnt += vals[i]
            vals[i] = cnt
        sorted_dict = {key: value for key, value in sorted(vals.items(), reverse=True)}
        print(sorted_dict)
        for k in sorted_dict.keys():
            if sorted_dict[k] >= k:
                ans = k
                break
        return ans
