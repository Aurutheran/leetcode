class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = len(height)-1
        total = 0
        
        while (leftmax != rightmax):   #Have to make sure that left and right aren't the same
            if (height[leftmax] > height[rightmax]):   #If the left height is highest, we gotta multiply container with the lowest height
                current = (rightmax-leftmax)*height[rightmax]
                rightmax -= 1  #We move the right max because it was the shortest, and if we move it in we may get a larger value
            else:
                current = (rightmax-leftmax)*height[leftmax] #Else if the reight height is highest we multiply left height and increment leftmax to get a potentially higher left height for future areas
                leftmax += 1
            if current>total:  #We finally check if the current area is greater than the total and change to current height if its greater than total
                total = current
        return total