class Solution:
    def findRadius(self,houses, heaters):
        houses.sort()
        heaters.sort()
        result = 0
        
        for house in houses:
            pos = bisect_left(heaters, house)
            
            right_distance = heaters[pos] - house if pos < len(heaters) else float('inf')
            
            left_distance = house - heaters[pos - 1] if pos > 0 else float('inf')
            
            min_distance = min(left_distance, right_distance)
            
            result = max(result, min_distance)
        
        return result
