class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        j = 0
        str_new = []
        dicts = defaultdict(list)
        for stri in strs:
            str_new = "".join(sorted(stri))
            dicts[str_new].append(stri)
        return list(dicts.values())