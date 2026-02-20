class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)
        arrows = 1
        l = 0
        for i in range(1,len(points)):
            if points[l][1] < points[i][0]:
                
                arrows += 1
                l = i
        return arrows