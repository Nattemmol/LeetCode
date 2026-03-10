class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = []
        i = 0

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            elif s[i] == "]":
                temp = ""
                while stack[-1] !="[":
                    temp = stack.pop() + temp
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)
                stack.append(temp*num)


        return ''.join(stack)
