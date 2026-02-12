class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        two = s1 + s2
        ans = 0
        if two.count("x") % 2 == 1 or two.count("y") % 2 == 1:
            return -1
        count_xy, count_yx = 0,0

        
        for char_s1, char_s2 in zip(s1, s2):
            if char_s1 == "x" and char_s2 == "y":
                count_xy += 1
            elif char_s1 == "y" and char_s2 == "x":
                count_yx += 1
        
        if count_xy % 2 == 0:
            ans += count_xy // 2
        if count_yx % 2 == 0:
            ans += count_yx // 2
        if count_xy % 2 == 1 and count_yx % 2 == 1:
            ans +=  count_xy // 2
            ans +=  count_yx // 2
            ans += 2
        return ans