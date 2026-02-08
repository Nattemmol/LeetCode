class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dicts = defaultdict(list)
        for path in paths:
            path = path.split()
            root = path[0]
            for sub in path[1:]:
                fname,_,cont = sub.partition("(")
                dicts[cont].append(root+"/"+fname)
        ans = []
        for k,v in dicts.items():
            if len(dicts[k]) > 1:
                ans.append(v)
        return ans
        