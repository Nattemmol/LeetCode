class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dicts = defaultdict(int)
        count = 0
        ans = []
        for cps in cpdomains:
            cps = cps.split()
            count = int(cps[0])
            doms = cps[1].split(".")
            mult = 1
            print(doms)
            for i in range(len(doms)-1):
                dicts[".".join(doms[i:])]+= count
                mult+=1
            dicts[doms[-1]] += count
        for k,v in dicts.items():
            ans.append(str(v)+" "+k)
        return ans


