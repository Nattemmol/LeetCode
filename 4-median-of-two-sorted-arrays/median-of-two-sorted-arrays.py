class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1+ nums2
        n = len(merged)
        merged.sort()
        median = 0

        if n % 2 == 0:
            mid1, mid2 = n//2, (n//2)-1
            median = (merged[mid1] + merged[mid2])/2
        else:
            mid = n//2
            median = merged[mid]



        return median