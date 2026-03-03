class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0 for _ in range(len(nums))]
        s = 1
        zero_count = nums.count(0)
        if zero_count > 1:
            return answer
        if zero_count == 1:
            s = 1
            zero_index = 0
            for i in range(len(nums)):
                if nums[i] == 0:
                    zero_index = i
                else:
                    s*=nums[i]
            answer[zero_index] = s
        s = 1
        for i in range(len(nums)):
            s*=nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                answer[i] = int(s / nums[i])
        return answer
