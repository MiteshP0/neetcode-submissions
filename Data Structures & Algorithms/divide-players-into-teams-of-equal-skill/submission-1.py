class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill) # sort from smallest to largest
        target = skill[0] + skill[-1] # sum up to get target val
        answer = 0
        for i in range(len(skill)//2): #floor division
            a,b = skill[i],skill[-1-i] # tuple pair from both ends
            if a+b != target: # check impossible sum 
                return -1
            answer += a*b # keep calc of chemistry
        return answer
