class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        for x in range(len(nums)):
            if nums[x] not in temp:
                temp.append(nums[x])      
        nums.clear()   
        for i in temp:
            nums.append(i)
        return len(nums)