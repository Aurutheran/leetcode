class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
        stringnum = str(x)
        size = len(stringnum)
        i=0
        while (i<size-1-i):
            if(stringnum[i] is not stringnum[size-1-i]):
                return False
            i = i+1
        return True
        

        #Work on faster solution*