import sys
class Solution:
    def myAtoi(self, s: str) -> int:
        allowed = [' ','1','2','3','4','5','6','7','8','9','0']
        
        ans = "0"
        sign = "+"
        if s[0] not in allowed:
            return 0
        for each in s:
            if each == "+" and sign == "+":
                sign = "+"
            elif each =="-" and sign == "+":
                sign = "-"
            elif each =="+" and sign == "-":
                sign ="-"
            elif each =="-" and sign == "-":
                sign ="+"
            elif each == " ":
                continue
            elif (each in allowed) and (each != ' '):
                ans = ans + each
            elif each not in allowed:
                return int(ans)
        ans = sign+ans
        
        if (int(ans)>2**32-1):
            ans = 2**32-1
        elif(int(ans)<-2**31):
            ans = -2**31
        return int(ans)