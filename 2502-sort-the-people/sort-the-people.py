class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        maxi = 0
        for i in heights:
            if i > maxi:
                maxi = i
        counts = {}
        for i in range(len(heights)):
            counts[heights[i]] = names[i]
        print(counts)

        ans = []
        mini = min(counts)
        for i in range(maxi,mini-1,-1):
            if i in counts:
                ans.append(counts[i])

        return ans
        