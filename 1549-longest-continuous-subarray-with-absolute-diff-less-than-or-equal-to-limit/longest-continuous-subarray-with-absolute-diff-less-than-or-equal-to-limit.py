class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue = deque()

        longest = 0
        mini = deque()
        maxi = deque()

        for r in range(len(nums)):
            queue.append(nums[r])
            
            while mini and nums[r] < mini[-1]:
                mini.pop()
            mini.append(nums[r])

            while maxi and nums[r] > maxi[-1]:
                maxi.pop()
            maxi.append(nums[r])

            while queue and maxi[0] - mini[0] > limit:
                left = queue.popleft()
                if left == maxi[0]:
                    maxi.popleft()
                if left == mini[0]:
                    mini.popleft()

            longest = max(longest, len(queue))
        
        return longest