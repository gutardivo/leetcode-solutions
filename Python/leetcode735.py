from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while a < 0 and stack and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)

        return stack
    
s = Solution()

asteroids1 = [5,10,-5]
asteroids2 = [8,-8]
asteroids3 = [10,2,-5]

print(s.asteroidCollision(asteroids1))
print(s.asteroidCollision(asteroids2))
print(s.asteroidCollision(asteroids3))