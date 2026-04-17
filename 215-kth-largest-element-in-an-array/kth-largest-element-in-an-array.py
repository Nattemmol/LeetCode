class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick_sort(nums):
            if len(nums) <= 1:
                return nums
            
            pivot = random.choice(nums)
            
            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]
            
            return quick_sort(left) + middle + quick_sort(right)

        n = len(nums)
        count = Counter(nums)
        unique_nums = list(set(nums))
        
        sorted_unique = quick_sort(unique_nums)
        
        ans = []
        for i in sorted_unique:
            ans.extend([i] * count[i])
            
        return ans[n-k]
