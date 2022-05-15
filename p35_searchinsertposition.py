class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index,x in enumerate(nums):
            if x>=target:
                return index
        return len(nums)