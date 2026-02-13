class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        vals1 = sorted(count1.values())
        vals2 = sorted(count2.values())

        if vals1 != vals2:
            return False
        return True
        #return vals1 == vals2
        