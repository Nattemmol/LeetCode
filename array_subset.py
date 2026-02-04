#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        counter_a = Counter(a)
        counter_b = Counter(b)
        print(counter_a)
        print(counter_b)
        
        for count_b in counter_b:
            if count_b not in counter_a or counter_b[count_b] > counter_a[count_b]:
                return False
        return True
