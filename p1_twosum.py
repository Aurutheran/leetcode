class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmaps = {}
        for index,x in enumerate(nums):
            if (target - x in hashmaps):
                sol = [hashmaps[target-x],index]
                return sol
            hashmaps[x] = index