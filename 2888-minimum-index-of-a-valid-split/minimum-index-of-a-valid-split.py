class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        dom_element, total_count = counts.most_common(1)[0]
        left = 0
        for i in range(len(nums)):
            if nums[i] == dom_element:
                left += 1
            right = total_count - left

            left_len = i + 1
            right_len = n - left_len
            
            if left > left_len //2 and right > right_len // 2:
                return i
        return -1