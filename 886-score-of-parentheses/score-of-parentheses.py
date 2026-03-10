class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    sums = 0
                    while stack and stack[-1] != '(':
                        sums += stack.pop()
                    stack.pop()
                    stack.append(sums*2)
        return sum(stack)