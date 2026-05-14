class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        
        for i in range(min(len(nums1),k)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        
        while heap and len(ans) < k:
            val, x,y = heapq.heappop(heap)
            ans.append([nums1[x],nums2[y]])

            if y+1 < len(nums2):
                heapq.heappush(heap,(nums1[x]+nums2[y+1],x,y+1))

        return ans
        


