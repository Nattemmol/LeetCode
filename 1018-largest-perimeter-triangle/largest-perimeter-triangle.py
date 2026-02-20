class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        sorted_indices = sorted(count.keys(), reverse=True)
        print(sorted_indices)
        ans = 0
        for k in sorted_indices:
            if count[k] >= 3:
                ans = k * 3
        two = []
        nums.sort(reverse=True)
        print(nums)
        for k in range(len(nums)-1):
            for j in range(k+1,len(nums)-1):
                if nums[j] + nums[j+1] > nums[k]:
                    return max(nums[j] + nums[j+1] + nums[k],ans)
        return 0
        
