class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_arr, right_arr):
            left = len(left_arr)
            right = len(right_arr)
            merged = []
            l,r = 0,0
            while l < left and r < right:
                if left_arr[l] <= right_arr[r]:
                    merged.append(left_arr[l])
                    l += 1
                else:
                    merged.append(right_arr[r])
                    r += 1
            while l < left:
                merged.append(left_arr[l])
                l += 1
            while r < right:
                merged.append(right_arr[r])
                r += 1
            
            return merged
        
        def merge_arr(left,right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right-left)//2
            left_part = merge_arr(left, mid, arr)
            right_part = merge_arr(mid+1, right, arr)

            return merge(left_part, right_part)
        return merge_arr(0,len(nums)-1, nums)