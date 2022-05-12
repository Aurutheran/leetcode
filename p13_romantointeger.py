class Solution:
    def romanToInt(self, s: str) -> int:
        dicto = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        soln = 0
        for x in range(len(s)-1):
            if(dicto[s[x+1]]>dicto[s[x]]):  #If the next value is greater, you subtract the current val
                soln -=dicto[s[x]]
            else:                           #If the next value is less, you can add the current val
                soln +=dicto[s[x]]
        soln += dicto[s[-1]]          #We finally add the last value cause there isn't any next value to check
        return soln