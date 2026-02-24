class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right = len(skill)-1
        skill.sort()
        sums = sum(skill) /(len(skill)/2)

        tup = list()
        total = 0
        while left < right:
            if skill[left] + skill[right] ==sums:
                tup.append([skill[left], skill[right]])
                left+=1
                right-=1
            else:
                return -1
        for mult in tup:
           total += mult[0]*mult[1]
        return total