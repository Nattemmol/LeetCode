class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        parts = []
        str_num = str(num)
        
        for i, digit in enumerate(str_num):
            place_value = int(digit) * (10 ** (len(str_num) - 1 - i))
            parts.append(place_value)
        print(parts)
        for i in parts:
            if i >= 1000:
                m = int(i / 1000)
                for j in range(m):
                    ans.append("M")
            elif i == 900:
                ans.append("CM")
            elif i > 500:
                m = int((i -500)/100)
                ans.append("D")
                for j in range(m):
                    ans.append("C")
            elif i == 500:
                ans.append("D")
            elif i == 400:
                ans.append("CD")
            elif i >= 100:
                m = int(i/100)
                for j in range(m):
                    ans.append("C")
            elif i == 90:
                ans.append("XC")
            elif i > 50:
                m = int((i-50)/10)
                ans.append("L")
                for j in range(m):
                    ans.append("X")
            elif i == 50:
                ans.append("L")
            elif i == 40:
                ans.append("XL")
            elif i > 10:
                m = int(i/10)
                for j in range(m):
                    ans.append("X")
            elif i == 10:
                ans.append("X")
            elif i == 9:
                ans.append("IX")
            elif i > 5:
                m = int(i-5)
                ans.append("V")
                for j in range(m):
                    ans.append("I")
            elif i == 5:
                ans.append("V")
            elif i == 4:
                ans.append("IV")
            elif i > 1:
                for j in range(i):
                    ans.append("I")
            elif i == 1:
                ans.append("I")  
        return "".join(ans)