from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Map, nums2Map = set(nums1), set(nums2)

        res1, res2 = set(), set()

        for n in nums1:
            if n not in nums2Map:
                res1.add(n)

        for m in nums2:
            if m not in nums1Map:
                res2.add(m)
        
        return [list(res1),list(res2)]
    
s = Solution()
nums1, nums2 = [1,2,3,3], [2,4,6]
nums3, nums4 = [1,2,3,3], [1,1,2,2]

print(s.findDifference(nums1,nums2))
print(s.findDifference(nums3,nums4))