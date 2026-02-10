class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        count = Counter(changed)
        ans = []
        if len(changed) % 2 == 1:
            return []

        if count[0] % 2 == 0:
            ans.extend([0] * (count[0]//2))

        for k,v in sorted(count.items()):
            if count[k] > 0:
                if count[k*2] < count[k]:
                    return []
                count[k*2] -= count[k]
        for k in sorted(count.keys()):
            ans.extend([k] * count[k])
        return ans
