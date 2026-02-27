class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        
        l = 0
        maxx = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r] , 0) + 1
            maxx = max(maxx , freq[s[r]])

            if (r - l + 1) - maxx > k:
                freq[s[l]] -= 1
                l += 1
        return r - l + 1
