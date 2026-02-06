class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        char_count = Counter(chars)
        print(char_count)
        for word in words:
            word_count = Counter(word)
            print(word_count)
            for j in word_count:
                if word_count[j] > char_count[j]:
                    break
            else:
                ans+=len(word)
        return ans