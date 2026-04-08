class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = list(enumerate(nums))
        result = [0] * len(nums)
        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    result[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            while i < len(left):
                result[left[i][0]] += j
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged
        
        mergeSort(arr)
        return result
