class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def segment_with_small_set(nums,k):

            l = 0
            r = 0
            maxi = 0
            
            l = 0
            unique_count = 0
            freq = defaultdict(int)
            total = 0

            for r in range(len(nums)):
                if freq[nums[r]] == 0:
                    unique_count += 1
                freq[nums[r]] += 1

                while unique_count > k:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        unique_count -= 1
                    l += 1
                total += r-l+1
                
            
            return total
            
        return segment_with_small_set(nums,k) - segment_with_small_set(nums,k-1)