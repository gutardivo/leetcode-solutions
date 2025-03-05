from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_operations = 0
        left, right = 0, len(nums) - 1

        nums.sort()  # Ordenação O(n log n)

        while right > left:
            sum_ = nums[left] + nums[right]

            if sum_ == k:
                max_operations += 1
                left += 1  # Move o ponteiro esquerdo
                right -= 1  # Move o ponteiro direito
            elif sum_ < k:
                left += 1
            else:
                right -= 1

        return max_operations

# Teste
s = Solution()
print(s.maxOperations([1, 2, 3, 4], 5))  # Saída esperada: 2
