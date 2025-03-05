from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_map = {}
        visited = set()
        for n in arr:
            if n in num_map:
                num_map[n] += 1
            else: 
                num_map[n] = 1
        
        for m in num_map:
            if num_map[m] not in visited:
                visited.add(num_map[m])
            else:
                return False

        return True



s = Solution()
arr = [1,2,2,2,1,1,3]
print(s.uniqueOccurrences(arr))