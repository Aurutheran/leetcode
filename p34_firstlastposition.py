class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        second = -1
        
        
        for i in range(len(nums)):
            
            if nums[i] == target:
                if (first == -1):
                    first = i
                    second = i
                else:
                    second = i
        return [first, second]
                    
                    
            