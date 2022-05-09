class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        words = []
        
        for each in nums:
            if each in words:
                return True
            words.append(int(each))
        return False