from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        res = [1] * len(nums)
        res2 = [1] * len(nums)
        
        for i in range(0,len(nums)-1):
            res[i+1] = nums[i] * res[i]

        for j in range(len(nums)-1,0,-1):
            res2[j-1] = nums[j] * res2[j]

        for k in range(0,len(nums)):
            answer.append(res[k]*res2[k])

        return answer

s = Solution()

nums = [1,2,3,4]
# [1,1,2,6]
# [24,12,4,1]

# res[0] = res[0] 1
# res[1] = nums[0] * res[0] 1
# res[2] = nums[1] * res[1] 2
# res[3] = nums[2] * res[2] 6

# res[3] = res[3] 1
# res[2] = nums[3] * res[3] 4
# res[1] = nums[2] * res[2] 12
# res[0] = nums[1] * res[1] 

print(s.productExceptSelf(nums))