from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        totalSum = sum(nums[0:k])
        maxRes = totalSum/k
        
        for i in range(len(nums)-k):
            print(i)
            totalSum = totalSum - nums[i] + nums[i+k]
            
            maxRes = max(totalSum/k, maxRes)

        return maxRes
            
nums = [5]
k = 1

s = Solution()
print(s.findMaxAverage(nums,k))