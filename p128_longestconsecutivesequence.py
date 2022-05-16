class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        maxs = tempmax = 1
        
        for x in range(1,len(nums)):
            if(nums[x-1]==nums[x]):
                continue
            elif(nums[x-1]+1 == nums[x]):
                tempmax += 1
            else:
                maxs = max(tempmax,maxs)
                tempmax = 1
        return max(tempmax,maxs)