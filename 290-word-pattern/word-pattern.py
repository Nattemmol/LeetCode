class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordToChar = {}
        charToWord = {}

        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        for c,w in zip(pattern, s_list):
            if c in charToWord and charToWord[c] !=w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            wordToChar[w] = c
            charToWord[c] = w
        return True