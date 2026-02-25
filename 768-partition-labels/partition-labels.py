class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        ans = []
        end = 0
        size = 0
        
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_occurrence[char])
            
            if i == end:
                ans.append(size)
                size = 0
                
        return ans
