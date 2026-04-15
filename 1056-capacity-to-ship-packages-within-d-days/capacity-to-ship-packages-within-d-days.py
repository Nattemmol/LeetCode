class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def validate(max_cap):
            cur_sum = 0
            total_day = 1

            for w in weights:
                cur_sum += w
                if cur_sum > max_cap:
                    cur_sum = w
                    total_day += 1
                    
                    if total_day > days:
                        return False
            return True
        
        left,right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right-left)//2
            if validate(mid):
                right = mid -1
            else:
                left = mid + 1
        
        return left