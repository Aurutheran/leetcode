class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = ""
        
        stringnum = str(x)
        
        size = len(stringnum)
        
        while (size-1>=0):
            temp = temp + str(stringnum[size-1])
            size = size-1
        
        if (temp == str(x)):
            return True
        return False