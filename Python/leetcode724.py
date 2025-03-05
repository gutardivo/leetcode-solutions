from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            print(nums[:i-1],nums[i:])
            if sum(nums[:i-1]) == sum(nums[i:]):
                return i-1
                
        return -1 

s = Solution()

nums = [-1,-1,0,1,1,0]
# nums = [1,7,3,6,5,6]

print(s.pivotIndex(nums))