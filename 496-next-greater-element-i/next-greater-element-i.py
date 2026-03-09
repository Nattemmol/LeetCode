class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicts = {n:i for i,n in enumerate(nums1)}
        print(dicts)
        stack=[]
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                val = stack.pop()
                ptr = dicts[val]
                res[ptr] = nums2[i]
            if nums2[i] in dicts:
                stack.append(nums2[i])
        return res