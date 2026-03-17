class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        ans = 0
        diff = []
        for i in range(len(costs)):
            diff.append((abs(costs[i][0]-costs[i][1]),i))
        sorted_diff = sorted(diff, key= lambda x: x[0], reverse=True)

        a_count = 0
        b_count = 0
        i = 0

        for df in sorted_diff:
            if a_count < int(len(costs)/2) and b_count < int(len(costs)/2):
                if costs[df[1]][0] > costs[df[1]][1]:
                    b_count += 1
                    ans += costs[df[1]][1]
                else:
                    a_count += 1
                    ans += costs[df[1]][0]
            else:
                if a_count < b_count:
                    ans += costs[df[1]][0]
                else:
                    ans += costs[df[1]][1]

        return ans