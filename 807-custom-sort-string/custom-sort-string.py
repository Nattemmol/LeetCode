class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        priority = {char: i for i, char in enumerate(order)}
        result = "".join(sorted(s, key=lambda x: priority.get(x, len(order))))

        return result