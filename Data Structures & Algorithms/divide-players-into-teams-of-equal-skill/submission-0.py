class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill) # sort from big to small
        target = skill[0] + skill[-1] # sum up to get target val
        answer = 0
        for i in range(len(skill)//2): #floor division
            a,b = skill[i],skill[-1-i]
            if a+b != target:
                return -1
            answer += a*b
        return answer
