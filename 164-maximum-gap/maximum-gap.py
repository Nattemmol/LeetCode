class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxi = 0
        if len(nums) == 1:
            return 0
        max_val = max(nums)

        def bucket_sort(arr):
            max_val = max(arr)
            num_buckets = len(arr)
            buckets = [[] for _ in range(num_buckets)]
            for num in arr:
                index = int((num_buckets * num)//(max_val+1))
                buckets[index].append(num)
            
            sorted_arr = []
            for i in range(num_buckets):
                buckets[i] = sorted(buckets[i])
            for bucket in buckets:
                sorted_arr.extend(bucket)

            return sorted_arr


        sorted_num = bucket_sort(nums)

        for i in range(len(nums)-1):
            maxi = max(maxi, sorted_num[i+1]-sorted_num[i])
        
        return maxi







