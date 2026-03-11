class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        inc_stack = []
        max_val = float("-inf")

        for i in range(len(nums)-1,-1,-1):
            if nums[i] < max_val:
                    return True
            
            while inc_stack and nums[i] > inc_stack[-1]:
                max_val = max(max_val,inc_stack.pop())
            inc_stack.append(nums[i])

        return False