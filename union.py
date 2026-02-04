class Solution:    
    def findUnion(self, a, b):
        # code here
        set1 = set(a)
        set2 = set(b)
        
        set_union = set1.union(set2)
        
        set_list = list(set_union)
        
        return set_list
