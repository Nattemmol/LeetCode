class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k == 1:
            return nums
        max_window = []
        dec_stack = deque()
        for i in range(k):
            while dec_stack and nums[i] > dec_stack[-1]:
                dec_stack.pop()
            dec_stack.append(nums[i])
        max_window.append(dec_stack[0])
        l = 0

        for i in range(k,len(nums)):
            
            while dec_stack and nums[i] > dec_stack[-1]:
                dec_stack.pop()

            if dec_stack and nums[l] == dec_stack[0]:
                left = dec_stack.popleft()
                
            l += 1
            dec_stack.append(nums[i])
            max_window.append(dec_stack[0])
        
        return max_window
        