class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        #Case where there is no Phone Digits:
        if not digits:
            return []
        
        #Result set
        res = []
        
        phonelet = {
            '2' : ["a","b","c"],
            '3' : ["d","e","f"],
            '4' : ["g","h","i"],
            '5' : ["j","k","l"],
            '6' : ["m","n","o"],
            '7' : ["p","q","r","s"],
            '8' : ["t","u","v"],
            '9' : ["w","x","y","z"]  
        }
        
        
        def backtrack(i, currentString):
            if len(currentString) == len(digits):
                res.append(currentString)
                return
            
            for character in phonelet[digits[i]]:
                backtrack(i+1, currentString + character)
            
        
        backtrack(0,"")
        return res