class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        print(count)
        
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)
        print(sorted_items)
        sorted_dict = dict(sorted_items)
        print(sorted_dict)
        ans = []
        i = 0
        for key,v in sorted_dict.items():
            print(key)
            if i < k:
                ans.append(key)
                i +=1
            else:
                break
        return ans

