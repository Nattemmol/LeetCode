class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ran = Counter(ransomNote)
        count_mag = Counter(magazine)
        for k in count_ran.keys():
            if count_mag[k] < count_ran[k]:
                return False
        return True