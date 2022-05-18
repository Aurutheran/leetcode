class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        i = 0
        j = 0
        #sorted list
        sortednum = []
        
        while (i<len(nums1) and j<len(nums2)):
            if (nums1[i]<nums2[j]):
                sortednum.append(nums1[i])
                i += 1
            else:
                sortednum.append(nums2[j])
                j += 1
                
        if i == len(nums1):
            sortednum.extend(nums2[j:])
        else:
            sortednum.extend(nums1[i:])

        low, high, result = 0, len(sortednum), 0
        
        while True:
            mid = (low + high) // 2
            
			if (len(sortednum) % 2 != 0):
                return sortednum[mid] / 1
    
			first = sortednum[mid - 1]
			second = sortednum[mid]

            return (first + second) / 2