from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, zero_occ = 0, 0
        while i < len(nums) - zero_occ:
            if nums[i] == 0:
                val = nums.pop(i)
                nums.append(val)
                zero_occ += 1
                i -= 1
            i += 1

        return nums

s = Solution()

nums = [0,0,1]

print(s.moveZeroes(nums))
