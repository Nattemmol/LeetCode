class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items)
        ans = []
        i = 0
        for key,v in sorted_dict.items():
            if i < k:
                ans.append(key)
                i +=1
            else:
                break
        return ans

