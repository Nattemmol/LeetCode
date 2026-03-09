class Solution:
    def simplifyPath(self, path: str) -> str:
        lis = path.split('/')
        stack = []
        for i in lis:
            if i == "..":
                if stack:
                    stack.pop()
            elif i !="." and i !="":
                stack.append(i)
        return "/"+"/".join(stack)