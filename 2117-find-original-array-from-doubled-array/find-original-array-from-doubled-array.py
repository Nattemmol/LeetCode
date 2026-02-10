class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        '''ans = []
        changed.sort()
        i = 0
        n = len(changed)

        if len(changed) == 1:
            return []
        if changed[i] == 0 and changed.count(0)%2 == 1:
                return []
        elif changed[i] == 0 and changed.count(0)%2 == 0:
            idx = changed[::-1].index(0)
            changed = changed[idx+1:]
        while i < n:
            
            if changed[i]*2 in changed:

                dob = changed.index(int(changed[i]*2))
                ans.append(changed[i])
                temp = changed[-1]
                changed[-1] = changed[dob]
                changed[dob] = temp
                changed.pop()
                i += 1
                n -= 1
                changed.sort()
            else:
                return []
        return ans'''
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
