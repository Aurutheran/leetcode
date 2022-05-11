class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        list = []
        for each in nums:
            for x in list:
                x = x + each
            list.append(int(each))
        return max(list)
    
    #make it better