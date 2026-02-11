class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        num1_set = set(nums1)
        num2_set = set(nums2)
        first = list(num1_set-num2_set)
        second = list(num2_set-num1_set)
        ans.append(first)
        ans.append(second)
        
        return ans
