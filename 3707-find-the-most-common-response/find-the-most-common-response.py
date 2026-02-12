class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        for i in range(len(responses)):
            for word in set(responses[i]):
                count[word] += 1
        
        sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0])) 

        return sorted_items[0][0]
