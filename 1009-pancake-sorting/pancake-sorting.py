class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)

        def flip(sub_arr_end_index):
            left = 0
            right = sub_arr_end_index
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        for current_size in range(n, 1, -1):
            
            max_index = 0
            for i in range(current_size):
                if arr[i] > arr[max_index]:
                    max_index = i

            if max_index != current_size - 1:
                if max_index != 0:
                    flip(max_index)
                    flips.append(max_index + 1)
                flip(current_size - 1)
                flips.append(current_size)
                
        return flips
