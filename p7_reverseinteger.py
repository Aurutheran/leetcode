import math
sign = lambda x: math.copysign(1, x)

class Solution:
    
    def reverse(self, x: int) -> int:
        
        sol = str(x)
        if sol[0] == "-":
            sol = sol[1:]
        sol = (sol[::-1])
        
        if (x<0):
            sol = -1*int(sol)
        else:
            sol = int(sol)
        
        if (sol>= 2**31-1):
            return 0
        elif(sol<= -2**31):
            return 0
        return sol