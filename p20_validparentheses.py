class Solution:
    def isValid(self, s: str) -> bool:
        stax = []
        opener = ['(','{','[']
        allowed = {'(':')','{':'}','[':']'}
        for x in s:
            if (x in opener):
                stax.append(x)
            elif(len(stax) == 0):
                return False
            else:
                popped = stax.pop()
                if (allowed[popped] != x):
                    return False
                
        if len(stax) == 0:
            return True
        return False